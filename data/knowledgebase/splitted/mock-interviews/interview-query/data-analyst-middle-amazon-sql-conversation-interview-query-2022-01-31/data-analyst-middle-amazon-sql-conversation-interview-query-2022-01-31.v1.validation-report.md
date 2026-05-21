# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interview-query/data-analyst-middle-amazon-sql-conversation-interview-query-2022-01-31`
- **Режим:** `split_and_validate` · **source_id:** `data_analyst_middle_amazon_sql_conversation_interview_query_2022_01_31`
- **Старт:** 2026-05-20 20:17:38 +0200 · **Обновлено:** 2026-05-20 20:29:12 +0200
- **Длительность прогона (стена):** 11 мин 34 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 2 мин 17 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ✅ все зафиксированные шаги завершены
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interview-query/data-analyst-middle-amazon-sql-conversation-interview-query-2022-01-31/data-analyst-middle-amazon-sql-conversation-interview-query-2022-01-31.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 2 | 2. Извлечение Q&A (LLM) | да | claude-sonnet-4-6 | 1 мин 30 с | ✅ |
| 3 | 3. Excel | нет | — | 1 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 1 с | ✅ |
| 5 | 5. Семантика глав (LLM) | да | claude-sonnet-4-6 | 45 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interview-query/data-analyst-middle-amazon-sql-conversation-interview-query-2022-01-31/data-analyst-middle-amazon-sql-conversation-interview-query-2022-01-31.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interview-query/data-analyst-middle-amazon-sql-conversation-interview-query-2022-01-31/data-analyst-middle-amazon-sql-conversation-interview-query-2022-01-31.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interview-query/data-analyst-middle-amazon-sql-conversation-interview-query-2022-01-31/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 5 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (3/3), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 4 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/interview-query/data-analyst-middle-amazon-sql-conversation-interview-query-2022-01-31/data-analyst-middle-amazon-sql-conversation-interview-query-2022-01-31.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 5
- **`source_id`:** `data_analyst_middle_amazon_sql_conversation_interview_query_2022_01_31`
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
| 1 | `01:15` | What's the distribution look like… | — | recognized (2 Q&A) | #1, #2 | `SQL` | ⏳ | — |
| 2 | `03:00` | Write a query to get the distribu… | — | recognized (1 Q&A) | #3 | `SQL` | ⏳ | — |
| 3 | `04:34` | Calculating the frequency | — | recognized (1 Q&A) | #4 | `SQL` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `01:15` — What's the distribution look like for all conversations?

- **Проверка главы:** ✅ у маркера 2 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | -74 с | `SQL` | so we're given two tables that represent messages uh by uh two users u… |
| #2 | +0 с | `SQL` | and then the second question is like what do you think the distributio… |

#### Item #1

- **Question** (`00:01`): so we're given two tables that represent messages uh by uh two users um on like a chat app so first question is what are some insights that could be derived from this table even before you start writing a query
- **Candidate answer** (`00:19`): um i think you could figure out what's um how many interactions people are actually making with each other right you could you could have an app say if no one uses it right so first thing you want to understand is like how many interactions are happening so how many what's the network how many people are connected to this user right or the number of people they interact with and then is the volume also like how many messages are going right whether it's just a good morning messages to 10 people or is it like actual conversations happening so i guess those are what are what i would be interested in and understanding is like okay what's the what's the network how many user and what's the volume of the interaction
- **Reference answer:** —
- **Interviewer feedback** (`01:05`): gotcha okay yeah that definitely makes sense especially if you're building like a messaging app and you're trying to figure out exactly the common kind of use cases here
- **Labels:** `SQL` · type=soft · stage=technical_qna

#### Item #2
- **⚠️ границы реплик:** текст `interviewer_feedback` повторяется в `candidate_answer` (или наоборот). Оставьте реплику только в одном поле.

- **Question** (`01:15`): and then the second question is like what do you think the distribution of the number of conversations created by each user per day would even look like so pretend that now or an actual like app on facebook let's say it's messenger right and so if you had a guess on the distribution what would you say it would look like
- **Candidate answer** (`01:32`): first i'll have to know how many introverts and extroverts exist on facebook okay um okay now i think on an average it's hard to guesstimate says you'll talk to less than um definitely less than 10 or 10 people per day on an average probably less than three three to six i guess should be like how many people you interact with on an average again personality depends right so that that's uh given even that is a facebook example you could also have no a lot of connections but you hardly you know uh like i am a facebook user you will not see a message more than happy birthday so yeah so that that could be one thing also you know some people i don't know the word there is a term for it where people just try the app and then stop using it i'm one of those users so i try stuff and then just stop using it so there's a turn right yeah yeah so that's something which we should be interested in like say from some what's what's the lifespan of an active user wow i think that that might be interesting
- **Reference answer:** —
- **Interviewer feedback** (`02:58`): okay
- **Labels:** `SQL` · type=hard · stage=technical_qna

### 2. `03:00` — Write a query to get the distribution

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #3 | +0 с | `SQL` | okay and so now we'll get to the actual sql writing part but let's say… |

#### Item #3

- **Question** (`03:00`): okay and so now we'll get to the actual sql writing part but let's say we want to get the distribution of the number of conversations uh created by each user uh each day uh for the year of 2020. so how are we going to write this query
- **Candidate answer** (`03:13`): okay in the base we have only one table so there there's nothing to join on so let's say it's an extra from messages okay so what we are trying to do is for let's say we have we have to understand it from uh user point of view right so say i am user one right and then i want to see how many people i interact with so count user 2 as number of interactions now my interaction definition is how many people i touch can you think of a better word uh no i think that makes sense i think conversations is like the one that we're using okay so let's stick to conversation but uh the number of messages are immaterial it's only how many miss you know how many conversations were initiated so if we do something like this this this tells us you know how many what did i do playground thought message yes oh okay thanks okay so this is only going to tell you how many how many people have we interacted with uh and let's just see how many interactions there has been now this is irrespective of date so the most one person has interacted to 44 people now this is irrespective of date but the question says per day so we are just going to group it by day to get at our daily level so we'll just say i did and this tells you long order by three descending so i'm i'm just saying order by three descending which means take the third column and just order it by three sorry uh order it in the descending order so we can say that user one one the state has had three conversations while previously we saw that in general someone had contacted someone 40 plus times right
- **Reference answer:** —
- **Interviewer feedback** (`05:41`): make sense so far yep okay good so now what we are trying to understand now at this point we have at a user at a day level how many conversations there has been okay
- **Labels:** `SQL` · type=hard · stage=technical_coding

### 3. `04:34` — Calculating the frequency

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #4 | +82 с | `SQL` | now the question is saying give us a distribution which is like basica… |

#### Item #4

- **Question** (`05:56`): now the question is saying give us a distribution which is like basically we need to count this in a frequency fashion so we just need to see how many times three happened how many times two happened how many times you know one happened
- **Candidate answer** (`06:11`): okay so this should be simple we take this data this is number of conversations as our main thing and then we just give count how many time that happened as let's call that column frequency let's call this something meaningful so let's call it number of conversations per day you don't have to but i just prefer having something meaningful of as a table alias and then you just group by number of conversations and okay this is overall okay so essentially there has there we have three thousand seven it's basically very skewed right essentially one person is only contacting one person on each day okay and then the question says hey filter on here 2020 so let's query uh filter on the base table so we just i'm not sure if there's a year function there or not let's let's recap once write a query to get the distribution of the number of conversations created by each user per day in the year 2020 okay so year 2020 filter we put in here and then we said we we literally just converted this into table right so we said number of conversations per day per user and then we went to the first part which is how to get the distribution just like count it so basically basically read the question in the reverse order
- **Reference answer:** —
- **Interviewer feedback** (`08:04`): what do you think yeah i think that's right
- **Labels:** `SQL` · type=hard · stage=technical_coding

## Speaker boundary check (heuristic)

Automatic role check (no diarization): Q/A duplicates, truncated questions, candidate speech in question field, interviewer lines inside answer.

- **Item #2:** текст `interviewer_feedback` повторяется в `candidate_answer` (или наоборот). Оставьте реплику только в одном поле.


## Check 3. Semantic field alignment per chapter (step 5, LLM)

The Cursor agent (same as step 2) reviews **extracted** Q&A: field timestamps vs chapter windows and whether texts match chapter titles and labels (`question_topic`, `question_type`). Does not change the overall verdict.


- **Статус:** ✅ все 4 глав без замечаний
- **Тайм-коды полей:** 4/4 ок · **Смысл/метки:** 4/4 ок


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
    },
    {
      "chapter_time": "00:01:15",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:03:00",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:04:34",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
