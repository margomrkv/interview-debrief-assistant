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
from src.common.prompt_tracer import PromptTracer
from src.common.tracer_setup import setup_phoenix, shutdown_phoenix
from src.kb.build_splits import (
    DEFAULT_INPUT as DEFAULT_CORPUS,
    DEFAULT_OUTPUT as DEFAULT_SPLITS,
    build_splits,
    log_split_summary,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RUNS_DIR = REPO_ROOT / "runs"

EvalSplits = Literal["test", "train", "both", "none"]


def _local_run_id() -> str:
    return dt.datetime.now().astimezone().strftime("%Y-%m-%d_%H-%M-%S")


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
        best = max(
            cps,
            key=lambda cp: (cp.get("score") if isinstance(cp, dict) and cp.get("score") is not None else float("-inf")),
        )
        if isinstance(best, dict) and best.get("program") is not None:
            target = best["program"]
    predictor = None
    for _name, p in target.named_predictors():
        predictor = p
        break
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
        "golden_source": "train/hard_skills.json",
        "golden_coverage": f"{splits_meta['stats']['train'] + splits_meta['stats']['test']}/{splits_meta['stats']['train'] + splits_meta['stats']['test'] + splits_meta['stats']['excluded_unscored']}",
        "split_strategy": splits_meta["strategy"],
        "smoke": splits_meta.get("smoke", False),
        "num_trials": num_trials,
        "train_mae": round(train_metrics["mae"], 3),
        "test_mae": round(test_metrics["mae"], 3),
        "test_mae_ci_95": [round(test_metrics["ci_low"], 3), round(test_metrics["ci_high"], 3)],
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
        f"- train MAE: **{fm['train_mae']}**",
        f"- test MAE: **{fm['test_mae']}** (95% CI: [{fm['test_mae_ci_95'][0]}, {fm['test_mae_ci_95'][1]}])",
        f"- accuracy ±1: **{fm['accuracy_pm1']}**",
        f"- test failures: {test_metrics['fails']}",
        "",
        "## Test MAE per source_id",
        "",
        "| source_id | MAE |",
        "|---|---|",
    ]
    for src, m in sorted(test_metrics["per_source_mae"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {src} | {m:.3f} |")
    lines += ["", "## Worst 20 cases (test)", ""]
    for rank, (avg_err, ex, p) in enumerate(test_metrics["worst"], 1):
        ref = ex.reference_score
        preds = {m: getattr(p, m, None) for m in METRICS}
        lines.append(
            f"{rank}. avg_err={avg_err:.2f} src={ex.source_id} "
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
        f"- MAE: **{metrics['mae']:.3f}** (95% CI: [{metrics['ci_low']:.3f}, {metrics['ci_high']:.3f}])",
        f"- accuracy ±1: **{metrics['accuracy_pm1']:.3f}**",
        "",
        "## MAE per metric",
        "",
        "| metric | MAE |",
        "|---|---|",
    ]
    for m in METRICS:
        lines.append(f"| {m} | {metrics['per_metric_mae'][m]:.3f} |")

    lines += ["", "## MAE per source_id", "", "| source_id | MAE | n |", "|---|---|---|"]
    for src, mae in sorted(metrics["per_source_mae"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {src} | {mae:.3f} | {metrics['per_source_n'][src]} |")

    lines += ["", "## Worst 20 cases", ""]
    for i, (avg_err, ex, pr) in enumerate(metrics["worst"], 1):
        ref = ex.reference_score
        pred = {m: getattr(pr, m, None) for m in METRICS}
        lines.append(
            f"{i}. avg_err={avg_err:.2f} src={ex.source_id} "
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
    num_trials: int = 3,
    num_candidates: int | None = None,
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
    logger = logging.getLogger("train")
    corpus = input_path or DEFAULT_CORPUS
    splits_out = splits_path or DEFAULT_SPLITS
    runs_root = runs_dir or DEFAULT_RUNS_DIR

    prompt_model_id = resolve_prompt_model_id(prompt_model)
    run_id = run_id or _local_run_id()
    run_dir = runs_root / run_id
    (run_dir / "logs").mkdir(parents=True, exist_ok=True)
    prompt_path = run_dir / "evaluator_prompt.md"
    report_path = run_dir / "train_report.md"
    jsonl_path = run_dir / "logs" / "train.jsonl"
    trace_jsonl_path = run_dir / "logs" / "train.trace.jsonl"

    # Step 1 — build splits
    splits_meta = build_splits(
        input_path=corpus,
        output_path=splits_out,
        smoke=smoke,
    )
    log_split_summary(splits_meta, logger)
    logger.info("wrote %s", splits_out.relative_to(REPO_ROOT))

    # Step 2 — train (MIPROv2 compile) + write prompt/report
    train, test, _ = load_split_examples(corpus, splits_out)
    seed_prompt = "Оцени ответ кандидата"

    student = ScoringEvaluator()
    student.score.predict.signature = student.score.predict.signature.with_instructions(seed_prompt)

    task = task_lm()
    prompt = prompt_lm(prompt_model_id)

    cb = CostCallback(version=run_id, jsonl_path=jsonl_path)
    tracer = PromptTracer(version=run_id, jsonl_path=trace_jsonl_path, phase_ref=cb)
    phase_handler = MIPROPhaseHandler(cb)
    mipro_loggers = [
        logging.getLogger("dspy.teleprompt.mipro_optimizer_v2"),
        logging.getLogger("dspy.teleprompt.mipro_v2"),
        logging.getLogger("dspy.evaluate.evaluate"),
    ]
    for lg in mipro_loggers:
        lg.addHandler(phase_handler)
        lg.setLevel(logging.INFO)

    tp = None if no_phoenix else setup_phoenix(project_name=f"evaluator-train-{run_id}")
    dspy.configure(lm=task, adapter=dspy.JSONAdapter(), callbacks=[cb, tracer], track_usage=True)

    cached_metrics: dict[str, dict[str, Any]] = {}
    try:
        print(f"compiling MIPROv2 num_trials={num_trials} task={TASK_MODEL_ID} prompt={prompt_model_id}")
        print(f"run dir: {run_dir.relative_to(REPO_ROOT)}")
        print(f"cost log: {jsonl_path.relative_to(REPO_ROOT)}")
        print(f"trace log: {trace_jsonl_path.relative_to(REPO_ROOT)}")
        if tp is not None:
            print("phoenix UI: http://localhost:6006")
        optimizer = MIPROv2(
            metric=mae_metric,
            prompt_model=prompt,
            task_model=task,
            auto=None,
            num_threads=2,
            num_candidates=num_candidates if num_candidates is not None else num_trials,
        )
        compiled = optimizer.compile(
            student,
            trainset=train,
            requires_permission_to_run=False,
            num_trials=num_trials,
        )

        # Production-mirror eval: run the extracted prompt through the same
        # path `predict_all` uses (fresh ScoringEvaluator, clean dspy context,
        # no JSONAdapter / track_usage / callbacks). See am-best-offer-et4.
        compiled_prompt = _extract_prompt(compiled) or seed_prompt
        print("evaluating on train...")
        train_metrics = run_evaluation(compiled_prompt, train, lm=task)
        print(f"  train MAE={train_metrics['mae']:.3f}  acc±1={train_metrics['accuracy_pm1']:.3f}")
        print("evaluating on test...")
        test_metrics = run_evaluation(compiled_prompt, test, lm=task)
        print(
            f"  test MAE={test_metrics['mae']:.3f}  acc±1={test_metrics['accuracy_pm1']:.3f}  "
            f"CI=[{test_metrics['ci_low']:.3f},{test_metrics['ci_high']:.3f}]"
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
        print(
            f"cost: ${cost_summary['total_spend']:.4f}  "
            f"calls={cost_summary['total_calls']}  "
            f"tokens={cost_summary['total_in'] + cost_summary['total_out']:,}"
        )
    finally:
        for lg in mipro_loggers:
            lg.removeHandler(phase_handler)
        cb.close()
        tracer.close()
        shutdown_phoenix(tp)

    # Step 3 — eval reports per requested split (reuse train/test metrics from
    # the post-compile production-mirror eval — identical to what evaluate.py
    # used to compute, just without spawning a subprocess).
    for split in _resolve_eval_splits(eval_splits):
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
        print(
            f"  {split}: MAE={metrics['mae']:.3f}  acc±1={metrics['accuracy_pm1']:.3f}  "
            f"failures={metrics['fails']}  → {out.relative_to(REPO_ROOT)}"
        )

    return run_dir
