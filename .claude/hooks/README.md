---
author: claude-code-opus-4-7
created_date: 2026-05-04
---

Хуки Claude Code для проекта.

## validate_mermaid.mjs

Валидирует ```mermaid``` блоки, которые Claude Code генерирует — в .md-файлах (PostToolUse: Write/Edit/MultiEdit) и в чат-ответах (Stop hook). При ошибке парсинга возвращает Claude'у `decision: block` с сообщением парсера, чтобы тот починил блок в той же итерации.

## Setup (один раз после клона репо)

```bash
cd .claude/hooks && npm install
```

Тянет пакет `mermaid` (~30 МБ), без headless-браузера. Используется только парсер (`mermaid.parse`), без рендера.

## Кеш

`.mermaid-cache.json` хранит SHA256 уже провалидированных блоков. Если `mermaid` обновится и старый блок станет невалидным — удалить руками: `rm .claude/hooks/.mermaid-cache.json`.

## Откатить хук временно

В `.claude/settings.json` удалить нужную секцию `PostToolUse` / `Stop`, либо положить override в `.claude/settings.local.json` (gitignored).
