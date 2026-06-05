# CLAUDE.md

Public release **`interview-debrief-assistant`** — pipeline *Interview Debrief Assistant*; demo UI *Transcript Lens*.

## Entry points

| Audience | Start here |
|----------|------------|
| Reviewers | [`README.md`](README.md) → [`docs/PROJECT_REPORT.md`](docs/PROJECT_REPORT.md) → [`review/`](review/) |
| Developers | [`README.md`](README.md), [`docs/spec/spec.md`](docs/spec/spec.md) |

## Layout

| Block | Path |
|-------|------|
| Team project report | `docs/PROJECT_REPORT.md` |
| Review package (report + `.docx`) | `review/` |
| KB data | `data/knowledgebase/` |
| UI demo | `data/emulator-data/` |
| Code | `src/`, `tests/`, `.claude/skills/` |

## Rules

Do not run tests against paid models during development unless necessary.
