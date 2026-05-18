"""Unit tests for PromptTracer — offline, no LM calls."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from src.train.cost_callback import CostCallback
from src.train.prompt_tracer import PromptTracer


class _FakeLM:
    """Mimics dspy.LM: exposes .model and .history (list of entries)."""

    def __init__(self, model: str = "fake/model") -> None:
        self.model = model
        self.history: list[dict] = []


@pytest.fixture
def cost_cb(tmp_path: Path) -> CostCallback:
    return CostCallback(version="vtest", jsonl_path=tmp_path / "cost.jsonl")


@pytest.fixture
def tracer(tmp_path: Path, cost_cb: CostCallback) -> PromptTracer:
    return PromptTracer(
        version="vtest",
        jsonl_path=tmp_path / "trace.jsonl",
        phase_ref=cost_cb,
    )


def _read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line]


def test_writes_messages_and_response(tracer: PromptTracer, cost_cb: CostCallback) -> None:
    lm = _FakeLM()
    tracer.on_lm_start(call_id="c1", instance=lm, inputs={})
    lm.history.append(
        {
            "uuid": "u1",
            "model": "fake/model",
            "messages": [{"role": "user", "content": "hello"}],
            "outputs": ["world"],
            "usage": {"prompt_tokens": 5, "completion_tokens": 1},
        }
    )
    tracer.on_lm_end(call_id="c1", outputs={"response": "world"})
    tracer.close()

    rows = _read_jsonl(tracer.jsonl_path)
    assert len(rows) == 1
    row = rows[0]
    assert row["call_id"] == "c1"
    assert row["model"] == "fake/model"
    assert row["messages"] == [{"role": "user", "content": "hello"}]
    assert row["response"] == ["world"]
    assert row["usage"]["prompt_tokens"] == 5
    assert row["error"] is None
    cost_cb.close()


def test_phase_ref_propagates(tracer: PromptTracer, cost_cb: CostCallback) -> None:
    cost_cb.current_phase = "propose"
    cost_cb.current_trial = "2/3"

    lm = _FakeLM()
    tracer.on_lm_start(call_id="c1", instance=lm, inputs={})
    lm.history.append({"uuid": "u1", "model": "fake/model", "messages": [], "outputs": []})
    tracer.on_lm_end(call_id="c1", outputs={})
    tracer.close()

    row = _read_jsonl(tracer.jsonl_path)[0]
    assert row["phase"] == "propose"
    assert row["trial"] == "2/3"
    cost_cb.close()


def test_records_exception(tracer: PromptTracer, cost_cb: CostCallback) -> None:
    lm = _FakeLM()
    tracer.on_lm_start(call_id="c1", instance=lm, inputs={})
    tracer.on_lm_end(call_id="c1", outputs=None, exception=ValueError("boom"))
    tracer.close()

    row = _read_jsonl(tracer.jsonl_path)[0]
    assert "ValueError" in row["error"]
    assert "boom" in row["error"]
    assert row["model"] is None  # no history entry was added
    cost_cb.close()


class _PydanticLikeUsageDetails:
    """Mimics litellm.types.utils.CompletionTokensDetailsWrapper: a pydantic
    BaseModel with model_dump(). Stdlib json can't serialize it directly."""

    def __init__(self, **fields: int) -> None:
        self._fields = fields

    def model_dump(self) -> dict:
        return dict(self._fields)


def test_serializes_pydantic_usage_details(tracer: PromptTracer, cost_cb: CostCallback) -> None:
    """Regression for am-best-offer-d4z: litellm puts pydantic models inside
    `usage.completion_tokens_details`; the tracer must not silently drop the line."""
    lm = _FakeLM()
    tracer.on_lm_start(call_id="c1", instance=lm, inputs={})
    details = _PydanticLikeUsageDetails(cached_tokens=12, reasoning_tokens=34)
    lm.history.append(
        {
            "uuid": "u1",
            "model": "fake/model",
            "messages": [{"role": "user", "content": "hi"}],
            "outputs": ["yo"],
            "usage": {
                "prompt_tokens": 5,
                "completion_tokens": 1,
                "completion_tokens_details": details,
            },
        }
    )
    tracer.on_lm_end(call_id="c1", outputs={})
    tracer.close()

    rows = _read_jsonl(tracer.jsonl_path)
    assert len(rows) == 1
    usage = rows[0]["usage"]
    assert usage["prompt_tokens"] == 5
    assert usage["completion_tokens_details"] == {"cached_tokens": 12, "reasoning_tokens": 34}
    cost_cb.close()


def test_claim_set_prevents_double_count(tracer: PromptTracer, cost_cb: CostCallback) -> None:
    """Two concurrent calls on the same LM — each claims its own uuid."""
    lm = _FakeLM()
    tracer.on_lm_start(call_id="c1", instance=lm, inputs={})
    tracer.on_lm_start(call_id="c2", instance=lm, inputs={})
    lm.history.append({"uuid": "u1", "model": "fake/model", "messages": [{"role": "user", "content": "A"}], "outputs": ["a"]})
    lm.history.append({"uuid": "u2", "model": "fake/model", "messages": [{"role": "user", "content": "B"}], "outputs": ["b"]})
    tracer.on_lm_end(call_id="c1", outputs={})
    tracer.on_lm_end(call_id="c2", outputs={})
    tracer.close()

    rows = _read_jsonl(tracer.jsonl_path)
    assert len(rows) == 2
    contents = sorted(r["messages"][0]["content"] for r in rows)
    assert contents == ["A", "B"]
    cost_cb.close()
