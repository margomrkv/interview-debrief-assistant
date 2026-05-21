#!/usr/bin/env python3
"""Read overall verdict from {basename}.vN.validation-report.md (step 4).

Exit codes for agent retry loop:
  0 — ✅ ПРОЙДЕНО
  1 — ❌ НЕ ПРОЙДЕНО (or unknown)
  2 — ⚠️ ЧАСТИЧНО

Also prints unrecognized chapter count when --chapters is set.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


_VERDICT_RE = re.compile(
    r"^#{2,3}\s*(?:Вердикт|Verdict):\s*(.+)$",
    re.MULTILINE,
)
_UNREC_RE = re.compile(
    r"❌\s*(?:не\s*распознан|not\s*recognized)",
    re.IGNORECASE,
)


def parse_verdict(text: str) -> str | None:
    m = _VERDICT_RE.search(text)
    return m.group(1).strip() if m else None


def verdict_exit_code(verdict: str) -> int:
    v = verdict.upper()
    if "✅" in verdict and ("ПРОЙДЕНО" in verdict or "PASSED" in v):
        return 0
    if "⚠️" in verdict or "ЧАСТИЧНО" in verdict or "PARTIAL" in v:
        return 2
    return 1


def count_unrecognized(text: str) -> int:
    return len(_UNREC_RE.findall(text))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="Path to *.validation-report.md")
    parser.add_argument(
        "--chapters",
        action="store_true",
        help="Print count of 'не распознан' markers to stderr",
    )
    args = parser.parse_args()
    if not args.report.is_file():
        print(f"ERROR: not found: {args.report}", file=sys.stderr)
        sys.exit(3)

    text = args.report.read_text(encoding="utf-8")
    verdict = parse_verdict(text)
    if verdict is None:
        print("ERROR: no '### Verdict:' / '### Вердикт:' line in report", file=sys.stderr)
        sys.exit(3)

    print(verdict)
    if args.chapters:
        n = count_unrecognized(text)
        print(f"unrecognized_chapters={n}", file=sys.stderr)

    code = verdict_exit_code(verdict)
    if code != 0 and count_unrecognized(text) > 0 and code == 1:
        pass  # already failure
    sys.exit(code)


if __name__ == "__main__":
    main()
