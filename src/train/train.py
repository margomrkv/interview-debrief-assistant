"""Train the scoring evaluator prompt via DSPy MIPROv2.

Reads kb/splits.json + train/hard_skills.json, optimizes ScoringEvaluator,
writes kb/evaluator_prompt_<version>.md and kb/reports/train_<version>_report.md.

See plan §"Step 4 — Train script".
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
from collections import defaultdict
from pathlib import Path
from typing import Any

import dspy
from dspy.teleprompt import MIPROv2

from src.train.cost_callback import (
    CostCallback,
    MIPROPhaseHandler,
    cost_breakdown_markdown,
)
from src.train.dspy_modules import (
    METRICS,
    ScoringEvaluator,
    accuracy_pm1,
    bootstrap_ci_95,
    mae_metric,
    mae_raw,
)
from src.train.llm_factory import (
    LABEL_MODEL_ID,
    PROMPT_MODEL_ID,
    TASK_MODEL_ID,
    prompt_lm,
    task_lm,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
HARD_SKILLS = REPO_ROOT / "train" / "hard_skills.json"
SPLITS = REPO_ROOT / "kb" / "splits.json"
SEED_PROMPT = REPO_ROOT / ".claude" / "skills" / "assess-interview" / "shared-evaluator-rules.md"
PROMPT_OUT_TPL = REPO_ROOT / "kb" / "evaluator_prompt_{version}.md"
REPORT_OUT_TPL = REPO_ROOT / "kb" / "reports" / "train_{version}_report.md"
JSONL_OUT_TPL = REPO_ROOT / "logs" / "train_{version}.jsonl"

INPUT_FIELDS = (
    "interviewer_question",
    "candidate_answer",
    "reference_answer",
    "interviewer_feedback",
    "question_topic",
    "interview_stage",
)


def _text(field: Any) -> str:
    if field is None:
        return ""
    if isinstance(field, dict):
        return field.get("text") or ""
    return str(field)


def _to_example(item: dict[str, Any]) -> dspy.Example:
    return dspy.Example(
        interviewer_question=_text(item["interviewer_question"]),
        candidate_answer=_text(item["candidate_answer"]),
        reference_answer=_text(item.get("reference_answer")),
        interviewer_feedback=_text(item.get("interviewer_feedback")),
        question_topic=item.get("question_topic", "") or "",
        interview_stage=item.get("interview_stage", "") or "",
        reference_score=item["reference_score"],
        source_id=item["source_id"],
    ).with_inputs(*INPUT_FIELDS)


def _load_data() -> tuple[list[dspy.Example], list[dspy.Example], dict[str, Any]]:
    raw = json.loads(HARD_SKILLS.read_text())
    items = raw["items"]
    splits = json.loads(SPLITS.read_text())
    train = [_to_example(items[i]) for i in splits["train_indices"]]
    test = [_to_example(items[i]) for i in splits["test_indices"]]
    return train, test, splits


def _predict_one(student: dspy.Module, ex: dspy.Example) -> Any:
    try:
        return student(**{k: getattr(ex, k) for k in INPUT_FIELDS})
    except Exception as e:  # parse error / API error
        return type("FailedPred", (), {m: None for m in METRICS} | {"_error": str(e)})()


def _eval(student: dspy.Module, examples: list[dspy.Example]) -> dict[str, Any]:
    preds = [_predict_one(student, ex) for ex in examples]
    fails = [i for i, p in enumerate(preds) if getattr(p, "_error", None)]
    mae = mae_raw(preds, examples)
    acc = accuracy_pm1(preds, examples)
    med, lo, hi = bootstrap_ci_95(preds, examples)

    per_source: dict[str, list[float]] = defaultdict(list)
    for p, ex in zip(preds, examples):
        if getattr(p, "_error", None):
            continue
        for m in METRICS:
            ref = ex.reference_score.get(m)
            pv = getattr(p, m, None)
            if ref is None or pv is None:
                continue
            try:
                per_source[ex.source_id].append(abs(int(pv) - ref))
            except (TypeError, ValueError):
                pass
    per_source_mae = {src: sum(es) / len(es) for src, es in per_source.items() if es}

    worst = []
    for idx, (p, ex) in enumerate(zip(preds, examples)):
        if getattr(p, "_error", None):
            continue
        errs = []
        for m in METRICS:
            ref = ex.reference_score.get(m)
            pv = getattr(p, m, None)
            if ref is None or pv is None:
                continue
            try:
                errs.append(abs(int(pv) - ref))
            except (TypeError, ValueError):
                pass
        if errs:
            worst.append((sum(errs) / len(errs), idx, ex, p))
    worst.sort(reverse=True)

    return {
        "mae": mae,
        "accuracy_pm1": acc,
        "ci_median": med,
        "ci_low": lo,
        "ci_high": hi,
        "fails": len(fails),
        "per_source_mae": per_source_mae,
        "worst": worst[:20],
    }


def _extract_prompt(student: dspy.Module) -> str:
    # Prefer student.score (the named ChainOfThought), but MIPROv2 in some DSPy versions
    # mutates that attribute on the compiled program — fall back to iterating predictors().
    predictor = None
    candidate = getattr(student, "score", None)
    if hasattr(candidate, "predict"):
        predictor = candidate
    else:
        try:
            for _name, p in student.named_predictors():
                predictor = p
                break
        except Exception:
            predictor = None
    if predictor is None:
        return ""
    sig = getattr(predictor, "signature", None) or getattr(getattr(predictor, "predict", None), "signature", None)
    instr = getattr(sig, "instructions", "") or ""
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
    version: str,
    train_metrics: dict[str, Any],
    test_metrics: dict[str, Any],
    splits_meta: dict[str, Any],
    seed_prompt: str,
    num_trials: int,
    cost_summary: dict[str, Any] | None = None,
) -> None:
    PROMPT_OUT_TPL.parent.mkdir(parents=True, exist_ok=True)
    REPORT_OUT_TPL.parent.mkdir(parents=True, exist_ok=True)
    prompt_path = Path(str(PROMPT_OUT_TPL).format(version=version))
    report_path = Path(str(REPORT_OUT_TPL).format(version=version))

    fm = {
        "version": version,
        "trained_at": dt.date.today().isoformat(),
        "task_model": TASK_MODEL_ID,
        "prompt_model": PROMPT_MODEL_ID,
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
        f"# Train report — {version}",
        "",
        f"- Trained at: {fm['trained_at']}",
        f"- Task model: `{TASK_MODEL_ID}`",
        f"- Prompt model: `{PROMPT_MODEL_ID}`",
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
    for rank, (avg_err, _idx, ex, p) in enumerate(test_metrics["worst"], 1):
        ref = ex.reference_score
        preds = {m: getattr(p, m, None) for m in METRICS}
        lines.append(
            f"{rank}. avg_err={avg_err:.2f} src={ex.source_id} "
            f"ref={ref} pred={preds} "
            f"q={ex.interviewer_question[:80]!r}"
        )
    if cost_summary is not None:
        lines += [""] + cost_breakdown_markdown(cost_summary)
    report_path.write_text("\n".join(lines) + "\n")
    print(f"wrote {prompt_path.relative_to(REPO_ROOT)}")
    print(f"wrote {report_path.relative_to(REPO_ROOT)}")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--budget", choices=["light", "medium"], default="light")
    p.add_argument("--out-version", default="v1")
    p.add_argument(
        "--num-trials",
        type=int,
        default=3,
        help="MIPROv2 num_trials (default 3). Higher = больше prompt-кандидатов, выше стоимость.",
    )
    args = p.parse_args()

    train, test, splits_meta = _load_data()
    seed_prompt = SEED_PROMPT.read_text()

    student = ScoringEvaluator()
    student.score.predict.signature = student.score.predict.signature.with_instructions(seed_prompt)

    task = task_lm()
    prompt = prompt_lm()

    jsonl_path = Path(str(JSONL_OUT_TPL).format(version=args.out_version))
    cb = CostCallback(version=args.out_version, jsonl_path=jsonl_path)
    phase_handler = MIPROPhaseHandler(cb)
    mipro_loggers = [
        logging.getLogger("dspy.teleprompt.mipro_optimizer_v2"),
        logging.getLogger("dspy.teleprompt.mipro_v2"),
        logging.getLogger("dspy.evaluate.evaluate"),
    ]
    for lg in mipro_loggers:
        lg.addHandler(phase_handler)
        lg.setLevel(logging.INFO)

    dspy.configure(lm=task, adapter=dspy.JSONAdapter(), callbacks=[cb], track_usage=True)

    try:
        print(f"compiling MIPROv2 budget={args.budget} num_trials={args.num_trials} task={TASK_MODEL_ID} prompt={PROMPT_MODEL_ID}")
        print(f"cost log: {jsonl_path.relative_to(REPO_ROOT)}")
        optimizer = MIPROv2(
            metric=mae_metric,
            prompt_model=prompt,
            task_model=task,
            auto=args.budget,
            num_threads=4,
        )
        compiled = optimizer.compile(
            student,
            trainset=train,
            requires_permission_to_run=False,
            num_trials=args.num_trials,
        )

        print("evaluating on train...")
        train_metrics = _eval(compiled, train)
        print(f"  train MAE={train_metrics['mae']:.3f}  acc±1={train_metrics['accuracy_pm1']:.3f}")
        print("evaluating on test...")
        test_metrics = _eval(compiled, test)
        print(f"  test MAE={test_metrics['mae']:.3f}  acc±1={test_metrics['accuracy_pm1']:.3f}  CI=[{test_metrics['ci_low']:.3f},{test_metrics['ci_high']:.3f}]")

        cost_summary = cb.render_summary()
        _write_artifacts(
            compiled, args.out_version, train_metrics, test_metrics, splits_meta, seed_prompt,
            num_trials=args.num_trials,
            cost_summary=cost_summary,
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


if __name__ == "__main__":
    main()
