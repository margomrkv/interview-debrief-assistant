"""Canonical splitted artifact names: {basename}.v{N}.{artifact}.{ext}

Artifacts live under ``data/knowledgebase/splitted/`` (see ``kb_paths.py``).

Version comes right after basename so `ls *v8*` groups one run.
Legacy names are still parsed for version detection and migration.
"""

from __future__ import annotations

import re
from pathlib import Path

# ── Canonical naming (2026-05) ───────────────────────────────────────────────
# {basename}.v{N}.qa-split.json | .xlsx
# {basename}.v{N}.validation-report.md  (semantic step-5 JSON embedded at end)
# {basename}.v{N}.pipeline-log.md       (manifest comment + journal + LLM inputs)

_RE_NEW_JSON = re.compile(r"^(?P<slug>.+)\.v(?P<ver>\d+)\.qa-split\.json$")
_RE_OLD_JSON = re.compile(r"^(?P<slug>.+)\.qa-split\.v(?P<ver>\d+)\.json$")


def paths_for_run(output_dir: Path, basename: str, version: int) -> dict[str, Path]:
    """All standard artifact paths for one version."""
    v = version
    b = basename
    d = output_dir
    return {
        "json": d / f"{b}.v{v}.qa-split.json",
        "xlsx": d / f"{b}.v{v}.qa-split.xlsx",
        "validation_report_md": d / f"{b}.v{v}.validation-report.md",
        "pipeline_log_md": d / f"{b}.v{v}.pipeline-log.md",
    }


def parse_json_path(path: Path) -> tuple[str, int] | None:
    """Return (basename, version) from a qa-split JSON path (new or legacy)."""
    m = _RE_NEW_JSON.match(path.name) or _RE_OLD_JSON.match(path.name)
    if not m:
        return None
    return m.group("slug"), int(m.group("ver"))


def validation_report_from_json(json_path: Path) -> Path:
    parsed = parse_json_path(json_path)
    if parsed:
        slug, ver = parsed
        parent = json_path.parent
        new = parent / f"{slug}.v{ver}.validation-report.md"
        if new.exists():
            return new
        legacy = parent / f"{slug}.v{ver}.validation.md"
        if legacy.exists():
            return legacy
        return new
    return json_path.with_name(
        re.sub(r"\.qa-split\.v(\d+)\.json$", r".qa-split.validation.v\1.md", json_path.name)
    )


# Back-compat alias
validation_md_from_json = validation_report_from_json


def validation_semantic_json_from_report(report_md: Path) -> Path:
    """Legacy sidecar path (migration only). Canonical storage is inside report .md."""
    m = re.match(r"^(?P<base>.+)\.v(?P<n>\d+)\.validation-report\.md$", report_md.name)
    if m:
        return report_md.parent / f"{m.group('base')}.v{m.group('n')}.validation-semantic.json"
    m = re.match(r"^(?P<base>.+)\.v(?P<n>\d+)\.validation\.md$", report_md.name)
    if m:
        parent = report_md.parent
        for name in (
            f"{m.group('base')}.v{m.group('n')}.validation-semantic.json",
            f"{m.group('base')}.v{m.group('n')}.validation.llm.json",
        ):
            p = parent / name
            if p.exists():
                return p
        return parent / f"{m.group('base')}.v{m.group('n')}.validation-semantic.json"
    return report_md.with_suffix(".semantic.json")


validation_llm_json_from_validation_md = validation_semantic_json_from_report


def pipeline_log_md_from_json(json_path: Path) -> Path:
    parsed = parse_json_path(json_path)
    if parsed:
        slug, ver = parsed
        parent = json_path.parent
        md = parent / f"{slug}.v{ver}.pipeline-log.md"
        if md.exists():
            return md
        legacy = parent / f"{slug}.v{ver}.pipeline-log.json"
        if legacy.exists():
            return md
        run_legacy = parent / f"{slug}.v{ver}.run.json"
        if run_legacy.exists():
            return md
        return md
    return json_path.with_name(json_path.stem + ".pipeline-log.md")


pipeline_log_json_from_report = pipeline_log_md_from_json  # back-compat alias


def xlsx_from_json(json_path: Path) -> Path:
    parsed = parse_json_path(json_path)
    if parsed:
        slug, ver = parsed
        return json_path.parent / f"{slug}.v{ver}.qa-split.xlsx"
    return json_path.with_suffix(".xlsx")


def next_version(output_dir: Path, basename: str) -> int:
    """Next vN from existing JSON artifacts (new or legacy names)."""
    used: set[int] = set()
    for pattern in (
        f"{basename}.v*.qa-split.json",
        f"{basename}.qa-split.v*.json",
    ):
        for f in output_dir.glob(pattern):
            p = parse_json_path(f)
            if p and p[0] == basename:
                used.add(p[1])
    return 1 if not used else max(used) + 1


def legacy_to_new_name(path: Path) -> Path | None:
    """Map one legacy filename to canonical scheme (same parent dir)."""
    name = path.name
    m = re.match(r"^(?P<slug>.+)\.qa-split\.v(?P<ver>\d+)\.json$", name)
    if m:
        return path.parent / f"{m.group('slug')}.v{m.group('ver')}.qa-split.json"
    m = re.match(r"^(?P<slug>.+)\.qa-split\.v(?P<ver>\d+)\.xlsx$", name)
    if m:
        return path.parent / f"{m.group('slug')}.v{m.group('ver')}.qa-split.xlsx"
    m = re.match(r"^(?P<slug>.+)\.qa-split\.validation\.v(?P<ver>\d+)\.md$", name)
    if m:
        return path.parent / f"{m.group('slug')}.v{m.group('ver')}.validation-report.md"
    m = re.match(r"^(?P<slug>.+)\.v(?P<ver>\d+)\.validation\.md$", name)
    if m:
        return path.parent / f"{m.group('slug')}.v{m.group('ver')}.validation-report.md"
    m = re.match(r"^(?P<slug>.+)\.qa-split\.validation\.llm\.v(?P<ver>\d+)\.json$", name)
    if m:
        return path.parent / f"{m.group('slug')}.v{m.group('ver')}.validation-semantic.json"
    m = re.match(r"^(?P<slug>.+)\.v(?P<ver>\d+)\.validation\.llm\.json$", name)
    if m:
        return None  # content moves into validation-report.md
    m = re.match(r"^(?P<slug>.+)\.v(?P<ver>\d+)\.validation-semantic\.json$", name)
    if m:
        return None
    m = re.match(r"^(?P<slug>.+)\.v(?P<ver>\d+)\.pipeline-log\.json$", name)
    if m:
        return None  # manifest moves into pipeline-log.md
    m = re.match(r"^(?P<slug>.+)\.qa-split\.llm-input\.v(?P<ver>\d+)\.txt$", name)
    if m:
        return None  # content moves into pipeline-log.md
    m = re.match(r"^(?P<slug>.+)\.v(?P<ver>\d+)\.llm-input\.txt$", name)
    if m:
        return None
    m = re.match(r"^(?P<slug>.+)\.v(?P<ver>\d+)\.run\.json$", name)
    if m:
        return None
    m = re.match(r"^(?P<slug>.+)\.v(?P<ver>\d+)\.run\.md$", name)
    if m:
        return path.parent / f"{m.group('slug')}.v{m.group('ver')}.pipeline-log.md"
    return None
