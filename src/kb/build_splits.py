"""QA-level stratified train/test split of train/hard_skills.json.

See plan §"Fixed decisions" D7, D8, D13.
"""
from __future__ import annotations

import json
import logging
import random
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = REPO_ROOT / "data/knowledgebase/train" / "hard_skills.json"
DEFAULT_OUTPUT = REPO_ROOT / "data/knowledgebase/train" / "splits.json"
SMOKE_SOURCE_COUNT = 2


def _is_scored(item: dict[str, Any]) -> bool:
    score = item.get("reference_score") or {}
    return score.get("factual_correctness") is not None


def _stratified_split(
    indexed: list[tuple[int, str]],
    train_ratio: float,
    seed: int,
) -> tuple[list[int], list[int]]:
    rng = random.Random(seed)
    by_source: dict[str, list[int]] = {}
    for idx, src in indexed:
        by_source.setdefault(src, []).append(idx)

    train_idx: list[int] = []
    test_idx: list[int] = []
    for src, idxs in by_source.items():
        rng.shuffle(idxs)
        n_train = max(1, round(len(idxs) * train_ratio))
        if n_train == len(idxs) and len(idxs) > 1:
            n_train = len(idxs) - 1  # keep at least 1 test
        train_idx.extend(idxs[:n_train])
        test_idx.extend(idxs[n_train:])

    train_idx.sort()
    test_idx.sort()
    return train_idx, test_idx


def build_splits(
    input_path: Path,
    output_path: Path,
    train_ratio: float = 0.7,
    seed: int = 42,
    smoke: bool = False,
) -> dict[str, Any]:
    raw = json.loads(input_path.read_text())
    items: list[dict[str, Any]] = raw["items"]

    scored_indexed = [(i, it["source_id"]) for i, it in enumerate(items) if _is_scored(it)]
    excluded = [i for i, it in enumerate(items) if not _is_scored(it)]

    if smoke:
        sources = sorted({src for _, src in scored_indexed})
        kept = set(sources[:SMOKE_SOURCE_COUNT])
        scored_indexed = [(i, src) for i, src in scored_indexed if src in kept]

    train_idx, test_idx = _stratified_split(scored_indexed, train_ratio, seed)

    per_source: dict[str, dict[str, int]] = {}
    for i, src in scored_indexed:
        bucket = per_source.setdefault(src, {"train": 0, "test": 0})
        bucket["train" if i in set(train_idx) else "test"] += 1

    result = {
        "strategy": "qa_level_stratified_by_source_id",
        "input": str(input_path.relative_to(REPO_ROOT)),
        "train_ratio": train_ratio,
        "seed": seed,
        "smoke": smoke,
        "stats": {
            "train": len(train_idx),
            "test": len(test_idx),
            "excluded_unscored": len(excluded),
            "per_source": per_source,
        },
        "train_indices": train_idx,
        "test_indices": test_idx,
        "excluded_indices": excluded,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    return result


def log_split_summary(result: dict[str, Any], logger: logging.Logger) -> None:
    s = result["stats"]
    logger.info(
        "split: %d train / %d test (excluded unscored: %d)",
        s["train"], s["test"], s["excluded_unscored"],
    )
    for src, b in s["per_source"].items():
        logger.info("  %s: %d train / %d test", src, b["train"], b["test"])
