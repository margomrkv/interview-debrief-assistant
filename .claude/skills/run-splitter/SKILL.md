---
name: run-splitter
description: >
  Устарело — см. `.claude/skills/splitter/SKILL.md`. Раньше: splitter_prepare_prompt → JSON → Excel →
  валидация; артефакты в splitter/output/.
---

> **Актуальный skill:** `.claude/skills/splitter/` — см. **`SKILL.md` там (v5.3)**. Артефакты в **`splitter_output/`** в корне репо; единый вход для LLM — **`<base>.splitter_llm_input.txt`**; промпты и схема — **`prompt,output_schema/splitter_system_prompt.txt`**, **`splitter_output_schema.json`**. Ниже — устаревшее описание `run-splitter` (пути `splitter/output/`, `full_bundle`).

# Skill: Run Splitter

## Версия

Текущая версия **5.0**. Включай версию в итоговый отчёт.

## Модель

**Model: claude-sonnet-4-6** — PRO-подписка через Agent tool (subagent). API-ключ для сплиттера не используется.

## Назначение

Один прогон = одна папка интервью → JSON (Q&A) + Excel + при наличии `video.md` — validation report.

Extraction через **Agent tool** (`subagent_type`: `general-purpose`): изолированный контекст, без истории родительского чата.

**Сборка контекста:** `splitter_prepare_prompt.py` (в этой папке) пишет:

- `splitter/output/<base>.full_bundle.txt` — **system + user + schema** (рекомендуется для Cloud и subagent: один файл).
- `splitter/output/<base>.user_prompt.txt` — только user-часть (если оркестратор разделяет system/user вручную).

## Вход

**Обязательный аргумент:** путь к папке интервью (от корня репо), например `transcripts/mock-avito-product-analyst-middle-2024-04-04`.

**Опциональные флаги:**

- `mode=<raw_split|mock_assisted_split>` — по умолчанию: **`mock_assisted_split` если в папке есть `video.md`**, иначе `raw_split`.
- `version=<N>` — иначе следующая свободная `vN` под `splitter/output/<source_id>.splitter.v*.mock.json` (или `.raw`).
- `source_id=<str>` — иначе из имени папки (как в `splitter_prepare_prompt.py`).
- `section_config=<path>` — для валидатора, напр. `.claude/skills/run-splitter/config/section_topic_map.example.json` (лучше копия с правками под интервью).

**Примеры:**

```
/run-splitter transcripts/mock-avito-product-analyst-middle-2024-04-04
/run-splitter transcripts/karpov-courses-собеседования/mock-karpov-product-analyst-junior-2021-06-24 version=2
/run-splitter transcripts/karpov-courses-собеседования/junior-data-scientist-... section_config=.claude/skills/run-splitter/config/section_topic_map.example.json
```

## Конфигурация (репозиторий)

| Артефакт | Путь |
|----------|------|
| Prompt builder | `.claude/skills/run-splitter/splitter_prepare_prompt.py` |
| Конфиг сборки | `.claude/skills/run-splitter/config/splitter_run_config.json` (читает только `splitter_prepare_prompt.py`) |
| System prompt | `.claude/skills/run-splitter/prompts/system_prompt_v3.txt` |
| Schema | `.claude/skills/run-splitter/prompts/splitter_output_schema_v1.json` |
| JSON / xlsx / validation | `splitter/output/<source_id>.splitter.v<N>.<mock\|raw>.*` |

Per-run **user** текст и схема — внутри `*.user_prompt.txt` (не дублируем отдельные user-template файлы).

### Файл `config/splitter_run_config.json`

**Машиночитаемый источник правды — только JSON-файл на диске.** `splitter_prepare_prompt.py` читает его с пути `SKILL_DIR / "config" / "splitter_run_config.json"`. Текст в этом `SKILL.md` **не парсится** кодом: здесь описание полей, чтобы не плодить отдельные гайды и не дублировать тело JSON (иначе два источника и расхождение).

| Поле | Назначение |
|------|------------|
| `system_prompt` | Путь к system-промпту **относительно папки skill** (по умолчанию `prompts/system_prompt_v3.txt`). |
| `schema` | Путь к JSON Schema выхода сплиттера **относительно папки skill** (по умолчанию `prompts/splitter_output_schema_v1.json`). |
| `inference` | Опционально: объект с полями вроде `model`, `temperature`, `max_tokens`. **API не вызывается** — значения копируются в секцию **`RUNTIME_HINTS`** внутри каждого сгенерированного `splitter/output/*.user_prompt.txt` для оператора и воспроизводимости. |

Устаревший вариант: те же `model` / `temperature` / `max_tokens` на **верхнем** уровне JSON — `splitter_prepare_prompt.py` их тоже учитывает при сборке `RUNTIME_HINTS`.

Менять настройки — **редактировать файл** `config/splitter_run_config.json` в репозитории.

## Алгоритм

Перед шагом: `▶ [Шаг N/10] …` — после: `✓ [Шаг N/10] …`

---

### Шаг 0: Парсинг входа

Выделить `<folder>`, флаги, убедиться что папка существует.

---

### Шаг 1: Режим и файлы

| Условие | Режим (default) | Транскрипт для LLM |
|--------|------------------|-------------------|
| Есть `video.md` | `mock_assisted_split` | `timecodes.txt` если есть, иначе `transcript.txt` |
| Нет `video.md` | `raw_split` | только `transcript.txt` |

| Файл в папке интервью | В LLM | Назначение |
|----------------------|--------|------------|
| `video.md` | **Никогда** | Режим mock (авто) + только **валидация** офлайн |
| `timecodes.txt` | Да (mock, предпочтительно) | Транскрипт с `[HH:MM:SS]` |
| `transcript.txt` | Да | В mock — fallback; в **raw** — единственный основной вход |
| `feedback.md` | Да (mock), опционально | Подсказки границ |

---

## Пример структуры одного item (LinkedText)

```json
{
  "interviewer_question": { "text": "...", "time": "HH:MM:SS" },
  "candidate_answer":     { "text": "...", "time": "HH:MM:SS" },
  "reference_answer":     { "text": null,  "time": null },
  "interviewer_feedback": { "text": null,  "time": null },
  "question_type":    "hard",
  "question_topic":   "Statistics",
  "interview_stage":  "technical_qna"
}
```

---

### Шаг 2: source_id и версия

Как в `splitter_prepare_prompt.py`: `mock-` срезать, дефисы → `_`, дата `YYYY-MM-DD` → `YYYYMMDD`. Версия — следующий `vN` среди `splitter/output/<source_id>.splitter.v*.<mock\|raw>.json`.

---

### Шаг 3: `splitter_prepare_prompt.py`

```bash
python3 .claude/skills/run-splitter/splitter_prepare_prompt.py \
    --folder <folder> \
    [--mode <raw_split|mock_assisted_split>] \
    [--version <N>] \
    [--source-id <source_id>]
```

Запомнить напечатанные пути к `*.full_bundle.txt`, `*.user_prompt.txt`, будущему `.json`.

**Read tool:** `splitter/output/<base>.full_bundle.txt` (предпочтительно для subagent).

---

### Шаг 4: Q&A extraction (Agent subagent)

- `subagent_type`: `general-purpose`
- `description`: `Q&A extraction: <source_id>`
- `prompt`: полное содержимое **`<base>.full_bundle.txt`**, плюс в конце:

```
OUTPUT REQUIREMENT: Return ONLY a valid JSON object.
No markdown, no explanation, no ```json fences. Start directly with {
```

Сохранить ответ как `RAW_OUTPUT`.

**Варианты контекста для модели:**  
**A)** один файл — всё содержимое `splitter/output/<base>.full_bundle.txt`;  
**B)** раздельно — system: `.claude/skills/run-splitter/prompts/system_prompt_v3.txt`, user: `splitter/output/<base>.user_prompt.txt` (как в API).

---

### Шаг 5: Парсинг JSON

Снять markdown-обёртку при необходимости; `json.loads`; проверить `source_id`, `splitter_mode`, `items`.

---

### Шаг 6: Сохранить JSON

Путь из вывода Шага 3, обычно `splitter/output/<base>.json`.

---

### Шаг 7: Excel

```bash
python3 .claude/skills/run-splitter/splitter_json_to_excel.py \
    splitter/output/<base>.json \
    --out splitter/output/<base>.xlsx
```

---

### Шаг 8: Валидация

Если `<folder>/video.md` есть:

```bash
python3 .claude/skills/run-splitter/splitter_validate_video.py \
    --splitter splitter/output/<base>.json \
    --video <folder>/video.md \
    --tolerance 120 \
    [--section-config <section_config>] \
    [--time-from <HH:MM:SS>] \
    [--time-to <HH:MM:SS>] \
    --out splitter/output/<base>.validation.md
```

Опционально: `--section-config` — путь к JSON (шаблон: `config/section_topic_map.example.json` в этой папке skill; обычно своя копия с правками).

Иначе — пропустить, явно написать пользователю.

---

### Шаг 9: Итерация до согласованности с валидацией (как в Cursor)

Если отчёт валидации показывает пропуски, лишние сопоставления или типичное **обобщение** в JSON (мета-описания вместо цитат):

1. Прочитать `splitter/output/<base>.validation.md` и сами проблемные `items` в JSON.
2. **Приоритет правок:** сначала `.claude/skills/run-splitter/prompts/system_prompt_v3.txt` (few-shot, усиление verbatim, краевые случаи). Транскрипт не искажать «под отчёт».
3. Если глава в `video.md` не является вопросом — при необходимости добавить префикс в `EXPLANATION_PREFIXES` в `.claude/skills/run-splitter/splitter_validate_video.py`.
4. Повторить **Шаги 3–8** (новый `--version` или тот же, по договорённости с пользователем), пока результат не станет приемлемым.

Если в `video.md` есть мета-секции (intro, тайминг и т.д.) без однозначного M↔Q↔A, **Coverage может быть ниже 100%** — это не автоматический fail при отсутствии жёстких misassignments.

Оркестратор (ты) ведёт себя как IDE-агент: анализ отчёта → точечная правка промпта/валидатора → перезапуск, а не разовый «сдал как есть».

---

### Шаг 10: Итоговый отчёт

```
[run-splitter v5.0 | model: claude-sonnet-4-6 | PRO | Agent subagent]
Folder:   <folder>
Mode:     <mode>  (default по video.md)
Version:  v<N>
Items:    N
Artifacts:
  bundle:     splitter/output/<base>.full_bundle.txt
  user-only:  splitter/output/<base>.user_prompt.txt
  JSON:       splitter/output/<base>.json
  Excel:      splitter/output/<base>.xlsx
  Validation: splitter/output/<base>.validation.md  (или N/A)

Validation: ✅ / ❌ — кратко
```

---

## Структура каталогов (где что лежит)

```
.claude/skills/run-splitter/
  SKILL.md
  README.md
  splitter_prepare_prompt.py      # шаг 1: сборка промпта
  splitter_json_to_excel.py       # после JSON
  splitter_validate_video.py      # офлайн vs video.md
  adhoc/                            # вне основного пайплайна
    splitter_enrich_feedback.py
    splitter_extract_feedback_windows.py
  config/
    splitter_run_config.json
    section_topic_map.example.json
    # опционально: interview_paths.md — черновик путей для людей; скрипты не читают
  prompts/
    system_prompt_v3.txt
    splitter_output_schema_v1.json
splitter/                        ← только артефакты (без кода)
  output/                        # *.json, *.xlsx, *.validation.md, *.user_prompt.txt, *.full_bundle.txt
transcripts/<папка-интервью>/   # transcript.txt, timecodes.txt, video.md, …
```

## Зависимости

- **`openpyxl`** — для `splitter_json_to_excel.py` (`pip install openpyxl`).

## Дополнительные скрипты (вне обязательных шагов 3–8)

| Скрипт | Назначение |
|--------|------------|
| `adhoc/splitter_enrich_feedback.py` | Постобработка уже готового JSON: дозаполнить `interviewer_feedback` из timecodes; пересобирает xlsx. |
| `adhoc/splitter_extract_feedback_windows.py` | Вспомогательный просмотр окон транскрипта между таймкодами. |

---

## Multi-candidate

Как раньше: `--transcript-file /tmp/timecodes_<name>.txt`, `--source-id-suffix _<name>`, валидация с `--time-from` / `--time-to`. Скрипты — из `.claude/skills/run-splitter/`; выход — `splitter/output/`.

## Ограничения

- Один прогон на вызов skill = одна папка (или явная последовательность для нескольких кандидатов).
- `video.md` никогда не отправлять в subagent.
