<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "data-scientist-senior-uber-coach-datainterview-2022-04-28",
  "transcript_folder": "transcripts/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/",
  "source_id": "data_scientist_senior_uber_coach_datainterview_2022_04_28",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:05:21 +0200",
  "updated_at": "2026-05-20 21:12:45 +0200",
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
    "json": "splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28//timecodes.txt",
        "en",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 21:05:21 +0200"
    },
    {
      "id": 2,
      "name": "qa_extraction",
      "llm": true,
      "model": "claude-sonnet-4-6",
      "inputs": [
        "splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.pipeline-log.md#LLM_INPUT_STEP_2"
      ],
      "outputs": [
        "splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.json"
      ],
      "status": "completed",
      "duration_sec": 180.0,
      "notes": null,
      "finished_at": "2026-05-20 21:12:45 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:12:45 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28//video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 0.0,
      "notes": null,
      "finished_at": "2026-05-20 21:12:45 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/`
- **Source ID:** `data_scientist_senior_uber_coach_datainterview_2022_04_28`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:05:21 +0200
- **Last updated:** 2026-05-20 21:12:45 +0200

Фильтр в IDE: `*data-scientist-senior-uber-coach-datainterview-2022-04-28.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28//timecodes.txt`<br>`en`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.pipeline-log.md` | — | completed |
| 2 | qa_extraction | yes | claude-sonnet-4-6 | `splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.pipeline-log.md#LLM_INPUT_STEP_2` | `splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.json` | 180.0s | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28//video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.validation-report.md` | 0.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.pipeline-log.md`

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
SOURCE_ID: data_scientist_senior_uber_coach_datainterview_2022_04_28
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/
INTERVIEW_LANGUAGE: en
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00] hello emma
[00:01] hi dan
[00:03] hey thanks for enrolling this mock
[00:05] interview video um this is a practice
[00:07] based on uber's technical phone screen
[00:10] for those who are watching uh typically
[00:12] the uber's technical phone screen is
[00:13] about 45 minutes with a senior data
[00:15] scientist or hiring manager in the
[00:17] technical field
[00:18] and
[00:19] um the there's two areas that they will
[00:23] um generally assess for more about like
[00:26] the uber data scientist or product
[00:28] analytic kind of role and it's basically
[00:30] the sql and product sense questions
[00:33] um the entire interview itself at least
[00:36] sql should be about like two to three
[00:37] problems
[00:39] uh in some cases four problems and the
[00:41] product sense questions should be about
[00:42] two three questions
[00:45] but for the sake of this mock interview
[00:47] um
[00:48] you know this is all sort of like a
[00:49] coaching session and so
[00:51] um it is more like a like a sample of
[00:54] what the actual mock interview is going
[00:56] to be like you know obviously it's also
[00:58] youtube video as well and so i won't be
[01:01] asking that many number of questions um
[01:04] probably like one question one or two
[01:06] questions for each area
[01:07] um and along the way
[01:09] um
[01:10] you know i'll provide some hints for the
[01:13] candidate so in terms of whether the
[01:15] interviewers generally provide hints or
[01:17] not
[01:18] that really depends on the interviewers
[01:20] there's a lot of variability with that
[01:22] even within the same company and same
[01:24] team
[01:25] um but for what i do is you know also
[01:28] coaching and so i'm going to be
[01:30] providing some inputs along the way that
[01:32] could be helpful for uma so i'll start
[01:34] with some questions
[01:35] and now in the solutions
[01:38] along with the um feedback
[01:40] um and
[01:42] if you are interested in any of these
[01:44] sort of mock interview videos and
[01:46] courses you know just check out data
[01:48] calm
[01:49] all right so um i have this table in
[01:51] front of me
[01:53] um i've got the right status table the
[01:56] order date the number of orders status
[01:57] of order monthly value and service name
[01:59] okay okay
[02:01] and um using this table i'd like you to
[02:03] address this question which is among the
[02:05] services with the top three highest
[02:06] cancellation rate find the average
[02:08] amount of value and maximum order count
[02:10] across order dates
[02:11] return the service name average monetary
[02:13] value and maximum order count
[02:16] okay so just repeat the question i have
[02:18] to find the top three highest
[02:20] cancellation rates the average monetary
[02:23] value and the maximum order count across
[02:25] the dates and this is something that i
[02:28] have to return that is service name
[02:30] monetary value and this so um
[02:33] my approach to go with this problem is
[02:36] to first figure out
[02:38] what the cancellation rate is so we have
[02:40] number of orders status of order
[02:42] monetary value and service name
[02:44] and we have to find the top
[02:47] highest cancellations rate so um
[02:52] in order to
[02:54] find because we have to output the
[02:56] maximum order count but obviously it's
[02:58] from the cancellation highest
[02:59] cancellation rate so first we have to
[03:02] figure out how are we going to find the
[03:04] cancellation rate
[03:06] um is it correct
[03:09] okay so um
[03:11] and then
[03:13] um as this is the cancellation rate so
[03:16] i'm just writing this according to
[03:19] chunks right now so that i can just draw
[03:21] them in first
[03:23] afterwards combine them is it okay
[03:27] so um to find out the cancellation rate
[03:30] and the
[03:32] obviously we have to average that out
[03:35] so that
[03:39] we can um
[03:42] yeah
[03:43] so let me just go with this so to find
[03:47] the cancellation rate we have to
[03:50] figure out the one that is cancelled
[03:53] within this block so that would be a
[03:56] case statement
[03:59] so um if i just for my own sake right
[04:03] now if i do
[04:04] yes
[04:05] when um
[04:07] order of status
[04:10] um
[04:12] is equal to
[04:15] cancelled
[04:18] then one
[04:20] else
[04:21] zero and
[04:23] and
[04:24] so this could be um
[04:27] all the values and then we have to
[04:29] average them to find the cancellation
[04:31] rate
[04:32] sorry this
[04:33] won't come here
[04:34] so um
[04:35] and i think what you're missing is a
[04:37] zero here
[04:38] sorry yeah
[04:39] i pressed the shift so it went there
[04:42] so
[04:43] yeah and in order to if we create a
[04:46] table for this it would be
[04:48] select
[04:49] um
[04:51] we have to output the services
[04:53] so just
[04:55] another table for this
[04:58] service name
[05:00] and because we have to find the
[05:01] cancellation rate we would obviously
[05:03] have to average this
[05:05] uh what do you mean
[05:08] [Music]
[05:12] to find the cancellation rate so the
[05:14] formula for cancellation rate would be
[05:16] uh the total number of rows within this
[05:20] are divided by the ones that are
[05:22] cancelled right
[05:25] so um this could be
[05:27] uh cancelled
[05:29] so
[05:30] um
[05:31] yeah i'll take this
[05:34] down
[05:36] and um
[05:39] uh sorry this is uh
[05:42] i status
[05:44] and obviously we're using a um an
[05:46] aggregation so we would definitely use a
[05:51] group by here
[05:52] um
[05:56] by
[05:57] one sorry
[06:01] um
[06:02] but um
[06:04] so
[06:05] we also have to figure out a way where
[06:06] we can like
[06:08] have all of them because we have to
[06:10] conquer the cancellation rate and to
[06:13] find the number of rows
[06:15] we would definitely want to use a window
[06:17] function over here
[06:20] so um
[06:23] to do that
[06:24] that window function all of this would
[06:27] be
[06:28] um
[06:30] subcuried within that window function
[06:41] so my whole approach would be finding
[06:43] that as a cancellation rate and then
[06:45] using that within maybe the
[06:49] ct function to figure out
[06:52] obviously
[06:54] all the average values of the one that
[06:56] have the canceled one
[06:58] and then we have to find the maximum
[07:00] count so maximum count um on the um
[07:03] the cancellation rate is it right okay
[07:07] so this would be um
[07:12] if i just write the sub query first to
[07:14] get the cancellation rate it would be
[07:16] select
[07:18] um service name
[07:21] and for
[07:23] for finding out the number of rows i
[07:25] would be
[07:26] using rank
[07:28] okay i can
[07:29] use dense rank as well but it's um it
[07:32] would it would have
[07:35] similar values of the numbers that we
[07:38] don't want
[07:40] uh so um this and
[07:43] if you go rank
[07:48] over and over here as um
[07:51] we have to find the top three so we
[07:54] would order this
[07:56] by
[07:59] um
[08:01] how can we order this
[08:04] we can order this
[08:07] by the cancellation rate
[08:12] yeah let me just so the cancer column is
[08:14] your cancellation rate that you've
[08:16] calculated right
[08:18] yeah so we can we can order that but
[08:20] this cancel right within the sub curie
[08:25] yeah so
[08:26] so
[08:27] yeah so the cancel column is what you
[08:31] would use to order by
[08:32] yeah
[08:34] so this would be cancel and obviously
[08:36] this because we have to find the top
[08:37] three we would use
[08:39] this as a
[08:41] cancel
[08:43] rank
[08:44] and uh now we can like uh
[08:46] because this would be from the sub curry
[08:49] of
[08:50] this
[08:53] so
[08:56] um
[08:57] yeah
[08:59] and then
[09:00] this hole
[09:01] could be and you need a one second so
[09:03] you actually need to name the subquery
[09:05] here so um
[09:07] so you you would whoops
[09:10] just call that
[09:12] sq
[09:13] sub chord
[09:14] okay
[09:15] so and then we would use this hole to
[09:18] find the now we can because now we have
[09:22] as a column we can have the service name
[09:25] rank and then we can use this
[09:28] to find the average value
[09:30] and then the maximum count
[09:34] of the cancellation rate
[09:37] okay
[09:39] um if i do with
[09:42] um
[09:46] [Music]
[09:52] uh i'm not sure do we do we i think we
[09:54] give a name here
[09:56] um
[09:58] you've already given a name
[10:00] so it must have been some time since you
[10:02] actually used with clause but you've
[10:03] already given a name which is ct in this
[10:05] case
[10:07] oh yeah oh yeah that's right yeah so
[10:10] you need to now have an open parenthesis
[10:12] and close parentheses so
[10:14] you've now wrapped this on under the
[10:16] first with clause yeah and now you can
[10:19] reference cte
[10:21] yeah yeah sorry
[10:25] so with this i can um
[10:29] use i can now i have to output we have
[10:33] to output the service name so we can do
[10:35] select
[10:37] uh the service name from here
[10:41] and then now we can calculate the
[10:43] average
[10:44] monetary value so um
[10:47] you go here energy
[10:50] as um
[10:53] which you want
[10:54] and then for um
[10:58] the maximum order count
[11:00] so the
[11:03] maximum order let me just um
[11:06] just complete this and then uh
[11:09] i would come for the
[11:11] this
[11:12] maximum order count so
[11:17] um
[11:18] this would be um
[11:20] obviously from
[11:21] [Music]
[11:24] the right status
[11:32] and then obviously we have to find the
[11:35] top highest three so there would be a
[11:38] where clause where um because we don't
[11:42] know what the services would be so we we
[11:45] can
[11:46] have a sub curry within this
[11:49] so um
[11:51] i i will come back to this max um
[11:54] initially
[11:55] after writing this
[11:56] so
[11:59] service name and then we can use the
[12:03] enclosed to filter um because we use in
[12:06] when we have multiple values and in this
[12:08] case we would be having multiple values
[12:10] for service
[12:11] name it would be select um
[12:14] [Music]
[12:18] select because we're using rare cost but
[12:20] select so this would be
[12:22] select from and now we can get this and
[12:26] then the row rank the rank function
[12:29] because we have to find the maximum
[12:32] ones so it would be from cp
[12:35] where
[12:37] uh this rank value
[12:40] is less than um
[12:44] four because um yeah
[12:47] because it's
[12:49] yeah okay fourth
[12:51] um
[12:52] okay and if we come back to
[12:55] this one
[12:58] so the maximum order count so it would
[13:01] be the
[13:03] max of um
[13:12] maximum order count so the count of the
[13:17] cancelled one right
[13:18] so it would be maybe this it would be
[13:21] the well it would be the number of
[13:23] orders
[13:26] oh it would be the number of products so
[13:28] it would be yes
[13:30] count
[13:32] no so it's the maximum of the number of
[13:35] orders column
[13:39] number orders means order count right
[13:42] oh yeah okay so it would be um
[13:46] so yeah i was thinking that it's
[13:48] yeah related to
[13:50] cancellation right that's the control
[13:52] number i should have asked this earlier
[13:55] well solving
[13:57] [Music]
[13:59] so
[14:02] this could be um max
[14:05] account
[14:07] and if i just go through
[14:11] uh do you think
[14:15] what do you think of this
[14:17] so this is the correct solution there
[14:20] were of course some bumps along the way
[14:21] and i you know provided some hint um but
[14:24] ultimately this is the correct solution
[14:27] um
[14:28] so i just want to provide some inputs
[14:30] here before we proceed to the next
[14:32] section
[14:33] um
[14:34] so
[14:36] it helps to clarify exactly what the
[14:39] output table is um so that you avoid a
[14:42] situation where as you're writing you're
[14:44] not really sure what the what some of
[14:47] the terminology actually means like
[14:48] maximum order count thought it was
[14:50] something else right yeah
[14:52] um
[14:52] so have a clear visual in terms of what
[14:54] that output table looks like by asking
[14:57] clarifying questions
[14:59] um and then proceed with the solution
[15:01] part okay
[15:03] okay um
[15:05] another thing i just want to input there
[15:07] is
[15:08] it helps to
[15:10] so it really depends on
[15:12] you know uh a candidate's response style
[15:15] like some candidate after some
[15:18] question like clarifying questions
[15:20] they'll immediately dive into writing
[15:22] the solution and then explain at the end
[15:25] um that could work
[15:27] um i think a much more effective way to
[15:30] respond to escrow question is once you
[15:32] ask the clarifying questions
[15:34] um jot down the logic so you kind of did
[15:37] it for the case part but then you didn't
[15:39] really do it for the other steps that
[15:41] are required you know basically
[15:42] calculating the
[15:44] um the average and maximum yeah i just
[15:46] wouldn't my word i should have it in it
[15:49] yeah yeah um it just it just helps to
[15:52] just like actually note it on a quarter
[15:54] pad um or whatever
[15:56] um
[15:57] you know um ide they they have you
[16:00] perform sql
[16:02] and just just in general you know just
[16:04] clearly like
[16:05] state things um and then proceed and and
[16:09] that would provide a much more much a
[16:11] better response than just verbally kind
[16:14] of outlining things and then immediately
[16:16] diving into solution
[16:17] yeah you're right
[16:20] all right
[16:21] so
[16:22] let's
[16:23] jump to the next section which is going
[16:25] to be product sense
[16:33] how would you measure the health of uber
[16:38] so
[16:39] the health of uber did you write the
[16:41] question summer okay here yep
[16:44] so
[16:47] okay
[16:48] so um in this case obviously i would um
[16:52] first
[16:54] measure the health of uber
[16:57] so in terms of health do you mean by
[17:00] the
[17:02] number of uh in terms of success do you
[17:05] mean
[17:08] what are your thoughts on that what do
[17:09] you think is a difference or the
[17:10] similarity between health versus success
[17:15] okay
[17:16] so um health can refer to my assumption
[17:20] is that um
[17:22] as the goal for uber is that um transpos
[17:25] to make transportation reliable as a
[17:27] running water and everyone everywhere
[17:29] for ev everyone uh it would definitely
[17:32] in terms of health focus on uh two
[17:34] domains one the
[17:38] the part of
[17:39] the
[17:40] customer and the driver
[17:43] so
[17:45] in terms of measuring the over of our
[17:47] health of
[17:48] the experience within the customer
[17:51] domain and the driver domain
[17:54] so um
[17:55] in terms of that um as i mentioned that
[17:58] the business goal is to create a
[18:00] reliable experience for both of them so
[18:03] do you want me to jot down and go
[18:06] specific within one domain within one of
[18:08] these or as an overall whole
[18:12] why don't we just focus on overall as a
[18:13] whole right now
[18:15] okay
[18:18] so
[18:19] okay so
[18:20] in terms of success um
[18:24] we can refer to the
[18:29] assumptions i can remember we care about
[18:31] health here
[18:32] how because you just said success in
[18:34] terms of success but we care our focus
[18:36] is really health
[18:38] yeah so yeah so um
[18:41] what i can assume here that in terms of
[18:43] health
[18:44] i can specifically refer that um the
[18:48] overall health because because this is a
[18:51] general term health and as i mentioned
[18:54] that it could be the experience within
[18:56] the driver and the
[18:59] um you know customer
[19:01] so
[19:03] what's our audience like
[19:05] who are we going to present this
[19:07] analysis because
[19:10] it can be the stakeholders or it can be
[19:13] maybe measuring it to make a new product
[19:16] to measure the health of to in in order
[19:18] to make a new product that is dependent
[19:20] on the health
[19:22] so
[19:26] okay okay so who do you think are the
[19:28] okay so so um i'll provide like hints
[19:31] along the way to kind of give you some
[19:32] structure um
[19:34] you know because once again this is like
[19:35] mocking every plus sort of coaching but
[19:38] um
[19:39] who do you think
[19:40] who do you think are the the key
[19:42] stakeholders who would consume
[19:45] metrics related to the health of uber
[19:47] yeah definitely this could be um
[19:50] the
[19:52] at the end of the day the investors the
[19:54] executives and as i mentioned uh the
[19:57] various teams that
[20:00] would want to further
[20:02] analyze
[20:03] within their
[20:05] sub modules that are made that they're
[20:07] developing so but most probably the um
[20:11] executives and the
[20:13] investors because
[20:15] they're the ones that are investing
[20:16] money
[20:18] okay um what teams you within uber do
[20:22] you think would care about this
[20:25] so
[20:27] measure the health of uber and the
[20:29] radius teams maybe the marketing team
[20:31] because um the marketing team would be
[20:34] responsible if the the health of uber is
[20:37] going down and the health could be in
[20:39] terms of the customer churn or in terms
[20:42] of um you know
[20:44] the we don't have expected drivers for
[20:48] our specific customers for different
[20:50] regions so definitely the marketing team
[20:53] to boost their marketing strategies
[20:55] so and it can be also the development
[20:58] teams
[20:59] but technically development teams would
[21:01] come after marketing
[21:04] okay so i think we could kind of first i
[21:07] think i think um
[21:08] um so i just want to recap this for
[21:11] cactus for a second because i think we
[21:12] need to go back to the definition of
[21:14] help
[21:15] so um
[21:17] so
[21:18] this is a
[21:20] people often see this as like an
[21:21] interchangeable term health versus
[21:23] success
[21:24] not necessarily
[21:26] um
[21:27] a concrete example is sort of like this
[21:29] um
[21:30] when it comes to like sports players
[21:32] let's just say like
[21:33] you know basketball player right you
[21:35] measure the successful player based on
[21:37] the number of points that they shoot
[21:39] in a game right and the more points they
[21:41] earn
[21:42] the more successful they are so to speak
[21:45] right
[21:47] but then um
[21:48] does that mean that they're healthy
[21:50] what if they have some injuries
[21:52] right
[21:53] so when it comes to health health is
[21:55] more like a 360 degree overview of the
[21:57] uber app as a whole
[21:59] it's not specifically focused on
[22:02] um hey guess what this is a number total
[22:04] number of order uh orders that we had or
[22:06] rides that we had
[22:08] there is a total number of dollars that
[22:10] we have generated health could also mean
[22:13] other attributes we care about as well
[22:16] um satisfaction of
[22:18] uber
[22:19] drivers
[22:21] and writers
[22:23] and the
[22:24] um
[22:25] and some metrics that
[22:27] engineering managers would care about
[22:30] you know like
[22:31] uh the loading time the effectiveness um
[22:35] of the uber app you know is there any
[22:37] erroring you know those sort of things
[22:39] so it's more like a 360 degree overview
[22:41] and
[22:42] i think based on the direction where
[22:44] you're getting at right now i think
[22:46] you're kind of getting the success and
[22:47] the health
[22:48] confused and
[22:50] yeah the audience that you're sort of
[22:51] mentioning are more so if you're talking
[22:54] about investor
[22:55] i think investors
[22:57] they're they don't care too much
[22:59] yeah they care about health but they
[23:00] care more about
[23:02] the bottom line
[23:04] profit yeah
[23:05] and the
[23:06] engagement and the retention the eu
[23:09] those kind of things so they would care
[23:11] a lot more about the
[23:13] uh
[23:14] success
[23:15] and that's really not the focus of the
[23:17] of of this question here okay so we care
[23:20] about so executives will obviously care
[23:22] about the health of uber right
[23:24] so when we're talking about executive
[23:25] team we're talking about like the vp's
[23:28] you know the ceo the ceo the cto right
[23:32] um
[23:34] cmo perhaps um but i think cmos would
[23:37] generally care more about the growth
[23:40] um which is another question as well how
[23:42] would you measure the growth of uber how
[23:43] was your measure as a successful uber
[23:45] how was your method the health over
[23:47] stay all seems similar but they're not
[23:48] really the same there's differences
[23:52] um so you want to be very precise when
[23:53] it comes to those products and sort of
[23:55] things
[23:56] okay so
[23:57] in terms of yeah go ahead
[23:59] yeah i just want to finish my thought
[24:00] and then i'll
[24:02] let you pick things up so executives yes
[24:05] uh investors marketing teams scratch
[24:08] that out
[24:09] um
[24:10] product managers
[24:12] um
[24:13] and
[24:14] engineering managers
[24:19] okay
[24:20] okay so those are the stakeholders
[24:23] um
[24:24] now
[24:26] what you're also sort of missing in the
[24:28] beginning part
[24:30] is
[24:31] a walkthrough of the uber app don't just
[24:33] assume
[24:34] that the interviewer knows
[24:37] that you understand the app so walk
[24:39] through the overall user experience
[24:40] because i think that's going to help you
[24:41] define metrics
[24:43] yeah so after assumptions i was about to
[24:45] go there oh okay all right go ahead
[24:48] so um do you want me to start over or
[24:51] no keep going okay so um so yeah as you
[24:55] mentioned um
[24:57] the health could be
[24:59] not for investors marketing teams and
[25:01] product managers that would be
[25:04] looking for um initial improvement
[25:07] within the health and of the app
[25:10] and just to
[25:12] jot down the overall user journey of how
[25:16] people can um of how uh that the team
[25:19] can measure successes if you log into
[25:21] app into the app the
[25:24] if you're a first time user you
[25:25] obviously have to sign up and
[25:28] um
[25:30] we can mention
[25:33] that as
[25:36] yeah so the overall
[25:38] user journey would be how user uses the
[25:41] product so if you specifically focus on
[25:44] customers they log in and is there any
[25:47] glitch when they're signing up it does
[25:49] the um
[25:51] opt or
[25:52] any uh sign up verification
[25:55] comes on time
[25:57] or not and if if that's that's a problem
[26:00] any loading time everything because uber
[26:04] is a
[26:05] real time application so there should be
[26:08] low latency for the application
[26:12] in terms of real-time and um
[26:15] apart from that we have to figure out
[26:18] when the user steps in even as a
[26:20] first-time user or a regular user how
[26:23] much time does it take to for a customer
[26:27] to
[26:28] to get to do the app or
[26:31] so sorry to get to the drivers um if
[26:34] he's going for obviously for
[26:37] using the app
[26:40] and
[26:41] uh times for driver weight that's the
[26:43] estimated um
[26:45] arrival time for drivers and we can
[26:48] obviously measure that and figure out
[26:50] whether our
[26:53] whole app is in terms of
[26:56] getting the right results and is healthy
[26:59] or not
[27:00] apart from that we can um we also have
[27:03] to figure out when the user logs in as a
[27:05] driver or a customer um the first thing
[27:08] he does is
[27:10] uh enters on the map uh the destination
[27:13] where he wants to go and if that
[27:17] towards that destination what's the
[27:18] estimated time he's getting he or she is
[27:21] getting and
[27:24] if that is long enough then uh probably
[27:29] they would not um use the app if the
[27:32] estimated time
[27:35] is
[27:36] long
[27:37] wait for the drivers
[27:39] so
[27:40] and in terms of health as well
[27:44] if we focus just on that um
[27:49] do you want me to focus on this specific
[27:52] um
[27:53] portion of these
[27:55] no it's okay um is
[27:57] um is there any other metrics you want
[27:59] to cover when it comes to the health of
[28:00] uber
[28:03] uh i think the main metrics would be the
[28:05] estimated um
[28:07] time of arrival and the maybe the number
[28:10] of in terms of health we're not just
[28:12] focusing on the as you said the success
[28:15] of a one-to-one customer and driver
[28:17] experience we obviously want to focus on
[28:19] maybe the
[28:21] number of crashes or the bugs that the
[28:23] app faces in the production as well is
[28:26] there any and um
[28:30] but the final metrics i booked that
[28:33] would
[28:34] figure out the whole experience of uber
[28:37] would be
[28:38] the essential um the estimated time
[28:41] because uber's mission is to make
[28:43] transportation reliable and running
[28:47] okay got it all right so
[28:51] um
[28:53] let me
[28:54] kind of give you some feedback and like
[28:56] you know
[28:57] we can walk through the solution
[28:58] solution together
[29:00] um
[29:00] so
[29:03] what's there's two elements that you're
[29:05] sort of missing in your metric response
[29:08] one
[29:09] um
[29:11] you didn't really spec
[29:13] your definition of a metric here in this
[29:16] case is actually somewhat incomplete and
[29:18] i'll talk about it in a second what i
[29:20] mean by that
[29:21] the second aspect is
[29:23] that
[29:25] you want to think about certain themes
[29:28] um and then think about
[29:30] two to three metrics that really define
[29:33] that theme
[29:34] um that's a that's a strategy that you
[29:36] can use when it comes to define like
[29:38] listing metrics very quickly but also
[29:40] even machine learning interviews as well
[29:42] where you have to like come up with you
[29:43] know
[29:44] uh
[29:45] features based on raw data
[29:48] so let me first of all talk about the
[29:51] first aspect
[29:53] um you mentioned
[29:56] let's see
[30:00] time for driver's weight
[30:03] when you're saying time for driver's
[30:04] weight
[30:06] uh of time
[30:08] time it takes for
[30:11] basically driver wait time right yeah
[30:13] and how much time
[30:15] a driver um wait how many
[30:18] customers does it get per day
[30:20] like yeah
[30:23] okay got it so so the
[30:26] in between time between
[30:29] rides provided to customers right
[30:32] yeah
[30:33] now
[30:34] when you just say that
[30:36] that's just a distribution but
[30:38] what are we really talking about here do
[30:40] we talk are we talking about the median
[30:42] the mean the sum
[30:44] oh the aggregation yeah
[30:47] you know what i mean so
[30:49] the average um
[30:51] when and this is a very common mistake
[30:54] um i mean
[30:55] you know at by this point i've worked
[30:56] with like over 100 clients
[31:00] but um
[31:01] what's commonly missing is that
[31:04] when it comes to defining a metric
[31:06] you need to have what is the statistical
[31:09] function or the aggregation in this case
[31:13] yeah okay count sum
[31:16] average right
[31:19] the other element is that you need to
[31:21] define what the action you did define
[31:23] what the actions are what you're trying
[31:24] to measure here
[31:27] the other aspect is the unit of analysis
[31:33] time for drivers wait
[31:35] over the lifetime
[31:37] that we have collected data about the
[31:39] driver or are we talking about on a per
[31:41] day because this is a time series thing
[31:45] yeah
[31:47] so definitely um
[31:50] we should
[31:52] measure it over
[31:53] um maybe a
[31:55] wee car per
[31:57] per day yeah
[32:02] so
[32:03] so you need to have these three elements
[32:05] in order to have a complete metric okay
[32:08] yeah
[32:09] all right now second aspect
[32:12] is it sometimes it's like it's a little
[32:16] bit of struggle so when it when it comes
[32:17] to like this open-ended like business
[32:20] problem
[32:21] it's really about thinking about
[32:23] um how can you provide a structural
[32:26] response and how are you going about
[32:27] doing that
[32:28] use frameworks
[32:30] so when it comes to measuring the
[32:32] quote-unquote health of any product
[32:36] one of the best frameworks you could use
[32:38] is something called the heart
[32:41] and i'm not sure if you're familiar with
[32:43] that but heart is a metric framework
[32:45] that
[32:46] um
[32:47] google's
[32:48] um
[32:49] product team have a ux researchers have
[32:52] proposed
[32:53] and various teams within google use this
[32:55] metric as a way to define the overall
[32:58] um
[32:59] you know health of
[33:01] google's apps okay
[33:03] and heart stands for the following so
[33:05] age is basically happiness
[33:09] and happiness is
[33:10] you know satisfaction okay
[33:13] e stands for engagement
[33:16] a stands for adoption
[33:19] or acquisition
[33:22] r stands for retention
[33:25] task t stands for task success
[33:31] okay
[33:32] so how do you think we could measure
[33:34] happiness
[33:36] of of users on uber
[33:39] what is the most what is the best way to
[33:41] measure that
[33:44] the for if you talk about per user the
[33:47] number of times or the number of times
[33:49] he has taken the rights
[33:52] so i think that would more be focused on
[33:55] engagement
[33:56] because we're talking about like actions
[33:57] and stuff like that so this is more
[33:59] about user sentiment right they're
[34:01] feeling
[34:04] then if they're happy obviously they
[34:06] would refer to someone the app
[34:10] yeah they could um
[34:12] what about surveys
[34:14] no
[34:15] satisfaction scores right
[34:23] okay so what about um engagement what
[34:25] metrics do we care about here
[34:28] so the percentage of users that have
[34:30] actually used the app the number of
[34:32] times
[34:33] per day
[34:36] yeah more or less um but we we we really
[34:40] care about the big number here the
[34:42] really the big picture the overall
[34:43] health right yeah
[34:45] um
[34:47] so
[34:48] what is the main function what is the
[34:50] main action on uber app
[34:53] uh having a ride so the number of rides
[34:56] yes yes exactly right
[34:58] this is a type of number that would
[35:00] probably show up on uber's um you know
[35:02] 10ks and 10qs yeah right
[35:05] so the number of rides
[35:07] total number of rides
[35:09] um over what unit of analysis
[35:13] so um
[35:15] total number of friends think about the
[35:16] big picture think about think about the
[35:18] big picture like okay this you know it's
[35:20] like the uber ceo
[35:22] you know on a annual conference call
[35:25] saying hey you know this is what we have
[35:27] achieved this year
[35:28] you know what would he say
[35:30] then obviously maybe uh
[35:33] quarterly or yearly
[35:36] yes
[35:38] um and we could also just say okay per
[35:42] day week month quarter a year yeah
[35:45] okay
[35:46] um
[35:48] you know
[35:49] of course like you want to sort of
[35:50] refine it based on the use case you know
[35:52] like if we're talking about av
[35:54] experiment you probably want to look at
[35:55] them more like on a daily basis
[35:57] right
[35:58] um but we're talking about the overall
[36:00] health and you looking at across day
[36:02] week month and quarter and year
[36:05] um depending on what is a business
[36:08] strategy we're focused on will have a
[36:10] different purpose
[36:12] yes um
[36:13] okay
[36:15] what about adoption
[36:18] so um adoption is how
[36:20] much users can we get i know about
[36:23] acquisition it's like how many because i
[36:26] know about the funnel so
[36:28] acquisition is the first step where how
[36:31] many users were
[36:33] registered
[36:34] to the app number of signups
[36:38] and in terms of um adoption
[36:42] yeah i'm confused about adoption
[36:46] so it's similar it's it's it's just it's
[36:48] um synonymous
[36:50] okay
[36:51] so out of the new visitors how many
[36:53] ended up using the app
[36:55] yeah
[36:56] okay um and you can kind of refine it
[36:58] into two-step procedure so
[37:00] um you visit the app
[37:03] um
[37:04] you know and you you download it
[37:07] right uh you sign in
[37:09] or you sign up
[37:11] and then you take the first ride so
[37:13] actually like it's like a three step
[37:14] sort of thing right yeah so you can
[37:17] think about it as like a download rate
[37:19] sign up rate first ride rate does that
[37:22] make sense yeah
[37:24] um but again
[37:26] we're not
[37:27] we're not really done we haven't really
[37:29] completed what that actually like what
[37:31] the unit of analysis is so are we
[37:33] talking about
[37:34] per day per week per month
[37:37] yeah or are we talking a light time
[37:41] so sign up would be different for every
[37:43] user but then an average sign up per
[37:45] week per day
[37:47] the number of signups we get
[37:51] so yeah sign and effort sign up
[37:54] for
[37:54] [Music]
[37:56] because today is something that that
[37:58] that won't be feasible so maybe week or
[38:02] month
[38:05] okay
[38:11] maybe we can do quarterly and a year as
[38:13] well so but because if if this is
[38:16] something it depends on the business
[38:18] metrics as well that like business
[38:20] evaluation so if this is an annual
[38:22] evaluation you would definitely want to
[38:25] be back and forth and check it check
[38:27] quarterly because there's this effect of
[38:29] seasonality or any external effects as
[38:32] well that can uh you know reduce or
[38:34] increase our uh sign up or any other
[38:37] engagement as well
[38:38] yeah
[38:40] yeah
[38:41] yeah so definitely weekly weekly because
[38:44] um maybe people want to travel on
[38:48] weekends and as well so that's why
[38:49] weekly is something that we should go to
[38:52] yep
[38:54] yep that's fine um okay so what about
[38:56] retention
[38:58] so um in terms of retention it's like
[39:00] the
[39:01] uh maybe the churn rate
[39:05] because we so that's a component of it
[39:07] but i think we have a better way to
[39:08] capture
[39:09] turn rate there's a more of a top-down
[39:11] top
[39:12] uh metric that
[39:14] um
[39:16] captures the meaning of churn as well
[39:18] but also focus on users and recurrent
[39:21] users so what is that
[39:26] um deu
[39:30] daily active user yeah okay yeah
[39:34] um
[39:35] what else
[39:38] but on a different time window
[39:41] yeah so definitely uh
[39:44] the because if if it's if we measure per
[39:47] day we would be having more people using
[39:50] it in the morning in office times
[39:59] right
[40:00] sorry uh that we got you got cut off for
[40:03] a second so deu and what else what else
[40:05] should we be using
[40:06] um
[40:07] so
[40:08] retention in terms of daily active uses
[40:11] and maybe if we check per day the number
[40:14] of times that the user uses the app so
[40:16] because we would be having a high
[40:18] retention in the morning
[40:19] so i'd say we could perhaps capture that
[40:22] in engagement
[40:24] okay um but um so we so more like
[40:29] weekly active user
[40:31] okay
[40:33] and nau multi-octave user
[40:37] okay okay so those are the common set of
[40:39] retention metrics
[40:44] um and what about for task success so
[40:46] task success is like the type of excuse
[40:48] type of metrics that the engineering
[40:49] managers would care about you you have
[40:51] noticed that you listed some aspect of
[40:53] these
[40:55] so what are those
[40:56] so success is success would be
[40:59] um
[41:01] obviously the time or the average
[41:04] estimated time eta of maybe a
[41:08] okay
[41:10] the
[41:13] yeah
[41:14] average time for um
[41:17] because this this one's tricky we can do
[41:19] it um
[41:20] per customer as well per driver or an
[41:23] overall
[41:26] i'd say i'd say we can think about it
[41:28] more on the um
[41:31] more on the overall level if you were
[41:34] thinking about it at the user level then
[41:36] you would need to average it sort of
[41:37] thing
[41:38] yeah or maybe this could be
[41:41] more specific to regional and location
[41:43] as well
[41:46] yeah you could do it by a segment but
[41:48] you know but let's just get the big
[41:49] picture here okay
[41:52] um so
[41:54] um and one thing i want to mention is
[41:55] that when it comes to past success you
[41:57] want to
[41:58] you want to think about efficiency so
[42:00] eta is an efficiency score um and
[42:02] effectiveness
[42:04] how successfully are you providing a
[42:05] ride right so that's one aspect that you
[42:07] can think about but the other aspect you
[42:09] can think about is like aerate bugs
[42:11] glitches
[42:13] and when someone opens the app
[42:15] out of all the app opens
[42:18] um what percentage of them did you uh
[42:21] what did the app open up without any
[42:23] bugs
[42:24] yeah this is
[42:27] right
[42:29] um so do you get the picture of what
[42:31] this heart metric is and
[42:33] and why we should be using heart to
[42:35] measure health
[42:37] yes definitely
[42:39] yeah i wasn't close towards the success
[42:41] side so i was just yeah
[42:43] it's a it's a it's a common it's a
[42:45] common mistake um
[42:47] you know people
[42:49] um you know all to sort of interchange
[42:52] growth success and health
[42:55] um
[42:56] they have some similar attributes but
[42:58] there are also differences as well
[43:01] um
[43:02] and interviewers are looking for
[43:05] for that like do you clearly understand
[43:08] the term
[43:09] and and know what are they appropriate
[43:12] attributes to
[43:13] explain
[43:15] explain that
[43:16] um
[43:17] so
[43:19] uh so this this should provide a much
[43:21] more um you know much
[43:23] a better response um when it comes to a
[43:25] question like this
[43:27] measured for like we can maybe we can
[43:30] use the aar
[43:32] metrics for that yeah so arg
[43:35] um so arg is another popular framework
[43:38] um i would actually argue
[43:41] that
[43:42] our
[43:43] it's a funnel metric right so it's like
[43:46] from the beginning to the end it follows
[43:48] some sort of like a chronological manner
[43:50] yeah um
[43:52] the problem in our arg is that it
[43:55] overlooks um two aspects that matter a
[43:58] lot which is
[43:59] satisfaction user satisfaction
[44:01] and also task success
[44:04] because none of the r dimension would
[44:07] have that so i wouldn't i wouldn't use
[44:09] arg in this case i would use arg
[44:11] um for
[44:12] measuring success
[44:15] um
[44:17] and even with you know when you're
[44:18] measuring success i wouldn't use the
[44:20] entire all like all five of them that's
[44:23] just way too exhausted that shows that
[44:24] you're not being discriminatory
[44:26] so
[44:27] maybe when it comes to measuring success
[44:30] i would focus on
[44:31] definitely engagement
[44:34] and and to be frank like i wouldn't even
[44:36] say like i'm going to use i'm going to
[44:37] use exactly the dimensions mentors like
[44:40] typically what i do is um when it comes
[44:42] to measuring success i talk about
[44:44] metrics related to growth
[44:46] engagement
[44:48] and monetization
[44:50] okay um so those are the three
[44:52] dimensions that we'll talk about when it
[44:53] comes to us
[44:55] um all right so
[44:57] you know
[44:58] this uh for for the people who are
[45:00] watching this um
[45:02] you know
[45:03] uh obviously there was a lot of like
[45:05] back and forth uh for the sql and
[45:07] product sets
[45:08] uh but this is really designed to you
[45:11] know first of all
[45:13] help
[45:14] um you know give you the extra practice
[45:16] that you need in order to prepare for
[45:18] whatever data science interview you have
[45:20] but also give you a glimpse of what is
[45:23] the type of coaching session um
[45:25] you know that i'm providing
[45:27] um and uma is
[45:30] you know she's relatively new in the
[45:32] interview
[45:33] prep space so obviously there's some
[45:35] uh
[45:37] basics and fundamentals that that she
[45:39] was having a hard time kind of going
[45:41] through but it's my job as a coach to
[45:43] spot those and help
[45:45] elevate and level up her interviewing
[45:48] skills
[45:49] so if you need any help with your
[45:52] upcoming interview make sure you check
[45:54] out data.com and reach out to me on my
[45:57] email dan at datantv.com once again it's
[46:00] dan at data tv.com
[46:03] and i hope you found this video helpful
[46:06] if you have any questions just leave a
[46:07] comment below
[46:09] and i'll see you in my next video next
[46:11] week
[46:12] thank you bye

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
Write JSON only to: splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.json \
    --video transcripts/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28//video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.json --out splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.qa-split.json \
    --video transcripts/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28//video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.validation-report.md

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
video.md: transcripts/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/video.md

--- CHAPTER `01:45` — SQL ---
window: 01:45 .. 16:23
recognition_status: single (1 items)

ITEM #1
  interviewer_question: time=02:01 text="and um using this table i'd like you to address this question which is among the services with the top three highest cancellation rate find the average amount of value and maximum order count across order dates return the service name average monetary value and maximum order count"
  candidate_answer: time=02:16 text="okay so just repeat the question i have to find the top three highest cancellation rates the average monetary value and the maximum order count across the dates and this is something that i have to return that is service name monetary value and this so um my approach to go with this problem is to first figure out what the cancellation rate is so we have number of orders status of order monetary value and service name and we have to find the top highest cancellations rate so um in order to find because we have to output the maximum order count but obviously it's from the cancellation highest cancellation rate so first we have to figure out how are we going to find the cancellation rate um is it correct okay so um and then um as this is the cancellation rate so i'm just writing this according to chunks right now so that i can just draw them in first afterwards combine them is it okay so um to find out the cancellation rate and the obviously we have to average that out so that we can um yeah so let me just go with this so to find the cancellation rate we have to figure out the one that is cancelled within this block so that would be a case statement so um if i just for my own sake right now if i do yes when um order of status um is equal to cancelled then one else zero and and so this could be um all the values and then we have to average them to find the cancellation rate sorry this won't come here so um zero here sorry yeah i pressed the shift so it went there so yeah and in order to if we create a table for this it would be select um we have to output the services so just another table for this service name and because we have to find the cancellation rate we would obviously have to average this to find the cancellation rate so the formula for cancellation rate would be uh the total number of rows within this are divided by the ones that are cancelled right so um this could be uh cancelled so um yeah i'll take this down and um uh sorry this is uh i status and obviously we're using a um an aggregation so we would definitely use a group by here um by one sorry um but um so we also have to figure out a way where we can like have all of them because we have to conquer the cancellation rate and to find the number of rows we would definitely want to use a window function over here so um to do that that window function all of this would be um subcuried within that window function so my whole approach would be finding that as a cancellation rate and then using that within maybe the ct function to figure out obviously all the average values of the one that have the canceled one and then we have to find the maximum count so maximum count um on the um the cancellation rate is it right okay so this would be um if i just write the sub query first to get the cancellation rate it would be select um service name and for for finding out the number of rows i would be using rank okay i can use dense rank as well but it's um it would it would have similar values of the numbers that we don't want uh so um this and if you go rank over and over here as um we have to find the top three so we would order this by um how can we order this we can order this by the cancellation rate your cancellation rate that you've calculated right yeah so we can we can order that but this cancel right within the sub curie yeah so so would use to order by yeah so this would be cancel and obviously this because we have to find the top three we would use this as a cancel rank and uh now we can like uh because this would be from the sub curry of this so um yeah and then this hole could be and you need a one second so here so um so you you would whoops just call that sq sub chord okay so and then we would use this hole to find the now we can because now we have as a column we can have the service name rank and then we can use this to find the average value and then the maximum count of the cancellation rate okay um if i do with um uh i'm not sure do we do we i think we give a name here um actually used with clause but you've already given a name which is ct in this case oh yeah oh yeah that's right yeah so and close parentheses so you've now wrapped this on under the first with clause yeah and now you can reference cte yeah yeah sorry so with this i can um use i can now i have to output we have to output the service name so we can do select uh the service name from here and then now we can calculate the average monetary value so um you go here energy as um which you want and then for um the maximum order count so the maximum order let me just um just complete this and then uh i would come for the this maximum order count so um this would be um obviously from the right status and then obviously we have to find the top highest three so there would be a where clause where um because we don't know what the services would be so we we can have a sub curry within this so um i i will come back to this max um initially after writing this so service name and then we can use the enclosed to filter um because we use in when we have multiple values and in this case we would be having multiple values for service name it would be select um select because we're using rare cost but select so this would be select from and now we can get this and then the row rank the rank function because we have to find the maximum ones so it would be from cp where uh this rank value is less than um four because um yeah because it's yeah okay fourth um okay and if we come back to this one so the maximum order count so it would be the max of um maximum order count so the count of the cancelled one right so it would be maybe this it would be the well it would be the number of orders oh it would be the number of products so it would be yes count orders column oh yeah okay so it would be um so yeah i was thinking that it's yeah related to cancellation right that's the control number i should have asked this earlier well solving so this could be um max account and if i just go through uh do you think yeah you're right all right"
  reference_answer: time=None text=None
  interviewer_feedback: time=14:17 text="so this is the correct solution there were of course some bumps along the way and i you know provided some hint um but ultimately this is the correct solution um so i just want to provide some inputs here before we proceed to the next section um so it helps to clarify exactly what the output table is um so that you avoid a situation where as you're writing you're not really sure what the what some of the terminology actually means like maximum order count thought it was something else right yeah um so have a clear visual in terms of what that output table looks like by asking clarifying questions um and then proceed with the solution part okay okay um another thing i just want to input there is it helps to so it really depends on you know uh a candidate's response style like some candidate after some question like clarifying questions they'll immediately dive into writing the solution and then explain at the end um that could work um i think a much more effective way to respond to escrow question is once you ask the clarifying questions um jot down the logic so you kind of did it for the case part but then you didn't really do it for the other steps that are required you know basically calculating the um the average and maximum yeah i just wouldn't my word i should have it in it yeah yeah um it just it just helps to just like actually note it on a quarter pad um or whatever um you know um ide they they have you perform sql and just just in general you know just clearly like state things um and then proceed and and that would provide a much more much a better response than just verbally kind of outlining things and then immediately diving into solution"
  question_topic: SQL

--- CHAPTER `16:23` — Product Sense ---
window: 16:23 .. конец
recognition_status: multiple (12 items)

ITEM #2
  interviewer_question: time=16:33 text='how would you measure the health of uber so'
  candidate_answer: time=16:48 text='so um in this case obviously i would um first measure the health of uber so in terms of health do you mean by the number of uh in terms of success do you mean'
  reference_answer: time=None text=None
  interviewer_feedback: time=16:39 text='the health of uber did you write the question summer okay here yep so okay'
  question_topic: Product Metrics

ITEM #3
  interviewer_question: time=17:08 text='what are your thoughts on that what do you think is a difference or the similarity between health versus success'
  candidate_answer: time=17:16 text='so um health can refer to my assumption is that um as the goal for uber is that um transpos to make transportation reliable as a running water and everyone everywhere for ev everyone uh it would definitely in terms of health focus on uh two domains one the the part of the customer and the driver so in terms of measuring the over of our health of the experience within the customer domain and the driver domain so um in terms of that um as i mentioned that the business goal is to create a reliable experience for both of them so do you want me to jot down and go specific within one domain within one of these or as an overall whole'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Product Metrics

ITEM #4
  interviewer_question: time=18:12 text="why don't we just focus on overall as a whole right now"
  candidate_answer: time=18:18 text="so okay so in terms of success um we can refer to the assumptions i can remember we care about health here how because you just said success in terms of success but we care our focus is really health yeah so yeah so um what i can assume here that in terms of health i can specifically refer that um the overall health because because this is a general term health and as i mentioned that it could be the experience within the driver and the um you know customer so what's our audience like who are we going to present this analysis because it can be the stakeholders or it can be maybe measuring it to make a new product to measure the health of to in in order to make a new product that is dependent on the health so"
  reference_answer: time=None text=None
  interviewer_feedback: time=18:32 text='how because you just said success in terms of success but we care our focus is really health yeah so yeah so um'
  question_topic: Product Metrics

ITEM #5
  interviewer_question: time=19:39 text='who do you think who do you think are the the key stakeholders who would consume metrics related to the health of uber'
  candidate_answer: time=19:47 text="yeah definitely this could be um the at the end of the day the investors the executives and as i mentioned uh the various teams that would want to further analyze within their sub modules that are made that they're developing so but most probably the um executives and the investors because they're the ones that are investing money"
  reference_answer: time=None text=None
  interviewer_feedback: time=19:26 text="okay okay so who do you think are the okay so so um i'll provide like hints along the way to kind of give you some structure um you know because once again this is like mocking every plus sort of coaching but um"
  question_topic: Stakeholder Management

ITEM #6
  interviewer_question: time=20:18 text='okay um what teams you within uber do you think would care about this'
  candidate_answer: time=20:25 text="so measure the health of uber and the radius teams maybe the marketing team because um the marketing team would be responsible if the the health of uber is going down and the health could be in terms of the customer churn or in terms of um you know the we don't have expected drivers for our specific customers for different regions so definitely the marketing team to boost their marketing strategies so and it can be also the development teams but technically development teams would come after marketing"
  reference_answer: time=None text=None
  interviewer_feedback: time=21:04 text="okay so i think we could kind of first i think i think um um so i just want to recap this for cactus for a second because i think we need to go back to the definition of help so um so this is a people often see this as like an interchangeable term health versus success not necessarily um a concrete example is sort of like this um when it comes to like sports players let's just say like you know basketball player right you measure the successful player based on the number of points that they shoot in a game right and the more points they earn the more successful they are so to speak right but then um does that mean that they're healthy what if they have some injuries right so when it comes to health health is more like a 360 degree overview of the uber app as a whole it's not specifically focused on um hey guess what this is a number total number of order uh orders that we had or rides that we had there is a total number of dollars that we have generated health could also mean other attributes we care about as well um satisfaction of uber drivers and writers and the um and some metrics that engineering managers would care about you know like uh the loading time the effectiveness um of the uber app you know is there any erroring you know those sort of things so it's more like a 360 degree overview and i think based on the direction where you're getting at right now i think you're kind of getting the success and the health confused and yeah the audience that you're sort of mentioning are more so if you're talking about investor i think investors they're they don't care too much yeah they care about health but they care more about the bottom line profit yeah and the engagement and the retention the eu those kind of things so they would care a lot more about the uh success and that's really not the focus of the of of this question here okay so we care about so executives will obviously care about the health of uber right so when we're talking about executive team we're talking about like the vp's you know the ceo the ceo the cto right um cmo perhaps um but i think cmos would generally care more about the growth um which is another question as well how would you measure the growth of uber how was your measure as a successful uber how was your method the health over stay all seems similar but they're not really the same there's differences um so you want to be very precise when it comes to those products and sort of things okay so in terms of yeah go ahead yeah i just want to finish my thought and then i'll let you pick things up so executives yes uh investors marketing teams scratch that out um product managers um and engineering managers okay okay so those are the stakeholders um now"
  question_topic: Stakeholder Management

ITEM #7
  interviewer_question: time=24:26 text="what you're also sort of missing in the beginning part is a walkthrough of the uber app don't just assume that the interviewer knows that you understand the app so walk through the overall user experience because i think that's going to help you define metrics"
  candidate_answer: time=24:51 text="no keep going okay so um so yeah as you mentioned um the health could be not for investors marketing teams and product managers that would be looking for um initial improvement within the health and of the app and just to jot down the overall user journey of how people can um of how uh that the team can measure successes if you log into app into the app the if you're a first time user you obviously have to sign up and um we can mention that as yeah so the overall user journey would be how user uses the product so if you specifically focus on customers they log in and is there any glitch when they're signing up it does the um opt or any uh sign up verification comes on time or not and if if that's that's a problem any loading time everything because uber is a real time application so there should be low latency for the application in terms of real-time and um apart from that we have to figure out when the user steps in even as a first-time user or a regular user how much time does it take to for a customer to to get to do the app or so sorry to get to the drivers um if he's going for obviously for using the app and uh times for driver weight that's the estimated um arrival time for drivers and we can obviously measure that and figure out whether our whole app is in terms of getting the right results and is healthy or not apart from that we can um we also have to figure out when the user logs in as a driver or a customer um the first thing he does is uh enters on the map uh the destination where he wants to go and if that towards that destination what's the estimated time he's getting he or she is getting and if that is long enough then uh probably they would not um use the app if the estimated time is long wait for the drivers so and in terms of health as well if we focus just on that um do you want me to focus on this specific um portion of these no it's okay um is"
  reference_answer: time=None text=None
  interviewer_feedback: time=24:43 text='yeah so after assumptions i was about to go there oh okay all right go ahead so um do you want me to start over or'
  question_topic: Product Metrics

ITEM #8
  interviewer_question: time=27:57 text='um is there any other metrics you want to cover when it comes to the health of uber'
  candidate_answer: time=28:03 text="uh i think the main metrics would be the estimated um time of arrival and the maybe the number of in terms of health we're not just focusing on the as you said the success of a one-to-one customer and driver experience we obviously want to focus on maybe the number of crashes or the bugs that the app faces in the production as well is there any and um but the final metrics i booked that would figure out the whole experience of uber would be the essential um the estimated time because uber's mission is to make transportation reliable and running"
  reference_answer: time=None text=None
  interviewer_feedback: time=28:51 text="um let me kind of give you some feedback and like you know we can walk through the solution solution together um so what's there's two elements that you're sort of missing in your metric response one um you didn't really spec your definition of a metric here in this case is actually somewhat incomplete and i'll talk about it in a second what i mean by that the second aspect is that you want to think about certain themes um and then think about two to three metrics that really define that theme um that's a that's a strategy that you can use when it comes to define like listing metrics very quickly but also even machine learning interviews as well where you have to like come up with you know uh features based on raw data so let me first of all talk about the first aspect um you mentioned let's see time for driver's weight when you're saying time for driver's weight uh of time time it takes for basically driver wait time right yeah and how much time a driver um wait how many customers does it get per day like yeah okay got it so so the in between time between rides provided to customers right yeah now when you just say that that's just a distribution but what are we really talking about here do we talk are we talking about the median the mean the sum oh the aggregation yeah you know what i mean so the average um when and this is a very common mistake um i mean you know at by this point i've worked with like over 100 clients but um what's commonly missing is that when it comes to defining a metric you need to have what is the statistical function or the aggregation in this case yeah okay count sum average right the other element is that you need to define what the action you did define what the actions are what you're trying to measure here the other aspect is the unit of analysis time for drivers wait over the lifetime that we have collected data about the driver or are we talking about on a per day because this is a time series thing yeah so definitely um we should measure it over um maybe a wee car per per day yeah so so you need to have these three elements in order to have a complete metric okay yeah all right now second aspect is it sometimes it's like it's a little bit of struggle so when it when it comes to like this open-ended like business problem it's really about thinking about um how can you provide a structural response and how are you going about doing that use frameworks so when it comes to measuring the quote-unquote health of any product one of the best frameworks you could use is something called the heart and i'm not sure if you're familiar with that but heart is a metric framework that um google's um product team have a ux researchers have proposed and various teams within google use this metric as a way to define the overall um you know health of google's apps okay and heart stands for the following so age is basically happiness and happiness is you know satisfaction okay e stands for engagement a stands for adoption or acquisition r stands for retention task t stands for task success okay"
  question_topic: Product Metrics

ITEM #9
  interviewer_question: time=33:32 text='so how do you think we could measure happiness of of users on uber what is the most what is the best way to measure that'
  candidate_answer: time=33:44 text="the for if you talk about per user the number of times or the number of times he has taken the rights so i think that would more be focused on engagement because we're talking about like actions and stuff like that so this is more about user sentiment right they're feeling then if they're happy obviously they would refer to someone the app yeah they could um"
  reference_answer: time=None text=None
  interviewer_feedback: time=33:56 text="because we're talking about like actions and stuff like that so this is more about user sentiment right they're feeling then if they're happy obviously they would refer to someone the app yeah they could um what about surveys no satisfaction scores right"
  question_topic: Product Metrics

ITEM #10
  interviewer_question: time=34:23 text='okay so what about um engagement what metrics do we care about here'
  candidate_answer: time=34:28 text='so the percentage of users that have actually used the app the number of times per day'
  reference_answer: time=None text=None
  interviewer_feedback: time=34:36 text="yeah more or less um but we we we really care about the big number here the really the big picture the overall health right yeah um so what is the main function what is the main action on uber app uh having a ride so the number of rides yes yes exactly right this is a type of number that would probably show up on uber's um you know 10ks and 10qs yeah right so the number of rides total number of rides um over what unit of analysis so um total number of friends think about the big picture think about think about the big picture like okay this you know it's like the uber ceo you know on a annual conference call saying hey you know this is what we have achieved this year you know what would he say then obviously maybe uh quarterly or yearly yes um and we could also just say okay per day week month quarter a year yeah okay um you know of course like you want to sort of refine it based on the use case you know like if we're talking about av experiment you probably want to look at them more like on a daily basis right um but we're talking about the overall health and you looking at across day week month and quarter and year um depending on what is a business strategy we're focused on will have a different purpose yes um okay"
  question_topic: Product Metrics

ITEM #11
  interviewer_question: time=36:15 text='what about adoption'
  candidate_answer: time=36:18 text="so um adoption is how much users can we get i know about acquisition it's like how many because i know about the funnel so acquisition is the first step where how many users were registered to the app number of signups and in terms of um adoption yeah i'm confused about adoption"
  reference_answer: time=None text=None
  interviewer_feedback: time=36:46 text="so it's similar it's it's it's just it's um synonymous okay so out of the new visitors how many ended up using the app yeah okay um and you can kind of refine it into two-step procedure so um you visit the app um you know and you you download it right uh you sign in or you sign up and then you take the first ride so actually like it's like a three step sort of thing right yeah so you can think about it as like a download rate sign up rate first ride rate does that make sense yeah um but again we're not we're not really done we haven't really completed what that actually like what the unit of analysis is so are we talking about per day per week per month yeah or are we talking a light time so sign up would be different for every user but then an average sign up per week per day the number of signups we get so yeah sign and effort sign up for because today is something that that that won't be feasible so maybe week or month okay maybe we can do quarterly and a year as well so but because if if this is something it depends on the business metrics as well that like business evaluation so if this is an annual evaluation you would definitely want to be back and forth and check it check quarterly because there's this effect of seasonality or any external effects as well that can uh you know reduce or increase our uh sign up or any other engagement as well yeah yeah yeah so definitely weekly weekly because um maybe people want to travel on weekends and as well so that's why weekly is something that we should go to yep yep that's fine um okay so what about"
  question_topic: Product Metrics

ITEM #12
  interviewer_question: time=38:54 text="yep that's fine um okay so what about retention"
  candidate_answer: time=38:58 text="so um in terms of retention it's like the uh maybe the churn rate because we so that's a component of it capture turn rate there's a more of a top-down top uh metric that um but also focus on users and recurrent users so what is that um deu daily active user yeah okay yeah um but on a different time window yeah so definitely uh the because if if it's if we measure per day we would be having more people using it in the morning in office times right should we be using um so retention in terms of daily active uses and maybe if we check per day the number of times that the user uses the app so because we would be having a high retention in the morning so i'd say we could perhaps capture that in engagement okay retention metrics"
  reference_answer: time=None text=None
  interviewer_feedback: time=39:07 text='but i think we have a better way to captures the meaning of churn as well what else sorry uh that we got you got cut off for a second so deu and what else what else okay um but um so we so more like weekly active user and nau multi-octave user okay okay so those are the common set of'
  question_topic: Product Metrics

ITEM #13
  interviewer_question: time=40:44 text='um and what about for task success so task success is like the type of excuse type of metrics that the engineering managers would care about you you have noticed that you listed some aspect of these so what are those'
  candidate_answer: time=40:56 text="so success is success would be um obviously the time or the average estimated time eta of maybe a okay the yeah average time for um because this this one's tricky we can do it um per customer as well per driver or an overall i'd say i'd say we can think about it more on the um more on the overall level if you were thinking about it at the user level then you would need to average it sort of thing yeah or maybe this could be more specific to regional and location as well yeah you could do it by a segment but you know but let's just get the big picture here okay um so um and one thing i want to mention is that when it comes to past success you want to you want to think about efficiency so eta is an efficiency score um and effectiveness how successfully are you providing a ride right so that's one aspect that you can think about but the other aspect you can think about is like aerate bugs glitches and when someone opens the app out of all the app opens um what percentage of them did you uh what did the app open up without any bugs yeah this is"
  reference_answer: time=None text=None
  interviewer_feedback: time=42:27 text="right um so do you get the picture of what this heart metric is and and why we should be using heart to measure health yes definitely yeah i wasn't close towards the success side so i was just yeah it's a it's a it's a common it's a common mistake um you know people um you know all to sort of interchange growth success and health um they have some similar attributes but there are also differences as well um and interviewers are looking for for that like do you clearly understand the term and and know what are they appropriate attributes to explain explain that um so uh so this this should provide a much more um you know much a better response um when it comes to a question like this measured for like we can maybe we can use the aar metrics for that yeah so arg um so arg is another popular framework um i would actually argue that our it's a funnel metric right so it's like from the beginning to the end it follows some sort of like a chronological manner yeah um the problem in our arg is that it overlooks um two aspects that matter a lot which is satisfaction user satisfaction and also task success because none of the r dimension would have that so i wouldn't i wouldn't use arg in this case i would use arg um for measuring success um and even with you know when you're measuring success i wouldn't use the entire all like all five of them that's just way too exhausted that shows that you're not being discriminatory so maybe when it comes to measuring success i would focus on definitely engagement and and to be frank like i wouldn't even say like i'm going to use i'm going to use exactly the dimensions mentors like typically what i do is um when it comes to measuring success i talk about metrics related to growth engagement and monetization okay um so those are the three dimensions that we'll talk about when it comes to us um all right so"
  question_topic: Product Metrics

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/datainterview/data-scientist-senior-uber-coach-datainterview-2022-04-28/data-scientist-senior-uber-coach-datainterview-2022-04-28.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
