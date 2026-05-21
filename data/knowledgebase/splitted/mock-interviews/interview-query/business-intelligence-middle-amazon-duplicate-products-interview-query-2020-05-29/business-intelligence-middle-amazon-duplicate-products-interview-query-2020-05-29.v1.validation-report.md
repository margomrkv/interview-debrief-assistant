# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29`
- **Режим:** `split_and_validate` · **source_id:** `business_intelligence_middle_amazon_duplicate_products_interview_query_2020_05_29`
- **Старт:** 2026-05-20 21:18:02 +0200 · **Обновлено:** 2026-05-20 21:30:16 +0200
- **Длительность прогона (стена):** 12 мин 14 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 5 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ⚠️ неполный журнал (проверьте pipeline-log)
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 3 | 3. Excel | нет | — | 4 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 1 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 7 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (2/2), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 2 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 7
- **`source_id`:** `business_intelligence_middle_amazon_duplicate_products_interview_query_2020_05_29`
- **`splitter_mode`:** `split_and_validate`


---

## Check 2. YouTube chapter alignment (step 4)


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

### All YouTube chapters

Every timestamp from `video.md`: question chapters — status and Q&A; service chapters — where speech landed in JSON. Full texts below per question chapter.


| # | YT | Заголовок | Секция | Привязка (4) | Q&A | Темы | Смысл (5) | Куда в JSON |
|---|-----|-----------|--------|--------------|-----|------|-----------|-------------|
| — | `00:00` | <Untitled Chapter 1> | — | skip | — | — | ⏳ | — |
| 1 | `00:35` | Shashank Intro | — | recognized (1 Q&A) | #1 | `Communication` | ⏳ | — |
| 2 | `02:55` | Business Intelligence Case Question | — | recognized (1 Q&A) | #2 | `Data Modeling` | ⏳ | — |
| — | `11:55` | Feedback and Tips | — | skip | — | — | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `00:35` — Shashank Intro

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | -8 с | `Communication` | before we get started I would love to just kind of like to ask you abo… |

#### Item #1

- **Question** (`00:27`): before we get started I would love to just kind of like to ask you about your background and how you got into data science and yeah how you got interested in it
- **Candidate answer** (`00:37`): sure thank you so much for having me over here Jay so a little bit about my background I've always been a data and numbers guy I used to work as a bi engineer back before I got a masters and then I did a master's in data analytics work with the data scientist for almost two years mostly my experience has been around machine learning problems and machine learning implementation ended up learning some DevOps skills as well and like PI spark stuff so that when you know when you have their products need to be scaled out if the coding is pretty different so I ended up learning how to convert like Python code to PI spark on my own learning experience and then I moved over to Amazon as a business intelligence engineer most of my work over here was around you know tableau reporting building ETL jobs figuring out what kind of data structure needs to be in the reporting databases so that your end reports work well and you know just digging into deeper into different metrics that the business wants to learn and just providing more information on what they could look at instead of what they're already looking at so that's pretty much what my experience has been so far from a technical point of view it's more about sequel Python Vice power tableau and then some Jango Web API as well because in my previous company nobody really knew how to use you know Python based data science models so I had to figure out how to production lies them on my own and have the end product just make like Web API calls to be predictions instead of dem trying to you know ingest a mortal end and interact with it so that was a pretty neat skill to have and think that's something that's being needed more and more in many companies these days
- **Reference answer:** —
- **Interviewer feedback** (`02:30`): definitely yeah I think the overall kind of scale of data Sciences needs a lot of what you just kind of described in different kinds of metrics track like ETL jobs being able to do the modeling for each and just having an idea of every part of the funnel in terms of
- **Labels:** `Communication` · type=behavioral · stage=fit_hr

### 2. `02:55` — Business Intelligence Case Question

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #2 | +0 с | `Data Modeling` | I'd love to start out with like a first question and let's say this ha… |

#### Item #2

- **Question** (`02:55`): I'd love to start out with like a first question and let's say this has to do with an e-commerce website like Amazon right so let's say you're running an e-commerce website and you want to get rid of let's say duplicate products I may be listed under different sellers names you know like a really large database so for example we have two products but that the same product but they're named iPhone X and Apple iPhone 10 right and so given that we have these two products we want to deduplicate it but let's say that this example shows up for like a lot of different cases what's one way that you would go a bit go about actually doing this
- **Candidate answer** (`03:35`): so if it's a established ecommerce company I would assume that they would have some kind of an ID for every product that they have in their inventory so something like an SKU or an ace and if it's Amazon then that's pretty unique and you know even the you know the description is different in different under different sellers and I would assume that they would have the same SKU so you know if you just look at the you know get a list of all the all like get a total of the SKU different sellers and then do a distinct list of SK use across sellers you will notice what kind of SK use are replicated and under which seller and then once you have that you can go to the business saying what do you want to do with them if people eat them whatever yeah
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Data Modeling` · type=hard · stage=technical_case


## Check 3. Semantic field alignment per chapter (step 5, LLM)

The Cursor agent (same as step 2) reviews **extracted** Q&A: field timestamps vs chapter windows and whether texts match chapter titles and labels (`question_topic`, `question_type`). Does not change the overall verdict.


- **Статус:** ✅ все 2 глав без замечаний
- **Тайм-коды полей:** 2/2 ок · **Смысл/метки:** 2/2 ок


## Transcript spans without Q&A in JSON

Intervals in `timecodes.txt` not covered by any item span. Check for a missed question or service speech.

_No large uncovered spans (threshold: ≥25s, ≥4 timecoded lines)._

<!-- SEMANTIC_VALIDATION -->

## Semantic validation (step 5)

Машинный ответ LLM (шаг 5). Валидатор читает этот блок при повторном прогоне.

```json
{
  "chapters": [
    {
      "chapter_time": "00:00:35",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:02:55",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
