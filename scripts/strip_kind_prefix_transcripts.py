#!/usr/bin/env python3
"""Remove mock-/real- prefix from leaf folder names under transcripts/mock|real-interviews/."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TRANSCRIPTS = REPO / "transcripts"
ALIASES = TRANSCRIPTS / "aliases.yaml"
KIND_PREFIXES = ("mock-", "real-")


def strip_kind_prefix(name: str) -> str:
    for prefix in KIND_PREFIXES:
        if name.startswith(prefix):
            return name[len(prefix) :]
    return name


def strip_kind_source_id(source_id: str) -> str:
    if source_id.startswith("mock_"):
        return source_id[5:]
    if source_id.startswith("real_"):
        return source_id[5:]
    return source_id


def strip_path_leaf(rel_path: str) -> str:
    parts = rel_path.replace("\\", "/").split("/")
    if len(parts) >= 3 and parts[0] in ("mock-interviews", "real-interviews"):
        parts[-1] = strip_kind_prefix(parts[-1])
    return "/".join(parts)


def migrate_transcript_dirs(dry_run: bool) -> int:
    changed = 0
    for corpus in ("mock-interviews", "real-interviews"):
        root = TRANSCRIPTS / corpus
        if not root.exists():
            continue
        for publisher_dir in sorted(root.iterdir()):
            if not publisher_dir.is_dir() or publisher_dir.name.startswith("."):
                continue
            for leaf in sorted(publisher_dir.iterdir()):
                if not leaf.is_dir():
                    continue
                new_name = strip_kind_prefix(leaf.name)
                if new_name == leaf.name:
                    continue
                dest = leaf.parent / new_name
                if dest.exists():
                    print(f"SKIP conflict: {leaf.relative_to(REPO)}", file=sys.stderr)
                    continue
                print(f"{'[dry]' if dry_run else 'OK'} {leaf.relative_to(REPO)} -> .../{new_name}/")
                if not dry_run:
                    leaf.rename(dest)
                changed += 1
    return changed


def migrate_aliases(dry_run: bool) -> None:
    if not ALIASES.exists():
        return
    raw = ALIASES.read_text(encoding="utf-8")
    text = re.sub(r"(mock-interviews/[^/\n]+/)mock-", r"\1", raw)
    text = re.sub(r"(real-interviews/[^/\n]+/)real-", r"\1", text)
    if dry_run:
        print(f"[dry] would update {ALIASES.relative_to(REPO)}")
        return
    ALIASES.write_text("# Last updated: 2026-05-19\n\n" + text.lstrip(), encoding="utf-8")
    print(f"updated {ALIASES.relative_to(REPO)}")


def migrate_source_ids_in_json(root: Path, dry_run: bool) -> int:
    n = 0
    for path in sorted(root.rglob("*.json")):
        if ".qa-split.v" not in path.name:
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        sid = data.get("source_id")
        if not sid or not isinstance(sid, str):
            continue
        new_sid = strip_kind_source_id(sid)
        if new_sid == sid:
            continue
        data["source_id"] = new_sid
        n += 1
        if not dry_run:
            path.write_text(
                json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
    return n


def patch_text_paths(root: Path, dry_run: bool) -> int:
    """Fix transcript paths in validation reports etc."""
    n = 0
    patterns = [
        (re.compile(r"(transcripts/mock-interviews/[^/\s]+/)mock-"), r"\1"),
        (re.compile(r"(transcripts/real-interviews/[^/\s]+/)real-"), r"\1"),
        (re.compile(r"(splitter_output/mock-interviews/[^/\s]+/)mock-"), r"\1"),
        (re.compile(r"(splitter_output/real-interviews/[^/\s]+/)real-"), r"\1"),
    ]
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in {".md", ".txt", ".json"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        new_text = text
        for pat, repl in patterns:
            new_text = pat.sub(repl, new_text)
        if new_text != text:
            n += 1
            if not dry_run:
                path.write_text(new_text, encoding="utf-8")
    return n


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-aliases", action="store_true")
    parser.add_argument("--skip-json", action="store_true")
    args = parser.parse_args()

    n_dirs = migrate_transcript_dirs(args.dry_run)
    if not args.skip_aliases:
        migrate_aliases(args.dry_run)
    n_json = 0 if args.skip_json else migrate_source_ids_in_json(REPO / "splitter_output", args.dry_run)
    n_text = 0
    for sub in (TRANSCRIPTS, REPO / "splitter_output", REPO / ".claude", REPO / "md"):
        if sub.exists():
            n_text += patch_text_paths(sub, args.dry_run)

    print(
        f"summary: {n_dirs} dirs, {n_json} json source_ids, {n_text} text files "
        f"({'dry-run' if args.dry_run else 'applied'})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
