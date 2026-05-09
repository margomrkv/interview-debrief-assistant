"""
validate_splitter_vs_video.py

Cross-validates a splitter JSON output against the YouTube video.md file
(chapters list). video.md is used ONLY for validation — it must not be
present in the splitter run context.

Usage:
    python labeling/validate_splitter_vs_video.py \
        --splitter labeling/data/karpov_junior_ds_20220330.splitter.v3.mock.json \
        --video transcripts/karpov-courses-собеседования/junior-data-scientist-собеседование-karpov-courses-20220330/video.md \
        [--tolerance 90] \
        [--section-config labeling/config/karpov_section_map.json] \
        [--out labeling/data/karpov_junior_ds_20220330.splitter.v3.mock.validation.md]

--section-config (optional) JSON file with keys:
  {
    "section_timecodes": {"Section Name": "HH:MM:SS", ...},
    "topic_map": {"Section Name": ["Topic1", "Topic2"], ...}
  }
If omitted, section assignment and topic-consistency check are skipped;
only coverage (did the splitter find every question chapter?) is reported.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


# ─── Section → accepted question_topic values ────────────────────────────────
# Loaded from --section-config at runtime; defaults to empty (topic check skipped).
# See labeling/config/karpov_section_map.json for the karpov interview config.

_DEFAULT_SECTION_TOPIC_MAP: dict[str, list[str]] = {}
_DEFAULT_SECTION_TIMECODES: dict[str, str] = {}

# Prefixes/keywords that mark an explanation or transition chapter, not a question
EXPLANATION_PREFIXES = (
    # Generic
    "Введение",
    "О структуре",
    "Объяснение",
    "Разбор",
    "Подводка к",
    "Интерпретация",
    "Конец",
    "Конец,",
    "Какие еще",
    "Общие рассуждения",
    # Stream/interview framing
    "Начало",
    "Приветствие",
    "Представление",
    "Завершение",
    "Комментирование",
    "Зачем задаем",
    "Фидбек",
    "Обратная связь",
)


# ─── Data structures ──────────────────────────────────────────────────────────

@dataclass
class Chapter:
    time_sec: int
    time_str: str
    title: str
    section: Optional[str] = None
    is_question: bool = False


@dataclass
class SplitterItem:
    index: int          # 1-based
    q_time_str: Optional[str]
    q_time_sec: Optional[int]
    question_topic: Optional[str]
    question_type: Optional[str]
    interview_stage: Optional[str]
    q_text_preview: str


@dataclass
class MatchResult:
    chapter: Chapter
    item: Optional[SplitterItem] = None
    drift_sec: Optional[int] = None
    topic_ok: Optional[bool] = None
    topic_allowed: Optional[list] = None   # list of accepted topic values for this section
    topic_actual: Optional[str] = None


# ─── Parsers ──────────────────────────────────────────────────────────────────

def _ts_to_sec(ts: str) -> int:
    """Convert HH:MM:SS or MM:SS to total seconds."""
    parts = ts.strip().split(":")
    parts = [int(p) for p in parts]
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    return int(parts[0])


def _sec_to_ts(sec: int) -> str:
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def parse_video_md(
    path: Path,
    section_timecodes: dict[str, str] | None = None,
) -> list[Chapter]:
    """Parse chapters from video.md, assign sections, classify questions.

    section_timecodes: mapping of section name → "HH:MM:SS" string.
    If None or empty, section assignment is skipped (all chapters get section=None).
    """
    text = path.read_text(encoding="utf-8")

    # Extract the ## Chapters block (stop at ## Description or end)
    chapters_block_match = re.search(r"## Chapters\n(.*?)(?:\n## |\Z)", text, re.DOTALL)
    if not chapters_block_match:
        raise ValueError(f"No '## Chapters' section found in {path}")

    chapters_block = chapters_block_match.group(1)

    # Build sorted section boundaries (sec_name → start_seconds)
    resolved_timecodes: dict[str, int] = {}
    for sec_name, ts_str in (section_timecodes or {}).items():
        resolved_timecodes[sec_name] = _ts_to_sec(ts_str)
    sorted_sections = sorted(resolved_timecodes.items(), key=lambda x: x[1])

    chapters: list[Chapter] = []
    pattern = re.compile(r"-\s+\[(\d{2}:\d{2}:\d{2})\]\s+(.+)")
    for line in chapters_block.splitlines():
        m = pattern.match(line.strip())
        if not m:
            continue
        ts, title = m.group(1), m.group(2).strip()
        sec = _ts_to_sec(ts)

        # Assign section
        section = None
        for sec_name, sec_start in reversed(sorted_sections):
            if sec >= sec_start:
                section = sec_name
                break

        # Classify as question vs. explanation
        is_question = not any(title.startswith(p) for p in EXPLANATION_PREFIXES)

        chapters.append(Chapter(
            time_sec=sec,
            time_str=ts,
            title=title,
            section=section,
            is_question=is_question,
        ))

    return chapters


def parse_splitter_json(path: Path) -> list[SplitterItem]:
    data = json.loads(path.read_text(encoding="utf-8"))
    items: list[SplitterItem] = []
    for i, it in enumerate(data.get("items", []), start=1):
        q = it.get("interviewer_question") or {}
        q_time = q.get("time")
        q_text = (q.get("text") or "")[:80].replace("\n", " ")
        items.append(SplitterItem(
            index=i,
            q_time_str=q_time,
            q_time_sec=_ts_to_sec(q_time) if q_time else None,
            question_topic=it.get("question_topic"),
            question_type=it.get("question_type"),
            interview_stage=it.get("interview_stage"),
            q_text_preview=q_text,
        ))
    return items


# ─── Matching ─────────────────────────────────────────────────────────────────

def match_chapters_to_items(
    chapters: list[Chapter],
    items: list[SplitterItem],
    tolerance_sec: int,
    section_topic_map: dict[str, list[str]] | None = None,
) -> list[MatchResult]:
    """
    For each question chapter, find the closest splitter item within tolerance.
    Each item can be matched to at most one chapter.

    Uses a global drift-sorted greedy strategy: consider all (chapter, item) pairs
    within tolerance, sort by drift ascending, then assign closest pairs first.
    This avoids the sequential greedy problem where an earlier chapter "steals" an
    item that would be a perfect match for a later chapter.

    section_topic_map: mapping of section name → allowed question_topic values.
    If None or empty, topic consistency check is skipped for all items.
    """
    topic_map = section_topic_map or {}
    question_chapters = [c for c in chapters if c.is_question]

    # Build all candidate pairs within tolerance, sorted by drift ascending
    candidates: list[tuple[int, Chapter, SplitterItem]] = []  # (drift, chapter, item)
    for ch in question_chapters:
        for item in items:
            if item.q_time_sec is None:
                continue
            drift = abs(item.q_time_sec - ch.time_sec)
            if drift <= tolerance_sec:
                candidates.append((drift, ch, item))
    candidates.sort(key=lambda x: x[0])

    # Greedy assignment: smallest drift first
    assigned_chapters: set[int] = set()  # chapter.time_sec used as key
    used_item_indices: set[int] = set()
    assignments: dict[int, tuple[SplitterItem, int]] = {}  # chapter.time_sec → (item, drift)

    for drift, ch, item in candidates:
        if ch.time_sec in assigned_chapters:
            continue
        if item.index in used_item_indices:
            continue
        assigned_chapters.add(ch.time_sec)
        used_item_indices.add(item.index)
        assignments[ch.time_sec] = (item, drift)

    # Build MatchResult list in chapter order
    results: list[MatchResult] = []
    for ch in question_chapters:
        result = MatchResult(chapter=ch)
        if ch.time_sec in assignments:
            best_item, best_drift = assignments[ch.time_sec]
            result.item = best_item
            result.drift_sec = best_drift

            # Topic check: pass if actual topic is in the allowed list for this section
            allowed_topics = topic_map.get(ch.section) if ch.section else None
            actual_topic = best_item.question_topic
            result.topic_allowed = allowed_topics
            result.topic_actual = actual_topic
            if allowed_topics is not None:
                result.topic_ok = (actual_topic in allowed_topics)

        results.append(result)

    return results


def find_unmatched_items(
    items: list[SplitterItem],
    match_results: list[MatchResult],
) -> list[SplitterItem]:
    matched_indices = {r.item.index for r in match_results if r.item is not None}
    return [it for it in items if it.index not in matched_indices]


def build_section_breakdown(
    match_results: list[MatchResult],
    unmatched_items: list[SplitterItem],
    all_chapters: list[Chapter],
) -> list[dict]:
    """
    For each section, compute:
      - video_q_count: number of question chapters in that section (from video.md)
      - splitter_count: number of matched splitter items + unmatched items whose time
        falls within that section's range
      - topics: set of question_topic values found in the splitter items
      - missing_chapters: question chapters with no matched item
    """
    # Section time boundaries derived from all chapters (sorted)
    section_starts = sorted(
        {c.section: c.time_sec for c in all_chapters if c.section}.items(),
        key=lambda x: x[1],
    )
    # Build ordered list of (section, start_sec, end_sec)
    section_ranges: list[tuple[str, int, int]] = []
    for i, (sec_name, start) in enumerate(section_starts):
        end = section_starts[i + 1][1] if i + 1 < len(section_starts) else 999999
        section_ranges.append((sec_name, start, end))

    def sec_for_time(t: int) -> str | None:
        for sec_name, start, end in reversed(section_ranges):
            if t >= start:
                return sec_name
        return None

    # Count question chapters per section
    section_video_q: dict[str, list[Chapter]] = {s: [] for s, _, _ in section_ranges}
    for ch in all_chapters:
        if ch.is_question and ch.section:
            section_video_q.setdefault(ch.section, []).append(ch)

    # Matched splitter items per section
    section_matched: dict[str, list[SplitterItem]] = {s: [] for s, _, _ in section_ranges}
    section_missing: dict[str, list[Chapter]] = {s: [] for s, _, _ in section_ranges}
    for r in match_results:
        sec = r.chapter.section
        if not sec:
            continue
        if r.item:
            section_matched.setdefault(sec, []).append(r.item)
        else:
            section_missing.setdefault(sec, []).append(r.chapter)

    # Unmatched splitter items — assign to section by time
    section_unmatched_extra: dict[str, list[SplitterItem]] = {s: [] for s, _, _ in section_ranges}
    for it in unmatched_items:
        if it.q_time_sec is not None:
            sec = sec_for_time(it.q_time_sec)
            if sec:
                section_unmatched_extra.setdefault(sec, []).append(it)

    rows = []
    for sec_name, _, _ in section_ranges:
        video_qs = section_video_q.get(sec_name, [])
        matched = section_matched.get(sec_name, [])
        extra = section_unmatched_extra.get(sec_name, [])
        missing = section_missing.get(sec_name, [])
        all_splitter = matched + extra
        topics = sorted({it.question_topic for it in all_splitter if it.question_topic})
        rows.append({
            "section": sec_name,
            "video_q_count": len(video_qs),
            "splitter_count": len(all_splitter),
            "delta": len(all_splitter) - len(video_qs),
            "topics": topics,
            "missing_chapters": missing,
        })
    return rows


# ─── Report ───────────────────────────────────────────────────────────────────

def build_report(
    match_results: list[MatchResult],
    unmatched_items: list[SplitterItem],
    all_chapters: list[Chapter],
    section_rows: list[dict],
    splitter_path: Path,
    video_path: Path,
    tolerance_sec: int,
    section_topic_map: dict[str, list[str]] | None = None,
) -> str:
    lines: list[str] = []

    total_q_chapters = len(match_results)
    matched = sum(1 for r in match_results if r.item is not None)
    topic_checks = [r for r in match_results if r.topic_ok is not None]
    topic_ok_count = sum(1 for r in topic_checks if r.topic_ok)
    drifts = [r.drift_sec for r in match_results if r.drift_sec is not None]
    avg_drift = sum(drifts) / len(drifts) if drifts else None
    max_drift = max(drifts) if drifts else None

    lines.append("# Splitter Validation Report\n")
    lines.append(f"- **splitter**: `{splitter_path}`")
    lines.append(f"- **video.md**: `{video_path}`")
    lines.append(f"- **tolerance**: ±{tolerance_sec}s\n")

    # ── How it works ──────────────────────────────────────────────────────────
    lines.append("## How this validation works\n")
    lines.append(
        "The validator uses `video.md` as a **ground-truth checklist** of what questions "
        "the video actually contains. `video.md` is the YouTube chapter list — it was written "
        "by the video authors independently of the transcript, so it is a clean external signal.\n"
    )
    lines.append("**Step 1 — Parse video chapters.**")
    lines.append(
        "Every line in the `## Chapters` block is extracted as a chapter: timestamp + title. "
        "Chapters whose titles start with words like \"Разбор\", \"Объяснение\", \"Подводка к\", etc. "
        "are classified as *explanations/transitions* and excluded from the question checklist. "
        "Only chapters that represent actual interview questions are kept.\n"
    )
    lines.append("**Step 2 — Match splitter items to chapters.**")
    lines.append(
        f"For each question chapter, the validator looks for the splitter item whose "
        f"`interviewer_question.time` is closest in time, within a ±{tolerance_sec}s window. "
        "The window is generous because chapter timestamps mark the *start of a topic segment*, "
        "while the splitter records the exact moment the interviewer starts speaking — these can "
        "differ by tens of seconds. Each splitter item can be matched to at most one chapter.\n"
    )
    lines.append("**Step 3 — Coverage % (the main quality signal).**")
    lines.append(
        "```\nCoverage = matched question chapters / total question chapters × 100\n```\n"
        "A chapter is 'matched' if a splitter item was found within the time window. "
        "Coverage = 100% means every question the video authors marked was found by the splitter. "
        "A missing chapter means the splitter skipped that question entirely.\n"
    )
    topic_map = section_topic_map or {}
    lines.append("**Step 4 — Topic consistency %.**")
    if topic_map:
        lines.append(
            "```\nTopic consistency = items with correct question_topic / all matched items with a known section × 100\n```\n"
            "For each matched item the validator checks that `question_topic` in the JSON is in the "
            "allowed set for the section that chapter belongs to:\n"
        )
        for sec, allowed in topic_map.items():
            lines.append(f"- Section **{sec}** → allowed topics: {allowed}")
        lines.append(
            "\nNote: one section can allow multiple topics. "
            "\"A/B-тесты\" accepts both `Experimentation` (experiment-design questions) and "
            "`Statistics` (t-test, normality, bootstrap questions) because both types appear "
            "in that section.\n"
        )
    else:
        lines.append(
            "_No `--section-config` provided — topic consistency check is skipped for this interview. "
            "Only coverage is validated._\n"
        )
    lines.append("**Step 5 — Unmatched splitter items.**")
    lines.append(
        "Some splitter items are NOT matched to any video chapter. This is expected and "
        "not penalised. The video authors only marked top-level topic segments; the splitter "
        "also captures follow-up sub-questions and interviewer clarifications that have no "
        "dedicated chapter. These are listed for manual review, not counted as errors.\n"
    )

    # ── Summary ───────────────────────────────────────────────────────────────
    lines.append("## Summary\n")
    lines.append("| Metric | Value | Meaning |")
    lines.append("|--------|-------|---------|")
    lines.append(
        f"| Question chapters in video.md | {total_q_chapters} | "
        "Ground-truth checklist size |"
    )
    lines.append(
        f"| Matched to splitter item | {matched} / {total_q_chapters} | "
        f"Splitter found a matching item within ±{tolerance_sec}s |"
    )
    lines.append(
        f"| **Coverage** | **{matched/total_q_chapters*100:.0f}%** | "
        "Main signal: did the splitter extract every question? |"
    )
    lines.append(
        f"| Unmatched question chapters | {total_q_chapters - matched} | "
        "Questions in video that splitter missed |"
    )
    lines.append(
        f"| Unmatched splitter items | {len(unmatched_items)} | "
        "Sub-questions / follow-ups extracted by splitter; no chapter in video — not an error |"
    )
    lines.append(
        f"| **Topic consistency** | **{topic_ok_count}/{len(topic_checks)} "
        f"({topic_ok_count/len(topic_checks)*100:.0f}%)** | "
        "question_topic label matches the video section |"
        if topic_checks else
        f"| Topic consistency | — | No section mapping available |"
    )
    if avg_drift is not None:
        lines.append(
            f"| Avg timing drift | {avg_drift:.1f}s | "
            "Mean |item time − chapter time| for matched pairs |"
        )
        lines.append(
            f"| Max timing drift | {max_drift}s | "
            "Worst-case match; still within tolerance |"
        )
    lines.append("")

    # ── Section breakdown ─────────────────────────────────────────────────────
    lines.append("## Section Breakdown\n")
    lines.append(
        "Compares the number of questions per section according to the video (ground truth) "
        "vs. the number of items the splitter extracted. Delta = splitter − video "
        "(positive = splitter found sub-questions beyond what video marked; "
        "negative = splitter missed questions).\n"
    )
    lines.append("| Section | Video Qs | Splitter items | Delta | Splitter topics |")
    lines.append("|---------|----------|----------------|-------|-----------------|")
    for row in section_rows:
        delta = row["delta"]
        delta_str = f"+{delta}" if delta > 0 else str(delta)
        delta_icon = "✅" if delta >= 0 else "❌"
        topics_str = ", ".join(f"`{t}`" for t in row["topics"]) if row["topics"] else "—"
        lines.append(
            f"| {row['section']} | {row['video_q_count']} | {row['splitter_count']} "
            f"| {delta_icon} {delta_str} | {topics_str} |"
        )
    lines.append("")

    # Missing per section
    any_missing = any(row["missing_chapters"] for row in section_rows)
    if any_missing:
        lines.append("### Missing questions by section\n")
        for row in section_rows:
            if row["missing_chapters"]:
                lines.append(f"**{row['section']}**\n")
                for ch in row["missing_chapters"]:
                    lines.append(f"- `{ch.time_str}` {ch.title}")
                lines.append("")

    # ── Chapter-by-chapter ────────────────────────────────────────────────────
    lines.append("## Chapter-by-Chapter Matching\n")
    lines.append(
        "Drift = `item time − chapter time` (positive = splitter item is later than chapter marker).\n"
    )
    lines.append("| # | Chapter time | Chapter title | Section | Item # | Item time | Drift | Topic |")
    lines.append("|---|-------------|---------------|---------|--------|-----------|-------|-------|")

    for i, r in enumerate(match_results, start=1):
        ch = r.chapter
        if r.item:
            item_no = f"#{r.item.index}"
            item_time = r.item.q_time_str or "—"
            raw_drift = (r.item.q_time_sec or 0) - ch.time_sec
            drift_s = f"{raw_drift:+d}s"
            if r.topic_ok is True:
                topic_cell = f"✅ `{r.topic_actual}`"
            elif r.topic_ok is False:
                allowed_str = " / ".join(f"`{t}`" for t in (r.topic_allowed or []))
                topic_cell = f"❌ got `{r.topic_actual}`, allowed: {allowed_str}"
            else:
                topic_cell = f"`{r.topic_actual}`"
        else:
            item_no = "❌ MISSING"
            item_time = "—"
            drift_s = "—"
            topic_cell = "—"

        lines.append(
            f"| {i} | `{ch.time_str}` | {ch.title[:52]} | {ch.section or '—'} "
            f"| {item_no} | {item_time} | {drift_s} | {topic_cell} |"
        )

    lines.append("")

    # ── Unmatched splitter items ───────────────────────────────────────────────
    if unmatched_items:
        lines.append("## Unmatched Splitter Items\n")
        lines.append(
            "These items were extracted by the splitter but have **no corresponding chapter** "
            "in `video.md`. This is **not an error** — the video authors only marked major topic "
            "transitions, not every follow-up question. Review these to confirm they are legitimate "
            "sub-questions or interviewer clarifications rather than hallucinated content.\n"
        )
        lines.append("| Item # | Time | Topic | Question (first 70 chars) |")
        lines.append("|--------|------|-------|--------------------------|")
        for it in unmatched_items:
            lines.append(
                f"| #{it.index} | {it.q_time_str or '—'} | `{it.question_topic or '—'}` "
                f"| {it.q_text_preview[:70]} |"
            )
        lines.append("")

    # ── Skipped chapters ──────────────────────────────────────────────────────
    non_q = [c for c in all_chapters if not c.is_question]
    if non_q:
        lines.append("## Skipped Chapters (explanations / transitions)\n")
        lines.append(
            "Chapters excluded from the question checklist because their titles indicate "
            "they contain an explanation, task walkthrough, or segment transition rather than "
            "a new interview question. These are not checked for splitter coverage.\n"
        )
        for c in non_q:
            lines.append(f"- `{c.time_str}` [{c.section or '—'}] {c.title}")
        lines.append("")

    # ── Verdict ───────────────────────────────────────────────────────────────
    coverage_pct = matched / total_q_chapters * 100 if total_q_chapters else 0
    topic_pct = topic_ok_count / len(topic_checks) * 100 if topic_checks else 100
    if coverage_pct >= 90 and topic_pct >= 90:
        verdict = "✅ PASS"
    elif coverage_pct >= 70 and topic_pct >= 70:
        verdict = "⚠️ PARTIAL — review flagged items"
    else:
        verdict = "❌ FAIL — significant coverage or topic issues"

    lines.append(f"## Verdict: {verdict}\n")
    lines.append(
        f"**Coverage** {coverage_pct:.0f}% = {matched} out of {total_q_chapters} question chapters "
        f"were found by the splitter within ±{tolerance_sec}s.  \n"
        f"**Topic consistency** {topic_pct:.0f}% = {topic_ok_count} out of {len(topic_checks)} "
        f"matched items have a `question_topic` label that matches the video section."
    )

    return "\n".join(lines) + "\n"


# ─── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Validate splitter JSON output against YouTube video.md chapters."
    )
    parser.add_argument("--splitter", required=True, help="Path to splitter output JSON")
    parser.add_argument("--video", required=True, help="Path to video.md")
    parser.add_argument(
        "--tolerance", type=int, default=90,
        help="Max allowed timing drift in seconds for a match (default: 90)"
    )
    parser.add_argument(
        "--section-config",
        help=(
            "Optional JSON file with section timecodes and topic map. "
            "Keys: 'section_timecodes' (name→HH:MM:SS) and 'topic_map' (name→[topics]). "
            "If omitted, section assignment and topic check are skipped."
        ),
    )
    parser.add_argument("--out", help="Write report to this .md file (default: print to stdout)")
    args = parser.parse_args()

    splitter_path = Path(args.splitter)
    video_path = Path(args.video)

    if not splitter_path.exists():
        print(f"ERROR: splitter file not found: {splitter_path}", file=sys.stderr)
        sys.exit(1)
    if not video_path.exists():
        print(f"ERROR: video.md not found: {video_path}", file=sys.stderr)
        sys.exit(1)

    # Load optional section config
    section_timecodes: dict[str, str] = {}
    section_topic_map: dict[str, list[str]] = {}
    if args.section_config:
        cfg_path = Path(args.section_config)
        if not cfg_path.exists():
            print(f"ERROR: section-config not found: {cfg_path}", file=sys.stderr)
            sys.exit(1)
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
        section_timecodes = cfg.get("section_timecodes", {})
        section_topic_map = cfg.get("topic_map", {})

    chapters = parse_video_md(video_path, section_timecodes=section_timecodes)
    items = parse_splitter_json(splitter_path)
    match_results = match_chapters_to_items(chapters, items, args.tolerance, section_topic_map)
    unmatched_items = find_unmatched_items(items, match_results)
    section_rows = build_section_breakdown(match_results, unmatched_items, chapters)

    report = build_report(
        match_results, unmatched_items, chapters, section_rows,
        splitter_path, video_path, args.tolerance,
        section_topic_map=section_topic_map,
    )

    if args.out:
        out_path = Path(args.out)
        out_path.write_text(report, encoding="utf-8")
        print(f"Report written to: {out_path}")
    else:
        print(report)


if __name__ == "__main__":
    main()
