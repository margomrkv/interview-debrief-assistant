"""Read evaluator-prompt artifacts (runs/<run_id>/evaluator_prompt.md).

The artifact begins with a YAML-ish frontmatter block (run metadata) followed
by the prompt body. `load_prompt_artifact` strips the frontmatter and returns
the body usable as `signature.with_instructions(...)` text.
"""
from __future__ import annotations

from pathlib import Path


def _strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end == -1:
        return text
    return text[end + 4 :].lstrip("\n")


def load_prompt_artifact(path: Path) -> str:
    return _strip_frontmatter(path.read_text())
