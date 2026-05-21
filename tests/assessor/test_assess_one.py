"""assess_one — offline, predict_all monkeypatched (no LM)."""
from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

from src.assessor import score

QA = {
    "interviewer_question": "What is a closure?",
    "candidate_answer": "A function capturing its enclosing scope.",
    "question_topic": "Python",
    "interview_stage": "technical_qna",
}


def test_assess_one_returns_metrics_reasoning(monkeypatch) -> None:
    captured: dict = {}

    def fake_predict_all(prompt_text, examples, *, lm=None):
        captured["n"] = len(examples)
        captured["ex"] = examples[0]
        return [SimpleNamespace(factual_correctness=8, focus=7, clarity=9, reasoning="solid")]

    monkeypatch.setattr(score, "predict_all", fake_predict_all)
    out = score.assess_one(QA, prompt_path=Path("/does/not/exist"))

    assert out["factual_correctness"] == 8
    assert out["focus"] == 7
    assert out["clarity"] == 9
    assert out["reasoning"] == "solid"
    assert out["error"] is None
    assert captured["n"] == 1  # exactly one example built → one LLM call
    assert captured["ex"].interviewer_question == QA["interviewer_question"]


def test_assess_one_propagates_error(monkeypatch) -> None:
    failed = SimpleNamespace(factual_correctness=None, focus=None, clarity=None, _error="boom")
    monkeypatch.setattr(score, "predict_all", lambda *a, **k: [failed])
    out = score.assess_one(QA, prompt_path=Path("/does/not/exist"))
    assert out["error"] == "boom"
    assert out["factual_correctness"] is None
