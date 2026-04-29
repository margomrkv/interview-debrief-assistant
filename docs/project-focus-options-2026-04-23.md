# Project Focus Options (for separate review)

**Date:** 2026-04-23  
**Purpose:** Зафиксировать идеи и варианты перефокусировки отдельно от meeting transcript и project hub.

## Context

- Источник тем: `docs/Intro to AI Agents_ Projects.xlsx` (лист `Projects`, темы `1.0-30.0`).
- Релевантное сравнение:
  - `4.0 Interview prep coach` — интерактивный multi-turn коуч.
  - `12.0 Job interview coach` — пост-анализ `JD + CV + transcript`.
- Наблюдение: у большинства тем в таблице четко определены input/output и expected result, что упрощает оценку качества.

## Варианты фокуса

## Option A (recommended): Interview Transcript Reviewer v1

- **Фокус:** пост-анализ уже прошедшего интервью.
- **Input:** `job_description`, `cv`, `transcript` (опционально `interviewer_feedback` как reference).
- **Output (фиксированный):**
  - `coverage map`,
  - `3 strengths`,
  - `3 gaps`,
  - `2 rewrites`,
  - `rubric scores`.
- **Почему реалистично:** меньше неопределенности, проще сделать reproducible eval.

## Option B: Interview Preparation Planner

- **Фокус:** персональный план подготовки к собеседованиям на 7-14 дней.
- **Input:** CV + target JD + прошлые транскрипты + учебные материалы.
- **Output:** приоритизированный план обучения/подготовки с action items.
- **Риск:** больше субъективности в оценке качества.

## Option C: Ingestion + Knowledge Base for job search materials

- **Фокус:** сбор и структурирование учебных материалов (включая транскрипты).
- **Input:** YouTube playlists / заметки / транскрипты интервью.
- **Output:** searchable база знаний + тематические саммари.
- **Риск:** может быть слабее связка с core value текущей темы `12.0`.

## Предложение по переформулировке темы 12.0 для промежуточного отчета

**Working title:** `Job interview coach: transcript review MVP`

- На вход: `JD + CV + transcript`.
- На выход: 5 обязательных блоков в фиксированной структуре.
- Ограничение домена: только `Data Analyst / Product Analyst`.
- Ограничение типов интервью: behavioral + general technical.
- Agent-слой (персональный трекинг прогресса) — только как `phase 2`.

## Черновые метрики качества (v0)

- Section completeness на golden set (target: >= 0.90).
- Rubric agreement с ручной разметкой (target: kappa >= 0.60).
- Coverage precision/recall по JD requirements.
- Форматная стабильность (JSON schema pass rate = 100%).

## Questions to decide later

- Насколько строгим делать ограничение по типам интервью?
- Нужен ли Telegram-интерфейс уже в MVP или достаточно CLI/notebook report?
- Какой минимальный объем golden set реалистичен до чекпоинта?
