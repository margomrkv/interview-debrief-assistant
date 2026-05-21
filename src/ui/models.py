"""Domain objects for the Backend contract (DTO / value objects).

The ``Backend`` interface (see ``src.ui.backend``) speaks these dataclasses
instead of bare dicts; ``app.py`` serializes them to JSON at the SSE/HTTP seam
via ``dataclasses.asdict``. Enums subclass ``str`` so ``json.dumps`` emits their
value (``"HIRE"``, ``"weak"``), keeping the wire contract the frontend reads.

Stdlib only (dataclasses + enum) so the emulator stays zero-install.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Verdict(str, Enum):
    HIRE = "HIRE"
    NO_HIRE = "NO_HIRE"


class Aggregate(str, Enum):
    STRONG = "strong"
    ADEQUATE = "adequate"
    WEAK = "weak"
    MISSING = "missing"


@dataclass
class InterviewSummary:
    """One catalogue entry for the interview list (sidebar)."""

    source_id: str
    title: str
    grade: str | None
    n_questions: int
    n_scored: int
    topics: list[str]


@dataclass
class QA:
    """A single interviewer-question / candidate-answer pair (Splitter output)."""

    idx: int
    id: str | None
    question: str | None
    question_time: str | None
    answer: str | None
    answer_time: str | None
    question_type: str | None
    question_topic: str | None
    interview_stage: str | None


@dataclass
class ScoreItem:
    """Per-QA assessment (Scoring output). Unscored items carry only idx+scored."""

    idx: int
    scored: bool
    factual_correctness: int | None = None
    focus: int | None = None
    clarity: int | None = None
    aggregate: Aggregate | None = None
    rationale: str | None = None
    unscored_reason: str | None = None


@dataclass
class InterviewReport:
    """Interview-level rollup → HIRE / NO_HIRE verdict (md/spec.md §3.4)."""

    source_id: str
    means: dict[str, float | None]
    overall: float | None
    p_hire: int | None
    verdict: Verdict | None
    n_questions: int
    n_scored: int
