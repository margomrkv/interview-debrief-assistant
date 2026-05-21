"""Download YouTube interview transcripts into data/knowledgebase/raw/.

Folder layout and leaf naming: see NAMING.md in this directory
(and data/knowledgebase/raw/README.md). Single video: raw/<bucket>/<slug>-<YYYY-MM-DD>/.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from youtube_transcript_api import (
    CouldNotRetrieveTranscript,
    NoTranscriptFound,
    YouTubeTranscriptApi,
)
from yt_dlp import YoutubeDL


PATH_VIDEO_ID_PATTERNS = [
    re.compile(r"youtu\.be/([A-Za-z0-9_-]{11})"),
    re.compile(r"youtube\.com/shorts/([A-Za-z0-9_-]{11})"),
    re.compile(r"youtube\.com/embed/([A-Za-z0-9_-]{11})"),
]

FEEDBACK_TITLE_RE = re.compile(r"обратн\w*\s+связ\w*|фидб[еэ]к|feedback", re.IGNORECASE)


def classify_url(url: str) -> tuple[str, str]:
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    if v := query.get("v", [None])[0]:
        return ("video", v)
    for pat in PATH_VIDEO_ID_PATTERNS:
        if m := pat.search(url):
            return ("video", m.group(1))
    if list_id := query.get("list", [None])[0]:
        return ("playlist", list_id)
    raise ValueError(f"Cannot parse as YouTube video or playlist: {url}")


def expand_playlist(url: str) -> list[dict]:
    with YoutubeDL({"quiet": True, "skip_download": True, "no_warnings": True}) as ydl:
        info = ydl.extract_info(url, download=False)
    return [
        {"id": e["id"], "title": e.get("title", ""), "upload_date": e.get("upload_date", "")}
        for e in info.get("entries", []) or []
        if e and e.get("id")
    ]


def resolve_video_meta(video_id: str) -> dict:
    url = f"https://www.youtube.com/watch?v={video_id}"
    with YoutubeDL({"quiet": True, "skip_download": True, "no_warnings": True}) as ydl:
        info = ydl.extract_info(url, download=False)
    return {
        "url": url,
        "title": info.get("title") or "",
        "upload_date": info.get("upload_date") or "",
        "duration": info.get("duration"),
        "channel": info.get("channel") or info.get("uploader"),
        "description": info.get("description") or "",
        "view_count": info.get("view_count"),
        "like_count": info.get("like_count"),
        "tags": info.get("tags") or [],
        "thumbnail_url": info.get("thumbnail"),
        "language": info.get("language"),
        "chapters": info.get("chapters") or [],
    }


def fetch_transcript(video_id: str, lang_priority: list[str]):
    tl = YouTubeTranscriptApi().list(video_id)
    try:
        return tl.find_manually_created_transcript(lang_priority).fetch().snippets
    except NoTranscriptFound:
        pass
    try:
        return tl.find_generated_transcript(lang_priority).fetch().snippets
    except NoTranscriptFound:
        pass
    for t in tl:
        if not t.is_generated:
            return t.fetch().snippets
    for t in tl:
        if t.is_generated:
            return t.fetch().snippets
    raise NoTranscriptFound(video_id, lang_priority, tl)


def to_plain_text(snippets) -> str:
    parts = [re.sub(r"\s+", " ", s.text).strip() for s in snippets]
    return " ".join(p for p in parts if p) + "\n"


def fmt_time(secs: float, use_hours: bool) -> str:
    s = int(secs)
    if use_hours:
        h, rem = divmod(s, 3600)
        m, sec = divmod(rem, 60)
        return f"{h:02d}:{m:02d}:{sec:02d}"
    m, sec = divmod(s, 60)
    return f"{m:02d}:{sec:02d}"


def use_hours_for(snippets) -> bool:
    if not snippets:
        return False
    total = snippets[-1].start + snippets[-1].duration
    return total >= 3600


def to_timestamped(snippets) -> str:
    if not snippets:
        return ""
    use_hours = use_hours_for(snippets)
    lines = []
    for s in snippets:
        text = re.sub(r"\s+", " ", s.text).strip()
        if not text:
            continue
        lines.append(f"[{fmt_time(s.start, use_hours)}] {text}")
    return "\n".join(lines) + "\n"


def find_feedback_chapter(chapters: list[dict]) -> dict | None:
    for ch in chapters or []:
        title = ch.get("title") or ""
        if FEEDBACK_TITLE_RE.search(title):
            return {
                "title": title,
                "start": float(ch["start_time"]),
                "end": float(ch["end_time"]),
            }
    return None


def slice_snippets(snippets, start: float, end: float):
    return [s for s in snippets if start <= s.start < end]


def _yaml_quote(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


_YAML_UNSAFE_RE = re.compile(r"""[:\[\]{},#&*!|>'"%@`]|^\s|\s$""")


def _yaml_flow_list(items: list[str]) -> str:
    parts = [_yaml_quote(i) if _YAML_UNSAFE_RE.search(i) else i for i in items]
    return "[" + ", ".join(parts) + "]"


def _format_iso_date(d: str) -> str:
    if len(d) == 8 and d.isdigit():
        return f"{d[:4]}-{d[4:6]}-{d[6:8]}"
    return d


def format_video_md(meta: dict, use_hours: bool) -> str:
    lines = ["---"]
    if url := meta.get("url"):
        lines.append(f"url: {url}")
    if title := meta.get("title"):
        lines.append(f"title: {_yaml_quote(title)}")
    if upload_date := meta.get("upload_date"):
        lines.append(f"upload_date: {_format_iso_date(upload_date)}")
    if duration := meta.get("duration"):
        lines.append(f"duration: {int(duration)}")
    if channel := meta.get("channel"):
        lines.append(f"channel: {_yaml_quote(channel)}")
    if view_count := meta.get("view_count"):
        lines.append(f"view_count: {int(view_count)}")
    if like_count := meta.get("like_count"):
        lines.append(f"like_count: {int(like_count)}")
    if language := meta.get("language"):
        lines.append(f"language: {language}")
    if thumbnail_url := meta.get("thumbnail_url"):
        lines.append(f"thumbnail_url: {_yaml_quote(thumbnail_url)}")
    if tags := meta.get("tags"):
        lines.append(f"tags: {_yaml_flow_list(tags)}")
    lines.append("---")

    if chapters := meta.get("chapters"):
        lines.append("")
        lines.append("## Chapters")
        for ch in chapters:
            start = fmt_time(float(ch.get("start_time") or 0), use_hours)
            lines.append(f"- [{start}] {ch.get('title') or ''}")

    if (description := (meta.get("description") or "").strip()):
        lines.append("")
        lines.append("## Description")
        lines.append("")
        lines.append(description)

    return "\n".join(lines) + "\n"


def format_feedback(match: dict, snippets, use_hours: bool) -> str:
    start_fmt = fmt_time(match["start"], use_hours)
    end_fmt = fmt_time(match["end"], use_hours)
    header = (
        "---\n"
        f"section: {_yaml_quote(match['title'])}\n"
        f'start: "{start_fmt}"\n'
        f'end: "{end_fmt}"\n'
        f"start_seconds: {int(match['start'])}\n"
        f"end_seconds: {int(match['end'])}\n"
        "---\n\n"
    )
    return header + to_plain_text(snippets)


def build_feedback_text(snippets, chapters: list[dict]) -> str | None:
    match = find_feedback_chapter(chapters)
    if not match:
        return None
    fb_snips = slice_snippets(snippets, match["start"], match["end"])
    if not fb_snips:
        return None
    text = format_feedback(match, fb_snips, use_hours_for(snippets))
    return text if text.strip() else None


def slugify(title: str) -> str:
    s = re.sub(r"[^\w]+", "-", title.lower(), flags=re.UNICODE)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "untitled"


def get_repo_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True,
    )
    return Path(result.stdout.strip())


def write_folder(folder: Path, meta: dict, snippets, overwrite: bool,
                 feedback_text: str | None = None) -> bool:
    if folder.exists() and not overwrite:
        print(f"warn: folder exists, skipping: {folder}", file=sys.stderr)
        return False
    folder.mkdir(parents=True, exist_ok=True)
    use_hours = use_hours_for(snippets)
    (folder / "video.md").write_text(format_video_md(meta, use_hours), encoding="utf-8")
    (folder / "transcript.txt").write_text(to_plain_text(snippets), encoding="utf-8")
    (folder / "timecodes.txt").write_text(to_timestamped(snippets), encoding="utf-8")
    if feedback_text:
        (folder / "feedback.md").write_text(feedback_text, encoding="utf-8")
    return True


def parse_args(argv=None):
    p = argparse.ArgumentParser(
        prog="transcript-downloader",
        description=(
            "Download YouTube transcripts. Naming: scripts/transcript_downloader/NAMING.md"
        ),
        epilog=(
            "Leaf pattern: {kind}-{role}-{level}[-{target}]-{publisher}[-{candidate}]"
            "[-{topic}]-{YYYY-MM-DD}. See NAMING.md."
        ),
    )
    p.add_argument("url", help="Video or playlist URL")
    p.add_argument(
        "--slug",
        help="Leaf folder base without date, e.g. data-scientist-junior-karpov",
    )
    p.add_argument("--date", help="Date YYYYMMDD (required for single video)")
    p.add_argument(
        "--bucket",
        default="single_videos",
        help="Path under data/knowledgebase/raw/ for single video (default: single_videos = staging)",
    )
    p.add_argument(
        "--playlist-name",
        dest="playlist_name",
        help="Path under data/knowledgebase/raw/ for playlist, e.g. mock-interviews/karpov",
    )
    p.add_argument("--lang", default="ru,en",
                   help="Comma-separated language priority (default: ru,en)")
    p.add_argument("--overwrite", action="store_true", help="Overwrite existing folder")
    p.add_argument("--repo-root", type=Path,
                   help="Repo root (default: git rev-parse --show-toplevel)")
    return p.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    repo_root = args.repo_root or get_repo_root()
    lang_priority = [x.strip() for x in args.lang.split(",") if x.strip()]

    try:
        kind, ident = classify_url(args.url)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if kind == "video":
        if args.playlist_name:
            print("error: --playlist-name is for playlist URLs only", file=sys.stderr)
            return 2
        if not args.slug or not args.date:
            print("error: --slug and --date are required for a single video URL",
                  file=sys.stderr)
            return 2
        if not re.fullmatch(r"\d{8}", args.date):
            print("error: --date must be YYYYMMDD", file=sys.stderr)
            return 2
        try:
            snippets = fetch_transcript(ident, lang_priority)
        except CouldNotRetrieveTranscript as exc:
            print(f"error: {ident}: {exc}", file=sys.stderr)
            return 1
        try:
            meta = resolve_video_meta(ident)
        except Exception as exc:
            print(f"error: failed to resolve video meta: {exc}", file=sys.stderr)
            return 1
        feedback_text = build_feedback_text(snippets, meta["chapters"])
        iso_date = _format_iso_date(args.date)
        folder = (
            repo_root / "data" / "knowledgebase" / "raw" / args.bucket / f"{args.slug}-{iso_date}"
        )
        written = write_folder(folder, meta, snippets, args.overwrite,
                               feedback_text=feedback_text)
        print(f"{'wrote' if written else 'skipped'}: {folder}"
              f"{' (+feedback)' if written and feedback_text else ''}")
        if written and args.bucket == "single_videos":
            print(
                "hint: move to mock-interviews/<publisher>/ or real-interviews/<publisher>/ "
                "per scripts/transcript_downloader/NAMING.md",
                file=sys.stderr,
            )
        return 0 if written else 1

    if args.slug or args.date:
        print("error: --slug/--date are for single video URLs only (playlists auto-derive them)",
              file=sys.stderr)
        return 2
    if not args.playlist_name:
        print("error: --playlist-name is required for a playlist URL", file=sys.stderr)
        return 2

    try:
        entries = expand_playlist(args.url)
    except Exception as exc:
        print(f"error: failed to expand playlist: {exc}", file=sys.stderr)
        return 2
    if not entries:
        print("error: playlist is empty", file=sys.stderr)
        return 1

    bucket = repo_root / "data" / "knowledgebase" / "raw" / args.playlist_name
    bucket.mkdir(parents=True, exist_ok=True)
    (bucket / "link.txt").write_text(args.url.strip() + "\n", encoding="utf-8")
    ok = skipped = failed = 0
    for e in entries:
        vid = e["id"]
        slug = slugify(e["title"]) if e["title"] else vid
        date = e["upload_date"] or "00000000"
        if date == "00000000":
            print(f"warn: no upload_date for {vid}, using 00000000", file=sys.stderr)
        folder = bucket / f"{slug}-{_format_iso_date(date)}"
        try:
            snippets = fetch_transcript(vid, lang_priority)
        except CouldNotRetrieveTranscript as exc:
            print(f"fail: {vid} ({e['title']}): {exc}", file=sys.stderr)
            failed += 1
            continue
        try:
            meta = resolve_video_meta(vid)
        except Exception as exc:
            print(f"fail: {vid} meta: {exc}", file=sys.stderr)
            failed += 1
            continue
        feedback_text = build_feedback_text(snippets, meta["chapters"])
        try:
            written = write_folder(folder, meta, snippets, args.overwrite,
                                   feedback_text=feedback_text)
        except OSError as exc:
            print(f"fail: {vid} write: {exc}", file=sys.stderr)
            failed += 1
            continue
        if written:
            ok += 1
            tag = " (+feedback)" if feedback_text else ""
            print(f"wrote: {folder}{tag}")
        else:
            skipped += 1

    print(f"summary: ok={ok} skipped={skipped} failed={failed}", file=sys.stderr)
    return 0 if ok > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
