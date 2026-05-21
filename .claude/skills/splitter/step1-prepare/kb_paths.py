"""Knowledge base paths for the splitter pipeline (post repo restructure, 2026-05).

Canonical layout:
  data/knowledgebase/raw/       — interview transcripts (input)
  data/knowledgebase/splitted/  — splitter artifacts (output)

Legacy roots ``transcripts/`` and ``splitter_output/`` are still accepted as CLI
arguments and remapped to the canonical tree when the legacy path is missing.
"""

from __future__ import annotations

from pathlib import Path

STEP1_DIR = Path(__file__).resolve().parent
SKILL_DIR = STEP1_DIR.parent
REPO_ROOT = SKILL_DIR.parents[2]

KB_ROOT = REPO_ROOT / "data" / "knowledgebase"
KB_RAW = KB_ROOT / "raw"
KB_SPLITTED = KB_ROOT / "splitted"

LEGACY_TRANSCRIPTS = REPO_ROOT / "transcripts"
LEGACY_SPLITTER_OUTPUT = REPO_ROOT / "splitter_output"

_KIND_PREFIXES = ("mock-", "real-")


def strip_kind_prefix(name: str) -> str:
    """Remove mock-/real- from leaf folder names (kind is in the parent folder)."""
    for prefix in _KIND_PREFIXES:
        if name.startswith(prefix):
            return name[len(prefix) :]
    return name


def artifact_basename(folder: Path) -> str:
    return strip_kind_prefix(folder.name)


def interview_rel_from_folder(folder: Path) -> Path:
    """Relative path under raw corpus: mock-interviews/<pub>/<basename>."""
    folder = folder.resolve()
    for base in (KB_RAW, LEGACY_TRANSCRIPTS):
        base = base.resolve()
        try:
            rel = folder.relative_to(base)
            parts = list(rel.parts)
            if parts:
                parts[-1] = strip_kind_prefix(parts[-1])
            return Path(*parts)
        except ValueError:
            continue
    kind = "mock-interviews" if folder.name.startswith("mock-") else "real-interviews"
    return Path(kind) / "unknown" / artifact_basename(folder)


def splitted_dir_for_interview(folder: Path) -> Path:
    return KB_SPLITTED / interview_rel_from_folder(folder)


def resolve_interview_folder(arg: str) -> Path:
    """Resolve --folder to an existing directory (canonical or legacy path)."""
    candidates: list[Path] = []
    p = Path(arg)
    if p.is_absolute():
        candidates.append(p)
    else:
        candidates.append(REPO_ROOT / arg)
        if arg.startswith("transcripts/"):
            candidates.append(KB_RAW / arg[len("transcripts/") :])
    seen: set[Path] = set()
    for c in candidates:
        c = c.resolve()
        if c in seen:
            continue
        seen.add(c)
        if c.is_dir():
            return c
    raise FileNotFoundError(arg)


def canonical_interview_folder_arg(folder: Path) -> str:
    """Repo-relative POSIX path for manifests (always under data/knowledgebase/raw/)."""
    rel = interview_rel_from_folder(folder)
    return (KB_RAW / rel).relative_to(REPO_ROOT).as_posix()


def remap_legacy_repo_path(path_str: str) -> str:
    """Rewrite legacy transcripts/ or splitter_output/ prefixes in stored strings."""
    if path_str.startswith("transcripts/"):
        return (KB_RAW / path_str[len("transcripts/") :]).relative_to(REPO_ROOT).as_posix()
    if path_str.startswith("splitter_output/"):
        return (KB_SPLITTED / path_str[len("splitter_output/") :]).relative_to(
            REPO_ROOT
        ).as_posix()
    return path_str
