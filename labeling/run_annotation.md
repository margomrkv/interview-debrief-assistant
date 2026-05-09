# Run Annotation

Last updated: 2026-05-06

## 1) Inputs

- System prompt: `labeling/prompts/system_prompt_v2.txt`
- User prompt (real interviews): `labeling/prompts/user_prompt_template_v2.txt`
- User prompt (mock-assisted): `labeling/prompts/user_prompt_template_mock_assisted_v2.txt`
- Output schema: `labeling/prompts/splitter_output_schema_v1.json`
- Interview paths: `labeling/config/interview_paths.md`

## 2) Recommended model settings

- Temperature: `0`
- Structured output: enabled with `splitter_output_schema_v1.json`
- Response format: strict JSON only

## 3) Run in Cursor / Claude Code (manual)

1. Open system prompt and copy it into system message.
2. Choose user prompt template by mode:
   - `raw_split`: transcript only (real interviews).
   - `mock_assisted_split`: transcript + sidecars (`timecodes.txt`, `video.md`, optional `feedback.md`).
3. Copy chosen user prompt into user message.
4. Attach transcript content from the target path in `interview_paths.md`.
5. For `mock_assisted_split`, also attach sidecar files from `interview_paths.md`.
6. Enforce schema from `splitter_output_schema_v1.json` (strict mode, no extra keys).
7. Run generation.

## 3.1) Run with CLI (automated)

Prerequisite:
- `ANTHROPIC_API_KEY` environment variable is set.
- Python dependency installed: `pip install anthropic`

Raw mode (transcript only):

```bash
python labeling/run_splitter_cli.py \
  --source-id karpov_junior_ds_20220330 \
  --mode raw_split \
  --model claude-sonnet-4-20250514 \
  --transcript transcripts/karpov-courses-собеседования/junior-data-scientist-собеседование-karpov-courses-20220330/transcript.txt \
  --out labeling/data/karpov_junior_ds_20220330.raw_splitter.v3.json
```

Mock-assisted mode (with sidecars):

```bash
python labeling/run_splitter_cli.py \
  --source-id karpov_junior_ds_20220330 \
  --mode mock_assisted_split \
  --model claude-sonnet-4-20250514 \
  --transcript transcripts/karpov-courses-собеседования/junior-data-scientist-собеседование-karpov-courses-20220330/transcript.txt \
  --timecodes transcripts/karpov-courses-собеседования/junior-data-scientist-собеседование-karpov-courses-20220330/timecodes.txt \
  --video transcripts/karpov-courses-собеседования/junior-data-scientist-собеседование-karpov-courses-20220330/video.md \
  --feedback transcripts/karpov-courses-собеседования/junior-data-scientist-собеседование-karpov-courses-20220330/feedback.md \
  --out labeling/data/karpov_junior_ds_20220330.mock_assisted_splitter.v3.json
```

## 4) Save output

- Save JSON result to:
  - `labeling/data/<source_id>.splitter.v2.json`
- Example:
  - `labeling/data/karpov_junior_ds_20220330.splitter.v2.json`

## 5) Quick validation checklist

- Top-level keys exist: `source_id`, `splitter_mode`, `items`
- Every item includes splitter fields from updated CSV:
  - `interviewer_question.{text,time}`
  - `candidate_answer.{text,time}`
  - `reference_answer.{text,time}`
  - `interviewer_feedback.{text,time}`
  - `question_type`, `question_topic`, `interview_stage`
- One interviewer question -> one item (no grouped questions)
- Text fields are verbatim excerpts (not summaries)
- No score/assessment/evaluation fields in splitter output

## 6) Convert JSON to tabular format (optional)

If needed for Excel (splitter output):

```bash
python labeling/splitter_json_to_excel.py labeling/data/<source_id>.splitter.v2.json
```

Optional custom output path:

```bash
python labeling/splitter_json_to_excel.py labeling/data/<source_id>.splitter.v2.json --out labeling/data/<source_id>.splitter.v2.xlsx
```

Output workbook sheets:
- `splitter_items` (flattened LinkedText fields)
- `meta` (top-level metadata and counts)

## 7) Versioning convention

- Prompt changes: bump prompt version in filename (e.g., `system_prompt_v3.txt`)
- Schema changes: bump schema version (e.g., `output_schema_v2.json`)
- Output changes: bump annotation version (`.v2.json`)
