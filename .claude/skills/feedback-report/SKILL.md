---
name: feedback-report
description: Генерирует структурированный per-question feedback по папке прошедшего интервью в формате martin-meeting.md schema плюс rollup из md/spec.md §E4-4. Два режима — blind (default, без feedback.txt; независимая оценка модели + HIRE/NO HIRE verdict с P(HIRE)) и with-feedback (читает feedback.txt и добавляет секцию Interviewer's signal, без verdict'а). Принимает path и опциональный флаг mode=<blind|with-feedback>; пишет в <folder>/feedback-report.<mode>.md.
---

# Skill: Feedback report по интервью

## Назначение

Один прогон = одна папка интервью → один markdown-отчёт `feedback-report.<mode>.md` в той же папке.

Два режима работы:

- **`blind` (default).** Независимая оценка только по транскрипту, JD и CV. `feedback.txt` НЕ ЧИТАЕТСЯ ни на одном шаге. Назначение — слепое мнение модели; результат можно сравнить с реальным фидбеком интервьюера как сигнал качества системы (LLM-as-judge baseline). **Включает verdict HIRE / NO HIRE и P(HIRE).**
- **`with-feedback`.** Все четыре файла, плюс секция `### Interviewer's signal` в rollup. Назначение — глубокий post-mortem с учётом перспективы интервьюера. Минус: spoiler-эффект, модель может подгонять оценки под ожидания feedback. **Verdict не выводится** — иначе рискует отражать verdict интервьюера, а не независимое суждение модели; точка независимого решения — это blind-режим.

Содержимое отчёта:

1. Summary table (быстрый sniff-test).
2. **Verdict & P(HIRE)** — только в `blind`.
3. Per-question Assessment Items по схеме `internal-notes/2026-04-30-martin-meeting.md`.
4. Rollup по требованиям JD (`aligned` / `partial` / `missing` / `Recommendations`, плюс `Interviewer's signal` только в `with-feedback`) — это `AlignmentReport` из `md/spec.md` §E4-4.

Не батчует, не использует knowledge base / karpov-корпус, не сравнивает с другими интервью кандидата.

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
- **Schema референс:** `internal-notes/2026-04-30-martin-meeting.md` (Assessment Item, LinkedText, Тип).
- **Rollup референс:** `md/spec.md` §E4-4 (`AlignmentReport`) и §E4-5 (quality criteria).
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

1. Проверить, что папка существует. Если нет — остановиться с ошибкой.
2. Перечислить наличные файлы из `{cv.md, vacancy.txt, transcript.txt}`. Для `with-feedback` — также `feedback.txt`.
3. Если `transcript.txt` отсутствует → остановиться: «без транскрипта анализ невозможен».
4. Если `vacancy.txt` отсутствует → rollup делается на общих industry expectations (lead DS-роль); секция `## Rollup` помечается ярлыком `(no JD; fallback to industry baseline)`.
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

### Шаг 4: Per-question Assessment Item (martin schema)

Для каждой Q&A пары:

- **вопрос: LinkedText** — `{text: <verbatim цитата интервьюера>, transcript_time: "MM:SS"}`. Допустимо `…` в середине, endpoints точные.
- **ответ кандидата: LinkedText** — `{text: <verbatim, можно сжать через `…`>, transcript_time: "MM:SS → MM:SS"}` (диапазон).
- **ожидаемый ответ** — что хороший lead-DS-кандидат сказал бы под этот JD и уровень. Привязка к bullets JD; учёт CV, если есть.
- **тип** — ровно одно из:
  - `hard skill` — ML/DS техника: метрики, калибровка, обучающие данные, sample bias, эксплуатация моделей, system design.
  - `behaviour` — STAR-вопросы, управление командой, career path narrative.
  - `soft skill` — стиль коммуникации, clarification questions, structuring of reasoning.
- **оценка llm** — `strong` / `adequate` / `weak` / `missing` + одна строка причины.
- **наш комментарий** — 2-3 предложения.
  - **Mode-specific:**
    - `blind`: оценка и комментарий выводятся **только** из транскрипта, JD и CV. НИКАКИХ ссылок на feedback.txt, на «интервьюер заметил», на «прямой match с feedback» и т.п. Если бы feedback не существовал — комментарий должен звучать так же.
    - `with-feedback`: можно (и нужно, где уместно) цитировать конкретные слова из feedback.txt в кавычках как якорь.

### Шаг 5: Rollup (AlignmentReport)

1. **JD checklist.** Из `vacancy.txt` извлечь requirements в bullet-list.
2. **Классификация по requirements:** для каждого пункта JD — `aligned` / `partial` / `missing` с цитатой Q-ID. Минимум один Q-ID на каждую строку.
3. **Mode-specific:**
   - `blind`: секции `### Interviewer's signal` НЕТ. Вообще не упоминать feedback.txt в отчёте. Если в Шаге 1 файл существовал — это не повод его учитывать; blind-режим строго слеп.
   - `with-feedback`: добавить `### Interviewer's signal`. Разобрать `feedback.txt` построчно/по утверждению, тегировать каждое как `confirms` / `contradicts` / `orthogonal-to` соответствующий пункт JD-rollup. При конфликте JD vs feedback ведущий — JD; feedback корректирует ячейку (`partial` вместо `aligned`) с явным callout.
4. **Recommendations.** 3-5 пунктов «next-time», конкретно.
   - `blind`: выводятся только из `partial` + `missing` JD-rollup и LLM-собственного суждения по транскрипту.
   - `with-feedback`: дополнительно учитывают `contradicts`-сигналы из feedback.

### Шаг 5.5: Verdict & P(HIRE) (только blind)

В режиме `with-feedback` этот шаг **пропускается** — verdict не выводится.

В режиме `blind` после rollup сформировать агрегированное решение:

1. **Решение** — ровно одно из `HIRE` / `NO HIRE`. Бинарно, без полутонов («lean hire» и т.п. не используются — заставляет модель честно встать на одну сторону).
2. **P(HIRE)** — целое число процентов в `[0, 100]`, отражает уверенность модели. Пороговая интерпретация: `≥ 50%` ⇒ HIRE, `< 50%` ⇒ NO HIRE; решение и вероятность должны быть согласованы.
3. **Обоснование** — 3-5 строк (буллет-лист), где модель явно перечисляет:
   - 1-2 ключевых **за** (опираясь на `aligned` rollup и `strong` Q-IDs);
   - 2-3 ключевых **против** (опираясь на `partial`/`missing` rollup и `weak`/`missing` Q-IDs);
   - factor, сильнее всего сдвигающий вероятность в одну сторону.

**Калибровка вероятности** (внутренний руководящий принцип, не показываем в отчёте):

| Картина                                                                 | P(HIRE) ориентир |
|-------------------------------------------------------------------------|------------------|
| ≥1 missing/weak в core hard skill JD-требовании + нет компенсирующих strong | 15–35%           |
| Mostly adequate, без явных red flags, без ярких strong                  | 40–55%           |
| ≥2 strong в JD-relevant областях + только мелкие weak в периферии       | 60–75%           |
| Bar-raising: strong по hard skill ядру JD, нет weak                     | 75–90%           |

Эти ориентиры — для согласованности через прогоны на разных кейсах. Не подгонять оценки Assessment Items под нужную P(HIRE); сначала оценки, потом verdict.

### Шаг 6: Self-check (E4-5 quality)

Базовый чек-лист (оба режима):

- [ ] Каждый Assessment Item имеет `transcript_time` в обоих LinkedText.
- [ ] Цитаты verbatim — grep'абельны в transcript.txt дословно (хотя бы endpoints).
- [ ] `тип` ровно из `{hard skill, behaviour, soft skill}`.
- [ ] `оценка llm` обоснована цитатой/наблюдением.
- [ ] Каждая строка rollup `aligned/partial/missing` ссылается на ≥1 Q-ID.
- [ ] Никаких дублирующих Q&A пар (echo dedup отработал).
- [ ] Никаких meta-турнов в роли вопросов.

**Mode-specific дополнения:**

`blind`:
- [ ] Слово `feedback` нигде в отчёте не встречается (кроме имени файла отчёта в frontmatter, если оно там).
- [ ] Нет цитат, которые есть только в `feedback.txt` и которых нет в transcript/JD/CV.
- [ ] Нет фраз вида «совпадает с заметками интервьюера», «интервьюер отметил» и т.п.
- [ ] `inputs_present` в frontmatter не включает `feedback.txt`, даже если файл существует.
- [ ] Секция `## Verdict` присутствует, содержит ровно одно из `HIRE`/`NO HIRE`, P(HIRE) — целое в `[0, 100]`, обоснование 3-5 буллетов.
- [ ] Согласованность: P(HIRE) ≥ 50% ⇔ HIRE; P(HIRE) < 50% ⇔ NO HIRE.

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
   ---
   ```
4. **Структура тела:**
   ```
   # Feedback Report (<mode>) — <Candidate> × <Company> (<YYYY-MM-DD>)

   ## Summary table
   | # | Тема | Тип | Оценка | Time |
   |---|------|-----|--------|------|
   | Q1 | ... | hard skill | adequate | 00:34 |

   ## Verdict (только blind)
   - **Решение:** HIRE | NO HIRE
   - **P(HIRE):** NN%
   - **За:** ...
   - **Против:** ...
   - **Главный фактор:** ...

   ## Assessment Items

   ### Q1 — <Тема> (<тип>, <time>)
   - **Вопрос** [`MM:SS`]: «verbatim quote»
   - **Ответ кандидата** [`MM:SS → MM:SS`]: «verbatim quote, можно `…`»
   - **Ожидаемый ответ**: ...
   - **Тип**: hard skill
   - **Оценка LLM**: adequate — <one-line reason>
   - **Наш комментарий**: ...

   ## Rollup (vs JD)

   ### aligned
   - <JD requirement>: <evidence Q-IDs>

   ### partial
   - <JD requirement>: <evidence Q-IDs> + <callout>

   ### missing
   - <JD requirement>: <evidence Q-IDs>

   ### Interviewer's signal (cross-check с feedback.txt)
   # Только в with-feedback. В blind эту секцию не выводить.

   ### Recommendations
   1. ...
   2. ...
   ```
5. После записи — короткий ответ пользователю: путь + summary (количество Q, распределение типов, расклад rollup, режим).

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
- В режиме `with-feedback` verdict «наняли бы / нет» не выводится — это прерогатива blind-прогона.
- Не сравнивает с другими интервью кандидата (`MemoryState` отложен по spec.md §8).
- Не использует knowledge base / curated corpus (это §E2-1).
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
  [classify+score] 13 hard / 2 behaviour / 2 soft; 2 strong / 9 adequate / 6 weak / 0 missing
  [rollup] 1 aligned / 3 partial / 0 missing
  [verdict] NO HIRE, P(HIRE) = 30%
  [self-check] OK; нет упоминаний feedback в теле; verdict + P согласованы
  wrote: [private]/avito-20251212/feedback-report.blind.md
  Summary (blind): 17 questions; rollup 1/3/0; verdict NO HIRE @ 30%; recommendations 5 пунктов.
```

### With-feedback

```
user: /feedback-report [private]/avito-20251212 mode=with-feedback
assistant:
  [parse] mode=with-feedback, folder=[private]/avito-20251212
  [validate] папка существует, файлы: cv.md, vacancy.txt, transcript.txt, feedback.txt
  [extract] 17 Q&A пар
  [classify+score] аналогично blind, плюс цитаты feedback в комментариях
  [rollup] aligned/partial/missing + Interviewer's signal: 8 утверждений feedback тегированы
  [self-check] OK
  wrote: [private]/avito-20251212/feedback-report.with-feedback.md
  Summary (with-feedback): 17 questions; rollup 1/3/0; Interviewer's signal 8 пунктов; recommendations 5 пунктов.
```
