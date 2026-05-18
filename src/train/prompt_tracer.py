"""Prompt+response tracer for DSPy LM calls.

Parallel to `CostCallback`: same `BaseCallback` hooks, separate JSONL sink.
Reads `instance.history` entries with a race-safe uuid claim set (independent
from CostCallback's claim set — both can run side by side under num_threads>1).

Phase/trial fields are read by reference from a `CostCallback` (DRY: we don't
re-parse MIPRO logs here; `MIPROPhaseHandler` already does that on the cost cb).
"""
from __future__ import annotations

import json
import logging
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dspy.utils.callback import BaseCallback

from src.train.cost_callback import CostCallback

_log = logging.getLogger(__name__)


def _json_default(obj: Any) -> Any:
    # litellm wraps usage details (e.g. CompletionTokensDetailsWrapper) in
    # pydantic BaseModel; stdlib json doesn't know about them.
    md = getattr(obj, "model_dump", None)
    if callable(md):
        return md()
    if hasattr(obj, "__dict__"):
        return vars(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


class PromptTracer(BaseCallback):
    """Writes one JSONL line per LM call with full messages + response."""

    def __init__(
        self,
        version: str,
        jsonl_path: Path,
        phase_ref: CostCallback,
    ) -> None:
        self.version = version
        self.phase_ref = phase_ref
        self._call_start: dict[str, float] = {}
        self._call_instance: dict[str, Any] = {}
        self._call_history_len: dict[str, int] = {}
        self._claimed_uuids: set[str] = set()
        self._lock = threading.Lock()
        jsonl_path.parent.mkdir(parents=True, exist_ok=True)
        self._fp = open(jsonl_path, "a", encoding="utf-8")
        self.jsonl_path = jsonl_path

    def on_lm_start(self, call_id: str, instance: Any, inputs: dict[str, Any]) -> None:
        with self._lock:
            self._call_start[call_id] = time.time()
            self._call_instance[call_id] = instance
            self._call_history_len[call_id] = len(getattr(instance, "history", []))

    def on_lm_end(
        self,
        call_id: str,
        outputs: dict[str, Any] | None,
        exception: Exception | None = None,
    ) -> None:
        now = time.time()
        with self._lock:
            t_start = self._call_start.pop(call_id, now)
            instance = self._call_instance.pop(call_id, None)
            start_len = self._call_history_len.pop(call_id, 0)
        latency_ms = int((now - t_start) * 1000)

        entry: dict[str, Any] | None = None
        try:
            history = getattr(instance, "history", None) if instance is not None else None
            if history is not None:
                with self._lock:
                    new_entries = list(history[start_len:])
                    for cand in new_entries:
                        uid = cand.get("uuid")
                        if uid and uid in self._claimed_uuids:
                            continue
                        if uid:
                            self._claimed_uuids.add(uid)
                        entry = cand
                        break
        except Exception as e:
            _log.debug("failed to read instance.history: %s", e)

        line = {
            "ts": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
            "phase": self.phase_ref.current_phase,
            "trial": self.phase_ref.current_trial,
            "call_id": call_id,
            "latency_ms": latency_ms,
            "model": (entry or {}).get("model"),
            "messages": (entry or {}).get("messages"),
            "response": (entry or {}).get("outputs") or (entry or {}).get("response"),
            "usage": (entry or {}).get("usage"),
            "error": (repr(exception) if exception is not None else None),
        }
        with self._lock:
            self._fp.write(json.dumps(line, ensure_ascii=False, default=_json_default) + "\n")
            self._fp.flush()

    def close(self) -> None:
        try:
            self._fp.flush()
            self._fp.close()
        except Exception:
            pass

    def __enter__(self) -> "PromptTracer":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()
