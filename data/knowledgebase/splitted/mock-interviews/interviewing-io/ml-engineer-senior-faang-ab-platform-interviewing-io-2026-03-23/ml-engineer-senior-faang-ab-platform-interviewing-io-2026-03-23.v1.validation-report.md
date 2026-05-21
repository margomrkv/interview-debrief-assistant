# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-faang-ab-platform-interviewing-io-2026-03-23`
- **Режим:** `split_and_validate` · **source_id:** `ml_engineer_senior_faang_ab_platform_interviewing_io_2026_03_23`
- **Старт:** 2026-05-20 21:18:05 +0200 · **Обновлено:** 2026-05-20 21:31:11 +0200
- **Длительность прогона (стена):** 13 мин 6 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 4 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ⚠️ неполный журнал (проверьте pipeline-log)
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-faang-ab-platform-interviewing-io-2026-03-23/ml-engineer-senior-faang-ab-platform-interviewing-io-2026-03-23.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 3 | 3. Excel | нет | — | 2 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 2 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-faang-ab-platform-interviewing-io-2026-03-23/ml-engineer-senior-faang-ab-platform-interviewing-io-2026-03-23.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-faang-ab-platform-interviewing-io-2026-03-23/ml-engineer-senior-faang-ab-platform-interviewing-io-2026-03-23.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-faang-ab-platform-interviewing-io-2026-03-23/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 11 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (1/1), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 5 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-faang-ab-platform-interviewing-io-2026-03-23/ml-engineer-senior-faang-ab-platform-interviewing-io-2026-03-23.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 11
- **`source_id`:** `ml_engineer_senior_faang_ab_platform_interviewing_io_2026_03_23`
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
| 1 | `00:24:01` | API wrapper and routing model bre… | — | recognized (1 Q&A) | #7 | `Experimentation` | ✅ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `00:24:01` — API wrapper and routing model breakthrough

- **Проверка главы:** ✅ у маркера 1 Q&A · ✅ по смыслу и тайм-кодам полей всё сходится (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #7 | -10 с | `Experimentation` | Well, how do you know which How do you know which category they're in?… |

#### Item #7

- **Question** (`00:23:51`): Well, how do you know which How do you know which category they're in? You're saying like based on front-end or back-end or treatment?
- **Candidate answer** (`00:23:57`): Um yeah, so I'm saying based on treatment. So yeah, there's there's this is sort of without our without our application. But like what we want to do is we want to essentially have like a routing or a like a translation layer that um we say that um essentially um we want to have I'm going to make a little bit of extra space here. Okay, so essentially your your platform is going to answer for them if it's function one or function like if you're going to go down which path. That makes sense? Right. Right, exactly. So I mean I would imagine here that the user would have basically, you know, we could uh determine um using some kind of like a hash. I'm thinking like almost in a similar way that you could do like uh hashing for partitioning that that you could basically take some information about the user like their email address or something like that and then it would basically put them into uh bucket user or like yeah, this is a layer that basically just determines what bucket a user is in. Um so maybe I'll just like draw a line here. And this is basically A. Oops. I want a text box here. And this is going to be B down here. Um and so this is going to be based on um yeah, it's going to be randomized so that we work we can split these users up fairly easily. Um and then depending on uh which bucket they're in when they make a certain call from the website well when they render the website, they're they're they're either going to be um calling API function one or API function two. So it it could be kind of like user if you're in option B, then you call um function one. Mhm. And if you're in bucket A, then maybe you call function two. Mhm. Um two. So um and then obviously this gives a response back to the user and will display it. So there's an arrow going going in that direction. Um so I guess what really needs to happen here though is that um I I guess what I meant by a wrapper by having a wrapper is that I mean in general you could have many different sort of features that could be swapped in. It's not just one function where it could be one or the other. It's really like a mapping of you know, uh several different components which depending on which bucket you're in, it's it's going to route you to API call one or API call two. And so I think, you know, it really inside this this uh routing layer here, there should be kind of like a mapping of which functions uh high-level functions map to which actual implementation in the API. Um so like essentially um if it's you know uh comments display or like display comments, let's say uh you know, we this mapping would say in in section A, display comments routes to function two and in section B, display comments wraps maps to function one. And And there could be several functions that have that mapping. Mhm. Here. And so it's basically uh basically a router. Um So yeah, okay. Um and then I think there's a similar I'm kind of focusing on the back-end here, but I think a part that I'm not really mentioning here is that this is also obviously important for just the front-end. There there's going to be a lot of front-end features that we want to um think about as well here. But I I guess I might want to try to run through a complete picture even just with these back-end AB testing like having different implementations of some of the API function calls and cuz what we're still not haven't met all of the functional requirements yet because what we need is to calculate different metrics here. Based on which bucket the user is in. So um I think this is So this is going to interact with uh the API obviously can be tracking various features and I think uh sorry, it can be tracking various metrics and storing them, you know, regardless of what the actual back-end database is for this application which is going to be very application specific. I think we want to be able to uh store these metrics in some kind of database that I would say probably because we want to do a lot of high-level analytics on this, I would recommend using like and it's sort of like OLAP style um interactions as opposed to transactional. I think we probably want a SQL database. Um and I'm sorry that I uh I don't know how to get the database icon here. that's okay. I actually don't know how to do it either. Every so often pops in with like this incredible shape and I'm like, "How did you even do that?" Yeah. Well, I'll just make a circle for now so That's great. cylinder or top-down view. Great. Uh so, let's just call this uh you know, a SQL database. It could be like Amazon RDS or something like that. Uh-huh. But, this is uh metrics database. And that's going to be SQL. Um And so, I think in this database what we want to do is uh I mean, I I may want to lay out some of the schema here. So, um the the types of things that we would want to track. So, we discussed having tracking some of these metrics like the click-through rate. Uh I mean, okay. Um let's see. There does I suppose need to be a separate process that's actually sort of listening like watching the user interactions here. Um that's separate. This isn't really triggered by anything in particular like that the user is it it Yeah, this is separate from the API that's watching the user. I think there's kind of like a um some process that's actually generating these metrics in real time and well, it doesn't need to be in real time. I suppose it could also be offline. But, I think there's a separate process that um is sort of listening to the uh well, really like the front end. I think it it's sort of the front end server that and that would be able to understand that would be able to read out how often is the user when they're on a certain page clicking through or uh how long are they staying on the page for example? I don't know if there's um uh a best practice there. But, so I guess what I'm saying is there might there might need to be like a separate microservice that is [clears throat] sort of listening to this. So, um maybe I'll move this down and I'll say that there's a service that's kind of um it's read-only from the the website and the back end that is sort of uh metrics generation. Like Yeah, you can assume it's kind of black boxy for us, right? Where it's like there's probably already trackers on the website that are pulling metrics. Right. Right. Okay. So, I don't have you just need to store them or specific ones about like what treatment the customer is in as an example. Yeah, that that makes a lot of sense. Um but so yeah, there's some service that's doing that. So, but in terms of um maybe we can get into the nitty-gritty of what's actually going to be stored here. So, we talked about um you know, for each uh so, let's see. Metrics table. Um so, um and I guess I'm going to assume that there's there's probably some process where you're like recording individual clicks and and things like that and then that is getting aggregated and and sent as like aggregate metrics. I'm going to skip over that intermediate step and I'm just going to say we're immediately getting aggregated metrics that are on the level of like we have sort of a user ID. Um we have uh which branch they're in. And then we have um time. I'm going to say it's not timestamp because again, we're not um I don't think this is like an events level table. I think this is already pre-aggregated just to kind of simplify things. So, I'm going to say like time buckets. So, this could be like uh maybe minutes or uh actually no, because um that's probably a little bit overly granular. Um It could be um I guess I'm So, I'm curious. Do we Yeah, this is a question about the functional requirements. Do we care about having these metrics um and tracking them over time or do we want to just let's say say, well, ever since inception of this branch, here's what the user's average um click-through rate has been? Or do we want like a chart that we could actually look at of uh you know, here's their average click-through rate in these time buckets over time like I guess Mhm. Um for me, it's probably a little bit more like on or off in terms of like, okay, for a customer who received A, did it improve the click-through rate over Oh, it also depends. Sorry, I'm that was confusing cuz A could be control, right? So, whichever one was your treatment, did it improve X metric over your control? Yeah. Yeah. Okay. That makes sense. the since inception things like since customers are trying to get trying to use it. Yep. Yep, that makes sense. Okay, so I think I might not actually even have a time bucket here. I might just go directly to here's sort of um you know, average click-through uh and the you know, time I forget exactly what this one is called. But, like time on site and thinking of some other metrics like, you know, money spent maybe if they're like it maybe there's some kind of integration with the payment processor cuz that would be something we would want to track. Um or you know, various different metrics here. Um And then I think it you mentioned that we want to be able to compare it to the control. So, I would say this metrics table should also include information about this user from before that change was instituted um because we don't want to just compare branch A to branch B. We probably want to be able to compare users on the branch that changed with their own data from before. Um and so, I guess I would say that uh probably this branch ID here should probably everyone should always be assigned a branch ID like even if you're just not even doing an AB test like you can still you're still updating some branch ID in this table which could later be referred to. Um And so, I I think um yeah, that that way you would be able to sort of say the the branch that the user was on before the AB test even started also has a name and we can also look up the aggregate information for that control. Um so, like there's there's always a branch happening. Everyone is always on a branch. Um And so, um okay. So, that just kind of covers how we would compare this to like to the data from before is let's say a branch ID is an always incrementing number. And so, you know, you might be on branch 150 not because there's 150 active branches, but just because that includes the full history of your AB testing over time. Um And so, that's just like an incrementing counter. Okay. Um So, we have this metrics database and then I guess what another important thing here is we need like someone to be able to read this information for the the business user the developer to obviously to be able to look at this information. So, then I think what we need is kind of like a business intelligence dashboard type of thing or analytics dashboard, let's call it maybe. Mhm. Um So, like BI dashboard. And this is reading from that SQL database. And um it's tracking things like uh what are the average metrics for one for each branch. Um it could have uh tracking aggregates, but it could also have um statistics. Like it could have some statistical capabilities like, you know, is it actually statistically significant difference? Like there could be some built-in you know, basic modeling functionality there. Um that allows the business user to to say, you know, is the you know, can we actually reject the null hypothesis uh that A that B is better than A with high confidence for example? Mhm. Um So, yeah. I think that would that would be sort of uh something that would have to be built by people with statistical expertise. Mhm. Um and probably it would have some visualizations as well. Yep. Um and that would be served to yeah, to a business user. Um, maybe I'll just call this, yeah, business user. Okay. Um, and okay. Biz user. Okay. Um, so let's see. Does that basic setup have I mean, I think there's a lot of missing components here to to cover the the missing components that I'm aware of at least right now. Obviously, um, scaling, um, I think um, I'm I'm thinking about the scaling thing. I You know, there there's probably a lot of scaling that's going to be happening inside the original API of that company. Um, if we're if we are really just a wrapper that's routing requests. Yeah. Um, then, you know, depending on how what kind of scale we're talking about here. That's a pretty low That's not a super compute intensive thing, just sort of translating one request to another and passing it along. Um, but I could imagine if it's like a a truly ginormous application that we're wrapping around, that even that routing layer may need to be um, handling scale well and may need like replication. Um, but I I guess for now I'm kind of setting that aside. Uh, I the other big thing is that I'm kind of really simplifying this into like calling different back end functions and I'm not really paying attention too much to the front end, uh, components and um, but um, so maybe I can talk a bit more about that, but in terms of like the overall framework of you have a user, you have some kind of routing thing that wrap that sort of routes you to different um, different Let's call them subsets of the API. So, it's not different API It's not totally different APIs, but kind of different subsets of the API that are available in all in one instance. Um, but then eventually it flows through a SQL database and to a business user's dashboard. Um, and I suppose I'm thinking, well, maybe I'll, uh, just ask that question first. Like, does this overall flow look like it's missing any major components?
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Experimentation` · type=hard · stage=system_design


## Check 3. Semantic field alignment per chapter (step 5, LLM)

The Cursor agent (same as step 2) reviews **extracted** Q&A: field timestamps vs chapter windows and whether texts match chapter titles and labels (`question_topic`, `question_type`). Does not change the overall verdict.


- **Статус:** ✅ все 5 глав без замечаний
- **Тайм-коды полей:** 5/5 ок · **Смысл/метки:** 5/5 ок


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
      "chapter_time": "00:10:08",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:15:30",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:24:01",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:31:35",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:44:06",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
