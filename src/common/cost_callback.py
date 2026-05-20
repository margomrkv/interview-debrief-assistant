"""Cost meter + per-trial progress for DSPy training runs.

Hooks all LM calls via `dspy.utils.callback.BaseCallback`, aggregates tokens
and dollars per model using an explicit `PRICES` table, and writes one JSONL
line per call. Throttled summary is emitted via `logger.debug` (hidden by
default; surfaced with `--verbose`).

Phase/trial tracking is handled by `MIPROPhaseHandler`, a `logging.Handler`
that sniffs INFO records from `dspy.teleprompt.mipro_v2`.

Pricing source: explicit dict (see plan tradeoffs). Models not in `PRICES`
get spend=0 and a one-time warning.
"""
from __future__ import annotations

import json
import logging
import re
import threading
import time
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dspy.utils.callback import BaseCallback

PRICES: dict[str, dict[str, float]] = {
    # USD per 1M tokens
    "anthropic/claude-sonnet-4-6": {"input": 3.0, "output": 15.0},
    "anthropic/claude-opus-4-7": {"input": 15.0, "output": 75.0},
    "anthropic/claude-haiku-4-5-20251001": {"input": 1.0, "output": 5.0},
    "openrouter/openai/gpt-5.4-nano": {"input": 0.2, "output": 1.5},
    "openrouter/nvidia/nemotron-3-super-120b-a12b:free": {"input": 0.0, "output": 0.0},
}

_SHORT_NAMES: dict[str, str] = {
    "anthropic/claude-sonnet-4-6": "sonnet",
    "anthropic/claude-opus-4-7": "opus",
    "anthropic/claude-haiku-4-5-20251001": "haiku",
    "openrouter/nvidia/nemotron-3-super-120b-a12b:free": "nemotron",
}

_log = logging.getLogger("cost")


@dataclass
class ModelStats:
    calls: int = 0
    in_tok: int = 0
    out_tok: int = 0
    spend: float = 0.0
    failures: int = 0


def _short(model: str) -> str:
    return _SHORT_NAMES.get(model, model.split("/")[-1][:20])


def _spend_for(model: str, in_tok: int, out_tok: int, prices: dict[str, dict[str, float]]) -> float:
    p = prices.get(model)
    if p is None:
        return 0.0
    return (in_tok * p["input"] + out_tok * p["output"]) / 1_000_000.0


class CostCallback(BaseCallback):
    """Aggregates per-call usage/spend, writes JSONL, prints throttled stderr."""

    def __init__(
        self,
        version: str,
        jsonl_path: Path,
        prices: dict[str, dict[str, float]] | None = None,
        throttle_sec: float = 2.0,
    ) -> None:
        self.version = version
        self.prices = prices if prices is not None else PRICES
        self.throttle_sec = throttle_sec
        self.totals: dict[str, ModelStats] = defaultdict(ModelStats)
        self.current_phase: str = "init"
        self.current_trial: str = "-"
        # Demoset / instruction indices of the trial currently under evaluation.
        # Updated *before* eval by the wrapper around MIPROv2's
        # `_select_and_insert_instructions_and_demos` (see src/kb/train.py); stay
        # "-" for bootstrap and the baseline full-eval (trial 1) that bypass it.
        self.current_demoset: str = "-"
        self.current_instruction: str = "-"
        # Proposed instruction texts in the order MIPROv2 proposed them (propose
        # phase). Filled by MIPROPhaseHandler from the `j: <instruction>` records;
        # consumed by _write_prompt_evolution to number instructions I0..In in
        # proposal order rather than first-seen-in-candidate_programs order.
        self.proposed_instructions: list[str] = []
        self._call_start: dict[str, float] = {}
        self._call_model: dict[str, str] = {}
        self._call_instance: dict[str, Any] = {}
        self._call_history_len: dict[str, int] = {}
        self._claimed_uuids: set[str] = set()
        self._unknown_warned: set[str] = set()
        self._last_log_t: float = 0.0
        self._lock = threading.Lock()
        # Counts DSPy-logger ERRORs that the LM callback can't see (adapter
        # parse failures happen after on_lm_end with a healthy token count, so
        # ModelStats.failures stays 0 even when MIPROv2 loses 46% of examples).
        # Surfaced in render_summary; populated by MIPROPhaseHandler.emit.
        self.parse_failures: int = 0
        jsonl_path.parent.mkdir(parents=True, exist_ok=True)
        self._jsonl_fp = open(jsonl_path, "a", encoding="utf-8")
        self.jsonl_path = jsonl_path

    def on_lm_start(self, call_id: str, instance: Any, inputs: dict[str, Any]) -> None:
        with self._lock:
            self._call_start[call_id] = time.time()
            self._call_model[call_id] = getattr(instance, "model", "unknown")
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
            model = self._call_model.pop(call_id, "unknown")
            instance = self._call_instance.pop(call_id, None)
            start_len = self._call_history_len.pop(call_id, 0)
        latency_ms = int((now - t_start) * 1000)

        # Race-safe per-call attribution: read instance.history[start_len:] and pick the
        # first entry whose uuid we haven't claimed yet. Under concurrent calls to the
        # same LM (num_threads>1), other threads may have appended in this window;
        # the claim set prevents double-counting.
        in_tok = 0
        out_tok = 0
        litellm_cost: float | None = None
        try:
            history = getattr(instance, "history", None) if instance is not None else None
            if history is not None:
                with self._lock:
                    new_entries = list(history[start_len:])
                    for entry in new_entries:
                        uid = entry.get("uuid")
                        if uid and uid in self._claimed_uuids:
                            continue
                        if entry.get("model") != model:
                            continue
                        if uid:
                            self._claimed_uuids.add(uid)
                        usage = entry.get("usage") or {}
                        in_tok = int(usage.get("prompt_tokens") or 0)
                        out_tok = int(usage.get("completion_tokens") or 0)
                        litellm_cost = entry.get("cost")
                        break
        except Exception as e:
            _log.debug("failed to read instance.history: %s", e)

        spend = _spend_for(model, in_tok, out_tok, self.prices)

        if model not in self.prices and model not in self._unknown_warned:
            self._unknown_warned.add(model)
            _log.warning("CostCallback: model %r not in PRICES — spend will be 0", model)

        with self._lock:
            s = self.totals[model]
            s.calls += 1
            s.in_tok += in_tok
            s.out_tok += out_tok
            s.spend += spend
            if exception is not None:
                s.failures += 1
            phase = self.current_phase
            trial = self.current_trial
            should_log = (now - self._last_log_t) >= self.throttle_sec
            if should_log:
                self._last_log_t = now
            snapshot = {m: (st.calls, st.in_tok, st.out_tok, st.spend) for m, st in self.totals.items()}

        # JSONL write (outside lock except for fp — fp itself is single-writer-safe enough
        # under GIL, but guard with lock to keep lines intact).
        line = json.dumps(
            {
                "ts": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
                "phase": phase,
                "trial": trial,
                "call_id": call_id,
                "model": model,
                "in_tok": in_tok,
                "out_tok": out_tok,
                "spend": round(spend, 6),
                "litellm_cost": litellm_cost,
                "latency_ms": latency_ms,
                "error": (repr(exception) if exception is not None else None),
            },
            ensure_ascii=False,
        )
        with self._lock:
            self._jsonl_fp.write(line + "\n")
            self._jsonl_fp.flush()

        if should_log:
            self._log_throttled(phase, trial, snapshot)

    def _log_throttled(
        self,
        phase: str,
        trial: str,
        snapshot: dict[str, tuple[int, int, int, float]],
    ) -> None:
        if not _log.isEnabledFor(logging.DEBUG):
            return
        try:
            total_calls = sum(v[0] for v in snapshot.values())
            total_in = sum(v[1] for v in snapshot.values())
            total_out = sum(v[2] for v in snapshot.values())
            total_spend = sum(v[3] for v in snapshot.values())
            parts = [f"{_short(m)}=${v[3]:.3f}" for m, v in snapshot.items()]
            _log.debug(
                "[%s %s] calls=%d  in=%.1fk out=%.1fk  $%.3f  (%s)",
                phase, trial, total_calls,
                total_in / 1000, total_out / 1000, total_spend,
                " ".join(parts),
            )
        except Exception as e:
            _log.warning("CostCallback throttled render failed: %s", e)

    def render_summary(self) -> dict[str, Any]:
        with self._lock:
            per_model = {
                m: {
                    "calls": s.calls,
                    "in_tok": s.in_tok,
                    "out_tok": s.out_tok,
                    "spend": round(s.spend, 6),
                    "failures": s.failures,
                }
                for m, s in self.totals.items()
            }
        total_in = sum(v["in_tok"] for v in per_model.values())
        total_out = sum(v["out_tok"] for v in per_model.values())
        total_spend = sum(v["spend"] for v in per_model.values())
        total_calls = sum(v["calls"] for v in per_model.values())
        return {
            "per_model": per_model,
            "total_calls": total_calls,
            "total_in": total_in,
            "total_out": total_out,
            "total_spend": round(total_spend, 6),
            "parse_failures": self.parse_failures,
            "jsonl_path": str(self.jsonl_path),
        }

    def close(self) -> None:
        try:
            self._jsonl_fp.flush()
            self._jsonl_fp.close()
        except Exception:
            pass

    def __enter__(self) -> "CostCallback":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()


class MIPROPhaseHandler(logging.Handler):
    """Sniff `dspy.teleprompt.mipro_v2` INFO records to update phase/trial on `cb`.

    Also counts ERROR-level records from DSPy's parallelizer/bootstrap/utils
    loggers as `cb.parse_failures` — these are adapter parse failures that
    don't surface through the LM callback (the LM call itself succeeded; only
    the structured-output extraction failed).
    """

    _TRIAL_RE = re.compile(r"[Tt]rial\s+(\d+)\s*/?\s*(\d+)?")
    # MIPROv2 logs each proposed instruction as one record `f"{j}: {instruction}"`
    # (mipro_optimizer_v2.py:504); DOTALL captures multi-line instruction bodies.
    _PROPOSED_RE = re.compile(r"^(\d+):\s(.*)", re.DOTALL)

    def __init__(self, cb: CostCallback) -> None:
        super().__init__(level=logging.INFO)
        self.cb = cb

    def emit(self, record: logging.LogRecord) -> None:
        if record.levelno >= logging.ERROR:
            with self.cb._lock:
                self.cb.parse_failures += 1
        try:
            msg = record.getMessage()
        except Exception:
            return
        low = msg.lower()
        if "bootstrap" in low:
            self.cb.current_phase = "bootstrap"
        elif "propos" in low or "instruction" in low:
            self.cb.current_phase = "propose"
        elif "optimiz" in low or "evaluat" in low or "average metric" in low:
            self.cb.current_phase = "evaluate"
        m = self._TRIAL_RE.search(msg)
        if m:
            total = m.group(2)
            self.cb.current_trial = f"{m.group(1)}/{total}" if total else m.group(1)
        # Capture proposed instructions in proposal order (only during propose).
        # j=0 is later overwritten with the seed by MIPROv2 — last write wins,
        # which mirrors the optimizer's own instruction_candidates[i][0] = seed.
        if self.cb.current_phase == "propose":
            pm = self._PROPOSED_RE.match(msg)
            if pm:
                j, text = int(pm.group(1)), pm.group(2).strip()
                lst = self.cb.proposed_instructions
                if j < len(lst):
                    lst[j] = text
                elif j == len(lst):
                    lst.append(text)
                else:  # gap (shouldn't happen) — pad to keep index alignment
                    lst.extend([""] * (j - len(lst)))
                    lst.append(text)


def cost_breakdown_markdown(summary: dict[str, Any]) -> list[str]:
    """Render `render_summary()` output as markdown lines for the train report."""
    lines: list[str] = [
        "## Cost breakdown",
        "",
        "| model | calls | input tokens | output tokens | spend USD |",
        "|---|---:|---:|---:|---:|",
    ]
    for model, s in sorted(summary["per_model"].items(), key=lambda kv: -kv[1]["spend"]):
        lines.append(
            f"| `{model}` | {s['calls']} | {s['in_tok']:,} | {s['out_tok']:,} | ${s['spend']:.4f} |"
        )
    lines.append(
        f"| **TOTAL** | {summary['total_calls']} | {summary['total_in']:,} | "
        f"{summary['total_out']:,} | **${summary['total_spend']:.4f}** |"
    )
    parse_failures = summary.get("parse_failures", 0)
    if parse_failures:
        lines += ["", f"⚠ DSPy adapter parse-failures: **{parse_failures}** (examples lost during bootstrap/evaluate)"]
    lines += ["", f"JSONL log: `{summary['jsonl_path']}`"]
    return lines
