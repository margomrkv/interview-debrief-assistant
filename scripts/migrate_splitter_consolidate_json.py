#!/usr/bin/env python3
"""Merge pipeline-log.json → pipeline-log.md and validation-semantic.json → validation-report.md."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL = REPO / ".claude/skills" / "splitter"
sys.path.insert(0, str(SKILL))
sys.path.insert(0, str(SKILL / "step4-validate-chapters"))

from run_manifest import load_run, save_run  # noqa: E402
from splitter_validate_chapters import save_semantic_json_to_report  # noqa: E402


def merge_pipeline_log_json(path: Path, *, dry_run: bool) -> bool:
    md = path.with_suffix(".md")
    if not path.exists():
        return False
    if dry_run:
        print(f"would merge manifest: {path.name} -> {md.name}")
        return True
    run = json.loads(path.read_text(encoding="utf-8"))
    slug = run.get("basename") or md.name.split(".v")[0]
    ver = run.get("version") or int(md.name.split(".v")[1].split(".")[0])
    parent = md.parent
    run["artifacts"] = {
        "json": str(parent / f"{slug}.v{ver}.qa-split.json"),
        "xlsx": str(parent / f"{slug}.v{ver}.qa-split.xlsx"),
        "validation_report_md": str(parent / f"{slug}.v{ver}.validation-report.md"),
        "pipeline_log_md": str(md.relative_to(REPO)),
    }
    save_run(run, md)
    path.unlink()
    print(f"merged pipeline log: {path.name} -> {md.name}")
    return True


def merge_semantic_json(path: Path, *, dry_run: bool) -> bool:
    if not path.exists():
        return False
    stem = path.name.replace(".validation-semantic.json", "").replace(".validation.llm.json", "")
    report = path.parent / f"{stem}.validation-report.md"
    if not report.exists():
        report = path.parent / f"{stem}.validation.md"
    if not report.exists():
        print(f"SKIP (no report): {path.name}", file=sys.stderr)
        return False
    if dry_run:
        print(f"would embed semantic JSON: {path.name} -> {report.name}")
        return True
    data = json.loads(path.read_text(encoding="utf-8"))
    save_semantic_json_to_report(report, data)
    path.unlink()
    print(f"embedded semantic: {path.name} -> {report.name}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(REPO / "splitter_output"))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    root = Path(args.root)
    n_pl = n_sem = 0
    for p in sorted(root.rglob("*.pipeline-log.json")) + sorted(root.rglob("*.run.json")):
        if merge_pipeline_log_json(p, dry_run=args.dry_run):
            n_pl += 1
    for p in sorted(root.rglob("*.validation-semantic.json")) + sorted(
        root.rglob("*.validation.llm.json")
    ):
        if merge_semantic_json(p, dry_run=args.dry_run):
            n_sem += 1
    print(f"Done. pipeline_logs={n_pl} semantic={n_sem} dry_run={args.dry_run}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
