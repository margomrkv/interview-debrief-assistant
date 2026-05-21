"""Live backend: real Splitter + real per-item scoring.

Both production stages run for real here. Stage 1 (Splitter) calls
``src.splitter.split_transcript`` — one LLM call turning the raw transcript into
Q&A — and the result is cached per ``source_id`` (the stream re-reads it for every
scoring/report call). Stage 2 (Scoring) is one LLM call per QA via
``src.assessor.assess.assess_one``. The interview-level verdict reuses the shared
``rollup_report`` so emulator and live report identical math (only the numbers —
labels vs model predictions — differ). The catalogue / transcript / upload-match
still come from ``EmulatorBackend`` (the demo's transcript store).
"""
from __future__ import annotations

from typing import Any

from src.assessor.assess import assess_one
from src.splitter.split import split_transcript
from src.ui.backend import EmulatorBackend
from src.ui.models import Aggregate, InterviewReport, InterviewSummary, QA, ScoreItem
from src.ui.report import METRICS, rollup_report

# Aggregate token from the 1..10 mean of the triplet; matches the CSS classes the
# frontend renders (strong / adequate / weak).
AGG_STRONG, AGG_ADEQUATE = 7.0, 4.0


def _text(node: Any) -> str | None:
    """Pull a non-empty ``.text`` out of a {text, time} node (mirror emulator)."""
    if isinstance(node, dict):
        t = node.get("text")
        return t if (isinstance(t, str) and t.strip()) else None
    return None


def _time(node: Any) -> str | None:
    return node.get("time") if isinstance(node, dict) else None


def _to_qa(item: QA) -> dict[str, Any]:
    """Map a ``QA`` split item to the fields ``assess_one`` expects."""
    return {
        "interviewer_question": item.question,
        "candidate_answer": item.answer,
        "question_topic": item.question_topic or "",
        "interview_stage": item.interview_stage or "",
    }


def _aggregate(triplet: dict[str, int]) -> Aggregate:
    mean = sum(triplet.values()) / len(triplet)
    if mean >= AGG_STRONG:
        return Aggregate.STRONG
    if mean >= AGG_ADEQUATE:
        return Aggregate.ADEQUATE
    return Aggregate.WEAK


class LiveBackend:
    demo_delays = False

    def __init__(self, lm: Any = None) -> None:
        self._emu = EmulatorBackend()       # catalogue + transcript store + match
        self._lm = lm                       # injectable LM for tests (mock)
        self._scored: dict[str, list[dict[str, int]]] = {}  # source_id -> triplets
        self._split_cache: dict[str, list[QA]] = {}         # source_id -> Q&A

    # ---- catalogue / transcript / match still come from the emulator -------
    def list_interviews(self) -> list[InterviewSummary]:
        return self._emu.list_interviews()

    def transcript_text(self, source_id: str) -> str:
        return self._emu.transcript_text(source_id)

    def match_source(self, uploaded_text: str) -> str | None:
        return self._emu.match_source(uploaded_text)

    # ---- real splitter, one LLM call per interview (cached) ----------------
    def split_items(self, source_id: str) -> list[QA]:
        """Stage 1: split the transcript into Q&A via one LLM call, cached.

        ``app.py`` re-invokes this for every scoring/report call within a stream;
        the cache keeps it to a single LLM call per ``source_id``.
        """
        if source_id in self._split_cache:
            return self._split_cache[source_id]

        raw = split_transcript(self.transcript_text(source_id), source_id)
        items = [
            QA(
                idx=idx,
                id=f"q{idx + 1:02d}",
                question=_text(it.get("interviewer_question")),
                question_time=_time(it.get("interviewer_question")),
                answer=_text(it.get("candidate_answer")),
                answer_time=_time(it.get("candidate_answer")),
                question_type=it.get("question_type"),
                question_topic=it.get("question_topic"),
                interview_stage=it.get("interview_stage"),
            )
            for idx, it in enumerate(raw)
        ]
        self._split_cache[source_id] = items
        return items

    # ---- real scoring, one LLM call per item -------------------------------
    def score_item(self, source_id: str, idx: int) -> ScoreItem:
        items = self.split_items(source_id)
        if not (0 <= idx < len(items)):
            return ScoreItem(idx=idx, scored=False)

        res = assess_one(_to_qa(items[idx]), lm=self._lm)
        triplet = {m: res.get(m) for m in METRICS}
        if res.get("error") or any(v is None for v in triplet.values()):
            return ScoreItem(idx=idx, scored=False)

        self._scored.setdefault(source_id, []).append(triplet)  # type: ignore[arg-type]
        return ScoreItem(
            idx=idx,
            scored=True,
            factual_correctness=triplet["factual_correctness"],
            focus=triplet["focus"],
            clarity=triplet["clarity"],
            aggregate=_aggregate(triplet),  # type: ignore[arg-type]
            rationale=res.get("reasoning"),
        )

    def report(self, source_id: str) -> InterviewReport:
        return rollup_report(
            source_id,
            self._scored.get(source_id, []),
            n_questions=len(self.split_items(source_id)),
        )
