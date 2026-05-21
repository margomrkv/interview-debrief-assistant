# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/interview-query/data-scientist-senior-dropbox-interview-query-2021-07-28`
- **Режим:** `split_and_validate` · **source_id:** `data_scientist_senior_dropbox_interview_query_2021_07_28`
- **Старт:** 2026-05-20 21:18:02 +0200 · **Обновлено:** 2026-05-20 21:30:22 +0200
- **Длительность прогона (стена):** 12 мин 20 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 3 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ⚠️ неполный журнал (проверьте pipeline-log)
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interview-query/data-scientist-senior-dropbox-interview-query-2021-07-28/data-scientist-senior-dropbox-interview-query-2021-07-28.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 3 | 3. Excel | нет | — | 1 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 2 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interview-query/data-scientist-senior-dropbox-interview-query-2021-07-28/data-scientist-senior-dropbox-interview-query-2021-07-28.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interview-query/data-scientist-senior-dropbox-interview-query-2021-07-28/data-scientist-senior-dropbox-interview-query-2021-07-28.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interview-query/data-scientist-senior-dropbox-interview-query-2021-07-28/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 6 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (1/1), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 3 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/interview-query/data-scientist-senior-dropbox-interview-query-2021-07-28/data-scientist-senior-dropbox-interview-query-2021-07-28.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 6
- **`source_id`:** `data_scientist_senior_dropbox_interview_query_2021_07_28`
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
| 1 | `00:00` | Trash Folder Logic Question | — | recognized (1 Q&A) | #1 | `Product Metrics` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `00:00` — Trash Folder Logic Question

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | +8 с | `Product Metrics` | okay so let's say that dropbox wants to change the logic of the trash … |

#### Item #1

- **Question** (`00:08`): okay so let's say that dropbox wants to change the logic of the trash folder from never permanently deleting anything in the trash to automatically deleting items after 30 days how would you look into the data and validate if this was a good idea or not
- **Candidate answer** (`00:24`): okay so we want to take a look at the logic of the trash folder so currently we are never deleting items in the trash folder but we are exploring whether we want to implement a new feature that would automatically delete items in the trash after 30 days is that correct okay let me take a moment to think about what structure i want to use to approach this problem the approach that i want to take is first thinking about why we might want to implement this new feature and kind of tying it back to the larger strategy and mission of the company thinking about our users and what their pain points are and then establishing a hypothesis and some metrics that i would want to dive deeper into to validate or invalidate that hypothesis okay so you know thinking back to the broader dropbox mission you know we are aiming to be the one place our users use to keep their life organized and keep work moving and so you know with all of the files that users are uploading and editing in dropbox um there's bound to be a lot of files that get moved to the trash as well um and so i think that um you know as our platform scales and grows this is bound to be a bigger problem especially if we're never deleting anything um and just i think this kind of string could potentially have performance um implementations and kind of hinder our effect to kind of provide a very speedy and quick uh experience for our customers so i would want to um so i'm going to take a moment now to kind of think about our users and their pain points around this problem and so when i think about our users and their behavior and dropbox i wanted to kind of think about why do users move things to the trash folder and so um i think that there are kind of a few different reasons why a user might move something into the trash folder so one it might be um they have uploaded a new version of something and so they might move the old version of that document into the trash um the second one is they might have uploaded a duplicate of something and so um instead of keeping both things and taking up extra space in their dropbox account they'll move the duplicate into the trash and then the third reason that i can think of is users you know with the current behavior of never deleting anything in the trash some users might kind of use that trash folder as an archive because they know that you know other items that they don't necessarily need on a day-to-day basis will not go away and stay in that folder and so um i would kind of think that most people are moving files to trash that they don't need anymore so that's kind of my hypothesis and so i'm going to take a moment now and kind of think about some metrics and that i would want to take a look at to validate whether or not that is true so i do have a clarifying question for you um so just to understand this a little better do items in a user's trash folder account against their storage limits for their dropbox account okay got it sounds good and are able are users able to only so users are only able to see the items in their trash can and the only action they would take on it is to restore it if they wanted to kind of open that file back backup is that correct got it sounds good thank you um so some things that i would want to take a look at in answering the question you know are in answering my hypothesis you know are users moving files to trash that they don't actually need anymore um so i would want to take a look at how often do users actually go into their trash folder um if we find that users are going in there pretty often then i might make the case that they're they might be using it more as an archive rather than you know a trash can where they just throw something and kind of forget about it um i would also want to take a look at kind of along those lines how often are items in the trash can uh kind of uh i think the only action we said you can take on it is restoring it so how often are items in the trash restored and then i would also uh so kind of along kind of explaining that one a little further um you know if they are things such as you know different versions or duplicates where users don't really need those items anymore because they either have another copy of it or they have the most recent copy of it then i would expect that users aren't really restoring items from the trashcan very frequently um and then i would also want to take a look at just kind of some general things you know the average amount of items that users have in their trash and kind of taking a look at on average how much file space are these things taking up i think that knowing that the trash doesn't count against their storage limits it could be very possible that users are using it more as an archive so i'd be interested in seeing you know just the sheer amount of things in there um and so those are some of the items that i would want to take a look at in order to kind of proceed in understanding whether or not users are moving items to the trash that they don't actually need anymore
- **Reference answer:** —
- **Interviewer feedback** (`00:44`): yep okay sounds good okay sounds good um yeah so i would say that it doesn't count against their storage limit right because it's in the trash right okay yeah readily access it unless they then um let's say they uh they like repurpose it back into their regular uh storage yes okay
- **Labels:** `Product Metrics` · type=hard · stage=technical_case

## Speaker boundary check (heuristic)

Automatic role check (no diarization): Q/A duplicates, truncated questions, candidate speech in question field, interviewer lines inside answer.

- **Item #3:** текст `interviewer_feedback` повторяется в `candidate_answer` (или наоборот). Оставьте реплику только в одном поле.
- **Item #6:** слишком короткий обрывок в `interviewer_question` — на шаге 2 склейте соседние реплики интервьюера в транскрипте; не парафразируйте по video.md.


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
      "chapter_time": "00:00:00",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:00:52",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:18:26",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
