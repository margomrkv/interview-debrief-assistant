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
| Данные              | `transcripts/`     | Транскрипты интервью — `mock-interviews/`, `real-interviews/`, `youtube-sessions/`, `own/` |
| Splitter (Q&A)    | `.claude/skills/splitter/` + **`splitter_output/`** в корне репо | шаги 1–5 + цикл исправления до ✅ в **`splitter/SKILL.md`** (`/splitter` в Cursor и Claude Code); постобработка `scripts/splitter_post.sh`; 4 файла на прогон: **`{basename}.vN.qa-split.json`**, `.xlsx`, `.validation-report.md`, `.pipeline-log.md` (см. `splitter_output/README.md`) |

### Правила 

Не запускай тесты с реальной платной моделью в процессе разработки без необходимости


### Именование файлов встреч и интервью

- Встречи (`internal-notes/`): `YYYY-MM-DD-transcript-<participants>-<topic>.{txt|md}`
  - Примеры: `2026-04-06-transcript-margo-anton-project-kickoff.txt`, `2026-04-22-transcript-alex-weekly-meeting-1.md`
- Mock-интервью: `transcripts/mock-interviews/<publisher>/mock-{role}-{level}-…-{YYYY-MM-DD}/` — см. `transcripts/README.md`
  - Содержимое: `transcript.txt`, `link.txt`, `timecodes.txt`; с YouTube — ещё `video.md` (главы для валидации сплиттера)
- Реальные (записи каналов): `transcripts/real-interviews/novoselov/real-…` (publisher slug **`novoselov`**, не `vadim`)
- Лайвы / разборы (не интервью): `transcripts/youtube-sessions/…`
- Собственные интервью: `transcripts/own/<person>-<company>-YYYYMMDD/`
  - Содержимое: `cv.md`, `transcript.txt`, `feedback.txt`, опционально `vacancy.txt` и файлы отчётов
- Шаблон новой папки: `transcripts/_template/`
- Миграция путей: `transcripts/aliases.yaml`


<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:ca08a54f -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd dolt push
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->
