---
name: splitter
description: >
  Split interview transcript into Q&A JSON: prepare → LLM → Excel → validation.
  Announce each step and total runtime to the user. Full procedure in this file.
---

# Splitter

Last updated: 2026-05-19

Документ для людей, **Cursor** (skill `/splitter`) и **Claude Code** (`/splitter`). Cursor Rules для splitter **не используются** — только этот SKILL.md. Отдельного `README.md` в skill нет.

---

## Структура skill (по шагам пайплайна)

| Шаг | Папка | Содержимое |
|-----|--------|------------|
| 1 Подготовка | `step1-prepare/` | `splitter_prepare_prompt.py`, `run_config.json`, `splitter_system_prompt.txt`, `splitter_output_schema.json` |
| 2 Извлечение Q&A | `step2-extract-qa/` | только `STEP.md` — шаг выполняет агент (LLM), скрипта нет |
| 3 Excel | `step3-excel/` | `splitter_json_to_excel.py` |
| 4 Валидация по главам | `step4-validate-chapters/` | `splitter_validate_video.py`, `splitter_validate_chapters.py`, `section_topic_map.*.json` |
| 5 LLM-валидация | `step5-validate-llm/` | `validation_llm_system_prompt.txt`, `validation_llm_output_schema.json` |
| — | `adhoc/` | разовые утилиты, не в пайплайне |

Постобработка после шага 2: `scripts/splitter_post.sh` в корне репо (Excel + шаг 4 + приложение LLM в конце того же `.md`).

**Шаг 4 vs 5:** шаг **4** — детерминированный отчёт (таблица YouTube ↔ сплиттер, непокрытые фрагменты). Шаг **5** — семантика через LLM: приложение в **том же** `*.validation.vN.md` → `*.validation.llm.vN.json` → строки LLM в таблице при `--llm-json`.

---

## Модели LLM (обязательно, для сопоставимости Cursor ↔ Claude Code)

Единый источник: **`step1-prepare/run_config.json`**.

| Шаг | Поле в config | Значение по умолчанию |
|-----|----------------|----------------------|
| 2 Извлечение Q&A | `inference.model` | `claude-sonnet-4-6` |
| 2 | `inference.temperature` | `0` |
| 5 LLM-валидация | `validation_inference.model` | `claude-sonnet-4-6` |
| 5 | `validation_inference.temperature` | `0` |

**Правила для агента:**

1. Читать модель из `run_config.json`, из `{basename}.vN.run.json` и из `RUNTIME_HINTS` в `*.llm-input.txt` (шаг 2) / приложении LLM в `*.validation.md` (шаг 5).
2. **Не выбирать модель самостоятельно** (не GPT, не «лучшую на взгляд») и **не** запускать subagent/Task с другой моделью.
3. В Cursor: режим Agent с **Claude Sonnet 4.6** (или эквивалент `claude-sonnet-4-6` из config). В Claude Code: та же модель по имени из config.
4. Смена модели — только если пользователь явно попросил; тогда зафиксировать в отчёте «Готово».

Почему Sonnet: одна и та же модель доступна в Cursor и Claude Code; temperature 0 для воспроизводимости.

---

## Что делает splitter

Читает **готовый транскрипт** интервью из папки `transcripts/` и выдаёт **список пар вопрос–ответ** с тайм-кодами.

**Splitter не скачивает видео и не создаёт транскрипты** — только читает файлы, которые уже лежат в папке интервью.

---

## Вход (до запуска)

Папка интервью, например:

`transcripts/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/`

| Файл | Что это |
|------|---------|
| **`timecodes.txt`** | Транскрипт **с** тайм-кодами (`[HH:MM:SS]` в начале строк). **Предпочтительный** вход, если файл есть |
| **`transcript.txt`** | Транскрипт **без** тайм-кодов. Используется, если нет `timecodes.txt` |
| **`video.md`** | Главы YouTube (тайм-код + название) + описание видео с YouTube. **Не** идёт в LLM; нужен только для валидации |
| `feedback.md`, `link.txt` | Опционально |

**Выбор транскрипта:** сначала `timecodes.txt`, иначе `transcript.txt` — для любых папок (`mock-interviews` и `real-interviews`).

Тип интервью (**mock** vs **real**) — только корень `mock-interviews/` или `real-interviews/` (в `transcripts/` и `splitter_output/` одинаково). Префикса `mock-` / `real-` в имени листовой папки и файлов **нет**. Режим splitter — только в JSON.

---

## Выход (после пайплайна)

### Куда сохраняются файлы

Структура как в `transcripts/` (корень `mock-interviews` / `real-interviews` + publisher), но **без** `mock-` / `real-` в имени листовой папки и файлов:

```text
splitter_output/mock-interviews/<publisher>/<basename>/
splitter_output/real-interviews/<publisher>/<basename>/
```

| | Пример |
|---|--------|
| Папка | `.../data-scientist-junior-karpov-2022-03-30/` (одинаковое имя) |
| Файл JSON | `data-scientist-junior-karpov-2022-03-30.v1.qa-split.json` |

- **`mock-interviews` / `real-interviews`** — тип корпуса (постановка vs реальная запись).
- **`<basename>`** — имя листовой папки (без префикса mock/real).

В JSON **`source_id`** = `basename` с `-` → `_` (например `data_scientist_junior_karpov_20220330`).

### Файлы в этой папке

| Файл | Назначение |
|------|------------|
| **`{basename}.vN.qa-split.json`** | **Главный результат** — массив пар Q&A |
| **`{basename}.vN.qa-split.xlsx`** | Те же данные в Excel — удобно читать человеку |
| **`{basename}.vN.validation.md`** | **Единственный** отчёт валидации (если есть `video.md`) |
| **`{basename}.vN.llm-input.txt`** | Снимок всего, что ушло в модель на этапе извлечения Q&A |
| **`{basename}.vN.run.json`** / **`.run.md`** | Протокол прогона: модели, шаги, входы/выходы, длительности |

Фильтр одного прогона в IDE: `*{basename}.v8*`. Старые имена `*.qa-split.vN.*` — legacy (см. `scripts/migrate_splitter_v_prefix_names.py`).

`v1`, `v2`, … — номер прогона; следующий прогон увеличивает версию.

### Поля в JSON

Полная схема: `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`.

**Корень:**

| Поле | Значение |
|------|----------|
| `source_id` | Идентификатор интервью (см. выше) |
| `splitter_mode` | Как отработал splitter (см. таблицу ниже), **не** тип интервью |
| `items` | Массив пар Q&A |

**Две оси — не путать:**

| Ось | Где | Значения |
|-----|-----|----------|
| **Тип интервью** | `mock-interviews/` / `real-interviews/` в `transcripts/` и `splitter_output/` | Постановочное vs запись реального собеседования |
| **Режим splitter** | поле `splitter_mode` в JSON | Как резали и проверяли транскрипт |

| `splitter_mode` | Когда (авто) | Шаг валидации |
|-----------------|--------------|---------------|
| `split_and_validate` | В папке есть **`video.md`** | Да |
| `split_only` | **`video.md`** нет | Нет |

У Новосёлова (`real-interviews/novoselov/…`) часто есть `video.md` → будет `split_and_validate`, хотя интервью **real**. Это нормально.

**Каждый элемент `items[]`:**

| Поле | Значение |
|------|----------|
| `interviewer_question` | `{ "text", "time" }` — вопрос, дословно из транскрипта |
| `candidate_answer` | `{ "text", "time" }` — ответ; `text: null`, если не отвечал |
| `reference_answer` | Эталон от интервьюера или `null` |
| `interviewer_feedback` | Комментарий после ответа или `null` |
| `question_type` | `hard` \| `soft` \| `behavioral` |
| `question_topic` | `Python`, `SQL`, `Statistics`, `ML`, … |
| `interview_stage` | `technical_qna`, `behavioral`, … |

### Отчёт validation (шаг 4) — один файл

Скрипт: `step4-validate-chapters/splitter_validate_video.py` (из `scripts/splitter_post.sh`).

**Артефакт для человека — только** `{basename}.vN.validation.md`. Протокол прогона — `{basename}.vN.run.md`. Не создавать `*.summary.md`, `*.full.md`.

**Содержимое файла (сверху вниз):**

1. Вердикт и метрики.
2. **Что проверяем** — правила (YouTube ↔ JSON, покрытие, тема, тайм-коды).
3. **Все главы YouTube** — таблица: статус, **куда в JSON** (item # и поле), items, Δt.
4. **Исключённые главы** — почему не вопрос; для «Разбор»/«Объяснение» — trace в `reference_answer` / `interviewer_feedback`.
5. **Подводки (🔗)** — в какой `interviewer_question` следующего (или предыдущего) item попал текст.
6. **Не распознанные (❌)** — гипотеза (пропуск / самоответ интервьюера / смещение) + транскрипт.
7. **Распознанные вопросы** — полные Q/A/reference/feedback (примеры).
8. **Фрагменты транскрипта без Q&A** — непокрытые куски `timecodes.txt`.
9. Комментарий и справочные таблицы.
10. **Приложение: LLM-валидация (шаг 5)** — в конце **того же** `.md`.

**Не путать с отчётом:** `*.validation.llm.vN.json` — только машинный ответ шага 5 для подмешивания строк LLM, не второй human-readable отчёт.

**Coverage** = доля вопросных глав (без подводок 🔗) с ≥1 item в **±tolerance** от маркера главы. Сдвиг тайм-кода (YouTube `00:30:57`, сплиттер `00:30:44`) — **не ошибка**, если item есть и Δt в допуске.

Подводки (`Подводка к…`) — статус 🔗, не отдельный вопрос; текст должен входить в следующий `interviewer_question` (промпт шага 2).

| Статус | Значение |
|--------|----------|
| ❌ не распознан | нет item в ±tolerance от маркера главы |
| ✅ один / несколько Q&A | есть item(s); полные тексты в том же `.md` |
| 🔗 подводка | не отдельный вопрос |
| — исключено | вступление, разбор, конец |

### LLM-валидация (шаг 5, опционально)

1. В конце `*.qa-split.validation.vN.md` — раздел **«Приложение: LLM-валидация»** (вход для модели).
2. Агент пишет JSON → `*.validation.llm.vN.json`.
3. Повторный запуск валидатора с `--llm-json` подмешивает строки **LLM — тайм-коды** / **LLM — содержание** в тот же `.md`.

Поля LLM на главу: `time_alignment_ok`, `content_alignment_ok`, `notes`.

### Что внутри `llm-input`

Один текстовый файл, который собирает `splitter_prepare_prompt.py`:

- system-промпт (`splitter_system_prompt.txt`) — как резать Q&A;
- JSON Schema (`splitter_output_schema.json`);
- транскрипт (`timecodes.txt` или `transcript.txt`);
- `SOURCE_ID`, `SPLITTER_MODE`, путь куда сохранить `.json`.

На этапе извлечения Q&A модель читает **только** этот файл.

---

## Пайплайн (пять шагов)

| # | Название | Папка / скрипт | LLM? | Вход → выход |
|---|----------|----------------|------|----------------|
| 1 | **Подготовка** | `step1-prepare/splitter_prepare_prompt.py` | Нет | Папка в `transcripts/` → `*.qa-split.llm-input.vN.txt` |
| 2 | **Извлечение Q&A** | `step2-extract-qa/` (агент) | Да | `llm-input` → `*.qa-split.vN.json` |
| 3 | **Excel** | `step3-excel/splitter_json_to_excel.py` | Нет | `json` → `*.qa-split.vN.xlsx` |
| 4 | **Валидация по главам** | `step4-validate-chapters/splitter_validate_video.py` | Нет | `json` + `video.md` → `*.qa-split.validation.vN.md` |
| 5 | **LLM-валидация** | `step5-validate-llm/` (агент) | Да | приложение в том же `.md` → `*.validation.llm.vN.json` → строки LLM в `.md` |

Шаги **3 и 4** одной командой: `scripts/splitter_post.sh <json> --video <папка>/video.md` (внутри Excel, validate, `--prepare-llm` для шага 5).  
Шаг **5** — отдельно в чате; затем перезапуск validate с теми же аргументами (json подхватится).

Без `video.md`: только шаги 1–3 (`splitter_mode: split_only`).

Повторный прогон с исправленным промптом: снова шаги 1–5 с версией `vN+1`.

### Цикл исправления (после шага 4)

Если в `*.qa-split.validation.vN.md` есть ❌ **не распознан** или вердикт не **ПРОЙДЕНО**:

1. Показать пользователю список нераспознанных глав и цитаты транскрипта из отчёта.
2. Решить: пропуск сплиттера → правка промпта / повтор шага 2; ложная глава YouTube → `EXPLANATION_PREFIXES` в `splitter_validate_video.py` или правка `video.md`.
3. При повторе извлечения: шаги **1–2** (новая версия `vN+1`), затем **3–5**. Не перезаписывать json без новой версии.
4. Максимум **2** полных цикла за один запуск `/splitter`, дальше — эскалация пользователю.

### Шаг 1 — Подготовка

```bash
python3 .claude/skills/splitter/step1-prepare/splitter_prepare_prompt.py \
  --folder transcripts/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30
```

Скрипт не вызывает API. В терминале — пути к `llm-input`, будущему `json` и команде `splitter_post.sh`.

### Шаг 2 — Извлечение Q&A

- Прочитать `*.qa-split.llm-input.vN.txt`.
- Модель: **`inference.model`** из `run_config.json` (см. RUNTIME_HINTS в файле).
- Не подмешивать `video.md` и другие интервью.
- Ответ: **только JSON**, без markdown-обёртки; temperature 0.
- Сохранить в путь `.json` из `llm-input`.

### Шаг 3 — Excel

```bash
python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py \
  splitter_output/.../....qa-split.vN.json \
  --out splitter_output/.../....qa-split.vN.xlsx
```

Или вместе со шагом 4 через `scripts/splitter_post.sh`.

### Шаг 4 — Валидация по главам

```bash
python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
  --splitter splitter_output/.../....qa-split.vN.json \
  --video transcripts/.../video.md \
  --out splitter_output/.../....qa-split.validation.vN.md \
  --prepare-llm
```

Обычно вызывается из `splitter_post.sh` (там же `--prepare-llm`).

### Шаг 5 — LLM-валидация

- Прочитать раздел **«Приложение: LLM-валидация»** в конце `*.qa-split.validation.vN.md`.
- Модель: **`validation_inference.model`** из `run_config.json` (RUNTIME_HINTS в файле).
- Ответ: JSON по `step5-validate-llm/validation_llm_output_schema.json`.
- Сохранить JSON по пути из приложения; перезапустить валидатор с `--llm-json` (те же `--splitter --video --out`).

---

## Протокол для пользователя (обязательно)

При **любом** запуске splitter (Cursor, Claude Code, `/splitter`) агент **обязан** писать пользователю, что делает, и фиксировать время.

### В начале

1. Записать время старта (локальное, например `2026-05-19 14:32`).
2. Вывести план прогона — какие шаги будут, с номерами:

```text
План splitter pipeline
──────────────────────
□ Шаг 0 — Проверка входа (FOLDER, файлы)
□ Шаг 1 — Подготовка (step1-prepare, без LLM)
□ Шаг 2 — Извлечение Q&A (LLM)
□ Шаг 3 — Excel (step3-excel / splitter_post.sh)
□ Шаг 4 — Валидация по главам (step4-validate-chapters)   [если есть video.md]
□ Шаг 5 — LLM-валидация (step5-validate-llm)             [если в .md есть приложение LLM]
```

Шаги 4–5 помечать «пропуск», если нет `video.md` / не делали `--prepare-llm`.

### Перед каждым шагом

Коротко объявить **текущий шаг**:

```text
▶ Шаг 2/4 — Извлечение Q&A (LLM)
Читаю: splitter_output/.../....qa-split.llm-input.v6.txt
```

Нумерация: **текущий / всего запланированных** (шаг 0 не входит в знаменатель). Полный прогон с `video.md`: **5** шагов (1–5).

| Сообщение | Шаг |
|-----------|-----|
| Проверка FOLDER | **Шаг 0** |
| `step1-prepare/splitter_prepare_prompt.py` | **Шаг 1** |
| LLM → json | **Шаг 2** |
| Excel (`splitter_post.sh` или step3) | **Шаг 3** |
| `splitter_validate_video.py` | **Шаг 4** |
| LLM validation → json + обновить md | **Шаг 5** |

`splitter_post.sh` объединяет шаги 3–4 и готовит llm-input для шага 5 — в сообщениях можно писать «▶ Шаг 3–4» один раз, но в плане лучше перечислить 3, 4, 5 отдельно.

### После каждого шага

1–2 строки итога: что создано (путь, версия `vN`), ошибка или ок. Обновлять **`{basename}.vN.run.json`** (шаги 2 и 5 — через `splitter_run_log.py`).

```text
✓ Шаг 1 готов — llm-input: .../....v6.llm-input.txt, json: ...v6.qa-split.json, run: ...v6.run.md
```

**Лог шагов (агент):**
```bash
python3 .claude/skills/splitter/scripts/splitter_run_log.py \
  --run-json splitter_output/.../....vN.run.json \
  --step 2 --name qa_extraction --llm --model claude-sonnet-4-6 \
  --input ...vN.llm-input.txt --output ...vN.qa-split.json --duration-sec 120
```
Шаги 3–4 пишет `scripts/splitter_post.sh` автоматически.

### В конце

1. Время окончания и **длительность** (минуты и секунды, от старта до финала).
2. Итоговый отчёт (пути, число items, вердикт validation, примеры глав).

```text
Готово
──────
Старт:  2026-05-19 14:32
Финиш:  2026-05-19 14:58
Время:  26 мин

FOLDER: transcripts/.../data-scientist-junior-karpov-2022-03-30
Версия: v6 | items: 33
...
```

Не пропускать объявления шагов, даже если шаг выполняется быстро.

---

## Запуск в Cursor (агент)

Один чат = одно интервью. Скопируй блок ниже в **новый чат** (Agent mode), подставь путь к папке.

### Промпт для агента (скопировать целиком)

```text
Запусти полный splitter pipeline для одного интервью.

FOLDER=transcripts/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30

Обязательно следуй .claude/skills/splitter/SKILL.md (разделы «Протокол для пользователя» и «Запуск в Cursor»).

Перед стартом — зафиксируй время, выведи план шагов (□), затем выполняй с объявлением «▶ Шаг N/…» до и «✓» после каждого шага.

Шаг 0 — проверка:
1) FOLDER существует; файлы: timecodes.txt / transcript.txt, video.md.
2) mock-interviews или real-interviews, basename.

Шаги (выполни все):
1. Подготовка (без LLM):
   python3 .claude/skills/splitter/step1-prepare/splitter_prepare_prompt.py --folder "$FOLDER"
   Запомни из вывода: путь к llm-input, путь к будущему json, версию vN.

2. Извлечение Q&A (LLM):
   - Прочитай ТОЛЬКО *.qa-split.llm-input.vN.txt из splitter_output (не video.md, не другие интервью).
   - Ответ: один JSON без markdown-обёртки, temperature 0.
   - Сохрани в путь json из llm-input.

3–4. Постобработка (без LLM), если есть video.md:
   scripts/splitter_post.sh <путь-к-json> --video "$FOLDER/video.md"
   (Excel + validation.md с приложением LLM для шага 5)

5. LLM-валидация (раздел «Приложение» в конце того же *.qa-split.validation.vN.md):
   - Прочитай приложение, верни JSON по step5-validate-llm/validation_llm_output_schema.json.
   - Сохрани в *.validation.llm.vN.json (путь в приложении).
   - Перезапусти step4-validate-chapters/splitter_validate_video.py с --llm-json.

В конце — блок «Готово» со временем (старт, финиш, длительность) и отчёт:
- FOLDER и версия vN
- число items в json
- пути: json, xlsx, validation.md, llm-input (и llm.json если был шаг 5)
- вердикт из validation.md (ПРОЙДЕНО / ЧАСТИЧНО / ПРОВАЛ)
- 2–3 главы YouTube: «не распознан» / «несколько Q&A», если есть
```

### Пример для теста (Karpov junior DS)

| | Путь |
|---|------|
| Вход | `transcripts/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/` |
| Выход | `splitter_output/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/` |

В папке входа должны быть `timecodes.txt` и `video.md`. Следующий прогон создаст `v6` (если уже есть v1–v5).

### Custom Agent в Cursor (опционально)

**Cursor Settings → Agents → New Agent**

- **Name:** `Splitter pipeline`
- **Instructions:** текст из промпта выше + «всегда читай `.claude/skills/splitter/SKILL.md`; соблюдай протокол шагов и времени для пользователя».

Запуск: новый чат → выбери агента **Splitter pipeline** → вставь только строку  
`FOLDER=transcripts/...`  
или полный промпт.

### Что смотреть после прогона

1. **`*.qa-split.vN.json`** — главный результат.
2. **`*.qa-split.vN.xlsx`** — то же для глаз.
3. **`*.qa-split.validation.vN.md`** — единственный отчёт валидации (таблица + непокрытые фрагменты транскрипта).

---

## Cursor / Claude Code

- **Cursor:** skill `/splitter` или промпт из раздела «Запуск в Cursor».
- **Claude Code:** `/splitter` + путь к папке интервью.
