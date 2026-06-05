# Interview Debrief Assistant

**Repository:** [`margomrkv/interview-debrief-assistant`](https://github.com/margomrkv/interview-debrief-assistant)  
**Demo UI:** **Transcript Lens** (TL) — `src/ui/`  
**Course:** Data Sanity — Intro to AI Agents (Belgrade, 2026)  
**Team:** Anton Voskobovich, Margarita Markova · **Mentor:** Alex Svetkin

*Interview Debrief Assistant* is the full pipeline (transcript → Q&A → scores → debrief report).  
*Transcript Lens* is the browser demo that replays that pipeline without API keys.

## Documents — what to read

| What | File | Who wrote it |
|------|------|--------------|
| **This page** | `README.md` | Entry point: how to run the demo and where everything lives |
| **Project report** | [`docs/PROJECT_REPORT.md`](docs/PROJECT_REPORT.md) | Team — product, architecture, evaluation, tests |
| **Review package** | [`review/`](review/) | Instructor feedback, rubric scores, and course `.docx` hand-ins |

There is only **one** README (this file). Review and submission `.docx` files live under [`review/`](review/).

## Quick demo (no API keys)

```bash
python3 src/ui/app.py 18000
# open http://127.0.0.1:18000 → Transcript Lens → "Use demo"
```

Alternative if you have [uv](https://docs.astral.sh/uv/): `make ui-emulator`

Demo uses English mock interview **Google data wrangling** (Interviewing.io, 2020) —
`data_scientist_middle_google_data_wrangling_interviewing_io_2020_04_28` in
`data/emulator-data/interviewing-io/`. Fixture built via `scripts/build_emulator_fixture.py`.

## Repository map

```text
├── README.md                 ← you are here
├── review/                   ← REVIEW_REPORT.md + course .docx hand-ins
├── docs/
│   ├── PROJECT_REPORT.md     ← team project report (read for technical depth)
│   ├── spec/
│   └── images/
├── data/
│   ├── knowledgebase/        ← public interview corpus + splitter artifacts
│   └── emulator-data/        ← UI demo fixtures
├── src/                      ← Python: splitter, assessor, UI, KB train
├── tests/
└── runs/                     ← training artifacts (gitignored)
```

## Tests

```bash
pytest tests/          # or: make test  (requires uv + dev deps)
```

## Private data (not in this repo)

Personal interview folders (`data/candidatecontext/`), internal meeting notes, and course lecture materials were removed from git history before publication.
