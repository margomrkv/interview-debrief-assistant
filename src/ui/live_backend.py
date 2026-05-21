"""Live backend: real per-item scoring, Q&A still sourced from the emulator.

Splitting is delegated to ``EmulatorBackend`` (pre-computed ``qa.json``) until a
real ``src/splitter`` lands; scoring is real — one LLM call per QA via
``src.assessor.score.assess_one`` (the UI-facing assessor entry point). The
interview-level verdict reuses the shared ``rollup_report`` so emulator and live
report identical math (only the numbers — labels vs model predictions — differ).
"""
from __future__ import annotations

from typing import Any

from src.assessor.score import assess_one
from src.ui.backend import EmulatorBackend
from src.ui.report import METRICS, rollup_report

# Aggregate token from the 1..10 mean of the triplet; matches the CSS classes the
# frontend renders (strong / adequate / weak).
AGG_STRONG, AGG_ADEQUATE = 7.0, 4.0


def _to_qa(item: dict[str, Any]) -> dict[str, Any]:
    """Rename emulator split-payload keys to the fields ``assess_one`` expects."""
    return {
        "interviewer_question": item.get("question"),
        "candidate_answer": item.get("answer"),
        "question_topic": item.get("question_topic", ""),
        "interview_stage": item.get("interview_stage", ""),
    }


def _aggregate(triplet: dict[str, int]) -> str:
    mean = sum(triplet.values()) / len(triplet)
    if mean >= AGG_STRONG:
        return "strong"
    if mean >= AGG_ADEQUATE:
        return "adequate"
    return "weak"


class LiveBackend:
    demo_delays = False

    def __init__(self, lm: Any = None) -> None:
        self._emu = EmulatorBackend()       # source of split items + catalogue + match
        self._lm = lm                       # injectable LM for tests (mock)
        self._scored: dict[str, list[dict[str, int]]] = {}  # source_id -> triplets

    # ---- delegated to the emulator (until a real splitter exists) ----------
    def list_interviews(self) -> list[dict[str, Any]]:
        return self._emu.list_interviews()

    def transcript_text(self, source_id: str) -> str:
        return self._emu.transcript_text(source_id)

    def match_source(self, uploaded_text: str) -> str | None:
        return self._emu.match_source(uploaded_text)

    def split_items(self, source_id: str) -> list[dict[str, Any]]:
        return self._emu.split_items(source_id)

    # ---- real scoring, one LLM call per item -------------------------------
    def score_item(self, source_id: str, idx: int) -> dict[str, Any]:
        items = self.split_items(source_id)
        if not (0 <= idx < len(items)):
            return {"idx": idx, "scored": False}

        res = assess_one(_to_qa(items[idx]), lm=self._lm)
        triplet = {m: res.get(m) for m in METRICS}
        if res.get("error") or any(v is None for v in triplet.values()):
            return {"idx": idx, "scored": False}

        self._scored.setdefault(source_id, []).append(triplet)  # type: ignore[arg-type]
        return {
            "idx": idx,
            "scored": True,
            **triplet,
            "aggregate": _aggregate(triplet),  # type: ignore[arg-type]
            "rationale": res.get("reasoning"),
        }

    def report(self, source_id: str) -> dict[str, Any]:
        return rollup_report(
            source_id,
            self._scored.get(source_id, []),
            n_questions=len(self.split_items(source_id)),
        )
