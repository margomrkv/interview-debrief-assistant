# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/interview-query/data-scientist-senior-uber-ride-requests-interview-query-2020-07-23`
- **Режим:** `split_and_validate` · **source_id:** `data_scientist_senior_uber_ride_requests_interview_query_2020_07_23`
- **Старт:** 2026-05-20 21:18:03 +0200 · **Обновлено:** 2026-05-20 21:30:33 +0200
- **Длительность прогона (стена):** 12 мин 30 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 5 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ⚠️ неполный журнал (проверьте pipeline-log)
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interview-query/data-scientist-senior-uber-ride-requests-interview-query-2020-07-23/data-scientist-senior-uber-ride-requests-interview-query-2020-07-23.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 3 | 3. Excel | нет | — | 2 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 3 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interview-query/data-scientist-senior-uber-ride-requests-interview-query-2020-07-23/data-scientist-senior-uber-ride-requests-interview-query-2020-07-23.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interview-query/data-scientist-senior-uber-ride-requests-interview-query-2020-07-23/data-scientist-senior-uber-ride-requests-interview-query-2020-07-23.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interview-query/data-scientist-senior-uber-ride-requests-interview-query-2020-07-23/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 9 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (3/3), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 3 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/interview-query/data-scientist-senior-uber-ride-requests-interview-query-2020-07-23/data-scientist-senior-uber-ride-requests-interview-query-2020-07-23.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 9
- **`source_id`:** `data_scientist_senior_uber_ride_requests_interview_query_2020_07_23`
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
| 1 | `00:54` | Chinmaya Background and Introduction | — | recognized (1 Q&A) | #1 | `Adaptability` | ⏳ | — |
| 2 | `03:20` | Uber Interview Question | — | recognized (3 Q&A) | #2, #3, #4 | `ML`, `Product Metrics` | ⏳ | — |
| 3 | `10:31` | Feature Engineering and Character… | — | recognized (1 Q&A) | #5 | `Product Metrics` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `00:54` — Chinmaya Background and Introduction

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | -15 с | `Adaptability` | i believe uh and so jamai i'd love to just first kind of like get a se… |

#### Item #1

- **Question** (`00:39`): i believe uh and so jamai i'd love to just first kind of like get a sense of your background um and tell the audience kind of how you uh got into data science and kind of like why you were interested in it
- **Candidate answer** (`00:53`): cool oh yeah thanks jay thanks for having me um i kind of stumbled on your interview query on when i was studying for my interviews at microsoft so it was it's come full circle uh so it's great to like you know look back and say oh wow like i've learned a lot enough to be here uh so thanks thanks for having me um my background i i did my undergrad at u of t in university of toronto for those who are not familiar with it in business administration i like had kind of data on my mind um never left me i i was always like curious about it how it worked where it could be used and how we could make better decisions with it um which led me like a down a very like winding path i would say uh first into like brand management then product management and product marketing and then finally kind of landed up at queen's university at the smith school of business and the ai program where i've been like trying to take all the things that i've learned about data about i.t about systems about marketing and business and like put them all together to make intelligent systems uh because that was like the opportunity that i saw and i and i was hoping to land a ai or ml based uh product management role which ended up happening so really happy about like the outcome there uh overall like just really excited about what this field has to offer i think we've barely like begun to tap into what's possible um and as as important as the technical skills are i've learned that there's a a lot of business context that data scientists need to think about and many times that uh a model just is is just the is just scratching the surface the real solution is often like how does it solve a problem for the end users um so that's kind of like where i want to keep growing and take my skills
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Adaptability` · type=behavioral · stage=fit_hr

### 2. `03:20` — Uber Interview Question

- **Проверка главы:** ✅ у маркера 3 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #2 | -10 с | `ML` | uh and so uh segwaying into this actual uh mock interview so today i'd… |
| #3 | +62 с | `Product Metrics` | at the driver angle not at the right or angle right |
| #4 | +88 с | `ML` | and do you know like what the driver is shown or an uber driver is sho… |

#### Item #2

- **Question** (`03:10`): uh and so uh segwaying into this actual uh mock interview so today i'd love to talk about a problem that is asked at uber and so it's modeling based and so the question at hand is uh you're tasked with building a model to predict if the driver on uber will accept a ride request or not and so how would you go about building this model and what kind of features would you use what model would you select and so on
- **Candidate answer** (`03:43`): cool so uber wants just to clarify the question so uber wants to know uh whether a person will accept a ride or not and we want to build a model to predict that i'm gonna do something that i like doing during interviews because i think it's like a neat trick yes uh so let me just start sharing my ipad screen i find that this is like a virtual whiteboard in covet times and i would normally have in a real interview okay so we're looking at um we're looking specifically
- **Reference answer:** —
- **Interviewer feedback** (`03:54`): yes cool okay uh just give me two minutes
- **Labels:** `ML` · type=hard · stage=technical_case

#### Item #3

- **Question** (`04:22`): at the driver angle not at the right or angle right
- **Candidate answer** (`04:25`): yep and so uh if you imagine how uber works uh we have you know the drivers uh and the writers and the writers make uh requests to get rides and then i guess uber sends out um general requests to each driver uh within a certain area or radius to see if they'd expect it was so the driver gets a request
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

#### Item #4

- **Question** (`04:48`): and do you know like what the driver is shown or an uber driver is shown about a writer and the kind of information that they give they're given to make that split second decision uh
- **Candidate answer** (`05:01`): let's say that as the company um this is a feature that you can customize right and so we can show a lot more information or we can show almost no information i think depending upon also there is like a monetary like this is how much it might uh you'll get from it um and i think that is uh something that they also use to incentivize writers to drivers to accept the request from them okay interesting so the way that i'm kind of like thinking through this is that there's like three buckets uh of of information that's shown to a driver about a writer okay one is like there's a lot of info the second one is there's some info and the third is lots of info yep okay so the reason that i'm kind of doing this to maybe i don't know what the circle is but anyway i will ignore it um so what i'm trying to do here is uh i'm trying to just get an understanding of the uber business and the kind of the user experience that a driver has with a rider um so i'm asking these kind of questions to determine whether because i'm kind of thinking through this as the driver has to make a split-second decision especially when they're like taking when they're either completing an existing trip or they're on a trip and about to end that's kind of like the two points um so maybe if i like model this out a little bit more the driver essentially has either they choose to new so i'm going to say like driver new trip trip so they either decide at the end of their current ride current ride or um middle of their existing one or like late in the game okay so given that i think what's what's usually as i'm kind of like brainstorming um if they're shown the distance so that that would actually be the first one to like to say okay well distance to next rider then of course if you show that and if it's small then they're likely to accept so that would be one of the features that i would kind of start thinking about as i'm starting this modeling exercise so uh before i mean i know what we're trying to do is get into the model but the first step that i'm trying to follow understand is the user journey the second one that i want to do is actually the exploratory data analysis piece to actually understand the relationships between data points that uber may have uh today about their driver or their rider and what the relationships between those features are so distance and then there's also so there's actually two kind of distance data points we have distance to next rider from the driver's current position and then you would have distance uh let's say trip trip distance that's kind of like the two main areas that i'm thinking yeah because i think the multi-sided marketplace brings up something that i didn't think about yet which was this idea of and i don't know if uber does this today but picking up uber eats orders on the way if they're taking a driver or they're just ending a trip maybe
- **Reference answer:** —
- **Interviewer feedback** (`08:48`): yeah so i think that's uh kind of a great way to frame it because there are um kind of like uh trip characteristics right and these are the distance trip distance and then um there can be other things uh such as uh the general um i think we mentioned this before like the price that you get from the trip um you know like how long this trip might take i guess that's a function of the distance and then just kind of like uh what time you know you're taking this trip right now uh you know if it's 12 a.m versus um you know like i don't know 3 p.m or something at rush hour uh and so these are all kind of like uh characteristics of this one entity and then there's also i think this you know multi-sided marketplace we have like the driver side and then also um potentially you know the user information that you uh put at the top as well right right [Music]
- **Labels:** `ML` · type=hard · stage=technical_case

### 3. `10:31` — Feature Engineering and Characteristics

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #5 | -18 с | `Product Metrics` | yeah that is true we could probably scope that down to just the uber d… |

#### Item #5

- **Question** (`10:13`): yeah that is true we could probably scope that down to just the uber driver marketplace okay
- **Candidate answer** (`10:23`): so no no cool so the two main buckets i think that you've highlighted which are really which we just kind of like briefly discussed are so if i kind of like think about characteristics from high level umbrella and then break that down into okay so there's kind of trip there's ryder there's oh yeah of course there's driver as well so the driver itself themself or him him or herself will have their own kind of propensity to accept rides or not accept rides based on certain time of day or number of rides that they've kind of they've done in their shift maybe or even like how much money they've made um throughout the entire week or whatever time span we choose to look at so if they if this driver is coming off like an eight hour shift they're not going to do another ride yeah so there's trip rider driver and oh of course how could we forget traffic traffic so traffic is a i feel like it that's how most decisions will be made in large cities it's like is it like 5 pm so if it's 5 pm it's like i'm not doing any that's it for me and especially like traffic would um i think traffic is kind of related but not directly i think there's like some indirect relationship between traffic and special events um this is of course like pre-covet times mm-hmm uh and special events so i'm thinking surge pricing during let's say like your favorite basketball game or hockey game or even like whatever sporting event or whatever event it could be anything yep um so traffic is likely to spike up but at the same time surge is gonna go up so people are so even if there's a special event like you know that's ending at 5 p.m even though there's a lot of traffic people might be on the road because there's a bunch of people that are requesting rides um the other thing yep characteristics of like a trip potentially like uh i guess the trip that you take the traffic would almost be like factored into it kind of special events as well um so either maybe not at this kind of dimensional analogy but like in general i think at some point they could all roll up under um uh kind of like a trip uh in a sense and because uh yeah i think the writer has its own information the driver has its own kind of information about themselves they have ratings writers have ratings and then a trip could then just have like a pension potentially its own rating too right from like one to ten of how like great this trip is versus like how horrible this trip might actually be yeah i think that's actually a good point i'm gonna put it down but it's something that i'd like to visit later on because if we start thinking about quality of trip then that itself is honestly a model to predict to like regress it or classify a trip um based on like certain factors we would actually need to do a deeper deeper dive into that yeah okay but another big thing is actually like and this is something that i don't think many people would think about but it's a vehicle condition so or actually not even vehicle condition i'm going to say vehicle itself and and i'll like kind of explain a little bit more so one of the use cases that i'm thinking about is i'm i'm kind of out like you know pre-covered uh i've had a decent day at work i have a couple like i have some energy left over and i want to pick up a few riders but likely what's going to happen is um i'm gonna do this like closer to 10 no sorry either closer to like 10 when people decide to head out and i'll pick them up to drop them off the club or whatever they're going or wherever whatever venue that they want to attend and then most likely i'm going to be out on the road either around midnight or 1am again but i can only but the number of riders or a number of rides is actually linked to the type of car that i have um so i couldn't really pick up you know a party if i if i only have a car or if i only have cooper i could only pick up two or three people but if the car that i have is in the garage or like my van my extra van is in the garage then i can't use that that's number one number two is i'm unlikely to if i have a second car i'm unlikely to actually use the van um during regular drop-offs when it's like one driver two driver interaction two rider interactions um i'm likely to use my regular car for that kind of so what i'm saying is that the vehicle type in the vehicle condition would affect the driver's ability to accept certain trips
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

## Speaker boundary check (heuristic)

Automatic role check (no diarization): Q/A duplicates, truncated questions, candidate speech in question field, interviewer lines inside answer.

- **Item #8:** текст `interviewer_feedback` повторяется в `candidate_answer` (или наоборот). Оставьте реплику только в одном поле.


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
      "chapter_time": "00:00:54",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:03:20",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:10:31",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
