"""DSPy signature + module + metrics for the scoring-prompt trainer.

Signature mirrors the fields present in train/hard_skills.json (see plan §D14).
vacancy/cv are deliberately absent — labeling policy ignores them.
"""
from __future__ import annotations

import random
from typing import Any, Sequence

import dspy

METRICS: tuple[str, str, str] = ("factual_correctness", "focus", "clarity")

# Single source of truth for the scoring scale. To switch to 1..10 later, edit
# SCORE_MAX here — mae_metric normalization, field descs and accuracy_pm1 all
# derive from these (data relabeling + prompt regen are a separate migration).
SCORE_MIN: int = 1
SCORE_MAX: int = 10
SCORE_RANGE: int = SCORE_MAX - SCORE_MIN   # max possible abs error per axis = 4
TOLERANCE_PM1: int = 1                      # "near miss" band for accuracy_pm1, in points


class ScoreInterviewQA(dspy.Signature):
    """Evaluate one interview QA pair on three 1..10 anchored axes (blind mode).

    Score policy: judge candidate_answer against interviewer_question using your
    own domain knowledge — there is no reference answer or interviewer feedback.
    Calibrate expectations to the interview_stage and question_topic in context.
    Output integers in 1..10.
    """

    interviewer_question: str = dspy.InputField()
    candidate_answer: str = dspy.InputField()
    question_topic: str = dspy.InputField()
    interview_stage: str = dspy.InputField()

    factual_correctness: int = dspy.OutputField(desc=f"{SCORE_MIN}..{SCORE_MAX} anchored")
    focus: int = dspy.OutputField(desc=f"{SCORE_MIN}..{SCORE_MAX} anchored")
    clarity: int = dspy.OutputField(desc=f"{SCORE_MIN}..{SCORE_MAX} anchored")


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


def _example_errs(example: Any, pred: Any) -> list[int]:
    """Abs errors for one example's valid axes (skips axes where ref/pred is None)."""
    errs: list[int] = []
    for m in METRICS:
        ref = _ref(example, m)
        pv = _pred(pred, m)
        if ref is None or pv is None:
            continue
        errs.append(abs(pv - ref))
    return errs


def mae_metric(example: Any, pred: Any, trace: Any = None) -> float:
    """MIPRO maximizes the metric — we return 1 - mean_abs_err/SCORE_RANGE so higher is better.

    Normalized to [0, 1]. Perfect match = 1.0. Worst case (SCORE_MAX vs SCORE_MIN) = 0.0.
    """
    errs = _example_errs(example, pred)
    if not errs:
        return 0.0
    return 1.0 - (sum(errs) / len(errs)) / SCORE_RANGE


def score_metric(preds: Sequence[Any], refs: Sequence[Any]) -> float:
    """Batch aggregate of the train metric: mean over examples of mae_metric.

    Equals MIPROv2's "Average Metric / N" by construction — the single [0, 1]
    higher-is-better number used in eval reports. Examples with no valid axis
    are skipped (not counted as 0.0).
    """
    vals = [mae_metric(r, p) for p, r in zip(preds, refs) if _example_errs(r, p)]
    return sum(vals) / len(vals) if vals else 0.0


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
            hits += int(abs(pv - ref) <= TOLERANCE_PM1)
    return hits / total if total else 0.0


def bootstrap_ci_95(
    preds: Sequence[Any],
    refs: Sequence[Any],
    n: int = 1000,
    seed: int = 42,
) -> tuple[float, float, float]:
    """Bootstrap CI on score_metric (the train metric). Returns (median, lo_2.5%, hi_97.5%).

    Score-space [0, 1], higher = better — so `lo` is the pessimistic bound.
    """
    rng = random.Random(seed)
    paired = list(zip(preds, refs))
    if not paired:
        return 0.0, 0.0, 0.0
    samples: list[float] = []
    for _ in range(n):
        bootstrap = [rng.choice(paired) for _ in range(len(paired))]
        ps, rs = zip(*bootstrap)
        samples.append(score_metric(ps, rs))
    samples.sort()
    return samples[n // 2], samples[int(n * 0.025)], samples[int(n * 0.975)]
