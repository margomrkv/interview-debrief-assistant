<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18",
  "transcript_folder": "transcripts/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18",
  "source_id": "ml_engineer_senior_meta_illegal_items_interview_query_2022_01_18",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:18:04 +0200",
  "updated_at": "2026-05-20 21:32:30 +0200",
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
    "json": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/timecodes.txt",
        "en",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.pipeline-log.md"
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
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:32:29 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:32:30 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18`
- **Source ID:** `ml_engineer_senior_meta_illegal_items_interview_query_2022_01_18`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:18:04 +0200
- **Last updated:** 2026-05-20 21:32:30 +0200

Фильтр в IDE: `*ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/timecodes.txt`<br>`en`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.pipeline-log.md` | — | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.validation-report.md` | 1.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.pipeline-log.md`

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
SOURCE_ID: ml_engineer_senior_meta_illegal_items_interview_query_2022_01_18
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18
INTERVIEW_LANGUAGE: en
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00] let's say that you are designing a
[00:01] marketplace for your website selling
[00:03] firearms is prohibited by your website's
[00:05] terms of service agreement not to
[00:07] mention the laws of your country to this
[00:09] end you want to create a system that can
[00:11] automatically detect if a listing on the
[00:12] marketplace is selling a gun how would
[00:14] you go about doing this yeah it's a
[00:16] interesting question i'm curious about a
[00:18] few things here first i guess one thing
[00:20] i'm wondering about is like how if i was
[00:21] given this task like how is this working
[00:23] in kind of production you know the task
[00:25] is to automatically identify the
[00:27] listings what happens with those
[00:28] identifications do they go to a human
[00:30] who checks it or is it like immediately
[00:33] changes the website yeah so let's say
[00:35] that the current setup is that it's all
[00:37] crowd source so let's say we have a flag
[00:40] and then a user can flag the listing if
[00:43] they see it's a gun or maybe someone who
[00:46] works in terms of like moderating the
[00:48] marketplace can also flag it and then
[00:50] it'll go to another internal let's say
[00:52] someone who works in customer support
[00:54] that can then remove the listing if they
[00:56] determine it as a gun and that's the
[00:57] only thing that kind of happens right
[00:58] now okay and then how would this fit in
[01:00] is the end of the line always going to
[01:02] be customer service or how would this
[01:04] fit in that pipeline you think so i
[01:05] guess reframe the question back to you
[01:07] but let's say that
[01:09] this is the current system right and i
[01:12] guess given the kind of context would
[01:15] you think that the goal is to first
[01:18] disable it when they're posting do you
[01:20] think we should be like detecting it
[01:22] afterwards after a few days and then
[01:24] sending it to customer support what part
[01:26] do you think
[01:27] yeah so i guess yeah the reason i was
[01:29] asking that question i guess i could
[01:30] have said that too because if if
[01:32] customer service is is going to look at
[01:35] it afterwards which i think would
[01:37] probably be the better way to go to
[01:39] start but if they're doing it that way
[01:41] then that means that i really need to do
[01:43] a very good job of detecting all the
[01:45] possible firearm listings it's bad if i
[01:48] miss something that is a firearm but i
[01:51] miss it because at the end the customer
[01:53] service is going to look at it and so
[01:55] i'm assuming it'll be okay it might cost
[01:57] some money but it's probably going to be
[01:59] okay if i give it false positives like
[02:01] listings that aren't guns and then let
[02:03] the customer service deal with it but it
[02:05] seems like this pipeline would be very
[02:08] costly
[02:09] in that in the sense that you're maybe
[02:11] breaking laws of your country or your
[02:13] terms of service if you totally miss the
[02:15] listing and you have this uh false
[02:17] negative right yes so that's that's yeah
[02:20] so that's how i would think about it so
[02:23] i guess given the costs do you think we
[02:26] would then err on the side of reducing
[02:29] the number of false negatives or false
[02:31] positives in this case so my initial
[02:33] point was about false negatives because
[02:36] we want the customer service to get
[02:38] everything that's pertinent and they can
[02:39] decide because they won't see anything
[02:42] that's not been flagged or not been
[02:44] identified so but if costs are a concern
[02:47] then yeah we would be concerned with the
[02:50] false positives
[02:51] because that would mean that the
[02:53] customer service gets extra ones that
[02:55] are not really relevant at all they're
[02:57] adding to their workload okay so let's
[02:59] like maybe think about an assumption of
[03:01] what is okay in terms of how the process
[03:04] might go and maybe this could be an
[03:06] example so you know in my mind i think
[03:08] like if we let's say someone posts a gun
[03:11] it gets put onto marketplace it gets
[03:13] removed within one hour that's probably
[03:15] good probably not a lot of time for
[03:17] someone to go out reach out message try
[03:19] to get that gun from the seller in that
[03:22] scenario maybe a bad case scenario is
[03:24] that we get overloaded with a bunch of
[03:27] other items that are trying to be sold
[03:28] that are not guns and then you know they
[03:31] get the typical your posting was flagged
[03:33] until it's reviewed by customer service
[03:35] therefore you know reducing kind of
[03:36] liquidity in this marketplace as well
[03:38] all of a sudden you know sellers are
[03:40] like oh like this marketplace sucks like
[03:42] i can't even list you know my plants on
[03:44] here or else they get flagged right and
[03:46] then therefore kind of reducing that
[03:48] when we're thinking about the different
[03:49] scenarios here what is it kind of like
[03:51] the optimal one you kind of have an idea
[03:54] of what you think is kind of best case
[03:56] scenario here for both parties bringing
[03:58] it back if you're facebook what would
[04:00] you think facebook would want to do in
[04:02] this scenario it does depend on what
[04:03] happens with the the model at the end so
[04:06] there are different scenarios we've laid
[04:08] out so if one of the scenarios is the
[04:10] one i was talking about which is that
[04:11] you don't want to miss anything that
[04:13] case false negatives are important in
[04:15] other cases like you're mentioning which
[04:17] is if if it ends up being a sticker
[04:19] that's posted because my the model
[04:20] identifies it but it's not there and
[04:22] then it can lead to a lot of issues so
[04:25] that's the the false positive case what
[04:27] we'll want to be concerned with then in
[04:29] our model so i guess if we're concerned
[04:31] with both those scenarios then we want
[04:32] to minimize both false positives and
[04:34] false negatives
[04:35] and so we can use metrics like f1 score
[04:38] to to sort of minimize that i guess
[04:40] another thing that's related to this of
[04:42] why we might choose something like an f1
[04:44] score which is basically a combination
[04:46] of precision and recall and precision is
[04:50] where you're really concerned with you
[04:52] make a bunch of predictions and how many
[04:54] of them are right the recall is the case
[04:56] where you make a bunch of predictions
[04:58] how many of the real case scenarios do
[05:00] you get so how much stuff do you miss i
[05:02] guess recall is like what do you miss
[05:03] another reason to use these two measures
[05:05] and i think that seems pertinent here is
[05:07] because the number of guns are probably
[05:09] gonna be small right the i'm assuming
[05:11] the actual number of gun posts is
[05:12] probably very small maybe even less than
[05:14] one percent in like a facebook
[05:15] marketplace that sells all sorts of
[05:17] stuff it's an imbalance sample too those
[05:20] measures that i just mentioned are good
[05:21] for that because they they sort of
[05:23] ignore the fact of the true negative
[05:25] which is that the post isn't about guns
[05:27] and you get that right but there's so
[05:29] many of those so you want to ignore
[05:30] those so measures like precision and
[05:32] recall will ignore the thing that's very
[05:35] obvious and predominant which is the
[05:37] listing not having guns and focuses on
[05:39] just getting the positive case of
[05:41] getting the listing with guns the
[05:43] imbalance case will also maybe come into
[05:45] consideration for the models we choose
[05:47] so that seems good for the imbalance
[05:49] sample and i guess false positives and
[05:50] false negatives i think the other things
[05:52] i was thinking is that what sort of the
[05:54] scale and scope and the kind of data we
[05:56] might have because that'll pertain to
[05:58] how we can answer this question so i'm
[05:59] guessing maybe speed at least for
[06:02] training the model isn't a big issue and
[06:04] the importance is accuracy like we're
[06:06] very concerned with an accurate model
[06:08] yeah definitely
[06:09] and i'm guessing online you had
[06:11] mentioned like maybe it's okay i mean
[06:13] the model doesn't need to be that fast i
[06:14] guess right
[06:15] in terms of when it gets deployed and
[06:17] it's making predictions for each post
[06:20] yeah and then i guess in terms of the
[06:21] prior data so i guess we would have
[06:24] access in this case to other postings
[06:26] and where customer service has flag
[06:28] stuff so we have like a large data set
[06:30] where we know that there was a posting
[06:32] and we know whether it was of guns or
[06:34] not yes yeah i think we can identify if
[06:37] there were guns there's probably
[06:38] something where the actual value itself
[06:41] is flagged and then probably also a
[06:43] categorization of why it was flagged for
[06:45] and for this scenario we could say that
[06:48] confidently probably customer service is
[06:49] labeling them as guns or firearms in
[06:52] that category okay yeah so we're we can
[06:54] select those flags that are for guns and
[06:56] farms okay it seems kind of
[06:58] straightforward then so the idea is that
[07:01] you know we really want to identify
[07:02] these gun postings part of it might be
[07:04] related to the law part of it also might
[07:07] be related to you know people don't want
[07:09] to see these gun postings and and they
[07:11] also don't want to be necessarily
[07:12] wrongly flagged for the guns postings so
[07:14] it's very important to have a very
[07:16] accurate model at identifying these very
[07:18] small cases of gun postings and we don't
[07:22] seem to have as many concerns about
[07:23] model training time or anything like
[07:25] that we're really concerned with
[07:26] accuracy with that in mind with the fact
[07:29] that we already have this data i'm
[07:31] guessing our data set is fairly large
[07:34] maybe there's some things we might want
[07:35] to do with augmenting the data which i
[07:37] think so if i think about data
[07:38] collection and then i can think about
[07:40] features and then think about the model
[07:41] so if now i think about the features
[07:43] that i have
[07:44] i have flags that might have been given
[07:46] by users so i have that as a feature i
[07:48] might have the particular user who
[07:50] posted it their demographic information
[07:52] location information so maybe you know
[07:54] parts of the country have more guns
[07:56] being sold or not there might be other
[07:58] contextual information i don't know why
[08:00] this might be but maybe early in the
[08:01] morning people like to post their gun
[08:03] sales
[08:05] and then i think what's critical for me
[08:07] here is the text as a feature the body
[08:10] of the text itself i guess another
[08:12] feature could be the maybe they post
[08:13] some images but i'm thinking maybe for
[08:15] now just to focus the model a little bit
[08:17] i can i might ignore the images part
[08:19] just for now but i think when i talk
[08:21] about the text a lot of what i'll say
[08:23] can apply to the images and i think the
[08:25] the big part here to me it seems like
[08:26] the text in that data and being able to
[08:28] leverage that information to get you
[08:31] know keywords or to get patterns of
[08:33] words yeah so so you might have that you
[08:35] might have other data to like the length
[08:36] of the text or something like that so we
[08:38] have those features user data flags
[08:41] context information the text so now i
[08:43] want to focus a little bit on on the
[08:44] text itself and what we can do with it
[08:47] to use for our model i think just to
[08:49] start i mean i often feel this way when
[08:51] dealing with text data you want to start
[08:52] with a simpler model i suppose and so
[08:54] the simpler model might be something
[08:55] like a bag of words one also reason to
[08:57] start with that is that you can get a
[08:59] nice baseline and i guess a related
[09:01] question here i i meant to ask this
[09:02] earlier was that you know we do we have
[09:05] other baselines like i guess we have
[09:07] previous performance of how the user
[09:09] flags worked or
[09:10] so we have some other data in the past
[09:12] yeah yeah let's assume that yeah we have
[09:14] all this data that facebook itself has
[09:16] yeah so we have some baseline data of
[09:18] how their current process is working and
[09:20] then i'm suggesting we can have this
[09:21] other baseline where we just we use the
[09:23] simplest approach for text analysis
[09:26] even though i did mention we did talk
[09:27] about this that there is a lot of time
[09:29] so technically we could use more
[09:30] complicated models like attention-based
[09:32] transformers that take contextual
[09:33] information into account but for now
[09:35] i'll just focus on the simpler model and
[09:37] and talk through with that maybe we can
[09:38] talk at the end of the value of these
[09:40] more uh sophisticated approaches so i
[09:42] guess if we have the text data then you
[09:44] know we want to we can extract the bag
[09:46] of words which just means that we get
[09:48] for each body of text we get the unique
[09:50] words in the text and the counts of
[09:52] those words we have like i don't know
[09:54] how many millions of posts so we have
[09:55] this for each post we have these bag of
[09:58] words the other thing we can do is an
[10:00] approach called the tfidf where we scale
[10:04] the value of each word based on its
[10:06] frequency in different postings and the
[10:08] reason this can be valuable is that you
[10:10] might expect that postings about guns
[10:12] for instance tend to use specific words
[10:14] not found in other postings you know
[10:16] before even running the model i might be
[10:18] helping my model by selecting words that
[10:20] are unique to particular listings and so
[10:23] this will up weight those words that
[10:25] tend to be very specific to specific
[10:28] listings because the bag of words can be
[10:30] like millions and millions of words so
[10:31] it's a huge sparse matrix so sometimes
[10:33] you might want to do additional
[10:34] reductions so you might do something
[10:36] like a pca to reduce that to something
[10:38] like 500 dimensions the point of all
[10:40] this process is is that you're taking
[10:41] the text and you're putting it into some
[10:43] embedding space and the value of the
[10:45] embedding space is it's almost like what
[10:47] you're doing is you're putting each
[10:48] listing you're plotting it in space and
[10:50] the idea is that you want to plot points
[10:52] in space that mean similar things this
[10:54] processing technique should before we
[10:56] even build our model should place each
[10:59] listing next to each other that mean the
[11:01] same thing that's the sort of idea of
[11:03] this process and since we know that idea
[11:05] we can always substitute it with other
[11:07] methods that are more sophisticated if
[11:09] we want
[11:10] that sort of like how we get the
[11:11] features
[11:12] so now i guess we want to think a bit
[11:14] about the model that we want to build
[11:16] because we have the imbalance sample i
[11:18] would think maybe the model to start
[11:20] with at least we can again iterate as we
[11:22] go but for our first prototype maybe we
[11:24] could start with a tree based model
[11:26] particularly something like a gradient
[11:27] boosted tree because what's nice about
[11:29] these models is that you have each tree
[11:31] that makes a prediction so in this case
[11:34] it's taking all our features and
[11:35] predicting whether it's a gun posting or
[11:38] not a gun posting and then it takes the
[11:41] points the data points that have the
[11:43] most error and it scales them so it up
[11:45] weights those data points that were in
[11:48] error for the next tree what this
[11:50] effectively will do is it'll upweight
[11:52] the sort of minority sample points those
[11:54] listings that are for guns are very few
[11:57] and so they'll if they keep causing an
[11:59] error in the model their weight will
[12:01] keep going up and they'll be more and
[12:02] more important in making the prediction
[12:04] that's maybe why a gradient booster tree
[12:06] would be good to start with yeah the
[12:08] only one issue could be if you want
[12:09] online training and so maybe if there's
[12:11] an issue of online training the gradient
[12:13] boosted trees may not be optimal for it
[12:15] and so we could try other models if we
[12:17] wanted and the difference between online
[12:19] and offline training is that online
[12:21] training happens while the model is
[12:23] deployed and does continual improvement
[12:26] is that right yeah yeah exactly but i'm
[12:28] guessing in this case what we probably
[12:30] would want to do is maybe every so often
[12:32] we update the model in which case the
[12:34] usually the gradient boosted trees are
[12:35] pretty quick to train and they're fast
[12:37] at also delivering the predictions at
[12:39] inference time so we could just retrain
[12:41] the whole model but say for whatever
[12:43] reason every time customer service
[12:45] answers that you want to update the
[12:46] model then this tree based approach
[12:48] depending on what package you use it
[12:49] it's not going to be very optimal so you
[12:51] might want to use other approaches like
[12:52] a neural network that could allow for
[12:55] this online training we talked a bit
[12:56] about like so we're building this model
[12:58] with the gradient boosted tree we talked
[13:00] earlier about we can't really use
[13:01] accuracy like just plain and simple
[13:03] accuracy because it's such a small
[13:06] sample that we have there's very few gun
[13:08] posts the one thing i could have
[13:09] mentioned earlier is one way to deal
[13:11] with that too is to balance the sample
[13:13] so if we have a lot of data we also
[13:14] could have evened out the the two
[13:16] samples so we could have taken how many
[13:18] gun postings we have and just gotten a
[13:21] matched sample of the equivalent other
[13:23] sample but say we're not doing that say
[13:26] there they're not enough gun postings to
[13:28] really have that match then accuracy
[13:30] won't be that great and what we'll want
[13:32] is like what we talked about is
[13:33] precision and recall are there other
[13:35] things to consider evaluating the model
[13:38] and maybe when we roll it out yeah like
[13:40] i said we can use precision and recall
[13:42] and we can combine them in this f1 score
[13:44] that just range between zero and one and
[13:46] that can tell us how well the model is
[13:49] performing at predicting those gun sales
[13:51] when we're building the model we we
[13:53] probably would be training i guess on
[13:55] our historic data we'd be taking some
[13:57] sample of data in time that's our
[13:59] training sample and then the test set is
[14:01] something later in time we should
[14:02] probably mimic how it's occurring in
[14:04] production where our model is trained
[14:06] with a given set of data in time and
[14:08] it's predicting new data in the future
[14:09] one thing we might want to consider is
[14:11] how long this prediction is good for how
[14:13] often we want to keep rebuilding this
[14:15] model because i guess as everything on
[14:17] the internet or the spam calls i get
[14:19] they get more and more creative at doing
[14:21] these things so yeah you know we might
[14:23] want to update the model uh to deal with
[14:25] these creativities that people have yeah
[14:28] and that's actually a good question
[14:29] because i think as people realize that
[14:31] their posts are being flagged we're
[14:33] dealing with very malicious actors that
[14:35] are active in their campaign to sell
[14:37] guns on the internet maybe one of the
[14:39] aspects is that they start creatively
[14:41] disguising their posts right and so that
[14:43] right the traditional nlp test of
[14:45] detecting bullets or guns for sale turns
[14:47] into like code names or something in
[14:49] which then we still have to then reuse
[14:51] that use of identifying manual tagging
[14:53] sorts so i guess one additional question
[14:55] i have is how do we know the performance
[14:57] edition of doing like more advanced
[14:59] approaches right and so let's say that
[15:01] we want to dive into computer vision i
[15:03] know you have a computer vision back
[15:05] under our and so like i guess like how
[15:07] would you assess the necessity of maybe
[15:10] using like images into your analysis
[15:12] versus just only using text and you know
[15:15] you know that image is probably harder
[15:16] to train there's probably a lot more
[15:18] difficulty with having expertise and
[15:20] images versus just text which has like
[15:23] great packages on python to use and so
[15:26] yeah how would you kind of like approach
[15:27] that situation how would you know that
[15:29] it's worth doing the image analysis into
[15:31] the features versus just going with a
[15:33] basic model yeah so i guess the question
[15:35] is like what's the added value of the
[15:37] images and is it worth bringing all that
[15:39] what whatever time it takes then exactly
[15:41] yes i think i mean a very simple
[15:44] approach that you could use that i like
[15:45] using is you just like sort of build the
[15:47] model you have all the features in there
[15:49] and then you get its prediction what the
[15:51] full model's prediction accuracy is so
[15:53] say for instance the full model is at 90
[15:57] seems really good and then you drop the
[15:59] images from the model and then you see
[16:02] you know when you remove the images what
[16:04] the value is and the accuracy and say
[16:07] it's 85 and then say you you do it again
[16:10] but you remove the text data and the
[16:12] text data when you remove it it's like 7
[16:13] 60 accuracy or something so so so yeah
[16:16] there you can know oh wow the text is
[16:18] very valuable but the images does drop
[16:21] it so you're like okay well you told me
[16:23] now when you drop the images the
[16:24] accuracy does drop but is that a
[16:26] meaningful drop so one thing i think you
[16:28] could do is just simulate like randomly
[16:30] sampling the data especially because we
[16:32] have enough data like i said here i
[16:34] guess in this facebook huge amount of
[16:35] data set so what you could do is
[16:36] randomly sample from the data and
[16:39] retrain the model each time and get this
[16:41] drop in accuracy when you remove the
[16:43] images and so say i guess i could say if
[16:45] 95 of the time the drop in accuracy is
[16:48] more than zero it's like it's like
[16:49] there's a negative drop so then i might
[16:52] say yeah images are important because
[16:54] almost all the time that i've tried it
[16:56] out in simulating across multiple
[16:58] samples there is that drop in accuracy
[17:00] gotcha okay cool yeah i mean that makes
[17:02] a lot of sense any additional kind of
[17:04] thoughts on this question oh i was going
[17:05] to say something about like if we could
[17:07] augment the data too for text data but
[17:09] some of those things are cool where you
[17:10] can use machine translation to change
[17:12] the specific text words but keep the
[17:15] meaning but i guess other things this
[17:18] model would be sort of a first step
[17:20] we're taking in all these features the
[17:22] user data the flags and the text we're
[17:24] making some predictions so i think the
[17:26] final thing would just be to check where
[17:28] the errors are happening and maybe use
[17:30] that to help with the model so one thing
[17:32] you might find is that say we flag toy
[17:35] guns all the time are being flagged yeah
[17:38] so one simple thing you could do with
[17:40] just the simple model where i use a bag
[17:42] of words is i could use like uh n-gram
[17:44] model so i could take every two words
[17:46] and and use the pairs of words and then
[17:48] in that case i would get toy gun and
[17:50] that way i could identify oh these
[17:52] things that are actually toy guns that
[17:54] are being wrongly flagged and i could
[17:55] solve that problem by just changing the
[17:57] model to include this local history um
[17:59] with pairs of words cool yeah that makes
[18:01] sense final question and this is kind of
[18:03] just more in relation to the question
[18:05] itself like what do you think about this
[18:07] question like how well do you think it
[18:08] assesses the candidate's performance
[18:10] just overall how do you feel your answer
[18:12] would kind of like fit in into like a
[18:13] broader facebook interview i mean i'm
[18:15] not sure about the broader facebook
[18:16] interview but
[18:18] i guess this i mean this question is
[18:19] pretty it seems very standard like it's
[18:21] very machine learning right you test
[18:23] your knowledge of minority like when you
[18:25] have very few things you're predicting
[18:27] you have to sort of build the model but
[18:29] you go from end to end and i think it's
[18:31] also to me seems like a fairly common
[18:33] problem you might face not this specific
[18:36] one but something like this where you
[18:37] know you need to identify something from
[18:39] a particular listing a particular post
[18:41] or or some you know in my case i deal
[18:43] with videos a lot and so it's it's like
[18:46] in line with i think what what you also
[18:48] might have to work on yeah what were
[18:49] your thoughts you have any yeah i mean i
[18:51] liked it a lot and i liked your answer
[18:52] and how you structured everything and i
[18:55] feel like that's a great approach for
[18:57] most machine learning type questions as
[18:59] well because i feel like most of them
[19:01] have a very defined beginning middle and
[19:04] end in terms of where's the data how do
[19:06] you build the model and then how would
[19:07] you deploy and evaluate it and i think
[19:10] focusing on those approaches is really
[19:12] key and so i think you did a great job
[19:13] there yeah good
[19:15] awesome

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
Write JSON only to: splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.json \
    --video transcripts/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.json --out splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.qa-split.json \
    --video transcripts/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.validation-report.md

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
video.md: transcripts/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/video.md

--- CHAPTER `00:00` — Meta illegal items ML mock interview ---
window: 00:00 .. конец
recognition_status: multiple (7 items)

ITEM #1
  interviewer_question: time=00:00 text="let's say that you are designing a marketplace for your website selling firearms is prohibited by your website's terms of service agreement not to mention the laws of your country to this end you want to create a system that can automatically detect if a listing on the marketplace is selling a gun how would you go about doing this"
  candidate_answer: time=00:14 text="yeah it's a interesting question i'm curious about a few things here first i guess one thing i'm wondering about is like how if i was given this task like how is this working in kind of production you know the task is to automatically identify the listings what happens with those identifications do they go to a human who checks it or is it like immediately changes the website okay and then how would this fit in is the end of the line always going to be customer service or how would this fit in that pipeline you think"
  reference_answer: time=None text=None
  interviewer_feedback: time=00:33 text="yeah so let's say that the current setup is that it's all crowd source so let's say we have a flag and then a user can flag the listing if they see it's a gun or maybe someone who works in terms of like moderating the marketplace can also flag it and then it'll go to another internal let's say someone who works in customer support that can then remove the listing if they determine it as a gun and that's the only thing that kind of happens right now"
  question_topic: ML

ITEM #2
  interviewer_question: time=01:05 text="so i guess reframe the question back to you but let's say that this is the current system right and i guess given the kind of context would you think that the goal is to first disable it when they're posting do you think we should be like detecting it afterwards after a few days and then sending it to customer support what part do you think"
  candidate_answer: time=01:27 text="yeah so i guess yeah the reason i was asking that question i guess i could have said that too because if if customer service is is going to look at it afterwards which i think would probably be the better way to go to start but if they're doing it that way then that means that i really need to do a very good job of detecting all the possible firearm listings it's bad if i miss something that is a firearm but i miss it because at the end the customer service is going to look at it and so i'm assuming it'll be okay it might cost some money but it's probably going to be okay if i give it false positives like listings that aren't guns and then let the customer service deal with it but it seems like this pipeline would be very costly in that in the sense that you're maybe breaking laws of your country or your terms of service if you totally miss the listing and you have this uh false negative right"
  reference_answer: time=None text=None
  interviewer_feedback: time=02:17 text="yes so that's that's yeah so that's how i would think about it"
  question_topic: ML

ITEM #3
  interviewer_question: time=02:23 text='so i guess given the costs do you think we would then err on the side of reducing the number of false negatives or false positives in this case'
  candidate_answer: time=02:31 text="so my initial point was about false negatives because we want the customer service to get everything that's pertinent and they can decide because they won't see anything that's not been flagged or not been identified so but if costs are a concern then yeah we would be concerned with the false positives because that would mean that the customer service gets extra ones that are not really relevant at all they're adding to their workload"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #4
  interviewer_question: time=02:59 text="okay so let's like maybe think about an assumption of what is okay in terms of how the process might go and maybe this could be an example so you know in my mind i think like if we let's say someone posts a gun it gets put onto marketplace it gets removed within one hour that's probably good probably not a lot of time for someone to go out reach out message try to get that gun from the seller in that scenario maybe a bad case scenario is that we get overloaded with a bunch of other items that are trying to be sold that are not guns and then you know they get the typical your posting was flagged until it's reviewed by customer service therefore you know reducing kind of liquidity in this marketplace as well all of a sudden you know sellers are like oh like this marketplace sucks like i can't even list you know my plants on here or else they get flagged right and then therefore kind of reducing that when we're thinking about the different scenarios here what is it kind of like the optimal one you kind of have an idea of what you think is kind of best case scenario here for both parties bringing it back if you're facebook what would you think facebook would want to do in this scenario"
  candidate_answer: time=04:02 text="it does depend on what happens with the the model at the end so there are different scenarios we've laid out so if one of the scenarios is the one i was talking about which is that you don't want to miss anything that case false negatives are important in other cases like you're mentioning which is if if it ends up being a sticker that's posted because my the model identifies it but it's not there and then it can lead to a lot of issues so that's the the false positive case what we'll want to be concerned with then in our model so i guess if we're concerned with both those scenarios then we want to minimize both false positives and false negatives and so we can use metrics like f1 score to to sort of minimize that i guess another thing that's related to this of why we might choose something like an f1 score which is basically a combination of precision and recall and precision is where you're really concerned with you make a bunch of predictions and how many of them are right the recall is the case where you make a bunch of predictions how many of the real case scenarios do you get so how much stuff do you miss i guess recall is like what do you miss another reason to use these two measures and i think that seems pertinent here is because the number of guns are probably gonna be small right the i'm assuming the actual number of gun posts is probably very small maybe even less than one percent in like a facebook marketplace that sells all sorts of stuff it's an imbalance sample too those measures that i just mentioned are good for that because they they sort of ignore the fact of the true negative which is that the post isn't about guns and you get that right but there's so many of those so you want to ignore those so measures like precision and recall will ignore the thing that's very obvious and predominant which is the listing not having guns and focuses on just getting the positive case of getting the listing with guns the imbalance case will also maybe come into consideration for the models we choose so that seems good for the imbalance sample and i guess false positives and false negatives i think the other things i was thinking is that what sort of the scale and scope and the kind of data we might have because that'll pertain to how we can answer this question so i'm guessing maybe speed at least for training the model isn't a big issue and the importance is accuracy like we're very concerned with an accurate model and i'm guessing online you had mentioned like maybe it's okay i mean the model doesn't need to be that fast i guess right in terms of when it gets deployed and it's making predictions for each post yeah and then i guess in terms of the prior data so i guess we would have access in this case to other postings and where customer service has flag stuff so we have like a large data set where we know that there was a posting and we know whether it was of guns or not yeah so we're we can select those flags that are for guns and farms okay it seems kind of straightforward then so the idea is that you know we really want to identify these gun postings part of it might be related to the law part of it also might be related to you know people don't want to see these gun postings and and they also don't want to be necessarily wrongly flagged for the guns postings so it's very important to have a very accurate model at identifying these very small cases of gun postings and we don't seem to have as many concerns about model training time or anything like that we're really concerned with accuracy with that in mind with the fact that we already have this data i'm guessing our data set is fairly large maybe there's some things we might want to do with augmenting the data which i think so if i think about data collection and then i can think about features and then think about the model so if now i think about the features that i have i have flags that might have been given by users so i have that as a feature i might have the particular user who posted it their demographic information location information so maybe you know parts of the country have more guns being sold or not there might be other contextual information i don't know why this might be but maybe early in the morning people like to post their gun sales and then i think what's critical for me here is the text as a feature the body of the text itself i guess another feature could be the maybe they post some images but i'm thinking maybe for now just to focus the model a little bit i can i might ignore the images part just for now but i think when i talk about the text a lot of what i'll say can apply to the images and i think the the big part here to me it seems like the text in that data and being able to leverage that information to get you know keywords or to get patterns of words yeah so so you might have that you might have other data to like the length of the text or something like that so we have those features user data flags context information the text so now i want to focus a little bit on on the text itself and what we can do with it to use for our model i think just to start i mean i often feel this way when dealing with text data you want to start with a simpler model i suppose and so the simpler model might be something like a bag of words one also reason to start with that is that you can get a nice baseline and i guess a related question here i i meant to ask this earlier was that you know we do we have other baselines like i guess we have previous performance of how the user flags worked or so we have some other data in the past so we have some baseline data of how their current process is working and then i'm suggesting we can have this other baseline where we just we use the simplest approach for text analysis even though i did mention we did talk about this that there is a lot of time so technically we could use more complicated models like attention-based transformers that take contextual information into account but for now i'll just focus on the simpler model and and talk through with that maybe we can talk at the end of the value of these more uh sophisticated approaches so i guess if we have the text data then you know we want to we can extract the bag of words which just means that we get for each body of text we get the unique words in the text and the counts of those words we have like i don't know how many millions of posts so we have this for each post we have these bag of words the other thing we can do is an approach called the tfidf where we scale the value of each word based on its frequency in different postings and the reason this can be valuable is that you might expect that postings about guns for instance tend to use specific words not found in other postings you know before even running the model i might be helping my model by selecting words that are unique to particular listings and so this will up weight those words that tend to be very specific to specific listings because the bag of words can be like millions and millions of words so it's a huge sparse matrix so sometimes you might want to do additional reductions so you might do something like a pca to reduce that to something like 500 dimensions the point of all this process is is that you're taking the text and you're putting it into some embedding space and the value of the embedding space is it's almost like what you're doing is you're putting each listing you're plotting it in space and the idea is that you want to plot points in space that mean similar things this processing technique should before we even build our model should place each listing next to each other that mean the same thing that's the sort of idea of this process and since we know that idea we can always substitute it with other methods that are more sophisticated if we want that sort of like how we get the features so now i guess we want to think a bit about the model that we want to build because we have the imbalance sample i would think maybe the model to start with at least we can again iterate as we go but for our first prototype maybe we could start with a tree based model particularly something like a gradient boosted tree because what's nice about these models is that you have each tree that makes a prediction so in this case it's taking all our features and predicting whether it's a gun posting or not a gun posting and then it takes the points the data points that have the most error and it scales them so it up weights those data points that were in error for the next tree what this effectively will do is it'll upweight the sort of minority sample points those listings that are for guns are very few and so they'll if they keep causing an error in the model their weight will keep going up and they'll be more and more important in making the prediction that's maybe why a gradient booster tree would be good to start with yeah the only one issue could be if you want online training and so maybe if there's an issue of online training the gradient boosted trees may not be optimal for it and so we could try other models if we wanted and the difference between online and offline training is that online training happens while the model is deployed and does continual improvement is that right but i'm guessing in this case what we probably would want to do is maybe every so often we update the model in which case the usually the gradient boosted trees are pretty quick to train and they're fast at also delivering the predictions at inference time so we could just retrain the whole model but say for whatever reason every time customer service answers that you want to update the model then this tree based approach depending on what package you use it it's not going to be very optimal so you might want to use other approaches like a neural network that could allow for this online training we talked a bit about like so we're building this model with the gradient boosted tree we talked earlier about we can't really use accuracy like just plain and simple accuracy because it's such a small sample that we have there's very few gun posts the one thing i could have mentioned earlier is one way to deal with that too is to balance the sample so if we have a lot of data we also could have evened out the the two samples so we could have taken how many gun postings we have and just gotten a matched sample of the equivalent other sample but say we're not doing that say there they're not enough gun postings to really have that match then accuracy won't be that great and what we'll want is like what we talked about is precision and recall are there other things to consider evaluating the model and maybe when we roll it out yeah like i said we can use precision and recall and we can combine them in this f1 score that just range between zero and one and that can tell us how well the model is performing at predicting those gun sales when we're building the model we we probably would be training i guess on our historic data we'd be taking some sample of data in time that's our training sample and then the test set is something later in time we should probably mimic how it's occurring in production where our model is trained with a given set of data in time and it's predicting new data in the future one thing we might want to consider is how long this prediction is good for how often we want to keep rebuilding this model because i guess as everything on the internet or the spam calls i get they get more and more creative at doing these things so yeah you know we might want to update the model uh to deal with these creativities that people have yeah and that's actually a good question because i think as people realize that their posts are being flagged we're dealing with very malicious actors that are active in their campaign to sell guns on the internet maybe one of the aspects is that they start creatively disguising their posts right and so that right the traditional nlp test of detecting bullets or guns for sale turns into like code names or something in which then we still have to then reuse that use of identifying manual tagging sorts"
  reference_answer: time=None text=None
  interviewer_feedback: time=06:09 text="yeah definitely yes yeah i think we can identify if there were guns there's probably something where the actual value itself is flagged and then probably also a categorization of why it was flagged for and for this scenario we could say that confidently probably customer service is labeling them as guns or firearms in that category okay yeah so we're we can select those flags that are for guns and farms yeah yeah let's assume that yeah we have all this data that facebook itself has yeah yeah exactly but i'm guessing in this case what we probably would want to do is maybe every so often we update the model"
  question_topic: ML

ITEM #5
  interviewer_question: time=14:55 text="so i guess one additional question i have is how do we know the performance edition of doing like more advanced approaches right and so let's say that we want to dive into computer vision i know you have a computer vision back under our and so like i guess like how would you assess the necessity of maybe using like images into your analysis versus just only using text and you know you know that image is probably harder to train there's probably a lot more difficulty with having expertise and images versus just text which has like great packages on python to use and so yeah how would you kind of like approach that situation how would you know that it's worth doing the image analysis into the features versus just going with a basic model"
  candidate_answer: time=15:41 text="yes i think i mean a very simple approach that you could use that i like using is you just like sort of build the model you have all the features in there and then you get its prediction what the full model's prediction accuracy is so say for instance the full model is at 90 seems really good and then you drop the images from the model and then you see you know when you remove the images what the value is and the accuracy and say it's 85 and then say you you do it again but you remove the text data and the text data when you remove it it's like 7 60 accuracy or something so so so yeah there you can know oh wow the text is very valuable but the images does drop it so you're like okay well you told me now when you drop the images the accuracy does drop but is that a meaningful drop so one thing i think you could do is just simulate like randomly sampling the data especially because we have enough data like i said here i guess in this facebook huge amount of data set so what you could do is randomly sample from the data and retrain the model each time and get this drop in accuracy when you remove the images and so say i guess i could say if 95 of the time the drop in accuracy is more than zero it's like it's like there's a negative drop so then i might say yeah images are important because almost all the time that i've tried it out in simulating across multiple samples there is that drop in accuracy"
  reference_answer: time=None text=None
  interviewer_feedback: time=17:00 text='gotcha okay cool yeah i mean that makes a lot of sense'
  question_topic: ML

ITEM #6
  interviewer_question: time=17:02 text='any additional kind of thoughts on this question'
  candidate_answer: time=17:05 text="oh i was going to say something about like if we could augment the data too for text data but some of those things are cool where you can use machine translation to change the specific text words but keep the meaning but i guess other things this model would be sort of a first step we're taking in all these features the user data the flags and the text we're making some predictions so i think the final thing would just be to check where the errors are happening and maybe use that to help with the model so one thing you might find is that say we flag toy guns all the time are being flagged yeah so one simple thing you could do with just the simple model where i use a bag of words is i could use like uh n-gram model so i could take every two words and and use the pairs of words and then in that case i would get toy gun and that way i could identify oh these things that are actually toy guns that are being wrongly flagged and i could solve that problem by just changing the model to include this local history um with pairs of words"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #7
  interviewer_question: time=18:01 text="final question and this is kind of just more in relation to the question itself like what do you think about this question like how well do you think it assesses the candidate's performance just overall how do you feel your answer would kind of like fit in into like a broader facebook interview"
  candidate_answer: time=18:15 text="i mean i'm not sure about the broader facebook interview but i guess this i mean this question is pretty it seems very standard like it's very machine learning right you test your knowledge of minority like when you have very few things you're predicting you have to sort of build the model but you go from end to end and i think it's also to me seems like a fairly common problem you might face not this specific one but something like this where you know you need to identify something from a particular listing a particular post or or some you know in my case i deal with videos a lot and so it's it's like in line with i think what what you also might have to work on yeah what were your thoughts you have any"
  reference_answer: time=None text=None
  interviewer_feedback: time=18:49 text="yeah i mean i liked it a lot and i liked your answer and how you structured everything and i feel like that's a great approach for most machine learning type questions as well because i feel like most of them have a very defined beginning middle and end in terms of where's the data how do you build the model and then how would you deploy and evaluate it and i think focusing on those approaches is really key and so i think you did a great job there yeah good awesome"
  question_topic: Communication

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/interview-query/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18/ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
