# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Репозиторий состоит из двух крупных частей: **курс** «Intro to AI Agents» (Data Sanity, Белград, 2026) и **курсовой проект**. Ниже — логическое разделение и маппинг на текущие директории (в будущем возможна перекладка).

## Курс

Делится на теорию, практику, домашки и общее описание.

| Логический блок                 | Директория                       | Что внутри                                                  |
|---------------------------------|----------------------------------|-------------------------------------------------------------|
| Описание курса                  | `course/syllabus/`               | PDF программы курса (syllabus)                              |
| Теория                          | `course/lectures/presentations/` | Слайды лекций (`.pdf` / `.pptx`)                            |
|                                 | `course/lectures/transcripts/`   | Транскрипты аудио лекций (`.txt`)                           |
| Практика                        | `course/lectures/workshops/`     | Jupyter-ноутбуки воркшопов (`.ipynb`)                       |
| Домашки                         | `course/assigments/<student>/`   | Сдачи ДЗ по студентам                                       |
| Конспекты лекций (только Антон) | {VAULT_DIR}/Professional/AI      | Конспекты в рамках лекций (название AI Agents Lecture N.md) |

### Именование материалов курса

Шаблон: `YYYY-MM-DD-{L|W}NN-<topic-slug>.<ext>`

- `YYYY-MM-DD` — дата занятия из syllabus.
- `L` = Lecture, `W` = Workshop.
- `NN` = номер занятия с ведущим нулём (`01`–`08`).
- `<topic-slug>` — тема в lowercase kebab-case. Для транскриптов лекций — фиксированный slug `lecture-transcript`.
- Расширенная версия воркшопа: суффикс `-full` (например, `...-W04-ai-workflows-langgraph-full.ipynb`).

Календарь занятий (источник: `course/syllabus/syllabus - Data Sanity Intro to AI Agents Belgrade 2026-03-21.pdf`):

| #  | Дата       | Тема                                     |
|----|------------|------------------------------------------|
| 01 | 2026-03-21 | Introduction to AI & LLM                 |
| 02 | 2026-03-28 | Prompt Engineering                       |
| 03 | 2026-04-04 | Retrieval-Augmented Generation (RAG)     |
| 04 | 2026-04-18 | AI Workflows & Introduction to AI Agents |
| 05 | 2026-04-25 | AI Agents                                |
| 06 | 2026-05-09 | Testing and Observability in LLM Systems |
| 07 | 2026-05-16 | System Design, Production & Deployment   |
| 08 | 2026-05-23 | Project Presentations & Wrap-up          |

## Проект

Делится на описание проекта, критерии оценки, код и данные.

| Логический блок     | Директория         | Что внутри                                                           |
|---------------------|--------------------|----------------------------------------------------------------------|
| Описание проекта    | `md/project.md`    | Постановка задачи (JD + CV + transcript → структурированный отчёт)   |
|                     | `docs/project-hub.md` | Хаб проекта / общий обзор                                         |
|                     | `internal-notes/`   | Транскрипты встреч по проекту                                        |
| Критерии оценки     | `grading/`         | `Project Criteria & Scoring.docx` и смежные документы                |
| Код                 | — (пока нет)       | В репозитории ещё нет исходников; появятся — разместить здесь        |
| Данные              | `transcripts/`     | Транскрипты интервью (mock и собственные) — основной вход проекта    |

### Именование файлов встреч и интервью

- Встречи (`internal-notes/`): `YYYY-MM-DD-transcript-<participants>-<topic>.{txt|md}`
  - Примеры: `2026-04-06-transcript-margo-anton-project-kickoff.txt`, `2026-04-22-transcript-alex-weekly-meeting-1.md`
- Mock-интервью (папка в `transcripts/`): `mock-<company>-<role>-<level>-YYYY-MM-DD/`
  - Содержимое: `transcript.txt`, `link.txt`, `timecodes.txt`
- Собственные интервью (папка в `transcripts/`): `<person>-<company>-YYYYMMDD/` (дата без дефисов)
  - Содержимое: `cv.md`, `transcript.txt`, `feedback.txt`, опционально `vacancy.txt` и файлы отчётов
- Шаблон новой папки mock-интервью: `transcripts/mock-template/`
