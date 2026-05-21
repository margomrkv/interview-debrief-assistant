<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29",
  "transcript_folder": "transcripts/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29",
  "source_id": "business_intelligence_middle_amazon_duplicate_products_interview_query_2020_05_29",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:18:02 +0200",
  "updated_at": "2026-05-20 21:30:16 +0200",
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
    "json": "splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/timecodes.txt",
        "en",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 21:18:02 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 4.0,
      "notes": null,
      "finished_at": "2026-05-20 21:30:16 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:30:16 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29`
- **Source ID:** `business_intelligence_middle_amazon_duplicate_products_interview_query_2020_05_29`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:18:02 +0200
- **Last updated:** 2026-05-20 21:30:16 +0200

Фильтр в IDE: `*business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/timecodes.txt`<br>`en`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.pipeline-log.md` | — | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.xlsx` | 4.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.validation-report.md` | 1.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.pipeline-log.md`

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
SOURCE_ID: business_intelligence_middle_amazon_duplicate_products_interview_query_2020_05_29
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29
INTERVIEW_LANGUAGE: en
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:03] hi everyone this is Jay from interview
[00:05] query today I am joined with Shashank I
[00:10] think I said that right even though I
[00:13] keep my forgetting um who has worked in
[00:16] data for a couple years now I figured as
[00:19] they worked at companies such as all
[00:22] startups in Amazon
[00:24] welcome to the mock interview and before
[00:27] we get started I would love to just kind
[00:30] of like to ask you about your background
[00:32] and how you got into data science and
[00:34] yeah how you got interested in it
[00:37] sure thank you so much for having me
[00:40] over here Jay so a little bit about my
[00:43] background I've always been a data and
[00:46] numbers guy I used to work as a bi
[00:49] engineer back before I got a masters and
[00:52] then I did a master's in data analytics
[00:54] work with the data scientist for almost
[00:57] two years mostly my experience has been
[01:00] around machine learning problems and
[01:02] machine learning implementation ended up
[01:04] learning some DevOps skills as well and
[01:06] like PI spark stuff so that when you
[01:09] know when you have their products need
[01:11] to be scaled out if the coding is pretty
[01:13] different so I ended up learning how to
[01:17] convert like Python code to PI spark on
[01:19] my own learning experience and then I
[01:22] moved over to Amazon as a business
[01:24] intelligence engineer most of my work
[01:26] over here was around you know tableau
[01:29] reporting building ETL jobs figuring out
[01:32] what kind of data structure needs to be
[01:35] in the reporting databases so that your
[01:38] end reports work well and you know just
[01:40] digging into deeper into different
[01:42] metrics that the business wants to learn
[01:43] and just providing more information on
[01:46] what they could look at instead of what
[01:48] they're already looking at so that's
[01:50] pretty much what my experience has been
[01:53] so far from a technical point of view
[01:55] it's more about sequel Python Vice power
[01:58] tableau and then some Jango Web API as
[02:03] well because in my previous company
[02:05] nobody really knew how to use you know
[02:07] Python based data science models so I
[02:09] had to figure out how to production lies
[02:12] them on my own and have the end product
[02:14] just make like Web API calls to be
[02:16] predictions instead of dem trying to you
[02:19] know ingest a mortal end and interact
[02:22] with it so that was a pretty neat skill
[02:25] to have and think that's something
[02:27] that's being needed more and more in
[02:29] many companies these days
[02:30] definitely yeah I think the overall kind
[02:34] of scale of data Sciences
[02:36] needs a lot of what you just kind of
[02:39] described in different kinds of metrics
[02:42] track like ETL jobs being able to do the
[02:46] modeling for each and just having an
[02:47] idea of every part of the funnel in
[02:50] terms of cool so I'd love to start out
[02:55] with like a first question and let's say
[02:57] this has to do with an e-commerce
[03:00] website like Amazon right so let's say
[03:03] you're running an e-commerce website and
[03:06] you want to get rid of let's say
[03:08] duplicate products I may be listed under
[03:09] different sellers names you know like a
[03:13] really large database so for example we
[03:17] have two products but that the same
[03:18] product but they're named iPhone X and
[03:21] Apple iPhone 10 right and so given that
[03:24] we have these two products we want to
[03:26] deduplicate it but let's say that this
[03:29] example shows up for like a lot of
[03:30] different cases what's one way that you
[03:33] would go a bit go about actually doing
[03:35] this so if it's a established ecommerce
[03:43] company I would assume that they would
[03:45] have some kind of an ID for every
[03:49] product that they have in their
[03:50] inventory so something like an SKU or an
[03:53] ace and if it's Amazon then that's
[03:56] pretty unique and you know even the you
[03:58] know the description is different in
[04:00] different under different sellers and I
[04:03] would assume that they would have the
[04:04] same SKU so you know if you just look at
[04:07] the you know get a list of all the all
[04:10] like get a total of the SKU different
[04:13] sellers and then do a distinct list of
[04:17] SK use across sellers you will notice
[04:19] what kind of SK use are replicated and
[04:23] under which seller and then once you
[04:25] have that you can go to the business
[04:26] saying what do you want to do with them
[04:28] if people eat them
[04:30] whatever yeah cool so let's say let's
[04:35] make it a little bit more complicated
[04:36] and let's say that we don't have that
[04:38] skate you right and let's say that
[04:40] people are just creating their listings
[04:43] by just entering in like what they think
[04:44] the product names are and then you know
[04:47] like a picture description and
[04:51] essentially what kind of goes on on
[04:52] Amazon right now right so how would we
[04:57] do the I guess the mapping to the SKU or
[05:01] would you even think of like a different
[05:02] approach towards even like solving the
[05:05] problem yeah I mean couple of things
[05:07] come to mind if we have recall like
[05:11] images for for these products that we
[05:14] think may be duplicated we can try to
[05:17] you know use some algorithms that
[05:18] identify similar images and then once
[05:22] you have that list of similar images
[05:24] then you look at the descriptions and
[05:25] then you can build a string similarity
[05:27] kind of algorithm which you know says
[05:30] with which descriptions sound very
[05:32] similar or are very close to each other
[05:34] and then you would have to at least two
[05:37] data points that say that you know these
[05:39] two products seem to be similar and then
[05:41] it's probably going to be a little bit
[05:42] of manual intervention to identify are
[05:44] they really similar or not but going by
[05:48] image similarity in our description
[05:49] similarity that should be the other
[05:53] thing that I can think of is maybe
[05:56] reviews on different products so imagine
[05:59] that there are two different products
[06:01] just named differently but both of them
[06:03] are like an Apple iPhone 10 you would
[06:05] assume that the reviews are pretty much
[06:07] talking about a phone and it's
[06:09] manufactured by Apple and probably have
[06:11] the same kind of experiences so you
[06:13] could try to see if the reviews are very
[06:16] similar to each other and that gives a
[06:19] good indication that the product is
[06:20] probably the same
[06:21] okay so let's say we go with the process
[06:26] all those things right now we're looking
[06:29] at similar across images cross
[06:31] descriptions across reviews right and so
[06:35] we're getting this like score for each
[06:37] one of them right so now how do we go
[06:41] about and
[06:43] if we can duplicate deduplicate them or
[06:46] not do we have like a human review of
[06:49] every single one do we do some sort of
[06:51] like scaling process because let's say
[06:53] we have to do this for like thousands
[06:55] and thousands of products right right
[06:57] what's the next step um so because we
[07:01] like from the beginning we don't really
[07:03] know which products are the same or not
[07:06] so it we can't really do like a
[07:08] supervised learning here it needs to be
[07:10] a unsupervised technique that first
[07:12] tries to identify what what stuff are
[07:16] similar to each other so I probably do
[07:19] like a clustering based on just
[07:21] descriptions you know like first we'll
[07:23] definitely do some cleaning and in a
[07:25] tokenization and stuff for the text data
[07:27] and then bring it to a structured format
[07:30] and then try to + try to maybe to like a
[07:33] tf-idf on different documents and these
[07:37] documents would have the prescription
[07:38] and maybe reviews as well so you do a
[07:41] tf-idf to find out which documents are
[07:43] similar to each other you'll get some
[07:45] scores and then you can depending on how
[07:50] many documents end up in a particular
[07:51] cluster you will definitely have to do a
[07:54] manual step to see if they're actually
[07:56] same or not images as well I think I'm
[08:01] not aware of a clustering technique that
[08:03] works on images but you will probably
[08:05] have to build out features from the
[08:06] image bring it to a structured format
[08:08] and then do clustering on top so you
[08:12] might be able to identify like ten
[08:14] different clusters if there are ten
[08:16] different if they're ten items that are
[08:17] duplicated and then look at the clusters
[08:20] descriptive statistics to see what what
[08:23] is this custom really talking about is
[08:24] it a phone is a tablet is it a computer
[08:27] or whatever and then try to and then go
[08:29] about in a manual investigation from
[08:31] that point of view from that point okay
[08:33] so let's say we do that and we're going
[08:36] through these clusters right and we find
[08:39] that the algorithm has at least for a
[08:43] couple of them has clustered just like
[08:44] phones together instead of doing
[08:46] specific enough for the same product
[08:49] right or maybe we're getting like
[08:52] thousands of different clusters
[08:55] potentially where like there may be no
[08:58] like not matched up as well is there any
[09:00] way that we can almost like optimize our
[09:03] manual intervention or like any other
[09:07] techniques in which we can kind of scale
[09:09] this problem out so that we somehow use
[09:14] like the least amount of you know manual
[09:17] overview while also figuring out like a
[09:20] way to do it efficiently as well right I
[09:25] guess it would depend on the features
[09:29] that we actually extract the more
[09:31] granular the features in our dataset and
[09:33] the better the clusters could be if we
[09:37] are creating clusters just on the type
[09:39] of device then you're right I think all
[09:41] phones and all computers will just end
[09:44] up together but if we given that these
[09:48] are also like you know we suspect that
[09:50] these are duplicate listings we would
[09:53] definitely want to look at more
[09:55] information of the listing itself like
[09:56] what is the price of the product what's
[09:58] the maybe the different types of colors
[10:01] that's available and then what is the I
[10:05] don't know what like you know stuff that
[10:08] iPhones and androids have similar to
[10:10] each other like an operating system and
[10:13] stuff like that so depending so the
[10:15] features need to be as close to the
[10:17] product itself so that our clusters are
[10:20] more identifiable among each other and
[10:23] not generic as phones and computers so
[10:27] that's what comes to mind but other than
[10:29] that let me think of it if there's
[10:33] anything else that could be useful here
[10:36] so we have a listing maybe there are
[10:39] sellers as well right like different
[10:41] sellers I mean you could assume that a
[10:43] particular seller of you know different
[10:46] phones are similar to each other in like
[10:50] electronic seller and they have so so
[10:54] and so different products and this is
[10:57] the amount of average driving it at the
[11:00] gate and stuff like that so depending on
[11:02] the seller's demographics I think we
[11:05] would be able to identify what seller is
[11:07] probably an electronic syllabus as a
[11:09] hardware setup so that could be
[11:12] something useful to look at and then
[11:16] maybe the customers itself are like you
[11:19] know we can look at purchased behavior
[11:21] as well
[11:22] iPhones typically tend to sell out as
[11:25] soon as they are launched so you can try
[11:27] to you know use information around when
[11:30] a particular product was launched and
[11:32] then look at the purchase pattern during
[11:35] that time and then try to integrate
[11:37] these features in your actual data set
[11:40] so that there's some customer purchase
[11:42] behavior being being looked at some
[11:45] seller behavior being looked at and and
[11:46] most of it would be the product
[11:48] description itself like the product
[11:50] itself and then I wanted to do a brief
[11:57] feedback session on the first question -
[12:01] so what did you think about the first
[12:03] question yeah I think the question was
[12:05] good it was pretty vague in the
[12:09] beginning but I think based on what your
[12:12] cues were I felt like a we wanted a more
[12:19] algorithmic solution than like a sequel
[12:21] database so initially I thought that
[12:26] it's more like a simple question where I
[12:28] can tell what kind of distinct or which
[12:30] columns I need to be grouping by but
[12:32] turned out that we wanted to check this
[12:36] at a more higher scale so I think it was
[12:39] a good brainstorming question there
[12:41] multiple ways that it could have gone
[12:43] but I think we ended up with a few good
[12:48] starting points at least a tackle oh
[12:50] yeah any so two bits of feedback I think
[12:53] like scaling out the approach to would
[12:57] be better so like having a broader
[12:59] horizon on the the case maybe like so
[13:04] not limit it to just like kind of phones
[13:06] and maybe think about other news cases
[13:10] with why ecommerce as big as like Amazon
[13:13] and then I think having like
[13:19] I think more data points is also helpful
[13:22] when explaining these things so like
[13:23] being able to either like create
[13:27] assumptions off of like how much like
[13:31] data we have to deal with and so one
[13:36] example of this is like being able to
[13:39] understand like if there are let's say
[13:41] like thousands of these duplicated
[13:43] products then like how much can we
[13:47] automate out and just assume like an
[13:49] error case of like you know let's say
[13:51] like 5% and how much can we like do
[13:56] manually because it's like important so
[13:58] like with iPhones let's say like it's
[14:00] pretty important but let's say that
[14:01] we're selling like pokemon cards that
[14:03] are like you know not blender duplicated
[14:07] it's like how much of that can we get on
[14:09] just like an automated solution of like
[14:10] doing word matching and then like
[14:14] getting a high enough threshold and then
[14:15] just being like okay that's fine and
[14:17] then like running through the cases
[14:19] getting like three percent error through
[14:21] manual selection getting like an idea
[14:25] that if we scale that out then we're
[14:27] okay with like three percent error going
[14:29] forward right so like a disclaimer or at
[14:33] least a dialogue around what officials
[14:36] could make sense in terms of
[14:38] implementation that would have been
[14:40] helpful because yeah I mean without
[14:42] really implementing I wouldn't really be
[14:44] able to tell you know what kind of get
[14:46] on that but assume you have enough data
[14:48] we should just assume that we'll have an
[14:50] algorithm that does well and then we can
[14:53] talk about the yeah exactly like
[14:57] basically being the tweak to sensitive
[15:00] enough for like our business cases right
[15:02] like assuming that obviously we don't
[15:05] really care about duplication if it's a
[15:07] you know something that doesn't affect
[15:09] the business too much well we do care if
[15:12] you know multiple sellers are like
[15:16] trying to sell you know really high
[15:18] value products like iPhones or Macs for
[15:21] whatever reason and we don't want it to
[15:23] like go past like you know a first page
[15:25] results yeah general thought process on
[15:29] that was pretty good and structured and
[15:30] like went down the narrow the path that
[15:32] like we're trying to lead
[15:33] towards cool and then I guess yeah I
[15:39] guess lastly on that like is is there
[15:41] any kind of ideas or thoughts you have
[15:45] around like potentially like how these
[15:49] questions are almost measured in like
[15:51] real interviews and this is kind of like
[15:53] apart from the mock interview but just
[15:54] like love your thoughts on like how you
[15:56] think these questions like that are more
[16:00] ambiguous should get well I kind of
[16:02] graded kind of like almost like rubric
[16:04] wise okay like from a rubric ways I
[16:08] think generally for case interviews what
[16:11] I think from a candidate perspective
[16:13] they should be graded based on what kind
[16:16] of questions they ask in the beginning
[16:17] like what kind of clarifying questions
[16:19] they ask how much information other than
[16:22] the problem statement they're able to
[16:23] extract out of the interviewer because
[16:25] they ask the right questions and the
[16:27] interviewer actually wanted to give them
[16:28] some information so that the discussion
[16:30] leads down to the path that they want to
[16:32] go to because from what I understand
[16:35] more often than not in the case study
[16:37] interviews
[16:37] it's the interviewer who decides what
[16:39] where the candidate needs to end up at
[16:42] and even if the candidate has like
[16:44] multiple different ideas it's up to the
[16:46] interview to guide and that this is the
[16:48] path I want you to take so yeah I think
[16:51] the first step would be like checking
[16:52] how many questions are they able to get
[16:55] in the beginning how many extra data
[16:58] points are able to think and then maybe
[17:00] like five minutes of questioning and
[17:02] then based on all the answers they get
[17:04] how are they able to like drill down on
[17:06] that on those data points like if do
[17:08] they have like a segmentation approach
[17:10] to estimating different values in that
[17:13] problem statement that should be pretty
[17:16] good and then of course calling out the
[17:19] assumptions you know at every point is a
[17:22] candidate calling out what assumptions
[17:23] he is making and then checking if those
[17:25] assumptions make sense or not with the
[17:27] business point of view so that seems to
[17:30] be a point that should be looked into
[17:32] and then yeah at the end I think it's
[17:35] there's never really a right answer so
[17:37] it's just about you know how well the
[17:39] candidate is able to summarize his
[17:41] solution to the problem okay oh no I
[17:46] like that I
[17:47] I enjoy that I think that's a great way
[17:49] to kind of define it as well and
[17:51] especially since it's so ambiguous on
[17:55] either side I think being able to make
[17:59] note of what the good points are is
[18:00] helpful right yeah Oh awesome thanks so
[18:04] much for your help

FEEDBACK_MD:
---
section: "Feedback and Tips"
start: "11:55"
end: "18:06"
start_seconds: 715
end_seconds: 1086
---

feedback session on the first question - so what did you think about the first question yeah I think the question was good it was pretty vague in the beginning but I think based on what your cues were I felt like a we wanted a more algorithmic solution than like a sequel database so initially I thought that it's more like a simple question where I can tell what kind of distinct or which columns I need to be grouping by but turned out that we wanted to check this at a more higher scale so I think it was a good brainstorming question there multiple ways that it could have gone but I think we ended up with a few good starting points at least a tackle oh yeah any so two bits of feedback I think like scaling out the approach to would be better so like having a broader horizon on the the case maybe like so not limit it to just like kind of phones and maybe think about other news cases with why ecommerce as big as like Amazon and then I think having like I think more data points is also helpful when explaining these things so like being able to either like create assumptions off of like how much like data we have to deal with and so one example of this is like being able to understand like if there are let's say like thousands of these duplicated products then like how much can we automate out and just assume like an error case of like you know let's say like 5% and how much can we like do manually because it's like important so like with iPhones let's say like it's pretty important but let's say that we're selling like pokemon cards that are like you know not blender duplicated it's like how much of that can we get on just like an automated solution of like doing word matching and then like getting a high enough threshold and then just being like okay that's fine and then like running through the cases getting like three percent error through manual selection getting like an idea that if we scale that out then we're okay with like three percent error going forward right so like a disclaimer or at least a dialogue around what officials could make sense in terms of implementation that would have been helpful because yeah I mean without really implementing I wouldn't really be able to tell you know what kind of get on that but assume you have enough data we should just assume that we'll have an algorithm that does well and then we can talk about the yeah exactly like basically being the tweak to sensitive enough for like our business cases right like assuming that obviously we don't really care about duplication if it's a you know something that doesn't affect the business too much well we do care if you know multiple sellers are like trying to sell you know really high value products like iPhones or Macs for whatever reason and we don't want it to like go past like you know a first page results yeah general thought process on that was pretty good and structured and like went down the narrow the path that like we're trying to lead towards cool and then I guess yeah I guess lastly on that like is is there any kind of ideas or thoughts you have around like potentially like how these questions are almost measured in like real interviews and this is kind of like apart from the mock interview but just like love your thoughts on like how you think these questions like that are more ambiguous should get well I kind of graded kind of like almost like rubric wise okay like from a rubric ways I think generally for case interviews what I think from a candidate perspective they should be graded based on what kind of questions they ask in the beginning like what kind of clarifying questions they ask how much information other than the problem statement they're able to extract out of the interviewer because they ask the right questions and the interviewer actually wanted to give them some information so that the discussion leads down to the path that they want to go to because from what I understand more often than not in the case study interviews it's the interviewer who decides what where the candidate needs to end up at and even if the candidate has like multiple different ideas it's up to the interview to guide and that this is the path I want you to take so yeah I think the first step would be like checking how many questions are they able to get in the beginning how many extra data points are able to think and then maybe like five minutes of questioning and then based on all the answers they get how are they able to like drill down on that on those data points like if do they have like a segmentation approach to estimating different values in that problem statement that should be pretty good and then of course calling out the assumptions you know at every point is a candidate calling out what assumptions he is making and then checking if those assumptions make sense or not with the business point of view so that seems to be a point that should be looked into and then yeah at the end I think it's there's never really a right answer so it's just about you know how well the candidate is able to summarize his solution to the problem okay oh no I like that I I enjoy that I think that's a great way to kind of define it as well and especially since it's so ambiguous on either side I think being able to make note of what the good points are is helpful right yeah Oh awesome thanks so much for your help

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
Write JSON only to: splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.json \
    --video transcripts/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.json --out splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.qa-split.json \
    --video transcripts/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.validation-report.md

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
video.md: transcripts/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/video.md

--- CHAPTER `00:35` — Shashank Intro ---
window: 00:35 .. 02:55
recognition_status: not_recognized (0 items)

(no items extracted)
--- CHAPTER `02:55` — Business Intelligence Case Question ---
window: 02:55 .. 11:55
recognition_status: multiple (4 items)

ITEM #2
  interviewer_question: time=02:55 text="I'd love to start out with like a first question and let's say this has to do with an e-commerce website like Amazon right so let's say you're running an e-commerce website and you want to get rid of let's say duplicate products I may be listed under different sellers names you know like a really large database so for example we have two products but that the same product but they're named iPhone X and Apple iPhone 10 right and so given that we have these two products we want to deduplicate it but let's say that this example shows up for like a lot of different cases what's one way that you would go a bit go about actually doing this"
  candidate_answer: time=03:35 text="so if it's a established ecommerce company I would assume that they would have some kind of an ID for every product that they have in their inventory so something like an SKU or an ace and if it's Amazon then that's pretty unique and you know even the you know the description is different in different under different sellers and I would assume that they would have the same SKU so you know if you just look at the you know get a list of all the all like get a total of the SKU different sellers and then do a distinct list of SK use across sellers you will notice what kind of SK use are replicated and under which seller and then once you have that you can go to the business saying what do you want to do with them if people eat them whatever yeah"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Data Modeling

ITEM #3
  interviewer_question: time=04:35 text="let's make it a little bit more complicated and let's say that we don't have that skate you right and let's say that people are just creating their listings by just entering in like what they think the product names are and then you know like a picture description and essentially what kind of goes on on Amazon right now right so how would we do the I guess the mapping to the SKU or would you even think of like a different approach towards even like solving the problem"
  candidate_answer: time=05:05 text="yeah I mean couple of things come to mind if we have recall like images for for these products that we think may be duplicated we can try to you know use some algorithms that identify similar images and then once you have that list of similar images then you look at the descriptions and then you can build a string similarity kind of algorithm which you know says with which descriptions sound very similar or are very close to each other and then you would have to at least two data points that say that you know these two products seem to be similar and then it's probably going to be a little bit of manual intervention to identify are they really similar or not but going by image similarity in our description similarity that should be the other thing that I can think of is maybe reviews on different products so imagine that there are two different products just named differently but both of them are like an Apple iPhone 10 you would assume that the reviews are pretty much talking about a phone and it's manufactured by Apple and probably have the same kind of experiences so you could try to see if the reviews are very similar to each other and that gives a good indication that the product is probably the same"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #4
  interviewer_question: time=06:21 text="okay so let's say we go with the process all those things right now we're looking at similar across images cross descriptions across reviews right and so we're getting this like score for each one of them right so now how do we go about and if we can duplicate deduplicate them or not do we have like a human review of every single one do we do some sort of like scaling process because let's say we have to do this for like thousands and thousands of products right right what's the next step um"
  candidate_answer: time=06:57 text="so because we like from the beginning we don't really know which products are the same or not so it we can't really do like a supervised learning here it needs to be a unsupervised technique that first tries to identify what what stuff are similar to each other so I probably do like a clustering based on just descriptions you know like first we'll definitely do some cleaning and in a tokenization and stuff for the text data and then bring it to a structured format and then try to + try to maybe to like a tf-idf on different documents and these documents would have the prescription and maybe reviews as well so you do a tf-idf to find out which documents are similar to each other you'll get some scores and then you can depending on how many documents end up in a particular cluster you will definitely have to do a manual step to see if they're actually same or not images as well I think I'm not aware of a clustering technique that works on images but you will probably have to build out features from the image bring it to a structured format and then do clustering on top so you might be able to identify like ten different clusters if there are ten different if they're ten items that are duplicated and then look at the clusters descriptive statistics to see what what is this custom really talking about is it a phone is a tablet is it a computer or whatever and then try to and then go about in a manual investigation from that point of view from that point"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #5
  interviewer_question: time=08:33 text="so let's say we do that and we're going through these clusters right and we find that the algorithm has at least for a couple of them has clustered just like phones together instead of doing specific enough for the same product right or maybe we're getting like thousands of different clusters potentially where like there may be no like not matched up as well is there any way that we can almost like optimize our manual intervention or like any other techniques in which we can kind of scale this problem out so that we somehow use like the least amount of you know manual overview while also figuring out like a way to do it efficiently as well right"
  candidate_answer: time=09:25 text="I guess it would depend on the features that we actually extract the more granular the features in our dataset and the better the clusters could be if we are creating clusters just on the type of device then you're right I think all phones and all computers will just end up together but if we given that these are also like you know we suspect that these are duplicate listings we would definitely want to look at more information of the listing itself like what is the price of the product what's the maybe the different types of colors that's available and then what is the I don't know what like you know stuff that iPhones and androids have similar to each other like an operating system and stuff like that so depending so the features need to be as close to the product itself so that our clusters are more identifiable among each other and not generic as phones and computers so that's what comes to mind but other than that let me think of it if there's anything else that could be useful here so we have a listing maybe there are sellers as well right like different sellers I mean you could assume that a particular seller of you know different phones are similar to each other in like electronic seller and they have so so and so different products and this is the amount of average driving it at the gate and stuff like that so depending on the seller's demographics I think we would be able to identify what seller is probably an electronic syllabus as a hardware setup so that could be something useful to look at and then maybe the customers itself are like you know we can look at purchased behavior as well iPhones typically tend to sell out as soon as they are launched so you can try to you know use information around when a particular product was launched and then look at the purchase pattern during that time and then try to integrate these features in your actual data set so that there's some customer purchase behavior being being looked at some seller behavior being looked at and and most of it would be the product description itself like the product itself"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Product Metrics

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/interview-query/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29/business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
