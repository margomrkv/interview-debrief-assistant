"""DSPy signature + module + metrics for the scoring-prompt trainer.

Signature mirrors the fields present in train/hard_skills.json (see plan §D14).
vacancy/cv are deliberately absent — labeling policy ignores them.
"""
from __future__ import annotations

import random
from typing import Any, Sequence

import dspy

METRICS: tuple[str, str, str] = ("factual_correctness", "focus", "clarity")


class ScoreInterviewQA(dspy.Signature):
    """Evaluate one interview QA pair on three 1..5 anchored axes.

    Score policy: use signal from interviewer_feedback and/or reference_answer;
    do not infer scores from industry baseline or generic expectations.
    Output integers in 1..5.
    """

    interviewer_question: str = dspy.InputField()
    candidate_answer: str = dspy.InputField()
    reference_answer: str = dspy.InputField(desc="may be empty string")
    interviewer_feedback: str = dspy.InputField(desc="may be empty string")
    question_topic: str = dspy.InputField()
    interview_stage: str = dspy.InputField()

    factual_correctness: int = dspy.OutputField(desc="1..5 anchored")
    focus: int = dspy.OutputField(desc="1..5 anchored")
    clarity: int = dspy.OutputField(desc="1..5 anchored")


class ScoringEvaluator(dspy.Module):
    def __init__(self) -> None:
        super().__init__()
        self.score = dspy.ChainOfThought(ScoreInterviewQA)

    def forward(self, **fields: Any) -> Any:
        return self.score(**fields)


def _ref(example: Any, metric: str) -> int | None:
    """reference_score lives on Example as a dict-like; tolerate both attr and dict."""
    rs = getattr(example, "reference_score", None)
    if rs is None and isinstance(example, dict):
        rs = example.get("reference_score")
    if rs is None:
        return None
    if isinstance(rs, dict):
        return rs.get(metric)
    return getattr(rs, metric, None)


def _pred(pred: Any, metric: str) -> int | None:
    val = getattr(pred, metric, None)
    if val is None:
        return None
    try:
        return int(val)
    except (TypeError, ValueError):
        return None


def mae_metric(example: Any, pred: Any, trace: Any = None) -> float:
    """MIPRO maximizes the metric — we return (5 - mean_abs_err)/5 so higher is better.

    Normalized to [0, 1]. Perfect match = 1.0. Worst case (5 vs 1) = 0.2.
    """
    errs: list[int] = []
    for m in METRICS:
        ref = _ref(example, m)
        pv = _pred(pred, m)
        if ref is None or pv is None:
            continue
        errs.append(abs(pv - ref))
    if not errs:
        return 0.0
    return (5.0 - (sum(errs) / len(errs)))/5


def mae_raw(preds: Sequence[Any], refs: Sequence[Any]) -> float:
    errs: list[int] = []
    for p, r in zip(preds, refs):
        for m in METRICS:
            ref = _ref(r, m)
            pv = _pred(p, m)
            if ref is None or pv is None:
                continue
            errs.append(abs(pv - ref))
    return sum(errs) / len(errs) if errs else 0.0


def accuracy_pm1(preds: Sequence[Any], refs: Sequence[Any]) -> float:
    hits = 0
    total = 0
    for p, r in zip(preds, refs):
        for m in METRICS:
            ref = _ref(r, m)
            pv = _pred(p, m)
            if ref is None or pv is None:
                continue
            total += 1
            hits += int(abs(pv - ref) <= 1)
    return hits / total if total else 0.0


def bootstrap_ci_95(
    preds: Sequence[Any],
    refs: Sequence[Any],
    n: int = 1000,
    seed: int = 42,
) -> tuple[float, float, float]:
    """Returns (median_mae, ci_low_2.5%, ci_high_97.5%)."""
    rng = random.Random(seed)
    paired = list(zip(preds, refs))
    if not paired:
        return 0.0, 0.0, 0.0
    samples: list[float] = []
    for _ in range(n):
        bootstrap = [rng.choice(paired) for _ in range(len(paired))]
        ps, rs = zip(*bootstrap)
        samples.append(mae_raw(ps, rs))
    samples.sort()
    return samples[n // 2], samples[int(n * 0.025)], samples[int(n * 0.975)]
