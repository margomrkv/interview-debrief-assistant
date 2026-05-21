<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22",
  "transcript_folder": "transcripts/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22",
  "source_id": "ml_engineer_senior_linkedin_recommendation_engine_interview_query_2021_06_22",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:18:04 +0200",
  "updated_at": "2026-05-20 21:30:49 +0200",
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
    "json": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/timecodes.txt",
        "en",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 21:18:04 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 2.0,
      "notes": null,
      "finished_at": "2026-05-20 21:30:48 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 2.0,
      "notes": null,
      "finished_at": "2026-05-20 21:30:49 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22`
- **Source ID:** `ml_engineer_senior_linkedin_recommendation_engine_interview_query_2021_06_22`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:18:04 +0200
- **Last updated:** 2026-05-20 21:30:49 +0200

Фильтр в IDE: `*ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/timecodes.txt`<br>`en`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.pipeline-log.md` | — | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.xlsx` | 2.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.validation-report.md` | 2.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.pipeline-log.md`

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
SOURCE_ID: ml_engineer_senior_linkedin_recommendation_engine_interview_query_2021_06_22
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22
INTERVIEW_LANGUAGE: en
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00] hi everyone uh this is jay here from
[00:03] interview query and today i'm with bed
[00:06] uh ved is currently a phd student
[00:09] at uh which university actually uh
[00:12] university of nebraska atlanta
[00:14] nebraska okay great and he's working at
[00:16] linkedin currently as
[00:18] a machine learning research scientist
[00:20] intern
[00:21] and so then i'd love for you to
[00:22] introduce yourself with your background
[00:24] and tell
[00:25] us a little bit more about how you got
[00:26] into data science okay
[00:28] uh thank you so much jay uh hi everyone
[00:31] my name is vade as jay mentioned and
[00:35] currently i'm doing a research data
[00:37] science internship
[00:38] with linkedin where we are looking at
[00:40] some a b testing approaches
[00:43] with that are deeply entrenched in the
[00:46] software development cycle
[00:48] i'm currently doing a phd in statistics
[00:50] where my research mainly focuses on
[00:53] recommendation systems and
[00:55] one recurring problem in recommendation
[00:57] systems is how do we incorporate
[01:00] multitude of features that are there
[01:02] there are many type of features that can
[01:04] be there
[01:05] and i also work in computer vision
[01:07] previously i completed my masters in
[01:09] stats from university of minnesota and
[01:12] i worked as a data science intern before
[01:15] this
[01:15] at travelers insurance um seagate
[01:19] technology where i was deploying some
[01:21] recommendation systems for some internal
[01:23] use and i've
[01:24] also had a brief stint with hennepin
[01:27] county which is like
[01:29] the county office for
[01:32] the county that minneapolis is
[01:34] encompassed in so
[01:36] that's my brief background i'm mostly
[01:38] interested in statistical concepts like
[01:41] a b testing recommendation systems
[01:43] computer vision but
[01:45] um the field is so wide that i feel at
[01:47] some meta level these are all connected
[01:49] and
[01:50] that's about me yeah definitely i'm sure
[01:53] that
[01:54] you know there may be testing two
[01:55] different pictures right now
[01:57] um as we speak on uh unsuspecting
[01:59] demographics to get them to click more
[02:02] uh we're in the right field
[02:06] for the question that i have today uh
[02:08] for this mock interview
[02:09] um i wanted you to ask was actually
[02:12] around a job board
[02:13] so kind of similar um but essentially
[02:17] uh this is kind of our weekly challenge
[02:19] question so pm wants to build
[02:21] a related jobs feature on every
[02:23] individual job description
[02:25] page right so this would be kind of like
[02:27] uh if you look on indeed right now
[02:29] there'd be like a job description and
[02:31] then on the right side
[02:32] it'd be like related jobs that you could
[02:34] apply to
[02:35] and so given that you're presented with
[02:38] this
[02:39] scenario you quickly realize that
[02:41] there's millions
[02:42] of new jobs posted every single day on
[02:45] the job board
[02:46] and finding the top 10 related jobs for
[02:48] every single job posted each
[02:50] day could be extremely inefficient the
[02:52] question is explain a system or a method
[02:55] that could solve the problem of finding
[02:56] the top 10 closest related jobs
[02:59] for millions of new jobs posted every
[03:02] single day
[03:03] 10 jobs okay yeah that's a great
[03:05] question and i think a
[03:07] very applied question um that many
[03:10] job boards could benefit from uh before
[03:13] i dive into
[03:15] the answers and kind of how i would
[03:17] attempt this one question i had is
[03:21] this particular question talks about
[03:24] retrieval of
[03:24] top 10 jobs from the jobs that were
[03:27] posted
[03:29] on that particular day could the jobs
[03:31] which
[03:32] have been posted in the past are they
[03:35] out of the table like are we not
[03:37] considering the jobs that have
[03:39] already been posted and it's only
[03:42] advertising the new jobs that have been
[03:43] posted today or are we also open to
[03:46] some previous jobs that might have
[03:49] already been posted
[03:51] yeah let's say um that for every single
[03:54] job we want to be able to consider all
[03:56] the jobs that have been posted in the
[03:57] past
[03:58] like month okay so we'll use like the
[04:00] past month as like a heuristic
[04:02] as it being active uh basically any kind
[04:05] of active job
[04:06] okay any kind of active jobs yes why i
[04:09] ask is because
[04:10] um some of the jobs that have been
[04:14] posted
[04:15] in the past um it would have been time
[04:19] for a lot of the other users to
[04:21] interact with those jobs as well which
[04:23] kind of gives us crucial
[04:25] information and patterns to mine as
[04:27] compared to
[04:28] some jobs which have been only posted
[04:30] today because
[04:32] if we are trying to find jobs which have
[04:33] been only posted today
[04:35] we lose out on any sort of user and item
[04:38] interactions because probably not a lot
[04:40] of people have interacted so
[04:42] the only way you could go about
[04:44] retrieving new jobs is through
[04:46] these embeddings and finding some
[04:48] closest some vector similarities and all
[04:51] that
[04:51] so okay uh using your
[04:54] info of uh using a heuristic of the last
[04:58] one month um we have to find
[05:01] um the related jobs uh that would be
[05:04] there so let me try to approach it with
[05:07] is it okay to share a whiteboard and
[05:09] yeah kind of just draw some stuff
[05:11] yeah okay so
[05:15] how i'm envisioning is is i'll try to
[05:18] because i think it is also important to
[05:20] see whether the
[05:21] company or the particular job board who
[05:24] has this project
[05:26] has the functionalities and capabilities
[05:28] to
[05:29] attempt this problem in the way that i'm
[05:31] doing right now so if any point of time
[05:33] you feel that oh
[05:34] maybe they do not have data like this or
[05:37] maybe
[05:38] this is not what they can do with the
[05:41] current resources just let me know and
[05:43] we can
[05:44] probably go down some other path but i'm
[05:46] assuming that
[05:47] at least what they have information on
[05:51] is the users
[05:55] are over here and the particular
[05:58] jobs are over here so this is just a
[06:01] matrix
[06:01] of a user and a particular job
[06:05] uh right so maybe we have user number
[06:07] one
[06:08] user number two up to a lot of other
[06:10] users
[06:11] here we have job id number one job id
[06:14] number two
[06:15] till job id number hundred and i'll i'll
[06:18] tell you a bit about
[06:20] why i'm going this route because um you
[06:22] had
[06:23] the question mentions that um that
[06:26] there are nlp concepts such as bag of
[06:29] words
[06:30] or uh word embeddings um
[06:34] i was just wondering is there any um
[06:37] like these are the methods that have
[06:39] been tried and we want to look at
[06:41] something new
[06:42] or using those nlp concepts is also fair
[06:46] game
[06:47] yeah yeah using any nlp concepts are
[06:49] fair game
[06:50] okay um i think those are just kind of
[06:52] examples of
[06:53] birds code science somewhere they're all
[06:55] things that
[06:56] are okay sure so this
[06:59] what uh i'm talking that the algorithm
[07:02] that i'm talking about right now is
[07:04] just the classic collaborative filtering
[07:07] the matrix factorization algorithm so
[07:10] um let's just assume and you can tell me
[07:12] if they have data like this or not
[07:14] let's just consider one particular user
[07:17] we would have information on
[07:20] uh let's say whether this user applied
[07:23] to job number one uh maybe he did not
[07:26] apply to job number two maybe he did not
[07:28] apply to job number three he applied to
[07:29] something over here
[07:31] uh and likewise so would it be a fair
[07:34] assumption to assume that they might
[07:35] have information like this
[07:37] yeah yeah so i guess to get the
[07:40] information to this
[07:42] yeah you're right so they would
[07:43] definitely have this information because
[07:44] it's the activity
[07:45] right but they'd only have for all the
[07:47] previous jobs
[07:48] but not yes they yeah yeah they would
[07:51] only have it for the previous jobs like
[07:53] the last
[07:54] uh 30 days and
[07:57] yes the that's a good point to bring up
[08:00] because we always have to think about
[08:02] what who are the target population that
[08:05] we are trying to
[08:07] propagate or advertise so this
[08:09] particular explanation will
[08:11] only aim for jobs uh let's say which
[08:14] have been there maybe we can put a
[08:15] heuristic like
[08:17] all the jobs which have had at least one
[08:20] interaction
[08:21] something like that so so maybe this is
[08:24] all the jobs which at least have one
[08:27] interaction
[08:28] uh in them and perhaps uh we can discuss
[08:31] how to tackle the latest jobs because
[08:34] uh they would not fit in this same
[08:37] matrix factorization way we would have
[08:39] to look at just some brute force
[08:41] nlp stuff for that but um this would
[08:44] give us
[08:44] like a nice way to attempt at jobs which
[08:47] have already been there
[08:48] so um what i'm thinking about this
[08:52] is there are uh so let's say this
[08:55] particular user has already applied to
[08:57] job 1
[08:58] has already applied to job 70
[09:01] there are a lot of missing spaces over
[09:04] here right
[09:04] we neither have zeros over there because
[09:08] zero would mean that he did not apply
[09:11] this is an example of explicit feedback
[09:14] where we only know the positive
[09:17] occurrences between the user and the
[09:19] item we never know
[09:20] which job he did not apply to because
[09:23] maybe he was interested and he was just
[09:26] not aware that such a job is there and
[09:28] that's the beauty of recommendations
[09:31] so the goal here if i were to explain it
[09:34] simply
[09:35] if we could come up with such an
[09:38] algorithm
[09:38] that helps us fill these empty spaces
[09:42] with a probability
[09:43] like maybe 0.8 or
[09:47] 0.9 then we would have a clear-cut
[09:50] probabilistic interpretation that okay
[09:52] if we recommend job number 68
[09:56] to user number one uh perhaps he would
[09:59] like it ninety percent of the time um or
[10:02] his liking his affinity to this
[10:04] particular job is 90
[10:06] and i agree the goal is
[10:09] not to target a user but
[10:12] to target a particular job and retrieve
[10:16] similar items to that particular job
[10:18] which i will get to once i talk about
[10:20] the algorithm
[10:22] but these kind of algorithms helps us
[10:25] address
[10:25] two major holy grails and recommendation
[10:31] retrieving similar items to the product
[10:33] but if you want to do some more
[10:35] targeted search right because whenever
[10:38] someone pulls up a particular job we
[10:41] know who that person is
[10:42] we know who what job that is so
[10:46] we could attempt it from either way from
[10:49] a user perspective
[10:50] or from an item perspective so i think
[10:52] how this problem is framed
[10:54] is from an item perspective but we can
[10:56] also attempt it from the user
[10:57] perspective
[10:58] and the interpretation of that would be
[11:01] if you
[11:02] give recommendations to the user which
[11:04] is
[11:06] tailored to him that would be a more
[11:08] personalized recommendation
[11:10] okay so do you have any questions any
[11:13] other directions you would want me to
[11:14] address else
[11:15] we can i can start talking about the
[11:17] algorithm a little bit from high
[11:19] perspective
[11:20] yeah so i guess to summarize if i
[11:23] understand it correctly like
[11:24] if we can apply these um measured
[11:28] characteristics we can get more features
[11:30] for the jobs
[11:31] and then user characteristics as well
[11:34] exactly how does that i guess then apply
[11:37] back to kind of the
[11:38] related jobs problem yeah exactly and
[11:41] i'll get
[11:42] to that i'm trying to see how um
[11:45] i can clear this let me see so let me
[11:48] rephrase your question uh you
[11:50] mentioned how will we use this algorithm
[11:53] to make the recommendations or
[11:55] finding the jobs for the relevant job so
[11:58] let's try to get at that so the the goal
[12:01] for us is we have a big matrix
[12:05] let's say let's call the dimension
[12:08] over here users so let's say there are m
[12:11] number of users
[12:13] and there are n number of items so
[12:16] the dimensionality of the matrix is m
[12:19] by n so
[12:22] the matrix factorization what it does is
[12:26] it comes up with two matrices which are
[12:29] of the dimension
[12:30] m by f
[12:34] and it also comes up with another matrix
[12:37] which has dimensions
[12:38] f by n so when you take a matrix
[12:41] multiplication of both of them
[12:44] you come back to the original dimensions
[12:46] which is m by
[12:47] n so
[12:50] once you find these lower so these are
[12:53] also matrix decomposition because what
[12:55] we are trying to do
[12:57] is we are trying to find two other
[13:00] matrices
[13:01] so this matrix is known as
[13:04] the user feature matrix and this matrix
[13:08] is known as the item feature matrix
[13:11] okay right so you can see that the
[13:13] dimensions match
[13:15] basically if i were to explain it simply
[13:18] what we have done in this process this
[13:20] is still high level
[13:21] is we are basically telling the
[13:23] algorithm that
[13:24] we think a user as well as an
[13:28] item can be expressed by
[13:31] a f dimensional vector so
[13:35] this algorithm automatically calculates
[13:38] these features uh
[13:39] obviously there is some loss function
[13:41] there is some sort of a stochastic
[13:43] gradient descent or any other
[13:44] optimization happening but this is the
[13:47] crux of the algorithm to understand
[13:49] the beauty in this algorithm that just
[13:52] realized that
[13:53] the only thing we had going in was just
[13:56] the interaction let's say
[13:58] if you and i were the only two users
[14:01] we literally only need to know what are
[14:04] the jobs you and i
[14:05] applied to that's it and this algorithm
[14:09] helps you
[14:10] create these abstract features for you
[14:12] and me which
[14:14] motivates so many downstream algorithms
[14:17] and that is why i like this because
[14:19] we started with nothing now we know a
[14:21] lot about
[14:24] me we know a lot about all the jobs that
[14:26] are there and now literally sky is the
[14:28] limit
[14:28] if we want to find similar users we can
[14:31] find similar users if we want to find
[14:32] similar jobs we can find similar jobs
[14:35] um so that's like the high level of
[14:39] this particular algorithm yeah so
[14:42] how uh what what would you like me to
[14:44] talk
[14:45] about how the training happens or
[14:48] uh should we base the execution from
[14:51] this high level perspective how would
[14:52] you like to
[14:54] proceed uh with the discussion
[14:57] i guess i'd be interested to figure out
[15:00] exactly
[15:01] what the i guess practical aspects are
[15:03] right because we dived into
[15:05] how the algorithm is going to work right
[15:08] it's major
[15:09] perfection we're taking activity from
[15:12] like the users and activity from the
[15:14] job or not the activity the users
[15:16] activity of the users on the job
[15:18] on the jobs right right and then um
[15:20] creating this
[15:21] uh now and dimensional by end yeah right
[15:26] training set and so how do we use that
[15:28] on like let's say a new job that comes
[15:30] in
[15:31] exactly yeah so going back to our
[15:34] earlier discussion we are only talking
[15:36] about the active job so far and the
[15:38] heuristic filter we put on this was
[15:40] all the jobs which have had at least one
[15:43] interaction
[15:44] and coupling this with the heuristic you
[15:46] told me last one month
[15:48] so the filters or the the filter on the
[15:50] sequel
[15:51] is like last one month at least one job
[15:54] so after you run this algorithm for the
[15:57] sake of simplicity and explanation let's
[15:59] just consider we have 10 jobs to offer
[16:02] or or let's just consider we have two
[16:04] jobs to offer
[16:06] right um let's actually make it till 10
[16:09] so we can motivate the example of
[16:11] retrieving after you are done running
[16:13] this algorithm
[16:14] all of these jobs will have a feature so
[16:17] this
[16:17] is a vector that i'm making over here
[16:19] and these have
[16:20] numbers filled in these are abstract
[16:22] features which have been
[16:23] uh extracted they don't have any um
[16:27] like artistic meaning like age or gender
[16:30] these are just
[16:30] abstract features which we can think of
[16:32] as a secret in coding for that job
[16:35] job number two will also have a secret
[16:37] encoding like that
[16:38] and job number 10 will also have a
[16:40] secret encoding like that
[16:41] so this is actually not very different
[16:45] from how
[16:46] the embeddings work in deep learning but
[16:49] the good thing about this algorithm is
[16:51] if you know a lot of the deep learning
[16:53] does not have analytical solutions it's
[16:56] stochastic gradient descent you have to
[16:57] make a bunch of passes through the data
[16:59] you have to
[17:00] make some epochs over the data but for
[17:03] matrix factorization there are some
[17:05] analytical solutions
[17:07] uh like basically matrix formulas which
[17:10] you can just use and iterate over
[17:12] very few times in order to find all of
[17:16] these features so just reiterating
[17:19] all of these features are what matrix
[17:21] decomposition gives us and we can call
[17:24] them
[17:24] item site features which basically means
[17:27] some sort of abstract representation of
[17:30] my jobs
[17:31] okay once we have all of these abstract
[17:34] representations
[17:36] a very nice thing to do would be to look
[17:38] at a correlation matrix right
[17:40] uh like what are the top 10 most similar
[17:43] jobs
[17:44] to item number to job posting number one
[17:47] or job posting number two
[17:48] or job posting number three which
[17:50] actually is a challenge because you
[17:52] mentioned
[17:52] um there are millions of job that are
[17:55] posted so i'm assuming even with those
[17:57] filters we will have quite a sizable
[18:00] number of jobs and doing those
[18:02] similarity calculations is not trivial
[18:04] right because let's say we have a
[18:06] million
[18:06] jobs the matrix would be 1 million by 1
[18:09] million which is a huge
[18:10] matrix and it wouldn't be a very sparse
[18:14] matrix which would take
[18:15] memory to store memory to look up memory
[18:17] to calculate
[18:18] causing downstream issues in latency and
[18:20] what not so
[18:22] i have an ad hoc solution for this um
[18:25] ideally we would want to go the route of
[18:28] not
[18:29] maybe doing ad hoc approaches but since
[18:31] there is a particular business
[18:32] requirement we
[18:33] we have to sort of find some hacks
[18:35] around this
[18:36] so how about this uh how about we take
[18:41] the
[18:41] idea of unsupervised algorithm to maybe
[18:44] make our lives a little bit easier and
[18:46] alleviate some of this problem
[18:49] there are always some assumptions to
[18:51] modeling that we have to take
[18:53] so if this assumption is
[18:56] tenable maybe we can go through with
[18:58] this process if not
[19:00] we will brainstorm something else so i
[19:02] am assuming
[19:04] this job board let's say if this is
[19:06] indeed or linkedin
[19:07] and let's say we or you or i pull up one
[19:10] particular job description of a data
[19:12] scientist right
[19:13] so there is an upper limit
[19:17] on the corpus of jobs which might be
[19:20] potential jobs for this
[19:21] because let's say a data scientist you
[19:24] might not want to recommend something
[19:25] for a mechanical engineer
[19:27] in that right or maybe for electrical
[19:29] engineer the class of jobs is very
[19:31] let's just say finite but obviously
[19:35] if we try to attempt it the manual way
[19:37] it might be a lot of problem because
[19:39] there can be so many features
[19:41] what do we stratify on what sort of
[19:44] hierarchical rules or
[19:46] manual rules we make is difficult how
[19:48] about this
[19:50] let's say if you remember we had n jobs
[19:53] so we had n jobs and
[19:56] we had f features
[19:59] on those jobs and these features have
[20:01] been extracted from this so
[20:03] over here it is one two three four so
[20:06] for example over here f is equal to four
[20:08] so now we have embedded every single job
[20:12] into a four dimensional vector right
[20:16] gotcha how about we just resort to some
[20:19] clustering algorithms like k
[20:21] means a very simple algorithm to cluster
[20:24] these jobs right
[20:26] maybe we will find that and we can look
[20:29] at things
[20:30] such as the very famous cree plots
[20:33] and what not uh which basically explain
[20:36] um
[20:37] some sort of measure of how good the
[20:40] clustering is so
[20:42] so over here we have the number of
[20:44] clusters and over here we have
[20:47] some particular metric i wouldn't
[20:49] pretend if i
[20:50] exactly know what that metric is over
[20:53] here but it basically
[20:55] uh tries to check let's just put it
[20:57] simply
[20:58] how good the k-mean is for this
[21:00] particular value of k so i think that is
[21:03] some measure of
[21:04] um how much is the variation explained
[21:07] between the clusters and within the
[21:09] cluster so something related to that but
[21:12] some measure of efficacy so let's say if
[21:14] we found that
[21:16] um there are five clusters in total
[21:19] right
[21:19] so uh now coming back to the problem if
[21:23] someone tells us
[21:24] hey wait can you recommend some
[21:27] similar jobs for job id number one
[21:31] we first map it back to the particular
[21:33] cluster
[21:34] so let's say this is in cluster number
[21:36] three then we have automatically
[21:39] uh discounted four of the other clusters
[21:43] right so that
[21:44] helps us in alleviating this problem of
[21:47] retrieval i'm not saying that this is a
[21:50] foolproof way
[21:51] obviously we would lose out on some good
[21:54] potential jobs that are there in some of
[21:56] the other clusters but
[21:57] if the business comes to us with a
[21:59] requirement we have to find some way of
[22:01] doing it and this is
[22:02] uh like my way of doing it so then it is
[22:05] pretty simple let's say
[22:06] uh we find job id one belongs to cluster
[22:09] number three
[22:10] and then we do the same kind of vector
[22:13] similarity for only the jobs that are
[22:15] there in the cluster number three
[22:17] uh not in all the other clusters so
[22:19] that's how
[22:20] um you could look at things like just
[22:22] the cosine scores
[22:24] um retrieve the top 10 ones but
[22:27] i am assuming the level of
[22:30] simplification
[22:31] that will be there with this approach is
[22:34] a direct artifact of
[22:36] how many inherent clusters are there in
[22:39] my job
[22:40] types if there are more number of
[22:42] clusters which will be automatically
[22:44] found out by
[22:45] some of these creep plots for k means
[22:48] then
[22:48] the level of simplification we do is is
[22:51] pretty significant if there are 10
[22:54] number of clusters then we have improved
[22:57] our finding algorithm to the order of 10
[23:00] which i think is a significant
[23:01] improvement
[23:02] so in order to summarize my approach the
[23:05] question
[23:06] you posed was we are a job board and we
[23:10] have to retrieve some similar jobs to a
[23:12] particular job
[23:14] and obviously there are many jobs so we
[23:16] do not want to just
[23:18] resort to the brute force way of looking
[23:20] at the similarities and
[23:22] my approach to this was let's just
[23:25] first look at only the occurrence data
[23:29] because uh one thing i have
[23:32] a lot of um disagreement on
[23:36] in our data science work is there is
[23:39] hardly
[23:40] i mean this might happen but i haven't
[23:42] seen it in my experience people directly
[23:44] jump to very complex solutions like okay
[23:46] we have nlp
[23:47] let's look at the data throw in a bunch
[23:49] of nlp text mining
[23:51] stuff but there is really no simple
[23:54] baseline to do that so
[23:55] how would we ever know how significant
[23:58] of an improvement do we have over a
[24:00] simple technique if a simple technique
[24:01] does the job
[24:03] then by ocam's razor we should be going
[24:06] with the simple stuff because it's
[24:08] easier to maintain
[24:09] deploy enhance so the idea i told was we
[24:12] will just take the user item matrix
[24:15] apply algorithms such as matrix
[24:17] factorization to extract
[24:19] abstract features on items which are the
[24:22] jobs
[24:22] and users as well then we still haven't
[24:26] solved the problem of retrieval we have
[24:28] only solved the problem of
[24:30] automatic feature generation so we will
[24:33] use that to cluster and when someone
[24:35] asks us to recommend a new job we will
[24:37] just find
[24:38] which particular cluster that job
[24:40] belongs to and then just make
[24:42] a vector similarity matrix for that
[24:45] particular job
[24:46] and sort by the cosine similarity so
[24:48] that's
[24:49] sort of my approach i'd be happy to
[24:50] discuss more ideas even news or any
[24:53] other questions you have
[24:54] no that sounds good so i guess my next
[24:58] question
[24:58] is more on the practical deployment side
[25:02] right um so you know we're let's say we
[25:05] attempt this
[25:06] right solution we get these jobs back
[25:10] we get like 10 jobs for every new job
[25:12] that gets posted
[25:14] everything looks good but how do we know
[25:17] if it's working well
[25:18] right how do we know how do we measure
[25:20] the
[25:21] efficacy of our like strategy right
[25:24] um are we testing this offline
[25:26] beforehand or are we like
[25:29] just rolling this out in production oh
[25:31] yeah that's a
[25:32] that's a great question because i think
[25:33] that's how we tie up
[25:35] the computer sciencey machine learning
[25:38] and deep learning with
[25:39] deriving some strategic insights with
[25:41] the use of a b
[25:42] testing before we push these changes out
[25:45] so
[25:46] and the reason to that is actually very
[25:48] fundamental
[25:51] let's discuss some very common metrics
[25:54] right let's just say
[25:55] root mean square error or average
[25:57] accuracy
[25:58] sure we when we are doing the local
[26:01] development testing out a bunch of
[26:03] models what is our approach we say okay
[26:05] i will test logistic regression i'll
[26:07] just random forest
[26:09] and whichever gives me the higher
[26:11] average accuracy
[26:12] is my model of choice right but the
[26:15] fundamental question we haven't
[26:17] addressed with this is
[26:19] is there a one-to-one correspondence
[26:21] between the average accuracy and how
[26:24] the end user will perceive it
[26:27] it's an open-ended question i mean sure
[26:32] but the problem is the observational
[26:34] data that we had collected was not
[26:36] collected in a controlled setting so
[26:38] making this sort of causal
[26:40] uh inferences can be a little bit of a
[26:44] slippery slope
[26:45] so coming back to the question of how
[26:47] would we know it is working
[26:49] so first of all uh we would have to
[26:53] discuss that there are two ways of
[26:55] knowing it is working or not
[26:56] one is the local metrics like the
[26:59] average accuracies or
[27:01] in this case accuracy does not make
[27:03] sense because
[27:04] why i say that is let's say we
[27:07] recommended
[27:08] job number one we recommended job number
[27:11] two
[27:11] and we recommended job number 10 to a
[27:13] particular user
[27:15] uh taking the average accuracy or
[27:19] basically saying
[27:20] okay how many of the 10 jobs did the
[27:22] user actually take
[27:23] is a bad metric because our metric
[27:26] should have some sort of
[27:27] ranking intuition in that because we
[27:30] should really
[27:31] give the mistake at the first position a
[27:33] higher penalty
[27:34] because let's say if i'm recommending
[27:36] you a movie
[27:38] at the very first position i better be
[27:40] sure about it because otherwise it
[27:42] translates to bad user experience so
[27:44] there are many ranking metrics
[27:46] that we have to look at which metric
[27:48] it's not important what is important is
[27:51] understanding this concept that if you
[27:53] are making recommendations
[27:54] usual metrics are not good we should
[27:56] look at some sort of a ranking metric
[27:58] so in order to do the local development
[28:00] you know find the better
[28:02] algorithm obviously matrix vectorization
[28:04] has a bunch of different hyper
[28:06] parameters
[28:06] k means we can do this sort of local
[28:10] development in order to basically come
[28:12] up with our best short algorithm and
[28:14] streamline process
[28:15] but we should also try to at least
[28:19] attempt to see how the end user will
[28:22] perceive
[28:23] recommendations from this right so i
[28:25] mean i'm assuming
[28:26] since the job board already is doing
[28:29] that there would be
[28:30] let's say the current standard of doing
[28:33] that recommendations right be it just be
[28:36] uh some sort of a very simple way of
[28:39] retrieval
[28:39] or any other way of retrieval uh
[28:42] we can take that uh what we can do is
[28:46] we at this point of time we have to talk
[28:48] to the company we have to talk to them
[28:50] hey are you guys allowing me to maybe do
[28:53] a very
[28:54] small randomized study where i will put
[28:57] some groups in the control group all of
[29:00] them will see recommendations
[29:02] from your current state of the art or
[29:05] whatever you are using
[29:06] and let's do the second group show
[29:09] recommendations from this modified
[29:11] approach of matrix factorization plus
[29:14] clustering followed by retrieval and
[29:16] then let's just
[29:18] basically use statistics to make some
[29:20] inferences right that would be getting
[29:21] into the inferential territory
[29:24] so we have to ask them can we do things
[29:26] like that do you have
[29:28] um the facilities do you have the budget
[29:30] do you have the patience
[29:32] and more so do you have the the
[29:35] interest to do that um then
[29:38] that's the gold standard um if we can do
[29:41] an experiment there is nothing better
[29:43] than that
[29:44] however if we are not able to do that we
[29:47] can also do something known as a causal
[29:49] analysis which is
[29:50] our best shot at
[29:53] recreating an experiment with the
[29:55] current data that is there so at this
[29:57] point of time
[29:58] uh in order to see if this thing is
[30:00] actually working
[30:02] um there are two ways one is from the
[30:04] modeling aspect one is from the end user
[30:06] consumption aspect
[30:08] and the second i would say is more
[30:10] important so i would ask the company
[30:12] can we do a small randomized study if
[30:15] they say yes that's the best thing
[30:17] um the inferences from there are very
[30:19] solid and have a sound theoretical
[30:21] underpinning
[30:22] if not we can go at some more ad hoc
[30:25] ways
[30:25] but obviously any sort of qualitative
[30:28] statement i make over there
[30:30] would have to be taken with a grain of
[30:32] salt because we have not randomized the
[30:34] groups um
[30:36] in a controlled fashion we are only
[30:38] trying to recreate it so
[30:39] that would be my uh two approaches and
[30:42] uh happy to discuss if we want to drill
[30:45] down on either of those
[30:47] i guess my last one would be what if
[30:50] that this is a because this is a new
[30:52] feature that's
[30:53] not launched yet let's say that we want
[30:56] to build this new feature
[30:58] okay and there's no like prior matching
[31:00] algorithm there's no prior related
[31:02] jobs what do we compare it to now to
[31:04] actually set a standard for success
[31:07] um okay so
[31:12] do you mean that this feature is not
[31:15] directly there
[31:16] as in in the sense that the company is
[31:18] not doing this kind of thing
[31:20] like they are not retrieving the top 10
[31:22] jobs and this is the very first time
[31:24] something like this would be attempted
[31:25] is it like that yeah like that so it's
[31:27] like this is the first time they're
[31:28] trying it
[31:30] then they want to build this feature for
[31:31] the first time yeah for sure um
[31:34] i mean um yeah so that kind of
[31:37] limits our options but not our
[31:40] motivations and
[31:41] excitement to do this in that case we
[31:44] can at least do our due diligence to do
[31:46] a best
[31:47] local validation that is having a sound
[31:50] validation set
[31:51] and a test set and finding our best set
[31:54] of hyper parameters
[31:55] and all that so that is only for the
[31:57] modeling aspect
[31:59] if if the company is still interested in
[32:01] knowing how the end user
[32:03] will perceive it that becomes a little
[32:07] bit tricky because
[32:08] we do not have current standards
[32:11] to compare it to to say that okay this
[32:14] would be an
[32:14] improvement uh but how i would attempt
[32:17] that is through an iterative process
[32:20] so what i would tell them is obviously
[32:23] uh you want to implement this feature
[32:25] so you guys do realize there is some
[32:28] definite
[32:28] utility and roi that you might derive
[32:31] from such a feature
[32:33] so how about we do this uh we
[32:36] come up with let's just put this box
[32:38] this box is everything we have done so
[32:40] far
[32:41] any type of model any type of retrieval
[32:43] any type of clustering
[32:45] uh obviously at time step
[32:48] zero they do not have any product so
[32:52] this decision can be boiled down to a
[32:54] binary decision
[32:56] and i will tell you my opinion on this
[32:58] and you can also tell
[33:00] rolling it out to the 100 audience is
[33:02] never a good strategy
[33:04] because we do not have ways to scale it
[33:07] back we do not have ways to stop the
[33:09] experiment if we notice negative effects
[33:11] so how about we start with some gradual
[33:13] stuff let's
[33:14] just first show it to five percent or
[33:17] 10 of the users uh
[33:21] at this point of time i don't think we
[33:23] would be able to compare it with any
[33:25] other state of the art because there is
[33:28] not one
[33:29] at the moment but we can get a good
[33:31] enough sense of
[33:33] okay is it too bad is it
[33:36] not that bad is it working by just
[33:38] looking at some descriptive statistics
[33:40] right at this point of time
[33:41] more so we are just making sure that we
[33:43] have some sort of
[33:44] sanity check and um so we roll it out at
[33:48] p0
[33:49] we show it to five percent if things
[33:50] look good we take it to ten percent
[33:53] twenty percent thirty percent um and at
[33:56] that point of time we would start to
[33:58] gain some data in an intelligent fashion
[34:00] of how the end user is perceiving it
[34:03] because um if you take a good sampling
[34:06] of the users we do not need to show it
[34:08] to everyone right the the analogy to
[34:10] that is if we are sick
[34:12] and we go for a blood draw they do not
[34:14] take our whole blood
[34:15] uh to check if we have an issue or not
[34:18] they just take a good enough sample and
[34:20] then
[34:20] from there they are able to tell a lot
[34:22] of very important stuff
[34:24] and provided we are doing this initially
[34:26] making sure this
[34:27] is working at time step one
[34:30] now we have a current state of the art
[34:33] or let's just say current state of
[34:35] execution whatever we have right now so
[34:37] from the second iteration
[34:39] we can start to do an a b testing as
[34:41] well here is what i have
[34:43] so far and now we can start to improve
[34:46] and
[34:46] throw in some baseline approaches throw
[34:48] in some modified approaches and
[34:51] really proceed in a data driven way we
[34:53] do not go in with any sort of philosophy
[34:56] or any sort of um
[35:00] biases that we might have of what we
[35:02] think it works it would be a very
[35:04] data vetted way we will only proceed if
[35:07] the data tells us to proceed
[35:09] if not we will all collaborate together
[35:11] to think of how we might
[35:13] address this issue so in order to
[35:15] summarize
[35:16] uh how we will know if it actually works
[35:19] if the company does not have the product
[35:22] we will come up with our best uh
[35:24] approach
[35:25] and at time zero we will start to show
[35:27] it to five percent ten percent if things
[35:29] look
[35:30] good you'll gradually scale it up once
[35:32] we have
[35:34] made the advent or the start or
[35:36] initiation
[35:37] of this method from the second iteration
[35:40] on
[35:40] we can resort to small scale a b testing
[35:43] in order to
[35:44] make very strong inferences on whether
[35:46] this approach is good
[35:48] and a b testing can also help shed light
[35:51] on a lot of the key processes right i
[35:53] think of this
[35:54] as a giant car and doing the a b testing
[35:57] can tell us whether the
[35:58] problem is in the engine whether the
[35:59] problem is in the wheels
[36:01] whether the problem is in the
[36:02] transmission so it actually gives us
[36:04] really good ways to diagnose
[36:06] what might not be going right and in
[36:09] doing that sort of
[36:11] diagnosis we are not resorting to any
[36:13] bias of the data scientist or any
[36:15] preconceived notions
[36:17] we are asking the data to guide us in
[36:19] this journey of continuous improvement
[36:22] so that the company benefits from this
[36:24] sort of rnd any sort of r d
[36:26] that we do which does not have tie ups
[36:30] with how might we use that
[36:32] institutional memory and information
[36:34] would not be a good research and
[36:36] development so this provides a seamless
[36:38] strategy
[36:39] going into the future that's interesting
[36:42] actually i think having a process for
[36:45] strategizing how development goes out
[36:48] is important given the fact that many
[36:51] times
[36:52] almost all the times actually it's
[36:54] always iterative in its approach
[36:55] for sure right you don't actually get
[36:57] the best result once you immediately
[36:59] launch
[36:59] your classifier uh yeah i would say one
[37:03] additional point is
[37:04] yeah uh we could try like running some
[37:07] random seed algorithms right so you
[37:09] could
[37:10] cheat it with like oh wow completely
[37:12] random jobs yeah
[37:13] yeah and then see if it actually
[37:15] performs better
[37:17] that's a i would say that's a very good
[37:19] point in order to bring
[37:20] like let's say because obviously we want
[37:23] to be better than random at least
[37:25] like how far apart we are from random
[37:28] will tell us how we are proceeding so i
[37:29] really like that point
[37:30] let's just recommend random stuff even
[37:33] if
[37:33] so that would actually give us ways to
[37:35] do this sort of a b testing right from
[37:37] the onset
[37:38] yeah we would just say okay let's
[37:41] first at least try to prove that what
[37:44] our data scientist came up with
[37:46] is better than random because if it is
[37:48] not then we have some real
[37:50] issues over here so let's say at the
[37:51] first iteration
[37:53] we use your idea to have one group who
[37:55] sees random seed recommendations another
[37:58] group which sees
[37:59] our recommendations then at least we
[38:01] have a winner
[38:02] at the first stage so now we just
[38:04] proceed in this round robin format
[38:06] whoever wins in the previous iteration
[38:09] goes into the next stage of development
[38:11] and now we
[38:12] have it compete with another variant of
[38:15] the algorithm i think that's a great
[38:16] strategy which actually
[38:18] decreases this development duration by
[38:21] however much the gap between p0 and t1
[38:24] is
[38:24] so yeah i really like that idea as well
[38:26] that's good yeah always having a
[38:28] baseline against
[38:30] something is good especially as the
[38:32] model probably
[38:33] continuously retrains right for sure
[38:36] bias or go in a different direction
[38:39] right
[38:39] yeah yeah no but these these are all
[38:42] really
[38:42] interesting problems at the heart of
[38:45] recommendation system i just feel
[38:47] like recommendation system is uh i'm not
[38:49] sure if it is a broadly studied topic
[38:51] within machine learning but i feel it
[38:53] just
[38:54] kind of gives us so much to work with
[38:56] and so many different directions to go
[38:59] on depending upon what the business uses
[39:01] it helps us find similar users
[39:03] and i just like to share one small point
[39:06] uh
[39:07] in a few minutes um i took a
[39:09] recommendation system class
[39:11] and our professor told
[39:14] us that only making recommendations is
[39:16] not
[39:17] important um and and the reason he told
[39:20] is
[39:21] um let's say we go to walmart and we
[39:24] paste on every single cart hey i am
[39:27] recommending that you buy bananas and
[39:30] milk
[39:30] that would be a pretty strong
[39:32] recommendation right everyone buys
[39:34] bananas and milk
[39:35] but whether was it a useful
[39:37] recommendation absolutely not
[39:39] they would have bought it anyways so
[39:41] knowing the intention of
[39:43] what the user would already be doing we
[39:46] need not recommend him that stuff
[39:48] but what he probably has an inclination
[39:51] for um is really the sweet spot and um
[39:57] this is open-ended how would we go about
[40:00] mining that sort of attention and uh
[40:03] one solution to that was we
[40:06] always explain our recommendations if
[40:08] you look at amazon if you look at
[40:10] netflix they always make efforts to tell
[40:12] us okay
[40:13] we are recommending you this coffee
[40:15] machine because you just recently bought
[40:17] coffee beans or
[40:19] we are recommending you this particular
[40:20] movie because you recently saw this
[40:22] movie so
[40:24] explaining why we are making a
[40:26] particular recommendation helps the user
[40:28] relate
[40:29] to this recommendation and makes it more
[40:31] amenable
[40:32] to consume that recommendation otherwise
[40:35] they feel that the recommendations are
[40:37] sort of
[40:37] in your face recommendations you know
[40:39] like the the company or the product is
[40:42] forcing me to take this and that sort of
[40:45] creates
[40:46] some apprehension and obviously this is
[40:48] just my hypothesis
[40:49] um working in this field for some years
[40:52] but these are some of the
[40:53] sort of next step questions to address
[40:56] once you have a basic system built
[40:59] yeah definitely and i think that it's
[41:02] almost like second order effects
[41:04] right because if the first
[41:05] recommendation is bad
[41:07] then you're not likely to go downstream
[41:10] unfortunate recommendation again but if
[41:11] it's good
[41:12] then it can create a cascading effect on
[41:14] its own oh yeah yeah if we are able to
[41:17] capture their attention and interest
[41:19] right when they first start to interact
[41:21] with our recommendation system we might
[41:23] also be able to
[41:24] hold on to those users or otherwise we
[41:27] might run the risk of them
[41:29] not coming back and interacting with our
[41:31] system which would be
[41:32] a loss for the company exactly awesome
[41:36] cool

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
Write JSON only to: splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.json, v2, ... except the target path above).
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
INTERVIEW_LANGUAGE: en (mandatory for this run)
- All text fields in JSON must be verbatim contiguous spans from PRIMARY_TRANSCRIPT in English. No Russian translation.
- Forbidden: summaries («The candidate explained…», «кандидат сказал…»).
- Labels question_type / question_topic / interview_stage stay English enums (schema); Q/A wording stays English ASR only.


======================================================================
OUTPUT PATHS (post-processing)
======================================================================
Save JSON to: splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.json \
    --video transcripts/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.json --out splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.qa-split.json \
    --video transcripts/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.validation-report.md

Sections: auto-parsed from `Секция «…»` in video.md Description.
Optional topic_map override:
  --section-config .claude/skills/splitter/step4-validate-chapters/section_topic_map.karpov_mock.json

Full procedure: .claude/skills/splitter/SKILL.md
```

<!-- /LLM_INPUT_STEP_2 -->

<!-- LLM_INPUT_STEP_5 -->

## Шаг 5 — семантическая валидация глав

Модель читает **только этот блок** на шаге 5 (не `video.md`, не другие интервью).

```text
======================================================================
SYSTEM
======================================================================
You validate splitter Q&A JSON quality for a mock/real interview transcript.

Context:
- YouTube chapters (video.md) are an external checklist. They are NOT the only way questions appear in the transcript.
- Follow-up questions inside a section are valid items even if they are far from a chapter marker or sit in a neighboring chapter window.
- The deterministic validator (step 4) uses strict per-window boundaries. The semantic validator (step 5) uses a 120-second tolerance.
- Small timestamp drift (even 1–60 seconds) between an item's timestamp and the chapter marker is NORMAL and must NOT trigger false flags. Judge by content match, not by exact boundary crossing.

For each listed chapter you receive:
- chapter time, title, and time window until the next chapter
- zero or more extracted items (interviewer_question, candidate_answer, reference_answer, interviewer_feedback, labels)

Judge two dimensions per chapter:

1) time_alignment_ok — true when:
   - at least one item exists in this chapter's window OR in an adjacent window within 60 seconds of this chapter's marker, covering the chapter's topic
   - interviewer_question.time is plausible for the chapter topic (no obviously wrong-minute timestamps)
   - do NOT fail because an item sits in a neighboring window due to small drift, or is a follow-up in the same topic block

2) content_alignment_ok — true when:
   - the chapter's topic is covered by an item in this window or an adjacent item within 60 seconds (before or after the marker)
   - question_type, question_topic, interview_stage fit the content
   - candidate_answer contains only the candidate's speech (flag false if interviewer lines like "давай я приведу пример", "я понял", "окей" are mixed into candidate_answer together with candidate phrases)
   - interviewer_question is a complete intelligible question (flag false if truncated ASR: ends mid-clause like "...еще не Что", "...должен быть", or duplicates the opening of candidate_answer)
   - interviewer_question and candidate_answer do NOT share a long verbatim prefix (flag false if the first 6+ words are identical — echo / mis-attributed span)
   - interviewer_feedback contains only the interviewer's speech (flag false if candidate biography/case continuation appears there: "я пошёл", "у нас Kanban", "мы причесали", "я считаю что лучший код", etc. — that belongs in candidate_answer)
   - self-answered interviewer turns correctly use candidate_answer.text = null and reference_answer for the explanation

When a chapter shows 0 extracted items (recognition_status: not_recognized):
- Look at the previous chapter's last item(s). If one has a timestamp within 60 seconds BEFORE this chapter's marker AND its content matches this chapter's title → set BOTH flags true, leave notes as empty string "". This is normal drift within tolerance.
- Set both flags false ONLY when the topic is genuinely not covered anywhere nearby: truly missed question, or a discussion/explanation segment with no interviewer question.

Return ONLY valid JSON matching the schema. No markdown fences.
Language for notes: English. Keep notes short and actionable. Leave notes as "" when both flags are true.

Correction hints (for notes when content_alignment_ok is false):
- Step 2 must use PRIMARY_TRANSCRIPT only; never suggest pasting YouTube chapter titles into interviewer_question.
- For truncated ASR or Q/A duplicate prefix: suggest merging adjacent interviewer lines in the transcript or re-cutting spans; for real interviews there is no video.md.

======================================================================
OUTPUT SCHEMA
======================================================================
{
  "type": "object",
  "additionalProperties": false,
  "required": ["chapters"],
  "properties": {
    "chapters": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "chapter_time",
          "time_alignment_ok",
          "content_alignment_ok",
          "notes"
        ],
        "properties": {
          "chapter_time": {
            "type": "string",
            "description": "HH:MM:SS from video.md chapter"
          },
          "time_alignment_ok": {
            "type": "boolean",
            "description": "true if extracted item times fall within this chapter window and match the chapter topic timing"
          },
          "content_alignment_ok": {
            "type": "boolean",
            "description": "true if question/answer texts match the YouTube chapter title meaning"
          },
          "notes": {
            "type": "string",
            "description": "Short Russian explanation; empty string if both checks pass"
          }
        }
      }
    }
  }
}

======================================================================
CHAPTERS TO VALIDATE
======================================================================
video.md: transcripts/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/video.md

--- CHAPTER `00:00` — Ved's background and introduction ---
window: 00:00 .. 02:20
recognition_status: multiple (2 items)

ITEM #1
  interviewer_question: time=00:22 text="and so then i'd love for you to introduce yourself with your background and tell us a little bit more about how you got into data science"
  candidate_answer: time=00:28 text="uh thank you so much jay uh hi everyone my name is vade as jay mentioned and currently i'm doing a research data science internship with linkedin where we are looking at some a b testing approaches with that are deeply entrenched in the software development cycle i'm currently doing a phd in statistics where my research mainly focuses on recommendation systems and one recurring problem in recommendation systems is how do we incorporate multitude of features that are there there are many type of features that can be there and i also work in computer vision previously i completed my masters in stats from university of minnesota and i worked as a data science intern before this at travelers insurance um seagate technology where i was deploying some recommendation systems for some internal use and i've also had a brief stint with hennepin county which is like the county office for the county that minneapolis is encompassed in so that's my brief background i'm mostly interested in statistical concepts like a b testing recommendation systems computer vision but um the field is so wide that i feel at some meta level these are all connected and that's about me"
  reference_answer: time=None text=None
  interviewer_feedback: time=01:50 text="yeah definitely i'm sure that you know there may be testing two different pictures right now um as we speak on uh unsuspecting demographics to get them to click more uh we're in the right field"
  question_topic: Communication

ITEM #2
  interviewer_question: time=02:06 text="for the question that i have today uh for this mock interview um i wanted you to ask was actually around a job board so kind of similar um but essentially uh this is kind of our weekly challenge question so pm wants to build a related jobs feature on every individual job description page right so this would be kind of like uh if you look on indeed right now there'd be like a job description and then on the right side it'd be like related jobs that you could apply to and so given that you're presented with this scenario you quickly realize that there's millions of new jobs posted every single day on the job board and finding the top 10 related jobs for every single job posted each day could be extremely inefficient the question is explain a system or a method that could solve the problem of finding the top 10 closest related jobs for millions of new jobs posted every single day"
  candidate_answer: time=03:03 text="10 jobs okay yeah that's a great question and i think a very applied question um that many job boards could benefit from uh before i dive into the answers and kind of how i would attempt this one question i had is this particular question talks about retrieval of top 10 jobs from the jobs that were posted on that particular day could the jobs which have been posted in the past are they out of the table like are we not considering the jobs that have already been posted and it's only advertising the new jobs that have been posted today or are we also open to some previous jobs that might have already been posted why i ask is because um some of the jobs that have been posted in the past um it would have been time for a lot of the other users to interact with those jobs as well which kind of gives us crucial information and patterns to mine as compared to some jobs which have been only posted today because if we are trying to find jobs which have been only posted today we lose out on any sort of user and item interactions because probably not a lot of people have interacted so the only way you could go about retrieving new jobs is through these embeddings and finding some closest some vector similarities and all that so okay uh using your info of uh using a heuristic of the last one month um we have to find um the related jobs uh that would be there so let me try to approach it with is it okay to share a whiteboard and how i'm envisioning is is i'll try to because i think it is also important to see whether the company or the particular job board who has this project has the functionalities and capabilities to attempt this problem in the way that i'm doing right now so if any point of time you feel that oh maybe they do not have data like this or maybe this is not what they can do with the current resources just let me know and we can probably go down some other path but i'm assuming that at least what they have information on is the users are over here and the particular jobs are over here so this is just a matrix of a user and a particular job uh right so maybe we have user number one user number two up to a lot of other users here we have job id number one job id number two till job id number hundred and i'll i'll tell you a bit about why i'm going this route because um you had the question mentions that um that there are nlp concepts such as bag of words or uh word embeddings um i was just wondering is there any um like these are the methods that have been tried and we want to look at something new or using those nlp concepts is also fair game okay um i think those are just kind of examples of birds code science somewhere they're all things that are okay sure so this what uh i'm talking that the algorithm that i'm talking about right now is just the classic collaborative filtering the matrix factorization algorithm so um let's just assume and you can tell me if they have data like this or not let's just consider one particular user we would have information on uh let's say whether this user applied to job number one uh maybe he did not apply to job number two maybe he did not apply to job number three he applied to something over here uh and likewise so would it be a fair assumption to assume that they might have information like this because we always have to think about what who are the target population that we are trying to propagate or advertise so this particular explanation will only aim for jobs uh let's say which have been there maybe we can put a heuristic like all the jobs which have had at least one interaction something like that so so maybe this is all the jobs which at least have one interaction uh in them and perhaps uh we can discuss how to tackle the latest jobs because uh they would not fit in this same matrix factorization way we would have to look at just some brute force nlp stuff for that but um this would give us like a nice way to attempt at jobs which have already been there so um what i'm thinking about this is there are uh so let's say this particular user has already applied to job 1 has already applied to job 70 there are a lot of missing spaces over here right we neither have zeros over there because zero would mean that he did not apply this is an example of explicit feedback where we only know the positive occurrences between the user and the item we never know which job he did not apply to because maybe he was interested and he was just not aware that such a job is there and that's the beauty of recommendations so the goal here if i were to explain it simply if we could come up with such an algorithm that helps us fill these empty spaces with a probability like maybe 0.8 or 0.9 then we would have a clear-cut probabilistic interpretation that okay if we recommend job number 68 to user number one uh perhaps he would like it ninety percent of the time um or his liking his affinity to this particular job is 90 and i agree the goal is not to target a user but to target a particular job and retrieve similar items to that particular job which i will get to once i talk about the algorithm but these kind of algorithms helps us address two major holy grails and recommendation retrieving similar items to the product but if you want to do some more targeted search right because whenever someone pulls up a particular job we know who that person is we know who what job that is so we could attempt it from either way from a user perspective or from an item perspective so i think how this problem is framed is from an item perspective but we can also attempt it from the user perspective and the interpretation of that would be if you give recommendations to the user which is tailored to him that would be a more personalized recommendation okay so do you have any questions any other directions you would want me to address else we can i can start talking about the algorithm a little bit from high perspective"
  reference_answer: time=None text=None
  interviewer_feedback: time=03:51 text="yeah let's say um that for every single job we want to be able to consider all the jobs that have been posted in the past like month okay so we'll use like the past month as like a heuristic as it being active uh basically any kind of active job okay any kind of active jobs yes why i yeah kind of just draw some stuff yeah okay so yeah yeah using any nlp concepts are fair game yeah yeah so i guess to get the information to this yeah you're right so they would definitely have this information because it's the activity right but they'd only have for all the previous jobs but not yes they yeah yeah they would only have it for the previous jobs like the last uh 30 days and"
  question_topic: ML

--- CHAPTER `02:20` — Interview question ---
window: 02:20 .. 15:00
recognition_status: multiple (3 items)

ITEM #3
  interviewer_question: time=11:20 text='yeah so i guess to summarize if i understand it correctly like if we can apply these um measured characteristics we can get more features for the jobs and then user characteristics as well exactly how does that i guess then apply back to kind of the related jobs problem'
  candidate_answer: time=11:38 text="related jobs problem yeah exactly and i'll get to that i'm trying to see how um i can clear this let me see so let me rephrase your question uh you mentioned how will we use this algorithm to make the recommendations or finding the jobs for the relevant job so let's try to get at that so the the goal for us is we have a big matrix let's say let's call the dimension over here users so let's say there are m number of users and there are n number of items so the dimensionality of the matrix is m by n so the matrix factorization what it does is it comes up with two matrices which are of the dimension m by f and it also comes up with another matrix which has dimensions f by n so when you take a matrix multiplication of both of them you come back to the original dimensions which is m by n so once you find these lower so these are also matrix decomposition because what we are trying to do is we are trying to find two other matrices so this matrix is known as the user feature matrix and this matrix is known as the item feature matrix okay right so you can see that the dimensions match basically if i were to explain it simply what we have done in this process this is still high level is we are basically telling the algorithm that we think a user as well as an item can be expressed by a f dimensional vector so this algorithm automatically calculates these features uh obviously there is some loss function there is some sort of a stochastic gradient descent or any other optimization happening but this is the crux of the algorithm to understand the beauty in this algorithm that just realized that the only thing we had going in was just the interaction let's say if you and i were the only two users we literally only need to know what are the jobs you and i applied to that's it and this algorithm helps you create these abstract features for you and me which motivates so many downstream algorithms and that is why i like this because we started with nothing now we know a lot about me we know a lot about all the jobs that are there and now literally sky is the limit if we want to find similar users we can find similar users if we want to find similar jobs we can find similar jobs um so that's like the high level of this particular algorithm yeah so"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #4
  interviewer_question: time=14:42 text='how uh what what would you like me to talk about how the training happens or uh should we base the execution from this high level perspective how would you like to proceed uh with the discussion'
  candidate_answer: time=None text=None
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #5
  interviewer_question: time=14:57 text="i guess i'd be interested to figure out exactly what the i guess practical aspects are right because we dived into how the algorithm is going to work right it's major perfection we're taking activity from like the users and activity from the job or not the activity the users activity of the users on the job on the jobs right right and then um creating this uh now and dimensional by end yeah right training set and so how do we use that on like let's say a new job that comes in"
  candidate_answer: time=15:31 text="exactly yeah so going back to our earlier discussion we are only talking about the active job so far and the heuristic filter we put on this was all the jobs which have had at least one interaction and coupling this with the heuristic you told me last one month so the filters or the the filter on the sequel is like last one month at least one job so after you run this algorithm for the sake of simplicity and explanation let's just consider we have 10 jobs to offer or or let's just consider we have two jobs to offer right um let's actually make it till 10 so we can motivate the example of retrieving after you are done running this algorithm all of these jobs will have a feature so this is a vector that i'm making over here and these have numbers filled in these are abstract features which have been uh extracted they don't have any um like artistic meaning like age or gender these are just abstract features which we can think of as a secret in coding for that job job number two will also have a secret encoding like that and job number 10 will also have a secret encoding like that so this is actually not very different from how the embeddings work in deep learning but the good thing about this algorithm is if you know a lot of the deep learning does not have analytical solutions it's stochastic gradient descent you have to make a bunch of passes through the data you have to make some epochs over the data but for matrix factorization there are some analytical solutions uh like basically matrix formulas which you can just use and iterate over very few times in order to find all of these features so just reiterating all of these features are what matrix decomposition gives us and we can call them item site features which basically means some sort of abstract representation of my jobs okay once we have all of these abstract representations a very nice thing to do would be to look at a correlation matrix right uh like what are the top 10 most similar jobs to item number to job posting number one or job posting number two or job posting number three which actually is a challenge because you mentioned um there are millions of job that are posted so i'm assuming even with those filters we will have quite a sizable number of jobs and doing those similarity calculations is not trivial right because let's say we have a million jobs the matrix would be 1 million by 1 million which is a huge matrix and it wouldn't be a very sparse matrix which would take memory to store memory to look up memory to calculate causing downstream issues in latency and what not so i have an ad hoc solution for this um ideally we would want to go the route of not maybe doing ad hoc approaches but since there is a particular business requirement we we have to sort of find some hacks around this so how about this uh how about we take the idea of unsupervised algorithm to maybe make our lives a little bit easier and alleviate some of this problem there are always some assumptions to modeling that we have to take so if this assumption is tenable maybe we can go through with this process if not we will brainstorm something else so i am assuming this job board let's say if this is indeed or linkedin and let's say we or you or i pull up one particular job description of a data scientist right so there is an upper limit on the corpus of jobs which might be potential jobs for this because let's say a data scientist you might not want to recommend something for a mechanical engineer in that right or maybe for electrical engineer the class of jobs is very let's just say finite but obviously if we try to attempt it the manual way it might be a lot of problem because there can be so many features what do we stratify on what sort of hierarchical rules or manual rules we make is difficult how about this let's say if you remember we had n jobs so we had n jobs and we had f features on those jobs and these features have been extracted from this so over here it is one two three four so for example over here f is equal to four so now we have embedded every single job into a four dimensional vector right gotcha how about we just resort to some clustering algorithms like k means a very simple algorithm to cluster these jobs right maybe we will find that and we can look at things such as the very famous cree plots and what not uh which basically explain um some sort of measure of how good the clustering is so so over here we have the number of clusters and over here we have some particular metric i wouldn't pretend if i exactly know what that metric is over here but it basically uh tries to check let's just put it simply how good the k-mean is for this particular value of k so i think that is some measure of um how much is the variation explained between the clusters and within the cluster so something related to that but some measure of efficacy so let's say if we found that um there are five clusters in total right so uh now coming back to the problem if someone tells us hey wait can you recommend some similar jobs for job id number one we first map it back to the particular cluster so let's say this is in cluster number three then we have automatically uh discounted four of the other clusters right so that helps us in alleviating this problem of retrieval i'm not saying that this is a foolproof way obviously we would lose out on some good potential jobs that are there in some of the other clusters but if the business comes to us with a requirement we have to find some way of doing it and this is uh like my way of doing it so then it is pretty simple let's say uh we find job id one belongs to cluster number three and then we do the same kind of vector similarity for only the jobs that are there in the cluster number three uh not in all the other clusters so that's how um you could look at things like just the cosine scores um retrieve the top 10 ones but i am assuming the level of simplification that will be there with this approach is a direct artifact of how many inherent clusters are there in my job types if there are more number of clusters which will be automatically found out by some of these creep plots for k means then the level of simplification we do is is pretty significant if there are 10 number of clusters then we have improved our finding algorithm to the order of 10 which i think is a significant improvement so in order to summarize my approach the question you posed was we are a job board and we have to retrieve some similar jobs to a particular job and obviously there are many jobs so we do not want to just resort to the brute force way of looking at the similarities and my approach to this was let's just first look at only the occurrence data because uh one thing i have a lot of um disagreement on in our data science work is there is hardly i mean this might happen but i haven't seen it in my experience people directly jump to very complex solutions like okay we have nlp let's look at the data throw in a bunch of nlp text mining stuff but there is really no simple baseline to do that so how would we ever know how significant of an improvement do we have over a simple technique if a simple technique does the job then by ocam's razor we should be going with the simple stuff because it's easier to maintain deploy enhance so the idea i told was we will just take the user item matrix apply algorithms such as matrix factorization to extract abstract features on items which are the jobs and users as well then we still haven't solved the problem of retrieval we have only solved the problem of automatic feature generation so we will use that to cluster and when someone asks us to recommend a new job we will just find which particular cluster that job belongs to and then just make a vector similarity matrix for that particular job and sort by the cosine similarity so that's sort of my approach i'd be happy to discuss more ideas even news or any other questions you have"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `15:00` — Practical application ---
window: 15:00 .. 25:00
recognition_status: single (1 items)

ITEM #6
  interviewer_question: time=24:54 text="no that sounds good so i guess my next question is more on the practical deployment side right um so you know we're let's say we attempt this right solution we get these jobs back we get like 10 jobs for every new job that gets posted everything looks good but how do we know if it's working well right how do we know how do we measure the efficacy of our like strategy right um are we testing this offline beforehand or are we like just rolling this out in production"
  candidate_answer: time=25:31 text="yeah that's a that's a great question because i think that's how we tie up the computer sciencey machine learning and deep learning with deriving some strategic insights with the use of a b testing before we push these changes out so and the reason to that is actually very fundamental let's discuss some very common metrics right let's just say root mean square error or average accuracy sure we when we are doing the local development testing out a bunch of models what is our approach we say okay i will test logistic regression i'll just random forest and whichever gives me the higher average accuracy is my model of choice right but the fundamental question we haven't addressed with this is is there a one-to-one correspondence between the average accuracy and how the end user will perceive it it's an open-ended question i mean sure but the problem is the observational data that we had collected was not collected in a controlled setting so making this sort of causal uh inferences can be a little bit of a slippery slope so coming back to the question of how would we know it is working so first of all uh we would have to discuss that there are two ways of knowing it is working or not one is the local metrics like the average accuracies or in this case accuracy does not make sense because why i say that is let's say we recommended job number one we recommended job number two and we recommended job number 10 to a particular user uh taking the average accuracy or basically saying okay how many of the 10 jobs did the user actually take is a bad metric because our metric should have some sort of ranking intuition in that because we should really give the mistake at the first position a higher penalty because let's say if i'm recommending you a movie at the very first position i better be sure about it because otherwise it translates to bad user experience so there are many ranking metrics that we have to look at which metric it's not important what is important is understanding this concept that if you are making recommendations usual metrics are not good we should look at some sort of a ranking metric so in order to do the local development you know find the better algorithm obviously matrix vectorization has a bunch of different hyper parameters k means we can do this sort of local development in order to basically come up with our best short algorithm and streamline process but we should also try to at least attempt to see how the end user will perceive recommendations from this right so i mean i'm assuming since the job board already is doing that there would be let's say the current standard of doing that recommendations right be it just be uh some sort of a very simple way of retrieval or any other way of retrieval uh we can take that uh what we can do is we at this point of time we have to talk to the company we have to talk to them hey are you guys allowing me to maybe do a very small randomized study where i will put some groups in the control group all of them will see recommendations from your current state of the art or whatever you are using and let's do the second group show recommendations from this modified approach of matrix factorization plus clustering followed by retrieval and then let's just basically use statistics to make some inferences right that would be getting into the inferential territory so we have to ask them can we do things like that do you have um the facilities do you have the budget do you have the patience and more so do you have the the interest to do that um then that's the gold standard um if we can do an experiment there is nothing better than that however if we are not able to do that we can also do something known as a causal analysis which is our best shot at recreating an experiment with the current data that is there so at this point of time uh in order to see if this thing is actually working um there are two ways one is from the modeling aspect one is from the end user consumption aspect and the second i would say is more important so i would ask the company can we do a small randomized study if they say yes that's the best thing um the inferences from there are very solid and have a sound theoretical underpinning if not we can go at some more ad hoc ways but obviously any sort of qualitative statement i make over there would have to be taken with a grain of salt because we have not randomized the groups um in a controlled fashion we are only trying to recreate it so that would be my uh two approaches and uh happy to discuss if we want to drill down on either of those"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Experimentation

--- CHAPTER `25:00` — Deployment ---
window: 25:00 .. конец
recognition_status: multiple (2 items)

ITEM #7
  interviewer_question: time=30:47 text="i guess my last one would be what if that this is a because this is a new feature that's not launched yet let's say that we want to build this new feature okay and there's no like prior matching algorithm there's no prior related jobs what do we compare it to now to actually set a standard for success"
  candidate_answer: time=31:07 text="um okay so do you mean that this feature is not directly there as in in the sense that the company is not doing this kind of thing like they are not retrieving the top 10 jobs and this is the very first time something like this would be attempted then they want to build this feature for the first time yeah for sure um i mean um yeah so that kind of limits our options but not our motivations and excitement to do this in that case we can at least do our due diligence to do a best local validation that is having a sound validation set and a test set and finding our best set of hyper parameters and all that so that is only for the modeling aspect if if the company is still interested in knowing how the end user will perceive it that becomes a little bit tricky because we do not have current standards to compare it to to say that okay this would be an improvement uh but how i would attempt that is through an iterative process so what i would tell them is obviously uh you want to implement this feature so you guys do realize there is some definite utility and roi that you might derive from such a feature so how about we do this uh we come up with let's just put this box this box is everything we have done so far any type of model any type of retrieval any type of clustering uh obviously at time step zero they do not have any product so this decision can be boiled down to a binary decision and i will tell you my opinion on this and you can also tell rolling it out to the 100 audience is never a good strategy because we do not have ways to scale it back we do not have ways to stop the experiment if we notice negative effects so how about we start with some gradual stuff let's just first show it to five percent or 10 of the users uh at this point of time i don't think we would be able to compare it with any other state of the art because there is not one at the moment but we can get a good enough sense of okay is it too bad is it not that bad is it working by just looking at some descriptive statistics right at this point of time more so we are just making sure that we have some sort of sanity check and um so we roll it out at p0 we show it to five percent if things look good we take it to ten percent twenty percent thirty percent um and at that point of time we would start to gain some data in an intelligent fashion of how the end user is perceiving it because um if you take a good sampling of the users we do not need to show it to everyone right the the analogy to that is if we are sick and we go for a blood draw they do not take our whole blood uh to check if we have an issue or not they just take a good enough sample and then from there they are able to tell a lot of very important stuff and provided we are doing this initially making sure this is working at time step one now we have a current state of the art or let's just say current state of execution whatever we have right now so from the second iteration we can start to do an a b testing as well here is what i have so far and now we can start to improve and throw in some baseline approaches throw in some modified approaches and really proceed in a data driven way we do not go in with any sort of philosophy or any sort of um biases that we might have of what we think it works it would be a very data vetted way we will only proceed if the data tells us to proceed if not we will all collaborate together to think of how we might address this issue so in order to summarize uh how we will know if it actually works if the company does not have the product we will come up with our best uh approach and at time zero we will start to show it to five percent ten percent if things look good you'll gradually scale it up once we have made the advent or the start or initiation of this method from the second iteration on we can resort to small scale a b testing in order to make very strong inferences on whether this approach is good and a b testing can also help shed light on a lot of the key processes right i think of this as a giant car and doing the a b testing can tell us whether the problem is in the engine whether the problem is in the wheels whether the problem is in the transmission so it actually gives us really good ways to diagnose what might not be going right and in doing that sort of diagnosis we are not resorting to any bias of the data scientist or any preconceived notions we are asking the data to guide us in this journey of continuous improvement so that the company benefits from this sort of rnd any sort of r d that we do which does not have tie ups with how might we use that institutional memory and information would not be a good research and development so this provides a seamless strategy"
  reference_answer: time=None text=None
  interviewer_feedback: time=31:25 text="is it like that yeah like that so it's like this is the first time they're trying it"
  question_topic: Experimentation

ITEM #8
  interviewer_question: time=37:04 text='yeah uh we could try like running some random seed algorithms right so you could cheat it with like oh wow completely random jobs yeah and then see if it actually performs better'
  candidate_answer: time=37:33 text="if so that would actually give us ways to do this sort of a b testing right from the onset yeah we would just say okay let's first at least try to prove that what our data scientist came up with is better than random because if it is not then we have some real issues over here so let's say at the first iteration we use your idea to have one group who sees random seed recommendations another group which sees our recommendations then at least we have a winner at the first stage so now we just proceed in this round robin format whoever wins in the previous iteration goes into the next stage of development and now we have it compete with another variant of the algorithm i think that's a great strategy which actually decreases this development duration by however much the gap between p0 and t1 is so yeah i really like that idea as well that's good yeah always having a baseline against something is good especially as the model probably continuously retrains right for sure"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Experimentation

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/interview-query/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22/ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
