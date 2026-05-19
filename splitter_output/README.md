# Splitter output

Last updated: 2026-05-19

## Layout

Same corpus split as `transcripts/`, but **leaf names omit `mock-` / `real-`** (kind is only in the parent folder):

```text
splitter_output/mock-interviews/<publisher>/<basename>/
splitter_output/real-interviews/<publisher>/<basename>/
```

## File naming (canonical)

**Version immediately after basename** — filter one run with `*{basename}.v8*`:

```text
{basename}.v{N}.qa-split.json          # главный результат Q&A
{basename}.v{N}.qa-split.xlsx
{basename}.v{N}.validation.md          # отчёт валидации (+ приложение LLM в конце)
{basename}.v{N}.validation.llm.json    # служебный JSON шага 5
{basename}.v{N}.llm-input.txt           # снимок промпта шага 2
{basename}.v{N}.user-prompt.txt         # user-часть (без system)
{basename}.v{N}.run.json                # протокол прогона (модели, шаги, in/out)
{basename}.v{N}.run.md                  # тот же протокол для чтения
```

Пример (все файлы v8):

```text
data-scientist-junior-karpov-2022-03-30.v8.qa-split.json
data-scientist-junior-karpov-2022-03-30.v8.validation.md
data-scientist-junior-karpov-2022-03-30.v8.run.md
```

### Legacy (до 2026-05-19)

```text
{basename}.qa-split.v{N}.json
{basename}.qa-split.validation.v{N}.md
…
```

Миграция: `python3 scripts/migrate_splitter_v_prefix_names.py` (поддерживается чтение обоих форматов).

`source_id` in JSON = leaf folder name with `-` → `_`.

Version `vN`: next free index per interview folder (`artifact_paths.next_version`).
