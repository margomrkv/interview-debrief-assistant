#!/usr/bin/env python3
"""Convert splitter JSON (LinkedText schema) to Excel."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from openpyxl import Workbook
except Exception as exc:  # pragma: no cover
    raise SystemExit("openpyxl is required. Install with: pip install openpyxl") from exc


ITEM_COLUMNS = [
    "source_id",
    "splitter_mode",
    "interviewer_question_text",
    "interviewer_question_time",
    "candidate_answer_text",
    "candidate_answer_time",
    "reference_answer_text",
    "reference_answer_time",
    "interviewer_feedback_text",
    "interviewer_feedback_time",
    "question_type",
    "question_topic",
    "interview_stage",
]


def _linked_text(linked: object) -> tuple[object, object]:
    if isinstance(linked, dict):
        return linked.get("text"), linked.get("time")
    return None, None


def convert(json_path: Path, xlsx_path: Path) -> None:
    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    source_id = data.get("source_id", "")
    splitter_mode = data.get("splitter_mode", "")
    items = data.get("items", [])

    wb = Workbook()
    ws = wb.active
    ws.title = "splitter_items"
    ws.append(ITEM_COLUMNS)

    for item in items:
        iq_t, iq_time = _linked_text(item.get("interviewer_question"))
        ca_t, ca_time = _linked_text(item.get("candidate_answer"))
        ra_t, ra_time = _linked_text(item.get("reference_answer"))
        fb_t, fb_time = _linked_text(item.get("interviewer_feedback"))

        ws.append(
            [
                source_id,
                splitter_mode,
                iq_t,
                iq_time,
                ca_t,
                ca_time,
                ra_t,
                ra_time,
                fb_t,
                fb_time,
                item.get("question_type"),
                item.get("question_topic"),
                item.get("interview_stage"),
            ]
        )

    meta = wb.create_sheet("meta")
    meta.append(["source_id", source_id])
    meta.append(["splitter_mode", splitter_mode])
    meta.append(["items_count", len(items)])

    xlsx_path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(xlsx_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert splitter JSON to Excel.")
    parser.add_argument("json_path", help="Path to splitter JSON")
    parser.add_argument("--out", dest="out_path", default=None, help="Output .xlsx path")
    args = parser.parse_args()

    json_path = Path(args.json_path)
    if not json_path.exists():
        raise SystemExit(f"Input file not found: {json_path}")

    if args.out_path:
        out_path = Path(args.out_path)
    else:
        out_path = json_path.with_suffix(".xlsx")

    convert(json_path, out_path)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
