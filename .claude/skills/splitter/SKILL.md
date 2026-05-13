---
name: splitter
description: >
  Splitter: scripts/splitter_prepare_prompt → JSON (subagent) → scripts/splitter_json_to_excel →
  scripts/splitter_validate_video по video.md; артефакты в splitter_output/ (в т.ч. *.splitter_llm_input.txt).
---

# Skill: Splitter

**Куда пишутся файлы:** в корне репозитория каталог **`splitter_output/`** (имя папки именно такое, в нижнем регистре). Туда же кладутся **все** артефакты прогона: `*.user_prompt.txt`, `*.splitter_llm_input.txt` (единый вход для LLM: system + user + схема), далее после шагов пайплайна — `*.json`, `*.xlsx`, `*.validation.md`. Скрипт `splitter_prepare_prompt.py` создаёт только текстовые снимки входа; JSON, Excel и отчёт валидации появляются после ответа модели и постобработки (см. шаги ниже).

## Версия

Текущая версия **5.3** (структура skill: `config/`, **`prompt,output_schema/`** — `splitter_system_prompt.txt` + `splitter_output_schema.json`, пути в `config/splitter_run_config.json`, `scripts/`). Включай версию в итоговый отчёт.

## Модель

**Model: claude-sonnet-4-6** — PRO-подписка через Agent tool (subagent). Отдельный API-ключ Anthropic для сплиттера не используется.

## Назначение

Один прогон = одна папка интервью → JSON (Q&A) + при необходимости Excel + при наличии `video.md` — отчёт валидации.

Извлечение через **Agent tool** (`subagent_type`: `general-purpose`): изолированный контекст, без истории родительского чата.

**Сборка контекста:** `scripts/splitter_prepare_prompt.py` пишет в **`splitter_output/`**:

- `<base>.splitter_llm_input.txt` — **system + user + schema** (один файл для модели / Claude Code subagent / Cursor).
- `<base>.user_prompt.txt` — только user-часть (если system/user разделяются вручную).

## Вход

**Обязательно:** путь к папке интервью **от корня репо**, например `transcripts/mock-avito-product-analyst-middle-2024-04-04`.

**Опциональные флаги:**

- `mode=<raw_split|mock_assisted_split>` — по умолчанию: **`mock_assisted_split`**, если в папке есть **`video.md`**, иначе **`raw_split`**.
- `version=<N>` — явно задать `vN`; иначе **автоверсия**: в `splitter_output/` ищутся все файлы вида `<source_id>.splitter.v*.<mock|raw>.*` (в т.ч. `.json`, `.xlsx`, `.validation.md`, `.user_prompt.txt`, `.splitter_llm_input.txt`); если таких нет — **v1**, иначе **max(N)+1** (следующий номер после максимального уже существующего для этой пары `source_id` + режим).
- `source_id=<str>` — иначе выводится из имени папки (логика в `splitter_prepare_prompt.py`).
- `section_config=<path>` — только для валидатора: JSON для **`--section-config`** (см. `config/section_topic_map.example.json`).

**Примеры вызова skill (имя может отличаться в клиенте):**

```
/splitter transcripts/mock-avito-product-analyst-middle-2024-04-04
/splitter transcripts/.../mock-karpov-product-analyst-junior-2021-06-24 version=2
```

## Конфигурация (пути в репозитории)

Корень skill: **`.claude/skills/splitter/`**.

| Артефакт | Путь |
|----------|------|
| Сборка промпта | `.claude/skills/splitter/scripts/splitter_prepare_prompt.py` |
| Конфиг | `.claude/skills/splitter/config/splitter_run_config.json` (читает только `splitter_prepare_prompt.py`) |
| System prompt | по полю `system_prompt` в конфиге (по умолчанию `prompt,output_schema/splitter_system_prompt.txt`) |
| JSON Schema выхода | по полю `schema` (по умолчанию `prompt,output_schema/splitter_output_schema.json`) |
| Результаты прогона | `splitter_output/<source_id>.splitter.v<N>.<mock\|raw>.*` — единый шаблон для JSON, xlsx, validation, снимков входа и др.; см. автоверсию ниже |

Per-run текст user и схема — внутри `splitter_output/*.user_prompt.txt`.

### Файл `config/splitter_run_config.json`

**Источник правды для путей и подсказок чата — только этот JSON на диске.** Скрипт читает `SKILL_DIR / "config" / "splitter_run_config.json"`, где `SKILL_DIR` — корень skill (родитель каталога `scripts/`). Содержимое в этом `SKILL.md` не парсится кодом — ниже смысл полей.

| Поле | Назначение |
|------|------------|
| `system_prompt` | Путь к system-промпту **относительно корня skill**. |
| `schema` | Путь к JSON Schema **относительно корня skill**. |
| `inference` | Опционально: `model`, `temperature`, `max_tokens` — **не вызывают API**; копируются в **`RUNTIME_HINTS`** в каждом `*.user_prompt.txt`. |

Устаревший вариант: `model` / `temperature` / `max_tokens` на **верхнем** уровне JSON — тоже учитываются при сборке `RUNTIME_HINTS`.

## Алгоритм

По желанию: `▶ [Шаг N] …` / `✓ [Шаг N] …`.

### Шаг 0: Парсинг входа

Выделить `<folder>`, флаги; убедиться, что `transcripts/<folder>/` существует.

### Шаг 1: Режим и файлы интервью

| Условие | Режим (default) | Транскрипт для LLM |
|--------|------------------|-------------------|
| Есть `video.md` | `mock_assisted_split` | `timecodes.txt`, иначе `transcript.txt` |
| Нет `video.md` | `raw_split` | только `transcript.txt` |

| Файл в папке интервью | В LLM | Назначение |
|----------------------|--------|------------|
| `video.md` | **Никогда** | Автовыбор mock + **только** офлайн-валидация |
| `timecodes.txt` | Да (mock, предпочтительно) | `[HH:MM:SS]` |
| `transcript.txt` | Да | mock fallback или единственный вход в raw |
| `feedback.md` | Да (mock), опционально | Подсказки границ |

### Пример одного `item` (LinkedText)

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

### Шаг 2: `source_id` и версия

**`source_id`:** как в `splitter_prepare_prompt.py`: префикс `mock-` убрать, дефисы → `_`, дата `YYYY-MM-DD` → `YYYYMMDD`.

**`vN` (авто):** по всем файлам в `splitter_output/` с шаблоном имени  
`<source_id>.splitter.v<number>.<mock|raw>.*`  
(например `…v4.mock.json`, `…v4.mock.xlsx`, `…v4.mock.validation.md`, `…v4.mock.user_prompt.txt`, `…v4.mock.splitter_llm_input.txt`).  
Если совпадений нет → **N=1**. Иначе **N = (максимальный уже встреченный номер для этого `source_id` и режима) + 1**.  
Режимы **mock** и **raw** версионируются **раздельно** (отдельные цепочки `vN`).  
Переопределение: флаг **`--version`** у `splitter_prepare_prompt.py` задаёт `N` вручную.

### Шаг 3: `splitter_prepare_prompt.py`

```bash
python3 .claude/skills/splitter/scripts/splitter_prepare_prompt.py \
    --folder <folder> \
    [--mode <raw_split|mock_assisted_split>] \
    [--version <N>] \
    [--source-id <source_id>]
```

Сохранить напечатанные пути к `*.splitter_llm_input.txt`, `*.user_prompt.txt`, будущему `.json`.

**Read tool (subagent):** `splitter_output/<base>.splitter_llm_input.txt`.

### Шаг 4: Q&A extraction (Agent subagent)

- `subagent_type`: `general-purpose`
- `description`: `Q&A extraction: <source_id>`
- `prompt`: полный текст **`splitter_output/<base>.splitter_llm_input.txt`**, в конце:

```
OUTPUT REQUIREMENT: Return ONLY a valid JSON object.
No markdown, no explanation, no ```json fences. Start directly with {
```

Сохранить ответ как сырой JSON (снять обёртку при необходимости).

**Варианты контекста:**  
**A)** один файл — `splitter_llm_input.txt`;  
**B)** system: `.claude/skills/splitter/prompt,output_schema/splitter_system_prompt.txt`, user: `splitter_output/<base>.user_prompt.txt`.

### Шаг 5–6: Парсинг и сохранение JSON

`json.loads`; проверить `source_id`, `splitter_mode`, `items`. Путь к файлу — из вывода шага 3.

### Шаг 7: Excel

```bash
python3 .claude/skills/splitter/scripts/splitter_json_to_excel.py \
    splitter_output/<base>.json \
    --out splitter_output/<base>.xlsx
```

### Шаг 8: Валидация (если есть `video.md`)

```bash
python3 .claude/skills/splitter/scripts/splitter_validate_video.py \
    --splitter splitter_output/<base>.json \
    --video <folder>/video.md \
    --tolerance 120 \
    [--section-config <path.json>] \
    [--time-from <HH:MM:SS>] \
    [--time-to <HH:MM:SS>] \
    --out splitter_output/<base>.validation.md
```

Шаблон формата для `--section-config`: **`config/section_topic_map.example.json`** (лучше своя копия с правками). Без флага секционные проверки тем пропускаются.

### Шаг 9: Итерация по отчёту валидации

1. Читать `*.validation.md` и проблемные `items` в JSON.  
2. Правки прежде всего в **`prompt,output_schema/splitter_system_prompt.txt`** (и при смене контракта — **`prompt,output_schema/splitter_output_schema.json`**).  
3. При необходимости — `EXPLANATION_PREFIXES` в **`scripts/splitter_validate_video.py`**.  
4. Повторить шаги 3–8 (новый `--version` или тот же — по договорённости).

Если в `video.md` есть мета-секции без однозначного Q&A, **Coverage может быть < 100%** — не обязательный fail без жёстких misassignments.

### Шаг 10: Итоговый отчёт

```
[splitter v5.3 | model: claude-sonnet-4-6 | PRO | Agent subagent]
Folder:   <folder>
Mode:     <mode>
Version:  v<N>
Items:    N
Artifacts:
  llm_input:  splitter_output/<base>.splitter_llm_input.txt
  user-only:  splitter_output/<base>.user_prompt.txt
  JSON:       splitter_output/<base>.json
  Excel:      splitter_output/<base>.xlsx
  Validation: splitter_output/<base>.validation.md  (или N/A)

Validation: ✅ / ❌ — кратко
```

## Структура каталогов

```
.claude/skills/splitter/          ← корень skill
  SKILL.md
  README.md
  config/
    splitter_run_config.json
    section_topic_map.example.json   # опционально, шаблон для --section-config
    # опционально: interview_paths.md — только для людей
  prompt,output_schema/
    splitter_system_prompt.txt
    splitter_output_schema.json
  scripts/
    splitter_prepare_prompt.py
    splitter_json_to_excel.py
    splitter_validate_video.py
  adhoc/                            # если есть: вне основного пайплайна
    splitter_enrich_feedback.py
    splitter_extract_feedback_windows.py
splitter_output/                  ← в корне репо: артефакты прогонов
transcripts/<папка-интервью>/    ← вход интервью
```

## Зависимости

- **`openpyxl`** — для `splitter_json_to_excel.py` (`pip install openpyxl`).

## Multi-candidate

`--transcript-file`, `--source-id-suffix`, валидация с `--time-from` / `--time-to`. Скрипты — из **`scripts/`**; выход — **`splitter_output/`**.

## Ограничения

- Один прогон на вызов skill = одна папка (или явная последовательность для нескольких кандидатов).
- **`video.md`** не отправлять в subagent.
