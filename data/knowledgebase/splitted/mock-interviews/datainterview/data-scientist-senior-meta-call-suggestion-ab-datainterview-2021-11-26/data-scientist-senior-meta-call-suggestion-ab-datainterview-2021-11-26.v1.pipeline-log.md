<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26",
  "transcript_folder": "transcripts/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/",
  "source_id": "data_scientist_senior_meta_call_suggestion_ab_datainterview_2021_11_26",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:05:21 +0200",
  "updated_at": "2026-05-20 21:12:43 +0200",
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
    "json": "splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26//timecodes.txt",
        "en",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.pipeline-log.md"
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
        "splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.pipeline-log.md#LLM_INPUT_STEP_2"
      ],
      "outputs": [
        "splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.json"
      ],
      "status": "completed",
      "duration_sec": 180.0,
      "notes": null,
      "finished_at": "2026-05-20 21:12:43 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:12:43 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26//video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 0.0,
      "notes": null,
      "finished_at": "2026-05-20 21:12:43 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/`
- **Source ID:** `data_scientist_senior_meta_call_suggestion_ab_datainterview_2021_11_26`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:05:21 +0200
- **Last updated:** 2026-05-20 21:12:43 +0200

Фильтр в IDE: `*data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26//timecodes.txt`<br>`en`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.pipeline-log.md` | — | completed |
| 2 | qa_extraction | yes | claude-sonnet-4-6 | `splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.pipeline-log.md#LLM_INPUT_STEP_2` | `splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.json` | 180.0s | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26//video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.validation-report.md` | 0.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.pipeline-log.md`

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
SOURCE_ID: data_scientist_senior_meta_call_suggestion_ab_datainterview_2021_11_26
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/
INTERVIEW_LANGUAGE: en
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00] hello mark
[00:01] hey dan how are you
[00:03] i'm good are you
[00:05] i'm doing well thanks for having me
[00:07] yeah thanks for partaking as a mock
[00:10] interview candidate
[00:11] um so for those who are watching uh mark
[00:14] is a um a currently an interview
[00:18] candidate for the meta um data scientist
[00:20] analytic physician along with other
[00:23] um startups and tech companies like chin
[00:26] um
[00:26] and amazon and so um we're gonna have
[00:30] mark basically go through some of the
[00:33] product sense questions um this is not
[00:35] gonna cover basically the entire
[00:37] like 30 to 40 minute you know product
[00:40] sense questions that are asked on the
[00:41] meta interview itself rather it's more
[00:43] like a kind of like a sample in terms of
[00:46] you know what kind of questions you
[00:47] could potentially be expected in
[00:50] you know these analytic based um
[00:52] questions that meta but also
[00:54] other products sense interview around
[00:56] the different companies as well
[00:58] um and lastly this is a glimpse of you
[01:01] know what are the premium content that's
[01:04] available in the monthly subscription
[01:05] course um currently right now as of
[01:08] right now there's about five recordings
[01:10] of these one one-hour mock interviews
[01:12] with um questions and solutions but also
[01:15] uh this is a glimpse of what a coaching
[01:18] service looks like in terms of you know
[01:20] if you were to pair up with me
[01:22] um what what i could offer in
[01:24] preparation for your interview and um
[01:27] you know the prep being highly
[01:28] personalized based on the companies that
[01:30] you're interviewing for
[01:33] uh so without further ado i'm going to
[01:36] go ahead and
[01:38] start the mock interview around
[01:40] um basically the process itself
[01:43] so i'll go ahead and um ask you the
[01:46] first product sense question which is
[01:48] the following
[01:49] um
[01:50] so
[01:53] so mark hopefully you've done some
[01:54] research uh you know prior to this
[01:56] interview about uh meta's portal device
[01:59] um could you figure out ways to kind of
[02:01] measure engagement on meta's portal
[02:05] sure so
[02:07] um before i jump into the like a
[02:09] brainstorm matrix and like a plan to
[02:12] take all this business question i have a
[02:14] couple of clarifying questions i have
[02:18] um i think first of all is like uh like
[02:22] what what is like business purpose of
[02:25] measuring the
[02:26] engagement of this mata portal device
[02:30] and then like how does that tie to the
[02:33] overall
[02:34] um meta mission or like a business
[02:38] objective
[02:39] yeah that's a very solid question um so
[02:42] basically
[02:43] um
[02:44] we just want to kind of understand
[02:46] whether you know meta is like a viable
[02:48] business product um you know in terms of
[02:51] like user engagement um are like how
[02:54] active are um you know basically
[02:56] customers of um
[02:58] portal is
[03:00] um and so
[03:01] uh so we want you to kind of come up
[03:03] with you know potential metrics that can
[03:05] help us you know are users um you know
[03:09] are they engaging on this portal device
[03:11] or not
[03:13] gotcha gotcha and just to make sure i
[03:16] understand the product correctly so as
[03:19] far as i know uh like a meta portal is a
[03:23] like a hardware product that enables
[03:26] users to be to do like a a video course
[03:29] with better sound and video qualities
[03:33] and also it has alexa built alexa
[03:37] building which you are able to watch
[03:39] news or schedule remind
[03:42] reminder and also play your music on the
[03:45] portal so yeah on is there any other
[03:48] feature i need to be aware of about this
[03:51] product
[03:52] i think that pretty much covers the core
[03:55] functionalities on the uh on the product
[03:58] itself ah yeah thank you so then uh like
[04:02] a i think i get in order to make sure
[04:05] the uh engagement on my portal device uh
[04:09] you know i think they are like a i think
[04:12] there are two diff uh two goals first
[04:14] like uh for the user goals um i can type
[04:17] it here how do you measure engagement uh
[04:21] let me let me first like a um uh
[04:23] supervisor why the major engagement is
[04:26] important because at facebook let me
[04:28] insurance to
[04:29] give the power give people the power to
[04:31] build a community and also bring a world
[04:34] cluster so this product can serve as the
[04:37] uh
[04:40] a tool enabling a more user to stay
[04:43] engaged with mata platforms and then so
[04:46] i think like for a years ago you can uh
[04:49] by using the portal or they can like do
[04:52] more um uh do more video clips with
[04:55] their friends or their families which
[04:58] intent which would also increase their
[05:00] can spend on uh on the uh um meta
[05:04] products like what's app and message us
[05:07] and then from business goals i think
[05:10] like a
[05:11] engagement like a um we can see like how
[05:14] our users keep coming back using these
[05:17] products and encourage them to stay
[05:20] engaged on facebook
[05:23] and so i think like uh like a potential
[05:26] impact is like once we increase the user
[05:28] test span on our platforms which will in
[05:31] turn uh increase and gross our revenues
[05:34] um for meta okay cool um then so i think
[05:39] i can i can bring this down some uh my
[05:42] trick around the
[05:44] uh
[05:45] around the meta portal device i think
[05:47] measure the engagement um
[05:51] i think first of all um
[05:54] i think
[05:57] so i just have a wi-fi question so we
[06:00] are just talking about the user who
[06:01] already bought the product devices right
[06:04] yes status quo
[06:06] so i think now like a uh like a couple
[06:09] dimension uh we can look at first first
[06:12] is the like a uh hyperspace activation
[06:18] activation would you like like a how
[06:21] many people really after they purchase
[06:23] this product how many like a login using
[06:26] this device on the device on total
[06:32] on portal and also like a how many like
[06:35] um like a how many
[06:38] how many people really like a um
[06:42] login i think login is activation and
[06:45] also
[06:46] start uh start like a inter like a using
[06:49] the feature on the device so maybe like
[06:52] a star number of like a video calls
[06:58] and then number of the
[07:00] uh like a uh also uh
[07:03] what else
[07:06] i think um
[07:08] a video calls with on my video we
[07:11] already have number of the video calls
[07:14] um
[07:15] like a what
[07:16] other than video code that like we
[07:18] talked about they can use this portal to
[07:21] like a set up uh their calendar so i
[07:25] also want other like interaction
[07:28] um they can like a like a
[07:31] like a meeting setup
[07:34] meeting setup
[07:36] or like a music play
[07:38] um play some play
[07:41] etc so basically it's like it was there
[07:43] like an interaction which would look
[07:45] like and then next next part here i will
[07:47] look at the like a um retention so um
[07:52] when i say uh
[07:53] when i say retention is about like a uh
[07:57] like a daddy ip user weekly ft user and
[08:01] um
[08:03] and monthly active search so
[08:06] so other than that so but we also need
[08:09] to define what what does the what is
[08:11] active nameless of the users um like i
[08:14] usually
[08:16] uh if we can look at what's the
[08:18] frequency a user do a video call or if
[08:23] if the frequency is about like a
[08:25] two or three times a day maybe we can
[08:27] look at a like a two weeks window to
[08:30] define whether a user is active or not
[08:32] and then also i will look at the ratio
[08:35] like a dau
[08:37] on wau ratio this will be served as like
[08:40] a to measure the
[08:44] techniques and stick techniques
[08:47] on like a how how many users come back
[08:50] to us like after a week or two weeks so
[08:53] that's what i will be looking at and
[08:56] then uh another another dimension i'll
[08:58] also touch on is the revenue because at
[09:02] the end of the day
[09:04] on the the from the user goal we we try
[09:07] to in
[09:08] um
[09:10] uh have more people uh using this
[09:13] product so that they will spend more
[09:15] time on the portal which like is the
[09:17] opportunity for us to display some ads
[09:21] or like embedding some
[09:23] sponsor
[09:24] accountants when like a uh when they
[09:27] interact with the user that will also
[09:29] like from a revenue perspective i will
[09:32] look at like a average like a dollar
[09:36] like a
[09:40] like uh
[09:42] on
[09:43] monitor producer
[09:46] and also
[09:48] gen every dollar as revenue
[09:51] for users and then also like a look at
[09:55] um like a
[09:57] customer like 10 value etc so
[10:00] yeah and
[10:03] yeah uh i think it's just like a three
[10:06] main
[10:06] category i'll be looking at um
[10:09] is there any
[10:11] uh particular bucket you want me to talk
[10:14] more about
[10:16] um no i think that pretty much covers um
[10:19] uh you know your you touch base on uh
[10:22] pretty good categories of metrics
[10:24] activation retention and revenue
[10:26] um now can you kind of pick out maybe
[10:28] like three
[10:29] metrics that you think would be
[10:31] important so suppose that you need to
[10:33] create some sort of a dashboard
[10:35] for
[10:36] um
[10:37] you know let's just say an executive
[10:38] right um who's part of the device and
[10:41] hardware team right and they're gonna be
[10:43] the ones that are looking at this along
[10:45] with other product managers in that
[10:47] vertical in that horizontal um you know
[10:50] basically the business of the hardware
[10:51] within meta um can you think about what
[10:54] three metrics you would want to display
[10:56] and then rank order those metrics from
[10:58] the most important to the least
[11:00] important gotcha so uh let me let me
[11:04] reframe what i just heard to make sure i
[11:05] understand the question correctly so
[11:07] basically assuming that we are building
[11:09] a negative analytic dashboard like
[11:12] empowering our business holders it can
[11:14] be product manager or executives to
[11:16] measure the effectiveness of this
[11:18] product so on like a uh the question is
[11:22] about like picking three main primary
[11:26] metrics that can like a help them
[11:29] monitoring the metrics over time um
[11:33] so cool um
[11:35] let me take a quick minute to organize
[11:39] my thoughts
[11:41] um
[11:42] yeah i think
[11:45] [Music]
[11:46] so i think the first
[11:49] and then ranking in the importance based
[11:51] on the importance level so i think uh
[11:54] the first um i didn't know what um i
[11:57] think the first primary metry i will
[12:01] look at is the video
[12:04] uh
[12:06] video like a call
[12:08] time
[12:10] in
[12:11] in minutes in hours
[12:14] um per month so because like as you
[12:17] mentioned
[12:18] the audience might be like a leadership
[12:21] or a security so like they will probably
[12:24] care the more about the
[12:25] like a high level overview how much i
[12:28] get total time uh they spend on this
[12:30] product over time and then also to see
[12:34] whether um like they do more uh video
[12:37] calls uh with uh this new launch product
[12:40] uh so like a um and i get this
[12:44] another reason why i picked this machine
[12:46] is this make sure also
[12:49] embodies all
[12:51] all the other like interaction like we
[12:54] talked about like a we do a video course
[12:57] or or like a set up meeting playing lucy
[13:00] so like the more activities they uh took
[13:04] um with this device no more time spent
[13:07] on so it's actually not that a video
[13:10] call time i will be
[13:12] like a little bit um like a time spent
[13:16] on hours
[13:19] and uh sorry type of spam in all around
[13:23] on photos
[13:26] um
[13:28] so yeah and then
[13:30] i think the secondary matrix i will look
[13:33] at would be
[13:34] because like i think one of the core
[13:37] functionality with portal is the video
[13:40] call so i want to like know what's the
[13:43] total number of the video calls
[13:46] per month
[13:47] so
[13:50] total
[13:51] number of video
[13:53] calls per month
[13:56] um
[13:57] i think this will on a day so
[14:00] we uh the reason for that
[14:03] would be uh i i would like to know
[14:05] whether
[14:06] uh uh like a whether um like a with
[14:10] these new products uh users are easier
[14:13] to do a video course or they will um
[14:16] like jump on the video call with their
[14:17] family or friends more frequently so uh
[14:20] and then lastly uh i will pick one from
[14:23] the revenue so
[14:25] um and for the monetization perspective
[14:29] on
[14:30] like a like a revenue
[14:33] per month
[14:34] so
[14:36] uh
[14:39] i think that will be like a
[14:41] um
[14:42] i'm not quite sorry i'm not quite sure
[14:45] about how the ass will
[14:47] embed it on the portal like a fun face
[14:50] from the meta news feed we know like it
[14:52] when you go through the post the no you
[14:54] will you will probably see some like a
[14:57] sponsored ass but i have a portal on
[15:00] like a could you like it give me some
[15:03] uh direction about like a how
[15:07] the from the advertising side how that
[15:10] would be
[15:11] embedding within this product or
[15:14] yeah
[15:15] um yeah so um in this case let's just
[15:18] assume that there's really no like
[15:19] advertisement that are displayed in the
[15:21] portal device itself
[15:23] um so i wouldn't so
[15:25] just kind of going back to original
[15:26] questions which is just focusing on
[15:28] engagement um just leaving that
[15:30] monetization aside can you think about
[15:32] perhaps any other metric that you may
[15:33] want to display in this metric based
[15:35] dashboard
[15:37] sure so
[15:39] so leaving a monetization site then i
[15:42] will
[15:43] um like a doula on like retention like a
[15:46] diu
[15:50] and
[15:51] user i think this is like for all the
[15:55] uh meta products uh
[15:58] so we care about like a daily activity
[16:01] so weekly i've used them on the active
[16:03] users so like they're having this um
[16:06] actually like having the active users uh
[16:10] on the dashboard will be give give our
[16:13] audience a better understanding of how
[16:16] how our uh how our products being used
[16:19] by the users and then their active new
[16:22] needs so yeah does that make sense okay
[16:24] got it got it now how do you so among
[16:27] these three metrics you have outlined um
[16:29] how would you go ahead and prioritize
[16:31] them from ranking from one to three
[16:34] sure so far name ranking one two three
[16:39] on
[16:39] us per month um
[16:42] i think uh let me move the
[16:45] daily attribution
[16:48] to the first one um
[16:51] um so
[16:53] i think the first that i think the
[16:55] problem images should be that you have
[16:56] the user with three user monthly active
[16:59] users and then by different like a
[17:01] segmentation by a country region all
[17:04] different
[17:06] uh like a
[17:07] language etc and then like because like
[17:11] um
[17:12] we have to
[17:16] the reason the main reason for that is
[17:19] um this will serve as the
[17:22] uh retention uh metrics like we just we
[17:26] don't want just like a launcher product
[17:28] and user just use once or twice and then
[17:31] put that put that away so that this will
[17:34] be served as the measure to know how
[17:36] like it what's their retention look like
[17:38] um so this will be my
[17:41] primary primary matrix and then secondly
[17:44] as i mentioned the time spent is also
[17:46] critical as that it will like tell us
[17:50] about how like a um how much time is
[17:53] spent with on a portal and then like a
[17:56] and in a and then what's their
[17:58] interactions um and yeah and that's
[18:01] least total number of video calls yeah
[18:05] just damage
[18:06] okay
[18:07] okay got it
[18:09] um all right now
[18:11] i have a new question problem for you
[18:17] the third question i have is following
[18:19] suppose a new feature is introduced on
[18:20] portal which is called call suggestion
[18:23] this future recommends calls to users
[18:26] how would you design an ap experiment on
[18:28] this feature
[18:30] um suppose a new feature introduced in
[18:32] portal uh which is called code
[18:35] suggestion
[18:39] you just
[18:40] design
[18:44] um so uh
[18:47] so the question is about how do we
[18:49] really
[18:50] um like design the
[18:52] uh
[18:54] experiment i think there are a couple of
[18:55] steps we need to follow when it comes to
[18:58] the experiment um first like they we
[19:01] need to state the
[19:02] uh hypothesis testing uh oh no i think
[19:06] first of all we need to define what was
[19:08] the success matrix like uh what are um
[19:11] like a what are we going to make sure uh
[19:14] okay um when we launch this new feature
[19:18] so i think the step one will be
[19:23] okay what what will be this assessment
[19:24] should look like
[19:29] so matrix and then like a i assume that
[19:34] um with this new features
[19:37] the purpose is to
[19:39] make users more easily to
[19:42] uh start a call start a call and then
[19:47] which will better
[19:48] the number of the calls will be
[19:51] in work will increase accordingly so i
[19:54] will
[19:56] i will pick uh um i will pick up
[19:59] average number of video calls per users
[20:03] as the
[20:04] nature we are going to
[20:06] make sure does that make sense or
[20:09] yeah that's good
[20:11] so average like a number
[20:15] of video have calls
[20:17] on per user
[20:20] and then secondly uh like a uh so like
[20:23] we need to define let's state the
[20:25] hypothesis testing so all i think the
[20:28] number uh here the null hypothesis will
[20:31] be uh the average number of the
[20:35] core per users um between the control
[20:39] and treatment group will be the same and
[20:41] alternative hypothesis will be the um um
[20:46] the average number of the uh average
[20:48] number of cost per user between two
[20:51] groups out on are different and then
[20:54] like we need to follow by uh we need
[20:56] followed by like i define the uh
[20:58] significance level uh statistical power
[21:01] and then the mde
[21:03] to determine how much uh same process uh
[21:07] we need and then um so let me let me put
[21:10] it down
[21:11] like i say the
[21:14] five pounds
[21:29] like a significant level
[21:32] uh power
[21:33] and the mde so alpha
[21:37] alpha like a power
[21:40] and like a md
[21:43] and then
[21:44] and then
[21:46] and then also we also need to determine
[21:48] what's the like a
[21:50] randomization unique so i think this is
[21:52] kind of like a um again
[21:55] or like a uh because like i will assume
[21:59] like
[21:59] in this setting the observation you need
[22:02] is the
[22:03] customer so uh like it's better we can
[22:07] we can perform a randomization at the
[22:09] customer level and then and then like a
[22:13] another uh also we've just talked well
[22:17] um we just focus on the user who own the
[22:20] portal device right otherwise we could
[22:23] we could like measure these features the
[22:26] effectiveness of this feature so i will
[22:28] be like a customer
[22:30] who own
[22:32] like a portable device
[22:36] yeah and then once we have that like a
[22:40] we are able to uh and again
[22:43] estimate the
[22:45] on like a experiment
[22:47] [Music]
[22:48] xp re
[22:50] augmentation
[22:51] [Music]
[22:52] time so
[22:55] um usually like a typical like a
[22:57] experimentation time in every testing on
[23:01] like usually
[23:03] it will last for like one week or two
[23:05] weeks
[23:07] on the reason for that if we if it is a
[23:10] short experimentation then it will
[23:12] probably be problematic given there's a
[23:15] um like a day of the week effect
[23:18] unfortunate for instance like a
[23:20] users tend to do a video call on the
[23:24] weekend or on a weekday so uh like the
[23:27] best practices will be usually um do
[23:30] like at least more than two weeks um so
[23:35] here i will use the two weeks
[23:38] yeah and then after that um
[23:43] how would you design and then after we
[23:45] gathered say two weeks of the data then
[23:49] we are able to uh
[23:51] use the um um
[23:53] uh two symbol t tests to
[23:56] to make sure the uh the leaf between the
[24:00] leaf in the metric uh across control and
[24:03] experiment and the treatment groups are
[24:06] actually
[24:07] achieve
[24:08] statistically uh significance um so
[24:13] that's like
[24:16] and by checking the p value and so
[24:21] um
[24:27] [Music]
[24:28] yeah
[24:29] and
[24:30] yeah and then after
[24:32] say given that the like a p value is
[24:35] less than 0.05
[24:37] 0.05 and like it it will be like a
[24:40] to decide like whether we should launch
[24:42] this new feature or not
[24:44] but like it's not it's not just um
[24:47] feature
[24:48] oh um by the way uh like when we uh
[24:51] something i didn't mention about is that
[24:54] uh we other than just pick one success
[24:56] symmetry it's better we can also have
[24:59] some of like a gar rail mattress which
[25:03] is like a geometry which that which
[25:05] shouldn't be degraded in pursuit of this
[25:07] assessment tree um so
[25:10] uh in here i will use the um the
[25:16] um i think
[25:18] like as revenue or 10 spend um portal as
[25:22] the gabriel so
[25:23] like a like as a career metric but like
[25:27] a um
[25:28] on the last step is to launch the new
[25:30] feature or not on and other than
[25:33] checking the statistical uh significant
[25:36] result from experimentation we also need
[25:39] to
[25:40] involve the business holder to see
[25:42] what's the um like a
[25:44] practical significance look like and
[25:47] also do some uh like a
[25:50] cost and benefit analysis to make sure
[25:53] it's gonna likely take too much
[25:54] resources to launch these new features
[25:57] um so now that would be the
[26:00] next step yeah does that make sense okay
[26:03] sounds good
[26:04] um and you so you define some good
[26:06] structure there but um
[26:08] but in terms of uh are there any other
[26:11] details you may want to populate
[26:13] uh any other detail um
[26:17] so i think like a um i think
[26:20] i will add more details around um like
[26:24] this closer i think
[26:26] um that sounds like a we need to also do
[26:30] something like a like a
[26:31] um
[26:32] velocity checks for example uh to make
[26:36] sure that the
[26:38] um like a um
[26:40] observation we gather should be
[26:42] independent uh
[26:44] with each other and also whether there
[26:47] sounds sensational seasonal or holiday
[26:50] holiday effect and also another effect i
[26:53] can think of is like novelty effect
[26:55] which means that when the new features
[26:57] uh uh on a
[26:59] product appears uh given its novelty you
[27:02] should probably may respond to this
[27:05] feature positively at first but like but
[27:08] over time uh the novelty of the feature
[27:11] will waste off then the behavior will
[27:13] return to normal so we need in that case
[27:16] we should probably uh extend the like a
[27:19] experimentation to get more data to
[27:21] validate that so yeah
[27:24] okay got it i have a question for you so
[27:26] what do you think would happen if this
[27:28] change was made over a let's just say
[27:31] christmas weekend
[27:33] um uh over christmas christmas christmas
[27:36] weekend yeah
[27:38] uh
[27:39] yeah then i think like a uh if we like a
[27:43] uh lunch experimentation during the
[27:46] holidays like christmas then we will
[27:48] probably see
[27:50] the uh we um like a the final result is
[27:54] um like a kind of like inflated or
[27:57] overly
[27:59] uh optimistic because like people um
[28:04] especially during the kobe most people
[28:07] cannot
[28:08] go home to like they have a family
[28:10] reunion
[28:12] so like they will probably do more video
[28:14] calls like a during holiday so in that
[28:16] case we will probably gather inflated uh
[28:19] average number of calls per user like
[28:22] during this during this time so uh in
[28:25] order to
[28:26] um um
[28:29] um to get a
[28:31] better reliable result we should
[28:33] probably
[28:34] um
[28:35] um like a
[28:37] alright
[28:38] we should probably uh
[28:41] gather more data
[28:43] and like because i'm assuming like um so
[28:48] yeah so probably like extend the
[28:51] experimentation time um
[28:53] yeah
[28:54] does that make sense or
[28:56] okay
[29:00] okay all right so this is the end of the
[29:02] question portion and and obviously you
[29:04] know
[29:05] um you know i would have wanted to ask
[29:07] you more follow-up questions but you
[29:09] know once again this is more of like um
[29:12] like a simulation exercise right so
[29:15] if we could do the actual mock interview
[29:16] then there'll be a lot more company sent
[29:18] than this um but i just want to go
[29:20] through um each question at a time from
[29:23] beginning to the end and we'll talk
[29:24] about you know what you did uh well and
[29:26] then what are some areas of improvement
[29:28] does that sound good yeah that sounds
[29:30] good to me yeah
[29:31] um and and just kind of before i
[29:34] actually dive into that just i would say
[29:35] just overall i think the way you were
[29:38] approaching each question
[29:40] um
[29:41] your communication was good um it was
[29:43] very clear to unders it was you you
[29:45] expressed your ideas very clearly so it
[29:48] was very easy to sort of follow through
[29:49] what your
[29:50] um reasonings are right on each of the
[29:53] um questions that you were addressing so
[29:55] that's really good that you were doing
[29:56] that
[29:57] um the second thing i i liked about the
[30:00] overall approach of how you were pushing
[30:02] the problems were that
[30:04] your solution styles were very
[30:06] structured um so you didn't just kind of
[30:08] ramble you had a framework in terms of
[30:10] you know how you're going to respond to
[30:12] each of the questions
[30:13] um so that made things very easy to
[30:15] follow um as an interviewer um and
[30:19] that's really good that you were doing
[30:20] that
[30:21] um
[30:22] but i would say that there were
[30:24] there was one thing that i i would kind
[30:27] of um refine your response because i
[30:29] noticed that there were some moments
[30:31] when you seem a little bit hesitant
[30:33] or
[30:34] unsure
[30:35] about whether your response is
[30:38] correct or not
[30:39] um i would try to refrain from doing
[30:41] that um because you want to project
[30:44] confidence and if you're not sure about
[30:46] certain things
[30:47] um just don't bring that up at all so
[30:50] for instance you asked me about you know
[30:53] does meta is there a way for meta to
[30:56] generate um revenue like are there some
[30:58] advertisement display right
[31:00] um
[31:02] uh
[31:03] when you're not sure whether there is a
[31:04] particular future that already exists in
[31:06] the product or not it's best not to just
[31:08] bring it up um because if you bring it
[31:11] up then you can expect some follow-up
[31:12] questions on that and that can cause you
[31:14] some troubles later down the road
[31:16] um those who are watching this um that's
[31:20] actually one of the key things that um a
[31:22] lot of candidates often kind of make
[31:24] mistakes on you know they read some
[31:27] techniques off the internet um you know
[31:29] and then they they'll basically just
[31:31] kind of rehash it
[31:32] um and talk about it during the
[31:34] interview
[31:35] and
[31:36] because they don't really know like the
[31:39] actual reasoning or they don't know the
[31:41] exact details behind why
[31:43] um you know that technique taking is
[31:46] exists or whether a particular feature
[31:47] on a product exists then you know they
[31:50] they just sort of bring it up but then
[31:51] like when an interviewer asks follow-up
[31:52] questions they're not able to justify
[31:54] um so it's best not to bring up
[31:56] something if you're not really sure
[31:59] okay yeah i think that's a great quote
[32:02] yeah um so so projecting more confidence
[32:05] i think that's something you really need
[32:06] to work on um because in each of the
[32:08] three questions i noticed that you were
[32:10] kind of hesitant in terms of your
[32:12] response um and you really want to be
[32:14] able to project uh certainty in your
[32:16] responses
[32:17] um rather than hesitations
[32:22] all right so that's just a general
[32:24] overview of what i was kind of gauging
[32:27] um off of the uh you know off of how
[32:29] you're responding now let's go through
[32:31] each question on each question at a time
[32:33] so starting with the first question
[32:35] how would you measure engagement or meta
[32:37] support of device
[32:38] um so i think i i really love how you
[32:41] are approaching this with a good
[32:42] framework activation retention revenue
[32:45] however though
[32:46] you were kind of missing the main focus
[32:49] of this question which is engagement
[32:51] right if i would ask a question about
[32:54] how would you measure success on meta
[32:56] meta portal device right
[32:58] then that might be
[33:00] um accommodating for activation
[33:02] retention plus
[33:03] revenue in this case but then i'm more
[33:05] talking about the engagement so it's not
[33:08] so much about the monetization i care
[33:10] about it's more about the retention here
[33:14] right um activation activation being the
[33:16] secondary thing and the primary thing
[33:18] being retention um and so i would have
[33:20] loved to see more focus on these
[33:23] two categories
[33:25] and um it would have actually been fine
[33:27] if you just left out revenue because
[33:28] that wasn't the main focus of the
[33:30] question which is engagement
[33:32] um so that's something
[33:34] um to kind of look out for um really
[33:36] understand the differentiation between
[33:38] when um when anybody is asking how do
[33:41] you measure happiness measure
[33:43] satisfaction measure engagement measure
[33:45] success
[33:46] these fours sound the same
[33:48] but to
[33:50] on certain extent they're a bit
[33:52] different um and so make sure you have a
[33:54] clear understanding of what the question
[33:56] is
[33:57] and you're not just listing some
[33:59] arbitrary set of metrics but you're
[34:00] actually said listen metrics that
[34:02] actually answer the question
[34:06] okay
[34:07] yeah sounds good
[34:09] um
[34:10] oh sorry can i ask the question
[34:13] yeah go ahead good uh so like a um did
[34:16] you have other suggestions on like a um
[34:19] um brainstorm the make brainstormer
[34:23] matrix when we were asked about the
[34:25] question because sometimes i would be
[34:28] stuck on like okay this is the other
[34:31] this is all the measure i can think of
[34:33] on top of my head but i don't know
[34:35] whether
[34:36] um or less sufficient or like what will
[34:39] uh like when with brainstorm make sure
[34:41] it will be like a fair number of the
[34:42] magic which you bring it out in an
[34:45] interview yeah so i would say that just
[34:47] start with actually so that's a really
[34:49] good question um uh it's especially
[34:51] common questions i get from clients all
[34:53] the time but basically the ideal i think
[34:56] instead of the way you should be
[34:58] addressing these kind of metric based
[35:00] questions is um think about you know two
[35:03] to three categories of metrics um so you
[35:06] kind of did that here and then within
[35:08] each category it lists two to three
[35:09] measures
[35:11] so this or itself already provided a
[35:14] good decent comprehensive set of metrics
[35:18] yeah
[35:19] thank you
[35:21] um and and when it when it comes to
[35:23] these type of you know questions about
[35:25] um you know measuring um measuring a
[35:28] future or product um a natural sort of
[35:31] following question is like you know how
[35:33] would you
[35:34] prioritize which metric to focus on
[35:36] um so that is expected you know um
[35:40] so this is more like a shout out to
[35:42] those who are prepared for these data
[35:44] scientists you know
[35:45] product data science interviews um when
[35:47] you're when you're practicing you know
[35:49] yourself to just kind of make sure
[35:52] um you know think about how to measure a
[35:54] product but also when you list these
[35:56] metrics think about how you would
[35:57] prioritize them based on different
[35:59] vocals
[36:00] um so so that's why i asked the
[36:02] follow-up question which is you know
[36:04] how would you pick out these three
[36:06] metrics and then how would you rank
[36:07] order them right
[36:09] um and so considering the fact that you
[36:11] know really the main focus is engagement
[36:13] um i think it made sense to focus on the
[36:16] um active users
[36:18] um
[36:19] set of metrics across these three three
[36:21] different windows
[36:22] the only thing i wasn't really too clear
[36:25] on and i think this is something that
[36:26] you sh you should have clarified a bit
[36:28] more is the definition of of active so
[36:32] what does what does it mean for a user
[36:34] to be active and that's something that i
[36:36] i notice um clients will kind of gloss
[36:38] over which is that they will just spew
[36:40] out okay you know i'm going to measure
[36:42] dau uh w-a-o-m-m-a-u right but then they
[36:45] don't clearly define what are the
[36:47] behaviors that actually define actions
[36:49] um and a key action can be it can be a
[36:53] it can be a set of multiple behaviors or
[36:55] it can be just one behavior right
[36:57] um and in the in the case of the portal
[37:00] um you know there's all these different
[37:02] primary functions right you make a call
[37:05] um you know you i'm sure you can also uh
[37:08] you know browse on a web application as
[37:10] well right um
[37:13] you know you can uh you can
[37:15] you have this calendar app you can set
[37:16] up meetings and stuff like that right uh
[37:18] so these are all these different type of
[37:20] actions and so you know do you want the
[37:22] action the key action to be defined
[37:25] based on um calls only or do you want it
[37:29] to be expressed based on a set of
[37:31] actions right
[37:32] um so that's something to clearly define
[37:35] in this case
[37:36] [Music]
[37:37] and i think i think in this case um you
[37:40] know even though portal one of the cool
[37:41] portal's primary function is like the
[37:44] video calls um it still doesn't mean
[37:46] that you know some users might just use
[37:48] it only for calendar purpose right
[37:50] um
[37:52] and so
[37:53] and so in that case um you know i would
[37:55] just have like an inclusive set of okay
[37:58] um you know if users
[37:59] are active in the form of any sort of
[38:02] app engagement whether it's on a
[38:04] calendar whether it's checking email
[38:06] whether it's um
[38:08] you know
[38:09] making a call
[38:10] um any set of like in-app engagement um
[38:14] then that that then i would consider
[38:16] that as an active engagement
[38:19] gotcha
[38:21] yeah
[38:23] all right so now let's look at the av
[38:26] experiment part right um
[38:28] so
[38:29] even before you
[38:31] talked about success metric do you think
[38:33] there were there could have been one
[38:36] topic uh topic that you could have flesh
[38:38] out with the more on
[38:43] i think one thing uh i think one thing i
[38:47] was missing is probably
[38:50] uh i didn't
[38:51] ask like clarifying questions around why
[38:56] why this is important and how this
[38:58] feature
[38:59] tied to the overall business goal so i
[39:02] just i jump directly into a framework
[39:04] without asking
[39:05] yeah that's precisely right yeah so for
[39:08] those who are watching this um this is
[39:10] this is another sort of common mistake
[39:12] which is like um candidates have a
[39:14] tendency and i think it kind of makes
[39:16] sense because a lot of what we do are
[39:18] very technical focus and so we have a
[39:20] natural tendency to produce a technical
[39:22] response from the get-go um but we have
[39:24] to keep in mind that
[39:26] um
[39:27] you know data science project from the
[39:29] beginning and also the end right are
[39:31] always business focused um so we have a
[39:34] business stakeholder we're working with
[39:36] they provide a context of what their
[39:37] needs are um and then we basically
[39:41] provide some you know we basically
[39:43] understand it in terms of you know you
[39:45] know what the business context is
[39:46] translate that into some system
[39:49] technical methodology and then we
[39:51] deliver it back into the business right
[39:53] so we also have to think about it in
[39:55] terms of okay whenever we need to
[39:58] provide a response to these type of um
[40:01] you know product
[40:02] based questions
[40:04] the the structure is always business
[40:06] technical and then business um and so in
[40:09] this case what hank did was he primarily
[40:12] focused on the technical part it kind of
[40:14] glossed over the business elements in
[40:16] the av experiment itself um and it's
[40:18] really important to just also just cover
[40:20] the business part of it as well because
[40:22] because you know because
[40:24] the interviewers sort of gauging you
[40:26] know if this was an actual project that
[40:27] you were actually performing
[40:29] um you know in real life like how would
[40:31] you actually
[40:32] you know deliver this right and so you
[40:34] want to provide a glimpse so it's really
[40:36] important for you to cover the business
[40:38] aspect of this question as well
[40:40] um and so yeah like focusing on you know
[40:43] what is the purpose of this experiment
[40:45] right but also
[40:47] focusing on um clarifying
[40:50] what this new future looks like you
[40:52] didn't walk through the user journey of
[40:54] what the current um process is and you
[40:57] didn't also walk through the experience
[40:59] of you know what this new future would
[41:00] do
[41:01] um and you sort of
[41:03] um yeah like you know basically just
[41:05] kind of overlooked it so skipped it over
[41:07] right
[41:08] um so just make sure you kind of you
[41:09] flesh it out
[41:11] and in this case the call suggestion
[41:12] would essentially be like a ui and so
[41:15] you know you could kind of imagine you
[41:17] know if you um go if you go to like a
[41:20] call list right it just looks like an
[41:22] endless scroll of all these different
[41:23] numbers right so instead of having
[41:26] having to go through
[41:27] uh scroll to find the number that you
[41:29] want to actually dial
[41:31] um you know imagine like there's like a
[41:33] call suggestion at the very top maybe
[41:35] it's like top three calls um that are
[41:38] suggested to you
[41:39] based on the likelihood that you would
[41:41] actually you would your intent is
[41:43] actually to make uh make a call to that
[41:45] person right
[41:47] so imagine what the benefit would be
[41:49] right um maybe it could help save time
[41:51] maybe it can also improve engagement as
[41:53] well right
[41:55] um and so
[41:57] fleshing out the context
[41:59] um are
[42:00] just as important as covering the
[42:02] technical aspect of it as well so once
[42:04] you paint the picture of this
[42:06] from there um you know hank what you did
[42:08] right you know what you
[42:10] did in terms of laying out the
[42:11] structures are good
[42:14] yeah yeah i think that's a great uh
[42:18] advice and i
[42:20] want the most commonly uh mistake
[42:23] uh like i i sometimes will uh ignore i'm
[42:26] not gonna lie i forgot so like before we
[42:29] jump into any solution or like a brain
[42:31] like a provider framework we need to uh
[42:35] stress on like what is the business
[42:37] purpose of this question and also uh go
[42:40] through what's the user journey look
[42:42] like when they interact with this new
[42:44] feature uh like it provides some of the
[42:46] contacts around from the business
[42:48] perspective i think uh it will make the
[42:51] answer more complete so yeah i really
[42:53] appreciate it
[42:55] yeah
[42:56] yeah of course now i do want to walk
[42:58] through a couple things here um so i
[43:00] think you laid out a good um procedure
[43:03] of running an av experiment but i felt
[43:05] that there were a lot of there were a
[43:07] couple details or someone missing there
[43:09] um so okay so success metric the average
[43:12] number of calls per user you know that
[43:14] um i i i like the idea so i think that
[43:17] works
[43:18] um
[43:20] um
[43:21] because this metric wouldn't necessarily
[43:22] violate the statistical assumption that
[43:24] the observation is independent in this
[43:26] case right
[43:27] you're aggregating at the user level and
[43:29] so that's why this metric would work
[43:32] in terms of stating the hypothesis so
[43:35] i have a question for you um
[43:37] could it be possible that just having
[43:40] some ui with arbitrary
[43:42] arbitrary
[43:44] lesson numbers
[43:45] like that itself could
[43:48] have an effect
[43:51] um
[43:56] yeah yeah so let me just rephrase that
[43:57] so so basically um if you if you think
[44:00] about the call suggestion right there's
[44:01] really two elements to this right so
[44:04] there's the ui
[44:05] and then there's the algorithm
[44:09] right so when you're displaying this at
[44:12] the very top
[44:13] how do you know if there's an actual
[44:15] effect right
[44:17] meaning that people are engaging a lot
[44:18] more because of this um ui right
[44:22] how do you know if it is a ui that is
[44:25] actually driving the engagement or it's
[44:28] the algorithm itself that is driving the
[44:30] engagement or the interaction of both
[44:33] gotcha
[44:34] so we're talking about like like a
[44:37] confounding variable
[44:39] yeah essentially right
[44:41] yeah yeah
[44:44] so how do we really um
[44:46] so
[44:47] [Music]
[44:48] yeah so so in this case this would
[44:50] essentially be um kind of like a
[44:52] multivariate testing so your your
[44:55] control is that okay
[44:57] here's a version without any
[44:59] okay and then second and then the second
[45:01] test
[45:02] is basically um you know uh just a ui
[45:05] with an arbitrary
[45:06] like list of numbers uh you know list of
[45:09] calls
[45:10] okay and then the third one is
[45:13] uh ui plus the algorithm itself
[45:16] gotcha like a motor
[45:20] so so it's not it's not just like a like
[45:22] a two groups like a game um
[45:26] i see three groups so it could be three
[45:28] groups uh one control um you know one
[45:31] treatment treatment number one and
[45:32] treatment number two
[45:34] yeah
[45:36] and
[45:37] gosh
[45:39] like this is like a ui and the second
[45:42] one ui plus
[45:50] you know essentially you would be doing
[45:52] uh like a pairwise t-test so you're
[45:54] comparing the control against t1 and
[45:56] then comparing the control against
[45:58] t2 and then you look at the relative
[46:01] life along with the system significance
[46:07] yeah
[46:08] and then you make the decision that okay
[46:10] hey you know what um this algorithm
[46:13] you know uh basically this call
[46:15] suggestion with the ui plus algorithm um
[46:18] is so significant and
[46:20] uh you know with the relative left being
[46:22] positive the positive direction right
[46:25] um and you
[46:26] would uh conclude that
[46:29] you know essentially um you know you
[46:31] would want to rule out the call
[46:32] suggestion to um to a larger population
[46:35] of the portal device users
[46:38] gotcha
[46:40] yeah that's something i did i didn't
[46:42] think of when i
[46:44] when i was asked about this question
[46:45] like maybe like when we when we we uh
[46:49] talk about the ui change we also need to
[46:51] think about uh whether the like a
[46:54] confounding effect from other
[46:56] driver like algorithm itself can also
[46:59] make an impact so how do we really
[47:01] validate that so yes
[47:06] it's about observing the sensitivity of
[47:08] the metric right so um when you make
[47:10] certain change like how do you know that
[47:12] the change is coming from
[47:14] um
[47:15] uh you know from from you know changing
[47:18] the metric is coming from basically what
[47:20] like the condition they have changed
[47:22] right
[47:22] um you know or is there some sort of
[47:25] like uh extraneous factors that are in
[47:27] the play here right so it's just a lot
[47:29] about being a bit more
[47:31] keen
[47:32] um being able to kind of differentiate
[47:34] you know where is the effect really
[47:35] coming from
[47:38] yeah
[47:39] um and in terms of defining the
[47:41] statistical parameter alpha power md i
[47:43] would have loved for you to actually
[47:44] flesh them out instead of just saying
[47:46] okay i i will go ahead and list off a
[47:48] power name
[47:50] right
[47:53] so
[47:55] so you could have cited like uh you go
[47:57] ahead
[47:57] i know i so i asking so
[48:00] uh maybe elaborate more on each of these
[48:03] three uh components like what was the
[48:06] significance level and then how do we
[48:08] define
[48:10] the
[48:10] the statistical power or etc or
[48:14] because sometimes i feel like it's kind
[48:15] of like a
[48:17] common sense that like
[48:20] we need these three to determine what
[48:22] the sample size needed
[48:24] but really then touch on the details
[48:26] about each of these yeah um bring it up
[48:28] bring it out anyways yeah cause the
[48:30] interpreter doesn't know whether you
[48:31] actually know it or not right
[48:35] really the main focus here is to prove
[48:37] provide evidence that you do know how to
[48:40] run an ap experiment and so
[48:42] uh and so i would not
[48:43] um
[48:45] you know i i wouldn't i wouldn't i
[48:46] wouldn't avoid like i wouldn't you know
[48:49] like basically like bring up anyways
[48:51] right even if it's common sense per se
[48:53] or even if it seems obvious like
[48:56] um you know so it's so really important
[48:58] to bring out these details
[49:00] gosh yeah
[49:04] um so in this case you know you could
[49:06] have just started off by you know citing
[49:08] some industry standard numbers right
[49:10] obviously that can kind of change
[49:12] depending on the type of test that
[49:14] you're running and what are the type one
[49:16] and type two risks um you're willing to
[49:19] tolerate um you know when you're
[49:21] designing and running these type of
[49:22] experiments you know but standard set of
[49:24] values like alpha being set at like
[49:26] point zero five power being a point
[49:28] eight
[49:31] um and and md um you know being
[49:34] somewhere between one to five percent in
[49:36] this case
[49:37] um
[49:38] actually let me
[49:40] truncate that value to like one to three
[49:41] percent um one to three percent would
[49:43] have been reasonable um and of course
[49:46] like you know you might expect the
[49:48] interviewer to ask you some additional
[49:49] follow-up questions about you know
[49:51] um you know like why do you like okay so
[49:54] putting outside industry center values
[49:56] like you know why can't you set the
[49:59] alpha at point one or power at point
[50:01] seven or md like at five percent or
[50:03] something like that right um
[50:05] in mid case then you know you can
[50:08] kind of follow up
[50:09] um
[50:10] on you know different values that you
[50:12] may want to explore
[50:13] gotcha
[50:14] yeah
[50:16] um
[50:18] yeah
[50:19] yep um yeah and uh randomization unit
[50:23] makes sense um estimating the
[50:25] experimentation
[50:26] uh
[50:27] basically the experimentation time set
[50:28] of two weeks makes sense um the only
[50:31] thing you forgot to mention is like how
[50:32] would you determine a sample size
[50:34] um so
[50:36] yeah so you would have you would have
[50:38] had to determine a sample size after
[50:40] step three
[50:41] um right
[50:43] yeah on determining uh
[50:45] yeah
[50:52] and you also
[50:54] it should come before determine the time
[50:57] right
[50:59] yeah once you know what the sample size
[51:00] is then from there um you
[51:03] uh you basically can figure out what the
[51:06] experimentation time partners
[51:07] yeah
[51:09] yeah
[51:10] yeah go ahead sorry
[51:12] yeah and and um do mention the
[51:15] statistical types you would be using in
[51:16] this case
[51:18] um
[51:20] yeah so
[51:21] i was saying the
[51:23] two sympathy tests
[51:26] yeah
[51:27] yeah because we are measuring the like a
[51:31] mean
[51:32] value across like a multiple groups but
[51:36] in this case right now we have three
[51:38] groups
[51:39] so maybe
[51:40] we should use anova instead
[51:43] no um so anova would only give you um
[51:47] if at least one
[51:48] um at least if at least one pair of the
[51:53] groups are different
[51:55] but it wouldn't give you information uh
[51:57] sorry if at least one group is at least
[52:00] if at least one group is different from
[52:02] all the other groups that's what donova
[52:04] will provide
[52:06] it wouldn't necessarily give you um
[52:08] information on
[52:09] um which pairs
[52:12] which pair of groups are actually
[52:13] different
[52:15] right so
[52:16] um so so in that case and so in this
[52:19] case you the type of um
[52:22] status quo test you would actually want
[52:24] to do is pairwise t-test
[52:26] comparing two simple means
[52:43] yeah i think yeah
[52:44] i'm mostly familiar with two groups like
[52:47] uh like a
[52:48] pairwise
[52:50] symbol t-test should we
[52:52] should be using this um scenario so yeah
[52:56] yeah
[52:57] um yeah and the last point on launching
[52:59] the new uh future i think you
[53:02] covered the essence of uh you know what
[53:05] what to do on that sense um yeah so
[53:08] overall you know you did a good job uh
[53:10] you provide a good structure in terms of
[53:12] how you responded to these questions um
[53:15] but really i think the main focus
[53:17] for you is that just make sure you're
[53:19] providing details that really matter to
[53:21] the questions and you're leaving out the
[53:22] details that don't that doesn't really
[53:24] matter okay um and so as long as you
[53:28] basically just continue to practice um
[53:30] you know come on these mock interviews
[53:32] with me and you know and basically just
[53:34] go through the uh practice questions in
[53:37] the subscription course then you know i
[53:38] think you'll be uh well prepared for the
[53:41] um
[53:43] uh the product interview at
[53:45] meadow
[53:47] thank you
[53:50] yep
[53:50] um great well i um i enjoy this mock
[53:53] interview with you and i look forward to
[53:56] more sessions like this with you in the
[53:58] future
[53:59] yeah thank you everybody appreciate your
[54:01] time
[54:03] yep
[54:03] sounds good all right thanks mark bye
[54:06] bye

FEEDBACK_MD:
---
section: "Solution + Feedback"
start: "29:40"
end: "54:08"
start_seconds: 1780
end_seconds: 3248
---

um your communication was good um it was very clear to unders it was you you expressed your ideas very clearly so it was very easy to sort of follow through what your um reasonings are right on each of the um questions that you were addressing so that's really good that you were doing that um the second thing i i liked about the overall approach of how you were pushing the problems were that your solution styles were very structured um so you didn't just kind of ramble you had a framework in terms of you know how you're going to respond to each of the questions um so that made things very easy to follow um as an interviewer um and that's really good that you were doing that um but i would say that there were there was one thing that i i would kind of um refine your response because i noticed that there were some moments when you seem a little bit hesitant or unsure about whether your response is correct or not um i would try to refrain from doing that um because you want to project confidence and if you're not sure about certain things um just don't bring that up at all so for instance you asked me about you know does meta is there a way for meta to generate um revenue like are there some advertisement display right um uh when you're not sure whether there is a particular future that already exists in the product or not it's best not to just bring it up um because if you bring it up then you can expect some follow-up questions on that and that can cause you some troubles later down the road um those who are watching this um that's actually one of the key things that um a lot of candidates often kind of make mistakes on you know they read some techniques off the internet um you know and then they they'll basically just kind of rehash it um and talk about it during the interview and because they don't really know like the actual reasoning or they don't know the exact details behind why um you know that technique taking is exists or whether a particular feature on a product exists then you know they they just sort of bring it up but then like when an interviewer asks follow-up questions they're not able to justify um so it's best not to bring up something if you're not really sure okay yeah i think that's a great quote yeah um so so projecting more confidence i think that's something you really need to work on um because in each of the three questions i noticed that you were kind of hesitant in terms of your response um and you really want to be able to project uh certainty in your responses um rather than hesitations all right so that's just a general overview of what i was kind of gauging um off of the uh you know off of how you're responding now let's go through each question on each question at a time so starting with the first question how would you measure engagement or meta support of device um so i think i i really love how you are approaching this with a good framework activation retention revenue however though you were kind of missing the main focus of this question which is engagement right if i would ask a question about how would you measure success on meta meta portal device right then that might be um accommodating for activation retention plus revenue in this case but then i'm more talking about the engagement so it's not so much about the monetization i care about it's more about the retention here right um activation activation being the secondary thing and the primary thing being retention um and so i would have loved to see more focus on these two categories and um it would have actually been fine if you just left out revenue because that wasn't the main focus of the question which is engagement um so that's something um to kind of look out for um really understand the differentiation between when um when anybody is asking how do you measure happiness measure satisfaction measure engagement measure success these fours sound the same but to on certain extent they're a bit different um and so make sure you have a clear understanding of what the question is and you're not just listing some arbitrary set of metrics but you're actually said listen metrics that actually answer the question okay yeah sounds good um oh sorry can i ask the question yeah go ahead good uh so like a um did you have other suggestions on like a um um brainstorm the make brainstormer matrix when we were asked about the question because sometimes i would be stuck on like okay this is the other this is all the measure i can think of on top of my head but i don't know whether um or less sufficient or like what will uh like when with brainstorm make sure it will be like a fair number of the magic which you bring it out in an interview yeah so i would say that just start with actually so that's a really good question um uh it's especially common questions i get from clients all the time but basically the ideal i think instead of the way you should be addressing these kind of metric based questions is um think about you know two to three categories of metrics um so you kind of did that here and then within each category it lists two to three measures so this or itself already provided a good decent comprehensive set of metrics yeah thank you um and and when it when it comes to these type of you know questions about um you know measuring um measuring a future or product um a natural sort of following question is like you know how would you prioritize which metric to focus on um so that is expected you know um so this is more like a shout out to those who are prepared for these data scientists you know product data science interviews um when you're when you're practicing you know yourself to just kind of make sure um you know think about how to measure a product but also when you list these metrics think about how you would prioritize them based on different vocals um so so that's why i asked the follow-up question which is you know how would you pick out these three metrics and then how would you rank order them right um and so considering the fact that you know really the main focus is engagement um i think it made sense to focus on the um active users um set of metrics across these three three different windows the only thing i wasn't really too clear on and i think this is something that you sh you should have clarified a bit more is the definition of of active so what does what does it mean for a user to be active and that's something that i i notice um clients will kind of gloss over which is that they will just spew out okay you know i'm going to measure dau uh w-a-o-m-m-a-u right but then they don't clearly define what are the behaviors that actually define actions um and a key action can be it can be a it can be a set of multiple behaviors or it can be just one behavior right um and in the in the case of the portal um you know there's all these different primary functions right you make a call um you know you i'm sure you can also uh you know browse on a web application as well right um you know you can uh you can you have this calendar app you can set up meetings and stuff like that right uh so these are all these different type of actions and so you know do you want the action the key action to be defined based on um calls only or do you want it to be expressed based on a set of actions right um so that's something to clearly define in this case [Music] and i think i think in this case um you know even though portal one of the cool portal's primary function is like the video calls um it still doesn't mean that you know some users might just use it only for calendar purpose right um and so and so in that case um you know i would just have like an inclusive set of okay um you know if users are active in the form of any sort of app engagement whether it's on a calendar whether it's checking email whether it's um you know making a call um any set of like in-app engagement um then that that then i would consider that as an active engagement gotcha yeah all right so now let's look at the av experiment part right um so even before you talked about success metric do you think there were there could have been one topic uh topic that you could have flesh out with the more on i think one thing uh i think one thing i was missing is probably uh i didn't ask like clarifying questions around why why this is important and how this feature tied to the overall business goal so i just i jump directly into a framework without asking yeah that's precisely right yeah so for those who are watching this um this is this is another sort of common mistake which is like um candidates have a tendency and i think it kind of makes sense because a lot of what we do are very technical focus and so we have a natural tendency to produce a technical response from the get-go um but we have to keep in mind that um you know data science project from the beginning and also the end right are always business focused um so we have a business stakeholder we're working with they provide a context of what their needs are um and then we basically provide some you know we basically understand it in terms of you know you know what the business context is translate that into some system technical methodology and then we deliver it back into the business right so we also have to think about it in terms of okay whenever we need to provide a response to these type of um you know product based questions the the structure is always business technical and then business um and so in this case what hank did was he primarily focused on the technical part it kind of glossed over the business elements in the av experiment itself um and it's really important to just also just cover the business part of it as well because because you know because the interviewers sort of gauging you know if this was an actual project that you were actually performing um you know in real life like how would you actually you know deliver this right and so you want to provide a glimpse so it's really important for you to cover the business aspect of this question as well um and so yeah like focusing on you know what is the purpose of this experiment right but also focusing on um clarifying what this new future looks like you didn't walk through the user journey of what the current um process is and you didn't also walk through the experience of you know what this new future would do um and you sort of um yeah like you know basically just kind of overlooked it so skipped it over right um so just make sure you kind of you flesh it out and in this case the call suggestion would essentially be like a ui and so you know you could kind of imagine you know if you um go if you go to like a call list right it just looks like an endless scroll of all these different numbers right so instead of having having to go through uh scroll to find the number that you want to actually dial um you know imagine like there's like a call suggestion at the very top maybe it's like top three calls um that are suggested to you based on the likelihood that you would actually you would your intent is actually to make uh make a call to that person right so imagine what the benefit would be right um maybe it could help save time maybe it can also improve engagement as well right um and so fleshing out the context um are just as important as covering the technical aspect of it as well so once you paint the picture of this from there um you know hank what you did right you know what you did in terms of laying out the structures are good yeah yeah i think that's a great uh advice and i want the most commonly uh mistake uh like i i sometimes will uh ignore i'm not gonna lie i forgot so like before we jump into any solution or like a brain like a provider framework we need to uh stress on like what is the business purpose of this question and also uh go through what's the user journey look like when they interact with this new feature uh like it provides some of the contacts around from the business perspective i think uh it will make the answer more complete so yeah i really appreciate it yeah yeah of course now i do want to walk through a couple things here um so i think you laid out a good um procedure of running an av experiment but i felt that there were a lot of there were a couple details or someone missing there um so okay so success metric the average number of calls per user you know that um i i i like the idea so i think that works um um because this metric wouldn't necessarily violate the statistical assumption that the observation is independent in this case right you're aggregating at the user level and so that's why this metric would work in terms of stating the hypothesis so i have a question for you um could it be possible that just having some ui with arbitrary arbitrary lesson numbers like that itself could have an effect um yeah yeah so let me just rephrase that so so basically um if you if you think about the call suggestion right there's really two elements to this right so there's the ui and then there's the algorithm right so when you're displaying this at the very top how do you know if there's an actual effect right meaning that people are engaging a lot more because of this um ui right how do you know if it is a ui that is actually driving the engagement or it's the algorithm itself that is driving the engagement or the interaction of both gotcha so we're talking about like like a confounding variable yeah essentially right yeah yeah so how do we really um so [Music] yeah so so in this case this would essentially be um kind of like a multivariate testing so your your control is that okay here's a version without any okay and then second and then the second test is basically um you know uh just a ui with an arbitrary like list of numbers uh you know list of calls okay and then the third one is uh ui plus the algorithm itself gotcha like a motor so so it's not it's not just like a like a two groups like a game um i see three groups so it could be three groups uh one control um you know one treatment treatment number one and treatment number two yeah and gosh like this is like a ui and the second one ui plus you know essentially you would be doing uh like a pairwise t-test so you're comparing the control against t1 and then comparing the control against t2 and then you look at the relative life along with the system significance yeah and then you make the decision that okay hey you know what um this algorithm you know uh basically this call suggestion with the ui plus algorithm um is so significant and uh you know with the relative left being positive the positive direction right um and you would uh conclude that you know essentially um you know you would want to rule out the call suggestion to um to a larger population of the portal device users gotcha yeah that's something i did i didn't think of when i when i was asked about this question like maybe like when we when we we uh talk about the ui change we also need to think about uh whether the like a confounding effect from other driver like algorithm itself can also make an impact so how do we really validate that so yes it's about observing the sensitivity of the metric right so um when you make certain change like how do you know that the change is coming from um uh you know from from you know changing the metric is coming from basically what like the condition they have changed right um you know or is there some sort of like uh extraneous factors that are in the play here right so it's just a lot about being a bit more keen um being able to kind of differentiate you know where is the effect really coming from yeah um and in terms of defining the statistical parameter alpha power md i would have loved for you to actually flesh them out instead of just saying okay i i will go ahead and list off a power name right so so you could have cited like uh you go ahead i know i so i asking so uh maybe elaborate more on each of these three uh components like what was the significance level and then how do we define the the statistical power or etc or because sometimes i feel like it's kind of like a common sense that like we need these three to determine what the sample size needed but really then touch on the details about each of these yeah um bring it up bring it out anyways yeah cause the interpreter doesn't know whether you actually know it or not right really the main focus here is to prove provide evidence that you do know how to run an ap experiment and so uh and so i would not um you know i i wouldn't i wouldn't i wouldn't avoid like i wouldn't you know like basically like bring up anyways right even if it's common sense per se or even if it seems obvious like um you know so it's so really important to bring out these details gosh yeah um so in this case you know you could have just started off by you know citing some industry standard numbers right obviously that can kind of change depending on the type of test that you're running and what are the type one and type two risks um you're willing to tolerate um you know when you're designing and running these type of experiments you know but standard set of values like alpha being set at like point zero five power being a point eight um and and md um you know being somewhere between one to five percent in this case um actually let me truncate that value to like one to three percent um one to three percent would have been reasonable um and of course like you know you might expect the interviewer to ask you some additional follow-up questions about you know um you know like why do you like okay so putting outside industry center values like you know why can't you set the alpha at point one or power at point seven or md like at five percent or something like that right um in mid case then you know you can kind of follow up um on you know different values that you may want to explore gotcha yeah um yeah yep um yeah and uh randomization unit makes sense um estimating the experimentation uh basically the experimentation time set of two weeks makes sense um the only thing you forgot to mention is like how would you determine a sample size um so yeah so you would have you would have had to determine a sample size after step three um right yeah on determining uh yeah and you also it should come before determine the time right yeah once you know what the sample size is then from there um you uh you basically can figure out what the experimentation time partners yeah yeah yeah go ahead sorry yeah and and um do mention the statistical types you would be using in this case um yeah so i was saying the two sympathy tests yeah yeah because we are measuring the like a mean value across like a multiple groups but in this case right now we have three groups so maybe we should use anova instead no um so anova would only give you um if at least one um at least if at least one pair of the groups are different but it wouldn't give you information uh sorry if at least one group is at least if at least one group is different from all the other groups that's what donova will provide it wouldn't necessarily give you um information on um which pairs which pair of groups are actually different right so um so so in that case and so in this case you the type of um status quo test you would actually want to do is pairwise t-test comparing two simple means yeah i think yeah i'm mostly familiar with two groups like uh like a pairwise symbol t-test should we should be using this um scenario so yeah yeah um yeah and the last point on launching the new uh future i think you covered the essence of uh you know what what to do on that sense um yeah so overall you know you did a good job uh you provide a good structure in terms of how you responded to these questions um but really i think the main focus for you is that just make sure you're providing details that really matter to the questions and you're leaving out the details that don't that doesn't really matter okay um and so as long as you basically just continue to practice um you know come on these mock interviews with me and you know and basically just go through the uh practice questions in the subscription course then you know i think you'll be uh well prepared for the um uh the product interview at meadow thank you yep um great well i um i enjoy this mock interview with you and i look forward to more sessions like this with you in the future yeah thank you everybody appreciate your time yep sounds good all right thanks mark bye bye

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
Write JSON only to: splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.json \
    --video transcripts/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26//video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.json --out splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.qa-split.json \
    --video transcripts/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26//video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.validation-report.md

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
video.md: transcripts/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/video.md

--- CHAPTER `01:55` — Measure engagement on Portal ---
window: 01:55 .. 10:55
recognition_status: single (1 items)

ITEM #2
  interviewer_question: time=10:26 text="um now can you kind of pick out maybe like three metrics that you think would be important so suppose that you need to create some sort of a dashboard for um you know let's just say an executive right um who's part of the device and hardware team right and they're gonna be the ones that are looking at this along with other product managers in that vertical in that horizontal um you know basically the business of the hardware within meta um can you think about what three metrics you would want to display and then rank order those metrics from important"
  candidate_answer: time=11:00 text="gotcha so uh let me let me reframe what i just heard to make sure i understand the question correctly so basically assuming that we are building a negative analytic dashboard like empowering our business holders it can be product manager or executives to measure the effectiveness of this product so on like a uh the question is about like picking three main primary metrics that can like a help them monitoring the metrics over time um so cool um let me take a quick minute to organize my thoughts um yeah i think [Music] so i think the first and then ranking in the importance based on the importance level so i think uh the first um i didn't know what um i think the first primary metry i will look at is the video uh video like a call time in in minutes in hours um per month so because like as you mentioned the audience might be like a leadership or a security so like they will probably care the more about the like a high level overview how much i get total time uh they spend on this product over time and then also to see whether um like they do more uh video calls uh with uh this new launch product uh so like a um and i get this another reason why i picked this machine is this make sure also embodies all all the other like interaction like we talked about like a we do a video course or or like a set up meeting playing lucy so like the more activities they uh took um with this device no more time spent on so it's actually not that a video call time i will be like a little bit um like a time spent on hours and uh sorry type of spam in all around on photos um so yeah and then i think the secondary matrix i will look at would be because like i think one of the core functionality with portal is the video call so i want to like know what's the total number of the video calls per month so total number of video calls per month um i think this will on a day so we uh the reason for that would be uh i i would like to know whether uh uh like a whether um like a with these new products uh users are easier to do a video course or they will um like jump on the video call with their family or friends more frequently so uh and then lastly uh i will pick one from the revenue so um and for the monetization perspective on like a like a revenue per month so uh i think that will be like a um i'm not quite sorry i'm not quite sure about how the ass will embed it on the portal like a fun face from the meta news feed we know like it when you go through the post the no you will you will probably see some like a sponsored ass but i have a portal on like a could you like it give me some uh direction about like a how the from the advertising side how that would be embedding within this product or yeah sure so so leaving a monetization site then i will um like a doula on like retention like a diu and user i think this is like for all the uh meta products uh so we care about like a daily activity so weekly i've used them on the active users so like they're having this um actually like having the active users uh on the dashboard will be give give our audience a better understanding of how how our uh how our products being used by the users and then their active new needs so yeah does that make sense okay"
  reference_answer: time=None text=None
  interviewer_feedback: time=15:15 text="um yeah so um in this case let's just assume that there's really no like advertisement that are displayed in the portal device itself um so i wouldn't so just kind of going back to original questions which is just focusing on engagement um just leaving that monetization aside can you think about perhaps any other metric that you may want to display in this metric based dashboard yeah that's good"
  question_topic: Product Metrics

--- CHAPTER `10:55` — Prioritize metrics ---
window: 10:55 .. 18:19
recognition_status: multiple (2 items)

ITEM #3
  interviewer_question: time=16:27 text='now how do you so among these three metrics you have outlined um how would you go ahead and prioritize them from ranking from one to three'
  candidate_answer: time=16:34 text="sure so far name ranking one two three on us per month um i think uh let me move the daily attribution to the first one um um so i think the first that i think the problem images should be that you have the user with three user monthly active users and then by different like a segmentation by a country region all different uh like a language etc and then like because like um we have to the reason the main reason for that is um this will serve as the uh retention uh metrics like we just we don't want just like a launcher product and user just use once or twice and then put that put that away so that this will be served as the measure to know how like it what's their retention look like um so this will be my primary primary matrix and then secondly as i mentioned the time spent is also critical as that it will like tell us about how like a um how much time is spent with on a portal and then like a and in a and then what's their interactions um and yeah and that's least total number of video calls yeah just damage okay"
  reference_answer: time=None text=None
  interviewer_feedback: time=18:07 text='okay got it um all right now'
  question_topic: Product Metrics

ITEM #4
  interviewer_question: time=18:11 text='i have a new question problem for you the third question i have is following suppose a new feature is introduced on portal which is called call suggestion this future recommends calls to users how would you design an ap experiment on this feature um suppose a new feature introduced in portal uh which is called code suggestion you just design'
  candidate_answer: time=18:44 text="um so uh so the question is about how do we really um like design the uh experiment i think there are a couple of steps we need to follow when it comes to the experiment um first like they we need to state the uh hypothesis testing uh oh no i think first of all we need to define what was the success matrix like uh what are um like a what are we going to make sure uh okay um when we launch this new feature so i think the step one will be okay what what will be this assessment should look like so matrix and then like a i assume that um with this new features the purpose is to make users more easily to uh start a call start a call and then which will better the number of the calls will be in work will increase accordingly so i will i will pick uh um i will pick up average number of video calls per users as the nature we are going to make sure does that make sense or so average like a number of video have calls on per user and then secondly uh like a uh so like we need to define let's state the hypothesis testing so all i think the number uh here the null hypothesis will be uh the average number of the core per users um between the control and treatment group will be the same and alternative hypothesis will be the um um the average number of the uh average number of cost per user between two groups out on are different and then like we need to follow by uh we need followed by like i define the uh significance level uh statistical power and then the mde to determine how much uh same process uh we need and then um so let me let me put it down like i say the five pounds like a significant level uh power and the mde so alpha alpha like a power and like a md and then and then and then also we also need to determine what's the like a randomization unique so i think this is kind of like a um again or like a uh because like i will assume like in this setting the observation you need is the customer so uh like it's better we can we can perform a randomization at the customer level and then and then like a another uh also we've just talked well um we just focus on the user who own the portal device right otherwise we could we could like measure these features the effectiveness of this feature so i will be like a customer who own like a portable device yeah and then once we have that like a we are able to uh and again estimate the on like a experiment [Music] xp re augmentation [Music] time so um usually like a typical like a experimentation time in every testing on like usually it will last for like one week or two weeks on the reason for that if we if it is a short experimentation then it will probably be problematic given there's a um like a day of the week effect unfortunate for instance like a users tend to do a video call on the weekend or on a weekday so uh like the best practices will be usually um do like at least more than two weeks um so here i will use the two weeks yeah and then after that um how would you design and then after we gathered say two weeks of the data then we are able to uh use the um um uh two symbol t tests to to make sure the uh the leaf between the leaf in the metric uh across control and experiment and the treatment groups are actually achieve statistically uh significance um so that's like and by checking the p value and so um [Music] yeah and yeah and then after say given that the like a p value is less than 0.05 0.05 and like it it will be like a to decide like whether we should launch this new feature or not but like it's not it's not just um feature oh um by the way uh like when we uh something i didn't mention about is that uh we other than just pick one success symmetry it's better we can also have some of like a gar rail mattress which is like a geometry which that which shouldn't be degraded in pursuit of this assessment tree um so uh in here i will use the um the um i think like as revenue or 10 spend um portal as the gabriel so like a like as a career metric but like a um on the last step is to launch the new feature or not on and other than checking the statistical uh significant result from experimentation we also need to involve the business holder to see what's the um like a practical significance look like and also do some uh like a cost and benefit analysis to make sure it's gonna likely take too much resources to launch these new features um so now that would be the next step yeah does that make sense okay"
  reference_answer: time=None text=None
  interviewer_feedback: time=20:09 text="yeah that's good sounds good um and you so you define some good structure there but um"
  question_topic: Experimentation

--- CHAPTER `18:19` — AB testing on the 'Call Suggestion' feature ---
window: 18:19 .. конец
recognition_status: multiple (2 items)

ITEM #5
  interviewer_question: time=26:08 text='but in terms of uh are there any other details you may want to populate uh any other detail um'
  candidate_answer: time=26:17 text='so i think like a um i think i will add more details around um like this closer i think um that sounds like a we need to also do something like a like a um velocity checks for example uh to make sure that the um like a um observation we gather should be independent uh with each other and also whether there sounds sensational seasonal or holiday holiday effect and also another effect i can think of is like novelty effect which means that when the new features uh uh on a product appears uh given its novelty you should probably may respond to this feature positively at first but like but over time uh the novelty of the feature will waste off then the behavior will return to normal so we need in that case we should probably uh extend the like a experimentation to get more data to validate that so yeah'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Experimentation

ITEM #6
  interviewer_question: time=27:26 text="what do you think would happen if this change was made over a let's just say christmas weekend"
  candidate_answer: time=27:39 text="yeah then i think like a uh if we like a uh lunch experimentation during the holidays like christmas then we will probably see the uh we um like a the final result is um like a kind of like inflated or overly uh optimistic because like people um especially during the kobe most people cannot go home to like they have a family reunion so like they will probably do more video calls like a during holiday so in that case we will probably gather inflated uh average number of calls per user like during this during this time so uh in order to um um um to get a better reliable result we should probably um um like a alright we should probably uh gather more data and like because i'm assuming like um so yeah so probably like extend the experimentation time um yeah does that make sense or"
  reference_answer: time=None text=None
  interviewer_feedback: time=28:56 text='okay'
  question_topic: Experimentation

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/datainterview/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26/data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
