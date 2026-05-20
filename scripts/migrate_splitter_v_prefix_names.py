#!/usr/bin/env python3
"""Rename legacy splitter artifacts to {basename}.v{N}.{artifact}.{ext} scheme."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL = REPO / ".claude/skills" / "splitter"
sys.path.insert(0, str(SKILL))

from artifact_paths import legacy_to_new_name  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        default=str(REPO / "splitter_output"),
        help="splitter_output root (default: repo/splitter_output)",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(args.root)
    renamed = 0
    skipped = 0
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        dest = legacy_to_new_name(path)
        if dest is None or dest == path:
            skipped += 1
            continue
        if dest.exists() and dest != path:
            print(f"SKIP (dest exists): {path.name} -> {dest.name}", file=sys.stderr)
            continue
        rel = path.relative_to(REPO)
        new_rel = dest.relative_to(REPO)
        if args.dry_run:
            print(f"would rename: {rel} -> {new_rel}")
        else:
            path.rename(dest)
            print(f"renamed: {rel} -> {new_rel}")
        renamed += 1
    print(f"Done. renamed={renamed} skipped={skipped} dry_run={args.dry_run}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
