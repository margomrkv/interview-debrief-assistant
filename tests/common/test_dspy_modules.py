"""Unit tests for mae_metric normalization — offline, no LM calls.

Guards the [0, 1] range fix (am-best-offer-ch0): normalization divides by
SCORE_RANGE (max abs error), not SCORE_MAX, so a worst-case miss yields 0.0.
"""
from __future__ import annotations

from types import SimpleNamespace

from src.common.dspy_modules import (
    METRICS,
    SCORE_MAX,
    SCORE_MIN,
    SCORE_RANGE,
    bootstrap_ci_95,
    mae_metric,
    score_metric,
)


def _example(**scores: int) -> SimpleNamespace:
    return SimpleNamespace(reference_score=dict(scores))


def _pred(**scores: int) -> SimpleNamespace:
    return SimpleNamespace(**scores)


def test_perfect_match_is_one() -> None:
    ref = {m: SCORE_MAX for m in METRICS}
    assert mae_metric(_example(**ref), _pred(**ref)) == 1.0


def test_worst_case_is_zero() -> None:
    ref = {m: SCORE_MIN for m in METRICS}
    pred = {m: SCORE_MAX for m in METRICS}
    assert mae_metric(_example(**ref), _pred(**pred)) == 0.0


def test_mean_err_034_matches_threshold() -> None:
    # One axis off by ~1, others perfect → mean_err ≈ 0.34 on three axes.
    ref = _example(factual_correctness=4, focus=4, clarity=4)
    pred = _pred(factual_correctness=4, focus=4, clarity=3)  # mean_err = 1/3 ≈ 0.333
    score = mae_metric(ref, pred)
    assert abs(score - (1.0 - (1 / 3) / SCORE_RANGE)) < 1e-9
    assert 0.0 <= score <= 1.0


def test_no_overlap_returns_zero() -> None:
    assert mae_metric(_example(), _pred()) == 0.0


# --- score_metric: batch aggregate of the train metric (eval headline) ---


def test_score_metric_perfect_is_one() -> None:
    ref = {m: SCORE_MAX for m in METRICS}
    refs = [_example(**ref), _example(**ref)]
    preds = [_pred(**ref), _pred(**ref)]
    assert score_metric(preds, refs) == 1.0


def test_score_metric_worst_is_zero() -> None:
    refs = [_example(**{m: SCORE_MIN for m in METRICS})]
    preds = [_pred(**{m: SCORE_MAX for m in METRICS})]
    assert score_metric(preds, refs) == 0.0


def test_score_metric_equals_mean_of_mae_metric() -> None:
    refs = [
        _example(factual_correctness=4, focus=4, clarity=4),
        _example(factual_correctness=2, focus=5, clarity=3),
    ]
    preds = [
        _pred(factual_correctness=4, focus=4, clarity=3),
        _pred(factual_correctness=2, focus=4, clarity=1),
    ]
    expected = sum(mae_metric(r, p) for p, r in zip(preds, refs)) / len(refs)
    assert abs(score_metric(preds, refs) - expected) < 1e-9


def test_score_metric_skips_examples_without_overlap() -> None:
    # Second example has no valid axis → skipped, not counted as 0.0.
    refs = [_example(factual_correctness=4, focus=4, clarity=4), _example()]
    preds = [_pred(factual_correctness=4, focus=4, clarity=4), _pred()]
    assert score_metric(preds, refs) == 1.0


def test_score_metric_empty_is_zero() -> None:
    assert score_metric([], []) == 0.0


# --- bootstrap_ci_95: now in score-space [0, 1], higher = better ---


def test_bootstrap_ci_perfect_is_all_one() -> None:
    ref = {m: SCORE_MAX for m in METRICS}
    refs = [_example(**ref) for _ in range(10)]
    preds = [_pred(**ref) for _ in range(10)]
    med, lo, hi = bootstrap_ci_95(preds, refs, n=200)
    assert med == lo == hi == 1.0


def test_bootstrap_ci_bounds_ordered_and_in_unit_range() -> None:
    refs = [
        _example(factual_correctness=4, focus=4, clarity=4),
        _example(factual_correctness=2, focus=5, clarity=3),
        _example(factual_correctness=5, focus=1, clarity=2),
    ]
    preds = [
        _pred(factual_correctness=4, focus=3, clarity=4),
        _pred(factual_correctness=1, focus=5, clarity=3),
        _pred(factual_correctness=5, focus=2, clarity=4),
    ]
    med, lo, hi = bootstrap_ci_95(preds, refs, n=500)
    assert 0.0 <= lo <= med <= hi <= 1.0
