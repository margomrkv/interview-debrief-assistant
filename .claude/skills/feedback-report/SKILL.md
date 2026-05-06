---
name: feedback-report
description: Генерирует per-question feedback по папке прошедшего интервью. Реализует требование md/spec.md §7 E3-4 «Отчёт по интервью» (Market Flow scope; упрощённая MVP-версия после ревизии 06-05). Два режима — blind (default, без feedback.txt; независимая оценка модели + HIRE/NO_HIRE verdict) и with-feedback (читает feedback.txt и добавляет секцию Interviewer's signal, без verdict'а). Принимает path и опциональный флаг mode=<blind|with-feedback>; пишет в <folder>/feedback-report.<mode>.md.
---

# Skill: Feedback report по интервью

## Версия 

Текущая версия 1.1. Включай версию в отчет. 

## Назначение

Один прогон = одна папка интервью → один markdown-отчёт `feedback-report.<mode>.md` в той же папке.

Два режима работы:

- **`blind` (default).** Независимая оценка только по транскрипту, JD и CV. `feedback.txt` НЕ ЧИТАЕТСЯ ни на одном шаге. Назначение — слепое мнение модели; результат можно сравнить с реальным фидбеком интервьюера как сигнал качества системы (LLM-as-judge baseline). **Включает verdict HIRE / NO_HIRE.**
- **`with-feedback`.** Все четыре файла, плюс секция `### Interviewer's signal`. Назначение — глубокий post-mortem с учётом перспективы интервьюера. Минус: spoiler-эффект, модель может подгонять оценки под ожидания feedback. **Verdict не выводится** — иначе рискует отражать verdict интервьюера, а не независимое суждение модели; точка независимого решения — это blind-режим.

Содержимое отчёта (упрощено по ревизии 06-05; расширения — `Recommendation[]`, `AssessmentTopic[]`, `P(HIRE)`, JD aligned/partial/missing rollup — postponed, см. `md/requirements_postponed.md` §5):

1. Summary table (быстрый sniff-test).
2. **Verdict** (HIRE / NO_HIRE) — только в `blind`.
3. Per-question `AssessmentItem[]` по схеме `md/spec.md` §3 (исторический первоисточник — `internal-notes/2026-04-30-martin-meeting.md`).
4. В `with-feedback`: секция `### Interviewer's signal` с разбором утверждений из `feedback.txt`.

Не батчует, не использует knowledge base / karpov-корпус, не сравнивает с другими интервью кандидата.

## Соответствие spec.md

Скилл реализует следующие требования (Market Flow scope; MVP после ревизии 06-05 «попроще»):

- **E1-4 «Транскрипт раунда»** (`md/spec.md` §7) — структура папки кейса, привязка к раунду.
- **E1-5 «Фидбэк раунда»** (`md/spec.md` §7) — режимы blind / with-feedback, разбор отличается с feedback vs без.
- **E3-4 «Отчёт по интервью»** (`md/spec.md` §7, ядро MVP) — markdown-render `AssessmentItem[]` (per-question оценка) + `AlignmentReport.verdict ∈ {HIRE, NO_HIRE}` в blind. Цитаты для сильных и слабых мест, формулировка проблемы (vague / off-topic / factual_error / incomplete) в `AssessmentItem.comment`.
- **§3 «Артефакты»** — `QA`, `AssessmentItem`, минимальный `AlignmentReport` (verdict + items), `LinkedText`.
- **§3.1 «Матрица заполненности»** — поведение при отсутствии CV/JD/feedback.
- **`md/assessors.md`** — критерии (`clarity` / `completeness` / `factual_correctness` / `question_fit` / `focus`; behavioral расширения STAR + Amazon SPID) для `AssessmentItem.score`.

Не реализуется в этом скилле (postponed, см. `md/requirements_postponed.md` §5):

- **E3-5 «Структура рекомендаций»**, **E3-6 «Topic rollup»**, **E3-7 «Структурированный отчёт»** — требуют артефактов `Recommendation`, `AssessmentTopic` и расширенного `AlignmentReport` (с `topic_assessments` / `recommendations` / `strengths_summary` / `gaps_summary` / `P(HIRE)`).
- JD aligned/partial/missing rollup относительно `Requirements` — часть Advanced `AlignmentReport`.

Расхождения, оставленные сознательно (фиксируются для последующего обновления spec):

- `md/spec.md` §8 + E3-4 требуют behavioral disclaimer «оценка категории behavioral в текущей версии не выполнена». Скилл оценивает behavioral наравне с hard_skill / soft_skill. Spec выправляется отдельно.

Не реализуется (вне Market Flow / отложено):

- E2 (Knowledge Base): `Requirements` / `Rubric` / `EvalDataset` не подключаются.
- E2-6 «Контроль качества» — отдельный изолированный pipeline (`md/spec.md` §7), не часть feedback-report.
- `MemoryState`, сравнение с другими интервью кандидата (`md/spec.md` §8).

## Вход

**Обязательный аргумент:** путь к папке интервью.

**Опциональный флаг** `mode=<blind|with-feedback>`. По умолчанию — `blind`.

- Если `args` пуст → использовать default путь `[private]/avito-20251212` и режим `blind`.
- Если default путь неприменим (директория не существует) → спросить через AskUserQuestion с вариантами из списка `[private]/*`.
- Если `mode` передан с другим значением → ошибка, перечислить разрешённые.

Папка должна содержать минимум `transcript.txt`. Остальные файлы опциональны (см. defensive fallback в Алгоритме). Для режима `with-feedback` отсутствие `feedback.txt` → fallback в `blind` с явным предупреждением.

## Конфигурация

- **Рабочий каталог:** корень репо (`git rev-parse --show-toplevel`).
- **Входные файлы (relative to папки интервью):**
  - `cv.md` — CV кандидата.
  - `vacancy.txt` — JD вакансии.
  - `transcript.txt` — диалог с timestamp'ами и speaker labels.
  - `feedback.txt` — заметки интервьюера. **Только в режиме `with-feedback`. В blind НЕ читать.**
- **Schema референс:**
  - `QA`, `AssessmentItem`, `LinkedText` — `md/spec.md` §3 (актуальный авторитетный источник; `internal-notes/2026-04-30-martin-meeting.md` — исторический первоисточник схемы).
  - Критерии оценки (`Score`) — `md/assessors.md`.
- **Rollup референс:** минимальный `AlignmentReport` (`{verdict, items}`) — `md/spec.md` §3 / §4.1; E3-4 (`md/spec.md` §7).
- **Output:**
  - blind → `<folder>/feedback-report.blind.md`
  - with-feedback → `<folder>/feedback-report.with-feedback.md`
  - При коллизии — `feedback-report.<mode>.v2.md`, `.v3.md` и т.д.

## Алгоритм

### Шаг 0: Парсинг входа

1. Выделить позиционный аргумент — путь к папке.
2. Распарсить `mode=<value>` если есть. Допустимые: `blind`, `with-feedback`. Default: `blind`.
3. Зафиксировать `MODE` для остального алгоритма.

### Шаг 1: Валидация входа и наличие файлов

Поведение при разной заполненности матрицы артефактов — `md/spec.md` §3.1; ожидание прикреплённого транскрипта — E1-4, опциональность фидбэка — E1-5 (`md/spec.md` §7).

1. Проверить, что папка существует. Если нет — остановиться с ошибкой.
2. Перечислить наличные файлы из `{cv.md, vacancy.txt, transcript.txt}`. Для `with-feedback` — также `feedback.txt`.
3. Если `transcript.txt` отсутствует → остановиться: «без транскрипта анализ невозможен» (E1-4: транскрипт обязателен — это вход в систему).
4. Если `vacancy.txt` отсутствует → rollup делается на общих industry expectations (lead DS-роль); секция `## Rollup` помечается ярлыком `(no JD; fallback to industry baseline)` (`md/spec.md` §3.1, кейс mock-Карпова).
5. Если `cv.md` отсутствует → ожидаемые ответы строятся только из JD без персонификации.
6. **Mode-specific:**
   - `blind`: НЕ открывать `feedback.txt`, даже если он есть. Не упоминать его в отчёте.
   - `with-feedback`: если `feedback.txt` отсутствует → авто-fallback в `blind` с предупреждением пользователю; имя файла остаётся `feedback-report.with-feedback.md`? Нет — переключаем на `feedback-report.blind.md`. Так пользователь видит, что отчёт фактически слепой.

### Шаг 2: Чтение и transcript reading rules

Прочитать `transcript.txt` целиком (для avito-20251212 ~158 KB / ~980 строк — помещается в один контекст). Для `with-feedback` — также прочитать `feedback.txt` (короткий, обычно 5-15 строк).

**Правила интерпретации спикеров (dual-track ASR):**

- Спикеры `Microphone` обычно = **кандидат**.
- Спикеры `Eugene Avito` / `Speaker 2` / `Speaker 3` / любой именованный = **интервьюер**.
- Dual-track ASR: один и тот же текст появляется дважды с лагом 1-2 сек (микрофон ловит интервьюера через колонки, и наоборот). Echo dedup:
  - если соседние блоки разных спикеров в окне ≤30 сек содержат ≥85% общего текста — это эхо;
  - оставлять версию того, кто реально это сказал, исходя из **содержания** (например, фраза «можешь рассказать о себе» — это интервьюер, даже если попала под `Microphone`).
- Backchannels («ага», «угу», «понятно, спасибо») — НЕ вопросы.
- Meta-турны («давай переходить к кейсу», «у нас 60-70 минут») — НЕ вопросы.
- Парафраз кандидатом вопроса интервьюера — это эхо, не самостоятельный ход.

### Шаг 3: Q&A extraction

1. Идти по транскрипту сверху вниз в порядке времени.
2. **Question boundary** = substantive interviewer turn (после фильтра шага 2).
3. **Candidate answer** = конкатенация всех `Microphone`-турнов от текущей question boundary до следующей (исключая эхо).
4. Короткие uplift-реплики интервьюера внутри ответа («ага, понял», «дай уточню») — не граница, ответ продолжается.
5. Длинные ответы → `transcript_time` хранится как диапазон `00:44 → 04:19`.
6. Прицеливаться на 10–20 substantive Q&A пар для интервью ~90 минут. <8 или >25 — пересмотреть фильтрацию.

### Шаг 4: Per-question Assessment Item

Поля `AssessmentItem` — по `md/spec.md` §3 (актуальный авторитетный источник; `internal-notes/2026-04-30-martin-meeting.md` — исторический первоисточник схемы).

Для каждой Q&A пары:

- **question: LinkedText** — `{text: <verbatim цитата интервьюера>, transcript_time: "MM:SS"}`. Допустимо `…` в середине, endpoints точные.
- **candidate_answer: LinkedText** — `{text: <verbatim, можно сжать через `…`>, transcript_time: "MM:SS → MM:SS"}` (диапазон).
- **expected_answer** — что хороший кандидат под этот JD и уровень сказал бы. Привязка к bullets JD; учёт CV, если есть.
- **type** — ровно одно из (`md/spec.md` §3):
  - `hard_skill` — ML/DS техника: метрики, калибровка, обучающие данные, sample bias, эксплуатация моделей, system design.
  - `soft_skill` — стиль коммуникации, clarification questions, structuring of reasoning.
  - `behavioral` — STAR-вопросы, управление командой, career path narrative.
- **interview_stage** — ровно одно из `{hr_screening, tech_qa, tech_coding, tech_case, system_design, behavioral, manager_round}` (`md/spec.md` §3 / §4.1). Класифицирует, на каком типе вопроса находимся (один QA, не весь раунд).
- **topic_tag** — открытый список (стартово: `experimentation`, `modeling`, `system_design`, `soft_communication`, `behavioral_situations`, …; пополняется по мере анализа корпуса).
- **score** — критерии из `md/assessors.md`. Generic-оси (любой `type`):
  - `question_fit`: bool — отвечает ли на поставленный вопрос.
  - `focus`: bool — есть ли основная мысль.
  - `clarity`: 1 (невнятно / off-topic) | 2 (частично понятно) | 3 (внятно и структурировано).
  - `completeness`: 1 (нет ключевых блоков) | 2 (закрыто частично) | 3 (закрыто полно).
  - `factual_correctness`: 1 (есть фактические ошибки) | 2 (смешанно / есть допущения) | 3 (фактически корректно).

  Behavioral-only (только при `type = behavioral`, см. `md/assessors.md` §3.2.2): `score.star` (4 binary флага S/T/A/R) и `score.amazon_spid` (4 балльных оси: scope, personal_contribution, impact, difficulty).

  Производные поля (implementation-уровень, не в spec — см. `md/arch_agents.md` §5.2):
  - `aggregate` — ярлык для summary table:
    - `strong` если `min(clarity, completeness, factual_correctness) == 3`;
    - `adequate` если `min == 2` и `sum >= 7`;
    - `weak` если `min == 2` и `sum < 7`, или есть хотя бы один балл `== 1`;
    - `missing` если кандидат вообще не дал ответа на вопрос (не путать с weak).
  - `rationale` — одна строка-обоснование с привязкой к цитате/наблюдению.
- **weakness_kind** — обязательно, если `aggregate ∈ {weak, adequate}` (`md/spec.md` §7 E3-4: «слабые места — с цитатами и формулировкой проблемы»). Ровно одно из:
  - `vague` — ответ-вода без сигнала.
  - `off-topic` — ответ на смежный вопрос.
  - `factual_error` — правдоподобный, но фактически неверный.
  - `incomplete` — ключевые блоки не раскрыты.
- **comment** — 2-3 предложения. LLM-генерируемый комментарий assessor'а (`AssessmentItem.comment` в `md/spec.md` §3). Не путать с `Evaluation.comment` (judge-уровень для EvalDataset, заполняется человеком в `md/requirements_postponed.md` §5 контексте; в feedback-report не используется).
  - **Mode-specific:**
    - `blind`: оценка и комментарий выводятся **только** из транскрипта, JD и CV. НИКАКИХ ссылок на feedback.txt, на «интервьюер заметил», на «прямой match с feedback» и т.п. Если бы feedback не существовал — комментарий должен звучать так же.
    - `with-feedback`: можно (и нужно, где уместно) цитировать конкретные слова из feedback.txt в кавычках как якорь.

### Шаг 5: Rollup (минимальный AlignmentReport + Interviewer's signal)

В MVP-варианте после ревизии 06-05 (`md/spec.md` §3) `AlignmentReport` содержит только `verdict` + `items` (последнее = весь набор `AssessmentItem` за раунд). JD aligned/partial/missing rollup и `Recommendation[]` — postponed (см. `md/requirements_postponed.md` §5, stories E3-5 / E3-7).

Этот шаг сводится к:

1. **Markdown-render `AssessmentItem[]`** — по одному блоку на каждый QA, в порядке `transcript_time`. Поля каждого блока: `question`, `candidate_answer`, `score` (по осям `md/assessors.md`), `expected_answer`, `comment`, `aggregate`-ярлык, `weakness_kind` (если применимо).
2. **Mode-specific:**
   - `blind`: секции `### Interviewer's signal` НЕТ. Вообще не упоминать feedback.txt в отчёте. Если в Шаге 1 файл существовал — это не повод его учитывать; blind-режим строго слеп.
   - `with-feedback`: добавить `### Interviewer's signal`. Разобрать `feedback.txt` построчно/по утверждению, тегировать каждое как `confirms` / `contradicts` / `orthogonal-to` соответствующий `AssessmentItem` (по Q-ID). Verbatim цитаты в кавычках.

### Шаг 5.5: Verdict (только blind)

Соответствие `md/spec.md` §3.1 (кейс Company A без feedback: «полный отчёт в blind mode»). В режиме `with-feedback` этот шаг **пропускается** — verdict не выводится, чтобы не отражать суждение интервьюера, а оставаться независимым решением модели.

В режиме `blind` после rollup сформировать `AlignmentReport.verdict ∈ {HIRE, NO_HIRE}`:

1. **Решение** — ровно одно из `HIRE` / `NO_HIRE`. Бинарно, без полутонов («lean hire» и т.п. не используются — заставляет модель честно встать на одну сторону). `P(HIRE)` postponed (см. `md/requirements_postponed.md` §5, story E3-7).
2. **Стартовая эвристика** (фиксируется здесь до прогона на нескольких кейсах):
   - `NO_HIRE`, если **≥1 `aggregate ∈ {weak, missing}`** среди `AssessmentItem` с `type = hard_skill` или `qa.interview_stage ∈ {tech_qa, tech_coding, tech_case, system_design}` (т.е. на критичных hard-вопросах).
   - `HIRE` иначе.
   - В пограничных случаях (все `adequate`, нет явных weak/missing, нет ярких strong) — `HIRE` по умолчанию (отказ требует доказательств).
3. **Обоснование** — 3-5 строк (буллет-лист), где модель явно перечисляет:
   - 1-2 ключевых **за** (опираясь на `strong` Q-IDs);
   - 2-3 ключевых **против** (опираясь на `weak`/`missing` Q-IDs);
   - factor, сильнее всего сдвигающий решение в одну сторону.

Эвристика — стартовая. Если на нескольких кейсах verdict стабильно расходится с интуицией, правило корректируется и фиксируется как открытый вопрос в `md/arch_agents.md` §9 «HIRE/NO_HIRE rule».

### Шаг 6: Self-check (quality)

Источники требований к чек-листу: `md/spec.md` §3 (артефакты), `md/assessors.md` (критерии), `md/spec.md` §7 E3-4.

Базовый чек-лист (оба режима):

- [ ] Каждый `AssessmentItem.qa` имеет `transcript_time` в обоих LinkedText (`md/spec.md` §3).
- [ ] Цитаты verbatim — grep'абельны в transcript.txt дословно (хотя бы endpoints).
- [ ] `qa.type` ровно из `{hard_skill, soft_skill, behavioral}` (`md/spec.md` §3).
- [ ] `qa.interview_stage` и `qa.topic_tag` заполнены (`md/spec.md` §3).
- [ ] `score` содержит generic-оси (`question_fit`, `focus`, `clarity`, `completeness`, `factual_correctness`) по `md/assessors.md`; для `qa.type = behavioral` — также `score.star` и/или `score.amazon_spid`.
- [ ] `aggregate`-ярлык согласован с triplet по правилу из Шага 4 (`strong`/`adequate`/`weak`/`missing`).
- [ ] Если `aggregate ∈ {weak, adequate}` — задан `weakness_kind ∈ {vague, off-topic, factual_error, incomplete}` (`md/spec.md` §7 E3-4).
- [ ] `rationale` обоснован цитатой/наблюдением.
- [ ] Никаких дублирующих Q&A пар (echo dedup отработал).
- [ ] Никаких meta-турнов в роли вопросов.

**Mode-specific дополнения:**

`blind`:
- [ ] Слово `feedback` нигде в отчёте не встречается (кроме имени файла отчёта в frontmatter, если оно там).
- [ ] Нет цитат, которые есть только в `feedback.txt` и которых нет в transcript/JD/CV.
- [ ] Нет фраз вида «совпадает с заметками интервьюера», «интервьюер отметил» и т.п.
- [ ] `inputs_present` в frontmatter не включает `feedback.txt`, даже если файл существует.
- [ ] Секция `## Verdict` присутствует, содержит ровно одно из `HIRE`/`NO_HIRE`, обоснование 3-5 буллетов (`md/spec.md` §3.1, кейс Company A без feedback). `P(HIRE)` не выводится (postponed, см. `md/requirements_postponed.md` §5).

`with-feedback`:
- [ ] Секция `### Interviewer's signal` присутствует и непустая.
- [ ] Все утверждения из feedback.txt разобраны и тегированы.
- [ ] Verbatim цитаты из feedback.txt grep'абельны в feedback.txt.

Если хоть один пункт не выполнен — исправить перед записью.

### Шаг 7: Запись результата

1. Путь:
   - `blind` → `<folder>/feedback-report.blind.md`
   - `with-feedback` → `<folder>/feedback-report.with-feedback.md`
2. Если файл уже существует → `feedback-report.<mode>.v2.md`, `.v3.md`, итеративно.
3. **Frontmatter:**
   ```yaml
   ---
   author: claude-code-opus-4-7
   source_folder: <folder>
   mode: <blind|with-feedback>
   generated_at: <YYYY-MM-DD>
   inputs_present:
     - cv.md
     - vacancy.txt
     - transcript.txt
     # feedback.txt — только если mode == with-feedback
   spec_compliance:
     scope: market-flow
     covers: [E1-4, E1-5, E3-4]
     divergences: [behavioral-evaluation]                  # см. блок «Соответствие spec.md»
     postponed: [E3-5, E3-6, E3-7]                         # см. md/requirements_postponed.md §5
   ---
   ```
4. **Структура тела:**
   ```
   # Feedback Report (<mode>) — <Candidate> × <Company> (<YYYY-MM-DD>)

   ## Summary table
   | #  | Тема (topic_tag) | type        | interview_stage | aggregate | weakness_kind | Time  |
   |----|------------------|-------------|-----------------|-----------|---------------|-------|
   | Q1 | experimentation  | hard_skill  | tech_qa         | adequate  | vague         | 00:34 |

   ## Verdict (только blind)
   - **Решение:** HIRE | NO_HIRE
   - **За:** ...
   - **Против:** ...
   - **Главный фактор:** ...

   ## Assessment Items

   ### Q1 — <topic_tag> (<type> / <interview_stage>, <time>)
   - **question** [`MM:SS`]: «verbatim quote»
   - **candidate_answer** [`MM:SS → MM:SS`]: «verbatim quote, можно `…`»
   - **expected_answer**: ...
   - **type**: hard_skill
   - **interview_stage**: tech_qa
   - **topic_tag**: experimentation
   - **score**:
     - question_fit: true / focus: true
     - clarity: 2 / completeness: 2 / factual_correctness: 3 → aggregate: adequate
     - (для type=behavioral также: star: {s,t,a,r}, amazon_spid: {scope, personal_contribution, impact, difficulty})
     - weakness_kind: vague
     - rationale: <one-line reason>
   - **comment**: ...

   ### Interviewer's signal (cross-check с feedback.txt)
   # Только в with-feedback. В blind эту секцию не выводить.
   ```
5. После записи — короткий ответ пользователю: путь + summary (количество Q, распределение типов, verdict, режим).

## Нюансы

- Транскрипт avito-кейса (~158 KB) целиком влезает в контекст; не чанкуем.
- `blind` особенно полезен когда хочется честно проверить, насколько LLM сама ловит gap'ы. Любая утечка из feedback.txt в blind-отчёт ломает основное value-proposition режима.
- При конфликте JD vs feedback (только в `with-feedback`) ведущий — JD; feedback корректирует ячейку (`partial` вместо `aligned`).
- Не выдумывать «ожидаемые ответы» из general knowledge без сигнала из vacancy.txt и cv.md.
- Если кандидат отвечает несколькими подряд `Microphone`-турнами с эхом интервьюера между ними — соединять в один ответ, эхо игнорировать.
- timecode хранится строкой как в источнике (`MM:SS` или `HH:MM:SS`); не нормализовать в секунды.
- Для аккуратного A/B сравнения двух режимов на одном кейсе — прогонять их в разных сессиях, чтобы избежать утечки контекста.

## Ограничения

- Один прогон = одна папка + один режим. Без батча, без одновременного blind+with-feedback в одном вызове.
- В режиме `with-feedback` verdict «наняли бы / нет» не выводится — это прерогатива blind-прогона (`md/spec.md` §3.1).
- Не сравнивает с другими интервью кандидата (`MemoryState` отложен по `md/spec.md` §8).
- Не использует Knowledge Base / curated corpus / `Requirements` / `Rubric` — это эпик E2 (`md/spec.md` §6, §7), вне scope feedback-report.
- Не редактирует входные файлы.

## Пример сессии

### Blind (default)

```
user: /feedback-report [private]/avito-20251212
assistant:
  [parse] mode=blind (default), folder=[private]/avito-20251212
  [validate] папка существует, файлы: cv.md, vacancy.txt, transcript.txt
  [skip] feedback.txt существует, но в blind НЕ читаю
  [extract] 17 Q&A пар после dedup
  [classify+score] 13 hard_skill / 2 behavioral / 2 soft_skill; 2 strong / 9 adequate / 6 weak / 0 missing
  [verdict] NO_HIRE (правило: ≥1 weak/missing на критичных hard-вопросах)
  [self-check] OK; нет упоминаний feedback в теле
  wrote: [private]/avito-20251212/feedback-report.blind.md
  Summary (blind): 17 questions; распределение по type 13/2/2; verdict NO_HIRE.
```

### With-feedback

```
user: /feedback-report [private]/avito-20251212 mode=with-feedback
assistant:
  [parse] mode=with-feedback, folder=[private]/avito-20251212
  [validate] папка существует, файлы: cv.md, vacancy.txt, transcript.txt, feedback.txt
  [extract] 17 Q&A пар
  [classify+score] аналогично blind, плюс цитаты feedback в комментариях
  [interviewer-signal] 8 утверждений feedback тегированы (confirms/contradicts/orthogonal)
  [self-check] OK
  wrote: [private]/avito-20251212/feedback-report.with-feedback.md
  Summary (with-feedback): 17 questions; распределение по type 13/2/2; Interviewer's signal 8 пунктов.
```
