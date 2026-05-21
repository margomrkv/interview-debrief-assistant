# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/datainterview/data-scientist-senior-facebook-churn-sql-datainterview-2021-09-30/`
- **Режим:** `split_and_validate` · **source_id:** `data_scientist_senior_facebook_churn_sql_datainterview_2021_09_30`
- **Старт:** 2026-05-20 21:05:21 +0200 · **Обновлено:** 2026-05-20 21:12:39 +0200
- **Длительность прогона (стена):** 7 мин 18 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 3 мин 2 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ✅ все зафиксированные шаги завершены
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-churn-sql-datainterview-2021-09-30/data-scientist-senior-facebook-churn-sql-datainterview-2021-09-30.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 2 | 2. Извлечение Q&A (LLM) | да | claude-sonnet-4-6 | 3 мин | ✅ |
| 3 | 3. Excel | нет | — | 1 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 1 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-churn-sql-datainterview-2021-09-30/data-scientist-senior-facebook-churn-sql-datainterview-2021-09-30.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-churn-sql-datainterview-2021-09-30/data-scientist-senior-facebook-churn-sql-datainterview-2021-09-30.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/datainterview/data-scientist-senior-facebook-churn-sql-datainterview-2021-09-30/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 6 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (2/2), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 2 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-churn-sql-datainterview-2021-09-30/data-scientist-senior-facebook-churn-sql-datainterview-2021-09-30.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 6
- **`source_id`:** `data_scientist_senior_facebook_churn_sql_datainterview_2021_09_30`
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
| 1 | `01:20` | How would you measure user churn … | — | recognized (1 Q&A) | #1 | `Product Metrics` | ⏳ | — |
| 2 | `08:05` | Choose one primary metric | — | recognized (2 Q&A) | #2, #3 | `Product Metrics` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `01:20` — How would you measure user churn on Instagram?

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | -2 с | `Product Metrics` | all right so how would you measure user turn on instagram |

#### Item #1

- **Question** (`01:18`): all right so how would you measure user turn on instagram
- **Candidate answer** (`01:23`): um okay let's see so um i think first thing is a couple of cliff questions i want to clarify before we move forward um so user churn so user return usually um just means that it's the way i think about it is inactive users so do you want me to kind of define more concrete time frame for that inactivity on my own and then the type of actions that they take so i would actually honestly prefer yeah of course and then um so instagram it's pretty broad um you know there are even multiple offerings within instagram for example you have the regular post you have stories you have um explore page and then now you have a shopping tab is there any subsection within instagram that you want me to focus on general user okay yeah yeah um okay so and is there can i know who um like who the stakeholder is uh are interested in this uh knowing this measurement okay so in this case i think even before we um like uh define a very quantitative and measurable metric on this i'll kind of back up a little bit and then think about instagram as a platform so you know it's primarily a photo sharing app but it has evolved into i think a lot more than just photo sharing and generally a very useful way for people to connect with each other and then it's also um i think it's unique in a way that the user demographic is quite different from facebook um as a whole and yeah so it's a pretty important business to instagram um so in terms of if executives want to know user trend i think they primarily want to know i would say i would guess there are two ways you can think about it right um so maybe there is just a decrease in the number of active users and then we can define the whether how we define active later but then there's also i also want to think about kind of engagement drop so maybe the users are kind of just checking a lot less frequently so um they don't necessarily turn all the way like they're not deleting their account for example but then maybe their time now are getting pulled to other uh competitors so like you mentioned like snapchat um tick tock that sort of thing so i would also almost in a way to kind of think about that as a user trend in a way if the engagement time is degrees a lot so i would say right now um let me try to kind of type out some notes so one is totally users and then two is then dramatic drop in so which of these do you think do you want me to focus on more i think those are very important and they kind of answer different questions for um so yeah so let's let's now talk about more details on how to define it so totally active users i would think about this i would want to define some kind of time frame for someone to be classified as inactive okay so you can think about it as well there are many ways right so i can think about how many times they log in say if they don't log in in a sunday period we can consider a return or we could also consider that maybe you want an even more fine grain level where they kind of log in but then they're not i guess it just relates to the second point more so they log in but they're not doing any engagement and by engagement i mean they're not liking any posts they're not viewing any stories they're not posting they're not commenting they're not direct messaging any users so let's see for the first case i can i think the way i'll define it would be say within a seven day period say um lot number of users who have not logged in now some day period um and then so that's a total number of um of user turn um in that seven-day period um and then for engagement i would say also within some day period for user engagement i would say for example i guess for this one i would define a rate so total number of unique user and then which number of so this is kind of how i would uh imagine engagement so within a seven day period so what is the number average number of engagement actions so engagement actions here i'm defining as liking commenting posting or viewing stories or or making stories or making direct messages so any kind of action other than just log in onto the platform take it during the seven days and then divide by the total number in the user so that will kind of give you average rate and you can watch how that rate changed
- **Reference answer:** —
- **Interviewer feedback** (`01:49`): um perhaps just think about the initial kind of approach and then maybe kind of work your way around this instead of okay you know telling you this is what you should be looking at first uh you know what let's just say general users yeah so i would say maybe like executives people who are on the higher up on the instagram chain okay when you think about this for a second first of all you have to have a way to measure that before you can prioritize in the second one right
- **Labels:** `Product Metrics` · type=hard · stage=technical_case

### 2. `08:05` — Choose one primary metric

- **Проверка главы:** ✅ у маркера 2 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #2 | -36 с | `Product Metrics` | all right so i have a couple follow-up questions starting with the sur… |
| #3 | +19 с | `Product Metrics` | but if you had to basically just pick one as your definition for churn… |

#### Item #2

- **Question** (`07:29`): all right so i have a couple follow-up questions starting with the sure so why seven days
- **Candidate answer** (`07:34`): so um yeah the seventh day for me is to kind of deal with things that are for example day of the week effect so for example i would imagine that maybe people would check um instagram less on tuesday than say on friday saturday on like for example on the weekend so i think kind of give you that seven day period smooth out some of this pure uh period periodic nature of uh instagram engagement
- **Reference answer:** —
- **Interviewer feedback** (`08:01`): okay got it um and i noticed that you know you've essentially kind of subdivided a turn to in terms of two different buckets right
- **Labels:** `Product Metrics` · type=hard · stage=technical_qna

#### Item #3

- **Question** (`08:24`): but if you had to basically just pick one as your definition for churn which one you actually pick
- **Candidate answer** (`08:30`): yeah especially for uh the business holder so you know in the beginning i asked who like the executives are the ones that are interested in this right and i think they this is much more important than drawing a drop in user engagement so the reason being that for example how instagram as a platform makes money is through advertising right so you need the users to actually be using the platform instead of you know kind of just briefly logging in and then be on the platform then they're not going to see ads as often for example right and they're not using the if they're not engaging with the app long term um they're they probably aren't it's probably an indicator that they're not having a good time so they're not having a good user experience with the application um so this i think serves as a very very important kind of um indicator so you can kind of watch out for uh things that may go wrong before they kind of catastrophically go wrong so to me like totally active users if they're not even logging in that's true it's very hard to pull the users back right instead of uh versus user who are right now they're on the platform by just not using your platform as much then maybe uh if we um kind of monitor this metric then we can inform the business holders that okay we're seeing this drop in user engagement then they can kind of devise new um strategies to pull it back so i think the second one is a lot more important in terms of defining user trend
- **Reference answer:** —
- **Interviewer feedback** (`09:57`): okay got it
- **Labels:** `Product Metrics` · type=hard · stage=technical_qna


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
      "chapter_time": "00:01:20",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:08:05",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
