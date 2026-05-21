# Шаг 5 — Семантическая проверка (LLM)

**Только LLM** (агент в чате, как шаг 2). Отдельного обязательного API в shell нет.

**Модель:** `step1-prepare/run_config.json` → `validation_inference.model` (по умолчанию `claude-sonnet-4-6`, temperature 0).

**Вход:** секция `LLM_INPUT_STEP_5` в `data/knowledgebase/splitted/.../*.vN.pipeline-log.md` (создаётся шагом 4 / `splitter_post.sh --prepare-llm`).

**Выход:**

1. JSON по `validation_llm_output_schema.json` → блок `<!-- SEMANTIC_VALIDATION -->` в `*.vN.validation-report.md`
2. Перезапуск `splitter_validate_video.py` (те же `--splitter --video --out`) — строки шага 5 **сливаются** с шагом 4 в деталях по главам

3. После шага 5 — **цикл исправления** в `SKILL.md`: `splitter_verdict.py` на `*.validation-report.md`; при провале — правки промпта/skill → новая `vN+1` → шаги 1–5 (макс. 2 ретрая).

**Полный прогон `/splitter` не завершать без шага 5**, если есть `video.md`.

См. `.claude/skills/splitter/SKILL.md` — шаг 5 и протокол для пользователя.
