# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18`
- **Режим:** `split_and_validate` · **source_id:** `ml_engineer_senior_meta_illegal_items_interview_query_2022_01_18`
- **Старт:** 2026-05-20 21:18:04 +0200 · **Обновлено:** 2026-05-20 21:32:30 +0200
- **Длительность прогона (стена):** 14 мин 26 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 2 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ⚠️ неполный журнал (проверьте pipeline-log)
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 3 | 3. Excel | нет | — | 1 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 1 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
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
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 1 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 7
- **`source_id`:** `ml_engineer_senior_meta_illegal_items_interview_query_2022_01_18`
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
| 1 | `00:00` | Meta illegal items ML mock interview | — | recognized (2 Q&A) | #1, #2 | `ML` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `00:00` — Meta illegal items ML mock interview

- **Проверка главы:** ✅ у маркера 2 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | +0 с | `ML` | let's say that you are designing a marketplace for your website sellin… |
| #2 | +65 с | `ML` | so i guess reframe the question back to you but let's say that this is… |

#### Item #1

- **Question** (`00:00`): let's say that you are designing a marketplace for your website selling firearms is prohibited by your website's terms of service agreement not to mention the laws of your country to this end you want to create a system that can automatically detect if a listing on the marketplace is selling a gun how would you go about doing this
- **Candidate answer** (`00:14`): yeah it's a interesting question i'm curious about a few things here first i guess one thing i'm wondering about is like how if i was given this task like how is this working in kind of production you know the task is to automatically identify the listings what happens with those identifications do they go to a human who checks it or is it like immediately changes the website okay and then how would this fit in is the end of the line always going to be customer service or how would this fit in that pipeline you think
- **Reference answer:** —
- **Interviewer feedback** (`00:33`): yeah so let's say that the current setup is that it's all crowd source so let's say we have a flag and then a user can flag the listing if they see it's a gun or maybe someone who works in terms of like moderating the marketplace can also flag it and then it'll go to another internal let's say someone who works in customer support that can then remove the listing if they determine it as a gun and that's the only thing that kind of happens right now
- **Labels:** `ML` · type=hard · stage=technical_case

#### Item #2

- **Question** (`01:05`): so i guess reframe the question back to you but let's say that this is the current system right and i guess given the kind of context would you think that the goal is to first disable it when they're posting do you think we should be like detecting it afterwards after a few days and then sending it to customer support what part do you think
- **Candidate answer** (`01:27`): yeah so i guess yeah the reason i was asking that question i guess i could have said that too because if if customer service is is going to look at it afterwards which i think would probably be the better way to go to start but if they're doing it that way then that means that i really need to do a very good job of detecting all the possible firearm listings it's bad if i miss something that is a firearm but i miss it because at the end the customer service is going to look at it and so i'm assuming it'll be okay it might cost some money but it's probably going to be okay if i give it false positives like listings that aren't guns and then let the customer service deal with it but it seems like this pipeline would be very costly in that in the sense that you're maybe breaking laws of your country or your terms of service if you totally miss the listing and you have this uh false negative right
- **Reference answer:** —
- **Interviewer feedback** (`02:17`): yes so that's that's yeah so that's how i would think about it
- **Labels:** `ML` · type=hard · stage=technical_case


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
