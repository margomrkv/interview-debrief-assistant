# Шаг 2 — Извлечение Q&A

**Только LLM** (агент в чате). Отдельного скрипта нет.

**Модель:** `step1-prepare/run_config.json` → `inference.model` (по умолчанию `claude-sonnet-4-6`, temperature 0). Не менять без явного запроса пользователя.

**Вход:** `splitter_output/.../*.qa-split.llm-input.vN.txt` (создаётся шагом 1).

**Выход:** `splitter_output/.../*.qa-split.vN.json`

Промпт и схема уже внутри `llm-input` (файлы шага 1: `splitter_system_prompt.txt`, `splitter_output_schema.json`).

См. `.claude/skills/splitter/SKILL.md` — шаг 2 и протокол для пользователя.
