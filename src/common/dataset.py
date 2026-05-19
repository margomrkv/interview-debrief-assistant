"""Load a stratified train/test split into dspy.Examples.

Generic JSON-corpus + splits.json → (train_examples, test_examples, splits_meta).
Callers (S3-train, S3-evaluate, future S4) supply the paths; this module knows
nothing about KB-specific layout.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import dspy

INPUT_FIELDS: tuple[str, ...] = (
    "interviewer_question",
    "candidate_answer",
    "reference_answer",
    "interviewer_feedback",
    "question_topic",
    "interview_stage",
)


def _text(field: Any) -> str:
    if field is None:
        return ""
    if isinstance(field, dict):
        return field.get("text") or ""
    return str(field)


def _to_example(item: dict[str, Any]) -> dspy.Example:
    return dspy.Example(
        interviewer_question=_text(item["interviewer_question"]),
        candidate_answer=_text(item["candidate_answer"]),
        reference_answer=_text(item.get("reference_answer")),
        interviewer_feedback=_text(item.get("interviewer_feedback")),
        question_topic=item.get("question_topic", "") or "",
        interview_stage=item.get("interview_stage", "") or "",
        reference_score=item["reference_score"],
        source_id=item["source_id"],
    ).with_inputs(*INPUT_FIELDS)


def load_split_examples(
    corpus_path: Path,
    splits_path: Path,
) -> tuple[list[dspy.Example], list[dspy.Example], dict[str, Any]]:
    raw = json.loads(corpus_path.read_text())
    items = raw["items"]
    splits = json.loads(splits_path.read_text())
    train = [_to_example(items[i]) for i in splits["train_indices"]]
    test = [_to_example(items[i]) for i in splits["test_indices"]]
    return train, test, splits
