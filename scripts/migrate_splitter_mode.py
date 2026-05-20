#!/usr/bin/env python3
"""Replace legacy splitter_mode values in splitter_output artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SPLITTER_OUTPUT = REPO_ROOT / "splitter_output"

REPLACEMENTS = (
    ("mock_assisted_split", "split_and_validate"),
    ("raw_split", "split_only"),
)
MAPPING = dict(REPLACEMENTS)

TEXT_SUFFIXES = {".json", ".txt", ".md"}


def migrate_text(content: str) -> tuple[str, int]:
    n = 0
    for old, new in REPLACEMENTS:
        count = content.count(old)
        if count:
            content = content.replace(old, new)
            n += count
    return content, n


def migrate_json(path: Path, dry_run: bool) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    mode = data.get("splitter_mode")
    if mode not in MAPPING:
        return 0
    data["splitter_mode"] = MAPPING[mode]
    if not dry_run:
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return 1


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=SPLITTER_OUTPUT)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root: Path = args.root
    if not root.exists():
        print(f"ERROR: not found: {root}", file=sys.stderr)
        sys.exit(1)

    files_changed = 0
    replacements = 0

    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue

        if path.suffix == ".json" and ".qa-split.v" in path.name:
            try:
                n = migrate_json(path, args.dry_run)
            except json.JSONDecodeError:
                text = path.read_text(encoding="utf-8")
                new_text, n = migrate_text(text)
                if n and not args.dry_run:
                    path.write_text(new_text, encoding="utf-8")
            if n:
                files_changed += 1
                replacements += n
            continue

        text = path.read_text(encoding="utf-8")
        new_text, n = migrate_text(text)
        if n:
            replacements += n
            files_changed += 1
            if not args.dry_run:
                path.write_text(new_text, encoding="utf-8")

    verb = "would update" if args.dry_run else "updated"
    print(f"{verb} {files_changed} files ({replacements} value replacements) under {root}")


if __name__ == "__main__":
    main()
