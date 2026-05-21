# Transcripts

Last updated: 2026-05-19

## Layout

| Directory | Contents |
|-----------|----------|
| `mock-interviews/<publisher>/` | **Постановочные** собеседования (учебные / staged) |
| `real-interviews/<publisher>/` | **Записи реальных** собеседований (`novoselov`, …) |
| `youtube-sessions/<publisher>/` | Lives, talks, resume reviews (not a single interview) |
| `own/` | Your interviews (`<person>-<company>-YYYYMMDD/`) |
| `_template/` | Template for new downloads |

Тип интервью (**mock** vs **real**) задаётся **только** корневой папкой `mock-interviews/` или `real-interviews/`, не префиксом в имени листовой папки.

### Тип интервью vs режим splitter

| | Где видно | Смысл |
|---|-----------|--------|
| **mock / real** (тип интервью) | `mock-interviews/` vs `real-interviews/` | Постановка vs подлинная запись |
| **split_and_validate / split_only** | `splitter_mode` в JSON после splitter | Есть `video.md` → validation; нет → только JSON/Excel |

См. также `splitter_output/README.md`.

## Leaf folder name (hiring)

```text
{role}-{level}[-{target}]-{publisher}[-{candidate}][-{topic}]-{YYYY-MM-DD}
```

| Segment | Values | Notes |
|---------|--------|-------|
| `role` | `data-scientist`, `data-analyst`, `product-analyst`, … | Primary sort key |
| `level` | `junior`, `middle`, `senior` | E5/E6 → `senior` |
| `target` | `amazon`, `avito`, `sber`, … | Employer in the case; omit if none |
| `publisher` | `karpov`, `interview-query`, `novoselov`, … | **Not** `vadim` — use `novoselov` |
| `candidate` | `sasha`, `yegor`, … | Only when split from one video |
| `topic` | `fraud-model`, `ml`, `v1`, … | Disambiguation / section |
| date | `YYYY-MM-DD` | Always last |

**Workshop tracks** (behavioral, system-design, ab-testing): track name in the `role` slot, e.g. `behavioral-senior-karpov-v1-2022-11-10`.

**Sessions:** `session-{topic}-{publisher}-{YYYY-MM-DD}` under `youtube-sessions/`.

### Examples

```text
mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/
mock-interviews/interview-query/data-scientist-senior-amazon-fraud-model-datainterview-2022-01-06/
mock-interviews/karpov/data-analyst-junior-karpov-sasha-2021-09-13/
real-interviews/novoselov/data-scientist-middle-sber-novoselov-2023-07-21/
```

## Files per interview

| File | Purpose |
|------|---------|
| `transcript.txt` | Full text |
| `timecodes.txt` | `[HH:MM:SS]` lines (preferred splitter input) |
| `video.md` | YouTube metadata + chapters |
| `link.txt` | Source URL |
| `feedback.md` | Interviewer feedback (optional) |

Path history: `aliases.yaml`.

## Downloading new interviews

CLI: `scripts/transcript_downloader/main.py` — skill `/download-transcript`.

Naming rules for `--slug` / `--bucket`: `scripts/transcript_downloader/NAMING.md`.
