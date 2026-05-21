# Отчёт валидации сплиттера


## Прогон пайплайна

- **Версия:** `v2` · **Интервью:** `transcripts/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24`
- **Режим:** `split_and_validate` · **source_id:** `system_design_senior_karpov_v3_2022_03_24`
- **Старт:** 2026-05-20 18:13:14 +0200 · **Обновлено:** 2026-05-20 18:19:32 +0200
- **Длительность прогона (стена):** 6 мин 18 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 4 мин 31 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ✅ все зафиксированные шаги завершены
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 2 | 2. Извлечение Q&A (LLM) | да | claude-sonnet-4-6 | 3 мин | ✅ |
| 3 | 3. Excel | нет | — | 1 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 0.00 с | ✅ |
| 5 | 5. Семантика глав (LLM) | да | claude-sonnet-4-6 | 1 мин 30 с | ✅ |

### Артефакты этого прогона

- **Разбивка Q&A (JSON):** `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.json`
- **Разбивка Q&A (Excel):** `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.xlsx`
- **Эталон для проверки:** `/Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/video.md` — описание YouTube с тайм-кодами и рубриками; сплиттер при извлечении Q&A этот файл **не видел**
- **Порог расхождения тайм-кодов:** ±90 с — максимальная разница между тайм-кодом вопроса на YouTube и временем `interviewer_question.time` в JSON, при которой пара Q&A всё ещё считается относящейся к этой главе

## Как устроена проверка

### Вердикт: ✅ ПРОЙДЕНО

Пайплайн — **5 шагов**. В этом файле — **проверки 1–3** (шаги 2, 4, 5). Шаги 1 и 3 только готовят данные.


| Шаг | Действие | Проверка в файле | Критерий | Статус | Результат | Цель |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Подготовка (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Проверка 1** | Валидный JSON по `splitter_output_schema.json` | ✅ | 12 items, JSON Schema OK | парсинг + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Сверка с `video.md` | **Проверка 2** | Сверка тайм-кодов YouTube с Q&A в JSON (рубрики в Description не заданы) | ✅ | Coverage 100% (11/11), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (агент) | **Проверка 3** | Смысл и тайм-коды полей vs заголовок главы и метки | ✅ | все 11 глав без замечаний | не блокирует вердикт |

---

## Проверка 1. Структура JSON (шаг 2 — выход сплиттера)

Детерминированная проверка файла после извлечения Q&A: парсинг и JSON Schema `splitter_output_schema.json`.


- **Файл:** `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 12
- **`source_id`:** `system_design_senior_karpov_v3_20220324`
- **`splitter_mode`:** `split_and_validate`


---

## Проверка 2. Сверка с тайм-кодами YouTube (шаг 4)


#### Термины (проверка 2)

- **Маркер** — тайм-код в `video.md` (строка в блоке Chapters): точка на шкале видео.

- **Вопросная глава** — маркер с реальным вопросом интервью; участвует в Coverage.

- **Служебная глава** — вступление, подводка (🔗), разбор задачи, пауза; в Coverage **не входит**, но в сводной таблице ниже указано, **куда ушла** речь в JSON.


#### Как считаем (проверка 2)

1. **Сопоставление по времени.** У каждого тайм-кода с вопросом на YouTube ищем пары Q&A в JSON, у которых время вопроса (`interviewer_question.time`) отличается от маркера не больше чем на **90 с** (в обе стороны). Одна пара Q&A относится только к одному ближайшему маркеру.


2. **Статус маркера.**
   - **распознан** — рядом с маркером есть «свои» Q&A;
   - **рядом** — своих нет, но в пределах порога есть Q&A у соседнего маркера (не считаем пропуском);
   - **не распознан** — в пределах порога нет ни одной пары (грубая ошибка);
   - **подводка / пропуск** — служебные главы, в метрики не входят.


3. **Coverage** — доля вопросных маркеров со статусом «распознан» или «рядом» (цель в сводке: ≥90%).


4. **Topic consistency** — у «своих» Q&A поле `question_topic` входит в список тем для секции интервью из Description `video.md` (цель: ≥90%). Тема в JSON может отличаться от заголовка главы YouTube — это нормально, если вопрос по смыслу из той же секции.


_Секции в Description не заданы — согласованность тем не считается._

### Все главы YouTube

Каждый тайм-код из `video.md`: вопросные — статус и Q&A; служебные — куда ушли в JSON. Развёрнутые тексты — ниже по вопросным главам.


| # | YT | Заголовок | Секция | Привязка (4) | Q&A | Темы | Смысл (5) | Куда в JSON |
|---|-----|-----------|--------|--------------|-----|------|-----------|-------------|
| — | `00:00` | Introduction and Interviewer's In… | — | пропуск | — | — | ⏳ | — |
| 1 | `01:37` | Problem Statement | — | распознан (1 Q&A) | #1 | `Product Metrics` | ⏳ | — |
| — | `02:50` | Problem Specifics: Beginning of t… | — | пропуск | — | — | ⏳ | — |
| 2 | `04:24` | Functional Requirements | — | распознан (1 Q&A) | #2 | `Communication` | ⏳ | — |
| 3 | `07:20` | Non-Functional Requirements | — | распознан (1 Q&A) | #3 | `Product Metrics` | ⏳ | — |
| 4 | `09:50` | Estimate (preliminary assessment … | — | распознан (1 Q&A) | #4 | `Product Metrics` | ⏳ | — |
| 5 | `14:17` | Information Storage Assessment | — | распознан (1 Q&A) | #5 | `Data Modeling` | ⏳ | — |
| 6 | `18:49` | GEO: How to Tell if a User and Dr… | — | распознан (1 Q&A) | #6 | `Data Modeling` | ⏳ | — |
| 7 | `25:22` | Quadtree Calculation for Moscow | — | распознан (1 Q&A) | #7 | `Data Modeling` | ⏳ | — |
| 8 | `29:35` | Description of Tree Search and It… | — | распознан (1 Q&A) | #8 | `Data Modeling` | ⏳ | — |
| 9 | `31:14` | Can Search Be Hashed? | — | распознан (1 Q&A) | #9 | `Data Modeling` | ⏳ | — |
| 10 | `33:13` | Can we quickly see the driver's c… | — | распознан (1 Q&A) | #10 | `Data Modeling` | ⏳ | — |
| — | `34:52` | Returning to the general structure | — | пропуск | — | — | ⏳ | — |
| 11 | `43:36` | Redundancy and availability | — | распознан (1 Q&A) | #12 | `Data Modeling` | ⏳ | — |
| — | `46:20` | Feedback | — | пропуск | — | — | ⏳ | — |

**Все извлечённые items (12)** — полный список из JSON:

| Item | Время вопроса | Окно главы YouTube | `question_topic` | Начало вопроса |
|------|---------------|--------------------|------------------|----------------|
| #1 | `01:37` | `01:37` Problem Statement | `Product Metrics` | Задача: спроектируй Uber-like сервис такси — где водитель и … |
| #2 | `04:24` | `04:24` Functional Requirements | `Communication` | Опиши функциональные требования для пешехода и водителя. |
| #3 | `07:20` | `07:20` Non-Functional Requirements | `Product Metrics` | Какие нефункциональные требования? |
| #4 | `09:50` | `09:50` Estimate (preliminary assessm… | `Product Metrics` | Сделай estimate: трафик, одновременные поездки, RPS. |
| #5 | `14:17` | `14:17` Information Storage Assessment | `Data Modeling` | Сколько места нужно для хранения профилей, поездок и данных … |
| #6 | `18:49` | `18:49` GEO: How to Tell if a User an… | `Data Modeling` | GEO: как понять, что пользователь и водитель рядом? |
| #7 | `25:22` | `25:22` Quadtree Calculation for Moscow | `Data Modeling` | Расчёт quadtree для Москвы — сколько уровней, сколько ячеек? |
| #8 | `29:35` | `29:35` Description of Tree Search an… | `Data Modeling` | Опиши поиск по дереву и его сложность. |
| #9 | `31:14` | `31:14` Can Search Be Hashed? | `Data Modeling` | Можно ли захэшировать поиск? |
| #10 | `33:13` | `33:13` Can we quickly see the driver… | `Data Modeling` | Можем ли быстро получить текущую позицию водителя? |
| #11 | `34:52` | `34:52` Returning to the general stru… | `Data Modeling` | Опиши общую архитектуру сервиса — полная схема компонентов. |
| #12 | `43:36` | `43:36` Redundancy and availability | `Data Modeling` | Redundancy и availability — как обеспечить отказоустойчивост… |

### Детали по вопросным главам

Развёрнутые тексты Q&A. Служебные главы — только в таблице «Все главы YouTube» выше.


### 1. `01:37` — Problem Statement

- **Проверка главы:** ✅ в окне главы 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Все Q&A в окне главы** (от маркера до следующей главы; без пропусков)

| Item | Δt | `question_topic` | Начало вопроса |
|------|-----|------------------|----------------|
| #1 | +0 с | `Product Metrics` | Задача: спроектируй Uber-like сервис такси — где водитель и пассажир, … |

#### Item #1

- **Вопрос** (`01:37`): Задача: спроектируй Uber-like сервис такси — где водитель и пассажир, поездки, глобально, ~500 млн пассажиров и ~5 млн водителей.
- **Ответ кандидата** (`02:50`): Главная особенность — локальный матчинг: искать водителя рядом с точкой вызова, а не глобально как в Twitter.
- **Reference answer:** —
- **Interviewer feedback:** —
- **Метки:** `Product Metrics` · type=hard · stage=system_design

### 2. `04:24` — Functional Requirements

- **Проверка главы:** ✅ в окне главы 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Все Q&A в окне главы** (от маркера до следующей главы; без пропусков)

| Item | Δt | `question_topic` | Начало вопроса |
|------|-----|------------------|----------------|
| #2 | +0 с | `Communication` | Опиши функциональные требования для пешехода и водителя. |

#### Item #2

- **Вопрос** (`04:24`): Опиши функциональные требования для пешехода и водителя.
- **Ответ кандидата** (`04:42`): Пешеход: указать адрес, найти водителя, поездка, профиль/оплата. Водитель: выйти на смену, принять/отклонить заказ, поездка, рейтинг, снова принять или завершить смену.
- **Reference answer:** —
- **Interviewer feedback:** —
- **Метки:** `Communication` · type=hard · stage=system_design

### 3. `07:20` — Non-Functional Requirements

- **Проверка главы:** ✅ в окне главы 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Все Q&A в окне главы** (от маркера до следующей главы; без пропусков)

| Item | Δt | `question_topic` | Начало вопроса |
|------|-----|------------------|----------------|
| #3 | +0 с | `Product Metrics` | Какие нефункциональные требования? |

#### Item #3

- **Вопрос** (`07:20`): Какие нефункциональные требования?
- **Ответ кандидата** (`07:29`): Низкая латентность поиска машины, высокая доступность, для водителя — заказы рядом, оптимальный маршрут/стоимость, прозрачность цены.
- **Reference answer:** —
- **Interviewer feedback:** —
- **Метки:** `Product Metrics` · type=hard · stage=system_design

### 4. `09:50` — Estimate (preliminary assessment in terms of space and durability)

- **Проверка главы:** ✅ в окне главы 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Все Q&A в окне главы** (от маркера до следующей главы; без пропусков)

| Item | Δt | `question_topic` | Начало вопроса |
|------|-----|------------------|----------------|
| #4 | +0 с | `Product Metrics` | Сделай estimate: трафик, одновременные поездки, RPS. |

#### Item #4

- **Вопрос** (`09:50`): Сделай estimate: трафик, одновременные поездки, RPS.
- **Ответ кандидата** (`12:48`): Порядка 1 млн поездок/день → ~10 RPS на инициацию; поездка ~1 ч → ~40k одновременных поездок; с учётом гео-поиска — сотни RPS на matching.
- **Reference answer:** —
- **Interviewer feedback** (`14:15`): Перейдём к оценке хранения информации.
- **Метки:** `Product Metrics` · type=hard · stage=system_design

### 5. `14:17` — Information Storage Assessment

- **Проверка главы:** ✅ в окне главы 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Все Q&A в окне главы** (от маркера до следующей главы; без пропусков)

| Item | Δt | `question_topic` | Начало вопроса |
|------|-----|------------------|----------------|
| #5 | +0 с | `Data Modeling` | Сколько места нужно для хранения профилей, поездок и данных сервиса? |

#### Item #5

- **Вопрос** (`14:17`): Сколько места нужно для хранения профилей, поездок и данных сервиса?
- **Ответ кандидата** (`16:02`): Отдельные сервисы: pedestrian, driver, matching/connection, trip history, payments; профили в БД, поездки в DWH/Kafka; гео-данные — отдельный location service.
- **Reference answer:** —
- **Interviewer feedback:** —
- **Метки:** `Data Modeling` · type=hard · stage=system_design

### 6. `18:49` — GEO: How to Tell if a User and Driver are Nearby

- **Проверка главы:** ✅ в окне главы 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Все Q&A в окне главы** (от маркера до следующей главы; без пропусков)

| Item | Δt | `question_topic` | Начало вопроса |
|------|-----|------------------|----------------|
| #6 | +0 с | `Data Modeling` | GEO: как понять, что пользователь и водитель рядом? |

#### Item #6

- **Вопрос** (`18:49`): GEO: как понять, что пользователь и водитель рядом?
- **Ответ кандидата** (`18:20`): Нужен geo backend: хранить координаты водителей, быстро искать ближайших к точке заказа; не реляционная БД — KV/гео-индекс.
- **Reference answer:** —
- **Interviewer feedback:** —
- **Метки:** `Data Modeling` · type=hard · stage=system_design

### 7. `25:22` — Quadtree Calculation for Moscow

- **Проверка главы:** ✅ в окне главы 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Все Q&A в окне главы** (от маркера до следующей главы; без пропусков)

| Item | Δt | `question_topic` | Начало вопроса |
|------|-----|------------------|----------------|
| #7 | +0 с | `Data Modeling` | Расчёт quadtree для Москвы — сколько уровней, сколько ячеек? |

#### Item #7

- **Вопрос** (`25:22`): Расчёт quadtree для Москвы — сколько уровней, сколько ячеек?
- **Ответ кандидата** (`25:22`): Делим карту на квадранты рекурсивно; для Москвы оцениваем глубину дерева и число листьев в зависимости от требуемой точности и числа водителей в ячейке.
- **Reference answer:** —
- **Interviewer feedback:** —
- **Метки:** `Data Modeling` · type=hard · stage=system_design

### 8. `29:35` — Description of Tree Search and Its Complexity

- **Проверка главы:** ✅ в окне главы 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Все Q&A в окне главы** (от маркера до следующей главы; без пропусков)

| Item | Δt | `question_topic` | Начало вопроса |
|------|-----|------------------|----------------|
| #8 | +0 с | `Data Modeling` | Опиши поиск по дереву и его сложность. |

#### Item #8

- **Вопрос** (`29:35`): Опиши поиск по дереву и его сложность.
- **Ответ кандидата** (`29:35`): Спуск по quadtree до нужной ячейки — O(log N) по глубине; в листе — список водителей; обновление позиции — пересчёт ячейки.
- **Reference answer:** —
- **Interviewer feedback:** —
- **Метки:** `Data Modeling` · type=hard · stage=system_design

### 9. `31:14` — Can Search Be Hashed?

- **Проверка главы:** ✅ в окне главы 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Все Q&A в окне главы** (от маркера до следующей главы; без пропусков)

| Item | Δt | `question_topic` | Начало вопроса |
|------|-----|------------------|----------------|
| #9 | +0 с | `Data Modeling` | Можно ли захэшировать поиск? |

#### Item #9

- **Вопрос** (`31:14`): Можно ли захэшировать поиск?
- **Ответ кандидата** (`31:14`): Хэш по координатам не заменяет гео-поиск — нужна структура по близости; кэшировать можно результаты запроса в hot-зонах.
- **Reference answer:** —
- **Interviewer feedback:** —
- **Метки:** `Data Modeling` · type=hard · stage=system_design

### 10. `33:13` — Can we quickly see the driver's current position?

- **Проверка главы:** ✅ в окне главы 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Все Q&A в окне главы** (от маркера до следующей главы; без пропусков)

| Item | Δt | `question_topic` | Начало вопроса |
|------|-----|------------------|----------------|
| #10 | +0 с | `Data Modeling` | Можем ли быстро получить текущую позицию водителя? |

#### Item #10

- **Вопрос** (`33:13`): Можем ли быстро получить текущую позицию водителя?
- **Ответ кандидата** (`33:13`): Да — частые обновления GPS в location service, in-memory индекс или quadtree с TTL; read по driver_id или по гео-запросу.
- **Reference answer:** —
- **Interviewer feedback:** —
- **Метки:** `Data Modeling` · type=hard · stage=system_design

### 11. `43:36` — Redundancy and availability

- **Проверка главы:** ✅ в окне главы 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Все Q&A в окне главы** (от маркера до следующей главы; без пропусков)

| Item | Δt | `question_topic` | Начало вопроса |
|------|-----|------------------|----------------|
| #12 | +0 с | `Data Modeling` | Redundancy и availability — как обеспечить отказоустойчивость? |

#### Item #12

- **Вопрос** (`43:36`): Redundancy и availability — как обеспечить отказоустойчивость?
- **Ответ кандидата** (`43:36`): Репликация geo и stateful сервисов, несколько AZ, health checks, graceful degradation при падении matching; Kafka для асинхронных side-effects.
- **Reference answer:** —
- **Interviewer feedback:** —
- **Метки:** `Data Modeling` · type=hard · stage=system_design


## Проверка 3. Смысл и тайм-коды полей внутри глав (шаг 5, LLM)

Модель в Cursor (как на шаге 2) проверяет **уже извлечённые** Q&A: правдоподобны ли тайм-коды полей в окне главы и совпадают ли тексты с заголовком главы и метками (`question_topic`, `question_type`). На общий вердикт не влияет.


- **Статус:** ✅ все 11 глав без замечаний
- **Тайм-коды полей:** 11/11 ок · **Смысл/метки:** 11/11 ок


## Фрагменты транскрипта без Q&A в JSON

Интервалы `timecodes.txt`, не попавшие в span ни одного item сплиттера (от `interviewer_question.time` до конца ответа / reference / feedback / следующего вопроса). Проверьте, не пропущен ли вопрос или это служебная речь.

_Крупных непокрытых фрагментов не найдено (порог: ≥25 с, ≥4 строк с тайм-кодом)._

<!-- SEMANTIC_VALIDATION -->

## Semantic validation (step 5)

Машинный ответ LLM (шаг 5). Валидатор читает этот блок при повторном прогоне.

```json
{
  "chapters": [
    {
      "chapter_time": "00:01:37",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:04:24",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:07:20",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:09:50",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:14:17",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:18:49",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:25:22",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:29:35",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:31:14",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:33:13",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:43:36",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
