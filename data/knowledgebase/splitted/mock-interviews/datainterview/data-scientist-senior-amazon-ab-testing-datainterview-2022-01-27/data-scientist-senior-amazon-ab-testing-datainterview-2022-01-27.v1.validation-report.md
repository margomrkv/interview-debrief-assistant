# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/`
- **Режим:** `split_and_validate` · **source_id:** `data_scientist_senior_amazon_ab_testing_datainterview_2022_01_27`
- **Старт:** 2026-05-20 21:05:20 +0200 · **Обновлено:** 2026-05-20 21:12:30 +0200
- **Длительность прогона (стена):** 7 мин 10 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 3 мин 2 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ✅ все зафиксированные шаги завершены
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 2 | 2. Извлечение Q&A (LLM) | да | claude-sonnet-4-6 | 3 мин | ✅ |
| 3 | 3. Excel | нет | — | 1 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 1 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 11 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (2/2), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 2 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 11
- **`source_id`:** `data_scientist_senior_amazon_ab_testing_datainterview_2022_01_27`
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
| — | `00:00` | Intro | — | skip | — | — | ⏳ | — |
| 1 | `00:50` | Recommender System Metrics | — | recognized (1 Q&A) | #1 | `Product Metrics` | ⏳ | — |
| 2 | `05:38` | AB Testing Recommender System | — | recognized (1 Q&A) | #2 | `Experimentation` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `00:50` — Recommender System Metrics

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | -4 с | `Product Metrics` | what i'd like to ask you whoops i just based in the wrong spot is how … |

#### Item #1

- **Question** (`00:46`): what i'd like to ask you whoops i just based in the wrong spot is how do you measure the effectiveness of a recommender system
- **Candidate answer** (`00:55`): okay so before i dive into uh this question so uh i have a few clarified ques uh clarifying question that i want to ask uh the first question is uh so are you talking about the recommend recommended system uh in amazon web specifically okay sounds good and uh in terms of uh effectiveness uh can you uh tell me a little bit about what you mean by effectiveness okay so maybe uh how accurate uh the recommended recommended system can predict uh the user's preference when they purchase products in amazon web do you think that's a fair assumption okay sounds good so essentially is a predictive the recommender system okay sounds good uh so a few things uh that i can think of is that like we just mentioned uh the percentage of uh products uh uh let's see number of uh product purchases out of a number of uh product recommended so right now i'm just coming up with a metrics that we can use to measure the effectiveness effectiveness of a recommender system and i think the number of products purchased out of all the product recommended will be an indicator to tell us how uh how uh how the recommended system can uh actively predict users preferences because the more product that they purchase uh the higher this percentage the more likely that uh the users are interested in the products that recommend the system is recommending and then the second metric that i can think of is the time the amount of time spent that users have spent on purchasing purchasing on the platform uh the reason so in this case uh i would say if the recommended system is doing its job it is likely that uh the user spend less time on uh picking the right product uh picking the products that they are interested because uh so when whenever users go to amazon right they have a product in mind that they want to purchase and if the recommended system is doing its job then it's likely that the time span in their purchase is low uh and the third one that i can think of is uh the uh average revenue uh average purchase uh revenue uh per user uh and i think if this is also a good indicator because revenue is the north star metrics that amazon wants to optimize and if the recommender system is uh effective it is most like likely that the average purchase revenue per user is high so these are the three metrics that i can i can come up with to measure the effectiveness of a recommended system
- **Reference answer:** —
- **Interviewer feedback** (`01:15`): yes you could perhaps think about it in terms of maybe the quality of the uh recommendation quality of the recommended system yep
- **Labels:** `Product Metrics` · type=hard · stage=technical_qna

### 2. `05:38` — AB Testing Recommender System

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #2 | -10 с | `Experimentation` | so segue over to this is um suppose that a new recommended system is p… |

#### Item #2

- **Question** (`05:28`): so segue over to this is um suppose that a new recommended system is proposed how do you know if this new version should be used
- **Candidate answer** (`05:37`): sounds good so in order to uh in order to understand whether we should launch this new version system the best way that we can do is do an ap test where the control group uh uh will will have uh the old other existing recommender system whereas the treatment group will have the new uh version of the recommender system uh and then the metrics that we can measure um is uh the number of uh like the number of product purchase out of the number of products recommended so let's say if the average number of product purchases the number of products recommended per user uh is uh increasing in the treatment group then we can conclude that the new version system can be used so do you have any questions uh based on uh the the control groups and treatment groups and the metrics that i have list so far if not then i can go on with the experimental framework that we can use
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Experimentation` · type=hard · stage=technical_qna

## Speaker boundary check (heuristic)

Automatic role check (no diarization): Q/A duplicates, truncated questions, candidate speech in question field, interviewer lines inside answer.

- **Item #7:** слишком короткий обрывок в `interviewer_question` — на шаге 2 склейте соседние реплики интервьюера в транскрипте; не парафразируйте по video.md.


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
      "chapter_time": "00:00:50",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:05:38",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
