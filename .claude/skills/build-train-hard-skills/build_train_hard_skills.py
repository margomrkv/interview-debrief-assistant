"""Собирает train/hard_skills.json из splitter_output/**/*.v*.qa-split.json (и legacy *.qa-split.v*.json).

Берёт только последнюю версию (vN) на каждый source_id, фильтрует
question_type == "hard", добавляет в каждый item поле source_id первым.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SPLITTER_DIR = REPO_ROOT / "splitter_output"
OUT_PATH = REPO_ROOT / "train" / "hard_skills.json"

VERSION_RE_NEW = re.compile(r"\.v(\d+)\.qa-split\.json$")
VERSION_RE_OLD = re.compile(r"\.qa-split\.v(\d+)\.json$")


def parse_version(path: Path) -> int:
    m = VERSION_RE_NEW.search(path.name) or VERSION_RE_OLD.search(path.name)
    if not m:
        raise ValueError(f"no vN qa-split json in filename: {path.name}")
    return int(m.group(1))


def main() -> int:
    files = sorted(
        set(SPLITTER_DIR.glob("**/*.v*.qa-split.json"))
        | set(SPLITTER_DIR.glob("**/*.qa-split.v*.json"))
    )
    if not files:
        print(f"no qa-split json files in {SPLITTER_DIR}", file=sys.stderr)
        return 1

    latest_per_source: dict[str, tuple[int, Path, dict]] = {}
    for f in files:
        version = parse_version(f)
        with f.open(encoding="utf-8") as fp:
            data = json.load(fp)
        source_id = data.get("source_id")
        if not source_id:
            print(f"WARN: {f.name} has no source_id, skipping", file=sys.stderr)
            continue
        prev = latest_per_source.get(source_id)
        if prev is None or version > prev[0]:
            latest_per_source[source_id] = (version, f, data)

    flat_items: list[dict] = []
    per_source_hard: Counter[str] = Counter()
    skipped_zero_hard: list[str] = []

    for source_id, (version, path, data) in sorted(latest_per_source.items()):
        items = data.get("items", [])
        hard_items = [i for i in items if i.get("question_type") == "hard"]
        if not hard_items:
            skipped_zero_hard.append(f"{source_id} (v{version})")
            continue
        per_source_hard[source_id] = len(hard_items)
        for item in hard_items:
            enriched = {"source_id": source_id, **item}
            flat_items.append(enriched)

    out = {
        "split_strategy": "по source_id (см. md/train.md §Обучение)",
        "items": flat_items,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", encoding="utf-8") as fp:
        json.dump(out, fp, ensure_ascii=False, indent=2)
        fp.write("\n")

    print("=" * 60, file=sys.stderr)
    print(f"written: {OUT_PATH.relative_to(REPO_ROOT)}", file=sys.stderr)
    print(f"total hard items: {len(flat_items)}", file=sys.stderr)
    print(f"sources with hard items: {len(per_source_hard)}", file=sys.stderr)
    for source_id, n in sorted(per_source_hard.items()):
        print(f"  {source_id:60s} {n:3d}", file=sys.stderr)
    if skipped_zero_hard:
        print(f"skipped (0 hard items): {len(skipped_zero_hard)}", file=sys.stderr)
        for s in skipped_zero_hard:
            print(f"  {s}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
