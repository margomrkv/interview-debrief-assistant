"""Download YouTube interview transcripts into transcripts/<bucket>/<slug>-<YYYYMMDD>/."""

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


def to_timestamped(snippets) -> str:
    if not snippets:
        return ""
    total = snippets[-1].start + snippets[-1].duration
    use_hours = total >= 3600
    lines = []
    for s in snippets:
        text = re.sub(r"\s+", " ", s.text).strip()
        if not text:
            continue
        secs = int(s.start)
        if use_hours:
            h, rem = divmod(secs, 3600)
            m, sec = divmod(rem, 60)
            stamp = f"[{h:02d}:{m:02d}:{sec:02d}]"
        else:
            m, sec = divmod(secs, 60)
            stamp = f"[{m:02d}:{sec:02d}]"
        lines.append(f"{stamp} {text}")
    return "\n".join(lines) + "\n"


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


def write_folder(folder: Path, url: str, snippets, overwrite: bool) -> bool:
    if folder.exists() and not overwrite:
        print(f"warn: folder exists, skipping: {folder}", file=sys.stderr)
        return False
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "link.txt").write_text(url.strip() + "\n", encoding="utf-8")
    (folder / "transcript.txt").write_text(to_plain_text(snippets), encoding="utf-8")
    (folder / "timecodes.txt").write_text(to_timestamped(snippets), encoding="utf-8")
    return True


def parse_args(argv=None):
    p = argparse.ArgumentParser(
        prog="transcript-downloader",
        description="Download YouTube transcripts into transcripts/<slug>-<YYYYMMDD>/",
    )
    p.add_argument("url", help="Video or playlist URL")
    p.add_argument("--slug", help="Slug for single video (required for single video)")
    p.add_argument("--date", help="Date YYYYMMDD for single video (required for single video)")
    p.add_argument("--playlist-name", dest="playlist_name",
                   help="Bucket folder name under transcripts/ (required for playlist URL)")
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
        folder = repo_root / "transcripts" / "single_videos" / f"{args.slug}-{args.date}"
        written = write_folder(folder, args.url, snippets, args.overwrite)
        print(f"{'wrote' if written else 'skipped'}: {folder}")
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

    bucket = repo_root / "transcripts" / args.playlist_name
    ok = skipped = failed = 0
    for e in entries:
        vid = e["id"]
        slug = slugify(e["title"]) if e["title"] else vid
        date = e["upload_date"] or "00000000"
        if date == "00000000":
            print(f"warn: no upload_date for {vid}, using 00000000", file=sys.stderr)
        folder = bucket / f"{slug}-{date}"
        video_url = f"https://www.youtube.com/watch?v={vid}"
        try:
            snippets = fetch_transcript(vid, lang_priority)
        except CouldNotRetrieveTranscript as exc:
            print(f"fail: {vid} ({e['title']}): {exc}", file=sys.stderr)
            failed += 1
            continue
        try:
            written = write_folder(folder, video_url, snippets, args.overwrite)
        except OSError as exc:
            print(f"fail: {vid} write: {exc}", file=sys.stderr)
            failed += 1
            continue
        if written:
            ok += 1
            print(f"wrote: {folder}")
        else:
            skipped += 1

    print(f"summary: ok={ok} skipped={skipped} failed={failed}", file=sys.stderr)
    return 0 if ok > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
