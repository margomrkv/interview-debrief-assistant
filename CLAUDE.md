# CLAUDE.md

Public release of **Post-Interview Debrief Assistant** (Data Sanity final project, Belgrade 2026).

## Entry points for humans

| Audience | Start here |
|----------|------------|
| Reviewers | [`docs/PROJECT_OVERVIEW.md`](docs/PROJECT_OVERVIEW.md) → [`COURSE_REVIEW.md`](COURSE_REVIEW.md) → [`review/`](review/) |
| Developers | [`README.md`](README.md), [`docs/spec/spec.md`](docs/spec/spec.md) |

## Repository layout

| Block | Directory | Contents |
|-------|-----------|----------|
| Project report | `docs/PROJECT_OVERVIEW.md` | Defense / checkpoint report |
| Course review | `COURSE_REVIEW.md`, `review/` | Instructor feedback + rubric `.docx` |
| Specs | `docs/spec/` | Product and pipeline specs |
| KB data | `data/knowledgebase/raw/`, `splitted/`, `train/` | Public interview corpus + splitter artifacts |
| UI demo | `data/emulator-data/` | Precomputed splitter/scoring fixtures (mock interviews only) |
| Code | `src/`, `tests/`, `.claude/skills/` | Python + agent skills |
| Training runs | `runs/` | Gitignored per-run artifacts |

## Naming (interviews)

- Mock KB: `data/knowledgebase/raw/mock-interviews/<publisher>/…` — see `data/knowledgebase/raw/README.md`
- Real channels: `data/knowledgebase/raw/real-interviews/novoselov/…`
- **Private** own interviews: `data/candidatecontext/` — **gitignored**, not in public history

## Splitter

`.claude/skills/splitter/SKILL.md` (`/splitter`) — steps 1–5 + correction loop until `splitter_verdict.py` exit 0.

## Rules

Do not run tests against paid models during development unless necessary.

## Private data (out of scope for this clone)

Removed from git history before publication: `data/candidatecontext/`, `internal-notes/`, `course/`, `data/emulator-data/karpov/`, legacy paths `transcripts/anton*`, `marketflow/`, `candidatecontext/`.
