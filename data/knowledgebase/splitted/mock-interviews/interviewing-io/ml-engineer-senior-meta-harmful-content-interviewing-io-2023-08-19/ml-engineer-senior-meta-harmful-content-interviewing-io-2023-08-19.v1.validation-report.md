# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19`
- **Режим:** `split_and_validate` · **source_id:** `ml_engineer_senior_meta_harmful_content_interviewing_io_2023_08_19`
- **Старт:** 2026-05-20 21:18:06 +0200 · **Обновлено:** 2026-05-20 21:31:17 +0200
- **Длительность прогона (стена):** 13 мин 11 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 2 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ⚠️ неполный журнал (проверьте pipeline-log)
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 3 | 3. Excel | нет | — | 1 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 1 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 19 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (7/7), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 12 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 19
- **`source_id`:** `ml_engineer_senior_meta_harmful_content_interviewing_io_2023_08_19`
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
| 1 | `00:05:38` | Question Starts | — | recognized (1 Q&A) | #5 | `Communication` | ✅ | — |
| 2 | `00:07:35` | Requirements | — | recognized (1 Q&A) | #6 | `ML` | ✅ | — |
| 3 | `00:10:19` | Volume estimates | — | recognized (1 Q&A) | #7 | `ML` | ✅ | — |
| 4 | `00:14:07` | Datasets | — | recognized (1 Q&A) | #8 | `ML` | ✅ | — |
| 5 | `00:33:53` | Services | — | recognized (1 Q&A) | #13 | `ML` | ✅ | — |
| 6 | `00:42:20` | Objective of the model | — | recognized (1 Q&A) | #14 | `Statistics` | ✅ | — |
| 7 | `00:54:48` | How did the interviewee feel abou… | — | recognized (1 Q&A) | #18 | `Communication` | ✅ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `00:05:38` — Question Starts

- **Проверка главы:** ✅ у маркера 1 Q&A · ✅ по смыслу и тайм-кодам полей всё сходится (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #5 | -36 с | `Communication` | okay what is happening with this thing are you able to see what's goin… |

#### Item #5

- **Question** (`00:05:02`): okay what is happening with this thing are you able to see what's going on on the screen
- **Candidate answer** (`00:05:06`): uh yeah
- **Reference answer:** —
- **Interviewer feedback** (`00:05:09`): yeah okay I'll reload so that the bug goes off I don't know what's going on with oh oh okay you're able to see my screen right oh well you see me type sorry yeah it was some weird infinite Loop thing okay it's okay okay
- **Labels:** `Communication` · type=soft · stage=fit_hr

### 2. `00:07:35` — Requirements

- **Проверка главы:** ✅ у маркера 1 Q&A · ✅ по смыслу и тайм-кодам полей всё сходится (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #6 | -50 с | `ML` | would like you to do is think of how you will build out a system to es… |

#### Item #6

- **Question** (`00:06:45`): would like you to do is think of how you will build out a system to essentially handle harmful content removal and by harmful content and feel free to add to this this is what you mean content related to abuse content related to nudity content related to what else uh violence oops misinformation this one is especially tricky since it's hard to know but you know yeah we can think of it as an extended goal we can discuss it once we have the rest done so that's kind of the synopsis of this feel free to take over just run me through how it's here to build this system assuming this watered down version of Reddit exists how you go by that
- **Candidate answer** (`00:07:33`): um so I have a couple like questions in terms of uh uh the overall I guess like requirements Gathering um uh so I guess the first question is is like um how soon do we need to moderate content right like so somebody posts a picture um I guess like well I guess I guess even before this like is this a like reactionary system or is this a proactive system depending on the type of home well certainly like with nudity violence I think another one is called like or something like that um uh those are all things that we'd want to like take down immediately or sorry this would be proactive and then other pieces of content like uh I mean abuse is is going here as well um but like we would say for the reactive case perhaps like misinformation there's just a different thing here okay um and this is just posts and reactions to posts there's no comments or anything like that um and then uh I'm assuming there's like other pipelines that like when you you post something it's not like in terms of Reddit like the uh I guess like SLO for like uh post to feed time um is probably not on the order of like milliseconds it's probably on the order of seconds assumption here like are there other like background like data processing jobs that are actually going on in the system or will at least be the first of these
- **Reference answer** (`00:08:06`): um that's some question so I would say maybe let's try get a hybrid where for some contents or specially categories of contents that are extremely harmful we basically react and for some other contents we can maybe take a day right so we we are open to different or variation in timing in this case excellent question so you can assume you have some background jobs let's say they'll also give you the freedom to Define what job you think will be convenient and if you think uh exposing the data that they're processing either in state or after okay okay um first async system okay cool ah let's see um let's get a sense of like like what are the number of like the volume of uh posts and reactions per day um so this is like Reddit right reddit's supposed to have like 50 million uh daily active users I don't know if they're uh posting 50 million videos a day um it's probably well like then we can just do sort of like a range estimate of like in the one to hundreds of Millions of uh posts and then just a clarification a post does that include comments so we don't care about comments um it probably revise this to be down a little bit maybe like to 50 million posts per day um including the all of the content that's in it um uh uh let's see do we have a question on
- **Interviewer feedback:** —
- **Labels:** `ML` · type=hard · stage=system_design

### 3. `00:10:19` — Volume estimates

- **Проверка главы:** ✅ у маркера 1 Q&A · ✅ по смыслу и тайм-кодам полей всё сходится (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #7 | +68 с | `ML` | that so when you say 50 million posts do you have a distribution in mi… |

#### Item #7

- **Question** (`00:11:27`): that so when you say 50 million posts do you have a distribution in mind because uh you know given what you have on line six it will be good to think about how this is distributed right
- **Candidate answer** (`00:11:38`): oh I see um yeah so given like so if there's 50 million posts then like if we're saying most of the texts are posts or sorry most of the posts are text only um if we add like like most meaning maybe 80 percent um if we say 80 or whoa okay 80 are texts only um this will leave us uh uh what would that actually be um I am not good at math right now 40 million to uh uh um million text posts per day with like a mix of image and video so like up to 10 million uh images and videos per day um
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `ML` · type=hard · stage=system_design

### 4. `00:14:07` — Datasets

- **Проверка главы:** ✅ у маркера 1 Q&A · ✅ по смыслу и тайм-кодам полей всё сходится (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #8 | -85 с | `ML` | yeah do you in terms of videos in this regard are there any assumption… |

#### Item #8

- **Question** (`00:12:42`): yeah do you in terms of videos in this regard are there any assumptions you're making with respect to what the size of the video is gonna be as well as what the input format is going to be so are you thinking somebody will upload an actual video or will they link a YouTube video a video video that's gonna be let's say rendered with an iframe in Reddit
- **Candidate answer** (`00:13:07`): uh yeah so um good question my assumption is um uh that's true so so text can have links um uh so that'll be something to consider we'll need like a link detection uh deal here service um if the if there's a video I'm assuming the videos are direct uploads so we'll be able to like analyze them within our system um these are like directly attached um yeah because otherwise it's really hard to moderate if somebody's adding like a YouTube embed I mean one we assume that YouTube is doing their own moderation they're doing a good job and two like if there's a sketchy link then what we may want to do is actually like um uh cue this stuff up so I guess the next um question is like do we have some data sets around of existing content that is like labeled um or is there like um or like do we need a um labeling slash like uh manual review system so that mechanism uh from what I'm familiar with uh is basically like the way the mechanism is structured is uh they monitor the number of uh reports um if reports exceed some threshold a cue or manual review and then we get the labels there um so in terms of data set size and distribution can we assume that the training data that we have is um mirrors the uh like mirrors the population data set distribution um like like an assumption is maybe like images are more frequently moderated than text only and so like it could be the case that the data set has like 50 50 images 50 text whereas we're getting 80 tax from our like prod distribution I see so I'll yeah I think it's fair to assume that the rate of report should the size of the data set in this case especially since uh you know from my uh point of view any abuse is always going to be abuse so once it's in the database we can always reuse it in the future so to a degree it's kind of hard to argue that the distribution of data we have currently will be the distribution all the time but for now I think for Simplicity purposes I think that's a fair assumption to make at least for design purposes okay right yes in addition to that I was actually going to suggest might it might be worth thinking of dated risk ahead of time in this case because you know one year ago or two years ago even five years ago we remember images of the thing like you know it was a bigger deal but now with the age of tick tock now that's a bigger deal right people are looking at videos more often and this is why like I'm saying it might be hard to argue that the distribution will stay static but at the end of the day the data is always going to be the same it's always going to be abuse right yeah yeah and then and then uh another question is like what percentage um of posts are uh marked harmful so I'm assuming it's in like a one to two percent range kind of thing here um right um the last thing I think uh I wanted to cover here well I think I have enough in terms of like requirements um to kind of move forward here the like I know it's um in terms of like machine learning today like multi-modal is starting to really take over where you can just sort of give a machine learning model like I think Salesforce came out with instruct blip like two uh pretty recently and you can just like feed it um feed the model like kind of anything and it'll all figure out like um whether the model is uh or sorry it'll figure out like whether the the actual like content is uh something like abusive or violent or might be misinformation or something like that um the more like traditional way of setting it up is just having uh like kind of one model per um uh modality um and so like like that's the system I'm more familiar with but I like today if I were setting this up from scratch or even just like joining a company I'd really look at multimodal uh first to see if there are like wins there and then um but the system I'm proposing for the interviews and what I'm more familiar with which is just uh um unimodal right um
- **Reference answer** (`00:14:33`): excellent question so online 31 I'll make reference to line four so feel free to make assumptions about having a human in the loop so we will actually have a continuous stream of uh some of the posts that will be labeled depending on the category so we do have humans in the loop and we actually do have a mechanism available for reports okay cool yeah so I see so I'll yeah I think it's fair to assume that the rate of report should the size of the data set in this case especially since uh you know from my uh point of view any abuse is always going to be abuse so once it's in the database we can always reuse it in the future so to a degree it's kind of hard to argue that the distribution of data we have currently will be the distribution all the time but for now I think for Simplicity purposes I think that's a fair assumption to make at least for design purposes okay right yes in addition to that I was actually going to suggest might it might be worth thinking of dated risk ahead of time in this case because you know one year ago or two years ago even five years ago we remember images of the thing like you know it was a bigger deal but now with the age of tick tock now that's a bigger deal right people are looking at videos more often and this is why like I'm saying it might be hard to argue that the distribution will stay static but at the end of the day the data is always going to be the same it's always going to be abuse right yeah yeah yeah and Reddit is crazy so yep that's a fair function maybe right it's like five percent I don't know yeah with that platform yeah three days a lot but yeah I agree yeah or like Twitter um yeah so uh uh I guess
- **Interviewer feedback:** —
- **Labels:** `ML` · type=hard · stage=system_design

### 5. `00:33:53` — Services

- **Проверка главы:** ✅ у маркера 1 Q&A · ✅ по смыслу и тайм-кодам полей всё сходится (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #13 | -76 с | `ML` | about the API so given what we have here talk to me about some apis we… |

#### Item #13
- **⚠️ границы реплик:** текст `interviewer_feedback` повторяется в `candidate_answer` (или наоборот). Оставьте реплику только в одном поле.

- **Question** (`00:32:37`): about the API so given what we have here talk to me about some apis we might want to design in order to solve this data uh yeah so
- **Candidate answer** (`00:32:48`): um uh let's see um so I could see like a few different uh systems here I mean so the idea is that we kind of said we're going to do um uh single modal um uh inference and um inference in this case it could be done uh as like a a batch inference or online um to me they kind of like both uh work um because talking with an async process um but also like the this data is kind of coming in as a stream so like uh to me I think it's just um like easier to kind of uh model it as an online uh inference system in just sort of like a little more future proof if you do need it to be more real-time it will still be there you don't have to migrate from batch to real time um so like there's basically going to be three services uh one for image one for text and one for video um so maybe it's like moderate um seek and say service dot moderate and then uh the request um should be like post requests and if we're thinking about like what kind of data we want for the body um uh so we should have like features and then we'll uh pass in a list of features [Music] um the I guess like should the I mean the services should be doing the same pre-processing that we're doing to uh generate the data and and train the model with it um so uh I think like these features I mean in in reality the way this would kind of work is that you use like feature IDs and then sort of work through some kind of a feature store um so this is actually something I didn't cover but I feel like we we should talk about is um uh it's not just um image text and video but also like user profiles might also be something that we want to like consider at least in the the future so it's not just like show me an image it's like show me um an image by a like particular user and then maybe that helps with identifying um things like misinformation like if a if there's a post and that user has been reported a number of times maybe that actually like positively impact um but maybe that's like a I'm like sorry I'm kind of thinking out loud here I'm a little disorganized I think um I think having the three services here and then another service a fourth one for just uh text misinformation that makes sense these are a lot easier to um moderate and then uh with misinformation it's a little more subjective and uh the model may end up having features in it that the text model uh uh doesn't need to include so that's why I'm kind of like uh building this out as a separate service here um so for uh this API um you'll pass in a a list of features maybe it's as simple as just saying like a dictionary and then we can say the text for text right um One Two Three or or um uh same with images it'd just be the blob or video um uh so the blob and the bite and then the same thing with the video right so that's just the the kind of the Epi there uh and then the response is going to be a list of um uh labels and uh confidences so uh you'd say like results and then so we'll have like a label and then so we may want to say like this is like the abuse label and then we can give a like a confidence uh and then this will be a float between zero and one so this could be like um and then like we can have other labels here as well so we'd have like labels for nudity violence um and then um yeah please these would be like the labels yeah um so that's basically the uh the apis of the service um in terms of like uh there's a few important things here um uh which is like as a system as a whole there are uh well the thing I want to touch on is like there's training metrics and then there's online metrics and like how are we doing um uh so for things like online metrics uh like actual production metrics we want to cover things like the number of um we call it harmful uh uh oops we'll call it harmful impressions um and so that's just the number of people that have seen these things uh and then like number of reports nice nice and uh uh maybe even um uh so there's um Impressions and then also maybe like a time-based one so like uh average time um to take down so when we when something is like posted reactively and we need to take it down we want to be able to take it down quicker and hopefully models will facilitate that that take down time um in terms of actual like uh training metrics uh some of the things that um we want to like consider here so when we're training on image text or video we're doing a um a multi-class classification um which means that we'll be doing a uh orals that are mixed up all the time it's um oh sorry um yeah yeah so uh we care about uh uh and recall um and so Precision is basically the uh number of uh true positives divided by um the two positives plus the false positives and the recall is two positive is divided by negatives in terms of like uh how we want to actually like present this I think just presenting in terms of precision and recall like you don't have to do an F1 score or like a receiver or operator curve just leaving his Precision recall works
- **Reference answer:** —
- **Interviewer feedback** (`00:38:17`): yeah
- **Labels:** `ML` · type=hard · stage=system_design

### 6. `00:42:20` — Objective of the model

- **Проверка главы:** ✅ у маркера 1 Q&A · ✅ по смыслу и тайм-кодам полей всё сходится (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #14 | +0 с | `Statistics` | sorry quick question objectively speaking because uh given this metric… |

#### Item #14
- **⚠️ границы реплик:** начало `interviewer_feedback` уже есть в `candidate_answer` («saying is we are okay rather»…). Перенесите в feedback только новую речь интервьюера.

- **Question** (`00:42:20`): sorry quick question objectively speaking because uh given this metrics these training metrics are there can you define to me the objective of the model and yeah um so that there's you're talking about like the loss function and not necessarily the most function we can speak on that later given we have a multi-classification problem here but I'm interested in what is the goal like do you want to minimize Precision while maximizing recoil or do you want to maximize both like what's the goals particularly
- **Candidate answer** (`00:42:52`): yeah so I think um uh so this is actually interesting because like it depends on the business um objectives and time so I've actually seen that at my company where um we basically said like for a while we were okay with businesses um we were okay with uh um being very strict in terms of of I want to say like false negatives and then economic downturn kind of happened and then we kind of said like hey we don't we don't want to be um uh we want less false positives because we want people to actually spend on our um platform and so we were actually willing to trade off like recall I think back for precision um or by any other way but like business metrics but if you're if you're trying to um juice engagement then uh you want to be careful with um uh I think it's okay so false negative in this case would be um classifying something as harmful when it's not and so um uh if you're trying to like juice engagement metrics having a very um uh High precision and low recall is good um because if you have high Precision low recall what we're basically saying is we're trying to um we're okay with like harmful content making it half the model uh because we don't want to block like good content so in this case essentially what you're saying is we are okay rather than being less sensitive and as missing on actual abuse contents like it's okay if they report something and they find out it's not harmful and restore it rather than the opposite way they failed reports or we fail to plug and excellent so we're basically making our thresholds very low forward abuse or or a flag for abuse
- **Reference answer:** —
- **Interviewer feedback** (`00:45:01`): saying is we are okay rather than being less sensitive and as missing on actual abuse contents like it's okay if they report something and they find out it's not harmful and restore it rather than the opposite way they failed reports or we fail to plug and excellent so we're basically making our thresholds very low forward abuse or or a flag for abuse but tell me of course we have the human in the loop so we'll always have a restoration process but those who did that yeah I think that's an excellent approach and I was actually very happy with that because I was gonna Grill you after that on that point like would you want it to be you know the opposite and why but I think you immediately went to it which was accident yeah and then yeah
- **Labels:** `Statistics` · type=hard · stage=system_design

### 7. `00:54:48` — How did the interviewee feel about their performance

- **Проверка главы:** ✅ у маркера 1 Q&A · ✅ по смыслу и тайм-кодам полей всё сходится (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #18 | -4 с | `Communication` | but for context I never give feedback straight up I usually want to fi… |

#### Item #18

- **Question** (`00:54:44`): but for context I never give feedback straight up I usually want to first get your intuition so looking back at the interview what do you think you did well and what do you think you could improve I think
- **Candidate answer** (`00:54:55`): um I did all right with the initial part um the sort of like requirements Gathering uh I definitely need to go deeper well I got like stuck on the tokenization uh piece um so like I think there's just a little bit more focus on some of the machine learning aspects of things like you know what are some of the more like common like pre-processing Steps tokenization looking at like the different scalings and things like that like doing log Transformations when your data distribution isn't exactly uh gaussian things like that I need to just like Refresh on um uh I thought like the API endpoint part was fine um yeah like I don't know if there's anything like really glaring there um uh I mean ultimately I feel like you know I'm not sure I mean I called it out in the beginning which was like we really should be doing a multimodal system that's just like more intelligent I I have a feeling that that would actually perform better um but like um so I'm glad I called that out and then went with the system that I'm a little bit more familiar with it's like it actually likes each of these things um I'm not actually sure if it's like better to do it that way uh in a real interview or if it's like by going this way I'm giving the interviewer an opportunity to dig on like like let's talk about image related models let's talk about like text related models um versus like potentially um like if I'm saying let's build some like multimodal system and the interviewer doesn't know how to or isn't familiar with multimodal systems than like I'm not sure if they're getting signal so I'm not sure if that's like the right path to to take there um I did just like I need to just do better on my loss function stuff um and uh uh just kind of yeah didn't get that piece um and then uh I mean other than that like I think everything kind of um did all right so that's sort of how I I feel like there's some ups and downs um definitely not like the perfect interview
- **Reference answer:** —
- **Interviewer feedback** (`00:57:30`): here's the thing I rarely find a person who finds out for mentorship but then at the end I'm telling them I will probably give you a pass so you actually be pretty damn well so I still took it still took a ton of notes as I said uh so you know to start with keeping it short I frankly think you're almost there like uh it was to give you like feedback in case you want to sign up for more sessions you probably need at most five if not three three just to kind of refine the process because in terms of content you probably are one of the few people been able to keep up with the line of questioning I've asked which was excellent so you know just to go through the feedback and mind you'll paste all of this in in addition to some extra resources you can look at at the end for the most part I agree with you but you know objectively communication excellent like you're really easy to communicate with easy to follow even throwing jokes on occasion in the interview which keeps it light-hearted so really really did well with that and then the line of questioning with respect to background processes I really really like that because most people fail to think about that they think they have to design Reddit in fact one of the biggest problem I've had with candidates is you ask them to detect how to design a harmful content protection process but they don't think about the background processes that exist so you started with that make it a point in any interview like nobody is asking to design the actual system they are designing a new system in exist in addition to the platform that's already there so feel free to denote exactly what you think already exists and maybe this is where one bit of improvement you can have here is actually detailing those bits so if we expect that let's say ready to give us apis that can extract text or alternatively if we expect that you have a push model where if a post is made a model automatically consumes that post or you know has that post uh pushed into let's say some message queue where we can consume it and process it it will be good to talk about it from that stage and in fact for most my most machine learning interviews I think that's probably the best Stage to start it just thinking about what's my input like what's the current platform giving me in terms of input of course yes it's not like a you know platform based system it could be different but typically data source is always the first stage but it was really really good to hear you actually talk about that because it shows that you had the intuition to think about that bit and then uh on line 85 I mentioned the pre-processing bit I felt as though you were not thinking about it until I pushed you in that direction and so okay right like you know I had to actually ask you okay how are you going to standardize this how are you going to pre-process it but once I asked you you went in depth on tokenization pre-processing removal of stopwatch it is key to think about that because part of the ml system design but sometimes you may find that that's the state that requires the most ml system design work because these are heavy processes like you can imagine uh you know when you have a bunch of images or even let's say videos where you have to do frame sampling then that's computationally intensive and it's usually what we're thinking about how that setup is going to look like what those features you know once you've extracted the features because this is basically the feature engineering part once you've extracted them where you're gonna store them because you know you don't want to process all of that and then all that data is basically output into some log file you want to actually think about the data output in that case talk about let's say readys or whatever you know data ta and storage solution you have where the model can consume from there in a quick manner so it might be what I was talking about API endpoints there maybe talk about them being marked by let's say I don't know ready for some other systems so that's stage one of the system design and then you know I give you a breakdown you can clearly see online 82 on how I typically do it it's kind of worked well for me maybe it can inspire you to curate a process for you so typically it's usually requirements pre-processing and then Define my apis both the input and output before I even jump into the model stuff and then I think we delve deep here yeah I actually made the point on that you went deep into it so I didn't really have any line of questioning on that so that was good so for the tokenization bit I think we kind of covered much of that conversation in the interview but Refresh on that that way at least you have a stronger sense of the intuition between of the implication or performance between shorter than the Lord so clearly that's probably the weakest point of the interview because I felt like we were going through like you know kind of like throw something at the wallet see if it sticks but for the most part it was good that you even knew of the different education strategies even went to a level of giving me examples which I could identify so I really appreciate that and then yeah like let's see I think this is the same point I've made there where pre-processing is always step one so it was good that we talked about that and then in terms of output I felt like you really you know once you were done with like the core apis the rest of the stages are perfect like it was like you talked about the output you expect in fact uh the funny thing when you said the API was okay to me it was like this is probably closer to what I would want to see in an interview where somebody actually gives me example payloads I always ask for example payloads most people won't give that so this was actually really really good so the only maybe you know there's a myths I would say maybe include the expected protocol for the for machine Learning System design I don't think I'll push anybody down to that uh you know up to that level but the reason why I might want to converse about that is sometimes it's worth thinking about let's say the concurrency or the number of requests I expect so if the API it is gonna it's gonna expect a lot of let's say get requests get requests tend to be more performance and let's say post requests so when you're talking about that especially in this case you know there will be a lot of text request coming in like as soon as the post is made that request is made so there should be a ton of them especially since the share volume is going to be a lot but most of the payloads will be tiny so in that case we probably want to have lightweight post requests in this case you know those maybe the downside might be since most uh most uh of the requests will correspond to a unique thread then maybe post my touch is that actually good is it supposed to put like in terms of method because I want to create a post is kind of a well like there's there's two ways to think about it's like rest and then there's just like Json or PC um so if you're thinking about it in terms of like rest a post request is more intend to create something and a put is like a update on the full entity people who like grpc is all post requests even if you want to get something um I see which one is the one that has bad impotency I think it's a post uh like in terms of like a session Aid and potential I can't remember which uh uh I mean I would assume like poets or I mean they're both supposed to be item potent I think uh it's it's uh um uh yeah I don't think it should matter like like for instance if you're doing a endpoint you want to post to like create the payment um but that's the item potent like if you try and call it twice um it needs to like have the same result today yeah actually I do believe put is actually item uh put his either important well post is not so and this is actually the key bit right there so if we made a put request especially since we know most requests will not be updating they'll be sending this one request to the process we're done and that's where maybe you can justify both because we you know I don't think we worry too much about reprocessing the same thread but the downside might be if somebody decides to spam our system then once they start sending threads and you know maybe they know we are pre-processing them for this or whatever so they just send like 20 30 threads if you are processing them using post each and every thread will be processed but if you're using a put type of request then once they've done it then we kind of Might monitor the session although if it's let's say along the same request line then yeah you might yeah so you know we could have a conversation on that much you know you kind of see why depending on user Behavior the method might be worth talking about but other than that most of the content was perfect in fact I really really appreciated that you thought of the multi-level approach without prompting I've honestly not had anybody immediately think of that so you've done a good job with that like a photo value you're going to prevent them in terms of multiple labels and then yeah I think I break this down for you in order to like give a sense of the sequence of steps yeah for the most part you know oh I think we already touched on the precision versus trickle bit honestly I'm not going to agree on that because I know I struggled with that too so without a suggestion ahead you just use a computation Matrix that way you avoid having to talk of the terms themselves but that said it always looks good if you immediately talk about it without even defining it because it kind of gives that interview the illusion that I work with this Matrix regularly I know what they mean so I don't need to think too heavily about what they mean so you know just essentially just review the review the resources to kind of have a sense of what high Precision low Precision means and then maybe I forgot to mention this but this objective the objective function or the objective of the of the modeling all together it might be something we want to highlight in the initial stages but you know it's totally understandable to talk about it even at the end I felt like you know it gave the interview a more natural flow but at the end you know you want that optimization in terms of process so maybe try and touch on it right at the get-go that way you know it's not something that you might miss out on let's say the interview is kind of hard and like you're stuck with some steps you want to just knock it out of the way because it's easy to do and then keep going yeah yeah for sure but other than that as I said
- **Labels:** `Communication` · type=soft · stage=fit_hr

## Speaker boundary check (heuristic)

Automatic role check (no diarization): Q/A duplicates, truncated questions, candidate speech in question field, interviewer lines inside answer.

- **Item #13:** текст `interviewer_feedback` повторяется в `candidate_answer` (или наоборот). Оставьте реплику только в одном поле.
- **Item #14:** начало `interviewer_feedback` уже есть в `candidate_answer` («saying is we are okay rather»…). Перенесите в feedback только новую речь интервьюера.
- **Item #17:** начало `interviewer_feedback` уже есть в `candidate_answer` («doesn t really make sense and»…). Перенесите в feedback только новую речь интервьюера.


## Check 3. Semantic field alignment per chapter (step 5, LLM)

The Cursor agent (same as step 2) reviews **extracted** Q&A: field timestamps vs chapter windows and whether texts match chapter titles and labels (`question_topic`, `question_type`). Does not change the overall verdict.


- **Статус:** ✅ все 12 глав без замечаний
- **Тайм-коды полей:** 12/12 ок · **Смысл/метки:** 12/12 ок


## Transcript spans without Q&A in JSON

Intervals in `timecodes.txt` not covered by any item span. Check for a missed question or service speech.

_No large uncovered spans (threshold: ≥25s, ≥4 timecoded lines)._


#### Короткие ответы кандидата (≤4 слов)

Проверьте по транскрипту: это **осмысленный** короткий ответ на вопрос, а не обрезанный span или пропуск речи кандидата.

| Item | Время | Ответ |
|------|-------|-------|
| #5 | 00:05:02 | uh yeah |

<!-- SEMANTIC_VALIDATION -->

## Semantic validation (step 5)

Машинный ответ LLM (шаг 5). Валидатор читает этот блок при повторном прогоне.

```json
{
  "chapters": [
    {
      "chapter_time": "00:05:38",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:07:35",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:10:19",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:14:07",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:33:53",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:36:35",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:38:40",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:39:54",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:42:20",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:53:40",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:54:48",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:57:30",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
