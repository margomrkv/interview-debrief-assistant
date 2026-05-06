# Labeling Workspace

This folder contains prompts and configuration for transcript annotation.

## Structure

- `prompts/system_prompt_v2.txt` - main system prompt for annotation behavior.
- `prompts/user_prompt_template_v2.txt` - run template for a specific interview.
- `prompts/output_schema_v1.json` - strict JSON schema for structured output.
- `config/interview_paths.md` - current input paths and source ids.
- `data/` - place generated JSON outputs here.

## Recommended run settings

- Temperature: `0`
- Structured output: enforce `output_schema_v1.json`
- Use transcript from `config/interview_paths.md`

## Behavioral rule

Apply `STAR_*` and `SCID_*` only when `question_type = behavioral`.
For non-behavioral questions set these fields to `null`.
