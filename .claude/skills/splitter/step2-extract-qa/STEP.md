# Шаг 2 — Извлечение Q&A

**Только LLM** (агент в чате). Отдельного скрипта нет.

**Модель:** `step1-prepare/run_config.json` → `inference.model` (по умолчанию `claude-sonnet-4-6`, temperature 0). Не менять без явного запроса пользователя.

**Вход:** секция `LLM_INPUT_STEP_2` в `splitter_output/.../*.vN.pipeline-log.md` (создаётся шагом 1 для **этой** `vN`).

**Выход:** `splitter_output/.../*.vN.qa-split.json` — **полная перезапись** файла.

## Запрещено (наследование прошлых прогонов)

- Не открывать и не копировать `{basename}.v1.qa-split.json`, `v2`, … любую версию **кроме** целевой `vN` из вывода шага 1.
- Не «переносить» `items[]` из старого JSON, не править schema точечно поверх прошлого прогона.
- Единственный источник пар Q&A: **`PRIMARY_TRANSCRIPT`** в `LLM_INPUT_STEP_2` текущего `pipeline-log.md`.

См. `.claude/skills/splitter/SKILL.md` — раздел **«Каждый прогон с нуля»**.

## Разделение спикеров

- `candidate_answer` — только кандидат (весь turn до следующего вопроса интервьюера).
- `interviewer_feedback` — только интервьюер в окне этого item; иначе `null`.
- Не класть продолжение ответа кандидата в `interviewer_feedback` (типичная ошибка на behavioral-интервью).

## Вопрос ≠ ответ (behavioral без diarization)

- **Запрещено** дублировать один и тот же фрагмент транскрипта в `interviewer_question` и `candidate_answer`.
- **Запрещено** использовать `video.md` или заголовки глав YouTube на шаге 2 — их нет в `LLM_INPUT_STEP_2` и не будет в real-интервью.
- Обрывки ASR — **склеить соседние реплики интервьюера** в транскрипте; не «улучшать» вопрос по внешнему оглавлению.
- Перед сохранением JSON: если первые ≥6 слов ответа = первые слова вопроса → переразметить span (см. `splitter_system_prompt.txt` § `interviewer_question vs candidate_answer`).

Промпт: `step1-prepare/splitter_system_prompt.txt` (§ `interviewer_feedback`).

См. `.claude/skills/splitter/SKILL.md` — шаг 2 и протокол для пользователя.
