# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12`
- **Режим:** `split_and_validate` · **source_id:** `ml_engineer_senior_meta_fraud_scam_interviewing_io_2025_08_12`
- **Старт:** 2026-05-20 21:18:05 +0200 · **Обновлено:** 2026-05-20 21:31:15 +0200
- **Длительность прогона (стена):** 13 мин 10 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 2 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ⚠️ неполный журнал (проверьте pipeline-log)
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 3 | 3. Excel | нет | — | 1 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 1 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 12 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (2/2), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 6 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 12
- **`source_id`:** `ml_engineer_senior_meta_fraud_scam_interviewing_io_2025_08_12`
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
| 1 | `00:00:30` | System design prompt: ML model to… | — | recognized (1 Q&A) | #1 | `Communication` | ✅ | — |
| 2 | `00:36:00` | Modeling strategy, focal loss, an… | — | recognized (1 Q&A) | #4 | `ML` | ✅ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `00:00:30` — System design prompt: ML model to detect scam content

- **Проверка главы:** ✅ у маркера 1 Q&A · ✅ по смыслу и тайм-кодам полей всё сходится (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | +21 с | `Communication` | This will be a machine learning system design interview. Um the way ge… |

#### Item #1

- **Question** (`00:51`): This will be a machine learning system design interview. Um the way generally uh it works is that I want to know a little bit more about you. Uh what's your background? Um and if you have any interviews coming up um and what companies might they be uh so I might be able to tailor um my feedback accordingly. Um and generally the system design part lasts around 40 45 minutes. Um and I can do some feedback post uh on that. Um or if you want um some people like to get feedback as we go. So um so yeah
- **Candidate answer** (`01:38`): um yeah I'll give you a quick background. I um I have a uh PhD in physics. I graduated about three years ago and I have my on-site with Meta next Monday. Uh so that's what things are looking like. As for the feedback,
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Communication` · type=soft · stage=fit_hr

### 2. `00:36:00` — Modeling strategy, focal loss, and label bias

- **Проверка главы:** ✅ у маркера 1 Q&A · ✅ по смыслу и тайм-кодам полей всё сходится (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #4 | -54 с | `ML` | Um yeah. Yeah, I just wanted to know like um what what are the inputs … |

#### Item #4

- **Question** (`35:06`): Um yeah. Yeah, I just wanted to know like um what what are the inputs to this
- **Candidate answer** (`35:13`): Oh yeah, sorry. Sorry. Yeah, I guess it it could come from there. Uh the user features. Sorry, I wasn't clear about that. The post features and then the user post interaction features will be the the input to the model. Um and this will just learn some kind of embedding. And um from here I think kind of uh uh maybe the best way is to have do multitask where you have you know some kind of um you know head for each um kind of scam you know whether it's crypto scam, cash app scam, you know um whatever uh you know cash uh bank related, right? And um so you feed all these features uh feed these features to to each of these models. Um and then um so each class, let's talk about how to train it. So you're going to have some uh a sigmoid activation at the end. And then for the loss function could use something just um since this each one of these is a binary classifier detecting um you could use something like binary cross entropy or you know normalized cross entropy which is just binary cross entropy dividing by the the average. Um but there is a class imbalance. Um, so there's a few different ways we can handle it here. So for the imbalance, you can use um class weights. So like you said, 2% of the post will be will be bad. So you could use class weights, you could win the threshold. Um, but I think maybe a better option at this stage would be to use a the focal loss um to handle the the the class imbalance. And you you you apply the same procedure across them all. And um then at the end the the the final loss is just the the sum of the the losses from before. And um yeah so the inputs will be you know like uh the the what I described earlier and then the outputs will be the the label for each one. It'll be a vector of like 1 1 0 or 1 0 1 0 0 1 so on so forth. Um and then probably you know you standard things like ru activation, dropout regularization um things like that. So the class imbalance um we addressed um before I forget let me write this down. Uh actually maybe I'll just bring up now. Yeah, there there is going to be some kind of label bias. Um so from what I've seen this is actually a a really hard problem. you know, if you have three different interviewers or uh not interviewers, three different people label label something, they might um well, actually, in the case of scans, I think it should probably maybe it wouldn't be in any case, maybe I'll come back to that. Um actually, yeah, like talk about that a little bit. So, um, so you're talking about label bias where there's multiple people who might, uh, label the same content differently.
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `ML` · type=hard · stage=system_design


## Check 3. Semantic field alignment per chapter (step 5, LLM)

The Cursor agent (same as step 2) reviews **extracted** Q&A: field timestamps vs chapter windows and whether texts match chapter titles and labels (`question_topic`, `question_type`). Does not change the overall verdict.


- **Статус:** ✅ все 6 глав без замечаний
- **Тайм-коды полей:** 6/6 ок · **Смысл/метки:** 6/6 ок


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
      "chapter_time": "00:00:30",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:13:00",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:36:00",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:48:00",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:51:00",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "01:07:00",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
