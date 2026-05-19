"""Train the scoring evaluator prompt via DSPy MIPROv2.

Reads kb/splits.json + train/hard_skills.json, optimizes ScoringEvaluator,
writes all artifacts of a single run into runs/<YYYY-MM-DD_HH-MM-SS>/ (local TZ):
evaluator_prompt.md, train_report.md, logs/train.jsonl, logs/train.trace.jsonl.

See plan §"Step 4 — Train script".
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
from pathlib import Path
from typing import Any

# MUST be imported before dspy/litellm — installs warning filters at import time.
from src.common.logging_setup import configure_logging  # noqa: I001

import dspy  # noqa: E402
from dspy.teleprompt import MIPROv2  # noqa: E402

from src.common.cost_callback import (  # noqa: E402
    CostCallback,
    MIPROPhaseHandler,
    cost_breakdown_markdown,
)
from src.common.dataset import load_split_examples  # noqa: E402
from src.common.dspy_modules import (  # noqa: E402
    METRICS,
    ScoringEvaluator,
    mae_metric,
)
from src.common.eval_runner import run_evaluation  # noqa: E402
from src.common.llm_factory import (  # noqa: E402
    LABEL_MODEL_ID,
    PROMPT_MODEL_ALIASES,
    TASK_MODEL_ID,
    prompt_lm,
    resolve_prompt_model_id,
    task_lm,
)
from src.common.prompt_tracer import PromptTracer  # noqa: E402
from src.common.tracer_setup import setup_phoenix, shutdown_phoenix  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
HARD_SKILLS = REPO_ROOT / "train" / "hard_skills.json"
SPLITS = REPO_ROOT / "kb" / "splits.json"
SEED_PROMPT = REPO_ROOT / ".claude" / "skills" / "assess-interview" / "shared-evaluator-rules.md"
RUNS_DIR = REPO_ROOT / "runs"


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


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--num-trials",
        type=int,
        default=3,
        help="MIPROv2 num_trials (default 3). Higher = больше prompt-кандидатов, выше стоимость.",
    )
    p.add_argument(
        "--num-candidates",
        type=int,
        default=None,
        help=(
            "MIPROv2 num_candidates (только когда --budget не задан). "
            "Default: mirrors --num-trials. DSPy требует num_candidates+num_trials когда auto=None."
        ),
    )
    p.add_argument(
        "--prompt-model",
        default=None,
        help=(
            "MIPROv2 proposer LM alias or fully-qualified id. "
            f"Aliases: {sorted(PROMPT_MODEL_ALIASES)}. Default: sonnet."
        ),
    )
    p.add_argument(
        "--no-phoenix",
        action="store_true",
        help="Disable Phoenix UI (JSONL trace still written).",
    )
    p.add_argument(
        "--run-id",
        default=None,
        help="Override run_id (default: generated from now() in local TZ).",
    )
    p.add_argument("--log-file", type=Path, default=None, help="Mirror logs into this file (append).")
    p.add_argument("--verbose", action="store_true", help="DEBUG-level logging (e.g. cost throttle).")
    args = p.parse_args()

    logger = configure_logging("train", log_file=args.log_file, verbose=args.verbose)

    prompt_model_id = resolve_prompt_model_id(args.prompt_model)

    run_id = args.run_id or _local_run_id()
    run_dir = RUNS_DIR / run_id
    (run_dir / "logs").mkdir(parents=True, exist_ok=True)
    prompt_path = run_dir / "evaluator_prompt.md"
    report_path = run_dir / "train_report.md"
    jsonl_path = run_dir / "logs" / "train.jsonl"
    trace_jsonl_path = run_dir / "logs" / "train.trace.jsonl"

    train, test, splits_meta = load_split_examples(HARD_SKILLS, SPLITS)
    seed_prompt = 'Оцени ответ кандидата'

    student = ScoringEvaluator()
    student.score.predict.signature = student.score.predict.signature.with_instructions(seed_prompt)

    task = task_lm()
    prompt = prompt_lm(prompt_model_id)

    cb = CostCallback(version=run_id, jsonl_path=jsonl_path)
    tracer = PromptTracer(version=run_id, jsonl_path=trace_jsonl_path, phase_ref=cb)
    # MIPROPhaseHandler is a sniffer (not a renderer): it watches INFO records
    # on DSPy's optimizer/evaluator loggers and mutates cb.current_phase /
    # cb.parse_failures. Display formatting is now owned by configure_logging.
    phase_handler = MIPROPhaseHandler(cb)
    mipro_loggers = [
        logging.getLogger("dspy.teleprompt.mipro_optimizer_v2"),
        logging.getLogger("dspy.teleprompt.mipro_v2"),
        logging.getLogger("dspy.evaluate.evaluate"),
    ]
    for lg in mipro_loggers:
        lg.addHandler(phase_handler)

    tp = None if args.no_phoenix else setup_phoenix(project_name=f"evaluator-train-{run_id}")
    dspy.configure(lm=task, adapter=dspy.JSONAdapter(), callbacks=[cb, tracer], track_usage=True)

    try:
        logger.info(
            "compiling MIPROv2 num_trials=%d task=%s prompt=%s",
            args.num_trials, TASK_MODEL_ID, prompt_model_id,
        )
        logger.info("run dir: %s", run_dir.relative_to(REPO_ROOT))
        logger.info("cost log: %s", jsonl_path.relative_to(REPO_ROOT))
        logger.info("trace log: %s", trace_jsonl_path.relative_to(REPO_ROOT))
        if tp is not None:
            logger.info("phoenix UI: http://localhost:6006")
        logger.info(
            "metric note: 'Average Metric: X / N (Y%)' = sum of mae_metric across "
            "N examples; mae_metric = 5 - mean_abs_err per metric, range 0..5. "
            "Y% = avg * 100 (~500% perfect, ~400% current baseline)."
        )
        optimizer = MIPROv2(
            metric=mae_metric,
            prompt_model=prompt,
            task_model=task,
            auto=None,
            num_threads=2,
            num_candidates=3
        )
        compile_kwargs: dict[str, Any] = {
            "trainset": train,
            "requires_permission_to_run": False,
        }
        # DSPy MIPROv2: auto and num_trials are mutually exclusive — auto picks num_trials.
        compile_kwargs["num_trials"] = 3
        compiled = optimizer.compile(student, **compile_kwargs)

        # Production-mirror eval: run the extracted prompt through the same
        # path evaluate.py uses (fresh ScoringEvaluator, clean dspy context,
        # no JSONAdapter / track_usage / callbacks). See am-best-offer-et4.
        compiled_prompt = _extract_prompt(compiled) or seed_prompt
        logger.info("evaluating on train...")
        train_metrics = run_evaluation(compiled_prompt, train, lm=task)
        logger.info(
            "  train MAE=%.3f  acc±1=%.3f",
            train_metrics["mae"], train_metrics["accuracy_pm1"],
        )
        logger.info("evaluating on test...")
        test_metrics = run_evaluation(compiled_prompt, test, lm=task)
        logger.info(
            "  test MAE=%.3f  acc±1=%.3f  CI=[%.3f,%.3f]",
            test_metrics["mae"], test_metrics["accuracy_pm1"],
            test_metrics["ci_low"], test_metrics["ci_high"],
        )

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
            num_trials=args.num_trials,
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
        shutdown_phoenix(tp)


if __name__ == "__main__":
    main()
