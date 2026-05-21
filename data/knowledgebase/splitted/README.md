# Splitter output

Last updated: 2026-05-20

## Layout

Same corpus split as `transcripts/`, but **leaf names omit `mock-` / `real-`** (kind is only in the parent folder):

```text
splitter_output/mock-interviews/<publisher>/<basename>/
splitter_output/real-interviews/<publisher>/<basename>/
```

## File naming (canonical) — **4 files per run**

**Version immediately after basename** — filter one run with `*{basename}.v8*`:

```text
{basename}.v{N}.qa-split.json           # главный результат Q&A
{basename}.v{N}.qa-split.xlsx           # Excel для человека
{basename}.v{N}.validation-report.md    # отчёт валидации + JSON шага 5 в конце
{basename}.v{N}.pipeline-log.md         # журнал прогона + промпты LLM (шаги 2 и 5)
```

**Внутри `pipeline-log.md`:**

- `<!-- PIPELINE_MANIFEST ... -->` — машинный журнал шагов (для скриптов)
- `<!-- LLM_INPUT_STEP_2 -->` / `_5` — что подавали модели

**Внутри `validation-report.md`:**

- `<!-- SEMANTIC_VALIDATION -->` … `<!-- /SEMANTIC_VALIDATION -->` — ответ LLM шага 5 (```json)

Пример (v9):

```text
data-scientist-junior-karpov-2022-03-30.v9.qa-split.json
data-scientist-junior-karpov-2022-03-30.v9.qa-split.xlsx
data-scientist-junior-karpov-2022-03-30.v9.validation-report.md
data-scientist-junior-karpov-2022-03-30.v9.pipeline-log.md
```

### Legacy (удалены при миграции)

`*.pipeline-log.json`, `*.validation-semantic.json`, `*.llm-input.txt`, `*.run.json`, …

```bash
python3 scripts/migrate_splitter_consolidate_json.py
```

`source_id` in JSON = leaf folder name with `-` → `_`.

Version `vN`: `artifact_paths.next_version` — each `vN` is a **separate full run**; step 2 must **not** copy QA from `v(N-1).qa-split.json` (see `.claude/skills/splitter/SKILL.md` → «Каждый прогон с нуля»).
