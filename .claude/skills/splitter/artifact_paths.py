"""Canonical splitter_output artifact names: {basename}.v{N}.{artifact}.{ext}

Version comes right after basename so `ls *v8*` groups one run.
Legacy names (*.qa-split.vN.*) are still parsed for version detection and migration.
"""

from __future__ import annotations

import re
from pathlib import Path

# ── New naming (canonical) ─────────────────────────────────────────────────────
# {basename}.v{N}.qa-split.json | .xlsx
# {basename}.v{N}.validation.md | .validation.llm.json
# {basename}.v{N}.llm-input.txt | .user-prompt.txt
# {basename}.v{N}.run.json | .run.md

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
        "validation_md": d / f"{b}.v{v}.validation.md",
        "validation_llm_json": d / f"{b}.v{v}.validation.llm.json",
        "llm_input": d / f"{b}.v{v}.llm-input.txt",
        "user_prompt": d / f"{b}.v{v}.user-prompt.txt",
        "run_json": d / f"{b}.v{v}.run.json",
        "run_md": d / f"{b}.v{v}.run.md",
    }


def parse_json_path(path: Path) -> tuple[str, int] | None:
    """Return (basename, version) from a qa-split JSON path (new or legacy)."""
    m = _RE_NEW_JSON.match(path.name) or _RE_OLD_JSON.match(path.name)
    if not m:
        return None
    return m.group("slug"), int(m.group("ver"))


def validation_md_from_json(json_path: Path) -> Path:
    parsed = parse_json_path(json_path)
    if parsed:
        slug, ver = parsed
        return json_path.parent / f"{slug}.v{ver}.validation.md"
    # fallback legacy
    return json_path.with_name(
        re.sub(r"\.qa-split\.v(\d+)\.json$", r".qa-split.validation.v\1.md", json_path.name)
    )


def validation_llm_json_from_validation_md(validation_md: Path) -> Path:
    m = re.match(r"^(?P<base>.+)\.v(?P<n>\d+)\.validation\.md$", validation_md.name)
    if m:
        return validation_md.parent / f"{m.group('base')}.v{m.group('n')}.validation.llm.json"
    m = re.match(r"^(?P<base>.+)\.qa-split\.validation\.v(?P<n>\d+)\.md$", validation_md.name)
    if m:
        return validation_md.parent / f"{m.group('base')}.v{m.group('n')}.validation.llm.json"
    return validation_md.with_suffix(".llm.json")


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
    """Map one legacy filename to new scheme (same parent dir)."""
    name = path.name
    m = re.match(r"^(?P<slug>.+)\.qa-split\.v(?P<ver>\d+)\.json$", name)
    if m:
        return path.parent / f"{m.group('slug')}.v{m.group('ver')}.qa-split.json"
    m = re.match(r"^(?P<slug>.+)\.qa-split\.v(?P<ver>\d+)\.xlsx$", name)
    if m:
        return path.parent / f"{m.group('slug')}.v{m.group('ver')}.qa-split.xlsx"
    m = re.match(r"^(?P<slug>.+)\.qa-split\.validation\.v(?P<ver>\d+)\.md$", name)
    if m:
        return path.parent / f"{m.group('slug')}.v{m.group('ver')}.validation.md"
    m = re.match(r"^(?P<slug>.+)\.qa-split\.validation\.llm\.v(?P<ver>\d+)\.json$", name)
    if m:
        return path.parent / f"{m.group('slug')}.v{m.group('ver')}.validation.llm.json"
    m = re.match(r"^(?P<slug>.+)\.qa-split\.llm-input\.v(?P<ver>\d+)\.txt$", name)
    if m:
        return path.parent / f"{m.group('slug')}.v{m.group('ver')}.llm-input.txt"
    m = re.match(r"^(?P<slug>.+)\.qa-split\.user-prompt\.v(?P<ver>\d+)\.txt$", name)
    if m:
        return path.parent / f"{m.group('slug')}.v{m.group('ver')}.user-prompt.txt"
    return None
