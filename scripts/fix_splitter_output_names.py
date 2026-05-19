#!/usr/bin/env python3
"""Repair .qa-split.prompt.json/.xlsx → .qa-split.vN.json/.xlsx from botched first migration pass."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "splitter_output"

WRONG_JSON = re.compile(r"^(?P<slug>.+)\.qa-split\.prompt\.json$")
WRONG_XLSX = re.compile(r"^(?P<slug>.+)\.qa-split\.prompt\.xlsx$")

# slug → version for duplicate junior DS v5 artifacts
V5_SLUG = "mock-data-scientist-junior-karpov-2022-03-30"


def main() -> int:
    fixed = 0
    for path in OUT.rglob("*.qa-split.prompt.json"):
        m = WRONG_JSON.match(path.name)
        if not m:
            continue
        slug = m.group("slug")
        ver = 5 if slug == V5_SLUG else 1
        dest = path.parent / f"{slug}.qa-split.v{ver}.json"
        if dest.exists():
            path.unlink()
            print(f"removed duplicate wrong json: {path.relative_to(REPO)}")
        else:
            path.rename(dest)
            print(f"renamed → {dest.relative_to(REPO)}")
        fixed += 1

    for path in OUT.rglob("*.qa-split.prompt.xlsx"):
        m = WRONG_XLSX.match(path.name)
        if not m:
            continue
        slug = m.group("slug")
        ver = 5 if slug == V5_SLUG else 1
        dest = path.parent / f"{slug}.qa-split.v{ver}.xlsx"
        if dest.exists():
            path.unlink()
        else:
            path.rename(dest)
        print(f"renamed xlsx → {dest.relative_to(REPO)}")
        fixed += 1

    print(f"fixed: {fixed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
