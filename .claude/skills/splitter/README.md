# Splitter — skill в репозитории

Код и материалы skill лежат в **`.claude/skills/splitter/`**.  
**Все артефакты прогонов** (снимки входа в модель, JSON, xlsx, validation) сохраняются в **`splitter_output/`** в корне репозитории — имя каталога **`splitter_output`**, нижний регистр, не внутри skill.

## Структура папки skill

| Папка / файл | Назначение |
|--------------|------------|
| **`SKILL.md`** | Сценарий для агента: шаги, команды, ограничения. |
| **`README.md`** | Этот файл: обзор для людей. |
| **`config/`** | `splitter_run_config.json` (пути к промпту/схеме, `RUNTIME_HINTS`); опционально `section_topic_map.example.json`, `interview_paths.md`. |
| **`prompt,output_schema/`** | System-промпт и JSON Schema выхода: `splitter_system_prompt.txt`, `splitter_output_schema.json` (один каталог; пути в `config/splitter_run_config.json`). |
| **`scripts/`** | Исполняемые шаги пайплайна: `splitter_prepare_prompt.py`, `splitter_json_to_excel.py`, `splitter_validate_video.py`. |
| **`adhoc/`** | Вне основного пайплайна (обогащение feedback, просмотр окон) — если папка есть. |

## Порядок работы (основной pipeline)

1. **`scripts/splitter_prepare_prompt.py`** — читает папку интервью под `transcripts/…`, режим по наличию `video.md`, подставляет system и схему из путей в **`config/splitter_run_config.json`** (по умолчанию каталог **`prompt,output_schema/`**), пишет в **`splitter_output/`** файлы `*.user_prompt.txt` и `*.splitter_llm_input.txt`, печатает путь для сохранения JSON.
2. **LLM** (Cursor / Claude Code / Cloud) — по `splitter_llm_input.txt` или раздельно system + user; ответ — один JSON без markdown-обёртки.
3. **`scripts/splitter_json_to_excel.py`** — JSON → xlsx для ручного просмотра.
4. **`scripts/splitter_validate_video.py`** — если в папке интервью есть **`video.md`**: офлайн-сверка с JSON. **`video.md` в модель не передавать.**

Опционально позже: скрипты в **`adhoc/`** (постобработка JSON, вспомогательный разбор текста).

## Зачем хранить `*.user_prompt.txt` / `*.splitter_llm_input.txt`

Это **снимок входа** на конкретный прогон (`vN`): схема + транскрипт + подсказки. Нужен для сравнения прогонов, отладки и истории без восстановления из чата.

### Имена файлов и версия `vN`

Все артефакты одного прогона делят **одну** базу имени:  
`<source_id>.splitter.v<N>.<mock|raw>`  
и расширения/суффиксы: `.json`, `.xlsx`, `.validation.md`, `.user_prompt.txt`, `.splitter_llm_input.txt` и т.д. (как в примере `karpov_junior_ds_20220330.splitter.v4.mock.*`).

**Автоверсия** (если не передан `--version`): скрипт `splitter_prepare_prompt.py` смотрит в `splitter_output/` все файлы, подходящие под `<source_id>.splitter.v*.<mock|raw>.*`; если ни одного нет — **`v1`**, иначе **`v(max+1)`** по уже существующим номерам для этой пары `source_id` + режим. Режимы **mock** и **raw** считаются отдельно.

## Быстрый чеклист

### Биллинг

Извлечение Q&A делается **в чате** по артефактам после **`splitter_prepare_prompt.py`** — в рамках подписки продукта; отдельный Anthropic API key под сплиттер не требуется.

### Входы в модель

- System: путь из `config/splitter_run_config.json` (по умолчанию **`prompt,output_schema/splitter_system_prompt.txt`**).
- User / единый вход: `splitter_output/<base>.user_prompt.txt` и/или **`splitter_output/<base>.splitter_llm_input.txt`** (system+user+схема в одном файле).
- Схема в репозитории: **`prompt,output_schema/splitter_output_schema.json`** (и встроена в user-файл при сборке).

### Настройки и `RUNTIME_HINTS`

Файл **`config/splitter_run_config.json`** читает только **`splitter_prepare_prompt.py`**. Поля `system_prompt` и `schema` — пути **относительно корня skill** (`.claude/skills/splitter/`). Блок **`inference`** API не вызывает: значения копируются в секцию **`RUNTIME_HINTS`** внутри каждого сгенерированного `splitter_output/*.user_prompt.txt`. Подробнее — в **`SKILL.md`**.

### Команды после JSON

```bash
python3 .claude/skills/splitter/scripts/splitter_json_to_excel.py \
  splitter_output/<base>.json --out splitter_output/<base>.xlsx

python3 .claude/skills/splitter/scripts/splitter_validate_video.py \
  --splitter splitter_output/<base>.json \
  --video transcripts/<папка-интервью>/video.md \
  --tolerance 120 \
  --out splitter_output/<base>.validation.md
```

Опционально для строгой проверки тем по блокам видео: **`--section-config`** (шаблон формата — `config/section_topic_map.example.json`; обычно копия с правками под интервью).

### Режим mock / raw

По умолчанию **mock**, если в папке интервью есть **`video.md`**, иначе **raw**.

## Документация

- **`SKILL.md`** — полный пошаговый сценарий для агента и детали конфига.

Первый запуск из корня репозитория:

```bash
python3 .claude/skills/splitter/scripts/splitter_prepare_prompt.py \
  --folder transcripts/<папка-интервью>
```
