# Splitter validation report


**Interview language:** `en` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.


## Прогон пайплайна

- **Версия:** `v1` · **Интервью:** `transcripts/mock-interviews/interview-query/product-analyst-senior-meta-friend-requests-interview-query-2022-04-21`
- **Режим:** `split_and_validate` · **source_id:** `product_analyst_senior_meta_friend_requests_interview_query_2022_04_21`
- **Старт:** 2026-05-20 21:18:05 +0200 · **Обновлено:** 2026-05-20 21:31:04 +0200
- **Длительность прогона (стена):** 12 мин 59 с (от старта до последнего обновления журнала)
- **Сумма длительностей шагов:** 2 с (только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)
- **Итог прогона:** ⚠️ неполный журнал (проверьте pipeline-log)
- **Журнал (технические подробности, промпты LLM, входы/выходы):** `splitter_output/mock-interviews/interview-query/product-analyst-senior-meta-friend-requests-interview-query-2022-04-21/product-analyst-senior-meta-friend-requests-interview-query-2022-04-21.v1.pipeline-log.md` — секции «Steps», «Artifacts», «Входы LLM»

| Шаг | Название | LLM | Модель | Длительность | Статус |
|-----|----------|-----|--------|--------------|--------|
| 1 | 1. Подготовка | нет | — | — | ✅ |
| 3 | 3. Excel | нет | — | 1 с | ✅ |
| 4 | 4. Валидация по главам | нет | — | 1 с | ✅ |

### Run artifacts

- **Q&A split (JSON):** `splitter_output/mock-interviews/interview-query/product-analyst-senior-meta-friend-requests-interview-query-2022-04-21/product-analyst-senior-meta-friend-requests-interview-query-2022-04-21.v1.qa-split.json`
- **Q&A split (Excel):** `splitter_output/mock-interviews/interview-query/product-analyst-senior-meta-friend-requests-interview-query-2022-04-21/product-analyst-senior-meta-friend-requests-interview-query-2022-04-21.v1.qa-split.xlsx`
- **Validation reference:** `transcripts/mock-interviews/interview-query/product-analyst-senior-meta-friend-requests-interview-query-2022-04-21/video.md` — YouTube chapters and sections; the splitter did **not** see this file during Q&A extraction
- **Timestamp tolerance:** ±90s — max drift between a YouTube chapter marker and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter

## How validation works

### Verdict: ✅ PASSED

Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). Steps 1 and 3 only prepare data.


| Step | Action | Check in file | Criterion | Status | Result | Goal |
|-----|----------|------------------|----------|--------|-----------|------|
| **1** | Prepare (`pipeline-log.md`) | — | — | — | — | — |
| **2** | LLM → JSON | **Check 1** | Valid JSON per `splitter_output_schema.json` | ✅ | 24 items, JSON Schema OK | parse + JSON Schema |
| **3** | Excel | — | — | — | — | — |
| **4** | Match `video.md` | **Check 2** | Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description) | ✅ | Coverage 100% (6/6), Topic consistency Н/Д | Coverage ≥90%, Topic consistency ≥90% |
| **5** | LLM (agent) | **Check 3** | Field meaning and timestamps vs chapter title and labels | ✅ | all 7 chapters OK | does not block verdict |

---

## Check 1. JSON structure (step 2 — splitter output)

Deterministic check after Q&A extraction: parse + JSON Schema `splitter_output_schema.json`.


- **Файл:** `splitter_output/mock-interviews/interview-query/product-analyst-senior-meta-friend-requests-interview-query-2022-04-21/product-analyst-senior-meta-friend-requests-interview-query-2022-04-21.v1.qa-split.json`
- **Схема:** `.claude/skills/splitter/step1-prepare/splitter_output_schema.json`
- **Парсинг JSON:** ✅ успешно
- **JSON Schema:** ✅ полностью соответствует схеме
- **Пар Q&A (`items`):** 24
- **`source_id`:** `product_analyst_senior_meta_friend_requests_interview_query_2022_04_21`
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
| 1 | `00:00` | Question | — | recognized (1 Q&A) | #1 | `Product Metrics` | ⏳ | — |
| 2 | `08:50` | New Users vs Old Users | — | recognized (2 Q&A) | #10, #11 | `Product Metrics` | ⏳ | — |
| 3 | `10:27` | Geographical Segmentation | — | recognized (3 Q&A) | #12, #13, #14 | `Product Metrics` | ⏳ | — |
| 4 | `13:23` | User Journey Analysis | — | recognized (3 Q&A) | #15, #16, #17 | `Product Metrics` | ⏳ | — |
| 5 | `18:17` | Conclusion | — | recognized (2 Q&A) | #19, #20 | `Product Metrics` | ⏳ | — |
| 6 | `21:07` | Additional Key Points | — | recognized (3 Q&A) | #21, #22, #23 | `Product Metrics`, `Communication` | ⏳ | — |

### Question chapter details

Full Q&A texts. Service chapters appear only in the table above.


### 1. `00:00` — Question

- **Проверка главы:** ✅ у маркера 1 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #1 | +0 с | `Product Metrics` | the first question is a product manager at facebook comes to you and t… |

#### Item #1

- **Question** (`00:00`): the first question is a product manager at facebook comes to you and tells you that friend requests are down by 10 on the facebook app all right what would you do to investigate this
- **Candidate answer** (`00:11`): if i could get the question right basically a product manager comes to me and say that request is going uh it's down by 10 percent and i have to basically investigate what is the reason behind it right i have few follow-up questions so firstly can you help me to understand what do you mean by friend request is it friendly question friend request accepted which part of metric is down and i just wanted to clarify on how is this metric calculated is it like a friend request accepted divided by friend request said is this how we would calculate the metric uh yes so it should be the number of friend requests that are accepted total so um specifically we're not looking at any sort of ratios uh there's friend requests right and then there's friend requests that are accepted so let's say friend requests that are accepted are down by ten percent okay so we are looking about looking into absolute metric so let's say okay got it friend requested the way i'm planning to approach this problem it would be broken down into four steps so firstly i'll be talking at a very high level reasons uh like not doing much analysis but checking for like any obvious miss out if we have and if we don't find anything there then i'll proceed to breaking down this metric into further components uh on top of that i would do some segmentation analysis and then come up with few hypotheses behind this problem so uh and i believe we are just talking about facebook the blue app we are not talking about other family of apps
- **Reference answer:** —
- **Interviewer feedback** (`00:22`): yeah give me a minute to structure my thoughts yeah so let's say that it is the number overall number of friend requests made yeah okay
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

### 2. `08:50` — New Users vs Old Users

- **Проверка главы:** ✅ у маркера 2 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #10 | -49 с | `Product Metrics` | so let's say that the number of active users is not going down right a… |
| #11 | +11 с | `Product Metrics` | so can you help me to understand which part of uh the user base is goi… |

#### Item #10

- **Question** (`08:01`): so let's say that the number of active users is not going down right and we already mentioned that before right yep um so then i guess it would have to be the number of average friend requests per user is then decreasing
- **Candidate answer** (`08:15`): okay so everything was accepted but user is going down uh so i would now break it down further and what i'll do i'll see this i'll divide this metric further into two parts average friend request uh friend request accepted by matured user like people who have been into the system for let's say more than 90 days versus people who have been into the system for less than 90 days so which part of metric is going down i would further investigate the reason is my initial hypothesis people who are new to the system they are more prone to sending and accepting more friend requests versus a mature user they already have majority of their friend
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

#### Item #11

- **Question** (`09:01`): so can you help me to understand which part of uh the user base is going down in terms of everything request accepted uh what do you think my initial hunch is
- **Candidate answer** (`09:14`): maybe maybe the new user base like the users who are new to the system because my point is if someone is already in the uh ecosystem for quite time generally people anyways like if i think about myself who is a active who has been a facebook user for like years i hardly send or accept from requests these days maybe like one a month so i should not be impacting that much that's also true so that's why even i was divided so i would like to have this data code before i start so so what do you think which station should i proceed
- **Reference answer:** —
- **Interviewer feedback** (`09:40`): okay but if uh the number of users that are over 90 days is let's say 99 of the total user yes right wouldn't just like a slight decrease there uh be a huge cause versus just like the new users of the 90 days
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

### 3. `10:27` — Geographical Segmentation

- **Проверка главы:** ✅ у маркера 3 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #12 | -16 с | `Product Metrics` | i would say what does your intuition say uh so if it is the new users … |
| #13 | +27 с | `Product Metrics` | nope that makes sense uh which one would you investigate first do you … |
| #14 | +49 с | `Product Metrics` | gotcha and why geography first |

#### Item #12

- **Question** (`10:11`): i would say what does your intuition say uh so if it is the new users then what would you do
- **Candidate answer** (`10:17`): i think um if it's new user or old user i would have proceeded with the segmentation analysis so the segmentation analysis i would start with something like a geographical cut because i don't think we can have a demography analysis for app like facebook where we don't know people are putting their current gender or age so i would have started with something like in which geography this decline are we seeing and then i would have seen further at the that versus ios versus android so see if there's a particular segment where i'm seeing that so any inputs on these segmentation
- **Reference answer:** —
- **Interviewer feedback** (`10:54`): nope that makes sense uh which one would you investigate first do you think
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

#### Item #13

- **Question** (`10:54`): nope that makes sense uh which one would you investigate first do you think
- **Candidate answer** (`11:00`): i would have started with geography i think we can we could start with any note geography or device level i would have started with geography and if there is particular geography where we have seen more div then i would have gone to the second layer of segmentation analysis which is android versus ios versus web
- **Reference answer:** —
- **Interviewer feedback** (`11:16`): gotcha and why geography first
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

#### Item #14

- **Question** (`11:16`): gotcha and why geography first
- **Candidate answer** (`11:20`): uh so geography i generally felt like user of a particular kind of geography have have a similar behavior so for example if we think about north america or western europe uh right now at this point of them i can say that yeah i have heard a lot of anecdotal uh inputs that yeah now facebook is for old people it is not even picking up and instagram is the place to go whereas in the asian market where people are still going like elderly people to meet people are still going to facebook so that's why i think it might be a stronger scene
- **Reference answer:** —
- **Interviewer feedback** (`11:57`): gotcha
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

### 4. `13:23` — User Journey Analysis

- **Проверка главы:** ✅ у маркера 3 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #15 | -85 с | `Product Metrics` | then uh wouldn't you have to segment for age at that point if your hyp… |
| #16 | -40 с | `Product Metrics` | so let's move on to the second segment so uh is there any specific geo… |
| #17 | +81 с | `Product Metrics` | it could go in any direction like people might be sending fewer friend… |

#### Item #15

- **Question** (`11:58`): then uh wouldn't you have to segment for age at that point if your hypothesis is kind of based on um so yeah agent accounts
- **Candidate answer** (`12:08`): so i think right right now with my understanding like i think we'll just say that you have to be more than 13 years old now i'm not sure whether the information which people provide about their gender and age how accurate it would be we can make some approximations by looking into friends uh and looking into picture that what general could it be but what each would be but if i just uh look at the first instance i would be doubtful about the quality of this data on facebook
- **Reference answer:** —
- **Interviewer feedback** (`12:42`): okay
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

#### Item #16

- **Question** (`12:43`): so let's move on to the second segment so uh is there any specific geography or device level where we are seeing the dip or that across something potentially yeah so let's say that uh we don't see anything what else did we do
- **Candidate answer** (`13:00`): okay so right now let's just summarize the things we have done so far so right now we saw that friend request accepted is going down for new users and we did not find any major pattern till the time we performed segmentation and i'll say that a demography level as well as device level okay so now i would try to go a little bit into the user journey analysis uh i would try to see how does a friend request saying happened versus acceptability so how did does that funnel now there are two sources of uh friend request sending if i understand correctly first is you make an organic search and you find a person and then you send a friend request and then there is other one is people you may know you might send friend requests from there so that would be my starting point firstly i would see in these two funnels um how many uh like number of friend requests sent how is it looking is it going down or is it going up uh even before that i would actually start with something like build a high level funnel so thing is friend request sent attempted then friend request actually process because there are sigma rules in the back end which execute those actions and then friend request eventually accepted so there are three steps of the funnel i'll see if there is drop of a drop happening at any point so is it the problem more on friend request sent or is it this friend request getting sent or not and when people are accepting is it getting accepted or not so can you tell me like which part of the funnel has seen the major drop off okay what do you think
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

#### Item #17

- **Question** (`14:44`): it could go in any direction like people might be sending fewer friend requests or there might be some slight technical bug which is let's say not letting friend friendly percent and then if not people are actually attempting this so it could actually any three direction would be possible and my analysis would depend on this input okay but uh that's not an answer right so i guess depending on how what you know about facebook what do you think is the most likely cause at this point given the current situation of facebook
- **Candidate answer** (`15:17`): okay see if we do not see any major decline in diu so then it means people are coming to the platform so if they are sending friend requests and i know there are a few bunch of few privacy features which now even restrict people from sending friend requests to people you might not be knowing then friend request which might be coming they might be of higher quality so i do not see any strong reason why somebody would not be accepting it so i think there should be decline at the top of the funnel which is intend to send friend request that so maybe people are sending fewer friend requests that's my if i would have started analysis with this point
- **Reference answer:** —
- **Interviewer feedback:** —
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

### 5. `18:17` — Conclusion

- **Проверка главы:** ✅ у маркера 2 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #19 | -71 с | `Product Metrics` | do you think it is the right direction to proceed |
| #20 | -26 с | `Product Metrics` | um what other methods could we do to see why they would be those frien… |

#### Item #19

- **Question** (`17:06`): do you think it is the right direction to proceed
- **Candidate answer** (`17:09`): well if they're investing more time in other facebook let's say instagram wouldn't daily active users also go down at that point so what happened you might might have still created facebook app but let's say your time spent on the app is low
- **Reference answer:** —
- **Interviewer feedback** (`17:24`): okay gotcha so we would be seeing a correlation and time spent on facebook go down by 10 or more correct uh for this you will segment yes okay gotcha so let's say that um time spent is normal all the other metrics are normal but we're seeing less uh people sending friend requests still at the same rate across all the top of the funnels
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

#### Item #20

- **Question** (`17:51`): um what other methods could we do to see why they would be those friend requests would be going down so i think we can establish now the problem is people are sending fewer friend requests that is the root cause of the problem now we have to come up with hypothesis why they are sending fewer friend requests and it is declined across both people you may know give me a relative structure my heart okay okay so just to summarize so far
- **Candidate answer** (`18:18`): what we have concluded so the problem is the in the segment of new users that is where we are seeing the lower friend request and we've further established that basically top of the funnel which is friend request sent is low uh then and this is low both from uh organic and search for sent friend request as well as py and now basically we have to understand uh why they flow so i can see uh two reasons first of all the reason why this user base has created the profile it the primary purpose is not interacting with their friend they might be playing some games or following certain pages and all second is they have just created a profile like across all the social media but they are active on let's say more on instagram and messenger so what i'll do for this user segment i would try to do the time spent analysis like on what activities are they doing and uh are they spending the time so this will give me a signal whether the intent is to interact more with the friends or their community or is it more about con interacting in group or let's say following certain pages so that is what i'll do is the first part of analysis second i'll also try to if available i will try to find their mapping on other app like instagram and messenger and see if these are the primary source of communication which these people are using so are we seeing uh more let's say follow back of follows and request or messenger collection for these user base or not so this will give me an initial hypothesis that the way they are using facebook that me that approach has changed and they are connecting with their friends on some other social media so this could be one of my hypothesis this is how i will proceed further
- **Reference answer:** —
- **Interviewer feedback** (`20:24`): okay
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

### 6. `21:07` — Additional Key Points

- **Проверка главы:** ✅ у маркера 3 Q&A · ⏳ смысл не проверен (шаг 5)

**Q&A at chapter marker** (±tolerance; each item in one chapter only)

| Item | Δt | `question_topic` | Question start |
|------|-----|------------------|----------------|
| #21 | -42 с | `Product Metrics` | so what metrics would prove to you that this that your hypothesis is t… |
| #22 | +0 с | `Product Metrics` | awesome i don't have any further questions uh but we could wrap it up … |
| #23 | +31 с | `Communication` | so i think on my review uh so what did you think about this question f… |

#### Item #21

- **Question** (`20:25`): so what metrics would prove to you that this that your hypothesis is true in this case
- **Candidate answer** (`20:31`): uh so followers sent request request on instagram and it's not like a fan page or a celebrity it's more like a genuine user page so number of are those requests going up or are stable that is one metric i'll see same i'll check in the messenger and then the third metric which i'll see is time is spent on organic content interaction divided by the total dimension sent on the facebook if that metric is going down and other two metric is going up then i can have a reasonable hypothesis that this could be the reason
- **Reference answer:** —
- **Interviewer feedback** (`21:04`): okay cool
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

#### Item #22

- **Question** (`21:07`): awesome i don't have any further questions uh but we could wrap it up any other kind of points that you want to make before we review it
- **Candidate answer** (`21:12`): no i think uh based on the thorough analysis of this root cause analysis problem we try to check every possible segment for my knowledge and we have concluded it's basically change in the behavior of newer users which we are seeing in the facebook uh which is driving the friend request down
- **Reference answer:** —
- **Interviewer feedback** (`21:37`): yeah
- **Labels:** `Product Metrics` · type=soft · stage=technical_case

#### Item #23

- **Question** (`21:38`): so i think on my review uh so what did you think about this question first off and then i'll kind of give you my thoughts of it as well
- **Candidate answer** (`21:47`): so i think it's uh it's one of the classic facebook questions and with this question you can take the candidate in any direction you want i can think about like 5-10 other variations right now so it's a good question and basically it also helps you to judge our understanding of facebook app from interview perspective so we are checking on things like our friend request i think this person have idea about pymk uh then uh basically how other ecosystem metric can impact one of the metric uh metric we can also check and we can also think about cross app uh cannibalization so it was a pretty good problem i think it gives a good signal if a person can solve the business case property or not
- **Reference answer:** —
- **Interviewer feedback** (`22:39`): yeah yeah i agree so i think a few things that i liked uh from the very beginning were how you did clarify the metric that it was friend request accepted versus friend requests given how you looked at like gradual or immediate decline these are pretty standard and then also kind of um uh framing your structure of your answer within um under like doing a segment analysis afterwards and then kind of a conclusion i think one thing that we didn't miss was around like the friend request so i think it's pretty obvious initially we probably should have looked at like number of friend requests sent versus friend requests accepted right and i think we kind of uh glanced over that or kind of missed that one uh so that one was just something that we should probably jump into immediately and then the other thing was um i think you know at facebook especially i don't know you know if this happens at your in your interviews or like specifically but i think with a lot of these case questions also the interviewers don't have like a set you know kind of root cause for a right answer right so they always just throw the answer the question back at you and that's kind of what i was doing there too right because i didn't really know like what was going to be like the right answer in the scenario i was just kind of looking for both of your sides and so um if you explain both sides well then i think that's like a good signal to the interviewers um i don't know what do you think uh is that usually what you have to do is kind of come up with both arguments and kind of create like a solution to that
- **Labels:** `Communication` · type=soft · stage=technical_case

## Speaker boundary check (heuristic)

Automatic role check (no diarization): Q/A duplicates, truncated questions, candidate speech in question field, interviewer lines inside answer.

- **Item #8:** текст `interviewer_feedback` повторяется в `candidate_answer` (или наоборот). Оставьте реплику только в одном поле.


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
| #3 | 02:53 | no changes okay |

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
      "chapter_time": "00:00:26",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:08:50",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:10:27",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:13:23",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:18:17",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    },
    {
      "chapter_time": "00:21:07",
      "time_alignment_ok": true,
      "content_alignment_ok": true,
      "notes": ""
    }
  ]
}
```

<!-- /SEMANTIC_VALIDATION -->
