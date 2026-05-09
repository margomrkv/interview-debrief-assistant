# Splitter Validation Report

- **splitter**: `labeling/data/karpov_junior_ds_20220330.splitter.v3.mock.json`
- **video.md**: `transcripts/karpov-courses-собеседования/junior-data-scientist-собеседование-karpov-courses-20220330/video.md`
- **tolerance**: ±90s

## How this validation works

The validator uses `video.md` as a **ground-truth checklist** of what questions the video actually contains. `video.md` is the YouTube chapter list — it was written by the video authors independently of the transcript, so it is a clean external signal.

**Step 1 — Parse video chapters.**
Every line in the `## Chapters` block is extracted as a chapter: timestamp + title. Chapters whose titles start with words like "Разбор", "Объяснение", "Подводка к", etc. are classified as *explanations/transitions* and excluded from the question checklist. Only chapters that represent actual interview questions are kept.

**Step 2 — Match splitter items to chapters.**
For each question chapter, the validator looks for the splitter item whose `interviewer_question.time` is closest in time, within a ±90s window. The window is generous because chapter timestamps mark the *start of a topic segment*, while the splitter records the exact moment the interviewer starts speaking — these can differ by tens of seconds. Each splitter item can be matched to at most one chapter.

**Step 3 — Coverage % (the main quality signal).**
```
Coverage = matched question chapters / total question chapters × 100
```
A chapter is 'matched' if a splitter item was found within the time window. Coverage = 100% means every question the video authors marked was found by the splitter. A missing chapter means the splitter skipped that question entirely.

**Step 4 — Topic consistency %.**
```
Topic consistency = items with correct question_topic / all matched items with a known section × 100
```
For each matched item the validator checks that `question_topic` in the JSON is in the allowed set for the section that chapter belongs to:

- Section **Python** → allowed topics: ['Python']
- Section **A/B-тесты** → allowed topics: ['Experimentation', 'Statistics']
- Section **Работа с данными** → allowed topics: ['SQL', 'Python']
- Section **ML алгоритмы** → allowed topics: ['ML']

Note: one section can allow multiple topics. "A/B-тесты" accepts both `Experimentation` (experiment-design questions) and `Statistics` (t-test, normality, bootstrap questions) because both types appear in that section.

**Step 5 — Unmatched splitter items.**
Some splitter items are NOT matched to any video chapter. This is expected and not penalised. The video authors only marked top-level topic segments; the splitter also captures follow-up sub-questions and interviewer clarifications that have no dedicated chapter. These are listed for manual review, not counted as errors.

## Summary

| Metric | Value | Meaning |
|--------|-------|---------|
| Question chapters in video.md | 21 | Ground-truth checklist size |
| Matched to splitter item | 20 / 21 | Splitter found a matching item within ±90s |
| **Coverage** | **95%** | Main signal: did the splitter extract every question? |
| Unmatched question chapters | 1 | Questions in video that splitter missed |
| Unmatched splitter items | 2 | Sub-questions / follow-ups extracted by splitter; no chapter in video — not an error |
| **Topic consistency** | **20/20 (100%)** | question_topic label matches the video section |
| Avg timing drift | 27.2s | Mean |item time − chapter time| for matched pairs |
| Max timing drift | 82s | Worst-case match; still within tolerance |

## Section Breakdown

Compares the number of questions per section according to the video (ground truth) vs. the number of items the splitter extracted. Delta = splitter − video (positive = splitter found sub-questions beyond what video marked; negative = splitter missed questions).

| Section | Video Qs | Splitter items | Delta | Splitter topics |
|---------|----------|----------------|-------|-----------------|
| Python | 5 | 6 | ✅ +1 | `Python`, `Statistics` |
| A/B-тесты | 6 | 5 | ❌ -1 | `Experimentation`, `Statistics` |
| Работа с данными | 4 | 5 | ✅ +1 | `ML`, `Python`, `SQL` |
| ML алгоритмы | 6 | 6 | ✅ 0 | `ML` |

### Missing questions by section

**A/B-тесты**

- `00:36:04` Как быть, если нет старых пользователей, и нужно провести тест только на новых

## Chapter-by-Chapter Matching

Drift = `item time − chapter time` (positive = splitter item is later than chapter marker).

| # | Chapter time | Chapter title | Section | Item # | Item time | Drift | Topic |
|---|-------------|---------------|---------|--------|-----------|-------|-------|
| 1 | `00:02:30` | Вопрос на изменяемые и неизменяемые типы данных | Python | #1 | 00:02:41 | +11s | ✅ `Python` |
| 2 | `00:06:21` | Задача на dict и ответ Дмитрия | Python | #2 | 00:06:22 | +1s | ✅ `Python` |
| 3 | `00:10:38` | Задача, цель которой — сделать, чтобы дикты были раз | Python | #3 | 00:10:40 | +2s | ✅ `Python` |
| 4 | `00:16:10` | Вопрос о выделении и очистке памяти в Python, ответ  | Python | #4 | 00:16:05 | -5s | ✅ `Python` |
| 5 | `00:19:00` | Вопрос о генераторах, декораторах и итераторах | Python | #5 | 00:19:03 | +3s | ✅ `Python` |
| 6 | `00:20:35` | Вопрос о моделировании A/B теста | A/B-тесты | #6 | 00:21:32 | +57s | ✅ `Experimentation` |
| 7 | `00:30:57` | Вопрос о генерации распределений | A/B-тесты | #8 | 00:32:15 | +78s | ✅ `Statistics` |
| 8 | `00:32:26` | О необходимости нормальности распределения | A/B-тесты | #9 | 00:33:48 | +82s | ✅ `Statistics` |
| 9 | `00:33:46` | Тесты для проверки на нормальность | A/B-тесты | #10 | 00:34:24 | +38s | ✅ `Statistics` |
| 10 | `00:34:24` | Как сравнить ненормальные распределения | A/B-тесты | #11 | 00:35:31 | +67s | ✅ `Statistics` |
| 11 | `00:36:04` | Как быть, если нет старых пользователей, и нужно про | A/B-тесты | ❌ MISSING | — | — | — |
| 12 | `00:42:04` | Вопрос про разницу Where и Having | Работа с данными | #12 | 00:43:16 | +72s | ✅ `SQL` |
| 13 | `00:44:20` | вопрос про виды join и задания на join | Работа с данными | #13 | 00:44:22 | +2s | ✅ `SQL` |
| 14 | `00:45:57` | подводка к задаче про group by в Python | Работа с данными | #14 | 00:44:49 | -68s | ✅ `SQL` |
| 15 | `00:47:49` | Задача на group by в Python | Работа с данными | #15 | 00:47:37 | -12s | ✅ `Python` |
| 16 | `01:06:22` | Задача о линейных регрессиях | ML алгоритмы | #16 | 01:07:00 | +38s | ✅ `ML` |
| 17 | `01:09:47` | Вопрос о градиентном спуске | ML алгоритмы | #18 | 01:09:49 | +2s | ✅ `ML` |
| 18 | `01:14:06` | Вопрос о переобучении | ML алгоритмы | #19 | 01:14:09 | +3s | ✅ `ML` |
| 19 | `01:22:20` | Вопрос о деревьях и их построении | ML алгоритмы | #20 | 01:22:19 | -1s | ✅ `ML` |
| 20 | `01:26:04` | Вопрос: почему случайный лес работает хорошо и не пе | ML алгоритмы | #21 | 01:26:05 | +1s | ✅ `ML` |
| 21 | `01:28:20` | Последний вопрос со звездочкой: в каких случаях логи | ML алгоритмы | #22 | 01:28:19 | -1s | ✅ `ML` |

## Unmatched Splitter Items

These items were extracted by the splitter but have **no corresponding chapter** in `video.md`. This is **not an error** — the video authors only marked major topic transitions, not every follow-up question. Review these to confirm they are legitimate sub-questions or interviewer clarifications rather than hallucinated content.

| Item # | Time | Topic | Question (first 70 chars) |
|--------|------|-------|--------------------------|
| #7 | 00:27:29 | `Statistics` | прости пожалуйста пока ты не ушёл далеко в сторону — вспомни метрики,  |
| #17 | 01:07:26 | `ML` | a0 + bx — какие коэффициенты с помощью обучения мы подбираем? Расскажи |

## Skipped Chapters (explanations / transitions)

Chapters excluded from the question checklist because their titles indicate they contain an explanation, task walkthrough, or segment transition rather than a new interview question. These are not checked for splitter coverage.

- `00:00:00` [—] Введение.
- `00:00:50` [—] О структуре и секциях, которые входят в интервью.
- `00:08:15` [Python] Объяснение первой задачи
- `00:13:51` [Python] Разбор второй задачи
- `00:16:26` [Python] Разбор вопроса
- `00:31:22` [A/B-тесты] Подводка к критерию стьюдента и вопрос про ограничения его применения
- `00:35:02` [A/B-тесты] Подводка к вопросу о нормальности распределения средних при бутстрапе
- `00:37:53` [A/B-тесты] Какие еще бывают вопросы и общие рассуждения
- `00:41:19` [A/B-тесты] Интерпретация Bootstrap
- `01:32:18` [ML алгоритмы] Конец, обратная связь

## Verdict: ✅ PASS

**Coverage** 95% = 20 out of 21 question chapters were found by the splitter within ±90s.  
**Topic consistency** 100% = 20 out of 20 matched items have a `question_topic` label that matches the video section.
