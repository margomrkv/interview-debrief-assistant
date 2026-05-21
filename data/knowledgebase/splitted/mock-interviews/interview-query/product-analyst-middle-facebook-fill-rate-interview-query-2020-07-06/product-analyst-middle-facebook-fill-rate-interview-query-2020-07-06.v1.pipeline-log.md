<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06",
  "transcript_folder": "transcripts/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06",
  "source_id": "product_analyst_middle_facebook_fill_rate_interview_query_2020_07_06",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:18:04 +0200",
  "updated_at": "2026-05-20 21:31:01 +0200",
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
    "json": "splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/timecodes.txt",
        "en",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.pipeline-log.md"
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
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:31:01 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:31:01 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06`
- **Source ID:** `product_analyst_middle_facebook_fill_rate_interview_query_2020_07_06`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:18:04 +0200
- **Last updated:** 2026-05-20 21:31:01 +0200

Фильтр в IDE: `*product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/timecodes.txt`<br>`en`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.pipeline-log.md` | — | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.validation-report.md` | 1.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.pipeline-log.md`

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
SOURCE_ID: product_analyst_middle_facebook_fill_rate_interview_query_2020_07_06
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06
INTERVIEW_LANGUAGE: en
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00] [Music]
[00:03] hi everyone this is Jay from interview
[00:05] query today I am doing a mock interview
[00:08] with Ben
[00:10] he's a data scientist next door and
[00:13] envoy and formerly at Blackrock as well
[00:17] then thanks for being here hey how are
[00:22] you doing Jay good so to start out I
[00:25] thought we could tackle one of these
[00:28] questions that is pretty popular in
[00:34] terms of ads but first I'd love to just
[00:38] kind of do like a quick summary on your
[00:41] like background like how did you get
[00:43] into data science sure um when I went in
[00:48] finance after graduating from college
[00:51] study computer science like a lot of
[00:54] folks here in Silicon Alley and was
[00:58] working on some level of analysis and
[01:00] construction of some model portfolios
[01:01] that we had and in doing so you know
[01:04] worked with a lot of data like financial
[01:06] data that was coming through um I became
[01:08] responsible for you know kind of
[01:11] reliable delivery of that data as well
[01:12] as kind of building tools to help make
[01:15] the analysis process more efficient so
[01:20] what kind of fell into data like that
[01:21] and when I decided that I didn't want to
[01:23] work in finance anymore and go into more
[01:25] you know consumer tech data was kind of
[01:28] a natural Avenue for mediums kind of
[01:30] continue working in so there was this
[01:33] hot term at the time data science it
[01:36] became like that kind of Explorer and
[01:38] you know one thing led to another nice
[01:40] cool I'm glad that you got into it and I
[01:45] think that there's definitely you know
[01:47] lots of people transitioning from
[01:48] finance over as well I can definitely
[01:50] resonate with that kind of
[01:53] characterization of your background cool
[01:57] so the first question that I have for
[02:00] you today is let's say that you work on
[02:02] the ads team had a social media company
[02:05] let's say Facebook right and a
[02:09] definition or term that they have in ads
[02:11] is fill rate and it's defined as the
[02:14] number of overall impressions divided by
[02:16] potential opportunities so let's say
[02:19] that you see that this film rate metric
[02:21] has dipped by 10%
[02:23] what would you investigate first I'd
[02:28] want to find out whether that 10% is
[02:30] like relative or you mean like in
[02:32] absolute terms let's say that it's
[02:36] relative so if you know fillrate was
[02:40] holding 70 percent yeah
[02:42] steady and then let's say it happened
[02:45] it's been steady for like a week and
[02:47] then it dipped down by 10 percent to
[02:51] like 81 percent okay okay so I guess you
[02:56] know seeing that it's a rate obviously
[02:59] made up of kind of like a numerator and
[03:03] denominator sometimes doesn't tell the
[03:05] full story when you look at it just as a
[03:07] metric by self so the first thing I
[03:09] would do would be to look into like
[03:11] what's going on like what's driving that
[03:13] that that drop in the fill rate so what
[03:17] could be happening is you know the
[03:19] denominator in this case the impression
[03:22] opportunities could be getting a lot
[03:24] bigger
[03:24] which you know my actually signal that a
[03:27] growth in the business so that might be
[03:29] something that that's favorable and
[03:31] simply we just need some time for the
[03:34] numerator to catch up on assuming like
[03:36] you know we're showing ads here so like
[03:38] you advertise yourself to come online
[03:41] yep
[03:42] the other scenario is obviously if the
[03:44] numerator is is the one dropping and
[03:46] we're not seeing any new activity on the
[03:48] denominator then that would be a little
[03:51] bit more of a cause for immediate
[03:53] concern and probably something we want
[03:55] to look into immediately okay so let's
[03:59] say that it was the denominator that
[04:02] actually increased and then let's
[04:06] clarify and say that this was like
[04:09] specifically like a one-time event so
[04:11] it's not like cyclical so it didn't
[04:13] happen it's not like a weekly thing
[04:15] because you know increased usage on the
[04:18] weekend or something like that like a
[04:21] monthly or yearly thing what would you
[04:23] then look at after that
[04:25] sorry did you say the new denominator oh
[04:28] yeah the denominator increased yeah and
[04:33] it was a one time thing
[04:34] okay yeah I would you know so in this
[04:37] case since its opportunities what might
[04:40] be happening is there's so so two things
[04:44] right like this is a social network so
[04:46] there are people who are coming onto the
[04:50] network to see these potential ads so
[04:53] it's probably unlikely that behavior
[04:56] changed overnight and like you know
[04:57] people are suddenly like engaging like a
[05:00] llama although who knows maybe with you
[05:02] know coronavirus coming around
[05:04] that did happen overnight yeah but it
[05:06] could also be the case that there's a
[05:08] ton of new user activity and like a
[05:10] bunch of new members be from like a like
[05:12] a big marketing push or something that
[05:15] led to a lot of new user signing up so
[05:17] we have a lot of new sessions where
[05:18] they're seeing a couple of these
[05:20] opportunities so I guess the next place
[05:22] that would check would be what's causing
[05:25] that increase in the opportunity number
[05:28] whether it's like a bunch of new members
[05:30] or a bunch of new sections gosh it and
[05:33] so is there any other way that you can
[05:37] divide it out even within like the new
[05:40] users or new sessions to understand
[05:43] where I might be coming from given like
[05:46] in this scenario Facebook is like a
[05:47] pretty big business so there's probably
[05:51] like a ton of different ways that people
[05:54] can sign up for a you know a Facebook
[05:57] account or potentially be using Facebook
[05:59] at the time so how else would I break
[06:02] out the increase in sessions you're
[06:04] saying yeah so so let's say let's say we
[06:12] see a lot of new sessions from new
[06:14] members I would obviously look into like
[06:17] like acquisition channels of all these
[06:19] new members and see you know if there's
[06:21] whether one of the theories that I just
[06:23] threw out might be the reason why there
[06:26] are there are new members joining like
[06:28] maybe some I don't know some advertising
[06:31] campaign we're running elsewhere
[06:32] suddenly everyone else stopped bidding
[06:33] on those keywords so now like you know
[06:35] we're just like it getting a lot of new
[06:38] users
[06:39] uh not sure if I'm going down the right
[06:41] track let's say like we're focusing in
[06:45] on sessions right so let's say that we
[06:50] know that there's a lot more sessions is
[06:53] there a way that we can verify that the
[06:55] sessions are coming from new users as
[06:56] well compared to just existing users
[06:59] using the platform suddenly yeah we
[07:02] would look at you know sessions per user
[07:04] and we would see like and we would
[07:07] compare to the total number of users so
[07:09] like you know sessions could go up but
[07:11] those could come from like a slew of new
[07:13] users or they could be that existing
[07:15] user suddenly are engaging a lot more on
[07:17] that particular date right so I will try
[07:19] to figure out like just take my number
[07:22] of sessions and divide it quickly over
[07:24] my number of distinct users that day and
[07:26] just get a sense of like what that ratio
[07:28] is and I would expect if it were new
[07:31] users that that number would drop right
[07:34] like New Year's I expect to have less
[07:35] engagement when they first join but and
[07:37] and driven by the figure member base
[07:40] it's increased from engagement in my
[07:43] existing users then I would expect that
[07:46] number to have increased okay so let's
[07:49] take a step back and say that let's say
[07:52] the denominator actually in that
[07:54] philaret calculation stayed the same is
[07:59] there something else that you could look
[08:00] at then yeah that would probably point
[08:04] towards the numerator being the problem
[08:06] in which case this is impressions so it
[08:11] may seem like a more dire problem before
[08:13] suddenly showing a lot fewer impressions
[08:17] there's a you know then it then it
[08:19] becomes a matter of like where we're
[08:21] getting advertisers from like if I would
[08:25] start with like you know an ops team and
[08:27] figure out whether some campaigns just
[08:29] ended and if we don't have direct
[08:32] campaigns we have like you know ad
[08:34] exchanges that were cooked into maybe
[08:36] like something broke like check for code
[08:38] that may have potentially like broken
[08:40] the integration yeah yeah but I mean the
[08:44] first step would be to verify that you
[08:45] know impressions actually did drop and I
[08:47] would find a third party source to try
[08:49] to verify that if possible because it
[08:53] could also mean
[08:53] like you know an engineering bug where
[08:55] our impression tracking just broke
[08:57] for example gotcha yeah let's say that
[09:00] there wasn't a bug anywhere in the code
[09:05] or anything where we double down that
[09:07] and we see that there was no error
[09:09] technically on where else could be then
[09:13] kind of investigate like I said goes
[09:19] through the business side of things and
[09:20] just trying to figure out like I am I
[09:22] seeing the same number of advertisers
[09:24] throughout the week as I am today like
[09:26] if I see a massive drop like or if I
[09:30] don't even see a massive drop I see that
[09:31] some advertisers were you know kind of
[09:34] doing pretty constant delivery
[09:35] throughout the week and some just
[09:37] dropped off maybe they reached their
[09:39] goal or they move through their budget
[09:42] so then you know they're not delivering
[09:44] anymore so try to find anything that
[09:46] looks abnormal by looking at kind of
[09:49] like a seven-day trend just to see
[09:52] gotcha okay cool

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
Write JSON only to: splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.json \
    --video transcripts/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.json --out splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.qa-split.json \
    --video transcripts/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.validation-report.md

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
video.md: transcripts/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/video.md

--- CHAPTER `00:45` — Background ---
window: 00:45 .. 06:10
recognition_status: multiple (3 items)

ITEM #2
  interviewer_question: time=02:00 text="so the first question that i have for you today is let's say that you work on the ads team had a social media company let's say facebook right and a definition or term that they have in ads is fill rate and it's defined as the number of overall impressions divided by potential opportunities so let's say that you see that this film rate metric has dipped by 10% what would you investigate first"
  candidate_answer: time=02:23 text="i'd want to find out whether that 10% is like relative or you mean like in absolute terms so i guess you know seeing that it's a rate obviously made up of kind of like a numerator and denominator sometimes doesn't tell the full story when you look at it just as a metric by self so the first thing i would do would be to look into like what's going on like what's driving that that that drop in the fill rate so what could be happening is you know the denominator in this case the impression opportunities could be getting a lot bigger which you know my actually signal that a growth in the business so that might be something that that's favorable and simply we just need some time for the numerator to catch up on assuming like you know we're showing ads here so like you advertise yourself to come online yep the other scenario is obviously if the numerator is is the one dropping and we're not seeing any new activity on the denominator then that would be a little bit more of a cause for immediate concern and probably something we want to look into immediately"
  reference_answer: time=None text=None
  interviewer_feedback: time=02:32 text="let's say that it's relative so if you know fillrate was holding 70 percent yeah steady and then let's say it happened it's been steady for like a week and then it dipped down by 10 percent to like 81 percent okay okay"
  question_topic: Product Metrics

ITEM #3
  interviewer_question: time=03:55 text="okay so let's say that it was the denominator that actually increased and then let's clarify and say that this was like specifically like a one-time event so it's not like cyclical so it didn't happen it's not like a weekly thing because you know increased usage on the weekend or something like that like a monthly or yearly thing what would you then look at after that"
  candidate_answer: time=04:25 text="sorry did you say the new denominator oh yeah the denominator increased yeah and it was a one time thing okay yeah i would you know so in this case since its opportunities what might be happening is there's so so two things right like this is a social network so there are people who are coming onto the network to see these potential ads so it's probably unlikely that behavior changed overnight and like you know people are suddenly like engaging like a llama although who knows maybe with you know coronavirus coming around that did happen overnight yeah but it could also be the case that there's a ton of new user activity and like a bunch of new members be from like a like a big marketing push or something that led to a lot of new user signing up so we have a lot of new sessions where they're seeing a couple of these opportunities so i guess the next place that would check would be what's causing that increase in the opportunity number whether it's like a bunch of new members or a bunch of new sections gosh it and"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Product Metrics

ITEM #4
  interviewer_question: time=05:33 text="so is there any other way that you can divide it out even within like the new users or new sessions to understand where i might be coming from given like in this scenario facebook is like a pretty big business so there's probably like a ton of different ways that people can sign up for a you know a facebook account or potentially be using facebook at the time so how else would i break out the increase in sessions you're saying"
  candidate_answer: time=06:04 text="yeah so so let's say let's say we see a lot of new sessions from new members i would obviously look into like like acquisition channels of all these new members and see you know if there's whether one of the theories that i just threw out might be the reason why there are there are new members joining like maybe some i don't know some advertising campaign we're running elsewhere suddenly everyone else stopped bidding on those keywords so now like you know we're just like it getting a lot of new users uh not sure if i'm going down the right track"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Product Metrics

--- CHAPTER `06:10` — Solution ---
window: 06:10 .. конец
recognition_status: multiple (3 items)

ITEM #5
  interviewer_question: time=06:45 text="let's say like we're focusing in on sessions right so let's say that we know that there's a lot more sessions is there a way that we can verify that the sessions are coming from new users as well compared to just existing users using the platform suddenly"
  candidate_answer: time=07:02 text="yeah we would look at you know sessions per user and we would see like and we would compare to the total number of users so like you know sessions could go up but those could come from like a slew of new users or they could be that existing user suddenly are engaging a lot more on that particular date right so i will try to figure out like just take my number of sessions and divide it quickly over my number of distinct users that day and just get a sense of like what that ratio is and i would expect if it were new users that that number would drop right like new years i expect to have less engagement when they first join but and and driven by the figure member base it's increased from engagement in my existing users then i would expect that number to have increased"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Product Metrics

ITEM #6
  interviewer_question: time=07:49 text="okay so let's take a step back and say that let's say the denominator actually in that philaret calculation stayed the same is there something else that you could look at then"
  candidate_answer: time=08:00 text="yeah that would probably point towards the numerator being the problem in which case this is impressions so it may seem like a more dire problem before suddenly showing a lot fewer impressions there's a you know then it then it becomes a matter of like where we're getting advertisers from like if i would start with like you know an ops team and figure out whether some campaigns just ended and if we don't have direct campaigns we have like you know ad exchanges that were cooked into maybe like something broke like check for code that may have potentially like broken the integration yeah yeah but i mean the first step would be to verify that you know impressions actually did drop and i would find a third party source to try to verify that if possible because it could also mean like you know an engineering bug where our impression tracking just broke for example"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Product Metrics

ITEM #7
  interviewer_question: time=08:57 text="gotcha yeah let's say that there wasn't a bug anywhere in the code or anything where we double down that and we see that there was no error technically on where else could be then kind of investigate"
  candidate_answer: time=09:13 text="like i said goes through the business side of things and just trying to figure out like i am i seeing the same number of advertisers throughout the week as i am today like if i see a massive drop like or if i don't even see a massive drop i see that some advertisers were you know kind of doing pretty constant delivery throughout the week and some just dropped off maybe they reached their goal or they move through their budget so then you know they're not delivering anymore so try to find anything that looks abnormal by looking at kind of like a seven-day trend just to see"
  reference_answer: time=None text=None
  interviewer_feedback: time=09:52 text='gotcha okay cool'
  question_topic: Product Metrics

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/interview-query/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06/product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
