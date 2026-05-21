# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10`
- **Режим:** `split_and_validate` · **source_id:** `ml_engineer_senior_meta_yelp_recs_interviewing_io_2026_04_10`
- **Старт:** 2026-05-20 21:18:06 +0200 · **Обновлено:** 2026-05-20 21:31:28 +0200
- **Длительность прогона (стена):** 13 мин 22 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 3 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ⚠️ неполный журнал (проверьте pipeline-log)
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 3 | 3. Excel | нет | — | 2 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 1 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 7 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (2/2), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 7 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 7
- **`source_id`:** `ml_engineer_senior_meta_yelp_recs_interviewing_io_2026_04_10`
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
| 1 | `04:54` | Problem clarification and busines… | — | recognized (2 Q&A) | #5, #6 | `Communication`, `ML` | ⏳ | — |
| 2 | `42:19` | Self-evaluation and feedback | — | recognized (1 Q&A) | #7 | `Communication` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `04:54` — Problem clarification and business metrics

- **Проверка главы:** ✅ у маркера 2 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #5 | -2 с | `Communication` | having said that, do you have any other question for me? Otherwise, we… |
| #6 | +65 с | `ML` | So, what we're actually designing today is we're designing like the Ye… |

#### Item #5

- **Question** (`04:52`): having said that, do you have any other question for me? Otherwise, we can start like with the mock ML system design.
- **Candidate answer** (`04:59`): Um no, I I've read the the prep guide from them. So, I think I understand what's coming up. I'm ready to go.
- **Reference answer:** —
- **Interviewer feedback** (`05:07`): Okay, perfect. So, what we going to do, we're going to switch over like to the to the whiteboard. And then what I'm expecting from you is to lead the whole design because this for a senior position, you might ask some clarifying question, but I will leave the time and space for you to lead the whole design. And then I will interrupt you at around like uh 43 mark and in order like to switch over like to feedback. So, also keep an eye on the time. And I might just sit back and I will only jump in and interrupt you if I want to ask like a a question. But the expectation is for you to lead the whole design. Perfect. The reason being is that during like the interview, you're also being evaluated on how you handle ambiguity, how you make a reasonable assumption, and you move on, and you unblock yourself.
- **Labels:** `Communication` · type=soft · stage=fit_hr

#### Item #6

- **Question** (`05:59`): So, what we're actually designing today is we're designing like the Yelp system, the recommendation algorithm behind the Yelp um system. Yelp recommendation system. Um so, this is like on the homepage, like you open up Yelp for the first time it today, and then you see a list of recommended venues, like they could be restaurants or bars or like any like place on the map, basically.
- **Candidate answer** (`06:40`): Got it. Um okay. And this is Is this just on the homepage? Are we thinking about the search system as well? Okay, so a user will come onto the page and given everything we know about them, um what's in their immediate vicinity, um what's open, we think they're going to we will show them the uh places that we think they're most going to want to visit. So, what Yeah, so what would we consider um to be like the thing that we're trying to optimize here? I guess it would be whether somebody actually visits the place. Um like how does Yelp make money? Okay. Okay, so so Yelp has a list of venues that have some either like a restaurant with a meal or like a laser tag place where you could sign up for an hour, but there's something uh where a user can convert for that venue. Uh and we want to like make sure like make that as like likely as possible that the user will convert whatever conversion means for the venue. Um I guess like do we get paid based on like if like you make a reservation for like I don't know, uh like $80 at a laser tag, like we get paid proportional to how big the the payment was for the reservation. you know, we want them to click on anything at all and and convert or we want to like optimize for I guess we maybe going to let people um or like I should say that the venues uh list their own prices. Um but yeah, we probably would want people to It's probably like a balance here between we want people to click on expensive reservations that we get a higher um commission for. But then we also don't want to like only show expensive things and then the user doesn't click on anything. Um and we should have shown them something a little cheaper. So, there's like a bit of a balance there. Um okay. what else should I think about? Um um Okay, so yeah, like we assume that the all the places that they're going to see are open and you can make a a reservation that night or I guess like sometime in the next week for for the venue, right? Like it doesn't really matter when the reservation happens as long as it happens during the session. Like they make the reservation during the session, right? Um What Okay, let me think about So, okay, so um Let me think about what we're trying to Okay, I think I have a sense of what we're trying to do. Um and we we Yeah, we want to uh increase I guess the the the online metric that we care about. I'll start writing things down. Um online online metric is Well, yeah, so like we get Do we get like a Is it a fixed commission? Sorry, I may may should be clear. Is it a fixed commission per click? Or do we get paid You said we get paid proportionally. So, so I guess like um total like the uh I hear a a being Oh, did you disconnect? No, I can still hear you. Okay, cool. Cool, sorry. Um So, I guess what we're going to try to optimize for is um the like total revenue generated um across all sessions uh through conversion. Like that's that's really what we're trying to optimize for. Um And then I'll think about what what we're going to be tracking in training uh towards that goal. So, Okay, so the general I'll maybe I'll talk about first um like what the end-to-end flow is going to look like. Um first from like when the user opens up the app and sees something and then um we can we can dive into different parts and and explore how how those work and like leading up to the inference. So, uh inference time um user goes to their app and then they make a request for So, at a certain time, they they open up Yelp and they want to see like given where I'm at um and what time it is uh what are all the places that I might want to look at right now. Um and maybe other day make a reservation for for tonight or for for somewhere down the line. Doesn't really matter as long as the session ends with a conversion uh where we're successful. Um So, then when when Yelp gets that um user request for for the homepage then we go into some sort of index of I guess like all the um So, this is like the Yelp server. And then we have an index which contains every um Yeah, these are just primarily venues, not like the events themselves, right? Um Right, so we have some sort of reverse index where we we know like where the location is, whether it's open um some basic things like that. I'll get into more things we know about the venues later. Um And then we we we get some sort of candidate set of of all the the potential venues that that are at least like within driving distance or or uh I guess I guess it doesn't have to be open right now, right? Because if we can make a reservation for like 5 days from now, then we don't have to really care if it's open at the moment that the user um goes to it. So, I think it's more important that we just see where the user is and find nearby places. Um and then the the index returns some candidates which we would then rank uh by some means. Uh and maybe just like something like a combination of like just clicking um clicking or converting. I'll think about that, how to balance between the two. Um And then we'll we'll serve up to the user whatever has the highest score. Maybe um if if we're optimizing for conversions, we could we could rank by that. Um but I guess given that that most people like that that the number of like the number of clicks across all views um is, you know, not that many. Like maybe like I don't know what the conversion may be like Well, if you're on the app, you're probably going to be looking at a few places. Um but like for all the items, maybe there's like a 10% chance that a given item gets clicked in a in a session. And then of those um that you convert is is like an even lower funnel. Um So, I would imagine that there'd be um like generally more like there'd be more positive labels in the click um like in the click data set and is it converted. So, maybe that would be make more sense as as like a primary filter. Maybe it could be like two stages depending on how large the um the candidate sets are. Of like first you could you could rank by is it going to get clicked? Um and then within those you could re-rank by like you once you once you cut to a cut-off of like the top I don't know, 50 most likely items to get clicked on, you could re-rank by the most like the the the likelihood that those would get a conversion. Um and then show the user from those uh 50 re-ranked. So, okay, anyway, sorry. I'm I should finish the end-to-end first. So, yes, the reverse index um would then I don't know how to represent a model. Uh Let's let's just call it like um some sort of let's say PCTR model. Oops, sorry. Um Right, which which then um Well, let's let's say for now, even though ultimately we care about revenue, we we we start by just predicting clicks. Um So, yeah, that's that's the overall flow at inference time. Um of how that would work. And So, yeah, let's talk about what kind of uh data we have available um before we talk about yeah, what kind of model we would make based on that data. Yeah? So, we have venues um and users and um I guess yeah, the way that a user's interact. So, so Yelp has Right, and then venues have different types of events. So, like a user who's going to bars is going to Yeah, I guess that's like a category of a a venue. Um All right, let me think of a few. So, there's there's like the free form text that describes it's or it's sorry, it's um it's name. Excuse me. Uh it's address. Um the owner's description. It has associated reviews across all things that people do in it. Um which are left by users, obviously. And uh we know the price of the uh whatever the the reservation. Um And then I'll just I'll just hop around a bit and I'll I'll jump back in if if I think of something else. So, a user and then like user um in a session. Just to make that clear that like this is what we know at inference time. Um So, we know what time it is that the user is browsing. The location that they're at. Um we know the history of past reservations. Um We know I guess like reviews that they've left. And Can you like Are you friends with other people on Yelp? Is there like I I guess that's not really a major feature of it, right? Is like the network of like where did your friends go out to, right? So, yeah, and then like we need some sort of I mean, I was Yeah, maybe like just a easier like predefined category instead of like just relying on this free form description. We give them certain categories that um like a taxonomy that they can fall into. We can maintain this taxonomy ourselves. The taxonomy could itself be like like some taxonomic classification. So, you could have like, you know, at a high level, nightlife. And then below that um uh like a bar versus a club versus a jazz venue. And those are like nested. And and then like yeah, you got a venue could have um multiple like levels of granularity of of classification there. Um Okay, so I think I think that's a that's enough to get started with. Uh or Okay, we also have our sessions. Um So, like historically, what is a what has happened on the app with regards to like what when a user um like saw a particular venue um and it was at this or Yeah, so a a a user so a So, a session is composed of a user looking at multiple venues at a certain like um position in the like like uh the results and then was clicked like did convert by the end of that session. Um which we should we should know that. Uh of like start time. Okay, so these are Oh, sorry. Um Right, so so that's that's what we know about what's what's happening. That's what we're trying to predict at at inference time. Um So, let me think more about um yeah, what what is the the the training objective that we're trying to optimize for. I guess um it might be like a combination of like did It's either we we could separately consider our success in predicting clicks and conversions or we could come up with like one overall uh metric that combines both of them. Um  Yeah, I guess I guess to keep it simple for now, I would rather just focus on predicting clicks and then I could think about how I would expand it to incorporate uh conversions as well later. Um Okay, so let me let me think about how to build like a um a training pipeline uh to to determine if someone's going to click on on a given results and then I'll Yeah, I'll think about um Yeah, we we don't really have to focus or maybe should I I Okay, I was thinking if I I need to worry about like building up the index properly um because like you know, like given given like uh a definition of the index that's going to determine what's even in or Sorry, am I am I like going to cold start this like from scratch or should I assume that a system already exists and I'm iterating on it? Um okay, so initially we're not going to have any sessions. We're not going to Right, all we're going to have is venues and users. So, initially we have to bootstrap this somehow um with with some heuristic metrics. So, I think before we get into like modeling anything um I would want to suggest that people visit popular uh venues in their area. So, um All right, so initially what kind of data So, okay, so so So, this is bootstrap So, this is like Yelp doesn't exist or Yelp is just a pure like database like you just search for things, but we don't like show anything on the homepage by default. where So, we we are giving uh people like things to possibly click on or convert to and we know whether they did or not. Um but yeah, those heuristics might be Yeah, things like uh I'm assuming um is it is it a popular venue in the area? Um does it have like a deal going on right now or good discount? I guess what I'm trying to say is there might be um like newer up-and-coming venues that aren't going like I don't know if if our old system has the ability to like balance exploring new venues versus exploiting ones and we have to come up with a way ourselves of of like randomly introducing like newer low PCTR uh items into people's feed just to get them out there and get information on whether people like them or not. Yeah? Right. So, yeah, so if I was Yeah, if I had the original system, then I would have some sort of basic uh yeah, like popularity metric and and I guess I don't know if we have like an ad system. Um or like based on like number of like good reviews, we do have that, right? Um which is a list of list of reviews and a review itself has like a numerical rating I guess out of five and and possibly photos and um and a text description of of the whatever, maybe like the event itself. Um text star rating out of five photo optional. Um and So, so yeah, let me let me think about how how I build a model which would um which would predict click given that Oh, the Yeah, as I said you even with the with the bootstrap model, it's going to be the case that most people like for the most part people aren't going to even click on a lot of the results. Um they're going to scroll through and then click on only a couple. So, there's going to be class imbalance that I'm going to have to address at some point. Um Maybe Yeah, and Yeah, given that I care a lot about um more about false Hmm, okay, so a false positive would be I show somebody something I think they're going to click on and they don't click on it. I mean, maybe they would think that I'm not really good at knowing what they like, but not a not a huge deal. If it's a false negative where there is something in my catalog that they could have clicked on, but I didn't show it to them, then that's potentially missed revenue. So, I guess I would And Yeah, and like given that clicking is a rarer thing, I would want to um maybe have a uh like a larger penalty for for missing uh like if the model predicts that they weren't going to click on it, but they actually would have, then that would that would incur a larger penalty than than the reverse. Um Okay, so Yeah, like for for setting up the training um system, I need to I need to create like a unified view of a user at a given point in time. Um I think it maybe should be Yeah, like pairwise. So, for for a user for a venue um predicts likely here that the user would have clicked on the venue um at the point of of browsing it in their search results. And then I guess Yeah, maybe some sort of offline metric that I would want to track would be if I'm just predicting like this this binary um label uh but it's it's showing up in a ranked list, then I'd want to use something like um discounted cumulative gain to uh assess like how well the the ranked results was um given that I like ran a simulation um and tried predicting the uh Yeah, the the likelihood of click for each item in the ranked list. All right, so I'll just add that offline metric and DCG for some n um posts at the top that that we care about uh for clicks, I guess. Um Okay, so so I think I'm going to Yeah, I'm going to build a a like Let me think. I guess I could start off by building a uh a vector that describes both the user and the um and the venue. And initially, to keep it very simple, I I could use some sort of linear model uh that that predicts, um, yeah, that that it produces a value between zero and one, uh, by feeding that through a sigmoid like a logistic regression, um, which predicts likelihood of click for a pair. And then we can think about making that more complicated, uh, if if we want to capture, uh, cross feature relationships. Um, but just to get something off the ground, I think I think logistic regression is is a fine start. Um, so yeah, let me think about what that would look like. Um, I think I'll just build up each each in uh, part of of this this vector at once or on on each side. So for a user,  um, yeah, I guess like given the time that they're browsing, if they're like looking for something to do right there and then, which I'm guessing is a lot of the time when you go on Yelp, it's not like just like plan out the the rest of your week, it's like I'm currently out somewhere and I want to find a place to go. That's probably the majority, I would imagine the majority use case. So, um, I want to have a sense of their, um, their city. So maybe like, yeah, so just the well, the city is already being used to do the filtering from the from the index like to to retrieve things that are close. Um, so maybe so I have user features, uh, venue features and user venue. Um, so I guess what I was trying to say is that um, like the the distance from a user to the venue could be something I'd want to use, but then that's very different in like Austin versus New York, right? Um, the like I you can drive in Austin, but you don't drive in New York. So then you could tend to go to you're willing to go further, relatively speaking, in Austin. Um, so I I guess maybe I I I'm just going to like throw something out here. Um, maybe like distance to venue divided by like something like city diameter. It's it's like a really rough, uh, ratio like like distance ratio. Um, just something to like normalize it, but I'd probably think about like whether it's like public transit or something. Um, and then uh, for the venue like is open as a bool, which mean yeah, again, we could we could still show venues that are closed. And obviously they're like when they're sending a Yeah, I'm not sure like there's like the balance between do I put this into the model or do I just like rely on the user doing the filtering themselves? Um, so they wouldn't even like see, let's say, um, venues that are closed if they're looking for something right this moment. Um, so I'll [clears throat] I'll think about whether doing cool like yeah, I think I'll just include everything by default. Um, but like I'll think about to do um, how to balance Maybe I shouldn't put it here, but uh, how to balance between uh, users doing filtering versus using uh, venue attributes in the model. Um, okay. And then So we have the address and then we have maybe like, um, average rating um, past month. Uh, sorry, did you disconnect for a sec? Excalidraw that's like you reconnected. Anyway, so I'm thinking about, um, yes, I want to know if it's a good venue, but then this is going to potentially penalize new venues who don't have many ratings yet. Um, so maybe there's some way of like normalizing this by like the the the the ratings that the venues received based and then like the number of ratings. Um, yeah, I'm not sure how to formulate that right now, but I'll think about that. Um, how to consider low rate Maybe like you have some sort of like, um, for the city you have like, uh, prior under like a prior probability of like what the average rating is for different venues of different categories at at diff like at different points in the life cycle and then you like use that as like the baseline that you're normalizing it by. I don't know. Um, and then the um, yeah, we could have like embedding repre from the text of the, um, of the name plus the description, which I could describe, um, later if if we have time, how to generate that, but we could use something like various like take an off-the-shelf just concatenate them together and then, uh, put it through an off-the-shelf BERT type model. Um, and that would give us an embedding to compare venues. And and yeah, again, we like even if it's in logistic regression, it doesn't matter. Like you can just, um, have each of these embedding dimensions as a separate coefficient. And you could have the taxonomy, um, as a categorical, um, one hot. Maybe like keep the category simple if the taxonomy simple and just use like the top level taxonomy. And then for a user, um, you could do something like  number of times uh, click We so we also know like well well, we know conversions. Like we know when people actually made reservations. So you could have like number of times clicked um, on yeah, let's say let's say venues of different So assuming that tax like for the top level taxonomy, um, we don't have that many categories. We have maybe like, I don't know, 15 or something. Like then it wouldn't be too bad to have a like one hot, um, features that were defined along like within that, um, set of values. Like number of times clicked on like taxonomy category one uh, last month. And then you can or like actually like basically I'm saying we you can have this like aggregated, um, feature which which describes like how often did they go to a bar or do they go to a restaurant that those of selling tacos or whatever, um, we choose for our top level taxonomies. And that should give us a good sense of what they're going to do next. Um, and then yeah, like maybe, um, some sort of uh, to like hour bucket. So like, you know, from zero to like 23 again as as like, um, as a one hot vector. Excuse me. Um, so to determine like when they're browsing that could affect what they want to click on. Um, okay. I I think I'll go a little deeper, but I I think this is pretty much the the basics of what I I would want to incorporate here. Um, given that we have we don't have much Well, so we also want to consider like people who tend to go to like So like a venue would have a certain type of person who goes to that venue, right? Like a jazz lover. So maybe I could think about like on the user-to-user side like like users who went to venues users who go to venues like the ones you go to, um, also go to venues like this one you haven't been to yet. Um, but that that's like a maybe like a later stage, um, interaction feature that, uh, is is worth incorporating, but just for the MVP for this initial iteration, we won't worry about it. But like, um, places that are like the ones that people similar to you go to. Um, and then yeah, maybe um, I guess this I'm not sure I'm not sure this is like a a model feature or this is like part of the index. Um, yeah, but you get it going the other way basically of of thinking about like of the places that the user has gone in the last month, what are venues that are similar to those places? Yeah, but I don't want to get too complicated right now before I've gotten the end-to-end system working for this set of features. So, I would build up a training set of examples of like from historical sessions hydrating the user and the venue with with these pieces of information then predicting or it would have the like did was clicked yeah as a bool and so how would I and I have to think about how I would split up this this data set into train validation and test. I think that I'd want to probably make sure that I don't leak user level data. So, I wouldn't want to have like data I would want to make sure that any users in the test set are not in the train or validation set. So, keep things separate like that. And then I probably would also want to consider that like what someone's done in the past is going to help me predict the future. So, I wouldn't want to have time leakage either with it within a user. So, I would probably want to consider like doing splits where like for some users I only consider like I I train on what like what their history was like what sessions from like 5 years ago and then I try to predict what they did well not sorry. I yeah I I only well sorry. I'm I'm I'm I'm not speaking very coherently. Okay, so I guess I guess within within this user stratified data set yeah I would I would want to let me let me let me
- **Reference answer:** —
- **Interviewer feedback** (`06:50`): Yeah, let's focus on the on the landing page. Yeah, through bookings, let's say. Yes. Yeah. Yes. Yeah. Yeah, okay, sorry. Mhm. The social aspect I don't believe that it is part of Yelp. Cold start. Yeah, we have a simple rule-based system. We can ask Okay. We already have a simple rule-based system which is giving us some sessions Make any reasonable assumption like you are designing the whole system so you have full power over any direction of the system.
- **Labels:** `ML` · type=hard · stage=system_design

### 2. `42:19` — Self-evaluation and feedback

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #7 | +10 с | `Communication` | stop you here in order to switch over to the feedback, but first I wou… |

#### Item #7

- **Question** (`42:29`): stop you here in order to switch over to the feedback, but first I would like to hear from you. How did you find this question and what is your self-evaluation?
- **Candidate answer** (`42:40`): All right, so I found well this is a good question. I found it a little difficult to know how to pace things out. I think I got bogged down with the features which is like a common thing that people get tripped up on and I maybe wasn't I should have like gone further into like quickly getting to having a model that predicts the basic thing and then getting it deployed and then describing how I would evaluate it online. I think I should have gone to that a little more quickly rather than going like listing out all the possible additional nuance features that I might want to have. So, my self-evaluation is maybe mid-level but probably not yet senior.
- **Reference answer:** —
- **Interviewer feedback** (`43:43`): tend to agree on that and I want to share with you. I'm just going to share with you a link. You covered stuff like the stuff that you covered it was actually okay, but it needed a more holistic view of the whole system. That was the missing point here.
- **Labels:** `Communication` · type=behavioral · stage=behavioral


## Check 3. Semantic field alignment per chapter (step 5, LLM)

The Cursor agent (same as step 2) reviews **extracted** Q&A: field timestamps vs chapter windows and whether texts match chapter titles and labels (`question_topic`, `question_type`). Does not change the overall verdict.


- **Статус:** ✅ все 7 глав без замечаний
- **Тайм-коды полей:** 7/7 ок · **Смысл/метки:** 7/7 ок


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
      "chapter_time": "00:04:54",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:10:25",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:16:28",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:25:13",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:42:19",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:44:22",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:52:54",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
