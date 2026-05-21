# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-instagram-reels-interviewing-io-2025-08-05`
- **Режим:** `split_and_validate` · **source_id:** `ml_engineer_senior_meta_instagram_reels_interviewing_io_2025_08_05`
- **Старт:** 2026-05-20 21:18:06 +0200 · **Обновлено:** 2026-05-20 21:31:20 +0200
- **Длительность прогона (стена):** 13 мин 14 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 2 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ⚠️ неполный журнал (проверьте pipeline-log)
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-instagram-reels-interviewing-io-2025-08-05/ml-engineer-senior-meta-instagram-reels-interviewing-io-2025-08-05.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 3 | 3. Excel | нет | — | 1 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 1 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-instagram-reels-interviewing-io-2025-08-05/ml-engineer-senior-meta-instagram-reels-interviewing-io-2025-08-05.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-instagram-reels-interviewing-io-2025-08-05/ml-engineer-senior-meta-instagram-reels-interviewing-io-2025-08-05.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-instagram-reels-interviewing-io-2025-08-05/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 20 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (4/4), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 7 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-instagram-reels-interviewing-io-2025-08-05/ml-engineer-senior-meta-instagram-reels-interviewing-io-2025-08-05.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 20
- **`source_id`:** `ml_engineer_senior_meta_instagram_reels_interviewing_io_2025_08_05`
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
| 1 | `00:00:53` | Problem presented: Instagram Reel… | — | recognized (1 Q&A) | #1 | `ML` | ✅ | — |
| 2 | `00:17:00` | Candidate defines ML framing and … | — | recognized (2 Q&A) | #8, #9 | `ML` | ✅ | — |
| 3 | `00:38:00` | Discussion of candidate generatio… | — | recognized (1 Q&A) | #18 | `ML` | ✅ | — |
| 4 | `00:45:00` | Interview ends and candidate self… | — | recognized (2 Q&A) | #19, #20 | `ML`, `Communication` | ✅ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `00:00:53` — Problem presented: Instagram Reels recommendation system

- **Проверка главы:** ✅ у маркера 1 Q&A · ✅ по смыслу и тайм-кодам полей всё сходится (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | -9 с | `ML` | So, I'll give you a highle problem statement and I want you to drive m… |

#### Item #1

- **Question** (`00:00:44`): So, I'll give you a highle problem statement and I want you to drive most of the discussion around the solution, but feel free to ask clarifying questions as required. So the system we'll be designing today is Instagram res. You might have used this product. It's a feed of short videos. So when you enter the app, there's a short video that's playing and then you can swipe up to see the next one and it's like an infinite scroll. Yeah. So over to you.
- **Candidate answer** (`00:01:16`): Okay, cool. Um so first I think um just so I uh like can frame the discussion a little bit and guide it uh I wanted to uh do a quick outline of the way I want to approach this problem. So first uh yeah I want to uh understand the constraints. Uh so then um I want to see how ML can help um maybe classify the problem. Um then uh talk about data um and feature engineering. Um how we'll train and uh well build a uh train set and uh you know train the model. talk about serving uh the uh you know quality or metrics, how do we know we're performing well? Um and then we can talk about any sort of deep dives. Um so that sound good?
- **Reference answer:** —
- **Interviewer feedback** (`00:02:32`): Yep. Cool. So um
- **Labels:** `ML` · type=hard · stage=system_design

### 2. `00:17:00` — Candidate defines ML framing and objective

- **Проверка главы:** ✅ у маркера 2 Q&A · ✅ по смыслу и тайм-кодам полей всё сходится (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #8 | -62 с | `ML` | uh sorry to interrupt you but before we jump into that maybe we should… |
| #9 | +42 с | `ML` | Yeah, that makes sense. Uh I want to understand how you define relevan… |

#### Item #8

- **Question** (`00:15:58`): uh sorry to interrupt you but before we jump into that maybe we should uh think about what is the output of the model and just the overall structure of the train data like what's the ML objective what's the label what's the training data format
- **Candidate answer** (`00:16:18`): sure sure u so I was going to do that after the the entities but we can maybe uh switch the order so um okay so if this is a ranking problem which it sounds like it is um we need to process whatever information that we have and output a ranked uh list of reels. So um there are several ways of doing this. Uh like the the classic one is you can for each um uh real uh and uh user pair you can assign a score um for uh relevance um or like the likelihood of seeing a thing, right? Um and essentially you can treat this as a uh like a binary classification problem like given input features and say history and and things like this uh what is the probability that uh the real is relevant and you kind of um then given a large group of reels that you could show that are on your platform uh you can um sort of uh rank them based on the score and show the most relevant things first. So that's one approach. Um another approach uh does that make sense?
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `ML` · type=hard · stage=system_design

#### Item #9

- **Question** (`00:17:42`): Yeah, that makes sense. Uh I want to understand how you define relevance here.
- **Candidate answer** (`00:17:48`): Sure. So uh relevance here is uh like if a uh user um say interacts with a post in in one of various ways. there's like um explicit and implicit feedback that we can get. Um for example, if they uh watch the um the real to completion, right? So that like you can you can treat this as um a probability like okay, a post is relevant. The one of the hypotheses is a post is relevant if a user when shown it will uh watch it to completion, right? So or like a large fraction of it. So we could treat this as a classification problem um where uh the person finished watching the reel. So another hypothesis is post is relevant if the user follows uh the the author of it or um you could also treat this as a uh like a regression problem like what fraction of the real um does the the user uh wash um as as a like a normalized time or maybe you can um treat this as a uh uh an ordinal regression problem where like you bin the durations and say you want to watch a large fraction of it. So like the probability that a person watches 5 minutes of a real or something or or some relevant time bins. Um the I mean each of these are are are viable. Um is there one that you would like to focus in particular or would you like me to choose one? Because I mean realistically
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `ML` · type=hard · stage=system_design

### 3. `00:38:00` — Discussion of candidate generation and ranking model

- **Проверка главы:** ✅ у маркера 1 Q&A · ✅ по смыслу и тайм-кодам полей всё сходится (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #18 | +4 с | `ML` | No, makes sense. Let's get into the next part which is the actual rank… |

#### Item #18
- **⚠️ границы реплик:** текст `interviewer_feedback` повторяется в `candidate_answer` (или наоборот). Оставьте реплику только в одном поле.

- **Question** (`00:38:04`): No, makes sense. Let's get into the next part which is the actual ranking system itself and you've sort of explained it a bit. So candidate selection ranking what model architectures would you choose for each stage?
- **Candidate answer** (`00:38:19`): Sure. So um I understood the difference in the features. Mhm. Uh but yeah let's talk about the model architecture. Sure. So um the in the in the candidate generation stage generally um well okay well generally these these days you can you can start with a simple model where uh you have um basically the the um some concatenated uh user features, right? You have your uh real features. Um you uh you do uh some um maybe relatively shallow uh neural network for processing uh the the features, right? And then uh you have a um like a similarity embedding where where you treat the um real features either directly as uh the video ID or uh you know you also process them in this kind of um in a separate embedding. um like this and then you uh do a uh product similarity. Um so like e uh real and then e user, right? And then you find similar features like this. That's if you do the the the contrast of learning case, right? So the other one we talked about is uh more for the ranking. So um uh so I guess here uh for the contrast of sorry before I go on to the ranking step the the the candidate generation step generally uh has um okay so you have users and reels that they interact so for each user you have some positive and negative examples for uh the reels that they've interacted as determined by the user reel interactions, right? Um, generally they have uh skipped a lot more um reels than uh they've watched. So you need to balance you need to watch um like the imbalance between um positive and negative interactions and you can do that with um basically negative sampling. you can um reweigh uh the positive and negative examples and then sort of train a model that way um to to train stably. That'll give you the ability to look up relevant reels for a given user based on their features at the initial stage. But you can also use other uh uristics to suggest things like um reels that are popular uh within a certain region or um you know like you're doing an advertisement, you want to uh show certain reels. Okay. So the uh for the for the ranking case, we specifically want to talk about um how likely they are to have a long um watch uh versus a skip, right? So we can watch the uh we can uh do a more advanced um sort of uh user features um where we uh um additionally have like um their history or embeddings of um reels they've watched in the session. something like this. Um and then we have a um uh a real uh like proposed reel. uh unlike the sort of the two tower architecture. Now we would um sort of have some shared uh shared and then or uh you know in the limiting case we could use a very simple model but um you have some set of um features or sorry some some set of um I don't know uh neural network layers that is shared that sort of uh produces these user features and or takes this uh user features uh at the ranking stage and the proposed reel for each element of of of the um list that we want to rank that we got from the candidate stage. And then we um so we had previously talked about uh multitask for now let's let's do a single task. Um we can um for one task uh stop for a single task we can talk about um the um um probability of uh positive uh interaction. So we treat this as a um a classification task, right? Uh and uh we train this as a u binary cross entropy um task. Um when we add additional tasks, we can have an uh sort of a task specific head for like um probability of um like or comment. Um and we we can uh then appropriately weigh the um you know we can have an objective that weighs these tasks and the overall um score of a reel for a given user based on their session uh would be given by some weighed um probability of these interactions. All right.
- **Reference answer:** —
- **Interviewer feedback** (`00:44:44`): All right.
- **Labels:** `ML` · type=hard · stage=system_design

### 4. `00:45:00` — Interview ends and candidate self-assessment

- **Проверка главы:** ✅ у маркера 2 Q&A · ✅ по смыслу и тайм-кодам полей всё сходится (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #19 | -15 с | `ML` | Cool. I think we're out of time so we can end here. |
| #20 | -10 с | `Communication` | Before I share my feedback, I want to understand from you how this int… |

#### Item #19

- **Question** (`00:44:45`): Cool. I think we're out of time so we can end here.
- **Candidate answer** (`00:44:50`): Mhm.
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `ML` · type=hard · stage=system_design

#### Item #20

- **Question** (`00:44:50`): Before I share my feedback, I want to understand from you how this interview went. What are the things you did well and what are the areas of improvement?
- **Candidate answer** (`00:45:02`): Um, I think maybe I did the initial um um question gathering in a more interactive way than I have before, but uh I think I really struggled with um time management and struggling on a particular choice. Um, and uh, yeah, I mean, I didn't get through most of the things that I wanted to talk about. I explored a lot of options, but I didn't get down into specifics. Um, I think that's the biggest thing. And I couldn't decide whether to do a um, sort of a short um, like a simple version at the top or just go dive into a more complex uh, like what I would actually probably build in in terms of state-of-the-art. Right. Right. Yeah. I think those are
- **Reference answer:** —
- **Interviewer feedback** (`00:46:04`): So overall, you know, subjective sense that I get, you know, from having done a lot of these interviews and also working as an ML engineer at a staff level is like you definitely know your stuff, right? Mhm. But I think just based on how this interview went, I couldn't recommend a higher for you to be honest, right? Like I didn't get enough signals in this interview for E6 and even E5 is honestly borderline, right? So there are a couple of reasons for that. The biggest reason I would say is time management and within that the biggest reason is just the amount of time you spend in the beginning. So just to give you a sense, right? We started like maybe 5 minutes into the hour. Yeah. And so like 20 minutes in, which is like 15 minutes out of the 45 that you get, you're still at this point here. We're talking and all of these like this highle diagram was not required. for a second I felt like you're going into like the traditional system design and you're talking about entities and all this kind of things right so I would just say and you mentioned binary classification like 20 minutes in roughly and even then there was a big discussion on binary versus regression on percentage watched and multitask and okay that was a decent discussion but you know like if you've already like you should be having that discussion maybe 5 to 10 minutes into the interview, right? So like I think you just need to go through things a lot faster like just understand the problem really quickly, understand the business objectives really quickly and yeah doesn't have to be super interactive, right? Like you you don't need to ask everything from me. You can just make some assumptions on your own. If you do a wrong assumption, I'll correct you, right? Okay. uh and then that whole part like the business objective should be over in less than 5 minutes and ML objective 5 minutes. So 10 minutes in you are at the point where you're talking about oh you know I'm going to model this as a binary classification with uh predicting like a significant watch versus no watch right and then use like as a secondary signal in a multitask approach so to get to that point should be like no more than 10 minutes whereas in your actual interview it took you like 30 minutes almost.
- **Labels:** `Communication` · type=behavioral · stage=behavioral

## Speaker boundary check (heuristic)

Automatic role check (no diarization): Q/A duplicates, truncated questions, candidate speech in question field, interviewer lines inside answer.

- **Item #18:** текст `interviewer_feedback` повторяется в `candidate_answer` (или наоборот). Оставьте реплику только в одном поле.


## Check 3. Semantic field alignment per chapter (step 5, LLM)

The Cursor agent (same as step 2) reviews **extracted** Q&A: field timestamps vs chapter windows and whether texts match chapter titles and labels (`question_topic`, `question_type`). Does not change the overall verdict.


- **Статус:** ✅ все 7 глав без замечаний
- **Тайм-коды полей:** 7/7 ок · **Смысл/метки:** 7/7 ок


## Transcript spans without Q&A in JSON

Intervals in `timecodes.txt` not covered by any item span. Check for a missed question or service speech.

_No large uncovered spans (threshold: ≥25s, ≥4 timecoded lines)._


#### Короткие ответы кандидата (≤4 слов)

Проверьте по транскрипту: это **осмысленный** короткий ответ на вопрос, а не обрезанный span или пропуск речи кандидата.

| Item | Время | Ответ |
|------|-------|-------|
| #19 | 00:44:45 | Mhm. |

<!-- SEMANTIC_VALIDATION -->

## Semantic validation (step 5)

Машинный ответ LLM (шаг 5). Валидатор читает этот блок при повторном прогоне.

```json
{
  "chapters": [
    {
      "chapter_time": "00:00:53",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:17:00",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:38:00",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:45:00",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:50:00",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:56:00",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "01:03:00",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
