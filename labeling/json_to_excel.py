#!/usr/bin/env python3
"""Convert annotation JSON to Excel (.xlsx) with fixed columns."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

try:
    from openpyxl import Workbook
except Exception as exc:  # pragma: no cover
    raise SystemExit(
        "openpyxl is required. Install with: pip install openpyxl"
    ) from exc


ITEM_COLUMNS = [
    "source_id",
    "question",
    "answer",
    "model_answer",
    "question_type",
    "topic_tag",
    "interview_stage",
    "question_fit",
    "focus",
    "clarity",
    "clarity_label",
    "completeness",
    "completeness_label",
    "accuracy",
    "accuracy_label",
    "STAR_S",
    "STAR_T",
    "STAR_A",
    "STAR_R",
    "SCID_S",
    "SCID_S_label",
    "SCID_C",
    "SCID_C_label",
    "SCID_I",
    "SCID_I_label",
    "SCID_D",
    "SCID_D_label",
    "notes_ai",
    "feedback_interviewer",
    "notes_user",
]


def _stringify(value: Any) -> Any:
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return value


def _score_label(score: Any) -> Any:
    mapping = {
        0: "None / Fails",
        1: "Weak",
        2: "Adequate",
        3: "Strong",
        None: None,
    }
    return mapping.get(score, None)


def convert(json_path: Path, xlsx_path: Path) -> None:
    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    source_id = data.get("source_id", "")
    items = data.get("items", [])
    summary = data.get("summary", {})

    wb = Workbook()
    ws_items = wb.active
    ws_items.title = "items"
    ws_items.append(ITEM_COLUMNS)

    for item in items:
        # Auto-fill labels for 0..3 metrics if missing.
        if "clarity_label" not in item:
            item["clarity_label"] = _score_label(item.get("clarity"))
        if "completeness_label" not in item:
            item["completeness_label"] = _score_label(item.get("completeness"))
        if "accuracy_label" not in item:
            item["accuracy_label"] = _score_label(item.get("accuracy"))
        if "SCID_S_label" not in item:
            item["SCID_S_label"] = _score_label(item.get("SCID_S"))
        if "SCID_C_label" not in item:
            item["SCID_C_label"] = _score_label(item.get("SCID_C"))
        if "SCID_I_label" not in item:
            item["SCID_I_label"] = _score_label(item.get("SCID_I"))
        if "SCID_D_label" not in item:
            item["SCID_D_label"] = _score_label(item.get("SCID_D"))

        row = []
        for col in ITEM_COLUMNS:
            if col == "source_id":
                row.append(source_id)
            else:
                row.append(_stringify(item.get(col)))
        ws_items.append(row)

    ws_summary = wb.create_sheet("summary")
    ws_summary.append(["source_id", source_id])
    ws_summary.append(["total_items", summary.get("total_items")])
    ws_summary.append(["by_question_type", _stringify(summary.get("by_question_type"))])
    ws_summary.append(
        ["by_interview_stage", _stringify(summary.get("by_interview_stage"))]
    )

    xlsx_path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(xlsx_path)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert annotation JSON to Excel (.xlsx)."
    )
    parser.add_argument("json_path", help="Path to input annotation JSON")
    parser.add_argument(
        "--out",
        dest="out_path",
        default=None,
        help="Output .xlsx path (default: same name next to JSON)",
    )
    args = parser.parse_args()

    json_path = Path(args.json_path)
    if not json_path.exists():
        raise SystemExit(f"Input file not found: {json_path}")

    if args.out_path:
        xlsx_path = Path(args.out_path)
    else:
        xlsx_path = json_path.with_suffix(".xlsx")

    convert(json_path, xlsx_path)
    print(f"Saved: {xlsx_path}")


if __name__ == "__main__":
    main()

