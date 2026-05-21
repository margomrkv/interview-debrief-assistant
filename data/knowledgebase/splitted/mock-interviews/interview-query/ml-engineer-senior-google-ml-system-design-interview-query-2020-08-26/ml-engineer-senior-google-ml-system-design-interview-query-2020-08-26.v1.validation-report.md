# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26`
- **Режим:** `split_and_validate` · **source_id:** `ml_engineer_senior_google_ml_system_design_interview_query_2020_08_26`
- **Старт:** 2026-05-20 21:18:03 +0200 · **Обновлено:** 2026-05-20 21:30:43 +0200
- **Длительность прогона (стена):** 12 мин 40 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 4 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ⚠️ неполный журнал (проверьте pipeline-log)
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 3 | 3. Excel | нет | — | 2 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 2 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 12 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (3/3), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 3 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 12
- **`source_id`:** `ml_engineer_senior_google_ml_system_design_interview_query_2020_08_26`
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
| 1 | `00:55` | Youtube Recommendations Interview… | — | recognized (1 Q&A) | #1 | `ML` | ⏳ | — |
| 2 | `03:35` | Collaborative Filtering | — | recognized (1 Q&A) | #2 | `ML` | ⏳ | — |
| 3 | `10:50` | Cold Start Problem? | — | recognized (1 Q&A) | #6 | `ML` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `00:55` — Youtube Recommendations Interview Question

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | -4 с | `ML` | uh but uh the question is uh so let's say that you're basically a mach… |

#### Item #1

- **Question** (`00:51`): uh but uh the question is uh so let's say that you're basically a machine learning engineer um on youtube right and this is uh you're tasked with basically building the youtube uh video recommendation algorithm how would you go about and start like this uh process for building it
- **Candidate answer** (`01:12`): uh yeah so i do have the advantage of having heard this question before uh and thinking about it i think it's uh it's just such a huge scope i mean youtube with billions of videos billions of or millions of users and accounts um they certainly have a difficult task ahead of them how do i recommend the right video to the right user at the right time in the right context yes um and so i think there's like multiple approaches there's the idea of you know starting what if youtube weren't as big as it is right now and it started small and we had maybe 100 videos and 10 users and then how do we scale that up to the youtube of 2020 and i think another approach is like hey it's youtube 2020 and we need to build the recommendation engine from scratch to be able to work across the entire corpus of of content on youtube and i think both of those are worthy of discussing and maybe meet in the middle a little bit about the approaches here but i'm just going to kind of brainstorm the various ideas i have around this so initially if you want to do this on a small data set uh how would you recommend the right video to the right user well what you can do is you can start with uh just saying okay what do users initially think about the videos they've seen so you can see uh user a saw video number one and watched uh 100 of it a 15 minute video watched all of it and then user b also watched video number one and watched all of it okay so now we can maybe reason that user a and user b uh maybe have similar tastes and so that might be used to predict whether a video that user a watched uh perhaps video two uh watched in its entirety now youtube might recommend that video number two to user b because well we've determined that user b is similar to user a um by some model that i can get into in a bit and we've determined that user a likes video number two so let's recommend video number two to that paired user and similarly if a user doesn't like a video then another user similar to them we might not recommend that video to them
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `ML` · type=hard · stage=system_design

### 2. `03:35` — Collaborative Filtering

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #2 | -2 с | `ML` | so is this technique the uh the collaborative filtering technique wher… |

#### Item #2

- **Question** (`03:33`): so is this technique the uh the collaborative filtering technique where it's based on
- **Candidate answer** (`03:40`): exactly yeah general neighbors right and so the definition as i know it is that uh users who watch the same thing would likely uh like the similar types of movies and so or videos right so you recommend the same videos that they might have liked and then users who are inherently themselves the same like demographically or something might like the same videos as well right so it's based on activity and then also attributes is that exactly yeah uh yeah and you can take a number of features to put into that model of collaborative filtering user user collaborative filtering we could take the demographics of the user their age and locale we could also take what they what they've been watching and not only what they've been watching like historically did they like this video at some point in time but also waiting more heavily what they've seen recently and i've certainly noticed for myself if i'm watching a series of videos in one topic well guess what the next video recommends to me is gonna be along that topic and i'm sure there's other features going into that but i think it's for the most part uh comparing like for this you know fat corner of the recommendation system uh it's going to be comparing hey this user liked this other video and i like the same things this user does so let's recommend it to them
- **Reference answer:** —
- **Interviewer feedback** (`05:09`): gotcha um sorry this is on a small scale right and so uh this is like youtube when it's very beginning right and so
- **Labels:** `ML` · type=hard · stage=system_design

### 3. `10:50` — Cold Start Problem?

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #6 | +3 с | `ML` | um so we're assuming that there are now let's say uh multi like millio… |

#### Item #6

- **Question** (`10:53`): um so we're assuming that there are now let's say uh multi like millions of users right and then millions of videos now right um and so i guess within the frame of the scope is uh is this um potentially the problem for where a new user joins a platform and then sees like the youtube page where they recommended you uh that like eight byte two like kind of youtube panel of different videos you can select or is this more like uh you've watched a video and then you get recommended like another one that auto plays um immediately so i guess in terms of like figuring out the scope um i guess that's probably like first question is um uh which one does that formula kind of apply to or the matrix multiplication
- **Candidate answer** (`11:38`): yeah yeah uh it's gonna be more applicable to when you've already seen a video you just you've been using youtube for a while you're a user who has been and you have an established uh you know corpus of this is what these are the types of videos i like these are the types of videos i don't like don't interact with and therefore you're able to construct a not quite uni or a distinct 1d user vector so that way we can actually save time by mult by combining many users who have also spent a lot of time on youtube and now we're saying okay for user a do they like video x for user b do they like video y and doing all the same time the opposite side of that problem uh we got a bunch of new users and most of them don't have a lot of well they haven't generated the data for youtube youtube doesn't know quite yet what kind of videos they like that's i'd say a different kind of problem because then you don't have so much data so you could is recommend them videos that new users tend to like or you could just say hey these are the most popular videos across all of them that's maybe good enough um i think those are different approaches but they don't solve the same meat of the problem as what i'm suggesting of combining multiple users in multiple videos in order to amortize your time to come to perform one calculation it's a huge calculation you're multiplying some pretty big matrices um but you're saving time by not doing it one by one
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `ML` · type=hard · stage=system_design


## Check 3. Semantic field alignment per chapter (step 5, LLM)

The Cursor agent (same as step 2) reviews **extracted** Q&A: field timestamps vs chapter windows and whether texts match chapter titles and labels (`question_topic`, `question_type`). Does not change the overall verdict.


- **Статус:** ✅ все 3 глав без замечаний
- **Тайм-коды полей:** 3/3 ок · **Смысл/метки:** 3/3 ок


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
      "chapter_time": "00:00:55",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:03:35",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:10:50",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
