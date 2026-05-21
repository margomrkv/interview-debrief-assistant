# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/`
- **Режим:** `split_and_validate` · **source_id:** `data_scientist_senior_doordash_commentary_datainterview_2021_02_15`
- **Старт:** 2026-05-20 21:05:20 +0200 · **Обновлено:** 2026-05-20 21:12:36 +0200
- **Длительность прогона (стена):** 7 мин 16 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 3 мин 2 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ✅ все зафиксированные шаги завершены
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 2 | 2. Извлечение Q&A (LLM) | да | claude-sonnet-4-6 | 3 мин | ✅ |
| 3 | 3. Excel | нет | — | 1 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 1 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 8 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (3/3), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 3 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 8
- **`source_id`:** `data_scientist_senior_doordash_commentary_datainterview_2021_02_15`
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
| 1 | `02:10` | What Does 90 Statistical Power Mean | — | recognized (1 Q&A) | #2 | `Statistics` | ⏳ | — |
| 2 | `04:50` | How Do You Determine the Practica… | — | recognized (1 Q&A) | #3 | `Experimentation` | ⏳ | — |
| 3 | `10:39` | Type 1 Error Rate | — | recognized (4 Q&A) | #5, #6, #7, #8 | `Statistics` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `02:10` — What Does 90 Statistical Power Mean

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #2 | -1 с | `Statistics` | all right so let's start with the first status questions what does 90 … |

#### Item #2

- **Question** (`02:09`): all right so let's start with the first status questions what does 90 statistical power mean
- **Candidate answer** (`02:15`): um so uh so it's 90 statistical power uh so statistical power is basically uh linked to the type one type of two errors which means uh what is the probability of uh finding a right observation when it uh when it doesn't exist or finding an observation uh or or saying that we found enough uh we did not found an observation when it exists so 90 statistical power means the the probability of uh finding an observation which uh of not finding an observation which exists is 90
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Statistics` · type=hard · stage=technical_qna

### 2. `04:50` — How Do You Determine the Practical Significance in a in an Experiment

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #3 | -2 с | `Experimentation` | next question how do you determine the practical significance in a in … |

#### Item #3

- **Question** (`04:48`): next question how do you determine the practical significance in a in an experiment
- **Candidate answer** (`04:53`): so when it depends on the type of experiment we run and the kind of metric we are looking at so matrix can be uh like mean um like mean is a metric or a rate can be a vector and metric can also be proportions right so it can be percentage of users that click on a particular link or things like that so in these both of these cases we do some kind of statistical tests like a two sided t test or a test of proportions uh and practical significant and the significance of those is determined by p value uh which in general it's if it's below 0.05 we say it's significant now that is just the statistical part if you wanna uh look at the practical part we would also look have to look at the business metrics for example the kind of lift that we have seen and that will depend on the cost benefit analysis so let's say uh a five percent increase in uh ltv of a consumer on a particular app would be profitable for us and that would be the break-even point and anything above that would be useful whereas anything below that would not be useful so if so if we look at that uh basically what we are seeing what we are saying is even if the results are significant statistically only if they make business sense then it would be practically significant and then there is one more aspect which is movement of multiple metrics so let's say we do an experimentation on one particular metric but and that comes out to be significant but the other metrics move along with it in the experiment uh and that can be like detrimental to our experiment so we will have to use that as well in our uh stating the practical significance of the experiment
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Experimentation` · type=hard · stage=technical_qna

### 3. `10:39` — Type 1 Error Rate

- **Проверка главы:** ✅ у маркера 4 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #5 | -83 с | `Statistics` | now how do you calculate type 1 and type your errors of your statistic… |
| #6 | -45 с | `Statistics` | do you want to start by explaining what type one type of error error r… |
| #7 | -3 с | `Statistics` | got it so in this case um what would be your type 1 error rate |
| #8 | +64 с | `Statistics` | so i'm going to interject there um because i think i want to kind of g… |

#### Item #5

- **Question** (`09:16`): now how do you calculate type 1 and type your errors of your statistical tests
- **Candidate answer** (`09:24`): okay so um one and type two errors uh can be calculated by uh use english can calculate it by um i mean by by using like uh you know uh i'm not really sure about this uh so probably
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Statistics` · type=hard · stage=technical_qna

#### Item #6

- **Question** (`09:54`): do you want to start by explaining what type one type of error error rates are sure
- **Candidate answer** (`10:02`): um a time for an error is basically uh nothing but a false positive so uh so it happens when uh the experiment incorrectly rejects the true null hypothesis uh and you know in which actually it should not so then a type one error occurs uh a type two error on the other hand it's a false negative it happens when an experiment does not reject the null hypothesis but it's uh but you know but the result is actually false so it should reject the hypothesis
- **Reference answer:** —
- **Interviewer feedback** (`10:35`): okay
- **Labels:** `Statistics` · type=hard · stage=technical_qna

#### Item #7

- **Question** (`10:36`): got it so in this case um what would be your type 1 error rate
- **Candidate answer** (`10:42`): uh so type 1 error rate uh you know in this case would be uh you know uh so basically let's say we have a null hypothesis uh that you know there is no significant change in the click-through rate uh of two types of users so there will be a type one uh error where you know this hypothesis will be rejected and and we find the results that there is a significant uh difference between the two uh you know the the two sides and one way of controlling that i can think of is using the power so power is nothing but uh statistical power is nothing but beta uh and that's the probability of making like say a type two error so power of of the set of three tests is one minus beta so you know we can adjust for that value
- **Reference answer:** —
- **Interviewer feedback** (`11:42`): okay
- **Labels:** `Statistics` · type=hard · stage=technical_qna

#### Item #8

- **Question** (`11:43`): so i'm going to interject there um because i think i want to kind of give you some hint here so let's just suppose that alpha is 0.05 and your beta is uh let's just let's just suppose that your power is um 0.8 then in that case how would you actually calculate your type 1 error type 1 and type tap to error rates
- **Candidate answer** (`12:07`): uh sure uh so the problem so you mentioned b beta is 20 power power is point eight power and your alpha is point zero five okay so if power is point eight it means a power is one minus beta so your beta would be 0.2 so the probability of making a type 2 error would be 0.2 um and alpha you mentioned is 0.05 right so alpha is 0.05 and i think that's the uh probability of committing a type one error so it's like a five percent probability of committing a type one
- **Reference answer:** —
- **Interviewer feedback** (`12:44`): okay okay awesome
- **Labels:** `Statistics` · type=hard · stage=technical_qna


## Check 3. Semantic field alignment per chapter (step 5, LLM)

The Cursor agent (same as step 2) reviews **extracted** Q&A: field timestamps vs chapter windows and whether texts match chapter titles and labels (`question_topic`, `question_type`). Does not change the overall verdict.


- **Статус:** ✅ все 3 глав без замечаний
- **Тайм-коды полей:** 3/3 ок · **Смысл/метки:** 3/3 ок


## Transcript spans without Q&A in JSON

Intervals in `timecodes.txt` not covered by any item span. Check for a missed question or service speech.

_No large uncovered spans (threshold: ≥25s, ≥4 timecoded lines)._


#### Короткие ответы кандидата (≤4 слов)

Проверьте по транскрипту: это **осмысленный** короткий ответ на вопрос, а не обрезанный span или пропуск речи кандидата.

| Item | Время | Ответ |
|------|-------|-------|
| #1 | 00:37 | sounds quick okay |

<!-- SEMANTIC_VALIDATION -->

## Semantic validation (step 5)

Машинный ответ LLM (шаг 5). Валидатор читает этот блок при повторном прогоне.

```json
{
  "chapters": [
    {
      "chapter_time": "00:02:10",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:04:50",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:10:39",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
