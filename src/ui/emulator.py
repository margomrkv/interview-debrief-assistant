"""Emulator backend for the demo UI.

No real LLM calls. The two production stages (Splitter → Scoring) are *replayed*
from pre-computed per-interview data laid out under
``data/emulator-data/**/emulator-data/`` (see that folder's README.md):

* ``../transcript.txt`` — the file the user "uploads" (Splitter input);
* ``qa.json``           — Splitter output: one Q&A per item, no scores;
* ``scores.json``       — Scoring output: the three criteria + aggregate per item.

``qa.json`` and ``scores.json`` are joined by the shared ``id`` (q01…qNN). Each
``emulator-data`` folder is one uploadable transcript, keyed by its ``source_id``.
The interview-level verdict (HIRE / NO_HIRE + p_hire 0..100) is rolled up from the
per-item scores, mirroring ``AlignmentReport`` in md/spec.md §3.4.
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
EMU_ROOT = REPO_ROOT / "data" / "emulator-data"

METRICS = ("factual_correctness", "focus", "clarity")
SCORE_MIN, SCORE_MAX = 1, 10


def _text(node: Any) -> str | None:
    """Pull ``.text`` out of a {text, time} node, tolerating None/str."""
    if isinstance(node, dict):
        t = node.get("text")
        return t if (isinstance(t, str) and t.strip()) else None
    if isinstance(node, str) and node.strip():
        return node
    return None


def _time(node: Any) -> str | None:
    return node.get("time") if isinstance(node, dict) else None


def _pretty_title(source_id: str) -> str:
    # data_scientist_junior_karpov_2022_03_30 → "Data Scientist Junior Karpov 2022 03 30"
    return source_id.replace("_", " ").strip().title()


@lru_cache(maxsize=1)
def _catalogue() -> dict[str, dict[str, Any]]:
    """Discover every ``emulator-data`` folder → one entry per ``source_id``.

    Each entry bundles the interview's transcript path and the two replay files
    already joined by ``id`` into an ordered list of {qa, score} pairs.
    """
    catalogue: dict[str, dict[str, Any]] = {}
    if not EMU_ROOT.exists():
        return catalogue

    for ed in sorted(EMU_ROOT.glob("**/emulator-data")):
        qa_path, scores_path = ed / "qa.json", ed / "scores.json"
        if not (qa_path.exists() and scores_path.exists()):
            continue
        qa = json.loads(qa_path.read_text(encoding="utf-8"))
        scores = json.loads(scores_path.read_text(encoding="utf-8"))

        source_id = qa.get("source_id") or scores.get("source_id") or ed.parent.name
        scores_by_id = {s["id"]: s for s in scores.get("items", [])}

        pairs: list[dict[str, Any]] = []
        for qa_item in qa.get("items", []):
            pairs.append({"qa": qa_item, "score": scores_by_id.get(qa_item["id"], {})})

        catalogue[source_id] = {
            "source_id": source_id,
            "transcript_path": ed.parent / "transcript.txt",
            "labeling": scores.get("labeling"),
            "pairs": pairs,
        }
    return catalogue


def _entry(source_id: str) -> dict[str, Any] | None:
    return _catalogue().get(source_id)


# --------------------------------------------------------------------------- API


def list_interviews() -> list[dict[str, Any]]:
    """Catalogue of emulated transcripts for the sidebar."""
    out: list[dict[str, Any]] = []
    for sid, entry in _catalogue().items():
        pairs = entry["pairs"]
        scored = sum(1 for p in pairs if p["score"].get("reference_score"))
        grade = next((p["qa"].get("grade") for p in pairs if p["qa"].get("grade")), None)
        topics = sorted({p["qa"].get("question_topic")
                         for p in pairs if p["qa"].get("question_topic")})
        out.append({
            "source_id": sid,
            "title": _pretty_title(sid),
            "grade": grade,
            "n_questions": len(pairs),
            "n_scored": scored,
            "topics": topics,
        })
    out.sort(key=lambda x: (-x["n_scored"], x["source_id"]))
    return out


def transcript_text(source_id: str) -> str:
    """The raw transcript the user "uploaded" (Splitter input)."""
    entry = _entry(source_id)
    if not entry:
        return ""
    path: Path = entry["transcript_path"]
    return path.read_text(encoding="utf-8") if path.exists() else ""


def split_items(source_id: str) -> list[dict[str, Any]]:
    """Stage 1 output: one Q&A per item, classification but no scores."""
    entry = _entry(source_id)
    if not entry:
        return []
    out: list[dict[str, Any]] = []
    for idx, pair in enumerate(entry["pairs"]):
        qa = pair["qa"]
        out.append({
            "idx": idx,
            "id": qa.get("id"),
            "question": _text(qa.get("interviewer_question")),
            "question_time": _time(qa.get("interviewer_question")),
            "answer": _text(qa.get("candidate_answer")),
            "answer_time": _time(qa.get("candidate_answer")),
            "question_type": qa.get("question_type"),
            "question_topic": qa.get("question_topic"),
            "interview_stage": qa.get("interview_stage"),
        })
    return out


def score_item(source_id: str, idx: int) -> dict[str, Any]:
    """Stage 2 output for one item: the three criteria + rationale, or no-signal."""
    entry = _entry(source_id)
    pairs = entry["pairs"] if entry else []
    if not (0 <= idx < len(pairs)):
        return {"idx": idx, "scored": False}
    score = pairs[idx]["score"]
    rs = score.get("reference_score")
    if not rs:
        return {"idx": idx, "scored": False,
                "unscored_reason": score.get("unscored_reason")}
    return {
        "idx": idx,
        "scored": True,
        "factual_correctness": rs.get("factual_correctness"),
        "focus": rs.get("focus"),
        "clarity": rs.get("clarity"),
        "aggregate": rs.get("aggregate"),
        "rationale": rs.get("rationale"),
    }


def report(source_id: str) -> dict[str, Any]:
    """Interview-level rollup → AlignmentReport-style verdict (md/spec.md §3.4)."""
    entry = _entry(source_id)
    pairs = entry["pairs"] if entry else []
    scored = [p["score"]["reference_score"] for p in pairs
              if p["score"].get("reference_score")]

    means: dict[str, float | None] = {}
    all_vals: list[float] = []
    for m in METRICS:
        vals = [rs[m] for rs in scored if rs.get(m) is not None]
        means[m] = round(sum(vals) / len(vals), 1) if vals else None
        all_vals += vals

    overall = sum(all_vals) / len(all_vals) if all_vals else None
    if overall is None:
        p_hire, verdict = None, None
    else:
        p_hire = round((overall - SCORE_MIN) / (SCORE_MAX - SCORE_MIN) * 100)
        verdict = "HIRE" if p_hire >= 50 else "NO_HIRE"

    return {
        "source_id": source_id,
        "means": means,
        "overall": round(overall, 1) if overall is not None else None,
        "p_hire": p_hire,
        "verdict": verdict,
        "n_questions": len(pairs),
        "n_scored": len(scored),
    }


def match_source(uploaded_text: str) -> str | None:
    """Map an uploaded transcript .txt back to a known ``source_id``.

    Compares the uploaded text against each interview's real ``transcript.txt``
    (exact match, then containment), so the "upload transcript" gesture resolves
    to the right replay data. Falls back to None when nothing matches.
    """
    needle = uploaded_text.strip()
    if not needle:
        return None
    candidates = [(sid, transcript_text(sid).strip()) for sid in _catalogue()]
    for sid, hay in candidates:
        if hay and needle == hay:
            return sid
    for sid, hay in candidates:
        if hay and (needle in hay or hay in needle):
            return sid
    return None
