"""Unit tests for ScoreLogger + MIPROPhaseHandler — offline, no LM calls."""
from __future__ import annotations

import csv
import logging
from pathlib import Path
from types import SimpleNamespace

import pytest

from src.common.cost_callback import CostCallback, MIPROPhaseHandler
from src.common.score_logger import ScoreLogger


@pytest.fixture
def cost_cb(tmp_path: Path) -> CostCallback:
    return CostCallback(version="vtest", jsonl_path=tmp_path / "cost.jsonl")


def _read_csv(path: Path) -> tuple[list[str], list[list[str]]]:
    rows = list(csv.reader(path.read_text().splitlines()))
    return rows[0], rows[1:]


def test_csv_carries_demoset_and_instruction(tmp_path: Path, cost_cb: CostCallback) -> None:
    cost_cb.current_phase = "evaluate"
    cost_cb.current_trial = "3/5"
    cost_cb.current_demoset = "2"
    cost_cb.current_instruction = "1"

    example = SimpleNamespace(
        reference_score={"factual_correctness": 4, "focus": 3, "clarity": 5},
        source_id="src-1",
        interview_stage="onsite",
        question_topic="dsa",
    )
    pred = SimpleNamespace(factual_correctness=4, focus=2, clarity=5, _error="")

    logger = ScoreLogger(csv_path=tmp_path / "scores.csv", phase_ref=cost_cb)
    logger.log(example, pred, 0.8)
    logger.close()

    header, rows = _read_csv(tmp_path / "scores.csv")
    assert header[:5] == ["ts", "phase", "trial", "demoset", "instruction"]
    assert len(rows) == 1
    row = dict(zip(header, rows[0]))
    assert row["demoset"] == "2"
    assert row["instruction"] == "1"
    assert row["trial"] == "3/5"
    assert row["ref_focus"] == "3"
    assert row["pred_focus"] == "2"
    assert row["err_focus"] == "1"


def test_csv_defaults_dash_when_unset(tmp_path: Path, cost_cb: CostCallback) -> None:
    # bootstrap / baseline calls never go through the selector wrapper.
    example = SimpleNamespace(
        reference_score={"factual_correctness": 5, "focus": 5, "clarity": 5},
        source_id="src-2",
        interview_stage="",
        question_topic="",
    )
    pred = SimpleNamespace(factual_correctness=5, focus=5, clarity=5)

    logger = ScoreLogger(csv_path=tmp_path / "scores.csv", phase_ref=cost_cb)
    logger.log(example, pred, 1.0)
    logger.close()

    _, rows = _read_csv(tmp_path / "scores.csv")
    row = rows[0]
    assert row[3] == "-"  # demoset
    assert row[4] == "-"  # instruction


def _record(msg: str, logger_name: str = "dspy.teleprompt.mipro_optimizer_v2") -> logging.LogRecord:
    return logging.LogRecord(
        name=logger_name, level=logging.INFO, pathname=__file__, lineno=1,
        msg=msg, args=(), exc_info=None,
    )


def test_phase_handler_captures_proposed_instructions_in_order(cost_cb: CostCallback) -> None:
    h = MIPROPhaseHandler(cost_cb)
    # Enter propose phase, then each instruction logged as `j: <text>`.
    h.emit(_record("\n==> STEP 2: PROPOSE INSTRUCTION CANDIDATES <=="))
    h.emit(_record("0: seed instruction"))
    h.emit(_record("1: second\nmulti-line instruction"))
    h.emit(_record("2: third"))

    assert cost_cb.proposed_instructions == [
        "seed instruction",
        "second\nmulti-line instruction",
        "third",
    ]


def test_phase_handler_ignores_proposal_lines_outside_propose(cost_cb: CostCallback) -> None:
    h = MIPROPhaseHandler(cost_cb)
    # In evaluate phase a "0: ..." line must not be mistaken for a proposal.
    h.emit(_record("== Trial 2 / 5 - Full Evaluation =="))
    h.emit(_record("0: 0.83, 0.91, 0.75"))  # e.g. a score dump, not a prompt
    assert cost_cb.proposed_instructions == []
    # trial parsing still works
    assert cost_cb.current_trial == "2/5"
