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
    mae_metric,
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
