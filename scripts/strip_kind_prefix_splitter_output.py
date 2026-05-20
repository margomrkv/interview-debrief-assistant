#!/usr/bin/env python3
"""Drop mock-/real- from leaf folder and file names under splitter_output/.

Top-level mock-interviews/ and real-interviews/ stay. Transcripts/ paths unchanged.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "splitter_output"
KIND_PREFIXES = ("mock-", "real-")


def strip_kind_prefix(name: str) -> str:
    for prefix in KIND_PREFIXES:
        if name.startswith(prefix):
            return name[len(prefix) :]
    return name


def rename_files_in_dir(directory: Path, old_slug: str, new_slug: str, dry_run: bool) -> int:
    n = 0
    if old_slug == new_slug:
        return 0
    for path in sorted(directory.iterdir()):
        if not path.is_file():
            continue
        if path.name.startswith(old_slug):
            dest = path.with_name(path.name.replace(old_slug, new_slug, 1))
            n += 1
            if dry_run:
                print(f"  file: {path.name} -> {dest.name}")
            else:
                path.rename(dest)
        elif old_slug in path.read_text(encoding="utf-8", errors="replace"):
            text = path.read_text(encoding="utf-8")
            new_text = text.replace(old_slug, new_slug)
            if new_text != text:
                n += 1
                if dry_run:
                    print(f"  patch refs in: {path.name}")
                else:
                    path.write_text(new_text, encoding="utf-8")
    return n


def migrate_leaf(directory: Path, dry_run: bool) -> bool:
    old_slug = directory.name
    new_slug = strip_kind_prefix(old_slug)
    if old_slug == new_slug:
        return False

    new_dir = directory.parent / new_slug
    if new_dir.exists() and new_dir != directory:
        print(f"SKIP conflict: {directory.relative_to(REPO)} -> {new_dir.name} exists", file=sys.stderr)
        return False

    print(f"{'[dry]' if dry_run else 'OK'} {directory.relative_to(REPO)} -> .../{new_slug}/")
    rename_files_in_dir(directory, old_slug, new_slug, dry_run)
    if not dry_run:
        directory.rename(new_dir)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not OUT.exists():
        print(f"ERROR: {OUT} not found", file=sys.stderr)
        return 1

    changed = 0
    for corpus in ("mock-interviews", "real-interviews"):
        root = OUT / corpus
        if not root.exists():
            continue
        for publisher_dir in sorted(root.iterdir()):
            if not publisher_dir.is_dir():
                continue
            for leaf in sorted(publisher_dir.iterdir()):
                if not leaf.is_dir():
                    continue
                if migrate_leaf(leaf, args.dry_run):
                    changed += 1

    verb = "would rename" if args.dry_run else "renamed"
    print(f"{verb} {changed} interview folders under {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
