#!/usr/bin/env python3
"""
Extract per-item transcript windows from timecodes.txt for feedback enrichment.

Usage:
    python labeling/extract_feedback_windows.py \
        --json labeling/data/karpov_ml_sysdesign_v2_20210828.splitter.v1.mock.json \
        --timecodes <path-to-timecodes.txt>

Outputs a structured view: for each Q&A item, shows the transcript segment
between its timestamp and the next item's timestamp. Use this to identify
interviewer feedback/corrections and fill in `interviewer_feedback`.
"""

import argparse
import json
import re
import sys
from pathlib import Path


def ts_to_sec(ts: str) -> int:
    """Parse [HH:MM:SS] or [MM:SS] to seconds."""
    ts = ts.strip("[]")
    parts = ts.split(":")
    if len(parts) == 3:
        h, m, s = parts
        return int(h) * 3600 + int(m) * 60 + int(s)
    elif len(parts) == 2:
        m, s = parts
        return int(m) * 60 + int(s)
    return 0


def sec_to_hms(sec: int) -> str:
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def load_timecodes(path: Path) -> list[tuple[int, str]]:
    """Return list of (seconds, text) from timecodes.txt."""
    pattern = re.compile(r"^\[(\d{1,2}:\d{2}(?::\d{2})?)\]\s*(.*)")
    lines = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        m = pattern.match(raw.strip())
        if m:
            sec = ts_to_sec(m.group(1))
            text = m.group(2).strip()
            if text:
                lines.append((sec, text))
    return lines


def extract_window(
    timecodes: list[tuple[int, str]],
    start_sec: int,
    end_sec: int,
    margin_before: int = 15,
) -> str:
    """Extract transcript lines between start and end seconds."""
    lines = []
    for sec, text in timecodes:
        if (start_sec - margin_before) <= sec < end_sec:
            lines.append(f"[{sec_to_hms(sec)}] {text}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", required=True, help="Path to splitter JSON")
    parser.add_argument("--timecodes", required=True, help="Path to timecodes.txt")
    parser.add_argument(
        "--margin", type=int, default=15,
        help="Seconds before item timestamp to include (default 15)"
    )
    parser.add_argument(
        "--output", default=None,
        help="Output file (default: stdout)"
    )
    args = parser.parse_args()

    json_path = Path(args.json)
    tc_path = Path(args.timecodes)

    if not json_path.exists():
        print(f"ERROR: JSON not found: {json_path}", file=sys.stderr)
        sys.exit(1)
    if not tc_path.exists():
        print(f"ERROR: timecodes.txt not found: {tc_path}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(json_path.read_text(encoding="utf-8"))
    items = data.get("items", [])
    timecodes = load_timecodes(tc_path)

    max_sec = timecodes[-1][0] if timecodes else 0

    out_lines = []
    out_lines.append(f"# Feedback windows: {json_path.name}")
    out_lines.append(f"# Timecodes: {tc_path}")
    out_lines.append(f"# {len(items)} items | transcript {sec_to_hms(max_sec)}")
    out_lines.append("")

    for i, item in enumerate(items):
        q = item.get("interviewer_question", {})
        a = item.get("candidate_answer", {})
        q_time_str = q.get("time", "00:00:00")
        q_text = (q.get("text") or "")[:120]
        topic = item.get("question_topic", "—")
        existing_fb = item.get("interviewer_feedback", {})
        has_fb = existing_fb and existing_fb.get("text")

        q_sec = ts_to_sec(q_time_str)

        # End = next item's q_time, or end of transcript
        if i + 1 < len(items):
            next_q = items[i + 1].get("interviewer_question", {})
            next_ts = next_q.get("time", "99:99:99")
            end_sec = ts_to_sec(next_ts)
        else:
            end_sec = max_sec + 1

        window = extract_window(timecodes, q_sec, end_sec, margin_before=args.margin)

        out_lines.append("=" * 70)
        out_lines.append(f"ITEM #{i+1}  [{q_time_str}]  topic={topic}")
        out_lines.append(f"Q: {q_text}")
        out_lines.append(f"FEEDBACK currently: {'✅ filled' if has_fb else '⬜ null'}")
        out_lines.append("")
        out_lines.append("--- TRANSCRIPT WINDOW ---")
        if window:
            out_lines.append(window)
        else:
            out_lines.append("(no lines found in this window)")
        out_lines.append("")

    result = "\n".join(out_lines)

    if args.output:
        Path(args.output).write_text(result, encoding="utf-8")
        print(f"Written to {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
