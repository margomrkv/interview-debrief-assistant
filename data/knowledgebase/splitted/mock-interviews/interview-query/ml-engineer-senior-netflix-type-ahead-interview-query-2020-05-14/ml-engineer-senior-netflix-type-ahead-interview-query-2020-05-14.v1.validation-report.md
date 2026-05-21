# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/interview-query/ml-engineer-senior-netflix-type-ahead-interview-query-2020-05-14`
- **Режим:** `split_and_validate` · **source_id:** `ml_engineer_senior_netflix_type_ahead_interview_query_2020_05_14`
- **Старт:** 2026-05-20 21:18:04 +0200 · **Обновлено:** 2026-05-20 21:30:58 +0200
- **Длительность прогона (стена):** 12 мин 54 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 4 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ⚠️ неполный журнал (проверьте pipeline-log)
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-netflix-type-ahead-interview-query-2020-05-14/ml-engineer-senior-netflix-type-ahead-interview-query-2020-05-14.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 3 | 3. Excel | нет | — | 2 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 2 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-netflix-type-ahead-interview-query-2020-05-14/ml-engineer-senior-netflix-type-ahead-interview-query-2020-05-14.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-netflix-type-ahead-interview-query-2020-05-14/ml-engineer-senior-netflix-type-ahead-interview-query-2020-05-14.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interview-query/ml-engineer-senior-netflix-type-ahead-interview-query-2020-05-14/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 8 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (5/5), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 5 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-netflix-type-ahead-interview-query-2020-05-14/ml-engineer-senior-netflix-type-ahead-interview-query-2020-05-14.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 8
- **`source_id`:** `ml_engineer_senior_netflix_type_ahead_interview_query_2020_05_14`
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
| — | `00:00` | Intro | — | skip | — | — | ⏳ | — |
| 1 | `00:17` | Welcome | — | recognized (1 Q&A) | #1 | `Adaptability` | ⏳ | — |
| — | `00:54` | Introduction | — | skip | — | — | ⏳ | — |
| 2 | `02:48` | How would you build a recommendat… | — | recognized (1 Q&A) | #2 | `ML` | ⏳ | — |
| 3 | `07:25` | Bias | — | recognized (1 Q&A) | #3 | `Experimentation` | ⏳ | — |
| 4 | `15:21` | Cache | — | recognized (1 Q&A) | #7 | `ML` | ⏳ | — |
| 5 | `16:04` | Performance | — | recognized (1 Q&A) | #8 | `ML` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `00:17` — Welcome

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | +30 с | `Adaptability` | just up front I'd love to just kind of get a quick background on like … |

#### Item #1

- **Question** (`00:47`): just up front I'd love to just kind of get a quick background on like how you got into engineering data in tech
- **Candidate answer** (`00:55`): yeah so my name is Dan I am 26 and from Orange County in high school I was always into math but not coding at all I shied away from it my dad was a programmer and I know I kind of wanted to branch out a little bit and try something new didn't really work out that way then I went to MIT and I played a lot of League of Legends and decided I wanted a companion tool to to determine what the optimal item to buy at a point in the game like say you're winning should you buy needlessly large rod or void staff that was a question always in my mind so I did my first Python class which enabled me to answer that question and answer that question more in real time than you know doing it on paper and pencil so then from there I switched majors actually and swishy computer science junior spring and hustle to finish and then I got my first job at a college ID inflection which is where I met Jay and I was a data scientist there but then actually shortly after that I went to Quizlet where I still am today after just over four years and Quizlet we do education technology and classroom tools study tools and classroom games and stuff like that and actually today we're announcing we just got a new series C round of funding and we're just valued Oh a billion dollars that's pretty sweet today pretty you know coincidentally on the day of the stock India yeah so Quizlet I do and data engineering right now but I'd say my toolset is pretty broad I was recently database administrator at Quizlet and doing a performance engineering and now is more compartmentalized data engineering as opposed to the sre work I used to do
- **Reference answer:** —
- **Interviewer feedback** (`02:46`): gotcha cool
- **Labels:** `Adaptability` · type=behavioral · stage=fit_hr

### 2. `02:48` — How would you build a recommendation engine

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #2 | +13 с | `ML` | I'd love to start this interview with a first question kind of and I t… |

#### Item #2

- **Question** (`03:01`): I'd love to start this interview with a first question kind of and I think around like more data engineering system design but there is some more machine learning kind of aspect question to this and so this is from Netflix but let's say that you work as machine learning engineer on Netflix how would you build like the recommendation engine for type-ahead search
- **Candidate answer** (`03:28`): yeah so I do have the advantage of having seen this question before so I have a little premeditation on it but here I go with my response anyway yeah so I'm gonna start with the first like right off the bat the first way I would go about solving this is I would say hey we want a recommendation algorithm sounds like an RNN recurrent neural network which is a lot of cruft and not easy to set up at all and even more difficult to reason about how it works but now that I'm a little more experienced I definitely see the benefit of a much simpler model with you know the benefit is that it's simpler and I propose that we can do that similar results to a big crusty or recurrent neural network with a simple prefix matching and we can certainly go into you know a lot of sophistication with a simple prefix matching algorithm it can be expanded upon and expanding on until we have something that will be on par with an RNN so working at Quizlet we actually have something similar to that we have we a Quizlet we have kind of a flashcards model for most of our most of our service and when a user is creating a flashcard it's similar to the Netflix type-ahead search we they will type in h-e-l-l-o h-e-l-l-o and then it will auto suggest Ola if you're doing a spanish translation set okay so you know we have that similar problem and before I saw how we solved it I would imagine the same way hey we should do a recurrent neural network that's not easy but quite powerful but actually we solved it using a prefix matching algorithm just to say hey look up in this database table what does h-e-l-l-o prefix to and its suffixes to the model H Ola because most people are typing that so we can I'm not going to be actually coding this out I'm just gonna be talking about the approach I would have but so we could start with a simple thing hey no matter who you are what context you're in we're just gonna have a prefix table and our prefix table starts with a an input string and that is your prefix and it will output let's say one at a time to start with your output string and I think scoping is very important so for this minimum viable product or MVP we're gonna start with okay you input a string and you're going to output your suggestion string already already I'm thinking of things like you know fuzzy matching and context matching like hey what if you were in a different language but you know we're gonna start off just scoping it so how do we build such a thing to do the simple prefix matching well what we can do is a quiz that we have the advantage of a huge corpus of data so we have you know billions of terms that say hey when I user types hello they usually want to output Ola I'm gonna back up a little bit and actually translate this to the Netflix algorithm we're trying to solve so if you're trying to I'm not so familiar with what's on Netflix but if you're trying to input the big that could output any number of suffixes if that's your prefix you could output the big short or the big lebowski to movies on the fana and so how is your model going to do this well what you can do is you can say well in our existing search corpus of billions of searches what proportion of the time to people hiding in the big actually click on the Big Lebowski and where proportion of time do they output the big short so so you could just have a simple thing that has every match every possible search prefix that has ever been typed on Netflix output that to the most common most common thing that they clicked on and boom that's your prefix matching a recommendation algorithm for type-ahead search
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `ML` · type=hard · stage=system_design

### 3. `07:25` — Bias

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #3 | +1 с | `Experimentation` | isn't that actually prone to bias there so that's based off an existin… |

#### Item #3

- **Question** (`07:26`): isn't that actually prone to bias there so that's based off an existing algorithm though right because that would then have to mean that when you typed in the big there was some like existing Netflix recommender that had to put the big short or the big lebowski like one of them in front the other so that would have given like sort of like biased towards like the first one which could have been the big short or the big lebowski
- **Candidate answer** (`07:50`): so the way that B then can you know counteract that because then it we could be feeding ourself into like some weird loop right of like just automating against bad data right because if Netflix in the initial case Netflix didn't even recommend what's another big movie I don't know like big the big like just big buy sure yeah so if we didn't even recommend that in the old case then we're gonna have very few hits where where the user typed in big and it outputs you know the Tom Hanks movie so a solution to that might be hey ignore whatever Netflix recommends and only use the corpus of what the user types so just freeform text we go from hey you typed the big and then you finished typing the big short regardless of any Netflix interaction that's hard to do because there's you know an existing state yeah of Netflix type ahead but I think it's a good happy medium and one thing you could do is do your best to account for that bias and say hey 10% of the time the user clicked on the Tom Hanks movie even though zero percent of the time in the existing case did we recommend so you get seems like you can Bayesian update that with to say hey even though it wasn't recommended the user really wanted to follow that so that should be a lot more valuable in a potential type-ahead search algorithm the thing I want to dive into more is a context matching so you could context match based on the user let's say hey if you're suggesting the Big Lebowski and the user happens to if you're typing in too big and the user you know is a big fan of Coen Brothers movies then you're gonna boost Lebowski a lot higher than it would be otherwise yeah
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Experimentation` · type=hard · stage=system_design

### 4. `15:21` — Cache

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #7 | +1 с | `ML` | gotcha so does that mean that this kind of trial would have it so that… |

#### Item #7

- **Question** (`15:22`): gotcha so does that mean that this kind of trial would have it so that for each word and then a space we have big and then like entire 26 letters of then the next kind of cache variable a could be like Apple I don't know Big B baby something like that and then all those tries don't know exactly
- **Candidate answer** (`15:39`): exactly exactly and if if so it could also take care of fuzzy matching depending how you build that if you build that try so if you type be cagey then you could say oh it's that finger okay instead of I your try perhaps could be knowledgeable about that cool this stuff like that
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `ML` · type=hard · stage=system_design

### 5. `16:04` — Performance

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #8 | +1 с | `ML` | and then in terms of serving this in real time is there anything that … |

#### Item #8

- **Question** (`16:05`): and then in terms of serving this in real time is there anything that we have to think about in terms of how would like the caching then works in terms of returning the results of the movies because and it seems like we have to then return a lot of results based on the user entity plus the actual input and so I'm imagining that distributing this across multiple like the entire world requires some more like performance like considerations right and like what are their durations we have to make um
- **Candidate answer** (`16:49`): so one thing that comes to mind as we're you know serving this live system has to be always up is deployments but hopefully at all our levels of employment we could have the version number be a cache key so we'll never have any overlap there returning scale results as far as scaling across all our users across the globe um our that layer of converting a user profile to a condensed feature set will hopefully reduce the cache size I reduced the cache domain so now yes we are caching on input string and this condensed user profile but we can grow that incrementally to say hey onon on initialization there are no user profiles there's just a one-size-fits-all and then as we grow we can say okay now there's two now there's a thousand and now there's two now there's three now there's ten now there's a thousand so we can hopefully grow those and see at what point which things start to break oh is our caste system falling over do we need to have a tighter tighter grasp around that to make sure that doesn't fall over but if we grow slowly I'm imagining on initialization one user profile you know cast on yes every input string is not going to fall over it be as a dimensionalities solo and you could limit on like the first 10 characters and that should fetch you that should give you a good signal on what move you're trying to get after 10 characters and yeah 26 to the 10 is pretty big but at least at least recently used cash is going to be you know pretty performance on real user input
- **Reference answer:** —
- **Interviewer feedback** (`18:22`): great awesome
- **Labels:** `ML` · type=hard · stage=system_design


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
      "chapter_time": "00:00:17",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:02:48",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:07:25",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:15:21",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:16:04",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
