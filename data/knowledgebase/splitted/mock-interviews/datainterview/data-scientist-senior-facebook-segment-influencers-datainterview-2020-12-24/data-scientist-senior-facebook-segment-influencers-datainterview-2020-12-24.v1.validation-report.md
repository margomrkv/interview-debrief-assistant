# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/`
- **Режим:** `split_and_validate` · **source_id:** `data_scientist_senior_facebook_segment_influencers_datainterview_2020_12_24`
- **Старт:** 2026-05-20 21:05:21 +0200 · **Обновлено:** 2026-05-20 21:12:41 +0200
- **Длительность прогона (стена):** 7 мин 20 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 3 мин 1 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ✅ все зафиксированные шаги завершены
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 2 | 2. Извлечение Q&A (LLM) | да | claude-sonnet-4-6 | 3 мин | ✅ |
| 3 | 3. Excel | нет | — | 1 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 0.00 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 20 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (3/3), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 3 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 20
- **`source_id`:** `data_scientist_senior_facebook_segment_influencers_datainterview_2020_12_24`
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
| 1 | `00:00` | Statistics Questions | — | recognized (2 Q&A) | #1, #2 | `Communication`, `Statistics` | ⏳ | — |
| 2 | `09:50` | SQL Questions | — | recognized (2 Q&A) | #10, #11 | `Statistics`, `SQL` | ⏳ | — |
| 3 | `20:00` | Case Questions | — | recognized (1 Q&A) | #14 | `Product Metrics` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `00:00` — Statistics Questions

- **Проверка главы:** ✅ у маркера 2 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | +34 с | `Communication` | do you have any questions on that before we proceed |
| #2 | +55 с | `Statistics` | can you can you explain to me um what is a beta coefficient of a multi… |

#### Item #1

- **Question** (`00:34`): do you have any questions on that before we proceed
- **Candidate answer** (`00:38`): no that sounds good thank you
- **Reference answer:** —
- **Interviewer feedback** (`00:40`): okay awesome
- **Labels:** `Communication` · type=soft · stage=fit_hr

#### Item #2

- **Question** (`00:55`): can you can you explain to me um what is a beta coefficient of a multiplier regression
- **Candidate answer** (`01:02`): uh yeah for sure so the beta if we um sorry let me think about how to frame it um so a multivariate regression describes the relationship between the left hand side variable the outcome and a series of right hand side variables let's call them the independent variables and the beta coefficient describes how the outcome changes in relationship to changes in the independent variables so if the independent variable changed by one and the beta coefficient is on that variable is beta for example then the outcome would change by beta
- **Reference answer:** —
- **Interviewer feedback** (`01:52`): is um that makes sense
- **Labels:** `Statistics` · type=hard · stage=technical_qna

### 2. `09:50` — SQL Questions

- **Проверка главы:** ✅ у маркера 2 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #10 | -60 с | `Statistics` | okay now what if it wasn't uh what if it was involved ratio if the if … |
| #11 | -5 с | `SQL` | so i'm going to go ahead and paste the table so this is a a basically … |

#### Item #10

- **Question** (`08:50`): okay now what if it wasn't uh what if it was involved ratio if the if the confidence interval has has um one what does that mean in terms of its uh statistical significance so let's just say that the odds ratio confidence interval falls somewhere between um point two four and point one uh one point two four what does it mean in terms of its statistical significance um
- **Candidate answer** (`09:25`): then in in which case because it includes one it's uh if you were to do a hypothesis testing exercise you would not find that it's statistically significant
- **Reference answer:** —
- **Interviewer feedback** (`09:37`): okay got it all right thank you um okay so we're going to move on to the uh x sql question um
- **Labels:** `Statistics` · type=hard · stage=technical_qna

#### Item #11
- **⚠️ границы реплик:** начало `interviewer_feedback` уже есть в `candidate_answer` («in that case i think marking»…). Перенесите в feedback только новую речь интервьюера.

- **Question** (`09:45`): so i'm going to go ahead and paste the table so this is a a basically a snippet of uh of the message um table set um and it contains your user id username the date and the message the number of message sent and the message the number of message received a given user on a day-to-day basis now go ahead and try to address the first question which is for each day return the name of the user or in this case you can return the user id who receive the highest message sent to message received ratio and this message ratio is your message sent divided by message received
- **Candidate answer** (`10:37`): got it um yes i think the first question that i would or the first thing that i would check for in this data database would be whether there are missing values in either um in you know any of these columns and in the following analysis i'm just going to pre i'm just going to assume that there aren't any missing values and the second thing that i would think is important is whether message received could be zero because then you have a division by zero issue that may need to be addressed okay so i'm not select so so um so here i'm creating uh you know i'm selecting the user name variable and i'm also creating a new variable called uh sent to sent to received ratio which computes the ratio between message sent and message received and here i'm marking the message received variable as null if it's equal to zero so that the division will also result in a null okay um oh and i guess the question that i then want to ask is how we want to um treat these users do we um do we see them as having the highest ratio yeah like basically like okay for october 1st 2020 user xyz had the highest ratio i say so you actually want to set it to like a really high number um so that it would come on top when you sort um when you sort it precisely off of a given day so you want to you want to do some kind of screening on a given day got it okay in that case i think marking it as a null may not be the best idea um
- **Reference answer:** —
- **Interviewer feedback** (`14:14`): in that case i think marking it as a null may not be the best idea um let's actually kind of simplify this for a bit so let's just presume that um there is no zero in the denominator and it's already it's always populated so how would you go ahead and proceed with that problem then okay yeah that sounds good um in that case um i'll just do a simple division to calculate the ratio um and we want to group by date um so that we return one user for each date and the other question is do we are we interested in returning um multiple users for each day if they have the same highest ratio for each day good question so in this case um let's let's presume that um it's just you just return one user in that case okay so any user in that alien user yeah okay yeah it sounds good um um i think in this case i want to do like a a window function so um i'll create another new variable which is let's call it rank and since you said that it's okay to just return one user i'll calculate row numbers over partition by date order by the ratio um oh actually i don't need to group by date um i just have to select all right because equal to one which is the highest um center received ratio but user what's the highest ratio um okay so final solution or do you want to make any kind of revision um yeah i think that's the final solution okay got it um so i'm going to give you another question so in this case um now let's just say that uh for each user return the first date when the user received zero message mm-hmm return the first date when the user received zero message and uh if the user never received zero message um do we then in that case like those users wouldn't wouldn't matter so basically for user we just want to see uh what so among the users who receive zero messages when when was it that they received that zero message for the first time got it yeah that makes sense um so i would select uh let's say we return username um messages which is database and we are only interested in cases where message received is equal to zero um and we also return the first day which is min date as um wait for each user um oh actually um sorry my bad we we only return one observation for each user so i'm gonna group my username assuming that both user id and username are unique okay yeah okay so what you're basically doing is you're aggregating at the user level uh after you apply the filter where you're only looking at the entries that have zero in the method you see um and then for each of the user you wanna you're extracting the minimum date yeah exactly okay got it um all right so that's uh that's pretty much it for the sql um let's move on to the next uh section which is on the analytic case study so this is so the so this this uh question is based on instagram and what instagram is trying to do is identify users who are influencers so how would you help instagram define um whom the who who which users are influencers or not yeah to kind of getting to to get started on this question i think the first um clarifying question maybe that i would ask is how we define a user as an influencer um and i think there might be several ways to defining them um definition we could determine that a user is an influencer if they have you know a huge amount of influence on instagram so maybe if their number of followers exceeds a threshold then we define them as an influencer or if they're if or if they have specific posts that are particularly popular so maybe not many people follow them but some of their posts went viral and so maybe the number of overall views of your posts could also be used as a criteria for determining whether an user is an influencer the other thing um that you know moving away from these definitions a little bit is whether a user is being paid for certain content that they post on instagram so um whether they do any paid ads um and maybe if they do we can define them as an influencer uh should i proceed with any particular one of these definitions or uh well i think so i think those are good so number of uh number of followers that they have number of uh overall views that they have on posts and then if they have any paid ads um those are the criteria criteria that you would use to um to identify the user as an influencer or not right yeah okay um now now uh so the so those are the measures now how would you actually bend the users into influencer or not bucket um yeah i guess in order to do that i would love to understand a little bit more about like what this definition is used for um so is is the team instagram interested in maybe getting more users into the influencer bucket to promote their business or um are we trying to cluster users into influencer versus not in order to do some kind of targeted experiment or targeted feature design or something like that in this in this in this um uh case uh we want so instagram um you know wants to promote um wants to match advertisers with influencers so uh we need to identify with the you know who the users are are they influencers or are they you know just regular consumers um this is where you need to help the team um define that yeah that's very helpful context um and so i guess in that case uh i can refine my previous criteria a little bit more so we are not primarily interested in who is being paid for ads um but instead like who has the potential to um serve as an influencer on instagram and generate ads revenue for advertisers um yeah and um sorry what was the sorry what was your previous question so so uh so like how would you actually define that criteria saying okay these are the users who are influencers yeah it's kind of like if you were building like a fraud model saying okay this is a buster or not mm-hmm yeah representative um so similarly how would you should do that for the users bucket them into influencer or not and have the model so i think there are two ways of approaching this problem and i would classify them into um you know the unsupervised approach uh versus supervised approach um in the unsupervised approach um we are interested in finding clusters within the user um within the list of users of instagram and trying to find the clusters that are that has a huge amount of influence in the supervised approach we would essentially try to obtain some type of labels on whether a user is currently an influencer um and try to classify the remaining users into having the potential to to become an influencer versus not okay yeah so and and i think the key distinction between these two approaches is that um in the supervised approach we have to come up with some ways of creating the label in the first place okay um so how would you go on about creating a label yeah so if we were proceeding with this um approach one way is to try to collect information on whether they have any paid ads in their um current in instagram posts okay and um i am not a hundred percent sure if this is true but i remember seeing some of the um influencer having these posts that are kind of labeled as advertisement and if instagram collects that sort of data then um that could serve as a useful label for this problem okay um all right now i'm gonna i have i have a follow-up um so now let's suppose that you do have this uh instagram influencer bucket now how would you go ahead and um and segment the influencer population so i'm going to paste the question here yeah and i imagine that the reason that we want to segment these influencers maybe to group them into different um categories so that advertisers with different needs can be matched to different groups of influencer is that right got it yeah and so i think you know what type of influence they have would be um really the prime the primary um variable of interest to us because we are interested in knowing what type of population they attract so if they are like a fashion blogger um let me write some potential categories um maybe they are like a fashion blogger or they are i am uh they post mainly political content um etc and so they their posts the content of their posts may say uh may wrap may generate a good signal for um what type of crowd they attract um so and so treating this as one of the features is um content uh content of posts and maybe we can do some computer vision type analysis or uh natural language processing analysis on the content of these posts to extract keywords and group them into categories um the other feature that i have in mind is the type of um users that follow them so they're followers um and if their users um you know label themselves and then you weigh on the instagram profile then we can get a pretty good sense of how what type of population they're attracting and the potential advertisement revenue they can generate yeah so these are the two main types of features that i can think of i don't care at this moment you identify the signals um now now with using the signals how would you actually perform the segmentation itself yeah um so say that we um use maybe some machine type of machine learning models to analyze their posts and the text that they post um and we can get uh sort of embeddings of um and we can get like embeddings of their content then we can perform a unsupervised clustering algorithm to try to group these influencers into different groups so one of the simplest models that we can i can think of is the k-means clustering okay there are many modifications of this that serves different purposes but yeah this may be a good starting point okay um and one last question and then we're done with the session um is how would you evaluate your cluster then um that's um that's a good question so evaluation um i think you know one way that i can think of on top of my head is if we get some human raiders human labelers to look at these influencers and then group them into categories and we can compare the human evaluation with the results that are generated from the algorithms okay got it got it all right yeah so that wraps up the session um thank you for uh being a participant as an interviewee for this mock interview um and i hope you have a good day yeah thank you so much for this question appreciate it yeah thank you
- **Labels:** `SQL` · type=hard · stage=technical_coding

### 3. `20:00` — Case Questions

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #14 | +23 с | `Product Metrics` | so how would you help instagram define um whom the who who which users… |

#### Item #14

- **Question** (`20:23`): so how would you help instagram define um whom the who who which users are influencers or not
- **Candidate answer** (`20:33`): yeah to kind of getting to to get started on this question i think the first um clarifying question maybe that i would ask is how we define a user as an influencer um and i think there might be several ways to defining them um definition we could determine that a user is an influencer if they have you know a huge amount of influence on instagram so maybe if their number of followers exceeds a threshold then we define them as an influencer or if they're if or if they have specific posts that are particularly popular so maybe not many people follow them but some of their posts went viral and so maybe the number of overall views of your posts could also be used as a criteria for determining whether an user is an influencer the other thing um that you know moving away from these definitions a little bit is whether a user is being paid for certain content that they post on instagram so um whether they do any paid ads um and maybe if they do we can define them as an influencer uh should i proceed with any particular one of these definitions
- **Reference answer:** —
- **Interviewer feedback** (`22:08`): or uh well i think so i think those are good so number of uh number of followers that they have number of uh overall views that they have on posts and then if they have any paid ads um those are the criteria criteria that you would use to um to identify the user as an influencer or not right
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

## Speaker boundary check (heuristic)

Automatic role check (no diarization): Q/A duplicates, truncated questions, candidate speech in question field, interviewer lines inside answer.

- **Item #11:** начало `interviewer_feedback` уже есть в `candidate_answer` («in that case i think marking»…). Перенесите в feedback только новую речь интервьюера.
- **Item #12:** начало `interviewer_feedback` уже есть в `candidate_answer` («so final solution or do you»…). Перенесите в feedback только новую речь интервьюера.
- **Item #18:** текст `interviewer_feedback` повторяется в `candidate_answer` (или наоборот). Оставьте реплику только в одном поле.


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
      "chapter_time": "00:09:50",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:20:00",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
