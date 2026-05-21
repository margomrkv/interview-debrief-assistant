"""Interview-level rollup shared by the emulator and live backends.

Both backends produce a list of per-item score triplets (factual_correctness /
focus / clarity); the verdict math (means → overall → p_hire → HIRE/NO_HIRE) is
identical, so it lives here once. Mirrors ``AlignmentReport`` in md/spec.md §3.4.
"""
from __future__ import annotations

from typing import Any

# Kept local (stdlib-only) so the emulator demo stays zero-install — must match
# src/common/dspy_modules.{METRICS,SCORE_MIN,SCORE_MAX}.
METRICS = ("factual_correctness", "focus", "clarity")
SCORE_MIN, SCORE_MAX = 1, 10


def rollup_report(
    source_id: str,
    scored: list[dict[str, Any]],
    n_questions: int,
) -> dict[str, Any]:
    """Aggregate per-item triplets into the ``report`` SSE payload.

    ``scored`` is the list of items that produced a score, each a dict carrying
    the three METRICS. ``n_questions`` is the total number of split items.
    """
    means: dict[str, float | None] = {}
    all_vals: list[float] = []
    for m in METRICS:
        vals = [s[m] for s in scored if s.get(m) is not None]
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
        "n_questions": n_questions,
        "n_scored": len(scored),
    }
