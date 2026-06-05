"""LiveBackend — offline, split_transcript & assess_one monkeypatched (no LM).

The catalogue/transcript/match delegate to the real EmulatorBackend (file replay);
both LLM calls (Stage 1 splitter, Stage 2 scoring) are faked, so these exercise the
live wiring without network.
"""
from __future__ import annotations

import pytest

from src.ui import emulator, live_backend
from src.ui.live_backend import LiveBackend
from src.ui.models import Aggregate, ScoreItem, Verdict

SID = "data_scientist_middle_google_data_wrangling_interviewing_io_2020_04_28"


@pytest.fixture(autouse=True)
def _offline_split(monkeypatch):
    """Default: stub Stage-1 so score_item/report never hit the splitter LLM.

    Returns one trivial raw item per real emulator Q&A so item counts (and the
    999-out-of-range case) stay valid. Tests that care about the split mapping
    re-patch ``split_transcript`` in their own body (last setattr wins).
    """
    n = len(emulator.split_items(SID))
    raw = [{
        "interviewer_question": {"text": "q", "time": "00:00"},
        "candidate_answer": {"text": "a", "time": "00:01"},
        "question_type": "hard", "question_topic": "ML",
        "interview_stage": "technical_qna",
    } for _ in range(n)]
    monkeypatch.setattr(live_backend, "split_transcript",
                        lambda transcript_text, source_id, **kw: raw)

# Two splitter-schema items the fake split_transcript returns.
_RAW_ITEMS = [
    {
        "interviewer_question": {"text": "Расскажи о себе", "time": "00:30"},
        "candidate_answer": {"text": "Я дата-сайентист", "time": "00:35"},
        "reference_answer": {"text": None, "time": None},
        "interviewer_feedback": {"text": None, "time": None},
        "question_type": "soft",
        "question_topic": "Communication",
        "interview_stage": "fit_hr",
    },
    {
        "interviewer_question": {"text": "Что такое p-value?", "time": "05:00"},
        "candidate_answer": {"text": "Это вероятность", "time": "05:10"},
        "reference_answer": {"text": None, "time": None},
        "interviewer_feedback": {"text": None, "time": None},
        "question_type": "hard",
        "question_topic": "Statistics",
        "interview_stage": "technical_qna",
    },
]


def _fake_assess(**scores):
    def _inner(qa, *, lm=None):
        return {**scores, "error": None, "reasoning": "because"}
    return _inner


def test_split_maps_to_qa_and_caches(monkeypatch) -> None:
    calls = {"n": 0}

    def fake_split(transcript_text, source_id, **kwargs):
        calls["n"] += 1
        return _RAW_ITEMS

    monkeypatch.setattr(live_backend, "split_transcript", fake_split)
    lb = LiveBackend()
    items = lb.split_items(SID)

    assert len(items) == 2
    assert items[0].id == "q01"
    assert items[0].question == "Расскажи о себе"
    assert items[0].question_time == "00:30"
    assert items[1].answer == "Это вероятность"
    assert items[1].question_topic == "Statistics"

    # cached: re-reading the split (as the stream does per item) must not re-call.
    lb.split_items(SID)
    lb.split_items(SID)
    assert calls["n"] == 1


def test_match_delegates_to_emulator() -> None:
    lb = LiveBackend()
    assert lb.match_source(lb.transcript_text(SID)) == SID
    assert lb.match_source("totally unrelated text") is None


def test_score_item_aggregate_thresholds(monkeypatch) -> None:
    cases = [
        (dict(factual_correctness=8, focus=8, clarity=8), Aggregate.STRONG),    # mean 8
        (dict(factual_correctness=5, focus=5, clarity=5), Aggregate.ADEQUATE),  # mean 5
        (dict(factual_correctness=2, focus=2, clarity=2), Aggregate.WEAK),      # mean 2
        (dict(factual_correctness=7, focus=7, clarity=7), Aggregate.STRONG),    # boundary 7
        (dict(factual_correctness=4, focus=4, clarity=4), Aggregate.ADEQUATE),  # boundary 4
    ]
    for scores, expected in cases:
        monkeypatch.setattr(live_backend, "assess_one", _fake_assess(**scores))
        out = LiveBackend().score_item(SID, 0)
        assert out.scored is True
        assert out.aggregate == expected
        assert out.rationale == "because"
        assert out.factual_correctness == scores["factual_correctness"]


def test_score_item_error_is_unscored(monkeypatch) -> None:
    def boom(qa, *, lm=None):
        return {"factual_correctness": None, "focus": None, "clarity": None,
                "error": "boom", "reasoning": None}

    monkeypatch.setattr(live_backend, "assess_one", boom)
    out = LiveBackend().score_item(SID, 0)
    assert out == ScoreItem(idx=0, scored=False)


def test_score_item_out_of_range() -> None:
    assert LiveBackend().score_item(SID, 999) == ScoreItem(idx=999, scored=False)


def test_report_matches_rollup_of_scored(monkeypatch) -> None:
    monkeypatch.setattr(live_backend, "assess_one",
                        _fake_assess(factual_correctness=6, focus=6, clarity=6))
    lb = LiveBackend()
    for idx in range(3):
        lb.score_item(SID, idx)
    r = lb.report(SID)
    assert r.n_scored == 3
    assert r.n_questions == 29
    assert r.means == {"factual_correctness": 6.0, "focus": 6.0, "clarity": 6.0}
    assert r.overall == 6.0
    assert r.verdict == Verdict.HIRE  # p_hire = round((6-1)/9*100) = 56
