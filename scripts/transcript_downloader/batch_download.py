"""Batch-download YouTube transcripts to per-channel buckets.

Input: TSV with columns `video_id<TAB>bucket<TAB>title_hint?`.
Reuses helpers from main.py.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

from main import (
    build_feedback_text,
    fetch_transcript,
    get_repo_root,
    resolve_video_meta,
    slugify,
    write_folder,
)
from youtube_transcript_api import CouldNotRetrieveTranscript


def parse_plan(path: Path) -> list[tuple[str, str, str]]:
    rows = []
    with path.open(encoding="utf-8") as f:
        for raw in csv.reader(f, delimiter="\t"):
            if not raw:
                continue
            first = raw[0].strip()
            if not first or first.startswith("#"):
                continue
            if len(raw) < 2:
                raise ValueError(f"row needs at least video_id<TAB>bucket: {raw}")
            vid, bucket = first, raw[1].strip()
            hint = raw[2].strip() if len(raw) > 2 else ""
            rows.append((vid, bucket, hint))
    return rows


def parse_args(argv=None):
    p = argparse.ArgumentParser(prog="batch-download")
    p.add_argument("plan", type=Path, help="TSV: video_id<TAB>bucket<TAB>title_hint?")
    p.add_argument("--lang", default="ru,en")
    p.add_argument("--overwrite", action="store_true")
    p.add_argument("--dry-run", action="store_true",
                   help="Resolve meta only; print where each row would be written")
    p.add_argument("--repo-root", type=Path)
    return p.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    repo_root = args.repo_root or get_repo_root()
    lang_priority = [x.strip() for x in args.lang.split(",") if x.strip()]
    rows = parse_plan(args.plan)

    ok = skipped = failed = 0
    buckets_seen: set[str] = set()

    for vid, bucket, hint in rows:
        try:
            meta = resolve_video_meta(vid)
        except Exception as exc:
            print(f"fail: {vid} meta: {exc}", file=sys.stderr)
            failed += 1
            continue
        title = meta.get("title") or hint or vid
        slug = slugify(title)
        date = meta.get("upload_date") or "00000000"
        folder = repo_root / "transcripts" / bucket / f"{slug}-{date}"

        if args.dry_run:
            print(f"plan: {folder}  ({title[:80]})")
            ok += 1
            continue

        try:
            snippets = fetch_transcript(vid, lang_priority)
        except CouldNotRetrieveTranscript as exc:
            print(f"fail: {vid} ({title[:60]}): {exc}", file=sys.stderr)
            failed += 1
            continue

        feedback_text = build_feedback_text(snippets, meta.get("chapters") or [])
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
            buckets_seen.add(bucket)
        else:
            skipped += 1

    # Drop a link.txt-style breadcrumb per bucket if it doesn't exist
    if not args.dry_run:
        for b in buckets_seen:
            marker = repo_root / "transcripts" / b / "source.txt"
            if not marker.exists():
                marker.write_text(f"# created by batch_download.py\n", encoding="utf-8")

    print(f"summary: ok={ok} skipped={skipped} failed={failed}", file=sys.stderr)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
