# Interview Debrief Assistant

**Repository:** [`interview-debrief-assistant`](https://github.com/)  
**Course:** Data Sanity — Intro to AI Agents (Belgrade, 2026)  
**Team:** Anton Voskobovich, Margarita Markova · **Mentor:** Alex Svetkin

AI workflow: interview transcript → structured Q&A → per-question scores → debrief report.

## Documents — what to read

| What | File | Who wrote it |
|------|------|--------------|
| **This page** | `README.md` | Entry point: how to run the demo and where everything lives |
| **Project report** | [`docs/PROJECT_REPORT.md`](docs/PROJECT_REPORT.md) | Team — product, architecture, evaluation, tests |
| **Review report** | [`REVIEW_REPORT.md`](REVIEW_REPORT.md) | Instructor — feedback and rubric scores |
| **Course submission** (`.docx`) | [`submission/`](submission/) | Official rubric + submitted Word report |

There is only **one** README (this file). The `.docx` files sit in `submission/` because they are course hand-in artifacts, not source code.

## Quick demo (no API keys)

```bash
python3 src/ui/app.py 18000
# open http://127.0.0.1:18000 → "Use demo"
```

Alternative if you have [uv](https://docs.astral.sh/uv/): `make ui-emulator`

Demo uses English mock interview **Google data wrangling** (Interviewing.io, 2020) —
`data_scientist_middle_google_data_wrangling_interviewing_io_2020_04_28` in
`data/emulator-data/interviewing-io/`. Fixture built via `scripts/build_emulator_fixture.py`.

## Repository map

```text
├── README.md                 ← you are here
├── REVIEW_REPORT.md          ← instructor review (scores + feedback)
├── submission/               ← project-criteria-scoring.docx, project-report-en_v1.docx
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
