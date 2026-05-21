# Transcript storage layout and folder naming

Last updated: 2026-05-19

Canonical copy for `transcript_downloader`. Mirror: `data/knowledgebase/raw/README.md`.

## Directory tree

```text
data/knowledgebase/raw/
├── mock-interviews/<publisher>/     # staged / educational mocks
├── real-interviews/<publisher>/     # real or leaked-style (e.g. novoselov)
├── youtube-sessions/<publisher>/    # lives, talks — not a single interview
├── single_videos/                   # staging only (CLI default bucket)
└── _template/                       # empty template per interview

data/candidatecontext/               # own interviews (CV, feedback) — not under raw/
```

**Publisher** = YouTube channel / course brand (`karpov`, `interview-query`, `novoselov`, …).  
**Not** `vadim` — use **`novoselov`** for Vadim Novoselov.

## Leaf folder name — hiring

**Interview kind** (`mock` vs `real`) is only the parent folder: `mock-interviews/` or `real-interviews/`.  
Do **not** prefix the leaf folder with `mock-` or `real-`.

```text
{role}-{level}[-{target}]-{publisher}[-{candidate}][-{topic}]-{YYYY-MM-DD}
```

| # | Segment | Examples | Required |
|---|---------|----------|----------|
| 1 | `role` | `data-scientist`, `data-analyst`, `product-analyst`, … | yes (hiring) |
| 2 | `level` | `junior`, `middle`, `senior` | if known (E5/E6 → `senior`) |
| 3 | `target` | `amazon`, `avito`, `sber` | only employer in the case |
| 4 | `publisher` | `karpov`, `interview-query`, `novoselov` | yes |
| 5 | `candidate` | `sasha`, `yegor`, `pasha` | split from one video only |
| 6 | `topic` | `fraud-model`, `ml`, `v1` | disambiguation |
| 7 | date | `2022-03-30` | yes, always last |

**Sort order** when browsing: `role` → `level` → `target` → `publisher` → …

### Workshop / series (no JD)

Use track name in the `role` slot:

```text
mock-interviews/karpov/behavioral-senior-karpov-v1-2022-11-10/
mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/
mock-interviews/karpov/ml-system-design-senior-karpov-v2-2021-08-28/
mock-interviews/karpov/ab-testing-senior-karpov-2024-01-19/
```

### YouTube sessions (not an interview)

```text
session-{topic}-{publisher}-{YYYY-MM-DD}
```

Under `youtube-sessions/<publisher>/`.

## Files inside each interview folder

| File | Purpose |
|------|---------|
| `video.md` | YouTube metadata + `## Chapters` + `## Description` |
| `transcript.txt` | Plain text (all snippets) |
| `timecodes.txt` | `[HH:MM:SS] line` — preferred input for splitter |
| `link.txt` | Source URL (playlist bucket root only, optional per video) |
| `feedback.md` | Interviewer feedback slice (if feedback chapter detected) |

`video.md` frontmatter uses `upload_date: YYYY-MM-DD`; folder suffix uses the same format.

## CLI mapping

### Single video

```bash
uv run python scripts/transcript_downloader/main.py "<url>" \
  --slug data-scientist-junior-karpov \
  --date 20220330 \
  --bucket mock-interviews/karpov
```

Writes:

```text
data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/
```

- `--slug` = leaf name **without** date (CLI appends `-YYYY-MM-DD`).
- `--date` = `YYYYMMDD` (from YouTube `upload_date` or user).
- `--bucket` = path under `data/knowledgebase/raw/` (default: `single_videos` = staging).

### Playlist

```bash
uv run python scripts/transcript_downloader/main.py "<playlist-url>" \
  --playlist-name mock-interviews/karpov
```

Per video: `data/knowledgebase/raw/mock-interviews/karpov/<slugified-title>-YYYY-MM-DD/`.  
**Rename** each leaf to the hiring pattern above (CLI auto-slug is YouTube title only).

## Publisher slugs

| Channel / source | `--bucket` / `--playlist-name` | In leaf name (`publisher` segment) |
|------------------|--------------------------------|--------------------------------------|
| karpov.courses | `mock-interviews/karpov` | `karpov` |
| Interview Query | `mock-interviews/interview-query` | `interview-query` |
| interviewing.io | `mock-interviews/interviewing-io` | `interviewing-io` |
| DataInterview | `mock-interviews/datainterview` | `datainterview` |
| DataEngineers Pro | `mock-interviews/dataengineers-pro` | `dataengineers-pro` |
| Avito Tech | `mock-interviews/avito` | `avito` |
| Vadim Novoselov | `real-interviews/novoselov` | `novoselov` |
| Yandex Practicum | `youtube-sessions/yandex-practicum` | `yandex-practicum` |

## After download

1. If bucket was `single_videos`, move folder to `mock-interviews/<publisher>/` or `real-interviews/<publisher>/`.
2. Rename leaf to match the pattern (playlist downloads almost always need this).
3. Multi-candidate video: split into separate folders (`-sasha`, `-yegor`, …) — see `scripts/reorganize_transcripts.py`.
4. Update `data/knowledgebase/raw/aliases.yaml` if renaming existing corpus.

Path history: `data/knowledgebase/raw/aliases.yaml`.
