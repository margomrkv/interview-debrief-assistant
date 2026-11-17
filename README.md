# Interview Debrief Assistant

**Repository:** [`margomrkv/interview-debrief-assistant`](https://github.com/margomrkv/interview-debrief-assistant)  
**Demo UI:** **Transcript Lens** (TL) — `src/ui/`  
**Course:** Data Sanity — Intro to AI Agents (Belgrade, 2026)  
**Team:** Anton Voskobovich, Margarita Markova · **Mentor:** Alex Svetkin

Interview Debrief Assistant (Transcript Lens) is an LLM workflow: job interview transcript → extracted Q&A → score per answer → hire / no-hire summary. Python, LiteLLM, DSPy.

Extraction quality was checked on YouTube mock interviews in data analytics, data science, and ML. Those videos have chapter lists the model does not see while it splits the transcript. Python then checks coverage, whether the question blocks were found, and topic match, whether the extracted topic fits that part of the interview. Target ≥90%. One junior data-science mock: 36 Q&A, both checks 100%. Corpus: 70+ public YouTube mock interviews.

Each answer is scored from 1 to 10 on factual correctness, focus, and clarity. DSPy MIPROv2 rewrote the scoring prompt and kept the wording closest to labels taken from the instructor’s expected answer and feedback: 169 labeled answers, 118 used to choose the prompt, 51 held out, split by whole interview. On the held-out answers, 72% of scores matched the label or missed by one point. Agreement score 0.86, where 1.00 is a perfect match.

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
