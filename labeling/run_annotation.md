# Run Annotation

Last updated: 2026-05-06

## 1) Inputs

- System prompt: `labeling/prompts/system_prompt_v2.txt`
- User prompt: `labeling/prompts/user_prompt_template_v2.txt`
- Output schema: `labeling/prompts/output_schema_v1.json`
- Interview paths: `labeling/config/interview_paths.md`

## 2) Recommended model settings

- Temperature: `0`
- Structured output: enabled with `output_schema_v1.json`
- Response format: strict JSON only

## 3) Run in Cursor / Claude Code (manual)

1. Open system prompt and copy it into system message.
2. Open user prompt template and copy it into user message.
3. Attach transcript content from the target path in `interview_paths.md`.
4. Enforce schema from `output_schema_v1.json`.
5. Run generation.

## 4) Save output

- Save JSON result to:
  - `labeling/data/<source_id>.annotation.v1.json`
- Example:
  - `labeling/data/karpov_junior_ds_20220330.annotation.v1.json`

## 5) Quick validation checklist

- Top-level keys exist: `source_id`, `items`, `summary`
- Every item has required fields from schema
- `model_answer` is present for each item
- `STAR_*` and `SCID_*` are:
  - filled only for `question_type = behavioral`
  - `null` for non-behavioral
- `question_fit` and `focus` are only `0` or `1`
- `clarity`, `completeness`, `accuracy`, `SCID_*` are within `0..3`
- labels exist for 0..3 metrics:
  - `clarity_label`, `completeness_label`, `accuracy_label`
  - `SCID_S_label`, `SCID_C_label`, `SCID_I_label`, `SCID_D_label`

## 6) Convert JSON to tabular format (optional)

If needed for Excel:

Use converter script:

```bash
python labeling/json_to_excel.py labeling/data/<source_id>.annotation.v1.json
```

Optional custom output path:

```bash
python labeling/json_to_excel.py labeling/data/<source_id>.annotation.v1.json --out labeling/data/<source_id>.annotation.v1.xlsx
```

Output workbook sheets:
- `items` (fixed annotation columns)
- `summary` (top-level metadata and counts)

## 7) Versioning convention

- Prompt changes: bump prompt version in filename (e.g., `system_prompt_v3.txt`)
- Schema changes: bump schema version (e.g., `output_schema_v2.json`)
- Output changes: bump annotation version (`.v2.json`)
