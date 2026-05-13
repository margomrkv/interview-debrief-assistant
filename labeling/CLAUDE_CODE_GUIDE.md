# Splitter pipeline — Claude Code guide

Руководство для запуска сплиттера через **Claude Code**, **Cursor** или другой клиент с **подпиской** (Pro / Max): один файл от `prepare_prompt.py`, затем чат и строгий JSON.

Актуально для команды с общим репозиторием на GitHub.

Last updated: 2026-05-10

---

## Что такое сплиттер

Берёт папку интервью (транскрипт + метаданные) → извлекает Q&A пары →  
сохраняет JSON + Excel + отчёт валидации.

Схема Q&A-item (LinkedText v1):

```json
{
  "interviewer_question": { "text": "...", "time": "HH:MM:SS" },
  "candidate_answer":     { "text": "...", "time": "HH:MM:SS" },
  "reference_answer":     { "text": null,  "time": null },
  "interviewer_feedback": { "text": null,  "time": null },
  "question_type":    "technical|behavioral|system_design|...",
  "question_topic":   "...",
  "interview_stage":  "..."
}
```

---

## Задача 1 — запустить сплиттер на новом интервью

### Входные файлы (папка интервью)

| Файл | Назначение |
|------|-----------|
| `timecodes.txt` | транскрипт с таймкодами `[HH:MM:SS] текст` — PRIMARY |
| `transcript.txt` | транскрипт без таймкодов — fallback |
| `video.md` | главы видео (только для валидации, Claude Code не читает) |

### Шаг 1 — собрать промпт

```bash
cd /путь/до/репо
python3 labeling/prepare_prompt.py \
  --folder transcripts/<папка-интервью>
```

Создаёт: `labeling/data/<source_id>.prompt.txt`  
_(если есть `timecodes.txt` → автоматически mode=`mock_assisted_split`)_

### Шаг 2 — запустить Claude Code

```bash
claude --dangerously-skip-permissions
```

_(флаг убирает паузы на `y/n` при записи файлов — экономит ~3 минуты)_

Затем в чате Claude Code написать:

```
Прочитай файл labeling/data/<source_id>.prompt.txt
Выполни Q&A extraction согласно инструкциям в нём.
Результат сохрани в labeling/data/<source_id>.splitter.v1.mock.json
```

Claude Code: прочитает промпт → сгенерирует JSON → запишет файл.

### Шаг 3 — сконвертировать в Excel

```bash
python3 labeling/splitter_json_to_excel.py \
  labeling/data/<source_id>.splitter.v1.mock.json
```

Создаёт: `labeling/data/<source_id>.splitter.v1.mock.xlsx`

### Шаг 4 — валидация против video.md

```bash
python3 labeling/validate_splitter_vs_video.py \
  --splitter labeling/data/<source_id>.splitter.v1.mock.json \
  --video transcripts/<папка-интервью>/video.md \
  --tolerance 120 \
  --out labeling/data/<source_id>.splitter.v1.mock.validation.md
```

Создаёт: `.validation.md` с coverage report (цель — 100%).

### Если coverage < 100%

Смотришь в `.validation.md` — там будет список непокрытых глав.  
Есть два типа пропусков:
1. **Реальный пропуск** — в JSON нет вопроса для этой главы → попросить Claude Code добавить.
2. **Лишняя глава** — это не вопрос, а вступление / комментарий интервьюера →
   добавить её начало в `EXPLANATION_PREFIXES` в `labeling/validate_splitter_vs_video.py`.

---

## Структура репо — что где

```
labeling/
  prepare_prompt.py              # собирает промпт из всех входных файлов
  splitter_json_to_excel.py      # JSON → xlsx
  validate_splitter_vs_video.py  # сравнивает JSON с главами video.md
  prompts/
    system_prompt_v2.txt                       # системный промпт для LLM
    user_prompt_template_v2.txt                # user промпт (raw_split)
    user_prompt_template_mock_assisted_v2.txt  # user промпт (mock_assisted_split)
    splitter_output_schema_v1.json             # JSON-схема выхода
  data/
    <source_id>.prompt.txt              # собранный промпт (промежуточный)
    <source_id>.splitter.v1.mock.json   # Q&A extraction output
    <source_id>.splitter.v1.mock.xlsx   # то же в Excel
    <source_id>.splitter.v1.mock.validation.md  # coverage report
transcripts/
  karpov-courses-собеседования/<interview>/
    timecodes.txt   # транскрипт с таймкодами
    video.md        # главы видео
  mock-<company>-<role>-<date>/
    timecodes.txt / transcript.txt
    video.md
```

---

## Пример полного прогона

```bash
cd /Users/you/ds-final-project

# 1. Собрать промпт
python3 labeling/prepare_prompt.py \
  --folder transcripts/mock-avito-product-analyst-middle-2024-04-04

# 2. Запустить Claude Code (в отдельном терминале)
claude --dangerously-skip-permissions
# > Прочитай labeling/data/avito_product_analyst_middle_20240404.prompt.txt
# > Выполни Q&A extraction, результат → labeling/data/avito_product_analyst_middle_20240404.splitter.v1.mock.json

# 3. Excel
python3 labeling/splitter_json_to_excel.py \
  labeling/data/avito_product_analyst_middle_20240404.splitter.v1.mock.json

# 4. Валидация
python3 labeling/validate_splitter_vs_video.py \
  --splitter labeling/data/avito_product_analyst_middle_20240404.splitter.v1.mock.json \
  --video transcripts/mock-avito-product-analyst-middle-2024-04-04/video.md \
  --tolerance 120 \
  --out labeling/data/avito_product_analyst_middle_20240404.splitter.v1.mock.validation.md

```

---

## Зависимости

```bash
pip install openpyxl
```

Claude Code / Claude CLI: https://claude.ai/code (требует Anthropic аккаунт)
