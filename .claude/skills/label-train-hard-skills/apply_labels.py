#!/usr/bin/env python3
"""Apply reference_score labels to train/hard_skills.json.

Reads per-item scores from labels.json (produced by the labeling step of the
label-train-hard-skills skill — see SKILL.md) and writes them into
train/hard_skills.json in the canonical structure (commit a2c7ebf shape):
each item gets a 6-field `reference_score`, plus a top-level `labeling` block.

Scale: 1..10, calibrated per item.grade (see SKILL.md prompt).
Policy: score only from interviewer_feedback and/or reference_answer.
Items absent from labels.json receive reference_score=null (unscored).
"""
import json
from datetime import date
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent
REPO_ROOT = SKILL_DIR.parents[2]  # .../label-train-hard-skills -> skills -> .claude -> repo
PATH = REPO_ROOT / "train" / "hard_skills.json"
LABELS = SKILL_DIR / "labels.json"

CRITERIA_SOURCE = ".claude/skills/label-train-hard-skills/SKILL.md (1..10, calibrated per item.grade)"
POLICY = (
    "score only from interviewer_feedback and/or reference_answer; "
    "calibrate to item.grade; no industry baseline"
)
VALID_SOURCES = {"feedback", "reference", "both"}


def aggregate(fc: int, fo: int, cl: int, candidate_empty: bool) -> str:
    """Map 1..10 scores to a verdict band aligned with the prompt anchors
    (7 = hire, 5-6 = borderline, <=4 = no-hire)."""
    if candidate_empty:
        return "missing"
    vals = [fc, fo, cl]
    if min(vals) <= 4:
        return "weak"
    if min(vals) >= 7:
        return "strong"
    return "adequate"  # all in 5..6 band


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    items = data["items"]

    raw = json.loads(LABELS.read_text(encoding="utf-8"))
    # labels.json: list of {"idx": int, "factual_correctness", "focus",
    # "clarity", "signal_source", "rationale"}
    scores: dict[int, dict] = {}
    for rec in raw:
        idx = rec["idx"]
        if idx in scores:
            raise RuntimeError(f"duplicate idx {idx} in {LABELS.name}")
        if idx < 0 or idx >= len(items):
            raise RuntimeError(f"idx {idx} out of range 0..{len(items) - 1}")
        scores[idx] = rec

    for i, it in enumerate(items):
        # Strip any stale label fields before re-applying (idempotent reruns).
        it.pop("reference_score", None)
        it.pop("unscored_reason", None)

        cand = (it.get("candidate_answer") or {}).get("text") or ""
        cand_empty = not cand.strip()

        rec = scores.get(i)
        if rec is None:
            it["reference_score"] = None
            it["unscored_reason"] = "no_interviewer_signal"
            continue

        fc = int(rec["factual_correctness"])
        fo = int(rec["focus"])
        cl = int(rec["clarity"])
        src = rec["signal_source"]
        rat = rec["rationale"]

        for v in (fc, fo, cl):
            if not (1 <= v <= 10):
                raise RuntimeError(f"item {i}: score {v} out of 1..10")
        if src not in VALID_SOURCES:
            raise RuntimeError(f"item {i}: signal_source {src!r} not in {VALID_SOURCES}")

        if cand_empty:
            fc, fo, cl = 1, 1, 1  # empty answer -> floor + missing
        agg = aggregate(fc, fo, cl, cand_empty)

        it["reference_score"] = {
            "factual_correctness": fc,
            "focus": fo,
            "clarity": cl,
            "aggregate": agg,
            "signal_source": src,
            "rationale": rat,
        }

    labeled = sum(1 for it in items if it.get("reference_score") is not None)
    unscored = sum(1 for it in items if it.get("reference_score") is None)
    data["labeling"] = {
        "labeled_at": date.today().isoformat(),
        "labeler": "claude-code-opus-4-7",
        "scale": "1..10",
        "criteria_source": CRITERIA_SOURCE,
        "policy": POLICY,
        "stats": {"total": len(items), "labeled": labeled, "unscored": unscored},
    }

    # Reorder: split_strategy, labeling, ..., items (items last).
    ordered: dict = {}
    for k in data:
        if k in ("items", "labeling"):
            continue
        ordered[k] = data[k]
    ordered["labeling"] = data["labeling"]
    ordered["items"] = data["items"]

    PATH.write_text(
        json.dumps(ordered, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {PATH}")
    print(f"labeled={labeled}, unscored={unscored}, total={len(items)}")


if __name__ == "__main__":
    main()
