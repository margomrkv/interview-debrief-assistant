---
name: splitter
description: >
  Split interview transcript into Q&A JSON: prepare → LLM (fresh per vN, no inheriting
  prior qa-split) → Excel → validation → correction loop until ✅ ПРОЙДЕНО.
  Same procedure in Cursor (/splitter) and Claude Code. Full steps in this file.
---

# Splitter

Last updated: 2026-05-21

Документ для людей, **Cursor** (skill `/splitter`) и **Claude Code** (`/splitter`). Cursor Rules для splitter **не используются** — только этот SKILL.md. Отдельного `README.md` в skill нет.

### Пути в репозитории (после mass moving)

| Назначение | Каталог |
|------------|---------|
| Вход интервью (`timecodes.txt`, `video.md`, …) | `data/knowledgebase/raw/mock-interviews/…` или `…/real-interviews/…` |
| Выход splitter (4 файла на `vN`) | `data/knowledgebase/splitted/…` (та же вложенность `mock|real-interviews/<publisher>/<basename>/`) |
| Собственные интервью (CV, feedback) | `data/candidatecontext/` — локально, **не** в public repo; **не** через splitter mock/real |

**`FOLDER` для шага 1:** `data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30` (пример).

Скрипт `step1-prepare/splitter_prepare_prompt.py` (+ `kb_paths.py`) принимает и устаревший префикс `transcripts/…`, если папка уже переехала в `raw/`.

---

## Структура skill (по шагам пайплайна)

| Шаг | Папка | Содержимое |
|-----|--------|------------|
| 1 Подготовка | `step1-prepare/` | `splitter_prepare_prompt.py`, `splitter_run_log.py`, `artifact_paths.py`, `run_manifest.py`, `kb_paths.py`, `interview_locale.py`, `run_config.json`, `splitter_system_prompt.txt`, `splitter_output_schema.json` |
| 2 Извлечение Q&A | `step2-extract-qa/` | только `STEP.md` — шаг выполняет агент (LLM), скрипта нет |
| 3 Excel | `step3-excel/` | `splitter_json_to_excel.py`, `splitter_post.sh` (шаги 3–4 одной командой) |
| 4 Валидация по главам | `step4-validate-chapters/` | `splitter_validate_video.py`, `splitter_validate_chapters.py`, `splitter_verdict.py`, `section_topic_map.*.json` |
| 5 LLM-валидация | `step5-validate-llm/` | `validation_llm_system_prompt.txt`, `validation_llm_output_schema.json`, `splitter_run_step5.py` (headless CI) |
| — | `adhoc/` | разовые утилиты, не в пайплайне |

Постобработка после шага 2: `step3-excel/splitter_post.sh` (Excel + шаг 4 + промпт шага 5 в `pipeline-log.md`). Старый путь `scripts/splitter_post.sh` в корне репо — обёртка на тот же файл.

**Шаг 4 vs 5:** шаг **4** — детерминированный `validation-report.md`. Шаг **5** — промпт в `pipeline-log.md`, ответ JSON в конце `validation-report.md` → строки LLM при перезапуске валидатора.

### Язык интервью (обязательно)

Определяется на шаге 1: `video.md` → `language:` в frontmatter, иначе эвристика по `PRIMARY_TRANSCRIPT` (кириллица → `ru`, иначе `en`). Пишется в `pipeline-log.md` как `INTERVIEW_LANGUAGE`.

| `INTERVIEW_LANGUAGE` | JSON (`text` в items) | `validation-report.md` | Заметки шага 5 |
|----------------------|------------------------|-------------------------|----------------|
| `ru` | дословный русский ASR | русский (заголовки, таблицы, проверки) | русский |
| `en` | дословный английский ASR | English (headers, tables, checks) | English |

Запрещено: русский транскрипт → английский пересказ в JSON; английский mock → русская оболочка отчёта. Enum в JSON (`question_type`, `question_topic`) — всегда по схеме на английском.

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

1. Читать модель из `run_config.json` и из `RUNTIME_HINTS` в `{basename}.vN.pipeline-log.md` — секции `LLM_INPUT_STEP_2` и `LLM_INPUT_STEP_5`.
2. **Не выбирать модель самостоятельно** (не GPT, не «лучшую на взгляд») и **не** запускать subagent/Task с другой моделью.
3. **Шаг 5 обязателен** при наличии `video.md`: после `splitter_post.sh` агент **в том же чате** выполняет `LLM_INPUT_STEP_5`, сохраняет JSON в `validation-report.md`, перезапускает `splitter_validate_video.py`. **Не завершать** прогон `/splitter`, пока в отчёте шаг 5 не отражён (колонка «Смысл (5)» и строки «Проверка главы»).
4. В Cursor: режим Agent с **Claude Sonnet 4.6** (или эквивалент `claude-sonnet-4-6` из config). В Claude Code: та же модель по имени из config.
5. Смена модели — только если пользователь явно попросил; тогда зафиксировать в блоке «Готово».

Почему Sonnet: одна и та же модель доступна в Cursor и Claude Code; temperature 0 для воспроизводимости.

---

## Каждый прогон с нуля (обязательно для агента)

Номер версии **`vN`** — только метка артефактов **этого** прогона. Он **не** означает «возьми результат прошлого прогона и подправь».

### Запрещено на шаге 2 (и в цикле исправления при новой `vN+1`)

- **Не читать**, **не копировать**, **не мержить** и **не «исправлять точечно»** файлы предыдущих версий:
  - `data/knowledgebase/splitted/.../{basename}.v(N-1).qa-split.json` (и любые `v1`, `v2`, … кроме **текущей** `vN` из шага 1);
  - старые `.xlsx`, `validation-report.md` прошлых прогонов — только для **диагностики** после шага 4–5, не как источник `items[]`.
- **Не** переносить `items`, тексты полей или enum из прошлого JSON «потому что валидация уже проходила».
- **Не** сокращать шаг 2 до «скопировать v(N-1) + поправить schema/feedback» — даже если в папке уже лежит удачный `v(N-1)`.

### Обязательно на шаге 2

1. Единственный источник Q&A: блок **`LLM_INPUT_STEP_2`** в **`{basename}.vN.pipeline-log.md`**, созданный **только что** на шаге 1 для этой `vN` — поле **`PRIMARY_TRANSCRIPT`** (+ sidecars только для границ, не для фактов).
2. Полный заново LLM-разбор транскрипта → записать **пустой** `{basename}.vN.qa-split.json` (файл из шага 1 ещё не существует или перезаписать целиком после извлечения).
3. Актуальные правила — из **`splitter_system_prompt.txt`** и system prompt **внутри** `LLM_INPUT_STEP_2` этого прогона (после смены SKILL/промпта старые JSON **устарели**).

### Версии `vN` vs `vN+1`

| Действие | Разрешено |
|----------|-----------|
| Сохранить старый `v(N-1).qa-split.json` на диске (история) | да |
| Использовать его как вход шага 2 для новой `vN` | **нет** |
| Цикл исправления: новая `vN+1` → снова шаги **1–2** с новым транскриптным промптом | да |
| Цикл исправления: только patch старого JSON без шага 2 | **нет** |

Если агент «ускоряет» прогон через наследование — прогон **невалиден**, даже при ✅ в отчёте.

**Техническая реализация (обязательно):**

| Момент | Скрипт | Что делает |
|--------|--------|------------|
| Шаг 1 | `step1-prepare/splitter_prepare_prompt.py` | Пишет **пустой** `{basename}.vN.qa-split.json` (`items: []`) и список **запрещённых** файлов `v1…v(N-1)` в `pipeline-log.md` |
| После шага 2 | `step1-prepare/splitter_check_prior_leak.py` | Exit **1**, если fingerprint `items[]` **совпадает** с любой старой версией |
| Шаг 3–4 | `step3-excel/splitter_post.sh` | Повторяет `splitter_check_prior_leak.py` перед Excel/validate |

```bash
python3 .claude/skills/splitter/step1-prepare/splitter_check_prior_leak.py \
  data/knowledgebase/splitted/.../{basename}.vN.qa-split.json
```

### Разделение спикеров (частые ошибки на behavioral)

В транскриптах **нет меток спикера**; длинный монолог кандидата часто продолжается **после** короткой реплики интервьюера.

| Поле | Только речь |
|------|-------------|
| `interviewer_question.text` | интервьюера: **только из PRIMARY_TRANSCRIPT** (склейка соседних реплик интервьюера; не текст кандидата) |
| `candidate_answer.text` | кандидата (весь turn до следующего вопроса интервьюера); **не повторяет** начало `interviewer_question` |
| `interviewer_feedback.text` | интервьюера: уточнение, «угу», разбор, подсказка **в окне этого item** |
| `reference_answer.text` | развёрнутый **самоответ** интервьюера (кандидат молчал) |

**Запрещено**

- один и тот же фрагмент в **вопросе и ответе** (типично при нарезке по `timecodes.txt` без ролей);
- класть в `interviewer_question` монолог кандидата;
- на шаге 2 подглядывать в `video.md` / заголовки YouTube (только шаги 4–5);
- «улучшать» обрывки вопроса по оглавлению YouTube вместо склейки реплик интервьюера в транскрипте;
- класть в `interviewer_feedback` продолжение биографии/кейса кандидата («я пошёл в Яндекс», «у нас Kanban», «мы причесали Trello») — только в `candidate_answer` или следующий item.

Если после ответа кандидата интервьюер **не** говорил по этой паре — `interviewer_feedback`: `{"text": null, "time": null}`.

Итоговый debrief («флажок», «красный флаг») — только речь интервьюера; привязать к item по теме.

Подробности: `splitter_system_prompt.txt` (§ `interviewer_question vs candidate_answer`, § `interviewer_feedback`).

**Проверка в отчёте:** `validation-report.md` → секция «Проверка границ реплик» (эвристика: дубли Q/A, обрывки вопроса, смешение в answer).

### Pair programming (`technical_coding`) — реплики перемешаны

В Colab/screen-share **нет diarization**: строка `[00:49:39]` может содержать и кандидата («ну я бы видел цикл»), и интервьюера («супер напиши») в одной строке.

| Поле | Содержимое |
|------|------------|
| `interviewer_question` | только постановка задачи |
| `candidate_answer` | **только** реплики кандидата за всю задачу (склейка span'ов) |
| `interviewer_feedback` | **только** подсказки интервьюера за ту же задачу (может быть длинным) |
| `reference_answer` | финальное эталонное решение в конце |

**Запрещено:** один длинный `candidate_answer` с «ты видишь», «давай напишем», «не слушай ты усложняешь» — это речь интервьюера, не кандидата.

Эвристика в отчёте: `pair programming (technical_coding): …` у item'ов вроде group-by Python.

---

## Что делает splitter

Читает **готовый транскрипт** интервью из папки `data/knowledgebase/raw/` и выдаёт **список пар вопрос–ответ** с тайм-кодами.

**Splitter не скачивает видео и не создаёт транскрипты** — только читает файлы, которые уже лежат в папке интервью.

### Разделение: извлечение vs валидация

| Источник | Шаг 2 (извлечение Q&A) | Шаги 4–5 (валидация) |
|----------|------------------------|----------------------|
| `timecodes.txt` / `transcript.txt` | **Да** — единственный обязательный вход для LLM | Косвенно (сверка тайм-кодов полей) |
| `video.md` (главы YouTube) | **Нет** — не в `LLM_INPUT_STEP_2`, агент не читает | **Да** — эталон для coverage и смысла |
| `feedback.md` | Опционально в sidecar (границы), не факты | Нет |

**Почему:** в **real-интервью** будет только транскрипт. Mock с `video.md` нужен, чтобы **после** разметки проверить качество; подсказки из оглавления на шаге 2 делают mock «слишком лёгким» и не переносятся на prod.

Если шаг 5 пишет «вопрос не совпадает с заголовком главы» — править **промпт шага 2** (роли, склейка ASR), а не подставлять заголовок YouTube в JSON.

---

## Вход (до запуска)

Папка интервью, например:

`data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/`

| Файл | Что это |
|------|---------|
| **`timecodes.txt`** | Транскрипт **с** тайм-кодами (`[HH:MM:SS]` в начале строк). **Предпочтительный** вход, если файл есть |
| **`transcript.txt`** | Транскрипт **без** тайм-кодов. Используется, если нет `timecodes.txt` |
| **`video.md`** | Главы YouTube (тайм-код + название) + описание видео с YouTube. **Не** идёт в LLM; нужен только для валидации |
| `feedback.md`, `link.txt` | Опционально |

**Выбор транскрипта:** сначала `timecodes.txt`, иначе `transcript.txt` — для любых папок (`mock-interviews` и `real-interviews`).

Тип интервью (**mock** vs **real**) — только корень `mock-interviews/` или `real-interviews/` (в `data/knowledgebase/raw/` и `data/knowledgebase/splitted/` одинаково). Префикса `mock-` / `real-` в имени листовой папки и файлов **нет**. Режим splitter — только в JSON.

### Мультикандидатные записи

Когда YouTube-видео содержит несколько кандидатов, каждый обрабатывается **отдельно**: своя папка в `data/knowledgebase/raw/`, свой прогон сплиттера, свой `data/knowledgebase/splitted/`.

**Признак сегмента:** комментарий в начале `video.md`:
```
<!-- split_from: <источник> [<имя>] -->
<!-- segment is a logical interview extracted from a multi-candidate recording -->
```

**Правила `video.md` для каждого кандидата:**

1. `video.md` содержит **только** главы своего кандидата (чужие главы удалены).
2. Тайм-коды в `video.md` — **всегда абсолютные** (как на YouTube), независимо от того, из какой части видео кандидат.
3. Если `timecodes.txt` кандидата содержит **относительные** тайм-коды (клип вырезан, стартует с 0:00), в `video.md` добавляется комментарий со смещением:

   ```html
   <!-- time_offset_seconds: N -->
   ```

   где `N` = абсолютное время начала сегмента на YouTube в секундах.  
   Пример: кандидат начинается в `00:31:05` → `time_offset_seconds: 1865`.

4. Первый кандидат обычно не требует смещения (клип совпадает с началом видео → offset = 0).

**Как валидатор использует смещение:**  
`splitter_validate_video.py` читает `time_offset_seconds` и при сопоставлении применяет:  
`effective_chapter_time = chapter_time_absolute − time_offset_seconds`  
Это переводит абсолютные тайм-коды глав в относительную систему тайм-кодов транскрипта.

**Когда добавлять `time_offset_seconds`:**  
Если `timecodes.txt` начинается около `00:00:xx` (< 30 с), а соответствующая глава в `video.md` — значительно позже (> 5 мин), то это относительные тайм-коды: добавьте смещение.

---

## Выход (после пайплайна)

### Куда сохраняются файлы

Структура как в `data/knowledgebase/raw/` (корень `mock-interviews` / `real-interviews` + publisher), но **без** `mock-` / `real-` в имени листовой папки и файлов:

```text
data/knowledgebase/splitted/mock-interviews/<publisher>/<basename>/
data/knowledgebase/splitted/real-interviews/<publisher>/<basename>/
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
| **`{basename}.vN.validation-report.md`** | Отчёт валидации (если есть `video.md`) |
| **`{basename}.vN.pipeline-log.md`** | Журнал прогона + промпты LLM (manifest в HTML-комментарии) |

Фильтр одного прогона в IDE: `*{basename}.v8*`. Старые имена `*.qa-split.vN.*` — legacy (удалены при миграции на `{basename}.vN.*`).

`v1`, `v2`, … — номер прогона; следующий прогон увеличивает версию. См. **«Каждый прогон с нуля»** — новая `vN` не наследует JSON предыдущих версий.

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
| **Тип интервью** | `mock-interviews/` / `real-interviews/` в `data/knowledgebase/raw/` и `data/knowledgebase/splitted/` | Постановочное vs запись реального собеседования |
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

Скрипт: `step4-validate-chapters/splitter_validate_video.py` (из `.claude/skills/splitter/step3-excel/splitter_post.sh`).

**Отчёт валидации:** `{basename}.vN.validation-report.md` — в начале секция **«Прогон пайплайна»** (длительности шагов, статусы) и ссылка на журнал. **Журнал прогона и промпты LLM:** `{basename}.vN.pipeline-log.md` (`PIPELINE_MANIFEST` + таблица Steps). Не создавать `*.summary.md`, `*.full.md`, отдельные `llm-input.txt` / `user-prompt.txt`.

**Содержимое файла (сверху вниз):**

1. Вердикт и метрики.
2. **Что проверяем** — правила (YouTube ↔ JSON, покрытие, тема, тайм-коды).
3. **Все главы YouTube** — таблица: статус, items **у маркера** (каждый item только в одной строке), Δt.
4. **Исключённые главы** — почему не вопрос; для «Разбор»/«Объяснение» — trace в `reference_answer` / `interviewer_feedback`.
5. **Подводки (🔗)** — в какой `interviewer_question` следующего (или предыдущего) item попал текст.
6. **Не распознанные (❌)** — гипотеза (пропуск / самоответ интервьюера / смещение) + транскрипт.
7. **Детали по вопросным главам** — полные Q/A только для items, привязанных к этой главе (±tolerance); без дубля по соседним главам.
8. **Фрагменты транскрипта без Q&A** — непокрытые куски `timecodes.txt`.
9. Комментарий и справочные таблицы.
10. **Шаг 5 (LLM)** — промпт в `pipeline-log.md`; ответ JSON в секции `Semantic validation` в конце **этого же** `validation-report.md`.

**Coverage** = доля вопросных глав (без подводок 🔗) с ≥1 item в **±tolerance** от маркера главы. Сдвиг тайм-кода (YouTube `00:30:57`, сплиттер `00:30:44`) — **не ошибка**, если item есть и Δt в допуске.

Подводки (`Подводка к…`) — статус 🔗, не отдельный вопрос; текст должен входить в следующий `interviewer_question` (промпт шага 2).

| Статус | Значение |
|--------|----------|
| ❌ не распознан | нет item в ±tolerance от маркера главы |
| ✅ один / несколько Q&A | есть item(s); полные тексты в том же `.md` |
| 🔗 подводка | не отдельный вопрос |
| — исключено | вступление, разбор, конец |

### LLM-валидация (шаг 5)

**Как шаг 2:** LLM вызывает **агент в Cursor** (модель из подписки / `run_config.json`), не скрипт в терминале.  
`splitter_post.sh` только готовит промпт (`--prepare-llm` → `LLM_INPUT_STEP_5` в `pipeline-log.md`).

1. Вход — секция `LLM_INPUT_STEP_5` в `*.pipeline-log.md`.
2. Агент возвращает JSON → `save_semantic_json_to_report` / блок `<!-- SEMANTIC_VALIDATION -->` в `validation-report.md`.
3. Повторный запуск `splitter_validate_video.py` (те же `--splitter --video --out`) подмешивает строки шага 5 в детали по главам.

Шаг 5 **обязателен** в полном прогоне `/splitter` в Cursor (сразу после `splitter_post.sh`, в том же чате).

Поля LLM на главу: `time_alignment_ok`, `content_alignment_ok`, `notes`.

**Критерии шага 5 (допуск 120 сек, строже шага 4 не нужно):**

- `time_alignment_ok = true`: есть item в этом или соседнем окне с тайм-кодом в пределах **60 сек** от маркера главы — и содержание совпадает. Сдвиг в единицы или десятки секунд — **не ошибка**; шаг 4 использует жёсткие границы окон, шаг 5 — семантику и допуск.
- `content_alignment_ok = true`: содержание главы покрыто — item в этом или соседнем окне в пределах 60 сек по теме.
- Если chapter `not_recognized` (0 items в окне): **сначала проверить последний item предыдущей главы**. Если его тайм-код < 60 сек до маркера текущей главы и тема совпадает → оба флага `true`, `notes: ""`. False только при реально пропущенном вопросе или сегменте-обсуждении без своего Q&A.
- `notes` оставлять `""` когда оба флага `true` — мелкие технические детали (дрейф в секунды) в notes не нужны.

### Входы LLM в `pipeline-log.md`

Секции `<!-- LLM_INPUT_STEP_N -->` заполняют скрипты:

| Шаг | Кто пишет | Содержимое |
|-----|-----------|------------|
| 2 | `splitter_prepare_prompt.py` | system + user + schema + транскрипт + RUNTIME_HINTS |
| 5 | `splitter_validate_video.py --prepare-llm` | payload для семантической проверки глав |

На шаге 2 модель читает **только** блок `LLM_INPUT_STEP_2` (не `video.md`, не другие интервью).

---

## Пайплайн (пять шагов)

| # | Название | Папка / скрипт | LLM? | Вход → выход |
|---|----------|----------------|------|----------------|
| 1 | **Подготовка** | `step1-prepare/splitter_prepare_prompt.py` | Нет | Папка → `pipeline-log` (секция step 2) |
| 2 | **Извлечение Q&A** | `step2-extract-qa/` (агент) | Да | `pipeline-log` step 2 → `*.vN.qa-split.json` |
| 3 | **Excel** | `step3-excel/splitter_json_to_excel.py` | Нет | `json` → `*.vN.qa-split.xlsx` |
| 4 | **Валидация по главам** | `step4-validate-chapters/splitter_validate_video.py` | Нет | `json` + `video.md` → `*.vN.validation-report.md` |
| 5 | **LLM-валидация** | `step5-validate-llm/` (агент) | Да | `pipeline-log` step 5 → JSON в `validation-report.md` → строки в report |

Шаги **3–4** одной командой: `.claude/skills/splitter/step3-excel/splitter_post.sh <json> --video <папка>/video.md` (Excel, validate, промпт шага 5).  
Шаг **5** — агент в том же чате после `splitter_post.sh` (как шаг 2 после prepare).

Без `video.md`: только шаги 1–3 (`splitter_mode: split_only`).

Повторный прогон с исправленным промптом: снова шаги **1–5** с версией **`vN+1`** (новые четыре файла на версию; старый `vN` не перезаписывать).

### Критерий «валидация пройдена» (шаг 4)

В `{basename}.vN.validation-report.md` строка **`### Вердикт:`** должна содержать **`✅ ПРОЙДЕНО`**.

Проверка в терминале (для агента):

```bash
python3 .claude/skills/splitter/step4-validate-chapters/splitter_verdict.py \
  data/knowledgebase/splitted/.../data-scientist-junior-karpov-2022-03-30.v9.validation-report.md \
  --json data/knowledgebase/splitted/.../data-scientist-junior-karpov-2022-03-30.v9.qa-split.json
echo $?   # 0 = пройдено, 1 = не пройдено / prior leak, 2 = частично
```

Шаг 5 (семантика LLM) **не меняет** этот вердикт — только колонку «Смысл (5)» и «Проверка 3». Цикл исправления смотрит на вердикт **после** шагов 4–5.

Дополнительный триггер: в таблице глав есть статус **❌ не распознан** — даже при «ЧАСТИЧНО» нужен исправляющий цикл.

### Цикл исправления (обязателен для агента)

**Когда:** после шага 5 (или после шага 4, если шаг 5 пропущен нет `video.md` — тогда критерий только шаг 4), если:

- `splitter_verdict.py` → exit **1** или **2**, **или**
- в отчёте есть **❌ не распознан**.

**Не писать «Готово»**, пока вердикт не **✅ ПРОЙДЕНО** (exit 0), если пользователь не попросил остановиться раньше.

| Попытка | Версия | Действие |
|---------|--------|----------|
| 1 | `vN` | Первый полный прогон шагов 1–5 |
| 2 | `vN+1` | Исправление + повтор 1–5 |
| 3 | `vN+2` | Второе исправление + повтор 1–5 |
| — | — | После **2** неудачных исправлений — эскалация пользователю с кратким разбором |

#### Шаг R — диагностика (прочитать отчёт)

Файл: **`data/knowledgebase/splitted/.../{basename}.vN.validation-report.md`**. Журнал: **`{basename}.vN.pipeline-log.md`**.

1. **`### Вердикт:`** — что не сошлось (Coverage / Topic / JSON / нераспознанные главы).
2. Таблица **«Все главы YouTube»** — строки **❌ не распознан**, **несколько Q&A**.
3. Секции **«Не распознанные»**, **«Фрагменты транскрипта без Q&A»**, **«Проверка 1»** (JSON Schema).
4. **«Проверка 3»** — замечания LLM по главам (не блокируют вердикт, но подсказывают правки промпта шага 2).

Кратко сообщить пользователю: 2–5 пунктов «что сломано» + гипотеза.

#### Шаг R — что править

| Симптом | Куда править | Повтор |
|---------|--------------|--------|
| Пропуск вопроса, плохая нарезка Q&A, подводки не в том item | `.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt` | шаги **1–5**, новая `vN+1` (шаг 2 заново, без копирования старого JSON) |
| Речь кандидата в `interviewer_feedback` | тот же `splitter_system_prompt.txt` (§ feedback) | шаги **1–5**, новая `vN+1` |
| Неверный `question_topic` / тип | тот же промпт или `section_topic_map.*.json` (шаг 4) | 1–5 или только 3–4 |
| Ложная «служебная» глава на YouTube | `EXPLANATION_PREFIXES` в `step4-validate-chapters/splitter_validate_video.py` | шаги **3–5** на том же json |
| Ошибка в `video.md` / тайм-кодах YouTube | `data/knowledgebase/raw/.../video.md` | шаги **3–5** |
| Только семантика (шаг 5) | пересмотреть ответ LLM / транскрипт; при системной ошибке — `step5-validate-llm/validation_llm_system_prompt.txt` | шаг **5** + перезапуск валидатора |

**Не перезаписывать** `{basename}.vN.qa-split.json` — только новая версия **`vN+1`** через шаг 1 (`splitter_prepare_prompt.py` сам поднимет версию).

#### Шаг R — повтор

1. Внести правки в репозиторий (промпт / skill / валидатор / `video.md`).
2. `splitter_prepare_prompt.py --folder "$FOLDER"` → новый `vN+1`, новый `pipeline-log.md`.
3. Шаги 2 → `splitter_post.sh` → 5, как в первом прогоне.
4. Снова `splitter_verdict.py` на новый `validation-report.md`.

Зафиксировать в чате: **«Цикл исправления k/2»**, какие файлы менялись.

### Шаг 1 — Подготовка

```bash
python3 .claude/skills/splitter/step1-prepare/splitter_prepare_prompt.py \
  --folder data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30
```

Скрипт не вызывает API. В терминале — пути к `pipeline-log.md`, будущему `json` и команде `splitter_post.sh`.

### Шаг 2 — Извлечение Q&A

- Прочитать секцию `LLM_INPUT_STEP_2` в `*.vN.pipeline-log.md` (**только** этот блок для текущей `vN`).
- Модель: **`inference.model`** из `run_config.json` (см. RUNTIME_HINTS в файле).
- Не подмешивать `video.md` и другие интервью.
- **Запрещено:** читать/копировать `*.v(N-1).qa-split.json` или любой старый qa-split (см. «Каждый прогон с нуля»).
- Извлечь Q&A **заново** из `PRIMARY_TRANSCRIPT`; проверить, что `interviewer_feedback` не содержит речь кандидата.
- Ответ: **только JSON**, без markdown-обёртки; temperature 0.
- Сохранить в путь `.json` из промпта (блок step 2) — **полная перезапись** файла (шаг 1 уже создал пустой stub).
- Сразу после сохранения — **`splitter_check_prior_leak.py`** на этот JSON; при exit **1** пересобрать из транскрипта, не копировать v(N-1).

### Шаг 3 — Excel

```bash
python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py \
  data/knowledgebase/splitted/.../data-scientist-junior-karpov-2022-03-30.vN.qa-split.json \
  --out data/knowledgebase/splitted/.../data-scientist-junior-karpov-2022-03-30.vN.qa-split.xlsx
```

Или вместе со шагом 4 через `.claude/skills/splitter/step3-excel/splitter_post.sh`.

### Шаг 4 — Валидация по главам

```bash
python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
  --splitter data/knowledgebase/splitted/.../data-scientist-junior-karpov-2022-03-30.vN.qa-split.json \
  --video data/knowledgebase/raw/.../video.md \
  --out data/knowledgebase/splitted/.../data-scientist-junior-karpov-2022-03-30.vN.validation-report.md \
  --prepare-llm
```

Обычно вызывается из `splitter_post.sh` (там же `--prepare-llm`).

### Шаг 5 — LLM-валидация (агент, как шаг 2)

- Прочитать `LLM_INPUT_STEP_5` в `*.vN.pipeline-log.md` (после `splitter_post.sh`).
- Модель: **`validation_inference.model`** из `run_config.json` (агент Cursor, как шаг 2).
- Ответ: JSON по `step5-validate-llm/validation_llm_output_schema.json` → `validation-report.md` (`<!-- SEMANTIC_VALIDATION -->`).
- Перезапуск: `splitter_validate_video.py` с теми же `--splitter --video --out`.

---

## Git — ЗАПРЕТ без согласования (обязательно)

> **Агент НЕ ДЕЛАЕТ `git add`, `git commit`, `git stash`, `git pull`, `git push` без явного разрешения пользователя.**

Правило действует на протяжении всего прогона splitter (шаги 1–5, цикл исправления, «Готово»).

После завершения прогона агент **спрашивает**:

```text
Закоммитить и запушить артефакты v{N}? (да / нет)
```

И ждёт ответа. Если пользователь не ответил — не коммитить. Если ответил «да» — выполнить. **Не интерпретировать молчание или «окей» как согласие на git-операции.**

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
□ Шаг 5 — LLM-валидация (агент, как шаг 2)               [если есть video.md]
□ Цикл исправления — до ✅ ПРОЙДЕНО (макс. 2 ретрая)     [если есть video.md]
```

Шаги 4–5 и цикл исправления помечать «пропуск», если нет `video.md`. Шаг 5 обязателен в полном прогоне: после `splitter_post.sh` агент читает `LLM_INPUT_STEP_5`.

### Перед каждым шагом

Коротко объявить **текущий шаг**:

```text
▶ Шаг 2/4 — Извлечение Q&A (LLM)
Читаю: data/knowledgebase/splitted/.../....v6.pipeline-log.md (LLM_INPUT_STEP_2)
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

`splitter_post.sh` — шаги 3–4 + промпт для шага 5. Затем агент **обязан** выполнить «▶ Шаг 5/5» (LLM в том же чате).

### После каждого шага

1–2 строки итога: что создано (путь, версия `vN`), ошибка или ок. Обновлять **`{basename}.vN.pipeline-log.md`** (шаги 2 и 5 — через `splitter_run_log.py`).

```text
✓ Шаг 1 готов — pipeline-log: .../....v6.pipeline-log.md, json: ...v6.qa-split.json
```

**Лог шагов (агент):**
```bash
python3 .claude/skills/splitter/step1-prepare/splitter_run_log.py \
  --pipeline-log data/knowledgebase/splitted/.../....vN.pipeline-log.md \
  --step 2 --name qa_extraction --llm --model claude-sonnet-4-6 \
  --input ...vN.pipeline-log.md#LLM_INPUT_STEP_2 --output ...vN.qa-split.json --duration-sec 120
```
Шаги 3–4 пишет `.claude/skills/splitter/step3-excel/splitter_post.sh` автоматически.

### В конце

Писать **«Готово»** только если:

- нет `video.md` — после шага 3, **или**
- есть `video.md` — шаг 5 выполнен **и** `splitter_verdict.py` → exit **0** (✅ ПРОЙДЕНО), **или**
- пользователь явно попросил остановиться / исчерпаны 2 цикла исправления (тогда указать причину).

1. Время окончания и **длительность** (минуты и секунды, от старта до финала).
2. Итоговый отчёт (пути, число items, вердикт validation, число циклов исправления).

```text
Готово
──────
Старт:  2026-05-20 14:32
Финиш:  2026-05-20 15:12
Время:  40 мин

FOLDER: data/knowledgebase/raw/.../data-scientist-junior-karpov-2022-03-30
Версия: v10 | items: 36 | циклы исправления: 1
Вердикт: ✅ ПРОЙДЕНО
Артефакты: ...v10.qa-split.json, ...v10.qa-split.xlsx,
           ...v10.validation-report.md, ...v10.pipeline-log.md
...
```

Не пропускать объявления шагов, даже если шаг выполняется быстро.

---

## Запуск в Cursor (агент)

Один чат = одно интервью. Скопируй блок ниже в **новый чат** (Agent mode), подставь путь к папке.

### Промпт для агента (скопировать целиком)

```text
Запусти полный splitter pipeline для одного интервью.

FOLDER=data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30

Обязательно следуй .claude/skills/splitter/SKILL.md целиком:
«Протокол для пользователя», «Цикл исправления», «Запуск в Cursor».

Перед стартом — зафиксируй время, выведи план шагов (□), затем выполняй с объявлением «▶ Шаг N/…» до и «✓» после каждого шага.

Шаг 0 — проверка:
1) FOLDER существует; файлы: timecodes.txt или transcript.txt; video.md (если полная валидация).
2) mock-interviews или real-interviews; basename = имя листовой папки.

Функция run_pipeline (выполни 1–5 для текущей версии vN):
1. Подготовка (без LLM):
   python3 .claude/skills/splitter/step1-prepare/splitter_prepare_prompt.py --folder "$FOLDER"
   Запомни: {basename}.vN.pipeline-log.md, {basename}.vN.qa-split.json, команду splitter_post.sh.

2. Извлечение Q&A (LLM):
   - Только LLM_INPUT_STEP_2 в *.vN.pipeline-log.md (не video.md).
   - ЗАПРЕЩЕНО: открывать/копировать {basename}.v(N-1).qa-split.json или любой старый qa-split.
   - Обязательно: полное извлечение из PRIMARY_TRANSCRIPT; interviewer_feedback — только речь интервьюера (иначе null).
   - Ответ: один JSON, temperature 0 → {basename}.vN.qa-split.json (перезапись целиком)
   - splitter_run_log.py --step 2 …

3–4. Если есть video.md:
   .claude/skills/splitter/step3-excel/splitter_post.sh data/knowledgebase/splitted/.../{basename}.vN.qa-split.json --video "$FOLDER/video.md"
   → {basename}.vN.qa-split.xlsx, {basename}.vN.validation-report.md

5. Если есть video.md (ОБЯЗАТЕЛЬНО):
   - LLM_INPUT_STEP_5 в *.vN.pipeline-log.md → JSON по validation_llm_output_schema.json
   - Вставить в {basename}.vN.validation-report.md: <!-- SEMANTIC_VALIDATION --> … <!-- /SEMANTIC_VALIDATION -->
     (или: python3 -c "… save_semantic_json_to_report …" из splitter_validate_chapters)
   - Перезапуск splitter_validate_video.py (--splitter, --video, --out на тот же validation-report.md)
   - splitter_run_log.py --step 5 …

Цикл исправления (если есть video.md) — после шага 5:
   python3 .claude/skills/splitter/step4-validate-chapters/splitter_verdict.py \
     data/knowledgebase/splitted/.../{basename}.vN.validation-report.md \
     --json data/knowledgebase/splitted/.../{basename}.vN.qa-split.json
   - exit 0 → можно «Готово» (в т.ч. leak check пройден)
   - exit 1 или 2, или в отчёте есть «❌ не распознан»:
     a) Прочитай validation-report.md: ### Вердикт, нераспознанные главы, Проверка 1–3
     b) Кратко объясни пользователю причину
     c) Правь: splitter_system_prompt.txt / EXPLANATION_PREFIXES / video.md / section_topic_map (см. SKILL)
     d) «Цикл исправления 1/2» или 2/2 → снова run_pipeline (новая vN+1, не перезаписывать старый json)
   - После 2 неудачных циклов — «Готово» с ⚠️ и эскалацией

Без video.md: только шаги 1–3, splitter_mode split_only, цикл исправления не нужен.

«Готово» — только при ✅ ПРОЙДЕНО (или без video.md после шага 3):
- старт, финиш, длительность
- FOLDER, финальная vN, items, число циклов исправления
- 4 файла: *.vN.qa-split.json, *.vN.qa-split.xlsx, *.vN.validation-report.md, *.vN.pipeline-log.md
- вердикт; 2–3 проблемных главы, если были
```

### Пример для теста (Karpov junior DS)

| | Путь |
|---|------|
| Вход | `data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/` |
| Выход | `data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/` |

В папке входа должны быть `timecodes.txt` и `video.md`. Следующий прогон создаст следующий `vN` (см. уже существующие `*.vN.*` в `data/knowledgebase/splitted/.../`).

### Custom Agent в Cursor (опционально)

**Cursor Settings → Agents → New Agent**

- **Name:** `Splitter pipeline`
- **Instructions:** текст из промпта выше + «всегда читай `.claude/skills/splitter/SKILL.md`; соблюдай протокол шагов, цикл исправления до ✅ ПРОЙДЕНО, время для пользователя».

Запуск: новый чат → Agent mode → skill **`/splitter`** или агент **Splitter pipeline** → `FOLDER=data/knowledgebase/raw/...`.

### Что смотреть после прогона

На одну версию **`vN`** — ровно **4 файла** (см. `data/knowledgebase/splitted/README.md`):

1. **`{basename}.vN.qa-split.json`** — главный результат.
2. **`{basename}.vN.qa-split.xlsx`** — то же для глаз.
3. **`{basename}.vN.validation-report.md`** — вердикт, таблица глав, проверки 1–3; JSON шага 5 в `<!-- SEMANTIC_VALIDATION -->`.
4. **`{basename}.vN.pipeline-log.md`** — журнал прогона, `LLM_INPUT_STEP_2` / `_5`.

---

## Запуск в Claude Code

Тот же SKILL.md — единственный источник процедуры для Cursor и Claude Code.

| Способ | Действие |
|--------|----------|
| Skill | `/splitter` и путь к папке интервью (или `FOLDER=…` в сообщении) |
| Явно | «Выполни `.claude/skills/splitter/SKILL.md` для `data/knowledgebase/raw/.../basename`» |

Агент обязан:

1. Соблюдать **протокол шагов** (□ / ▶ / ✓) и **модели** из `run_config.json`.
2. **Шаг 2 с нуля** — не наследовать `*.v(N-1).qa-split.json`; только `PRIMARY_TRANSCRIPT` из `LLM_INPUT_STEP_2` текущей `vN` (раздел «Каждый прогон с нуля»).
3. Выполнить шаги **1–5**, если есть `video.md`.
4. Запустить **цикл исправления** до **✅ ПРОЙДЕНО** (`splitter_verdict.py` exit 0) или до **2** ретраев — как в разделе «Цикл исправления».

Промпт для Claude Code (эквивалент Cursor):

```text
/splitter

FOLDER=data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30

Полный pipeline по .claude/skills/splitter/SKILL.md:
шаги 0–5, цикл исправления до ✅ ПРОЙДЕНО (макс. 2 ретрая),
протокол времени и «Готово» только при exit 0 от splitter_verdict.py.
Шаг 2: полное извлечение из транскрипта; ЗАПРЕЩЕНО копировать прошлые v*.qa-split.json;
interviewer_feedback — только речь интервьюера (иначе null).
```

Скрипты — те же пути от корня репозитория (`python3 .claude/skills/splitter/...`, `.claude/skills/splitter/step3-excel/splitter_post.sh`).

---

## Cursor / Claude Code (сводка)

| Среда | Как запустить |
|-------|----------------|
| **Cursor** | Skill `/splitter` или промпт из «Запуск в Cursor» |
| **Claude Code** | `/splitter` + `FOLDER=…` или явная ссылка на SKILL.md |

Оба читают **один** `.claude/skills/splitter/SKILL.md`; отдельных Cursor Rules для splitter нет.
