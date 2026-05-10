---
name: run-splitter
description: >
  Запускает splitter pipeline для папки интервью: собирает промпт через prepare_prompt.py,
  генерирует JSON Q&A extraction через Agent tool (subagent, PRO-подписка, без API-ключа),
  конвертирует в Excel, запускает валидацию против video.md.
---

# Skill: Run Splitter

## Версия

Текущая версия 4.0. Включай версию в итоговый отчёт.

## Модель

**Model: claude-sonnet-4-6** — используется PRO-подписка через Agent tool (subagent).
API-ключ и API-кредиты не используются.

## Назначение

Один прогон = одна папка интервью → один JSON файл с Q&A парами + Excel + validation report.

Extraction выполняется через **Agent tool** (spawn subagent, тип `general-purpose`):
- subagent получает чистый контекст (только промпт + транскрипт, без истории разговора)
- работает в рамках той же PRO-сессии, без API-кредитов
- быстрее inline-генерации за счёт меньшего контекста

**Ключевая оптимизация:** промпт собирается через `labeling/prepare_prompt.py` — один Bash-вызов
вместо 5 отдельных Read tool calls. Claude Code читает один файл, а не пять.

## Вход

**Обязательный аргумент:** путь к папке интервью (относительно корня репо).

**Опциональные флаги:**

- `mode=<raw_split|mock_assisted_split>` — Default: `timecodes.txt` есть → `mock_assisted_split`, иначе → `raw_split`.
- `version=<N>` — номер версии (default: следующая незанятая `vN`).
- `source_id=<str>` — Default: строится из имени папки.
- `section_config=<path>` — путь к JSON с section timecodes для валидатора.

**Примеры:**

```
/run-splitter transcripts/mock-avito-product-analyst-middle-2024-04-04
/run-splitter transcripts/mock-karpov-product-analyst-junior-2021-06-24 version=2
/run-splitter transcripts/karpov-courses-собеседования/junior-data-scientist-... mode=mock_assisted_split section_config=labeling/config/karpov_section_map.json
```

## Конфигурация

- **Execution:** Agent tool, subagent_type=`general-purpose` (PRO-подписка, без API-кредитов)
- **Model:** `claude-sonnet-4-6`
- **Prompt builder:** `labeling/prepare_prompt.py` (собирает все входные файлы в один)
- **System prompt:** `labeling/prompts/system_prompt_v2.txt`
- **User prompt (mock_assisted_split):** `labeling/prompts/user_prompt_template_mock_assisted_v2.txt`
- **User prompt (raw_split):** `labeling/prompts/user_prompt_template_v2.txt`
- **Output schema:** `labeling/prompts/splitter_output_schema_v1.json`
- **Output JSON:** `labeling/data/<source_id>.splitter.v<N>.<mode_tag>.json`
- **Output Excel:** то же, `.xlsx`
- **Validation report:** то же, `.validation.md`

## Алгоритм

Перед каждым шагом выводить: `▶ [Шаг N/9] <Название> — <детали>`
После завершения: `✓ [Шаг N/9] <кратко результат>`

---

### Шаг 0: Парсинг входа

`▶ [Шаг 0/9] Парсинг входа`

Выделить путь к папке. Распарсить флаги. Проверить, что папка существует.

`✓ [Шаг 0/9] Папка найдена: <path>`

---

### Шаг 1: Определение режима и входных файлов

`▶ [Шаг 1/9] Определение режима`

| Файл | mock_assisted_split | raw_split |
|------|---------------------|-----------|
| `timecodes.txt` | PRIMARY transcript | не используется |
| `transcript.txt` | fallback | PRIMARY transcript |
| `feedback.md` | sidecar (optional) | не используется |
| `video.md` | только для валидации — НЕ в LLM | не используется |

`video.md` НИКОГДА не передаётся в subagent.

`✓ [Шаг 1/9] Режим: <mode>. Транскрипт: <file>`

---

### Шаг 2: Определение source_id и версии

`▶ [Шаг 2/9] Определение source_id и версии`

- `source_id`: имя папки → убрать `mock-`, дефисы → `_`, дата без дефисов.
  - `mock-karpov-product-analyst-junior-2021-06-24` → `karpov_product_analyst_junior_20210624`
- `version`: найти существующие `labeling/data/<source_id>.splitter.v*.json`, взять следующий.
- Пути: `labeling/data/<source_id>.splitter.v<N>.<mode_tag>.json` (+ `.xlsx`, `.validation.md`)

`✓ [Шаг 2/9] source_id: <id>, версия: v<N>`

---

### Шаг 3: Сборка промпта через prepare_prompt.py

`▶ [Шаг 3/9] Сборка промпта — labeling/prepare_prompt.py`

```bash
python3 labeling/prepare_prompt.py \
    --folder <folder> \
    --mode <mode> \
    --version <N> \
    [--source-id <source_id>]
```

Скрипт читает все входные файлы и собирает их в один файл
`labeling/data/<source_id>.prompt.txt`. Это заменяет 5 отдельных Read tool calls одним вызовом.

Затем прочитать получившийся файл через Read tool:

```
Read: labeling/data/<source_id>.prompt.txt
```

`✓ [Шаг 3/9] Промпт готов: labeling/data/<source_id>.prompt.txt (~X chars)`

---

### Шаг 4: Q&A extraction через Agent subagent

`▶ [Шаг 4/9] Запуск Agent subagent для Q&A extraction (PRO, claude-sonnet-4-6)`

Использовать **Agent tool** с параметрами:
- `subagent_type`: `general-purpose`
- `description`: `Q&A extraction: <source_id>`
- `prompt`: содержимое файла из Шага 3, плюс явная инструкция:

```
Ты — экстрактор вопросов и ответов из транскриптов собеседований.
Следуй точно инструкциям ниже.

<содержимое labeling/data/<source_id>.prompt.txt>

OUTPUT REQUIREMENT: Return ONLY a valid JSON object.
No markdown, no explanation, no ```json fences. Start directly with {
```

Subagent возвращает JSON строкой в своём ответе — сохранить этот ответ как `RAW_OUTPUT`.

`✓ [Шаг 4/9] Subagent завершён, получен ответ (~X chars)`

---

### Шаг 5: Парсинг и валидация JSON

`▶ [Шаг 5/9] Парсинг и валидация JSON`

Записать `RAW_OUTPUT` из Шага 4 в `/tmp/splitter_raw_<source_id>.txt` через Write tool, затем:

```bash
python3 - << 'PYEOF'
import json, sys, re

raw = open("/tmp/splitter_raw_<source_id>.txt").read().strip()
if raw.startswith("```"):
    raw = re.sub(r'^```(?:json)?\n?', '', raw)
    raw = re.sub(r'\n?```$', '', raw)
try:
    data = json.loads(raw)
except json.JSONDecodeError as e:
    print(f"JSON PARSE ERROR: {e}", file=sys.stderr)
    print("First 500 chars:", raw[:500], file=sys.stderr)
    sys.exit(1)

assert "source_id" in data, "Missing source_id"
assert "splitter_mode" in data, "Missing splitter_mode"
assert isinstance(data.get("items"), list), "Missing/invalid items"
print(f"OK: {len(data['items'])} items")
PYEOF
```

Если JSON большой (>4K tokens) и bash-escaping проблематичен — использовать Write tool напрямую
для записи JSON-файла, минуя temp-файл.

`✓ [Шаг 5/9] JSON валиден: <N> items`

---

### Шаг 6: Сохранение JSON

`▶ [Шаг 6/9] Сохранение JSON → labeling/data/<source_id>.splitter.v<N>.<mode_tag>.json`

```bash
python3 - << 'PYEOF'
import json, re, pathlib

raw = open("/tmp/splitter_raw_<source_id>.txt").read().strip()
if raw.startswith("```"):
    raw = re.sub(r'^```(?:json)?\n?', '', raw)
    raw = re.sub(r'\n?```$', '', raw)
data = json.loads(raw)

out = pathlib.Path("labeling/data/<source_id>.splitter.v<N>.<mode_tag>.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved: {out}")
PYEOF
```

`✓ [Шаг 6/9] JSON сохранён`

---

### Шаг 7: Конвертация в Excel

`▶ [Шаг 7/9] Конвертация в Excel`

```bash
python3 labeling/splitter_json_to_excel.py \
    labeling/data/<source_id>.splitter.v<N>.<mode_tag>.json \
    --out labeling/data/<source_id>.splitter.v<N>.<mode_tag>.xlsx
```

`✓ [Шаг 7/9] Excel сохранён`

---

### Шаг 8: Валидация против video.md

`▶ [Шаг 8/9] Валидация против video.md`

Если `<folder>/video.md` существует:

```bash
python3 labeling/validate_splitter_vs_video.py \
    --splitter labeling/data/<source_id>.splitter.v<N>.<mode_tag>.json \
    --video <folder>/video.md \
    --tolerance 120 \
    [--section-config <section_config>] \
    [--time-from <HH:MM:SS>] \
    [--time-to <HH:MM:SS>] \
    --out labeling/data/<source_id>.splitter.v<N>.<mode_tag>.validation.md
```

`--time-from` / `--time-to` — фильтруют главы video.md по временному диапазону.
**Обязательно использовать для multi-candidate транскриптов** (иначе coverage занижен,
т.к. validator сравнивает фрагмент интервью с полным списком глав всего видео).

Если нет — пропустить, сообщить.

`✓ [Шаг 8/9] Validation report готов`

---

### Шаг 9: Итоговый отчёт

```
[run-splitter v4.0 | model: claude-sonnet-4-6 | PRO subscription | execution: Agent subagent]
Folder:   transcripts/...
Mode:     mock_assisted_split
Version:  v1
Items:    N
Output:
  JSON:       labeling/data/<source_id>.splitter.v1.mock.json
  Excel:      labeling/data/<source_id>.splitter.v1.mock.xlsx
  Validation: labeling/data/<source_id>.splitter.v1.mock.validation.md

Validation: ✅ / ❌ — <результат>
```

---

## Нюансы

- `video.md` — только для валидации, НИКОГДА не передавать в subagent.
- Если subagent вернул JSON в markdown-обёртке — Шаги 5/6 снимают её.
- Если JSON большой и bash-heredoc escaping ломается — писать файл через Write tool напрямую.
- `prepare_prompt.py` экономит 2–4 минуты за счёт замены 5 Read tool calls одним Bash-вызовом.

### Multi-candidate транскрипты

Если в `timecodes.txt` несколько кандидатов (смена собеседуемого по ходу записи):

1. **Детектировать границу** по смене имени собеседуемого и/или фразам типа
   "сейчас буквально минуточку ждём", "к нам присоединится следующий кандидат".
2. **Разбить** содержимое на N фрагментов, сохранить во временные файлы
   (`/tmp/timecodes_<name>.txt`).
3. **Сообщить пользователю** о найденных кандидатах и временных границах перед запуском.
4. **Для каждого кандидата** запустить отдельный прогон (Шаги 3–9):

   **Шаг 3** — использовать `--transcript-file` и `--source-id-suffix`:
   ```bash
   python3 labeling/prepare_prompt.py \
       --folder <folder> \
       --mode mock_assisted_split \
       --transcript-file /tmp/timecodes_<name>.txt \
       --source-id-suffix _<name> \
       --version <N>
   ```

   **Шаг 8** — использовать `--time-from` / `--time-to` с границами кандидата:
   ```bash
   python3 labeling/validate_splitter_vs_video.py \
       --splitter labeling/data/<source_id>_<name>.splitter.v<N>.mock.json \
       --video <folder>/video.md \
       --tolerance 120 \
       --time-from <HH:MM:SS> \
       --time-to <HH:MM:SS> \
       --out labeling/data/<source_id>_<name>.splitter.v<N>.mock.validation.md
   ```

   Без `--time-from`/`--time-to` coverage будет занижен: validator сопоставит
   фрагмент кандидата с главами всего видео.

5. **Итоговый отчёт** — по каждому кандидату отдельная строка с coverage.

## Ограничения

- Один прогон = одна папка + один mode.
- API-ключ и API-кредиты не используются. Только PRO-подписка.
