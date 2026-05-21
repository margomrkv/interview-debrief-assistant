# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/interview-query/data-scientist-senior-linkedin-interview-query-2020-09-09`
- **Режим:** `split_and_validate` · **source_id:** `data_scientist_senior_linkedin_interview_query_2020_09_09`
- **Старт:** 2026-05-20 21:18:02 +0200 · **Обновлено:** 2026-05-20 21:30:27 +0200
- **Длительность прогона (стена):** 12 мин 25 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 3 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ⚠️ неполный журнал (проверьте pipeline-log)
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interview-query/data-scientist-senior-linkedin-interview-query-2020-09-09/data-scientist-senior-linkedin-interview-query-2020-09-09.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 3 | 3. Excel | нет | — | 2 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 1 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interview-query/data-scientist-senior-linkedin-interview-query-2020-09-09/data-scientist-senior-linkedin-interview-query-2020-09-09.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interview-query/data-scientist-senior-linkedin-interview-query-2020-09-09/data-scientist-senior-linkedin-interview-query-2020-09-09.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interview-query/data-scientist-senior-linkedin-interview-query-2020-09-09/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 7 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (1/1), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 3 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/interview-query/data-scientist-senior-linkedin-interview-query-2020-09-09/data-scientist-senior-linkedin-interview-query-2020-09-09.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 7
- **`source_id`:** `data_scientist_senior_linkedin_interview_query_2020_09_09`
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
| 1 | `02:00` | Newsfeed Ranking Question | — | recognized (2 Q&A) | #2, #3 | `ML`, `Product Metrics` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `02:00` — Newsfeed Ranking Question

- **Проверка главы:** ✅ у маркера 2 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #2 | -49 с | `ML` | i guess is there anything you could talk about about uh like machine l… |
| #3 | -8 с | `Product Metrics` | awesome so i guess for the first question i think it might be kind of … |

#### Item #2

- **Question** (`01:11`): i guess is there anything you could talk about about uh like machine learning at doordash uh in terms of the stuff that you've worked on that's uh been pretty cool or interesting
- **Candidate answer** (`01:21`): definitely so um yeah i was one of the first ml data science hires at doordash so i worked on a little bit of everything on all sides of the business i worked a little bit on our personalization recommendation algorithm helped work a bit on marketing segmentation and marketing attribution and i've also done some work on our pay model how do we optimally pay drivers and then uh recently i've been working a lot on demand forecasting
- **Reference answer:** —
- **Interviewer feedback** (`01:48`): gotcha cool yeah um
- **Labels:** `ML` · type=soft · stage=fit_hr

#### Item #3
- **⚠️ границы реплик:** текст `interviewer_feedback` повторяется в `candidate_answer` (или наоборот). Оставьте реплику только в одном поле.

- **Question** (`01:52`): awesome so i guess for the first question i think it might be kind of similar it's more machine learning based um and so let's say you work as like a data scientist on the uh linkedin um engagement team right um and let's say that we uh have like a obviously we have like a news feed ranking algorithm right so that when you log in uh you see like a general news feed of um stuff that might be interested to you so the first question is how would you actually measure the success of the news feed ranking out
- **Candidate answer** (`02:28`): okay taking some notes here yep definitely okay cool so i think before i start diving in i just want to make sure i really understood the problem uh i'm going to be a data i am a data scientist on linkedin's engagement team and we're working on the news feed ranking algorithm and then we want to measure the success of a new news feed algorithm and the first step will be to just kind of come up with some metrics that we think can evaluate how effective this news feed algorithm is am i getting it right cool okay cool so you mind if i take a second i'm just gonna kind of brainstorm to myself so then we can't walk through the solutions for sure okay cool so i think um just kind of preliminary i uh first couple things that i can think of related to engagement to on a news feed is um click-through rate so the likelihood of a user just clicking on a piece of content however i think a better measure on like how engaged and how relevant the content could be for a user is if they actually share content because that means that they're much more likely they like it enough to say hey i think this is valuable i think that you should also look at this as well and the third one i can think of is related to comments so um yeah comments is a huge indicator of how engaged they are and i think the next one is how many times they post as well it's a number of posts i think uh yeah so i would say those are the four different metric uh four different components that i might want to look at um it's still a little bit vague right now would you want me to break this down into more of a defined metric or uh do we want to keep uh moving moving forward
- **Reference answer:** —
- **Interviewer feedback** (`03:02`): yep
- **Labels:** `Product Metrics` · type=hard · stage=technical_case

## Speaker boundary check (heuristic)

Automatic role check (no diarization): Q/A duplicates, truncated questions, candidate speech in question field, interviewer lines inside answer.

- **Item #3:** текст `interviewer_feedback` повторяется в `candidate_answer` (или наоборот). Оставьте реплику только в одном поле.


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
      "chapter_time": "00:02:00",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:03:14",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:14:43",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
