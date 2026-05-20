#!/usr/bin/env python3
"""Rename run/validation artifacts and merge *.llm-input.txt into pipeline-log.md."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL = REPO / ".claude/skills" / "splitter"
sys.path.insert(0, str(SKILL))

from artifact_paths import legacy_to_new_name  # noqa: E402
from run_manifest import set_llm_input_section  # noqa: E402

_RE_VER = re.compile(r"\.v(\d+)\.")


def _basename_version(path: Path) -> tuple[str, int] | None:
    m = _RE_VER.search(path.name)
    if not m:
        return None
    slug = path.name[: m.start()]
    return slug, int(m.group(1))


def merge_llm_input(slug: str, ver: int, parent: Path, *, dry_run: bool) -> None:
    llm_legacy = parent / f"{slug}.v{ver}.llm-input.txt"
    llm_old = parent / f"{slug}.qa-split.llm-input.v{ver}.txt"
    llm_path = llm_legacy if llm_legacy.exists() else llm_old
    if not llm_path.exists():
        return

    pl_md = parent / f"{slug}.v{ver}.pipeline-log.md"
    run_md = parent / f"{slug}.v{ver}.run.md"
    if not pl_md.exists() and run_md.exists():
        if dry_run:
            print(f"would copy run.md -> pipeline-log.md: {run_md.name}")
        else:
            pl_md.write_text(run_md.read_text(encoding="utf-8"), encoding="utf-8")

    if not pl_md.exists():
        print(f"SKIP merge (no pipeline-log.md): {llm_path.name}", file=sys.stderr)
        return

    body = llm_path.read_text(encoding="utf-8")
    if dry_run:
        print(f"would merge LLM step 2 into: {pl_md.name} from {llm_path.name}")
        return
    set_llm_input_section(pl_md, 2, "Шаг 2 — извлечение Q&A", body)
    print(f"merged step 2 LLM input: {llm_path.name} -> {pl_md.name}")
    llm_path.unlink()


def update_run_json_keys(path: Path, *, dry_run: bool) -> None:
    if not path.exists():
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    arts = data.get("artifacts") or {}
    mapping = {
        "validation_md": "validation_report_md",
        "validation_llm_json": "validation_semantic_json",
        "llm_input": None,
        "user_prompt": None,
        "run_json": "pipeline_log_json",
        "run_md": "pipeline_log_md",
    }
    changed = False
    new_arts = {}
    for k, v in arts.items():
        nk = mapping.get(k, k)
        if nk is None:
            changed = True
            continue
        if nk != k:
            changed = True
        p = (
            v.replace(".validation.md", ".validation-report.md")
            .replace(".validation.llm.json", ".validation-semantic.json")
            .replace(".run.json", ".pipeline-log.json")
            .replace(".run.md", ".pipeline-log.md")
            .replace(".llm-input.txt", ".pipeline-log.md")
        )
        new_arts[nk] = p
    if changed:
        data["artifacts"] = new_arts
        if dry_run:
            print(f"would update artifact keys in {path.name}")
        else:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(REPO / "splitter_output"))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(args.root)
    renamed = 0
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        dest = legacy_to_new_name(path)
        if dest is None or dest == path:
            continue
        if dest.exists() and dest != path:
            continue
        if args.dry_run:
            print(f"would rename: {path.relative_to(REPO)} -> {dest.relative_to(REPO)}")
        else:
            path.rename(dest)
            print(f"renamed: {path.name} -> {dest.name}")
        renamed += 1

    seen: set[tuple[str, int, str]] = set()
    for path in sorted(root.rglob("*.llm-input.txt")) + sorted(root.rglob("*.qa-split.llm-input.v*.txt")):
        parsed = _basename_version(path)
        if not parsed:
            continue
        slug, ver = parsed
        key = (str(path.parent), ver, slug)
        if key in seen:
            continue
        seen.add(key)
        merge_llm_input(slug, ver, path.parent, dry_run=args.dry_run)

    for pl_json in root.rglob("*.pipeline-log.json"):
        update_run_json_keys(pl_json, dry_run=args.dry_run)
    for run_json in root.rglob("*.run.json"):
        update_run_json_keys(run_json, dry_run=args.dry_run)

    print(f"Done. renamed={renamed} dry_run={args.dry_run}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
