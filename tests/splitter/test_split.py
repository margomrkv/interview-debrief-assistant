"""split_transcript — offline, the completion call injected (no network).

`complete` is a fake that returns a LiteLLM-shaped response object, so these
exercise the JSON parsing / failure handling without hitting a model.
"""
from __future__ import annotations

import json
from types import SimpleNamespace

from src.splitter.split import _detect_language, split_transcript


def _resp(content: str):
    """Mimic litellm's response.choices[0].message.content access path."""
    return SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content=content))]
    )


def _fake_complete(content: str):
    def _inner(**kwargs):
        return _resp(content)
    return _inner


ITEM = {
    "interviewer_question": {"text": "Что такое p-value?", "time": "01:00"},
    "candidate_answer": {"text": "Это вероятность...", "time": "01:05"},
    "reference_answer": {"text": None, "time": None},
    "interviewer_feedback": {"text": None, "time": None},
    "question_type": "hard",
    "question_topic": "Statistics",
    "interview_stage": "technical_qna",
}


def test_parses_items_from_json() -> None:
    payload = json.dumps({"source_id": "x", "splitter_mode": "split_only",
                          "items": [ITEM]})
    out = split_transcript("кандидат говорит много текста", "x",
                           complete=_fake_complete(payload))
    assert len(out) == 1
    assert out[0]["interviewer_question"]["text"] == "Что такое p-value?"
    assert out[0]["question_topic"] == "Statistics"


def test_parses_markdown_fenced_json() -> None:
    # Anthropic ignores response_format=json_object and wraps output in a ```json fence.
    inner = json.dumps({"source_id": "x", "items": [ITEM]})
    fenced = f"```json\n{inner}\n```"
    out = split_transcript("текст интервью", "x", complete=_fake_complete(fenced))
    assert len(out) == 1
    assert out[0]["question_topic"] == "Statistics"


def test_malformed_json_returns_empty() -> None:
    out = split_transcript("some transcript", "x",
                           complete=_fake_complete("not json {{{"))
    assert out == []


def test_missing_items_key_returns_empty() -> None:
    out = split_transcript("some transcript", "x",
                           complete=_fake_complete(json.dumps({"source_id": "x"})))
    assert out == []


def test_completion_exception_returns_empty() -> None:
    def boom(**kwargs):
        raise RuntimeError("network down")
    assert split_transcript("transcript text", "x", complete=boom) == []


def test_blank_transcript_skips_call() -> None:
    def must_not_run(**kwargs):
        raise AssertionError("should not call the model on empty transcript")
    assert split_transcript("   ", "x", complete=must_not_run) == []


def test_language_detection() -> None:
    assert _detect_language("это русский текст про модели") == "ru"
    assert _detect_language("this is an english transcript") == "en"
