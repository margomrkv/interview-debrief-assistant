"""Train the scoring evaluator prompt via DSPy MIPROv2 and write a full run.

`run_kb_pipeline` is the single in-process pipeline that powers `scripts/kb.py`:
  1. build_splits → kb/splits.json
  2. MIPROv2 compile on the train split (writes evaluator_prompt.md, train_report.md, logs/*)
  3. evaluate(prompt) on the requested split(s) (writes eval_<split>.md)

All artifacts of a single run live in `runs/<run_id>/` (default run_id = local TZ
timestamp). No argparse / subprocess: callers either invoke from a CLI wrapper
(see `scripts/kb.py`) or import and call `run_kb_pipeline(...)` directly.
"""
from __future__ import annotations

import datetime as dt
import json
import logging
from pathlib import Path
from typing import Any, Literal

import dspy
from dspy.teleprompt import MIPROv2

from src.common.cost_callback import (
    CostCallback,
    MIPROPhaseHandler,
    cost_breakdown_markdown,
)
from src.common.dataset import load_split_examples
from src.common.dspy_modules import (
    METRICS,
    SCORE_RANGE,
    ScoringEvaluator,
    mae_metric,
)
from src.common.eval_runner import run_evaluation
from src.common.llm_factory import (
    LABEL_MODEL_ID,
    TASK_MODEL_ID,
    prompt_lm,
    resolve_prompt_model_id,
    task_lm,
)
from src.common.logging_setup import configure_logging, phase_banner
from src.common.prompt_tracer import PromptTracer
from src.common.score_logger import ScoreLogger, make_logged_metric
from src.common.tracer_setup import setup_phoenix, shutdown_phoenix
from src.kb.build_splits import (
    DEFAULT_INPUT as DEFAULT_CORPUS,
    DEFAULT_OUTPUT as DEFAULT_SPLITS,
    build_splits,
    log_split_summary,
)

NUM_TRIALS = 100
NUM_CANDIDATES = 15
MINIBATCH_SIZE = 20
MAX_LABELED_DEMOS = 4
MAX_BOOTSTRAPPED_DEMOS = 4


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RUNS_DIR = REPO_ROOT / "runs"

EvalSplits = Literal["test", "train", "both", "none"]


def default_run_id() -> str:
    """Local-TZ timestamp used as the default `run_id` for a kb pipeline run."""
    return dt.datetime.now().astimezone().strftime("%Y-%m-%d_%H-%M-%S")


def _first_predictor(program: dspy.Module | None) -> Any | None:
    """The first named predictor of a (candidate) program, or None."""
    if program is None:
        return None
    for _name, p in program.named_predictors():
        return p
    return None


def _candidate_instruction(program: dspy.Module | None) -> str:
    """The instruction text on a candidate program's (first) predictor."""
    p = _first_predictor(program)
    return (getattr(getattr(p, "signature", None), "instructions", "") or "") if p else ""


def _candidate_demos(program: dspy.Module | None) -> int:
    """Number of few-shot demos on a candidate program's (first) predictor."""
    p = _first_predictor(program)
    return len(getattr(p, "demos", []) or []) if p else 0


def _demo_label(demo: Any) -> str:
    """One-line `source_id: question…` label for a few-shot demo."""
    d = demo.toDict() if hasattr(demo, "toDict") else dict(demo)
    q = d.get("interviewer_question", "")
    if isinstance(q, dict):
        q = q.get("text", "")
    src = d.get("source_id", "?")
    return f"{src}: {str(q).strip()[:70]}"


def _candidate_sort_key(cp: Any) -> tuple[float, int]:
    """Rank candidate_programs by (score, demo_count).

    The demo_count is the tie-breaker: MIPROv2 routinely produces a bare
    baseline (0 demos) and a demo-bearing candidate that score *identically*
    (am-best-offer-7xc — both full-eval at 432.59). The baseline is added first,
    so a plain `max(...)` would pick it and drop the demos. Preferring more demos
    on ties surfaces the richer prompt without ever overriding a strictly better
    score.
    """
    score = cp.get("score") if isinstance(cp, dict) and cp.get("score") is not None else float("-inf")
    program = cp.get("program") if isinstance(cp, dict) else None
    return (score, _candidate_demos(program))


def _extract_prompt(student: dspy.Module) -> str:
    # The canonical MIPROv2 winner lives in student.candidate_programs (list of
    # {"program": Module, "score": float}). On this ScoringEvaluator the attribute
    # `score` collides with MIPROv2's internal scoring and gets overwritten by a
    # float on the returned program, so its own named_predictors() yields nothing —
    # we read from the highest-scoring candidate instead. Falls back to `student`
    # when no candidate_programs are exposed (e.g., other optimizers).
    cps = getattr(student, "candidate_programs", None) or []
    target: dspy.Module = student
    if cps:
        best = max(cps, key=_candidate_sort_key)
        if isinstance(best, dict) and best.get("program") is not None:
            target = best["program"]
    predictor = _first_predictor(target)
    if predictor is None:
        return ""
    instr = getattr(predictor.signature, "instructions", "") or ""
    demos = getattr(predictor, "demos", []) or []
    demos_md = ""
    if demos:
        demos_md = "\n\n## Few-shot demos\n\n" + "\n\n---\n\n".join(
            json.dumps(d.toDict() if hasattr(d, "toDict") else dict(d), ensure_ascii=False, indent=2)
            for d in demos
        )
    return f"{instr}{demos_md}"


def _write_prompt_evolution(
    compiled: dspy.Module,
    run_id: str,
    out_path: Path,
    seed_prompt: str,
    proposed_order: list[str] | None = None,
) -> None:
    """Dump the full MIPROv2 search trajectory to runs/<id>/prompt_candidates.md.

    Reads MIPROv2's own bookkeeping off the compiled program (track_stats=True):
      - candidate_programs    — full-eval programs, the pool _extract_prompt picks from
      - mb_candidate_programs  — minibatch trials (cheap probes, not full-eval)
      - trial_logs            — per-trial chosen (instruction_idx, demoset_idx, score)
    Each entry is {"score", "program", "full_eval"}; instruction + demos live on the
    program's predictor. Instructions are numbered I0…In in MIPROv2's *proposal*
    order (`proposed_order`, captured during the propose phase) so the index matches
    `trial_logs`' instruction indices; anything not seen there is appended. We mark
    the row _extract_prompt selects.
    """
    full = list(getattr(compiled, "candidate_programs", None) or [])
    mb = list(getattr(compiled, "mb_candidate_programs", None) or [])
    trial_logs = getattr(compiled, "trial_logs", None) or {}
    winner = max(full, key=_candidate_sort_key) if full else None

    # I-index = proposal order (MIPROv2's instruction_candidates index), seeded from
    # the propose-phase capture so it lines up with trial_logs. Texts that never
    # appeared there (edge case) are appended in first-seen order.
    instr_ids: dict[str, int] = {}
    for text in (proposed_order or []):
        instr_ids.setdefault(text.strip(), len(instr_ids))

    def _iid(program: dspy.Module | None) -> int:
        text = _candidate_instruction(program).strip()
        if text not in instr_ids:
            instr_ids[text] = len(instr_ids)
        return instr_ids[text]

    def _rows(pool: list[Any]) -> list[dict[str, Any]]:
        out = []
        for cp in pool:
            prog = cp.get("program") if isinstance(cp, dict) else None
            out.append({
                "score": cp.get("score") if isinstance(cp, dict) else None,
                "iid": _iid(prog),
                "ndemos": _candidate_demos(prog),
                "is_winner": cp is winner,
            })
        return out

    full_rows = _rows(full)
    mb_rows = _rows(mb)

    def _fmt_score(s: Any) -> str:
        return f"{s:.2f}" if isinstance(s, (int, float)) else str(s)

    lines = [
        f"# Prompt evolution — {run_id}",
        "",
        "Полная траектория поиска MIPROv2: какие инструкции/демо рассмотрены и что",
        "набрали. Победитель = строка с ★ (выбор `_extract_prompt` по score, затем",
        "числу demos). Score = сумма `mae_metric` по valset (выше — лучше, ~N идеал, где N = размер valset).",
        "Eval-репорты показывают тот же метрик усреднённым: `score_metric` = score/N ∈ [0,1].",
        "",
        "## Победитель",
        "",
    ]
    if winner is not None:
        wprog = winner.get("program")
        lines += [
            f"- score: **{_fmt_score(winner.get('score'))}**",
            f"- инструкция: **I{instr_ids.get(_candidate_instruction(wprog).strip(), '?')}** (см. ниже)",
            f"- few-shot demos: **{_candidate_demos(wprog)}**",
            "",
        ]
    else:
        lines += ["- нет candidate_programs (track_stats off?)", ""]

    lines += ["## Инструкции-кандидаты", ""]
    for text, i in sorted(instr_ids.items(), key=lambda kv: kv[1]):
        seed_tag = " — = seed" if text.strip() == seed_prompt.strip() else ""
        lines += [f"### I{i}{seed_tag}", "", "```", text or "<пусто>", "```", ""]

    lines += [
        "## Full-eval кандидаты (ранжированы)",
        "",
        "| rank | score | instr | demos | win |",
        "|---|---|---|---|---|",
    ]
    for rank, r in enumerate(
        sorted(full_rows, key=lambda r: ((r["score"] if r["score"] is not None else -1e9), r["ndemos"]), reverse=True),
        1,
    ):
        lines.append(
            f"| {rank} | {_fmt_score(r['score'])} | I{r['iid']} | {r['ndemos']} | {'★' if r['is_winner'] else ''} |"
        )

    lines += [
        "",
        "## Minibatch trials (дешёвые пробы, не full-eval)",
        "",
        "| score | instr | demos |",
        "|---|---|---|",
    ]
    for r in sorted(mb_rows, key=lambda r: (r["score"] if r["score"] is not None else -1e9), reverse=True):
        lines.append(f"| {_fmt_score(r['score'])} | I{r['iid']} | {r['ndemos']} |")

    # Per-trial parameters straight from MIPROv2's trial_logs: which instruction
    # (proposal-order I-index) and which demoset (Few-Shot Set index) each trial
    # used. Lets you join train.scores.csv rows (tagged demoset/instruction) back
    # to the trajectory. Predictor 0 only (single-predictor ScoringEvaluator).
    if trial_logs:
        lines += [
            "",
            "## Параметры по трайлам (из trial_logs)",
            "",
            "instr — индекс инструкции в порядке предложения (= I-индекс выше); "
            "demoset — индекс few-shot set; те же значения тэгируют строки train.scores.csv.",
            "",
            "| trial | instr | demoset | full_eval_score |",
            "|---|---|---|---|",
        ]
        for tnum in sorted(trial_logs.keys(), key=lambda k: (isinstance(k, str), k)):
            tl = trial_logs[tnum] or {}
            instr_idx = tl.get("0_predictor_instruction", "-")
            demoset_idx = tl.get("0_predictor_demos", "-")
            instr_cell = f"I{instr_idx}" if isinstance(instr_idx, int) else str(instr_idx)
            fe_score = tl.get("full_eval_score")
            lines.append(
                f"| {tnum} | {instr_cell} | {demoset_idx} | "
                f"{_fmt_score(fe_score) if fe_score is not None else '-'} |"
            )

    if winner is not None:
        wdemos = getattr(_first_predictor(winner.get("program")), "demos", []) or []
        lines += ["", "## Демо победителя", ""]
        if wdemos:
            for d in wdemos:
                lines.append(f"- {_demo_label(d)}")
        else:
            lines.append("- (победитель без few-shot demos)")

    out_path.write_text("\n".join(lines) + "\n")
    logging.getLogger("train").info("wrote %s", out_path.relative_to(REPO_ROOT))


def _write_artifacts(
    student: dspy.Module,
    run_id: str,
    prompt_path: Path,
    report_path: Path,
    train_metrics: dict[str, Any],
    test_metrics: dict[str, Any],
    splits_meta: dict[str, Any],
    seed_prompt: str,
    num_trials: int,
    prompt_model_id: str,
    cost_summary: dict[str, Any] | None = None,
    trace_jsonl_path: Path | None = None,
) -> None:
    fm = {
        "run_id": run_id,
        "trained_at": dt.date.today().isoformat(),
        "task_model": TASK_MODEL_ID,
        "prompt_model": prompt_model_id,
        "labeler": f"{LABEL_MODEL_ID} (pre-existing, not invoked in this run)",
        "golden_source": "data/knowledgebase/train/hard_skills.json",
        "golden_coverage": f"{splits_meta['stats']['train'] + splits_meta['stats']['test']}/{splits_meta['stats']['train'] + splits_meta['stats']['test'] + splits_meta['stats']['excluded_unscored']}",
        "split_strategy": splits_meta["strategy"],
        "smoke": splits_meta.get("smoke", False),
        "num_trials": num_trials,
        "train_score": round(train_metrics["score"], 3),
        "test_score": round(test_metrics["score"], 3),
        "test_score_ci_95": [round(test_metrics["ci_low"], 3), round(test_metrics["ci_high"], 3)],
        "accuracy_pm1": round(test_metrics["accuracy_pm1"], 3),
        "test_failures": test_metrics["fails"],
    }
    if cost_summary is not None:
        fm["total_spend_usd"] = round(cost_summary["total_spend"], 4)
        fm["total_tokens"] = cost_summary["total_in"] + cost_summary["total_out"]
        fm["total_lm_calls"] = cost_summary["total_calls"]
    fm_lines = ["---"] + [f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in fm.items()] + ["---", ""]

    prompt_body = _extract_prompt(student) or seed_prompt
    prompt_path.write_text("\n".join(fm_lines) + prompt_body + "\n")

    lines = [
        f"# Train report — {run_id}",
        "",
        f"- Trained at: {fm['trained_at']}",
        f"- Task model: `{TASK_MODEL_ID}`",
        f"- Prompt model: `{prompt_model_id}`",
        f"- Labeler (pre-existing): `{LABEL_MODEL_ID}`",
        f"- Split: {splits_meta['stats']['train']} train / {splits_meta['stats']['test']} test (excluded {splits_meta['stats']['excluded_unscored']} unscored)",
        f"- Smoke: {splits_meta.get('smoke', False)}",
        f"- num_trials: {num_trials}",
        "",
        "## Aggregate metrics",
        "",
        "score = 1 − MAE/SCORE_RANGE, [0,1] higher=better (same metric MIPROv2 maximizes).",
        "",
        f"- train score: **{fm['train_score']}**",
        f"- test score: **{fm['test_score']}** (95% CI: [{fm['test_score_ci_95'][0]}, {fm['test_score_ci_95'][1]}])",
        f"- accuracy ±1: **{fm['accuracy_pm1']}**",
        f"- test failures: {test_metrics['fails']}",
        "",
        "## Test score per source_id",
        "",
        "| source_id | score |",
        "|---|---|",
    ]
    for src, m in sorted(test_metrics["per_source_score"].items(), key=lambda kv: kv[1]):
        lines.append(f"| {src} | {m:.3f} |")
    lines += ["", "## Worst 20 cases (test)", ""]
    for rank, (score, ex, p) in enumerate(test_metrics["worst"], 1):
        ref = ex.reference_score
        preds = {m: getattr(p, m, None) for m in METRICS}
        lines.append(
            f"{rank}. score={score:.2f} src={ex.source_id} "
            f"ref={ref} pred={preds} "
            f"q={ex.interviewer_question[:80]!r}"
        )
    if cost_summary is not None:
        lines += [""] + cost_breakdown_markdown(cost_summary)
    if trace_jsonl_path is not None:
        rel = trace_jsonl_path.relative_to(REPO_ROOT)
        lines += [
            "",
            "## Trace artifacts",
            "",
            f"- Phoenix project: `evaluator-train-{run_id}` (см. http://localhost:6006 во время прогона)",
            f"- Trace JSONL: `{rel}` (не в git)",
            f"- Просмотр: `jq 'select(.phase==\"propose\")' {rel}`",
        ]
    report_path.write_text("\n".join(lines) + "\n")
    logger = logging.getLogger("train")
    logger.info("wrote %s", prompt_path.relative_to(REPO_ROOT))
    logger.info("wrote %s", report_path.relative_to(REPO_ROOT))


def _write_eval_report(
    *,
    prompt_path: Path,
    split: str,
    examples: list[dspy.Example],
    metrics: dict[str, Any],
    out_path: Path,
) -> None:
    run_label = prompt_path.parent.name
    lines = [
        f"# Eval report — {run_label} ({split})",
        "",
        f"- prompt: `{prompt_path.relative_to(REPO_ROOT)}`",
        f"- task model: `{TASK_MODEL_ID}`",
        f"- examples: {len(examples)} (failures: {metrics['fails']})",
        "",
        "## Aggregate",
        "",
        f"- score (1 − MAE/SCORE_RANGE, higher=better): **{metrics['score']:.3f}** "
        f"(95% CI: [{metrics['ci_low']:.3f}, {metrics['ci_high']:.3f}])",
        f"- accuracy ±1: **{metrics['accuracy_pm1']:.3f}**",
        "",
        "## Score per metric",
        "",
        "| metric | score |",
        "|---|---|",
    ]
    for m in METRICS:
        lines.append(f"| {m} | {metrics['per_metric_score'][m]:.3f} |")

    lines += ["", "## Score per source_id", "", "| source_id | score | n |", "|---|---|---|"]
    for src, sc in sorted(metrics["per_source_score"].items(), key=lambda kv: kv[1]):
        lines.append(f"| {src} | {sc:.3f} | {metrics['per_source_n'][src]} |")

    lines += ["", "## Worst 20 cases", ""]
    for i, (score, ex, pr) in enumerate(metrics["worst"], 1):
        ref = ex.reference_score
        pred = {m: getattr(pr, m, None) for m in METRICS}
        lines.append(
            f"{i}. score={score:.2f} src={ex.source_id} "
            f"ref={ref} pred={pred} q={ex.interviewer_question[:80]!r}"
        )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + "\n")
    logger = logging.getLogger("train")
    logger.info("wrote %s", out_path.relative_to(REPO_ROOT))


def _resolve_eval_splits(eval_splits: EvalSplits) -> list[str]:
    if eval_splits == "none":
        return []
    if eval_splits == "both":
        return ["test", "train"]
    return [eval_splits]


def run_kb_pipeline(
    *,
    prompt_model: str | None = None,
    smoke: bool = False,
    no_phoenix: bool = False,
    eval_splits: EvalSplits = "test",
    run_id: str | None = None,
    input_path: Path | None = None,
    splits_path: Path | None = None,
    runs_dir: Path | None = None,
) -> Path:
    """Build splits → MIPROv2 compile → eval(test/train) → write run artifacts.

    Returns the run directory path. All side effects are confined to:
      - `splits_path` (kb/splits.json) — overwritten by build_splits
      - `runs_dir/<run_id>/` — fresh directory with prompt, reports, logs
    """
    # Defensive: scripts/kb.py normally configures logging first (with log_file),
    # but library callers may import run_kb_pipeline directly. configure_logging
    # is idempotent — a prior call from the entry point script wins.
    logger = configure_logging("train")
    corpus = input_path or DEFAULT_CORPUS
    splits_out = splits_path or DEFAULT_SPLITS
    runs_root = runs_dir or DEFAULT_RUNS_DIR

    num_trials = NUM_TRIALS

    prompt_model_id = resolve_prompt_model_id(prompt_model)
    run_id = run_id or default_run_id()
    run_dir = runs_root / run_id
    (run_dir / "logs").mkdir(parents=True, exist_ok=True)
    prompt_path = run_dir / "evaluator_prompt.md"
    report_path = run_dir / "train_report.md"
    candidates_path = run_dir / "prompt_candidates.md"
    jsonl_path = run_dir / "logs" / "train.jsonl"
    trace_jsonl_path = run_dir / "logs" / "train.trace.jsonl"
    scores_csv_path = run_dir / "logs" / "train.scores.csv"

    # Step 1 — build splits
    phase_banner(logger, 1, 3, "build_splits")
    splits_meta = build_splits(
        input_path=corpus,
        output_path=splits_out,
        smoke=smoke,
    )
    log_split_summary(splits_meta, logger)
    logger.info("wrote %s", splits_out.relative_to(REPO_ROOT))

    # Step 2 — train (MIPROv2 compile) + write prompt/report
    phase_banner(logger, 2, 3, "train (DSPy MIPROv2)")
    train, test, _ = load_split_examples(corpus, splits_out)
    seed_prompt = "Оцени ответ кандидата (**Factual Correctness**, **Focus**, **Clarity**)"

    student = ScoringEvaluator()
    student.score.predict.signature = student.score.predict.signature.with_instructions(seed_prompt)

    task = task_lm()
    prompt = prompt_lm(prompt_model_id)

    cb = CostCallback(version=run_id, jsonl_path=jsonl_path)
    tracer = PromptTracer(version=run_id, jsonl_path=trace_jsonl_path, phase_ref=cb)
    # Per-iteration score log: one CSV row per metric call (ref vs pred), tagged
    # with cb.current_phase / cb.current_trial. Captures bootstrap + trial evals.
    score_logger = ScoreLogger(csv_path=scores_csv_path, phase_ref=cb)
    # MIPROPhaseHandler is a sniffer (not a renderer): it watches INFO records
    # on DSPy's optimizer/evaluator loggers and mutates cb.current_phase /
    # cb.parse_failures. Level/format are owned by configure_logging.
    phase_handler = MIPROPhaseHandler(cb)
    mipro_loggers = [
        logging.getLogger("dspy.teleprompt.mipro_optimizer_v2"),
        logging.getLogger("dspy.teleprompt.mipro_v2"),
        logging.getLogger("dspy.evaluate.evaluate"),
    ]
    for lg in mipro_loggers:
        lg.addHandler(phase_handler)

    tp = None if no_phoenix else setup_phoenix(project_name=f"evaluator-train-{run_id}")
    dspy.configure(lm=task, adapter=dspy.JSONAdapter(), callbacks=[cb, tracer], track_usage=True)

    cached_metrics: dict[str, dict[str, Any]] = {}
    try:
        logger.info(
            "compiling MIPROv2 num_trials=%d task=%s prompt=%s",
            num_trials, TASK_MODEL_ID, prompt_model_id,
        )
        logger.info("run dir: %s", run_dir.relative_to(REPO_ROOT))
        logger.info("cost log: %s", jsonl_path.relative_to(REPO_ROOT))
        logger.info("trace log: %s", trace_jsonl_path.relative_to(REPO_ROOT))
        logger.info("scores log: %s", scores_csv_path.relative_to(REPO_ROOT))
        if tp is not None:
            logger.info("phoenix UI: http://localhost:6006")
        logger.info(
            "metric note: 'Average Metric: X / N (Y%)' = sum of mae_metric across "
            "N examples; mae_metric = 1 - mean_abs_err/SCORE_RANGE, range 0..1. "
            "Y% = avg * 100 (~100% perfect, ~80% current baseline; "
            "full-eval sum X tops out at N, not 5*N). Eval reports show the SAME "
            "metric averaged (score_metric = X/N), so 'test score' is comparable "
            "to the winner's Average Metric."
        )
        # demo-фильтр MIPROv2: оставляем кандидатов с mean abs err <= этого (в баллах).
        # threshold выражен в error-space, чтобы пережить смену шкалы (см. SCORE_RANGE).
        THRESHOLD_MAX_MEAN_ERR = 0.34
        optimizer = MIPROv2(
            metric=make_logged_metric(mae_metric, score_logger),
            prompt_model=prompt,
            task_model=task,
            auto=None,
            num_threads=2,
            num_candidates=NUM_CANDIDATES,
            metric_threshold=1.0 - THRESHOLD_MAX_MEAN_ERR / SCORE_RANGE,  # = 0.915 на шкале 1..5
        )

        # Real-time demoset/instruction tagging for train.scores.csv: MIPROv2 picks
        # the (instruction, demoset) combo for a trial inside this method *before*
        # evaluating it (the indices only hit the logs *after* eval, too late to
        # sniff). We wrap the bound method so the indices land on `cb` before the
        # metric calls fire — bootstrap and the baseline full-eval bypass it and
        # keep "-". Instance attribute shadows the class method.
        _orig_select = optimizer._select_and_insert_instructions_and_demos

        def _select_traced(*a: Any, **kw: Any) -> Any:
            chosen, raw = _orig_select(*a, **kw)
            cb.current_demoset = str(raw.get("0_predictor_demos", "-"))
            cb.current_instruction = str(raw.get("0_predictor_instruction", "-"))
            return chosen, raw

        optimizer._select_and_insert_instructions_and_demos = _select_traced

        compiled = optimizer.compile(
            student,
            trainset=train,
            num_trials=num_trials,
            minibatch_size=MINIBATCH_SIZE,
            max_labeled_demos=MAX_LABELED_DEMOS,
            max_bootstrapped_demos=MAX_BOOTSTRAPPED_DEMOS,
        )

        # Prompt-evolution log: dump every instruction/demo candidate MIPROv2
        # considered + their scores (am-best-offer-udt). Reads compiled's own
        # bookkeeping — no re-parsing of pipeline.log.
        _write_prompt_evolution(compiled, run_id, candidates_path, seed_prompt, cb.proposed_instructions)

        # Production-mirror eval: run the extracted prompt through the same
        # path `predict_all` uses (fresh ScoringEvaluator, clean dspy context,
        # no JSONAdapter / track_usage / callbacks). See am-best-offer-et4.
        compiled_prompt = _extract_prompt(compiled) or seed_prompt
        logger.info("evaluating on train...")
        train_metrics = run_evaluation(compiled_prompt, train, lm=task)
        logger.info(
            "  train score=%.3f  acc±1=%.3f",
            train_metrics["score"], train_metrics["accuracy_pm1"],
        )
        logger.info("evaluating on test...")
        test_metrics = run_evaluation(compiled_prompt, test, lm=task)
        logger.info(
            "  test score=%.3f  acc±1=%.3f  CI=[%.3f,%.3f]",
            test_metrics["score"], test_metrics["accuracy_pm1"],
            test_metrics["ci_low"], test_metrics["ci_high"],
        )
        cached_metrics["train"] = train_metrics
        cached_metrics["test"] = test_metrics

        cost_summary = cb.render_summary()
        _write_artifacts(
            compiled,
            run_id=run_id,
            prompt_path=prompt_path,
            report_path=report_path,
            train_metrics=train_metrics,
            test_metrics=test_metrics,
            splits_meta=splits_meta,
            seed_prompt=seed_prompt,
            num_trials=num_trials,
            prompt_model_id=prompt_model_id,
            cost_summary=cost_summary,
            trace_jsonl_path=trace_jsonl_path,
        )
        logger.info(
            "cost: $%.4f  calls=%d  tokens=%s",
            cost_summary["total_spend"],
            cost_summary["total_calls"],
            f"{cost_summary['total_in'] + cost_summary['total_out']:,}",
        )
    finally:
        for lg in mipro_loggers:
            lg.removeHandler(phase_handler)
        cb.close()
        tracer.close()
        score_logger.close()
        shutdown_phoenix(tp)

    # Step 3 — eval reports per requested split (reuse train/test metrics from
    # the post-compile production-mirror eval — identical to what evaluate.py
    # used to compute, just without spawning a subprocess).
    resolved_eval = _resolve_eval_splits(eval_splits)
    if resolved_eval:
        phase_banner(logger, 3, 3, "evaluate (eval reports)")
    for split in resolved_eval:
        examples = train if split == "train" else test
        metrics = cached_metrics[split]
        out = run_dir / f"eval_{split}.md"
        _write_eval_report(
            prompt_path=prompt_path,
            split=split,
            examples=examples,
            metrics=metrics,
            out_path=out,
        )
        logger.info(
            "  %s: score=%.3f  acc±1=%.3f  failures=%d  → %s",
            split, metrics["score"], metrics["accuracy_pm1"],
            metrics["fails"], out.relative_to(REPO_ROOT),
        )

    return run_dir
