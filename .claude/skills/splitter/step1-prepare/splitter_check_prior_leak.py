#!/usr/bin/env python3
"""Fail if qa-split JSON duplicates a prior version (anti copy-paste guard).

Exit codes:
  0 — ok (differs from all v1..v(N-1) or empty stub)
  1 — leak detected (identical items fingerprint to an older version)
  2 — usage / read error
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from splitter_no_prior_versions import check_prior_leak


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "json",
        type=Path,
        help="Path to {basename}.vN.qa-split.json for the current run",
    )
    args = parser.parse_args()
    path = args.json.resolve()
    if not path.is_file():
        print(f"ERROR: not found: {path}", file=sys.stderr)
        return 2

    ok, msg = check_prior_leak(path)
    if ok:
        print("OK: no prior-version leak detected")
        return 0
    print(f"PRIOR_VERSION_LEAK: {msg}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
