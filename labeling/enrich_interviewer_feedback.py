#!/usr/bin/env python3
"""
Enrich interviewer_feedback in existing splitter JSON files
using verbatim ASR text from timecodes.txt.

Strategy:
  1. ML SysDesign interviews: use explicit "комментарий" chapters from video.md
     to pinpoint the feedback window for each Q&A item.
  2. All other interviews: extract the last 90s of the window between candidate
     answer time and next item's question time. If the tail window is < 20s, skip.

Does NOT re-run the splitter or validation.
Regenerates .xlsx after updating JSON.

Usage:
    python labeling/enrich_interviewer_feedback.py [--dry-run] [--json <glob>]
"""

import argparse
import glob
import json
import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent.parent  # repo root

# ── Manual mapping overrides for multi-candidate interviews or non-standard dates ──
MANUAL_TIMECODES: dict[str, str] = {
    # sasha and yegor share one directory for 20210913
    "junior_аналитик_данных_собеседование_karpov_courses_20210913_sasha": (
        "transcripts/karpov-courses-собеседования/"
        "junior-аналитик-данных-собеседование-karpov-courses-20210913/timecodes.txt"
    ),
    "junior_аналитик_данных_собеседование_karpov_courses_20210913_yegor": (
        "transcripts/karpov-courses-собеседования/"
        "junior-аналитик-данных-собеседование-karpov-courses-20210913/timecodes.txt"
    ),
    # pasha and vyacheslav share one directory for 20210624
    "karpov_product_analyst_junior_20210624_pasha": (
        "transcripts/karpov-courses-собеседования/"
        "аналитик-данных-собеседование-karpov-courses-20210624/timecodes.txt"
    ),
    "karpov_product_analyst_junior_vyacheslav_20210624": (
        "transcripts/karpov-courses-собеседования/"
        "аналитик-данных-собеседование-karpov-courses-20210624/timecodes.txt"
    ),
    # avito is in a different base directory
    "avito_product_analyst_middle_20240404": (
        "transcripts/mock-avito-product-analyst-middle-2024-04-04/timecodes.txt"
    ),
}

MANUAL_VIDEOMDS: dict[str, str] = {
    k: v.replace("timecodes.txt", "video.md") for k, v in MANUAL_TIMECODES.items()
}


# ────────────────────────── helpers ──────────────────────────

TS_RE = re.compile(r"^\[(\d{1,2}:\d{2}(?::\d{2})?)\]\s*(.*)")


def ts_to_sec(ts: str) -> int:
    ts = ts.strip("[]")
    parts = ts.split(":")
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    return int(parts[0]) * 60 + int(parts[1])


def sec_to_hms(sec: int) -> str:
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def load_timecodes(path: Path) -> list[tuple[int, str]]:
    lines = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        m = TS_RE.match(raw.strip())
        if m:
            sec = ts_to_sec(m.group(1))
            text = m.group(2).strip()
            if text:
                lines.append((sec, text))
    return lines


def extract_window_text(
    timecodes: list[tuple[int, str]], start_sec: int, end_sec: int
) -> tuple[str, str | None]:
    """Return (verbatim_text, first_timestamp_str) for lines in [start_sec, end_sec)."""
    lines = []
    first_ts = None
    for sec, text in timecodes:
        if start_sec <= sec < end_sec:
            if first_ts is None:
                first_ts = sec_to_hms(sec)
            lines.append(text)
    return " ".join(lines), first_ts


def load_chapters(video_md: Path) -> list[tuple[int, str]]:
    """Return (seconds, chapter_title) pairs from video.md ## Chapters section."""
    if not video_md.exists():
        return []
    content = video_md.read_text(encoding="utf-8")
    # Find ## Chapters block
    m = re.search(r"##\s*Chapters\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if not m:
        return []
    chapters = []
    for line in m.group(1).splitlines():
        cm = re.match(r"\s*-\s*\[(\d{1,2}:\d{2}(?::\d{2})?)\]\s*(.*)", line)
        if cm:
            chapters.append((ts_to_sec(cm.group(1)), cm.group(2).strip()))
    return chapters


COMMENT_PATTERN = re.compile(
    r"(комментари|comment|замечани|пять копеек|обратная связь|ос от|feedback)",
    re.IGNORECASE,
)


def find_feedback_chapter(
    chapters: list[tuple[int, str]], item_q_sec: int, next_q_sec: int
) -> tuple[int, int] | None:
    """
    Find a 'комментарий' chapter between item_q_sec and next_q_sec.
    Returns (comment_start_sec, comment_end_sec) or None.
    """
    comment_windows = []
    for i, (sec, title) in enumerate(chapters):
        if item_q_sec <= sec < next_q_sec and COMMENT_PATTERN.search(title):
            # end of this chapter = start of next chapter (or next_q_sec)
            end = next_q_sec
            for j in range(i + 1, len(chapters)):
                if chapters[j][0] > sec:
                    end = min(chapters[j][0], next_q_sec)
                    break
            comment_windows.append((sec, end))
    if not comment_windows:
        return None
    # Merge all comment windows into one span
    start = comment_windows[0][0]
    end = comment_windows[-1][1]
    return start, end


def auto_find_timecodes(json_stem: str) -> Path | None:
    """Find timecodes.txt by date matching in karpov-courses-собеседования."""
    m = re.search(r"(\d{8})", json_stem)
    if not m:
        return None
    date = m.group(1)
    pattern = str(
        BASE / "transcripts" / "karpov-courses-собеседования" / f"*{date}*" / "timecodes.txt"
    )
    matches = glob.glob(pattern)
    return Path(matches[0]) if matches else None


def auto_find_video_md(json_stem: str) -> Path | None:
    m = re.search(r"(\d{8})", json_stem)
    if not m:
        return None
    date = m.group(1)
    pattern = str(
        BASE / "transcripts" / "karpov-courses-собеседования" / f"*{date}*" / "video.md"
    )
    matches = glob.glob(pattern)
    return Path(matches[0]) if matches else None


# ────────────────────────── core ──────────────────────────

def enrich_file(json_path: Path, dry_run: bool = False) -> dict:
    """
    Returns a summary dict with stats about what was added.
    """
    stem = json_path.stem.replace(".splitter.v1.mock", "")

    # Resolve timecodes / video.md paths
    if stem in MANUAL_TIMECODES:
        tc_path = BASE / MANUAL_TIMECODES[stem]
        vm_path = BASE / MANUAL_VIDEOMDS.get(stem, "")
    else:
        tc_path = auto_find_timecodes(stem) or Path("__not_found__")
        vm_path = auto_find_video_md(stem) or Path("__not_found__")

    if not tc_path.exists():
        return {"file": json_path.name, "status": "SKIP (no timecodes.txt)", "filled": 0, "skipped": 0}

    timecodes = load_timecodes(tc_path)
    if not timecodes:
        return {"file": json_path.name, "status": "SKIP (empty timecodes)", "filled": 0, "skipped": 0}

    chapters = load_chapters(vm_path) if vm_path.exists() else []
    max_sec = timecodes[-1][0]

    data = json.loads(json_path.read_text(encoding="utf-8"))
    items = data.get("items", [])

    filled = 0
    skipped_no_content = 0
    skipped_already = 0

    for i, item in enumerate(items):
        fb = item.get("interviewer_feedback", {})
        if fb and fb.get("text"):
            skipped_already += 1
            continue  # already populated, don't overwrite

        q_time = item.get("interviewer_question", {}).get("time", "00:00:00")
        q_sec = ts_to_sec(q_time)

        # Next item's question start (or end of transcript)
        if i + 1 < len(items):
            next_q_time = items[i + 1].get("interviewer_question", {}).get("time", "99:99:99")
            next_q_sec = ts_to_sec(next_q_time)
        else:
            next_q_sec = max_sec + 1

        # ── Strategy 1: look for explicit "комментарий" chapter ──
        feedback_window = None
        if chapters:
            feedback_window = find_feedback_chapter(chapters, q_sec, next_q_sec)

        # ── Strategy 2: take tail of the item window (last 90s before next Q) ──
        if feedback_window is None:
            window_len = next_q_sec - q_sec
            TAIL = 90  # seconds
            MIN_WINDOW = 20  # skip if too short
            if window_len > MIN_WINDOW:
                tail_start = max(q_sec, next_q_sec - TAIL)
                feedback_window = (tail_start, next_q_sec)

        if feedback_window is None:
            skipped_no_content += 1
            continue

        fb_text, fb_time = extract_window_text(timecodes, feedback_window[0], feedback_window[1])
        fb_text = fb_text.strip()

        # Sanity: skip if essentially empty
        if not fb_text or len(fb_text) < 20:
            skipped_no_content += 1
            continue

        item["interviewer_feedback"] = {"text": fb_text, "time": fb_time or q_time}
        filled += 1

    result = {
        "file": json_path.name,
        "status": "OK",
        "filled": filled,
        "skipped_already": skipped_already,
        "skipped_no_content": skipped_no_content,
    }

    if not dry_run and filled > 0:
        json_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        # Regenerate xlsx
        xlsx_script = BASE / "labeling" / "splitter_json_to_excel.py"
        if xlsx_script.exists():
            subprocess.run(
                [sys.executable, str(xlsx_script), str(json_path)],
                capture_output=True,
                cwd=str(BASE),
            )

    return result


# ────────────────────────── main ──────────────────────────

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Don't write files")
    parser.add_argument(
        "--json",
        default="labeling/data/*.splitter.v1.mock.json",
        help="Glob for JSON files to process",
    )
    args = parser.parse_args()

    json_files = sorted(glob.glob(str(BASE / args.json)))
    if not json_files:
        print("No JSON files found.")
        sys.exit(1)

    print(f"Processing {len(json_files)} files {'(DRY RUN)' if args.dry_run else ''}\n")

    total_filled = 0
    for jf in json_files:
        res = enrich_file(Path(jf), dry_run=args.dry_run)
        status_icon = "✅" if res["status"] == "OK" and res["filled"] > 0 else (
            "⏩" if res["status"] == "OK" and res.get("skipped_already", 0) > 0 else "⬜"
        )
        print(
            f"{status_icon} {res['file']}\n"
            f"   status={res['status']}  filled={res.get('filled',0)}  "
            f"already_had={res.get('skipped_already',0)}  "
            f"no_content={res.get('skipped_no_content',0)}"
        )
        total_filled += res.get("filled", 0)

    print(f"\n── Total items enriched: {total_filled} ──")


if __name__ == "__main__":
    main()
