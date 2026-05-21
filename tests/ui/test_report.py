"""rollup_report math + emulator.report delegation — offline, no LLM, stdlib only."""
from __future__ import annotations

from src.ui import emulator
from src.ui.models import Verdict
from src.ui.report import rollup_report


def test_rollup_basic_means_and_verdict() -> None:
    scored = [
        {"factual_correctness": 4, "focus": 4, "clarity": 4},
        {"factual_correctness": 2, "focus": 5, "clarity": 3},
    ]
    r = rollup_report("sid", scored, n_questions=3)
    assert r.means == {"factual_correctness": 3.0, "focus": 4.5, "clarity": 3.5}
    # overall = 22/6 = 3.6667 → p_hire = round((3.6667-1)/9*100) = 30 → NO_HIRE
    assert r.overall == 3.7
    assert r.p_hire == 30
    assert r.verdict == Verdict.NO_HIRE
    assert (r.n_questions, r.n_scored) == (3, 2)


def test_rollup_empty_is_none() -> None:
    r = rollup_report("sid", [], n_questions=5)
    assert r.means == {m: None for m in ("factual_correctness", "focus", "clarity")}
    assert r.overall is None and r.p_hire is None and r.verdict is None
    assert (r.n_questions, r.n_scored) == (5, 0)


def test_emulator_report_delegation_regression() -> None:
    """Lock the known fixture's verdict after report() was refactored to delegate."""
    sid = "data_scientist_junior_karpov_2022_03_30"
    r = emulator.report(sid)
    assert r.p_hire == 52
    assert r.verdict == Verdict.HIRE
    assert (r.n_questions, r.n_scored) == (29, 29)
    assert r.means == {"factual_correctness": 5.8, "focus": 5.6, "clarity": 5.7}
