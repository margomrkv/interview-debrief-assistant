# UI emulator

Web UI for the two-stage pipeline (**Splitter → Scoring**), streamed asynchronously **without LLM calls** — both stages replay precomputed fixtures from `data/emulator-data/`.

## Run

```bash
python3 src/ui/app.py        # http://127.0.0.1:8000
python3 src/ui/app.py 18000  # custom port
```

Stdlib only — no extra install for emulator mode. No authentication (local demo).

## Layout

```text
src/ui/
├── app.py        # stdlib HTTP server + SSE stream
├── emulator.py   # loads emulator-data, joins qa ↔ scores by id
└── static/       # single-page frontend (index.html, app.js, styles.css)
```

Each folder under `data/emulator-data/**/` is one interview (`source_id`):

- `transcript.txt` — Splitter input (what the user “uploads”);
- `qa.json` — Splitter output (Q&A metadata, no scores);
- `scores.json` — Scoring output (`factual_correctness` / `focus` / `clarity` + rollup).

To add an interview, place `qa.json` and `scores.json` next to its `transcript.txt`; restart the server.

## Default demo

`data_scientist_middle_google_data_wrangling_interviewing_io_2020_04_28` — English
Interviewing.io case interview (filesystem + hashing + MapReduce). Rebuild fixture:

```bash
python3 scripts/build_emulator_fixture.py \
  --split data/knowledgebase/splitted/mock-interviews/interviewing-io/data-scientist-middle-google-data-wrangling-interviewing-io-2020-04-28/data-scientist-middle-google-data-wrangling-interviewing-io-2020-04-28.v1.qa-split.json \
  --raw-dir data/knowledgebase/raw/mock-interviews/interviewing-io/data-scientist-middle-google-data-wrangling-interviewing-io-2020-04-28 \
  --out-dir data/emulator-data/interviewing-io/data-scientist-middle-google-data-wrangling-interviewing-io-2020-04-28
```
