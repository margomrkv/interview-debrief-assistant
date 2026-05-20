#!/usr/bin/env python3
"""One-shot reorganize transcripts/ layout (2026-05). Idempotent-ish: skips missing sources."""

from __future__ import annotations

import re
import shutil
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TRANSCRIPTS = REPO / "transcripts"

TIME_RE = re.compile(r"\[(\d{2}):(\d{2}):(\d{2})\]")


def ts_to_sec(h: int, m: int, s: int) -> int:
    return h * 3600 + m * 60 + s


def parse_ts(ts: str) -> int:
    parts = ts.strip().split(":")
    if len(parts) == 3:
        return ts_to_sec(int(parts[0]), int(parts[1]), int(parts[2]))
    if len(parts) == 2:
        return ts_to_sec(0, int(parts[0]), int(parts[1]))
    raise ValueError(ts)


def fmt_ts(sec: int) -> str:
    h, rem = divmod(max(0, sec), 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def rebase_timecodes(text: str, start_sec: int, end_sec: int) -> str:
    out: list[str] = []
    for line in text.splitlines():
        m = TIME_RE.search(line)
        if not m:
            continue
        t = ts_to_sec(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        if t < start_sec or t >= end_sec:
            continue
        new_t = t - start_sec
        new_line = TIME_RE.sub(f"[{fmt_ts(new_t)}]", line, count=1)
        out.append(new_line)
    return "\n".join(out) + ("\n" if out else "")


def timecodes_to_transcript(timecodes: str) -> str:
  parts = []
  for line in timecodes.splitlines():
    m = TIME_RE.search(line)
    if m:
      parts.append(line[m.end() :].strip())
  return " ".join(p for p in parts if p) + ("\n" if parts else "")


def split_feedback(text: str, start_sec: int, end_sec: int) -> str:
    if not text.strip():
        return ""
    blocks = re.split(r"\n(?=---\n)", text)
    kept: list[str] = []
    for block in blocks:
        if "start_seconds:" not in block:
            if kept:
                continue
            kept.append(block)
            continue
        m = re.search(r"start_seconds:\s*(\d+)", block)
        n = re.search(r"end_seconds:\s*(\d+)", block)
        if not m or not n:
            continue
        bs, be = int(m.group(1)), int(n.group(1))
        if be <= start_sec or bs >= end_sec:
            continue
        kept.append(block)
    return "\n".join(kept).strip() + ("\n" if kept else "")


def copy_video_md(src: Path, dst_video: Path, note: str) -> None:
    if not src.exists():
        return
    body = src.read_text(encoding="utf-8")
    header = (
        f"<!-- split_from: {note} -->\n"
        f"<!-- segment is a logical interview extracted from a multi-candidate recording -->\n\n"
    )
    dst_video.write_text(header + body, encoding="utf-8")


@dataclass(frozen=True)
class Segment:
    new_name: str
    start: str
    end: str
    candidate: str


def split_folder(src: Path, dest_parent: Path, segments: list[Segment]) -> list[tuple[str, str]]:
    aliases: list[tuple[str, str]] = []
    timecodes_path = src / "timecodes.txt"
    feedback_path = src / "feedback.md"
    video_path = src / "video.md"
    link_path = src / "link.txt"

    timecodes_all = timecodes_path.read_text(encoding="utf-8") if timecodes_path.exists() else ""
    feedback_all = feedback_path.read_text(encoding="utf-8") if feedback_path.exists() else ""

    for seg in segments:
        start_sec = parse_ts(seg.start)
        end_sec = parse_ts(seg.end)
        dest = dest_parent / seg.new_name
        dest.mkdir(parents=True, exist_ok=True)

        tc = rebase_timecodes(timecodes_all, start_sec, end_sec)
        (dest / "timecodes.txt").write_text(tc, encoding="utf-8")
        (dest / "transcript.txt").write_text(timecodes_to_transcript(tc), encoding="utf-8")

        fb = split_feedback(feedback_all, start_sec, end_sec)
        if fb.strip():
            (dest / "feedback.md").write_text(fb, encoding="utf-8")

        if link_path.exists():
            shutil.copy2(link_path, dest / "link.txt")
        copy_video_md(video_path, dest / "video.md", f"{src.name} [{seg.candidate}]")

        old_rel = str(src.relative_to(TRANSCRIPTS)).replace("\\", "/")
        new_rel = str(dest.relative_to(TRANSCRIPTS)).replace("\\", "/")
        aliases.append((old_rel, new_rel))

    return aliases


# (old path relative to transcripts/, new path relative to transcripts/)
# Skip duplicate аналитик-данных — merged into split of mock-karpov
MOVES: list[tuple[str, str]] = [
    # --- mock-interviews / karpov ---
    ("karpov-courses/junior-data-scientist-собеседование-karpov-courses-20220330", "mock-interviews/karpov/karpov-junior-data-scientist-20220330"),
    ("karpov-courses/junior-ml-инженер-собеседование-karpov-courses-20230309", "mock-interviews/karpov/karpov-junior-ml-engineer-20230309"),
    ("karpov-courses/middle-data-scientist-выпуск-1-секция-ml-собеседование-karpov-courses-20220626", "mock-interviews/karpov/karpov-middle-data-scientist-ml-20220626"),
    ("karpov-courses/middle-data-scientist-часть-2-секция-python-и-работы-с-данными-собеседование-karpov-courses-20220702", "mock-interviews/karpov/karpov-middle-data-scientist-python-20220702"),
    ("karpov-courses/ml-system-design-с-валерием-бабушкиным-выпуск-1-собеседование-karpov-courses-20210803", "mock-interviews/karpov/karpov-ml-system-design-v1-20210803"),
    ("karpov-courses/ml-system-design-с-валерием-бабушкиным-выпуск-2-собеседование-karpov-courses-20210828", "mock-interviews/karpov/karpov-ml-system-design-v2-20210828"),
    ("karpov-courses/ml-system-design-с-валерием-бабушкиным-выпуск-3-собеседование-karpov-courses-20210919", "mock-interviews/karpov/karpov-ml-system-design-v3-20210919"),
    ("karpov-courses/system-design-с-валерием-бабушкиным-выпуск-1-собеседование-karpov-courses-20220119", "mock-interviews/karpov/karpov-system-design-v1-20220119"),
    ("karpov-courses/system-design-с-валерием-бабушкиным-выпуск-2-собеседование-karpov-courses-20220228", "mock-interviews/karpov/karpov-system-design-v2-20220228"),
    ("karpov-courses/system-design-с-валерием-бабушкиным-выпуск-3-собеседование-karpov-courses-20220324", "mock-interviews/karpov/karpov-system-design-v3-20220324"),
    ("karpov-courses/system-design-с-валерием-бабушкиным-выпуск-4-собеседование-karpov-courses-20220505", "mock-interviews/karpov/karpov-system-design-v4-20220505"),
    ("karpov-courses/system-design-с-валерием-бабушкиным-собеседование-karpov-courses-20230714", "mock-interviews/karpov/karpov-system-design-20230714"),
    ("karpov-courses/a-b-тесты-с-валерием-бабушкиным-собеседование-karpov-courses-20240119", "mock-interviews/karpov/karpov-ab-testing-20240119"),
    ("karpov-courses/игровой-аналитик-собеседование-karpov-courses-20211120", "mock-interviews/karpov/karpov-game-analyst-20211120"),
    ("karpov-courses/поведенческое-интервью-behavioral-interview-выпуск-1-валерий-бабушкин-karpov-courses-20221110", "mock-interviews/karpov/karpov-behavioral-v1-20221110"),
    ("karpov-courses/поведенческое-интервью-behavioral-interview-выпуск-2-валерий-бабушкин-karpov-courses-20221215", "mock-interviews/karpov/karpov-behavioral-v2-20221215"),
    ("karpov-courses/поведенческое-интервью-behavioral-interview-выпуск-3-валерий-бабушкин-karpov-courses-20230121", "mock-interviews/karpov/karpov-behavioral-v3-20230121"),
    ("karpov-courses/собеседование-на-senior-аналитика-данных-валерий-бабушкин-karpov-courses-20240523", "mock-interviews/karpov/karpov-senior-data-analyst-20240523"),
    # avito
    ("mock-avito-product-analyst-middle-2024-04-04", "mock-interviews/avito/avito-middle-product-analyst-20240404"),
    # datainterview
    ("datainterview-mock/amazon-data-scientist-mock-interview-ab-testing-20220127", "mock-interviews/datainterview/amazon-data-scientist-ab-testing-20220127"),
    ("datainterview-mock/amazon-data-scientist-mock-interview-fraud-model-20220106", "mock-interviews/datainterview/amazon-data-scientist-fraud-model-20220106"),
    ("datainterview-mock/doordash-data-scientist-mock-interview-commentary-20210215", "mock-interviews/datainterview/doordash-data-scientist-commentary-20210215"),
    ("datainterview-mock/facebook-data-scientist-mock-interview-measure-user-churn-sql-problem-20210930", "mock-interviews/datainterview/facebook-data-scientist-churn-sql-20210930"),
    ("datainterview-mock/facebook-data-scientist-mock-interview-segment-influencers-20201224", "mock-interviews/datainterview/facebook-data-scientist-segment-influencers-20201224"),
    ("datainterview-mock/meta-data-scientist-mock-interview-call-suggestion-on-portal-product-metrics-ab-testing-20211126", "mock-interviews/datainterview/meta-data-scientist-call-suggestion-ab-20211126"),
    ("datainterview-mock/uber-data-scientist-mock-interview-interview-coach-ex-google-20220428", "mock-interviews/datainterview/uber-data-scientist-coach-20220428"),
    # interview-query
    ("interview-query-jay-feng-mock/amazon-business-intelligence-mock-interview-duplicate-products-20200529", "mock-interviews/interview-query/amazon-business-intelligence-duplicate-products-20200529"),
    ("interview-query-jay-feng-mock/amazon-data-engineer-mock-interview-tips-and-feedback-20200521", "mock-interviews/interview-query/amazon-data-engineer-tips-20200521"),
    ("interview-query-jay-feng-mock/amazon-sql-mock-interview-question-conversation-distribution-20220131", "mock-interviews/interview-query/amazon-sql-conversation-distribution-20220131"),
    ("interview-query-jay-feng-mock/dropbox-data-scientist-mock-interview-20210728", "mock-interviews/interview-query/dropbox-data-scientist-20210728"),
    ("interview-query-jay-feng-mock/facebook-product-investigation-mock-interview-part-1-fill-rate-20200706", "mock-interviews/interview-query/facebook-product-investigation-fill-rate-20200706"),
    ("interview-query-jay-feng-mock/google-machine-learning-system-design-mock-interview-20200826", "mock-interviews/interview-query/google-ml-system-design-20200826"),
    ("interview-query-jay-feng-mock/linkedin-data-scientist-mock-interview-feedback-with-ex-doordash-spotify-data-scientist-20200909", "mock-interviews/interview-query/linkedin-data-scientist-feedback-20200909"),
    ("interview-query-jay-feng-mock/linkedin-machine-learning-mock-interview-design-a-recommendation-engine-20210622", "mock-interviews/interview-query/linkedin-ml-recommendation-engine-20210622"),
    ("interview-query-jay-feng-mock/meta-facebook-machine-learning-mock-interview-illegal-items-detection-20220118", "mock-interviews/interview-query/meta-ml-illegal-items-20220118"),
    ("interview-query-jay-feng-mock/meta-facebook-product-sense-mock-interview-friend-requests-down-20220421", "mock-interviews/interview-query/meta-product-sense-friend-requests-20220421"),
    ("interview-query-jay-feng-mock/netflix-machine-learning-mock-interview-type-ahead-search-20200514", "mock-interviews/interview-query/netflix-ml-type-ahead-20200514"),
    ("interview-query-jay-feng-mock/think-like-a-senior-data-scientist-live-mock-interview-20260224", "mock-interviews/interview-query/verizon-senior-data-scientist-fraud-case-20260224"),
    ("interview-query-jay-feng-mock/uber-data-scientist-mock-interview-ride-requests-model-20200723", "mock-interviews/interview-query/uber-data-scientist-ride-requests-20200723"),
    ("interview-query-jay-feng-mock/walmart-data-science-case-study-mock-interview-underpricing-algorithm-20200804", "mock-interviews/interview-query/walmart-data-scientist-underpricing-20200804"),
    # interviewing.io
    ("interviewing-io-mock/design-a-centralized-ml-management-platform-system-design-interview-with-a-meta-engineer-20250603", "mock-interviews/interviewing-io/meta-ml-system-design-ml-platform-20250603"),
    ("interviewing-io-mock/design-an-a-b-experimentation-platform-ml-system-design-interview-with-a-faang-engineer-20260323", "mock-interviews/interviewing-io/faang-ml-system-design-ab-platform-20260323"),
    ("interviewing-io-mock/design-yelp-recommendations-ml-system-design-interview-with-a-meta-engineer-20260410", "mock-interviews/interviewing-io/meta-ml-system-design-yelp-recs-20260410"),
    ("interviewing-io-mock/detect-fraud-scam-content-e6-machine-learning-system-design-interview-with-a-meta-engineer-20250812", "mock-interviews/interviewing-io/meta-e6-ml-system-design-fraud-20250812"),
    ("interviewing-io-mock/harmful-content-removal-machine-learning-system-design-staff-level-mentorship-20230819", "mock-interviews/interviewing-io/meta-staff-ml-system-design-harmful-content-20230819"),
    ("interviewing-io-mock/personalized-newsfeed-system-ml-system-design-interview-with-a-google-engineer-20251111", "mock-interviews/interviewing-io/google-ml-system-design-newsfeed-20251111"),
    ("interviewing-io-mock/python-interview-with-a-facebook-engineer-xml-parser-20211104", "mock-interviews/interviewing-io/meta-python-xml-parser-20211104"),
    ("interviewing-io-mock/technical-interview-with-a-google-engineer-data-wrangling-20200428", "mock-interviews/interviewing-io/google-technical-data-wrangling-20200428"),
    ("interviewing-io-mock/what-separates-e5-from-e6-machine-learning-system-design-interview-design-instagram-reels-20250805", "mock-interviews/interviewing-io/meta-e5-e6-ml-system-design-instagram-reels-20250805"),
    # dataengineers-pro mocks
    ("dataengineers-pro-mock/мок-интервью-data-engineer-тренировочное-собеседование-20250218", "mock-interviews/dataengineers-pro/junior-data-engineer-practice-20250218"),
    ("dataengineers-pro-mock/мок-собеседование-data-engineer-с-объяснениями-s2e2-rzv_de-march-2025-20250318", "mock-interviews/dataengineers-pro/middle-data-engineer-rzv-s2e2-20250318"),
    ("dataengineers-pro-mock/мок-собеседование-data-engineer-с-объяснениями-в-облаках-s2e1-rzv_de-march-2025-20250318", "mock-interviews/dataengineers-pro/middle-data-engineer-rzv-s2e1-20250318"),
    ("dataengineers-pro-mock/мок-собеседование-на-junior-data-engineer-s1e5-rzv_de-aug-2024-20240902", "mock-interviews/dataengineers-pro/junior-data-engineer-rzv-s1e5-20240902"),
    ("dataengineers-pro-mock/мок-собеседование-на-middle-data-engineer-s1e4-rzv_de-jul-2024-20240727", "mock-interviews/dataengineers-pro/middle-data-engineer-rzv-s1e4-20240727"),
    ("dataengineers-pro-mock/мок-собеседование-на-senior-data-engineer-s1e7-rzv_de-oct-2024-20241002", "mock-interviews/dataengineers-pro/senior-data-engineer-rzv-s1e7-20241002"),
    ("dataengineers-pro-mock/открытое-собеседование-tinkoff-dwh-connect-20240410", "mock-interviews/dataengineers-pro/tinkoff-data-engineer-dwh-connect-20240410"),
    # real-interviews / vadim-novoselov
    ("vadim-novoselov/1-реальное-собеседование-data-scientist-сбер-20230721", "real-interviews/vadim-novoselov/sber-data-scientist-20230721"),
    ("vadim-novoselov/2-успешное-собеседование-в-яндекс-секция-machine-learning-20230725", "real-interviews/vadim-novoselov/yandex-data-scientist-ml-20230725"),
    ("vadim-novoselov/3-собеседование-data-scientist-на-650к-в-месяц-20230802", "real-interviews/vadim-novoselov/1xbet-data-scientist-20230802"),
    ("vadim-novoselov/4-реальное-собеседование-data-science-вся-теория-в-одном-видео-20230806", "real-interviews/vadim-novoselov/general-data-science-theory-20230806"),
    ("vadim-novoselov/6-собеседование-data-scientist-на-350к-в-мес-райффайзен-банк-20230816", "real-interviews/vadim-novoselov/raiffeisen-data-scientist-20230816"),
    ("vadim-novoselov/8-реальное-собеседование-data-science-в-vk-алгоритмы-20230827", "real-interviews/vadim-novoselov/vk-data-science-algorithms-20230827"),
    ("vadim-novoselov/16-собеседование-data-scientist-на-госуслуги-пора-менять-профессию-20231117", "real-interviews/vadim-novoselov/gosuslugi-data-scientist-20231117"),
    ("vadim-novoselov/17-успешное-собеседование-data-scientist-лайфкодинг-20231126", "real-interviews/vadim-novoselov/general-data-scientist-live-coding-20231126"),
    ("vadim-novoselov/26-junior-data-scientist-реальное-собеседование-ответы-20240926", "real-interviews/vadim-novoselov/junior-data-scientist-answers-20240926"),
    ("vadim-novoselov/29-интервью-data-scientist-в-мосбиржу-секция-system-design-machine-learning-20241113", "real-interviews/vadim-novoselov/moex-data-scientist-ml-system-design-20241113"),
    ("vadim-novoselov/30-аналитик-данных-в-mytona-собеседование-20241120", "real-interviews/vadim-novoselov/mytona-data-analyst-20241120"),
    ("vadim-novoselov/слил-настоящее-интервью-в-компанию-самокат-data-science-machine-learning-20260225", "real-interviews/vadim-novoselov/samokat-data-scientist-ml-20260225"),
    # youtube-sessions (not structured mock/real interviews)
    ("yandex-practicum/live-собеседования-чего-ждут-от-новичков-в-аналитике-20250601", "youtube-sessions/yandex-practicum/analytics-newcomer-live-20250601"),
    ("yandex-practicum/разбор-резюме-и-собеседования-бизнес-аналитика-и-аналитика-данных-20250930", "youtube-sessions/yandex-practicum/ba-da-resume-review-20250930"),
    ("dataengineers-pro-mock/как-успешно-пройти-интервью-на-позицию-data-engineer-с-уклоном-на-spark-курс-spark-developer-20231215", "youtube-sessions/dataengineers-pro/data-engineer-spark-interview-tips-20231215"),
]

SPLITS: list[tuple[str, list[Segment]]] = [
    (
        "karpov-courses/mock-karpov-product-analyst-junior-2021-06-24",
        [
            Segment("karpov-junior-data-analyst-vyacheslav-20210624", "00:02:35", "00:30:34", "vyacheslav"),
            Segment("karpov-junior-data-analyst-pasha-20210624", "00:31:05", "01:02:08", "pasha"),
        ],
    ),
    (
        "karpov-courses/junior-аналитик-данных-собеседование-karpov-courses-20210913",
        [
            Segment("karpov-junior-data-analyst-sasha-20210913", "00:05:19", "00:39:06", "sasha"),
            Segment("karpov-junior-data-analyst-yegor-20210913", "00:41:54", "01:12:29", "yegor"),
        ],
    ),
]

REMOVE_AFTER_SPLIT = [
    "karpov-courses/аналитик-данных-собеседование-karpov-courses-20210624",
]


def move_folder(old_rel: str, new_rel: str) -> None:
    src = TRANSCRIPTS / old_rel
    dst = TRANSCRIPTS / new_rel
    if not src.exists():
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        raise SystemExit(f"Destination already exists: {dst}")
    shutil.move(str(src), str(dst))


def main() -> None:
    aliases: list[tuple[str, str]] = []

    for old_rel, new_rel in MOVES:
        if (TRANSCRIPTS / old_rel).exists():
            move_folder(old_rel, new_rel)
            aliases.append((old_rel, new_rel))

    karpov_dest = TRANSCRIPTS / "mock-interviews/karpov"
    karpov_dest.mkdir(parents=True, exist_ok=True)

    for src_rel, segments in SPLITS:
        src = TRANSCRIPTS / src_rel
        if not src.exists():
            continue
        split_aliases = split_folder(src, karpov_dest, segments)
        aliases.extend(split_aliases)
        shutil.rmtree(src)

    for old_rel in REMOVE_AFTER_SPLIT:
        p = TRANSCRIPTS / old_rel
        if p.exists():
            shutil.rmtree(p)
            aliases.append((old_rel, "(removed: duplicate of split source)"))

    # template
    for tmpl in ("!mock-template", "mock-template"):
        src = TRANSCRIPTS / tmpl
        if src.exists():
            dst = TRANSCRIPTS / "_template"
            if dst.exists():
                shutil.rmtree(dst)
            shutil.move(str(src), str(dst))
            aliases.append((tmpl, "_template"))
            break

    # playlist source.txt files -> keep next to publisher under mock-interviews or youtube-sessions
    for bucket, dest in [
        ("datainterview-mock/source.txt", "mock-interviews/datainterview/source.txt"),
        ("interview-query-jay-feng-mock/source.txt", "mock-interviews/interview-query/source.txt"),
        ("dataengineers-pro-mock/source.txt", "mock-interviews/dataengineers-pro/source.txt"),
        ("vadim-novoselov/source.txt", "real-interviews/vadim-novoselov/source.txt"),
        ("yandex-practicum/source.txt", "youtube-sessions/yandex-practicum/source.txt"),
        ("karpov-courses/link.txt", "mock-interviews/karpov/source.txt"),
    ]:
        s, d = TRANSCRIPTS / bucket, TRANSCRIPTS / dest
        if s.exists():
            d.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(s), str(d))

    old_buckets = [
        "karpov-courses",
        "datainterview-mock",
        "interview-query-jay-feng-mock",
        "interviewing-io-mock",
        "dataengineers-pro-mock",
        "vadim-novoselov",
        "yandex-practicum",
    ]
    for name in old_buckets:
        d = TRANSCRIPTS / name
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()

    # write aliases
    lines = ["# Auto-generated by scripts/reorganize_transcripts.py", "paths:"]
    for old, new in aliases:
        lines.append(f"  {old}: {new}")
    (TRANSCRIPTS / "aliases.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Done. {len(aliases)} path mappings written to transcripts/aliases.yaml")


if __name__ == "__main__":
    main()
