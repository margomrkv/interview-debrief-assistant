# Post-Interview Debrief Assistant

**Course:** Data Sanity — Intro to AI Agents (Belgrade, 2026)  
**Team:** Anton Voskobovich, Margarita Markova · **Mentor:** Alex Svetkin  
**Repository status:** code freeze reference — 2026-05-21

LLM-based workflow: interview transcript → structured Q&A → per-question scores → debrief report.

## Where to start

**[docs/PROJECT_OVERVIEW.md](docs/PROJECT_OVERVIEW.md)** — project report for course review (product, architecture, how we built the system, evaluation and tests).

## Repository map

```text
├── README.md                          ← you are here
├── docs/
│   ├── PROJECT_OVERVIEW.md            ← project report (read first)
│   └── images/                        ← architecture diagram
├── review/              ← submitted report + grading rubric
├── data/
│   ├── knowledgebase/raw/             ← interview transcripts (mock / real / YouTube)
│   ├── knowledgebase/splitted/        ← splitter output (*.vN.* per run)
│   ├── knowledgebase/train/           ← training JSON for evaluator
│   └── candidatecontext/              ← own interviews (CV, feedback, reports)
├── .claude/skills/                    ← workflows (splitter, feedback-report, …)
│   └── splitter/                      ← Q&A extraction (steps 1–5)
├── src/                               ← Python: KB train, AR score, downloader
│   ├── kb/
│   ├── ar/
│   └── transcriptdownloader/
├── tests/
└── runs/                              ← KB training artifacts (gitignored)
```
