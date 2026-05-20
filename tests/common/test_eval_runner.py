"""run_evaluation report numbers — offline, predict_all monkeypatched (no LM).

Verifies the headline `score` equals 1 − MAE/SCORE_RANGE for known canned
predictions, and that the dict carries the renamed score-space keys.
"""
from __future__ import annotations

from types import SimpleNamespace

from src.common import eval_runner
from src.common.dspy_modules import METRICS, SCORE_RANGE


def _example(src: str, **scores: int) -> SimpleNamespace:
    return SimpleNamespace(
        reference_score=dict(scores),
        source_id=src,
        interviewer_question="q?",
    )


def _pred(**scores: int) -> SimpleNamespace:
    return SimpleNamespace(**scores)


def test_run_evaluation_score_matches_known_mae(monkeypatch) -> None:
    refs = [
        _example("a", factual_correctness=4, focus=4, clarity=4),
        _example("b", factual_correctness=2, focus=5, clarity=3),
    ]
    preds = [
        _pred(factual_correctness=4, focus=4, clarity=3),  # err 1 on one axis
        _pred(factual_correctness=2, focus=4, clarity=3),  # err 1 on one axis
    ]
    # Each example: mean_err = 1/3 → per-example score = 1 - (1/3)/RANGE; both equal.
    expected = 1.0 - (1 / 3) / SCORE_RANGE

    monkeypatch.setattr(eval_runner, "predict_all", lambda *a, **k: preds)
    out = eval_runner.run_evaluation("prompt", refs)

    assert abs(out["score"] - expected) < 1e-9
    assert set(METRICS) == set(out["per_metric_score"])
    assert set(out["per_source_score"]) == {"a", "b"}
    assert out["fails"] == 0
    # renamed keys present, old raw-MAE keys gone
    assert "mae" not in out and "per_source_mae" not in out


def test_run_evaluation_worst_sorted_ascending(monkeypatch) -> None:
    refs = [
        _example("good", factual_correctness=4, focus=4, clarity=4),
        _example("bad", factual_correctness=5, focus=5, clarity=5),
    ]
    preds = [
        _pred(factual_correctness=4, focus=4, clarity=4),  # perfect → score 1.0
        _pred(factual_correctness=1, focus=1, clarity=1),  # large err → low score
    ]
    monkeypatch.setattr(eval_runner, "predict_all", lambda *a, **k: preds)
    out = eval_runner.run_evaluation("prompt", refs)

    worst_scores = [s for s, _ex, _pr in out["worst"]]
    assert worst_scores == sorted(worst_scores)  # lowest (worst) first
    assert out["worst"][0][1].source_id == "bad"
