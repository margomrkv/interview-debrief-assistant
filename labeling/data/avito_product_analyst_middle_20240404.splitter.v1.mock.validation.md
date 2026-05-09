# Splitter Validation Report

- **splitter**: `labeling/data/avito_product_analyst_middle_20240404.splitter.v1.mock.json`
- **video.md**: `transcripts/mock-avito-product-analyst-middle-2024-04-04/video.md`
- **tolerance**: ±120s

## How this validation works

The validator uses `video.md` as a **ground-truth checklist** of what questions the video actually contains. `video.md` is the YouTube chapter list — it was written by the video authors independently of the transcript, so it is a clean external signal.

**Step 1 — Parse video chapters.**
Every line in the `## Chapters` block is extracted as a chapter: timestamp + title. Chapters whose titles start with words like "Разбор", "Объяснение", "Подводка к", etc. are classified as *explanations/transitions* and excluded from the question checklist. Only chapters that represent actual interview questions are kept.

**Step 2 — Match splitter items to chapters.**
For each question chapter, the validator looks for the splitter item whose `interviewer_question.time` is closest in time, within a ±120s window. The window is generous because chapter timestamps mark the *start of a topic segment*, while the splitter records the exact moment the interviewer starts speaking — these can differ by tens of seconds. Each splitter item can be matched to at most one chapter.

**Step 3 — Coverage % (the main quality signal).**
```
Coverage = matched question chapters / total question chapters × 100
```
A chapter is 'matched' if a splitter item was found within the time window. Coverage = 100% means every question the video authors marked was found by the splitter. A missing chapter means the splitter skipped that question entirely.

**Step 4 — Topic consistency %.**
_No `--section-config` provided — topic consistency check is skipped for this interview. Only coverage is validated._

**Step 5 — Unmatched splitter items.**
Some splitter items are NOT matched to any video chapter. This is expected and not penalised. The video authors only marked top-level topic segments; the splitter also captures follow-up sub-questions and interviewer clarifications that have no dedicated chapter. These are listed for manual review, not counted as errors.

## Summary

| Metric | Value | Meaning |
|--------|-------|---------|
| Question chapters in video.md | 14 | Ground-truth checklist size |
| Matched to splitter item | 13 / 14 | Splitter found a matching item within ±120s |
| **Coverage** | **93%** | Main signal: did the splitter extract every question? |
| Unmatched question chapters | 1 | Questions in video that splitter missed |
| Unmatched splitter items | 3 | Sub-questions / follow-ups extracted by splitter; no chapter in video — not an error |
| Topic consistency | — | No section mapping available |
| Avg timing drift | 13.1s | Mean |item time − chapter time| for matched pairs |
| Max timing drift | 82s | Worst-case match; still within tolerance |

## Section Breakdown

Compares the number of questions per section according to the video (ground truth) vs. the number of items the splitter extracted. Delta = splitter − video (positive = splitter found sub-questions beyond what video marked; negative = splitter missed questions).

| Section | Video Qs | Splitter items | Delta | Splitter topics |
|---------|----------|----------------|-------|-----------------|

## Chapter-by-Chapter Matching

Drift = `item time − chapter time` (positive = splitter item is later than chapter marker).

| # | Chapter time | Chapter title | Section | Item # | Item time | Drift | Topic |
|---|-------------|---------------|---------|--------|-----------|-------|-------|
| 1 | `00:07:34` | Рассказ Вовы про свой опыт | — | #1 | 00:07:34 | +0s | `Behavioral` |
| 2 | `00:12:06` | Уточняющие вопросы Егора про SQL- запросы | — | #2 | 00:12:06 | +0s | `SQL` |
| 3 | `00:15:05` | Вопросы про Python | — | #4 | 00:15:05 | +0s | `Python` |
| 4 | `00:17:07` | Вопросы про ML | — | #5 | 00:17:07 | +0s | `ML` |
| 5 | `00:18:05` | Рассказ Вовы про рабочие кейсы | — | #6 | 00:19:27 | +82s | `Behavioral` |
| 6 | `00:25:28` | Вопросы Егора про опыт | — | ❌ MISSING | — | — | — |
| 7 | `00:26:00` | Как формируются задачи | — | #7 | 00:26:00 | +0s | `Behavioral` |
| 8 | `00:28:40` | Как происходит планирование | — | #8 | 00:28:40 | +0s | `Behavioral` |
| 9 | `00:32:00` | Взаимодействие с коллегами и приоритизация задач | — | #9 | 00:32:17 | +17s | `Behavioral` |
| 10 | `00:34:45` | Принятие решений | — | #10 | 00:34:34 | -11s | `Behavioral` |
| 11 | `00:36:03` | Пример задачи с неопределенностью | — | #11 | 00:36:03 | +0s | `Experimentation` |
| 12 | `00:41:12` | Пример задачи со сложными аналитическими подходами | — | #12 | 00:41:12 | +0s | `Statistics` |
| 13 | `00:44:54` | Техническая задача про кубик | — | #13 | 00:44:54 | +0s | `Statistics` |
| 14 | `00:55:50` | Продуктовый кейс на примере Telegram | — | #14 | 00:56:50 | +60s | `Product` |

## Unmatched Splitter Items

These items were extracted by the splitter but have **no corresponding chapter** in `video.md`. This is **not an error** — the video authors only marked major topic transitions, not every follow-up question. Review these to confirm they are legitimate sub-questions or interviewer clarifications rather than hallucinated content.

| Item # | Time | Topic | Question (first 70 chars) |
|--------|------|-------|--------------------------|
| #3 | 00:14:20 | `SQL` | план запроса смотрел? использовал вообще этот инструмент? |
| #15 | 00:59:11 | `Product` | давай представим что ты аналитик по ту сторону экрана — получаешь фидб |
| #16 | 01:20:00 | `Experimentation` | если мы говорим о проверке этой гипотезы с помощью A/B теста — как бы  |

## Skipped Chapters (explanations / transitions)

Chapters excluded from the question checklist because their titles indicate they contain an explanation, task walkthrough, or segment transition rather than a new interview question. These are not checked for splitter coverage.

- `00:00:00` [—] Начало трансляции
- `00:03:57` [—] Приветствие
- `00:05:47` [—] Представление интервьюера и кандидата
- `00:06:49` [—] Начало собеседования: вводное слово и план интервью
- `01:44:05` [—] Завершение собеседования
- `01:45:59` [—] Комментирование собеседования
- `01:46:35` [—] Зачем задаем именно эти вопросы?
- `01:52:34` [—] Фидбек Вове по собеседованию по матрице компетенций аналитиков Авито

## Verdict: ✅ PASS

**Coverage** 93% = 13 out of 14 question chapters were found by the splitter within ±120s.  
**Topic consistency** 100% = 0 out of 0 matched items have a `question_topic` label that matches the video section.
