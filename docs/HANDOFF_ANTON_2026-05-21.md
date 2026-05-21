# Handoff для Антона — 2026-05-21

**От:** Rita · **Ухожу до ~20:00**, вернусь после 20:00.  
**Сделано сегодня:** `git commit` + `push` (README + доработанный project report).

---

## Что сделала

1. **[`README.md`](../README.md)** — точка входа в репо, code freeze 2026-05-21, карта папок.
2. **[`docs/PROJECT_OVERVIEW.md`](PROJECT_OVERVIEW.md)** — **основной отчёт / задел под презентацию** (checkpoint + defense):
   - что такое **main output** (debrief report, не JSON);
   - таблица под **rubric Technical Implementation**;
   - метрики Splitter + Evaluator (что значит golden, MAPE, accuracy ±1, worst cases);
   - **integration tests** vs unit — простым языком + что в `pytest tests/`;
   - **logging** — где лежат промпты и ответы LLM;
   - **сквозной пример mock** (Karpov junior DS v11) — заполнен;
   - **сквозной пример real** — **пустой блок, тебе дописать**;
   - **чеклист в конце файла** — что тебе проверить перед защитой.

3. **Splitter — наблюдение (не баг-репорт на весь корпус):**  
   На **длинных сессиях с live coding** сплиттер путает границы реплик: в субтитрах нет speaker labels, промпт заточен под чередование «интервьюер → кандидат», а в кодинге реплики перемешаны → иногда **поджевывает блоки** (feedback уезжает в answer и т.п.).  
   **Решение до freeze:** не перезапускать сплиттер на **всех** mock-interviews; корпус для train уже достаточный. Могу сегодня слегка подкрутить промпт — без массового re-run.

---

## Что нужно от тебя

| # | Задача | Где |
|---|--------|-----|
| 1 | **Проверить** `PROJECT_OVERVIEW.md` — факты, цифры train run, пути | весь файл |
| 2 | **Вставить метрики** последнего KB train (test score, accuracy ±1, run_id) | секция *Evaluator*, блок `[TBD — Anton]` |
| 3 | **Один сквозной пример real interview** — папка в `data/candidatecontext/`, входы, путь к `feedback-report.blind.md`, 2–3 предложения про verdict | секция *End-to-end example (real interview)* |
| 4 | Отметить в чеклисте внизу `PROJECT_OVERVIEW.md`, что проверено | *Handoff checklist* |

Файлы из Telegram (`train_report.md`, `evaluator_prompt.md`, …) — это как раз п.2; можно вставить в отчёт или сослаться на `runs/2026-05-20_20-45-53/`.

---

## Приоритеты до code freeze (сегодня вечером)

- Закрыть **отчёт + цифры Evaluator** (ты).
- **Не** блокировать freeze полным re-split mock-корпуса (я).
- Soft / behavioral train — **после freeze**, на защите можно сказать «hard done, rest roadmap».

---

## Быстрые ссылки

- Отчёт: [`docs/PROJECT_OVERVIEW.md`](PROJECT_OVERVIEW.md)
- Пример debrief: `data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/`
- Пример mock split: `data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/*.v11.*`
- Критерии курса: `review/Project Criteria & Scoring.docx`
