# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/interview-query/data-scientist-senior-walmart-underpricing-interview-query-2020-08-04`
- **Режим:** `split_and_validate` · **source_id:** `data_scientist_senior_walmart_underpricing_interview_query_2020_08_04`
- **Старт:** 2026-05-20 21:18:03 +0200 · **Обновлено:** 2026-05-20 21:32:26 +0200
- **Длительность прогона (стена):** 14 мин 23 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 2 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ⚠️ неполный журнал (проверьте pipeline-log)
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interview-query/data-scientist-senior-walmart-underpricing-interview-query-2020-08-04/data-scientist-senior-walmart-underpricing-interview-query-2020-08-04.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 3 | 3. Excel | нет | — | 1 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 1 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interview-query/data-scientist-senior-walmart-underpricing-interview-query-2020-08-04/data-scientist-senior-walmart-underpricing-interview-query-2020-08-04.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interview-query/data-scientist-senior-walmart-underpricing-interview-query-2020-08-04/data-scientist-senior-walmart-underpricing-interview-query-2020-08-04.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interview-query/data-scientist-senior-walmart-underpricing-interview-query-2020-08-04/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 8 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (1/1), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 1 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/interview-query/data-scientist-senior-walmart-underpricing-interview-query-2020-08-04/data-scientist-senior-walmart-underpricing-interview-query-2020-08-04.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 8
- **`source_id`:** `data_scientist_senior_walmart_underpricing_interview_query_2020_08_04`
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
| 1 | `00:00` | Walmart underpricing case mock in… | — | recognized (1 Q&A) | #1 | `Product Metrics` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `00:00` — Walmart underpricing case mock interview

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | +8 с | `Product Metrics` | let's say that you're a data scientist working on pricing different pr… |

#### Item #1

- **Question** (`00:08`): let's say that you're a data scientist working on pricing different products on our e-commerce site right and the online price is dependent on the availability of the product the demand and the logistics cost of providing it to the end consumer right uh so you discover that suddenly the algorithm is vastly underpricing a certain consumer product what are the steps that you take in diagnosing the problem
- **Candidate answer** (`00:32`): so you mentioned that the price of a product is dependent on the availability uh the logistic cost and the demand right so and then you said a particular type of products are getting underpriced by the algorithm now i guess um the first off i'd like to understand um like where are we getting this uh the demand information from like i'm sure the logistic cost is something that the company handles so they're able to keep a track on what it costs to ship and stuff um but how do we get the demand aspect of uh the of a product is it from a competitor's website is a third-party website or is it like for data that we trust really well okay and then you mentioned that the algorithm is under pricing a particular group of products right um do we know um how much like is it are we saying is underpriced because uh what other computers are selling the same product at or is it that uh the the product used to cost x dollars in like five months ago and now it's showing x minus you know some y percentage right like there's a significant drop in uh in the price
- **Reference answer:** —
- **Interviewer feedback** (`01:14`): uh let's say it's from our own internal data it's from the amount of people that have historically bought the product in the past um let's say that we have availability of all the other kinds of data on our website as well like user clicks you know like searches et cetera yeah how does that work yeah it's the latter so let's say that we saw that it's dropped by like 50 percent from like five months ago so from a historical uh trend downwards um
- **Labels:** `Product Metrics` · type=hard · stage=technical_case


## Check 3. Semantic field alignment per chapter (step 5, LLM)

The Cursor agent (same as step 2) reviews **extracted** Q&A: field timestamps vs chapter windows and whether texts match chapter titles and labels (`question_topic`, `question_type`). Does not change the overall verdict.


- **Статус:** ✅ все 1 глав без замечаний
- **Тайм-коды полей:** 1/1 ок · **Смысл/метки:** 1/1 ок


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
      "chapter_time": "00:00:00",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
