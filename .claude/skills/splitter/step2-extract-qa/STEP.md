# Шаг 2 — Извлечение Q&A

**Только LLM** (агент в чате). Отдельного скрипта нет.

**Модель:** `step1-prepare/run_config.json` → `inference.model` (по умолчанию `claude-sonnet-4-6`, temperature 0). Не менять без явного запроса пользователя.

**Вход:** секция `LLM_INPUT_STEP_2` в `data/knowledgebase/splitted/.../*.vN.pipeline-log.md` (создаётся шагом 1 для **этой** `vN`).

**Выход:** `data/knowledgebase/splitted/.../*.vN.qa-split.json` — **полная перезапись** файла.

## Запрещено (наследование прошлых прогонов) — hard

- Не открывать и не копировать `{basename}.v1.qa-split.json`, `v2`, … `v(N-1)` — список в `pipeline-log.md` → `forbidden_prior_artifacts`.
- Не «переносить» `items[]` из старого JSON, не править schema точечно поверх прошлого прогона.
- Шаг 1 создаёт **пустой** `{basename}.vN.qa-split.json` — единственный допустимый файл для записи.

## После сохранения JSON (обязательно)

```bash
python3 .claude/skills/splitter/step1-prepare/splitter_check_prior_leak.py \
  data/knowledgebase/splitted/.../{basename}.vN.qa-split.json
```

Exit **0** — ок. Exit **1** — JSON идентичен старой версии → прогон невалиден, извлечь заново из `PRIMARY_TRANSCRIPT`.
- Единственный источник пар Q&A: **`PRIMARY_TRANSCRIPT`** в `LLM_INPUT_STEP_2` текущего `pipeline-log.md`.

См. `.claude/skills/splitter/SKILL.md` — раздел **«Каждый прогон с нуля»**.

## Разделение спикеров

- `candidate_answer` — только кандидат (весь turn до следующего вопроса интервьюера).
- `interviewer_feedback` — только интервьюер в окне этого item; иначе `null`.
- Не класть продолжение ответа кандидата в `interviewer_feedback` (типичная ошибка на behavioral-интервью).

### Pair programming (`technical_coding`)

Реплики **чередуются каждые несколько секунд** — режьте по смыслу внутри строки `timecodes.txt` (§11 в system prompt).

- В `candidate_answer` — только «я бы», «не понимаю», описание своего кода.
- В `interviewer_feedback` — «давай напиши», «ты видишь», «не слушай ты усложняешь», «проговори» (блок может быть длинным).
- Не сливайте обоих в один `candidate_answer`, даже если так проще «сохранить весь диалог».

## Вопрос ≠ ответ (behavioral без diarization)

- **Запрещено** дублировать один и тот же фрагмент транскрипта в `interviewer_question` и `candidate_answer`.
- **Запрещено** использовать `video.md` или заголовки глав YouTube на шаге 2 — их нет в `LLM_INPUT_STEP_2` и не будет в real-интервью.
- Обрывки ASR — **склеить соседние реплики интервьюера** в транскрипте; не «улучшать» вопрос по внешнему оглавлению.
- Перед сохранением JSON: если первые ≥6 слов ответа = первые слова вопроса → переразметить span (см. `splitter_system_prompt.txt` § `interviewer_question vs candidate_answer`).

Промпт: `step1-prepare/splitter_system_prompt.txt` (§ `interviewer_feedback`).

См. `.claude/skills/splitter/SKILL.md` — шаг 2 и протокол для пользователя.
