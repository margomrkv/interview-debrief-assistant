<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "data-scientist-senior-1xbet-novoselov-2023-08-02",
  "transcript_folder": "transcripts/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02",
  "source_id": "data_scientist_senior_1xbet_novoselov_2023_08_02",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-21 09:41:08 +0200",
  "updated_at": "2026-05-21 09:47:40 +0200",
  "models": {
    "step2_qa_extraction": {
      "model": "claude-sonnet-4-6",
      "temperature": 0
    },
    "step5_llm_validation": {
      "model": "claude-sonnet-4-6",
      "temperature": 0
    }
  },
  "artifacts": {
    "json": "splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.qa-split.json",
    "xlsx": "splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/timecodes.txt",
        "ru",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-21 09:41:08 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 2.0,
      "notes": null,
      "finished_at": "2026-05-21 09:47:40 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02`
- **Source ID:** `data_scientist_senior_1xbet_novoselov_2023_08_02`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-21 09:41:08 +0200
- **Last updated:** 2026-05-21 09:47:40 +0200

Фильтр в IDE: `*data-scientist-senior-1xbet-novoselov-2023-08-02.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/timecodes.txt`<br>`ru`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.pipeline-log.md` | — | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.qa-split.xlsx` | 2.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.qa-split.json`
- **xlsx:** `splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.pipeline-log.md`

## Входы LLM (что подавали модели)

<!-- LLM_INPUT_STEP_2 -->

## Шаг 2 — извлечение Q&A

Модель читает **только этот блок** на шаге 2 (не `video.md`, не другие интервью).

```text
======================================================================
SYSTEM PROMPT (.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt)
======================================================================
You are an interview annotation engine for DS/DA interview transcripts (Splitter v3).

Primary objective:
Produce precise splitter output (Q&A extraction only) for each interviewer question and candidate answer pair.

Critical constraints:
1) Output JSON only (no markdown, no prose before/after the JSON object).
2) Follow the splitter schema exactly (`splitter_output_schema.json`) with LinkedText objects. No extra top-level keys.
3) Be conservative: do not invent missing facts.
4) Splitter only: do NOT output any scoring/assessment/evaluation fields.
5) Do not merge, cluster, or summarize multiple interviewer questions into one item. One interviewer question -> one item.
6) If the interviewer asks follow-up clarifications, keep them as separate items when they are semantically new questions.
7) Sidecars in the user message (e.g. FEEDBACK_MD) are optional hints for boundaries only. **video.md / YouTube chapter titles are never in step 2** — they exist only for offline validation (steps 4–5). Never invent facts that are not supported by PRIMARY_TRANSCRIPT text.
8) Verbatim contract (hard — applies in every runtime, including cloud/batch):
   - `interviewer_question.text` and `candidate_answer.text` MUST be built from contiguous spans of the PRIMARY_TRANSCRIPT (after the light joining rules in §11). Wording must match the transcript; do not replace sentences with summaries like "The candidate discussed X" or "They explained their approach to…".
   - Forbidden patterns in `text` fields: meta-phrases such as "The interviewer asks about…", "In this segment…", "The candidate responds by…", bullet lists that restate content, translated paraphrase when the transcript is Russian (or vice versa).
   - Allowed light cleanup ONLY: remove excessive filler tokens ("ээ", "ну" repeated stutter), normalize whitespace, fix obvious ASR typos ONLY when the intended word is unambiguous from context; do not rewrite phrasing for style.
   - If you cannot fit a full answer in limits, prefer splitting into the next linked item (if it is a genuinely new question) rather than compressing into an abstract summary.
9) Prefer verbatim excerpts over summaries. Do not paraphrase into abstract descriptions.
10) Do not intentionally truncate question/answer text unless absolutely necessary due to model limits.
11) **Interview language (hard):** read `INTERVIEW_LANGUAGE` in the user message (`ru` or `en`).
    - `ru` — all `text` fields (`interviewer_question`, `candidate_answer`, `interviewer_feedback`, `reference_answer`) MUST be verbatim Russian from PRIMARY_TRANSCRIPT. Never translate to English. Validation report for this run is Russian.
    - `en` — all `text` fields MUST be verbatim English from PRIMARY_TRANSCRIPT. Never translate to Russian. Validation report for this run is English.
    - Enum fields (`question_type`, `question_topic`, `interview_stage`) stay English per schema; only spoken-text fields follow interview language.

§ Verbatim Q&A contract (single rule for question + answer)
- One item = exactly one interviewer question and the candidate's response to that question (or null answer if the candidate never spoke).
- Build `interviewer_question.text` and `candidate_answer.text` from contiguous PRIMARY_TRANSCRIPT spans. Wording must stay as close to the transcript as possible.
- ASR (automatic speech recognition) cleanup — allowed ONLY when the intended word is unambiguous:
  * Fix obvious mis-hearings (e.g. «шапира» → «шоппер», «пандас» → «pandas»).
  * Restore standard technical terms (SQL, Python, bootstrap, A/B test, gradient descent).
  * Add punctuation and capitalization; normalize whitespace.
  * Do NOT rephrase, summarize, reorder clauses, or «improve style».
  * Do NOT delete «ээ», «ну», «мм» unless they are stutter noise inside a single word — when in doubt, keep the filler.
- Forbidden: meta descriptions («кандидат рассказал о…»), bullet summaries, answers of 2–4 words when the transcript shows a long turn (merge fragments instead).
- Timestamps: use the first fragment where the speaker starts that turn (see §11).
11) Transcript format handling: if transcript lines start with `[HH:MM:SS]` timestamps (e.g. `[00:05:12] word word word`), the transcript is a sequence of short timestamped fragments. When reconstructing a Q or A span:
   - Concatenate consecutive fragments into a single coherent text.
   - Assign `time` as the timestamp of the **first fragment** that opens the question or answer span.
   - Do not use timestamps from the middle or end of a span.
   - Light joining only: remove line breaks between fragments, preserve original wording.
   - CRITICAL — intra-line speaker changes: a single `[HH:MM:SS]` fragment may contain speech from TWO speakers when one speaker finishes and another begins within the same ~4–8 second window. Do NOT assume speaker changes always coincide with timecode boundaries. Use semantic analysis to detect the split point:
     * A question mark, direct address, or request signals the interviewer ending their turn.
     * Phrases like "я читала", "я думаю", "на практике", "не пользовался" signal the candidate starting or continuing their turn.
     * Phrases like "давай я приведу пример", "давайте я приведу", "я понял", "окей хорошо", "ну я тогда" signal the **interviewer** — put them in `interviewer_feedback` or the next question, never inside `candidate_answer`.
     * Confirmations like "да", "хорошо", "супер" after a question may be interviewer or candidate — use surrounding semantics.
     * When a split is found mid-line, assign the fragment's timestamp to whichever speaker STARTS their turn in that line; the other speaker's text gets the preceding or following fragment's timestamp.
     * Include only one speaker's text per LinkedText field — never merge two speakers into one `text` value.
12) Use LinkedText structure for text+time fields:
   - `interviewer_question: {text, time}`
   - `candidate_answer: {text, time}`
   - `reference_answer: {text, time}`
   - `interviewer_feedback: {text, time}`
13) Fill `splitter_mode` exactly as given in INPUT DATA (`split_only` or `split_and_validate`).

Few-shot style reference (illustrative — do not copy text into output unless it appears in your transcript):
- BAD candidate_answer.text: "The candidate explains how they would investigate a metric drop using funnels and cohorts."
- GOOD candidate_answer.text: "я бы сначала посмотрел на воронку по шагам, потом отфильтровал когорту по платформе и версии приложения"
- BAD: пропустить блок, где интервьюер спрашивает про A/B только на новых пользователях и сам отвечает (кандидат не говорит).
- GOOD (самоответ интервьюера): отдельный item — `interviewer_question` с формулировкой вопроса;
  `candidate_answer`: `{"text": null, "time": null}`;
  `reference_answer.text` — развёрнутый ответ интервьюера (честный рандом, hash по user_id, mod 2 и т.д.).
- BAD candidate_answer (смешение спикеров): «я читала… давайте я приведу пример декоратора… нет, не пользовался» в одном поле.
- GOOD: `candidate_answer` только «я читала, знакомо, на практике мало»; просьба интервьюера «давай пример» → `interviewer_feedback` или отдельный уточняющий `interviewer_question`; «нет, не пользовался» → `candidate_answer` (короткий отказ).
- BAD interviewer_feedback: тот же текст, что уже в `candidate_answer`, или продолжение ответа кандидата после «угу» интервьюера.
- GOOD interviewer_feedback: короткая реплика интервьюера или `null`, если интервьюер молчал до следующего вопроса.

Definitions:
- technical_qna: direct technical question-answer format (concepts, methods, trade-offs, tools, metrics).
- behavioral: question about past behavior in a concrete situation (usually story-based: "tell me about a time...", conflict, failure, leadership case).
- technical_case: open-ended practical scenario (diagnose problem, propose approach) without mandatory coding.
- technical_coding: writing code/SQL/algorithmic task.
- system_design: high-level architecture/design discussion.
- fit_hr / manager_round: motivation/expectation/team-fit discussions.

Boundary policy for Q&A extraction:
- Extract only interviewer-led questions as primary items.
- Candidate-to-interviewer questions should not become standalone items unless explicitly requested by input instructions.
- If interviewer provides immediate per-question feedback or a reference answer, put them into:
  - `interviewer_feedback`
  - `reference_answer`
- If unavailable, use null for optional fields.

§ interviewer_question vs candidate_answer — no duplication (hard)
- `interviewer_question.text` and `candidate_answer.text` MUST NOT repeat the same verbatim span from the transcript.
- **Forbidden:** the answer starts by echoing the question (common ASR failure when the first line of a timecode window is mis-attributed).
- **Forbidden:** putting the candidate's monologue into `interviewer_question` because it is the first line after a long candidate block.
- **Forbidden on step 2:** using YouTube chapter titles, `video.md`, or any external agenda not present in PRIMARY_TRANSCRIPT. Real interviews have no such file; mock runs must train the same rule.
- **How to assign roles without speaker labels (behavioral / no diarization):**
  * Interviewer turn: short, directed at the candidate («как ты…», «а ты понимаешь…», «что делать…», «получается ты…», «тогда такой вопрос»), often ends before a long story.
  * Candidate turn: long first-person story («я пошёл», «у нас было», «мы делали», «я бы сказал»), answers the posed question.
  * If a `[HH:MM:SS]` line is clearly the candidate continuing a story, it is **never** the question.
- **Truncated / garbled ASR questions (transcript-only repair):**
  * **First:** merge **consecutive interviewer** fragments on adjacent timestamps until the question is one intelligible clause (e.g. [32:36]+[32:40] → one `interviewer_question`).
  * **Allowed:** minimal function words already implied by the surrounding transcript («ли», «что», «или») — **not** new topics or paraphrase from outside the transcript.
  * **Forbidden:** inventing a «clean» question from a chapter title or interview outline you were not given.
  * If the interviewer question is still incomplete after merge — keep the **best contiguous verbatim** interviewer span; do **not** copy the candidate's opening into the question field.
- **Sanity check before output:** if the first ≥6 words of `candidate_answer` match the first words of `interviewer_question`, re-cut spans; if `interviewer_question` contains «я знаю / я просто / у нас / мы » (candidate voice), move that text to `candidate_answer`.

Few-shot (Q vs A):
- BAD Q: «что делать… я знаю что в русских компаниях…» + BAD A starting with the same «классический вопрос… русских компаниях…» (candidate text split across both fields).
- GOOD Q: «что что делать как жить» (verbatim Valera at [31:21]) · GOOD A: from [31:24] «Я просто лично ни разу…» — no duplicate prefix.
- BAD Q: «а ты понимаешь что повышать его еще не» alone · GOOD Q: merged verbatim «а ты понимаешь что повышать его еще не Что делаешь» from adjacent interviewer lines in the transcript.

§ interviewer_feedback — speaker contract (hard)
- `interviewer_feedback.text` MUST contain **only** the interviewer's speech for this item's window (reaction, clarification, coaching, short "угу/понятно", debrief remark tied to this question).
- **Never** put the candidate's words in `interviewer_feedback` — including long continuations of the same story, career history, process description, or "мы сделали / я считаю / у нас Kanban" from the candidate.
- If the candidate keeps talking after the interviewer asked a question, that continuation belongs in `candidate_answer.text` (extend the span to the next interviewer question), NOT in `interviewer_feedback`.
- If the interviewer did not speak again before the next question (or debrief block is clearly later), use `interviewer_feedback`: `{"text": null, "time": null}`.
- Do NOT dump "leftover" transcript tail into `interviewer_feedback` because the field is optional.
- End-of-interview debrief ("флажок", "красный флаг", разбор ответов) — only interviewer lines; attach to the relevant item by topic, not duplicated into every item.

Few-shot (interviewer_feedback):
- BAD feedback: «я попросил новый проект… ко мне пришёл оффер… мы причесали Trello…» (candidate biography / case — belongs in `candidate_answer`).
- GOOD feedback: «понятно, а почему именно ушёл из VK?» or «флажок: ты не спросил команду про 1:1» (interviewer only).
- GOOD when silent: `{"text": null, "time": null}`.
- CRITICAL — interviewer-posed-and-self-answered questions: in mock interview recordings the
  interviewer sometimes poses a question and immediately provides the answer themselves, without
  giving the candidate a turn. This MUST still be extracted as a standalone item:
    * `interviewer_question.text` — the question as posed
    * `candidate_answer` — `{"text": null, "time": null}` (candidate did not respond)
    * `reference_answer.text` — the interviewer's own answer/explanation
  Do not skip these items. Markers that indicate this pattern:
    * Interviewer asks a question and continues speaking without pause (no candidate turn)
    * Phrases like "на будущее", "на будущее просто сразу скажу", "кстати", "а вот ещё",
      "ещё один момент", "последний вопрос который я бы задал" followed by a question
    * The question ends and the interviewer immediately says "ответ:", "правильный вариант:",
      "здесь нужно сказать...", "на самом деле здесь все вариант ответа", or starts explaining the answer
    * The topic is flagged as a "bonus" or "for future reference" question
    * A/B / experimentation edge cases where the interviewer poses the scenario and answers:
      e.g. only new users (no returning users to split), store users vs new users, "честный рандом",
      split via hash(user_id) or remainder mod 2 — extract as one item even if the candidate is silent
  Timestamps: `interviewer_question.time` = when the question is posed; `reference_answer.time` =
  when the interviewer starts the substantive answer (often after "на самом деле").

======================================================================
USER PROMPT (variable input + schema)
======================================================================
Task: Q&A extraction for the transcript below. Match the system prompt used in this run
(repository file: .claude/skills/splitter/step1-prepare/splitter_system_prompt.txt).
Return a single JSON object only (no markdown fences).

======================================================================
OUTPUT SCHEMA (contract)
======================================================================
{
  "type": "object",
  "additionalProperties": false,
  "required": ["source_id", "splitter_mode", "items"],
  "properties": {
    "source_id": {
      "type": "string"
    },
    "splitter_mode": {
      "type": "string",
      "enum": ["split_only", "split_and_validate"]
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "interviewer_question",
          "candidate_answer",
          "reference_answer",
          "interviewer_feedback",
          "question_type",
          "question_topic",
          "interview_stage"
        ],
        "properties": {
          "interviewer_question": {
            "type": "object",
            "additionalProperties": false,
            "required": ["text", "time"],
            "properties": {
              "text": { "type": "string" },
              "time": { "type": ["string", "null"] }
            }
          },
          "candidate_answer": {
            "type": "object",
            "additionalProperties": false,
            "required": ["text", "time"],
            "properties": {
              "text": { "type": ["string", "null"] },
              "time": { "type": ["string", "null"] }
            }
          },
          "reference_answer": {
            "type": "object",
            "additionalProperties": false,
            "required": ["text", "time"],
            "properties": {
              "text": { "type": ["string", "null"] },
              "time": { "type": ["string", "null"] }
            }
          },
          "interviewer_feedback": {
            "type": "object",
            "additionalProperties": false,
            "required": ["text", "time"],
            "properties": {
              "text": { "type": ["string", "null"] },
              "time": { "type": ["string", "null"] }
            }
          },
          "question_type": {
            "type": "string",
            "enum": ["hard", "soft", "behavioral"]
          },
          "question_topic": {
            "type": "string",
            "enum": [
              "SQL",
              "Python",
              "Statistics",
              "Experimentation",
              "Product Metrics",
              "ML",
              "Data Modeling",
              "Communication",
              "Stakeholder Management",
              "Prioritization",
              "Conflict",
              "Leadership",
              "Ownership",
              "Collaboration",
              "Adaptability"
            ]
          },
          "interview_stage": {
            "type": "string",
            "enum": [
              "fit_hr",
              "technical_qna",
              "technical_case",
              "technical_coding",
              "system_design",
              "behavioral",
              "manager_round"
            ]
          }
        }
      }
    }
  }
}

======================================================================
INPUT DATA
======================================================================
SOURCE_ID: data_scientist_senior_1xbet_novoselov_2023_08_02
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02
INTERVIEW_LANGUAGE: ru
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00] Привет Сегодня покажу собеседование в
[00:02] 1xbet это букмекерская контора и она
[00:04] запрещена в РФ А ее основатель романти
[00:06] миохи находится в международном розыске
[00:09] сама компания как ее основатели и
[00:11] сотрудники располагаются на Кипре
[00:12] собственно туда они пригласили меня
[00:14] самое интересное что они уже делали мне
[00:16] offer когда еще не записывал свои
[00:18] собеседования на камеру они мне прислали
[00:20] offer в размере 6000 евро с релокации на
[00:23] Кипр начала этот оффер принял но потом
[00:25] подумав решил отказаться но так они уже
[00:28] успели оформить документы Теперь у меня
[00:29] есть бесплатная виза на киперы Болгарию
[00:32] собственно ребят лайфхак Пользуйтесь не
[00:34] успею про них забыть как мне написала
[00:35] другая Чар уже другой компании с
[00:38] предложением пройти собеседование Я
[00:40] сразу понял что это 1xbet и подумал
[00:42] классный будет контент здесь важно
[00:44] понимать как работает на такие
[00:46] организации не будут напрямую устраивать
[00:48] 1xbet вам предложат устроиться в другую
[00:50] компанию посредник который предоставляет
[00:52] якобы у студии xbet и располагается не в
[00:55] России Конечно все мы понимаем что это
[00:57] одно и до тех пор пока вы не про йдете
[01:00] собеседование вам не сделают оффер Вы не
[01:02] узнаете хуже компанию
[01:04] локации здесь Единственный плюс это
[01:06] деньги здесь просить можно действительно
[01:08] много Потому что жизнь на Кипре стоит
[01:10] достаточно много жильё здесь дорогое
[01:12] снять двухкомнатную квартиру вам
[01:14] обойдётся минимум 1500 евро в общем сами
[01:17] сейчас всё увидите
[01:18] не передавала что вы соответственно
[01:21] рассматривайте наши предложения
[01:22] непосредственно с релакацией и верной
[01:25] информации Да
[01:31] компания липолиметр Как говорила ранее
[01:33] мы занимаемся B2B решением в
[01:36] развлекательный игровой спортивной сферы
[01:39] в том числе букмекерское направление
[01:41] веттинг и кемплинг открыть пожалуйста
[01:44] было бы вам интересно поработать над
[01:47] проектами с нашей тематикой конечно
[01:49] Дальше она рассказала мне про задачи
[01:51] которые меня ждут если коротко то им
[01:53] нужен чат-бот для службы поддержки
[01:55] потому что они не справляются с наплывом
[01:57] пользователей Наверное вы Спросите
[01:59] причем здесь дата сайнс хуй его знает
[02:01] в любом случае
[02:17] на момент испытательного срока вы сейчас
[02:20] Москве находитесь
[02:23] совсем не боюсь что меня посадят в
[02:26] тюрьму например Дальше она рассказывала
[02:27] работы плюшки которые они предоставляют
[02:31] также на Кипре на Кипре у нас
[02:33] корпоративное питание формате шведского
[02:35] стола также есть компенсация аренды
[02:39] жилья Это плюс 750 евро ежемесячно к
[02:42] вашей заработной плате в оффер эту сумму
[02:44] отдельно прописываем
[02:45] вот так же у нас
[02:48] имеется возможны беспроцентного
[02:50] автокредитования различные курсы
[02:52] конференции не так все что вам будет
[02:54] интересно постить для вашего развития
[02:56] также компании уплачивает
[02:58] вот что касается
[03:03] страховка естественно у нас тоже имеется
[03:06] вместе с вашей рабочей визой её ну и
[03:10] соответственно компания оформляет для
[03:12] вас рабочую визу а перевозит вас тоже
[03:15] это за счёт компании пакет билеты
[03:18] трансфера всё входит
[03:23] компенсация английского языка и у нас
[03:26] есть спортзал в одном из наших главных
[03:28] офисов кстати вполне нормальные условия
[03:32] показали правда 750 евро за квартиру это
[03:36] Маловато на эти деньги нельзя снять даже
[03:38] однушку
[03:41] будут воскресенье мы отдыхаем и нас
[03:43] гибкое начало рабочего дня возможно
[03:45] через 9 до 11 утра по московскому
[03:48] времени короче полы неплохие условия
[03:51] Ставь лайк если у тебя на работе хуже
[03:53] переходим к техническому интервью тогда
[03:54] соответственно расскажите в каких
[03:56] проектах вы участвую ты участвовал Какие
[04:00] задания там были единственное мое
[04:02] соприкосновение с чат-ботами было на
[04:03] Моей первой работе где я писал ботов на
[04:05] движке раса это такой фреймвор для
[04:08] написания ботов он сделан настолько
[04:09] просто чтобы разобраться могла даже пару
[04:11] раз я добыча Альберта G5 собственно это
[04:14] и был весь мой опыт но рассказывал я про
[04:17] это конечно так чтобы это звучало очень
[04:19] красиво
[04:23] свои модели выводили и на каких
[04:26] технологиях Это был докер это
[04:28] микросервис или это был какой-то случай
[04:30] моделей Как это работает кучей модели
[04:33] микросервисы Да да все именно для
[04:35] обучения использовалось что в Облаке
[04:38] где-нибудь обучали там не знаю в амазоне
[04:40] еще там
[04:42] или это только ресурсы свои просто
[04:45] говорите что обучали ВВС Я всегда так
[04:47] отвечаю хуй знает что это такое хорошо
[04:49] то есть если что-то вы можете сможете
[04:51] это настроить как бы конечно смогу
[04:53] Давайте в общем конкретики по какой-то
[04:56] ада будет Да вот и вот это вот задача
[04:58] допустим у нас нет асессоров В принципе
[05:00] мы можем их найти но как бы если у нас
[05:03] есть просто диалоги Как нам их разметить
[05:06] смотря для какой задачи конечно
[05:08] задать классификации классификации есть
[05:11] и задача Nerf в принципе наверное больше
[05:13] никаких других и не будет значит вообще
[05:15] если данных нет то размещать можно
[05:17] Только руками например есть удобный
[05:19] инструмент лейбл студию там есть очень
[05:20] удобный UI для разметки и там есть фишка
[05:23] что можно использовать модели для помощи
[05:26] разметчикам это очень ускоряет процесс А
[05:28] вот типа я просто я их не пробовал не
[05:31] просто интересно допустим попробовать
[05:33] создавать фронтов там для Чан гпт чтобы
[05:36] это сказать по аналогии что-нибудь
[05:38] распознал такое не пробовали Ребята кто
[05:40] пробовал Пишите в комментах это
[05:42] интересно как это можно использовать А
[05:44] вообще вот отпишитесь стандартный план
[05:46] для обучения модели решающей
[05:49] какую-нибудь НЛП задач приведение к
[05:51] нужному формату который используется для
[05:53] обучения модели Ну там еще разбивка на 3
[05:55] А какие-нибудь кластеризации вы работали
[05:59] с текста наиболее часто используемый
[06:00] алгоритм это минус случае если известно
[06:02] число кластеров если нам число кластеров
[06:04] неизвестно то использует гибиска Какие
[06:07] виды такие зации вы знаете самый простой
[06:09] способ токенизации это разбить по словам
[06:11] символом это более современных методов
[06:16] [музыка]
[06:20] первые модели НЛП это уже Берт как бы до
[06:24] них было добер то я в основном делал
[06:26] викторизацию при помощи собственно Это
[06:28] самый простой и рабочий способ
[06:33] загуглить Если вы не знаете собственно
[06:35] это просто способ это рисовать
[06:41] вот век и глав вот эти вот victorizer и
[06:46] типа ты знаешь что такое World of wark Я
[06:48] знаю что такое глов уже забыл вроде то
[06:50] же самое а недостаток допустим вот у
[06:52] века какой На мой взгляд недостаток в
[06:54] том что у него маленькое окно контекста
[06:56] и сам алгоритм достаточно старый
[06:58] чем он отличается на самом деле хз я
[07:02] ответил что это какая-то более
[07:03] современная нейронка Но на самом деле
[07:10] еще с добавлением соответственно
[07:15] на самом деле все это не важно этим
[07:18] давно уже никто не пользуется спрашивает
[07:19] просто чтобы спросить основные задачи я
[07:22] ответил что это классификация
[07:23] распознавание именованных сущность и
[07:25] генерации
[07:28] есть такая Метрика перплексия есть еще я
[07:32] не знаю
[07:34] я пользовался уже готовыми инструментами
[07:37] для этого саму задачу
[07:41] на самом деле На мой взгляд это часто
[07:43] случаи задачи распознавания сущности Где
[07:46] сегодня сущность это собственно ответ на
[07:47] вопрос
[07:54] Если вы поняли о чем это вопрос Напишите
[07:57] в комментариях Потому что я не знаю
[08:00] это такая архитектура кто изучал неронки
[08:03] наверняка
[08:11] сверточные сети какие там параметры
[08:13] количество входных и выходных каналов
[08:15] размер еда свертки шаг отступ Ну и
[08:19] что такое Кто не знает что это такое
[08:22] советую почитать статью на хабре чем
[08:24] нормально Расписал для ответа на вопросы
[08:26] пойдет
[08:30] незнакомо замечательно Вот это вот
[08:32] задачи которые
[08:33] маски
[08:34] [музыка]
[08:37] какой-то алгоритм обучения когда мы
[08:40] закрашиваем некоторые слова в
[08:41] предложении пытаемся сказать по
[08:43] контексту Что такое
[08:45] если вы не знаете наверняка на храбре
[08:48] есть хорошая
[09:00] Она выходе как он как может искать
[09:03] следующее слово то есть какие-то
[09:05] методики Трансформеры прошли
[09:09] это было те есть Нам нужно выбрать
[09:11] цепочку слов с максимальным
[09:13] правдоподобием Короче просто гриб Search
[09:16] всевозможные
[09:18] А как можно уменьшить размер модели эти
[09:21] есть техники Я знаю три это дистилляция
[09:23] и кандидат какие есть функции потерь Для
[09:27] НЛП для и для задачи классификации Разве
[09:30] я что-то кроме красоты Я не знаю
[09:42] дальше Мы перешли моим вопросам на мой
[09:45] вопрос про то знает и сам куда устроился
[09:47] он ответил
[09:48] [музыка]
[09:51] Все шифруются
[09:54] единственная большая проблема что у них
[09:56] считает их очень чувствительными поэтому
[09:58] они хотят чтобы с ними работали из офиса
[10:00] Но самое главное он меня заверил что нет
[10:03] никаких наркотиков и всего типа трафика
[10:06] какого-нибудь а так Нет ну ты поймешь Да
[10:10] ладно расслабьтесь я уже все понял На
[10:11] самом деле первый Собес когда меня туда
[10:13] взяли он был где-то месяц назад он был
[10:15] еще проще потому что еще не было этого
[10:17] мужика который нанимала это тимли А
[10:19] нанимал меня глава отдела по машинному
[10:23] обучению и этот Собес Он был очень
[10:25] простой потому что этот глава занимается
[10:27] иммелем всего 6 месяцев от силы и
[10:30] собственно все о чем мы с ним могли
[10:31] поговорить Это о том какой Чад G5 крутой
[10:34] Как можно много всего решать с его
[10:37] помощью В общем я просто показал пару
[10:39] своих проектов и меня взяли это был
[10:42] самый легкий совет своей жизни Ну это
[10:43] получилось уже посложнее конечно самое
[10:46] интересный момент про формат работает Вы
[10:48] помните что говорила что у них только
[10:50] офисная работа Я думаю что в начале как
[10:53] минимум
[10:54] в течение
[10:57] разговаривал И в общем договорились что
[11:01] полгода где-то нужен офис дальше когда
[11:04] они уже будут
[11:06] нормальные люди можно будет говорить о
[11:09] удаленке и не обязательно типа Кипр Да
[11:11] если бы у них была удаленка по России я
[11:13] бы согласился А ты Фух ребят такой
[11:14] получился Собес собственно вы все видели
[11:16] сами посмотрим дадут не оперы или нет но
[11:18] как он сказал что в принципе они готовы
[11:21] меня взять первый раз я к ним проходила
[11:23] не сделали мне offer 6000 евро по
[11:25] текущему курсу это 600 тысяч рублей
[11:27] собственно не такие уж и плохие условия
[11:28] согласились ли бы пойти на такую работу
[11:30] или нет Решайте сами Если вдруг у вас
[11:33] был опыт работы В подобных компаниях
[11:34] Пишите в комментариях очень интересно
[11:36] чтобы это все ставьте этому видео лайки
[11:39] Мне очень приятно что вы пишите
[11:41] комментарии
[11:42] слова поддержки я буду продолжать
[11:45] выкладывать собеседование буду делать их
[11:47] более интересными очень увидимся на
[11:49] следующем

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required for step 2 (Q&A extraction). splitter_prepare_prompt.py does not call any LLM API.
Do NOT substitute another model (e.g. GPT) unless the user explicitly overrides.
Required model: claude-sonnet-4-6
Suggested temperature: 0

======================================================================
STEP 2 AGENT RULES (mandatory — Cursor / Claude Code)
======================================================================
Target version for this run: v1 only.
Write JSON only to: splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. data-scientist-senior-1xbet-novoselov-2023-08-02.v1.qa-split.json, v2, ... except the target path above).
- Reuse items[] or field text from older splitter runs because validation passed before.

REQUIRED on step 2:
- Extract Q&A solely from PRIMARY_TRANSCRIPT in this LLM_INPUT_STEP_2 block.
- Do NOT read video.md or YouTube chapter titles (validation-only; absent in real interviews).
- Full fresh extraction; overwrite the target JSON completely.
- interviewer_feedback: interviewer speech only; candidate continuation -> candidate_answer or null feedback.
- Truncated interviewer ASR: merge adjacent interviewer lines in the transcript; do not paraphrase from external outlines.

======================================================================
LOCALE (mandatory — JSON + validation report)
======================================================================
INTERVIEW_LANGUAGE: ru (обязательно для этого прогона)
- Все поля text в JSON — дословные фрагменты из PRIMARY_TRANSCRIPT на русском. Без перевода на английский.
- Запрещены пересказы («кандидат рассказал о…», «The candidate…»).
- Метки question_type / question_topic / interview_stage — enum на английском (схема), тексты Q&A — только русский ASR.


======================================================================
OUTPUT PATHS (post-processing)
======================================================================
Save JSON to: splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.qa-split.json \
    --video transcripts/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.qa-split.json --out splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.qa-split.json \
    --video transcripts/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/video.md \
    --tolerance 120 \
    --out splitter_output/real-interviews/novoselov/data-scientist-senior-1xbet-novoselov-2023-08-02/data-scientist-senior-1xbet-novoselov-2023-08-02.v1.validation-report.md

Sections: auto-parsed from `Секция «…»` in video.md Description.
Optional topic_map override:
  --section-config .claude/skills/splitter/step4-validate-chapters/section_topic_map.karpov_mock.json

Full procedure: .claude/skills/splitter/SKILL.md
```

<!-- /LLM_INPUT_STEP_2 -->
