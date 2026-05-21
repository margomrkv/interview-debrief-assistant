# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06`
- **Режим:** `split_and_validate` · **source_id:** `product_analyst_middle_facebook_fill_rate_interview_query_2020_07_06`
- **Старт:** 2026-05-20 21:18:04 +0200 · **Обновлено:** 2026-05-20 21:31:01 +0200
- **Длительность прогона (стена):** 12 мин 57 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 2 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ⚠️ неполный журнал (проверьте pipeline-log)
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 3 | 3. Excel | нет | — | 1 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 1 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
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


- **Файл:** `splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 7
- **`source_id`:** `product_analyst_middle_facebook_fill_rate_interview_query_2020_07_06`
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
| — | `00:00` | Introduction | — | skip | — | — | ⏳ | — |
| 1 | `00:45` | Background | — | recognized (2 Q&A) | #1, #2 | `Adaptability`, `Product Metrics` | ⏳ | — |
| 2 | `06:10` | Solution | — | recognized (2 Q&A) | #4, #5 | `Product Metrics` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `00:45` — Background

- **Проверка главы:** ✅ у маркера 2 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | -20 с | `Adaptability` | so to start out i thought we could tackle one of these questions that … |
| #2 | +75 с | `Product Metrics` | so the first question that i have for you today is let's say that you … |

#### Item #1

- **Question** (`00:25`): so to start out i thought we could tackle one of these questions that is pretty popular in terms of ads but first i'd love to just kind of do like a quick summary on your like background like how did you get into data science
- **Candidate answer** (`00:43`): sure um when i went in finance after graduating from college study computer science like a lot of folks here in silicon alley and was working on some level of analysis and construction of some model portfolios that we had and in doing so you know worked with a lot of data like financial data that was coming through um i became responsible for you know kind of reliable delivery of that data as well as kind of building tools to help make the analysis process more efficient so what kind of fell into data like that and when i decided that i didn't want to work in finance anymore and go into more you know consumer tech data was kind of a natural avenue for mediums kind of continue working in so there was this hot term at the time data science it became like that kind of explorer and you know one thing led to another
- **Reference answer:** —
- **Interviewer feedback** (`01:40`): nice cool i'm glad that you got into it and i think that there's definitely you know lots of people transitioning from finance over as well i can definitely resonate with that kind of characterization of your background cool
- **Labels:** `Adaptability` · type=behavioral · stage=fit_hr

#### Item #2

- **Question** (`02:00`): so the first question that i have for you today is let's say that you work on the ads team had a social media company let's say facebook right and a definition or term that they have in ads is fill rate and it's defined as the number of overall impressions divided by potential opportunities so let's say that you see that this film rate metric has dipped by 10% what would you investigate first
- **Candidate answer** (`02:23`): i'd want to find out whether that 10% is like relative or you mean like in absolute terms so i guess you know seeing that it's a rate obviously made up of kind of like a numerator and denominator sometimes doesn't tell the full story when you look at it just as a metric by self so the first thing i would do would be to look into like what's going on like what's driving that that that drop in the fill rate so what could be happening is you know the denominator in this case the impression opportunities could be getting a lot bigger which you know my actually signal that a growth in the business so that might be something that that's favorable and simply we just need some time for the numerator to catch up on assuming like you know we're showing ads here so like you advertise yourself to come online yep the other scenario is obviously if the numerator is is the one dropping and we're not seeing any new activity on the denominator then that would be a little bit more of a cause for immediate concern and probably something we want to look into immediately
- **Reference answer:** —
- **Interviewer feedback** (`02:32`): let's say that it's relative so if you know fillrate was holding 70 percent yeah steady and then let's say it happened it's been steady for like a week and then it dipped down by 10 percent to like 81 percent okay okay
- **Labels:** `Product Metrics` · type=hard · stage=technical_case

### 2. `06:10` — Solution

- **Проверка главы:** ✅ у маркера 2 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #4 | -37 с | `Product Metrics` | so is there any other way that you can divide it out even within like … |
| #5 | +35 с | `Product Metrics` | let's say like we're focusing in on sessions right so let's say that w… |

#### Item #4

- **Question** (`05:33`): so is there any other way that you can divide it out even within like the new users or new sessions to understand where i might be coming from given like in this scenario facebook is like a pretty big business so there's probably like a ton of different ways that people can sign up for a you know a facebook account or potentially be using facebook at the time so how else would i break out the increase in sessions you're saying
- **Candidate answer** (`06:04`): yeah so so let's say let's say we see a lot of new sessions from new members i would obviously look into like like acquisition channels of all these new members and see you know if there's whether one of the theories that i just threw out might be the reason why there are there are new members joining like maybe some i don't know some advertising campaign we're running elsewhere suddenly everyone else stopped bidding on those keywords so now like you know we're just like it getting a lot of new users uh not sure if i'm going down the right track
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Product Metrics` · type=hard · stage=technical_case

#### Item #5

- **Question** (`06:45`): let's say like we're focusing in on sessions right so let's say that we know that there's a lot more sessions is there a way that we can verify that the sessions are coming from new users as well compared to just existing users using the platform suddenly
- **Candidate answer** (`07:02`): yeah we would look at you know sessions per user and we would see like and we would compare to the total number of users so like you know sessions could go up but those could come from like a slew of new users or they could be that existing user suddenly are engaging a lot more on that particular date right so i will try to figure out like just take my number of sessions and divide it quickly over my number of distinct users that day and just get a sense of like what that ratio is and i would expect if it were new users that that number would drop right like new years i expect to have less engagement when they first join but and and driven by the figure member base it's increased from engagement in my existing users then i would expect that number to have increased
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Product Metrics` · type=hard · stage=technical_case


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
      "chapter_time": "00:00:45",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:06:10",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
