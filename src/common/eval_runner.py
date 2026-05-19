"""Production-mirror evaluation runner shared by train.py and evaluate.py.

Both the post-MIPRO full-eval in `train.py` and the standalone `evaluate.py`
construct a fresh `ScoringEvaluator` with the prompt as signature instructions
and run predictions under a clean dspy context — no train-time `JSONAdapter`,
no `track_usage`, no `callbacks`. This guarantees train_report.md and
eval_<split>.md report identical numbers on the same artifact (am-best-offer-et4).
"""
from __future__ import annotations

import logging
from collections import defaultdict
from typing import Any

import dspy

from src.common.dataset import INPUT_FIELDS
from src.common.dspy_modules import (
    METRICS,
    ScoringEvaluator,
    accuracy_pm1,
    bootstrap_ci_95,
    mae_raw,
)
from src.common.llm_factory import task_lm

logger = logging.getLogger(__name__)


def _predict_one(student: dspy.Module, ex: dspy.Example) -> Any:
    try:
        return student(**{k: getattr(ex, k) for k in INPUT_FIELDS})
    except Exception as e:
        logger.warning(
            "predict failed for source=%s: %s",
            getattr(ex, "source_id", "?"),
            e,
            exc_info=True,
        )
        return type("FailedPred", (), {m: None for m in METRICS} | {"_error": repr(e)})()


def predict_all(
    prompt_text: str,
    examples: list[dspy.Example],
    *,
    lm: dspy.LM | None = None,
) -> list[Any]:
    """Run `prompt_text` over `examples` in a production-mirror dspy context.

    Isolates from any caller-set `dspy.settings` (JSONAdapter, track_usage,
    callbacks) so the result equals what the prompt will produce in deployment.
    Returns predictions only (no aggregation, no reference_score required).
    Failures are returned as objects with `_error` set and METRICS attrs as None.
    """
    student = ScoringEvaluator()
    student.score.predict.signature = student.score.predict.signature.with_instructions(prompt_text)

    with dspy.context(
        lm=(lm or task_lm()),
        adapter=dspy.ChatAdapter(),
        callbacks=[],
        track_usage=False,
    ):
        return [_predict_one(student, ex) for ex in examples]


def run_evaluation(
    prompt_text: str,
    examples: list[dspy.Example],
    *,
    lm: dspy.LM | None = None,
) -> dict[str, Any]:
    """Evaluate `prompt_text` on `examples` against their reference_score.

    Thin wrapper over `predict_all` that aggregates MAE / accuracy±1 / bootstrap
    CI / per-source-id / per-metric / worst cases. Examples MUST carry a
    `reference_score` dict.
    """
    preds = predict_all(prompt_text, examples, lm=lm)

    fails = sum(1 for p in preds if getattr(p, "_error", None))
    mae = mae_raw(preds, examples)
    acc = accuracy_pm1(preds, examples)
    med, lo, hi = bootstrap_ci_95(preds, examples)

    per_source_errs: dict[str, list[int]] = defaultdict(list)
    per_metric_errs: dict[str, list[int]] = defaultdict(list)
    for pr, ex in zip(preds, examples):
        if getattr(pr, "_error", None):
            continue
        for m in METRICS:
            ref = ex.reference_score.get(m)
            pv = getattr(pr, m, None)
            if ref is None or pv is None:
                continue
            try:
                err = abs(int(pv) - ref)
                per_source_errs[ex.source_id].append(err)
                per_metric_errs[m].append(err)
            except (TypeError, ValueError):
                pass
    per_source_mae = {src: sum(es) / len(es) for src, es in per_source_errs.items() if es}
    per_source_n = {src: len(es) for src, es in per_source_errs.items() if es}
    per_metric_mae = {
        m: (sum(per_metric_errs[m]) / len(per_metric_errs[m]) if per_metric_errs.get(m) else 0.0)
        for m in METRICS
    }

    worst: list[tuple[float, dspy.Example, Any]] = []
    for pr, ex in zip(preds, examples):
        if getattr(pr, "_error", None):
            continue
        errs: list[int] = []
        for m in METRICS:
            ref = ex.reference_score.get(m)
            pv = getattr(pr, m, None)
            if ref is None or pv is None:
                continue
            try:
                errs.append(abs(int(pv) - ref))
            except (TypeError, ValueError):
                pass
        if errs:
            worst.append((sum(errs) / len(errs), ex, pr))
    worst.sort(key=lambda t: -t[0])

    return {
        "fails": fails,
        "mae": mae,
        "accuracy_pm1": acc,
        "ci_median": med,
        "ci_low": lo,
        "ci_high": hi,
        "per_source_mae": per_source_mae,
        "per_source_n": per_source_n,
        "per_metric_mae": per_metric_mae,
        "worst": worst[:20],
    }
