# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/interviewing-io/data-scientist-middle-google-data-wrangling-interviewing-io-2020-04-28`
- **Режим:** `split_and_validate` · **source_id:** `data_scientist_middle_google_data_wrangling_interviewing_io_2020_04_28`
- **Старт:** 2026-05-20 21:18:05 +0200 · **Обновлено:** 2026-05-20 21:32:32 +0200
- **Длительность прогона (стена):** 14 мин 27 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 2 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ⚠️ неполный журнал (проверьте pipeline-log)
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interviewing-io/data-scientist-middle-google-data-wrangling-interviewing-io-2020-04-28/data-scientist-middle-google-data-wrangling-interviewing-io-2020-04-28.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 3 | 3. Excel | нет | — | 1 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 1 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interviewing-io/data-scientist-middle-google-data-wrangling-interviewing-io-2020-04-28/data-scientist-middle-google-data-wrangling-interviewing-io-2020-04-28.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interviewing-io/data-scientist-middle-google-data-wrangling-interviewing-io-2020-04-28/data-scientist-middle-google-data-wrangling-interviewing-io-2020-04-28.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interviewing-io/data-scientist-middle-google-data-wrangling-interviewing-io-2020-04-28/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 17 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (1/1), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 1 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/interviewing-io/data-scientist-middle-google-data-wrangling-interviewing-io-2020-04-28/data-scientist-middle-google-data-wrangling-interviewing-io-2020-04-28.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 17
- **`source_id`:** `data_scientist_middle_google_data_wrangling_interviewing_io_2020_04_28`
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
| 1 | `00:00` | Google data wrangling technical i… | — | recognized (3 Q&A) | #1, #2, #3 | `Communication`, `Data Modeling` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `00:00` — Google data wrangling technical interview

- **Проверка главы:** ✅ у маркера 3 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | +14 с | `Communication` | just really quick question about your background like what this isn't … |
| #2 | +48 с | `Communication` | last quick question do you understand the the fundamentals of baseball… |
| #3 | +88 с | `Data Modeling` | basically what what what's happened to set the tone so you've just sta… |

#### Item #1

- **Question** (`00:14`): just really quick question about your background like what this isn't really too much the the question I have is into heavy in programming but just what kind of programming languages are you comfortable with
- **Candidate answer** (`00:25`): so I'm like an idea uh-uh Python would be my favorite a little bit of JavaScript
- **Reference answer:** —
- **Interviewer feedback** (`00:31`): okay perfect
- **Labels:** `Communication` · type=soft · stage=fit_hr

#### Item #2

- **Question** (`00:48`): last quick question do you understand the the fundamentals of baseball like the mechanics of innings and batters and pictures of ah um problem gonna goes no
- **Candidate answer** (`01:02`): no okay yeah I know very very little bit baseball I depend how fundamental I know there's like nine innings okay there's four bases and stuff like that
- **Reference answer:** —
- **Interviewer feedback** (`01:15`): okay I think that's all that's all we need we don't certainly we're not we're not going to get too too crazy into it but um yeah if you know that there's nine innings and four bases that's that's all we need um so
- **Labels:** `Communication` · type=soft · stage=fit_hr

#### Item #3

- **Question** (`01:28`): basically what what what's happened to set the tone so you've just started to work at a new startup that's called internet baseball database and their customers have started to complain that there's the features aren't very good and that it's the site is really slow so you've been you've been told to come on in and kind of help clean everything up so the idea is that this company gets a regular data feed from from major league baseball that has data that they're going to want to display on their site and you can you read what I'm what I'm typing here is like
- **Candidate answer** (`02:22`): yep I see
- **Reference answer:** —
- **Interviewer feedback** (`02:27`): hi yeah okay so basically what they are sending every day is an update of what happened in each of the the baseball games so it's a very simple text file with tabs and it's going to have just column fields and it's going to say we have the date that the game was played the home team CoA team and every column actually is going to be an at-bat so it's going to have the batter and right now we'll just say the results like the the outcome so an example here might be like today's game would be on 26 the home team was giants and new a-team was a's and batter was cocoa Chris and the outcome was that he got a single so the outcomes will be a like s is a single which counts as a hit D is a double which is a hit - a triple its H home run the hit and then there's also uh K is a strikeout it's just not a hit which is no hit and F would be a flyout something like that so there's there's sort of like a little for what happened and what what what the site currently how it works is that you get this text file every day that contains all of these like lines and the owner of the sites is very paranoid so he doesn't want to put it into a database because he thinks the database people are out to get him so he stores it on the file system so he'll have sort of on the file system you'll see data and then he'll put the year and then he'll put the day and then he'll just have the date the data for that that day and and you yeah the other thing is that he he also is very paranoid and doesn't trust file system developer so he invented his own file system that's very inefficient and can only hold a thousand files in every directory so that's why you can't just put the date like this because at some point there'll be too many too many directories or files and into this directory so he has to kind of split it up this way and when someone comes to the site they can right now the only thing they can do is they can look up a certain date and look at all of the information for the games played on that day but he started to get some comments that wouldn't it be nice to look up other things so for example wouldn't it be great if you could just look up a particular player and see some of the stats for that player and it might imagine using this technique of storing the data that's a bit inefficient so your task in that sort of a larger overall task is to come up with a way given these constraints that you know you have to store the day on in sweat files in the file system and no more than a thousand for directory and that kind of thing
- **Labels:** `Data Modeling` · type=hard · stage=technical_case


## Check 3. Semantic field alignment per chapter (step 5, LLM)

The Cursor agent (same as step 2) reviews **extracted** Q&A: field timestamps vs chapter windows and whether texts match chapter titles and labels (`question_topic`, `question_type`). Does not change the overall verdict.


- **Статус:** ✅ все 1 глав без замечаний
- **Тайм-коды полей:** 1/1 ок · **Смысл/метки:** 1/1 ок


## Transcript spans without Q&A in JSON

Intervals in `timecodes.txt` not covered by any item span. Check for a missed question or service speech.

_No large uncovered spans (threshold: ≥25s, ≥4 timecoded lines)._


#### Короткие ответы кандидата (≤4 слов)

Проверьте по транскрипту: это **осмысленный** короткий ответ на вопрос, а не обрезанный span или пропуск речи кандидата.

| Item | Время | Ответ |
|------|-------|-------|
| #3 | 01:28 | yep I see |

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
