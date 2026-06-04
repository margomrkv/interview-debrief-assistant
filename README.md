# Post-Interview Debrief Assistant

**Course:** Data Sanity — Intro to AI Agents (Belgrade, 2026)  
**Team:** Anton Voskobovich, Margarita Markova · **Mentor:** Alex Svetkin  
**Repository status:** public release — sanitized history (no private interview data)

LLM-based workflow: interview transcript → structured Q&A → per-question scores → debrief report.

## For reviewers — start here

1. **[docs/PROJECT_OVERVIEW.md](docs/PROJECT_OVERVIEW.md)** — project report: product, architecture, evaluation, tests.
2. **[COURSE_REVIEW.md](COURSE_REVIEW.md)** — instructor feedback and rubric scores.
3. **[review/](review/)** — scoring rubric (`.docx`) and submitted Word report.

## Quick demo (no API keys)

```bash
make ui-emulator
```

Opens the web UI with a **mock interview** demo (`data_scientist_junior_karpov_2022_03_30` from `data/emulator-data/karpov/`).

## Repository map

```text
├── README.md                          ← you are here
├── COURSE_REVIEW.md                   ← instructor feedback & scores
├── review/                            ← rubric + submitted report (.docx)
├── docs/
│   ├── PROJECT_OVERVIEW.md            ← project report (read first)
│   ├── spec/                          ← product & pipeline specs
│   └── images/                        ← architecture diagram
├── data/
│   ├── knowledgebase/raw/             ← interview transcripts (mock / real / YouTube)
│   ├── knowledgebase/splitted/        ← splitter output (*.vN.* per run)
│   ├── knowledgebase/train/           ← training JSON for evaluator
│   └── emulator-data/               ← UI demo fixtures (public mock interviews)
├── .claude/skills/                    ← workflows (splitter, feedback-report, …)
├── src/                               ← Python: KB train, assessor, UI, downloader
├── tests/
└── runs/                              ← KB training artifacts (gitignored)
```

## Private data (not in this repo)

Personal interview folders (`data/candidatecontext/`), internal meeting notes, and course lecture materials were removed from git history before publication. To run **feedback-report** on your own interview, create a local folder (see `.claude/skills/feedback-report/SKILL.md`) — it is gitignored by default.

## Tests

```bash
pytest tests/
```
