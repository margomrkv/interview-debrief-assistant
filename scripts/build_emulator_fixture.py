#!/usr/bin/env python3
"""Build data/emulator-data fixture from a validated *.qa-split.json.

Scores are heuristic demo labels when hard_skills.json has no reference_score
for the source (public mock interviews). For production labels use train JSON.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def _text(node) -> str | None:
    if isinstance(node, dict):
        t = node.get("text")
        return t if isinstance(t, str) and t.strip() else None
    return None


def _has_signal(item: dict) -> bool:
    return bool(_text(item.get("interviewer_feedback")) or _text(item.get("reference_answer")))


def _aggregate(avg: float) -> str:
    if avg < 5:
        return "weak"
    if avg < 7:
        return "adequate"
    return "strong"


def _heuristic_scores(item: dict) -> dict:
    fb = (_text(item.get("interviewer_feedback")) or "").lower()
    ans = _text(item.get("candidate_answer")) or ""

    boosts = [
        ("exactly it", (8, 8, 8)),
        ("really good", (8, 7, 7)),
        ("definitely along", (8, 7, 7)),
        ("that's great", (8, 7, 7)),
        ("good point", (7, 7, 6)),
        ("good start", (6, 6, 6)),
        ("right path", (7, 6, 6)),
        ("really close", (7, 6, 6)),
        ("super", (7, 7, 6)),
    ]
    for needle, triple in boosts:
        if needle in fb:
            f, fo, c = triple
            avg = (f + fo + c) / 3
            return {
                "factual_correctness": f,
                "focus": fo,
                "clarity": c,
                "aggregate": _aggregate(avg),
                "signal_source": "feedback",
                "rationale": f"Demo heuristic: positive interviewer cue (“{needle}”).",
            }

    if len(ans) < 40:
        return {
            "factual_correctness": 4,
            "focus": 4,
            "clarity": 4,
            "aggregate": "weak",
            "signal_source": "feedback",
            "rationale": "Demo heuristic: short / incomplete answer.",
        }

    f, fo, c = 6, 6, 5
    return {
        "factual_correctness": f,
        "focus": fo,
        "clarity": c,
        "aggregate": _aggregate((f + fo + c) / 3),
        "signal_source": "feedback",
        "rationale": "Demo heuristic: neutral progression on case discussion.",
    }


def build(split_path: Path, raw_dir: Path, out_dir: Path, *, hard_only: bool = True) -> None:
    split = json.loads(split_path.read_text(encoding="utf-8"))
    source_id = split["source_id"]
    selected: list[dict] = []
    for item in split.get("items", []):
        if hard_only and item.get("question_type") not in ("hard", "technical_qna"):
            continue
        if not _has_signal(item):
            continue
        selected.append(item)

    qa_items = []
    score_items = []
    for n, item in enumerate(selected, start=1):
        qid = f"q{n:02d}"
        qa_items.append({
            "id": qid,
            "interviewer_question": item.get("interviewer_question"),
            "candidate_answer": item.get("candidate_answer"),
            "reference_answer": item.get("reference_answer"),
            "interviewer_feedback": item.get("interviewer_feedback"),
            "question_type": item.get("question_type"),
            "question_topic": item.get("question_topic"),
            "interview_stage": item.get("interview_stage"),
            "grade": item.get("grade") or "middle",
        })
        rs = _heuristic_scores(item)
        score_items.append({"id": qid, "reference_score": rs})

    out_dir.mkdir(parents=True, exist_ok=True)
    transcript_src = raw_dir / "transcript.txt"
    if not transcript_src.exists():
        raise SystemExit(f"missing transcript: {transcript_src}")
    shutil.copy2(transcript_src, out_dir / "transcript.txt")

    qa_path = out_dir / "qa.json"
    qa_path.write_text(
        json.dumps({"source_id": source_id, "items": qa_items}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    scores_path = out_dir / "scores.json"
    scores_path.write_text(
        json.dumps(
            {
                "source_id": source_id,
                "labeling": {
                    "labeled_at": date.today().isoformat(),
                    "labeler": "build_emulator_fixture.py (demo heuristic)",
                    "scale": "1..10",
                    "policy": "public UI demo only — not Opus/human labels",
                    "stats": {
                        "total": len(score_items),
                        "labeled": len(score_items),
                        "unscored": 0,
                    },
                },
                "items": score_items,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {qa_path} ({len(qa_items)} items)")
    print(f"Wrote {scores_path}")
    print(f"source_id={source_id}")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--split", type=Path, required=True)
    p.add_argument("--raw-dir", type=Path, required=True)
    p.add_argument("--out-dir", type=Path, required=True)
    p.add_argument("--all-types", action="store_true", help="include soft/behavioral items")
    args = p.parse_args()
    build(args.split, args.raw_dir, args.out_dir, hard_only=not args.all_types)


if __name__ == "__main__":
    main()
