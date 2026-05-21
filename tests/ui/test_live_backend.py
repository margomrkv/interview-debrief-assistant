"""LiveBackend — offline, assess_one monkeypatched (no LM).

Splitting/match/transcript delegate to the real EmulatorBackend (file replay);
only the scoring call is faked, so these exercise the live wiring without network.
"""
from __future__ import annotations

from src.ui import live_backend
from src.ui.live_backend import LiveBackend

SID = "data_scientist_junior_karpov_2022_03_30"


def _fake_assess(**scores):
    def _inner(qa, *, lm=None):
        return {**scores, "error": None, "reasoning": "because"}
    return _inner


def test_split_and_match_delegate_to_emulator() -> None:
    lb = LiveBackend()
    items = lb.split_items(SID)
    assert len(items) == 29
    assert items[0]["id"] == "q01"
    # match a real transcript back to its source_id
    assert lb.match_source(lb.transcript_text(SID)) == SID
    assert lb.match_source("totally unrelated text") is None


def test_score_item_aggregate_thresholds(monkeypatch) -> None:
    lb = LiveBackend()
    cases = [
        (dict(factual_correctness=8, focus=8, clarity=8), "strong"),   # mean 8
        (dict(factual_correctness=5, focus=5, clarity=5), "adequate"),  # mean 5
        (dict(factual_correctness=2, focus=2, clarity=2), "weak"),      # mean 2
        (dict(factual_correctness=7, focus=7, clarity=7), "strong"),    # boundary 7
        (dict(factual_correctness=4, focus=4, clarity=4), "adequate"),  # boundary 4
    ]
    for scores, expected in cases:
        monkeypatch.setattr(live_backend, "assess_one", _fake_assess(**scores))
        out = LiveBackend().score_item(SID, 0)
        assert out["scored"] is True
        assert out["aggregate"] == expected
        assert out["rationale"] == "because"
        assert out["factual_correctness"] == scores["factual_correctness"]


def test_score_item_error_is_unscored(monkeypatch) -> None:
    def boom(qa, *, lm=None):
        return {"factual_correctness": None, "focus": None, "clarity": None,
                "error": "boom", "reasoning": None}

    monkeypatch.setattr(live_backend, "assess_one", boom)
    out = LiveBackend().score_item(SID, 0)
    assert out == {"idx": 0, "scored": False}


def test_score_item_out_of_range() -> None:
    assert LiveBackend().score_item(SID, 999) == {"idx": 999, "scored": False}


def test_report_matches_rollup_of_scored(monkeypatch) -> None:
    monkeypatch.setattr(live_backend, "assess_one",
                        _fake_assess(factual_correctness=6, focus=6, clarity=6))
    lb = LiveBackend()
    for idx in range(3):
        lb.score_item(SID, idx)
    r = lb.report(SID)
    assert r["n_scored"] == 3
    assert r["n_questions"] == 29
    assert r["means"] == {"factual_correctness": 6.0, "focus": 6.0, "clarity": 6.0}
    assert r["overall"] == 6.0
    assert r["verdict"] == "HIRE"  # p_hire = round((6-1)/9*100) = 56
