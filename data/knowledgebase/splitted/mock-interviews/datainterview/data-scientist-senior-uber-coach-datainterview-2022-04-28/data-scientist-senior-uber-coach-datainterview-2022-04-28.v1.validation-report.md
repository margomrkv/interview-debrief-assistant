# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/`
- **Режим:** `split_and_validate` · **source_id:** `data_scientist_senior_uber_coach_datainterview_2022_04_28`
- **Старт:** 2026-05-20 21:05:21 +0200 · **Обновлено:** 2026-05-20 21:12:45 +0200
- **Длительность прогона (стена):** 7 мин 24 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 3 мин 1 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ✅ все зафиксированные шаги завершены
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 2 | 2. Извлечение Q&A (LLM) | да | claude-sonnet-4-6 | 3 мин | ✅ |
| 3 | 3. Excel | нет | — | 1 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 0.00 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 13 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (2/2), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 2 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 13
- **`source_id`:** `data_scientist_senior_uber_coach_datainterview_2022_04_28`
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
| 1 | `01:45` | SQL | — | recognized (1 Q&A) | #1 | `SQL` | ⏳ | — |
| 2 | `16:23` | Product Sense | — | recognized (2 Q&A) | #2, #3 | `Product Metrics` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `01:45` — SQL

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | +16 с | `SQL` | and um using this table i'd like you to address this question which is… |

#### Item #1

- **Question** (`02:01`): and um using this table i'd like you to address this question which is among the services with the top three highest cancellation rate find the average amount of value and maximum order count across order dates return the service name average monetary value and maximum order count
- **Candidate answer** (`02:16`): okay so just repeat the question i have to find the top three highest cancellation rates the average monetary value and the maximum order count across the dates and this is something that i have to return that is service name monetary value and this so um my approach to go with this problem is to first figure out what the cancellation rate is so we have number of orders status of order monetary value and service name and we have to find the top highest cancellations rate so um in order to find because we have to output the maximum order count but obviously it's from the cancellation highest cancellation rate so first we have to figure out how are we going to find the cancellation rate um is it correct okay so um and then um as this is the cancellation rate so i'm just writing this according to chunks right now so that i can just draw them in first afterwards combine them is it okay so um to find out the cancellation rate and the obviously we have to average that out so that we can um yeah so let me just go with this so to find the cancellation rate we have to figure out the one that is cancelled within this block so that would be a case statement so um if i just for my own sake right now if i do yes when um order of status um is equal to cancelled then one else zero and and so this could be um all the values and then we have to average them to find the cancellation rate sorry this won't come here so um zero here sorry yeah i pressed the shift so it went there so yeah and in order to if we create a table for this it would be select um we have to output the services so just another table for this service name and because we have to find the cancellation rate we would obviously have to average this to find the cancellation rate so the formula for cancellation rate would be uh the total number of rows within this are divided by the ones that are cancelled right so um this could be uh cancelled so um yeah i'll take this down and um uh sorry this is uh i status and obviously we're using a um an aggregation so we would definitely use a group by here um by one sorry um but um so we also have to figure out a way where we can like have all of them because we have to conquer the cancellation rate and to find the number of rows we would definitely want to use a window function over here so um to do that that window function all of this would be um subcuried within that window function so my whole approach would be finding that as a cancellation rate and then using that within maybe the ct function to figure out obviously all the average values of the one that have the canceled one and then we have to find the maximum count so maximum count um on the um the cancellation rate is it right okay so this would be um if i just write the sub query first to get the cancellation rate it would be select um service name and for for finding out the number of rows i would be using rank okay i can use dense rank as well but it's um it would it would have similar values of the numbers that we don't want uh so um this and if you go rank over and over here as um we have to find the top three so we would order this by um how can we order this we can order this by the cancellation rate your cancellation rate that you've calculated right yeah so we can we can order that but this cancel right within the sub curie yeah so so would use to order by yeah so this would be cancel and obviously this because we have to find the top three we would use this as a cancel rank and uh now we can like uh because this would be from the sub curry of this so um yeah and then this hole could be and you need a one second so here so um so you you would whoops just call that sq sub chord okay so and then we would use this hole to find the now we can because now we have as a column we can have the service name rank and then we can use this to find the average value and then the maximum count of the cancellation rate okay um if i do with um uh i'm not sure do we do we i think we give a name here um actually used with clause but you've already given a name which is ct in this case oh yeah oh yeah that's right yeah so and close parentheses so you've now wrapped this on under the first with clause yeah and now you can reference cte yeah yeah sorry so with this i can um use i can now i have to output we have to output the service name so we can do select uh the service name from here and then now we can calculate the average monetary value so um you go here energy as um which you want and then for um the maximum order count so the maximum order let me just um just complete this and then uh i would come for the this maximum order count so um this would be um obviously from the right status and then obviously we have to find the top highest three so there would be a where clause where um because we don't know what the services would be so we we can have a sub curry within this so um i i will come back to this max um initially after writing this so service name and then we can use the enclosed to filter um because we use in when we have multiple values and in this case we would be having multiple values for service name it would be select um select because we're using rare cost but select so this would be select from and now we can get this and then the row rank the rank function because we have to find the maximum ones so it would be from cp where uh this rank value is less than um four because um yeah because it's yeah okay fourth um okay and if we come back to this one so the maximum order count so it would be the max of um maximum order count so the count of the cancelled one right so it would be maybe this it would be the well it would be the number of orders oh it would be the number of products so it would be yes count orders column oh yeah okay so it would be um so yeah i was thinking that it's yeah related to cancellation right that's the control number i should have asked this earlier well solving so this could be um max account and if i just go through uh do you think yeah you're right all right
- **Reference answer:** —
- **Interviewer feedback** (`14:17`): so this is the correct solution there were of course some bumps along the way and i you know provided some hint um but ultimately this is the correct solution um so i just want to provide some inputs here before we proceed to the next section um so it helps to clarify exactly what the output table is um so that you avoid a situation where as you're writing you're not really sure what the what some of the terminology actually means like maximum order count thought it was something else right yeah um so have a clear visual in terms of what that output table looks like by asking clarifying questions um and then proceed with the solution part okay okay um another thing i just want to input there is it helps to so it really depends on you know uh a candidate's response style like some candidate after some question like clarifying questions they'll immediately dive into writing the solution and then explain at the end um that could work um i think a much more effective way to respond to escrow question is once you ask the clarifying questions um jot down the logic so you kind of did it for the case part but then you didn't really do it for the other steps that are required you know basically calculating the um the average and maximum yeah i just wouldn't my word i should have it in it yeah yeah um it just it just helps to just like actually note it on a quarter pad um or whatever um you know um ide they they have you perform sql and just just in general you know just clearly like state things um and then proceed and and that would provide a much more much a better response than just verbally kind of outlining things and then immediately diving into solution
- **Labels:** `SQL` · type=hard · stage=technical_coding

### 2. `16:23` — Product Sense

- **Проверка главы:** ✅ у маркера 2 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #2 | +10 с | `Product Metrics` | how would you measure the health of uber so |
| #3 | +45 с | `Product Metrics` | what are your thoughts on that what do you think is a difference or th… |

#### Item #2

- **Question** (`16:33`): how would you measure the health of uber so
- **Candidate answer** (`16:48`): so um in this case obviously i would um first measure the health of uber so in terms of health do you mean by the number of uh in terms of success do you mean
- **Reference answer:** —
- **Interviewer feedback** (`16:39`): the health of uber did you write the question summer okay here yep so okay
- **Labels:** `Product Metrics` · type=hard · stage=technical_case

#### Item #3

- **Question** (`17:08`): what are your thoughts on that what do you think is a difference or the similarity between health versus success
- **Candidate answer** (`17:16`): so um health can refer to my assumption is that um as the goal for uber is that um transpos to make transportation reliable as a running water and everyone everywhere for ev everyone uh it would definitely in terms of health focus on uh two domains one the the part of the customer and the driver so in terms of measuring the over of our health of the experience within the customer domain and the driver domain so um in terms of that um as i mentioned that the business goal is to create a reliable experience for both of them so do you want me to jot down and go specific within one domain within one of these or as an overall whole
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

## Speaker boundary check (heuristic)

Automatic role check (no diarization): Q/A duplicates, truncated questions, candidate speech in question field, interviewer lines inside answer.

- **Item #4:** текст `interviewer_feedback` повторяется в `candidate_answer` (или наоборот). Оставьте реплику только в одном поле.
- **Item #9:** начало `interviewer_feedback` уже есть в `candidate_answer` («because we re talking about like»…). Перенесите в feedback только новую речь интервьюера.
- **Item #11:** слишком короткий обрывок в `interviewer_question` — на шаге 2 склейте соседние реплики интервьюера в транскрипте; не парафразируйте по video.md.


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
      "chapter_time": "00:01:45",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:16:23",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
