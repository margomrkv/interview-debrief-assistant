# Labeling Workspace

This folder contains prompts, configuration, and tooling for transcript annotation.

## How to run the splitter

Use **`prepare_prompt.py`** → open `labeling/data/<source_id>.prompt.txt` in **Claude Code**, **Cursor**, or **claude.ai** (your subscription) → save JSON → `splitter_json_to_excel.py` + `validate_splitter_vs_video.py`. See `CLAUDE_CODE_GUIDE.md`.

| Path | Billing |
|------|---------|
| **Subscription** | Claude **Pro / Max**, **Cursor**, **Claude Code** — run extraction in chat using the bundled `.prompt.txt`; no API key |

## Scripts

| Script | Purpose |
|--------|---------|
| `prepare_prompt.py` | Bundle system + user prompts + schema + transcript/sidecars into one `.prompt.txt` |
| `splitter_json_to_excel.py` | Convert splitter JSON (LinkedText) to XLSX |
| `validate_splitter_vs_video.py` | Cross-validate splitter output against YouTube `video.md` chapters |
| `json_to_excel.py` | Generic JSON → XLSX converter |

## Prompts & config

| File | Purpose |
|------|---------|
| `prompts/system_prompt_v2.txt` | Main system prompt controlling extraction behavior |
| `prompts/user_prompt_template_v2.txt` | User prompt template for `raw_split` mode |
| `prompts/user_prompt_template_mock_assisted_v2.txt` | User prompt template for `mock_assisted_split` mode |
| `prompts/splitter_output_schema_v1.json` | Strict JSON schema for splitter output (LinkedText contract) |
| `config/splitter_run_config.json` | Optional paths for system/user prompts and schema (`prepare_prompt.py`). Fields like `model` / `temperature` are hints for chat runs, not API calls |
| `config/interview_paths.md` | Current input paths and source IDs |

## Output files in `data/`

All output files for a given run share the same base name and live in `data/`.
Naming convention: `<source_id>.splitter.<version>.<mode>.<ext>`

| Extension | Content |
|-----------|---------|
| `.json` | Raw splitter output (LinkedText schema) |
| `.xlsx` | Excel export — human-readable review |
| `.validation.md` | Validation report from `validate_splitter_vs_video.py` |

Example for `source_id=karpov_junior_ds_20220330`, version `v4`, mode `mock`:
```
data/karpov_junior_ds_20220330.splitter.v4.mock.json         ← splitter output
data/karpov_junior_ds_20220330.splitter.v4.mock.xlsx         ← excel export
data/karpov_junior_ds_20220330.splitter.v4.mock.validation.md ← validation report
```

## Recommended run settings

- Temperature: `0` (fixed in `config/splitter_run_config.json`)
- Structured output: enforce `splitter_output_schema_v1.json`
- For mock interviews: use `timecodes.txt` as transcript; exclude `video.md` from context (reserve for post-run validation only)

## Behavioral rule

Apply `STAR_*` and `SCID_*` only when `question_type = behavioral`.
For non-behavioral questions set these fields to `null`.
