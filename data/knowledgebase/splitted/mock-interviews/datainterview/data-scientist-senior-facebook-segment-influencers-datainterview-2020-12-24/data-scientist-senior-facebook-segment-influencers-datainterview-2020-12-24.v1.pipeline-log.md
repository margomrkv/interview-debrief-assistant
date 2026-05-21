<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24",
  "transcript_folder": "transcripts/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/",
  "source_id": "data_scientist_senior_facebook_segment_influencers_datainterview_2020_12_24",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:05:21 +0200",
  "updated_at": "2026-05-20 21:12:41 +0200",
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
    "json": "splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24//timecodes.txt",
        "en",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.pipeline-log.md"
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
        "splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.pipeline-log.md#LLM_INPUT_STEP_2"
      ],
      "outputs": [
        "splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.json"
      ],
      "status": "completed",
      "duration_sec": 180.0,
      "notes": null,
      "finished_at": "2026-05-20 21:12:41 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:12:40 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24//video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 0.0,
      "notes": null,
      "finished_at": "2026-05-20 21:12:40 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/`
- **Source ID:** `data_scientist_senior_facebook_segment_influencers_datainterview_2020_12_24`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:05:21 +0200
- **Last updated:** 2026-05-20 21:12:41 +0200

Фильтр в IDE: `*data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24//timecodes.txt`<br>`en`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.pipeline-log.md` | — | completed |
| 2 | qa_extraction | yes | claude-sonnet-4-6 | `splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.pipeline-log.md#LLM_INPUT_STEP_2` | `splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.json` | 180.0s | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24//video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.validation-report.md` | 0.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.pipeline-log.md`

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
SOURCE_ID: data_scientist_senior_facebook_segment_influencers_datainterview_2020_12_24
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/
INTERVIEW_LANGUAGE: en
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00] hey how's it going good how are you
[00:03] doing
[00:04] very good so thank you for being a
[00:07] interviewee for this mock interview so
[00:09] this small interview is going to
[00:11] mimic a facebook data scientist
[00:14] um analytic interview um interview style
[00:18] um and this is gonna be a three minute
[00:21] round and what we're gonna do is we're
[00:23] gonna go through
[00:24] some statistics questions for the first
[00:25] 10 minutes
[00:27] follow my um sql questions for 15
[00:29] minutes
[00:30] yeah and then we'll use the remainder of
[00:32] the time on an analytic case study
[00:34] do you have any questions on that before
[00:36] we proceed
[00:38] no that sounds good thank you okay
[00:40] awesome
[00:41] all right so i'm gonna go ahead and
[00:44] actually use this quarter pad and feel
[00:45] free to make notes
[00:46] um as much as you want um really you
[00:49] know just treat this as so it's your
[00:51] uh it's your white board okay so let's
[00:54] start with the first question
[00:55] can you can you explain to me um what is
[00:59] a beta coefficient of a multiplier
[01:00] regression
[01:02] uh yeah for sure so the beta
[01:06] if we um
[01:11] sorry let me think about how to frame it
[01:13] um
[01:15] so a multivariate regression describes
[01:18] the relationship between the left hand
[01:21] side variable the outcome
[01:23] and a series of right hand side
[01:25] variables
[01:26] let's call them the independent
[01:28] variables and the beta coefficient
[01:30] describes
[01:31] how the outcome changes in relationship
[01:34] to changes in the
[01:38] independent variables so if the
[01:41] independent variable changed by one
[01:43] and the beta coefficient is on that
[01:46] variable
[01:46] is beta for example then the outcome
[01:50] would change by beta
[01:52] is um that makes sense so how would you
[01:56] actually derive the coefficient
[01:58] of the uh of a linear model in this case
[02:02] um yeah there's a sort of a well-known
[02:05] solution um analytically which is
[02:09] that i can write it actually here
[02:13] which is that the beta
[02:16] beta vector is
[02:20] um x prime y
[02:24] um times
[02:28] x prime the inverse of
[02:33] x prime x and here
[02:36] the um the x
[02:40] is uh the here x represents the matrix
[02:45] the independent variables and y
[02:48] represents the vector of outcomes
[02:50] yeah okay that makes uh that makes
[02:52] perfect sense yeah so
[02:53] prime in this case would be your uh your
[02:55] transpose
[02:56] yeah exactly got it um now how would you
[02:59] how would you um how would you estimate
[03:03] it without
[03:04] using so i believe what you're using the
[03:05] least squares approach but is there any
[03:07] other ways
[03:08] a different way of estimating the beta
[03:11] coefficient
[03:13] um yeah so we
[03:16] could use a maximum likelihood
[03:18] estimation for it
[03:19] um for example um and do like a
[03:23] optimization exercise on that to
[03:25] maximize
[03:26] the the likelihood function okay got it
[03:29] all right that makes it
[03:30] make sense all right so let's talk about
[03:34] the next question um now suppose that
[03:37] your target variable is inflated with
[03:39] zero um
[03:40] how would you actually going about
[03:42] approaching that problem um
[03:46] so if my data is um
[03:51] zero uh if my target variable is zero
[03:54] inflated i think the first question
[03:56] that i would ask is is there
[03:59] some type of censoring that is happening
[04:01] with
[04:02] um the target variable to cause these
[04:06] zeros
[04:06] or are these zeros like actually um
[04:10] the values of uh that we're interested
[04:12] in got it that's a really good
[04:14] point um but now let's just presume that
[04:16] in this case
[04:17] um it is an actual value um and let's
[04:20] see that the
[04:21] presence of zero so this is actually a
[04:23] non-negative
[04:25] um continuous distribution and um
[04:28] the presence of zero uh is uh has
[04:31] is it's about eighty percent of your um
[04:34] of your observations
[04:35] um in this case how would you how would
[04:38] your model
[04:39] uh model this type of data
[04:42] yeah that's a great question um
[04:47] i believe that there are statistical
[04:51] methods that help you deal with
[04:54] variables that are
[04:57] that follow distributions like this so
[04:59] the probit model or the tobit model for
[05:02] example
[05:03] can handle target variables that are
[05:05] particular like this one
[05:08] if we so that's that's sort of one
[05:11] statistical modeling approach that we
[05:13] can take
[05:14] alternatively i think just for like
[05:16] sanity checks and
[05:17] um understanding the data more we can
[05:19] also just
[05:21] model the target variable as being zero
[05:24] versus not
[05:25] running maybe a regression to see um
[05:29] how the beta coefficients look like and
[05:32] then
[05:33] proceeding with like the original
[05:36] modeling with the original variables
[05:38] okay got it all right that makes sense
[05:40] um
[05:41] now let's move on to the next question
[05:44] um can you just can you um explain what
[05:48] a confidence interval is
[05:49] of a logistic regression model
[05:53] uh yeah so and the confidence interval
[05:56] meaning
[05:57] um the confidence intervals on the beta
[05:59] coefficients
[06:00] i'm assuming yeah yeah yeah so
[06:04] the confidence intervals um
[06:08] represents uh so let's say we have like
[06:11] a 95 percent
[06:12] confidence interval um and the
[06:15] statistical interpretation of that is
[06:17] that um
[06:20] they're like 95 of the time
[06:23] the actual beta coefficient will fall
[06:26] into
[06:26] the confidence interval that we
[06:28] estimated
[06:30] um and and that represents sort of
[06:33] um our our uncertainty around
[06:36] this this variable okay got it
[06:39] well now what if um so the
[06:43] the uh the beta coefficients of the
[06:46] logistic regression
[06:48] could either be in logos or alts ratio
[06:51] right
[06:53] um now let's presume that
[06:56] there's a presence of zero
[06:59] um in either one of those cases
[07:02] what does that mean presence of zero in
[07:06] the confidence interval then what would
[07:07] that mean
[07:09] in terms of the statistical significance
[07:11] of of its
[07:12] uh predictor oh i see so
[07:17] um you you're asking
[07:20] what does it mean if your confidence
[07:22] interval includes zero
[07:24] yes yes in either cases where
[07:27] it's either already in log odds or odds
[07:30] ratio
[07:32] uh beta coefficient because the logistic
[07:34] regression model can be in both forms
[07:36] yeah exactly um
[07:40] so i think my interpretation with that
[07:42] would be that the beta coefficients are
[07:45] not statistically distinguishable
[07:48] distinguishable from zero um
[07:51] and yeah uh if you were to do hypothesis
[07:55] testing on
[07:56] that coefficient then you would not
[07:58] reject the null hypothesis
[08:00] okay so if it's uh so if the coefficient
[08:03] is already it's in the log odds form
[08:07] um uh would it be
[08:10] possible to have a value of zero
[08:15] oh i see um
[08:18] right so yeah in that case i
[08:23] don't think that's possible
[08:29] right because it would be yeah sorry if
[08:32] the
[08:33] predictor doesn't is uncorrelated with
[08:36] the
[08:36] um outcome variable then the logos ratio
[08:39] should actually be one
[08:40] instead of zero um
[08:44] and it's not actually possible to have a
[08:47] zero value for that
[08:50] okay now what if it wasn't uh what if it
[08:53] was involved ratio
[08:54] if the if the confidence interval
[08:58] has has um
[09:02] one what does that mean in terms of its
[09:04] uh
[09:05] statistical significance so let's just
[09:07] say that the
[09:08] odds ratio confidence interval falls
[09:11] somewhere between
[09:12] um point two
[09:15] [Music]
[09:16] four and point
[09:19] one uh one point two four what does it
[09:21] mean in terms of its
[09:22] statistical significance um
[09:25] then in in which case because it
[09:27] includes one it's uh
[09:29] if you were to do a hypothesis testing
[09:31] exercise you
[09:32] would not find that it's statistically
[09:36] significant
[09:37] okay got it all right thank you um okay
[09:40] so we're going to move on to the
[09:42] uh x sql question um
[09:45] so i'm going to go ahead and paste the
[09:48] table
[09:49] so this is a a
[09:52] basically a snippet of
[09:55] uh of the message um
[09:59] table set um and it contains your user
[10:02] id username
[10:03] the date and the message the number of
[10:06] message sent and the message
[10:08] the number of message received a given
[10:11] user on a day-to-day basis
[10:13] now go ahead and try to address the
[10:16] first question
[10:17] which is for each day return the name of
[10:20] the user
[10:21] or in this case you can return the user
[10:23] id who receive the
[10:25] highest message sent to message received
[10:28] ratio and this message
[10:30] ratio is your message
[10:34] sent divided by message received
[10:37] got it um yes i think
[10:41] the first question that i would or the
[10:45] first
[10:45] thing that i would check for in this
[10:47] data
[10:49] database would be whether there are
[10:51] missing values in either
[10:53] um in you know any of these columns and
[10:57] in the following analysis i'm just going
[10:59] to pre i'm just going to assume that
[11:02] there
[11:02] aren't any missing values and the second
[11:05] thing that i would
[11:07] think is important is
[11:10] whether message received could be zero
[11:13] because then you have a division by zero
[11:15] issue that may need to be addressed
[11:19] okay so i'm not
[11:26] select
[11:40] so
[12:08] so
[12:28] [Music]
[12:36] um
[12:41] so here i'm creating uh you know i'm
[12:43] selecting the user name variable
[12:45] and i'm also creating a new variable
[12:48] called
[12:49] uh sent to sent to received ratio
[12:53] which computes the ratio between message
[12:56] sent and
[12:57] message received and here i'm marking
[13:01] the message received variable as null
[13:04] if it's equal to zero so that the
[13:06] division will also result in a null
[13:11] okay
[13:18] um oh
[13:21] and i guess the question
[13:25] that i then want to ask is
[13:28] how we want to
[13:32] um treat these users do we
[13:36] um do we see them as having the highest
[13:40] ratio yeah
[13:43] like basically like okay for october 1st
[13:46] 2020 user xyz
[13:51] had the highest ratio i say so you
[13:54] actually want to set
[13:55] it to like a really high number
[13:58] um so that it would come on top when you
[14:01] sort
[14:02] um when you sort it precisely
[14:06] off of a given day so you want to you
[14:08] want to do some kind of screening
[14:11] on a given day got it okay
[14:14] in that case i think marking it as a
[14:16] null may not be the
[14:17] best idea um
[14:22] let's actually kind of simplify this for
[14:24] a bit so let's just presume that
[14:26] um there is no zero in the denominator
[14:29] and it's already it's always
[14:30] populated so how would you go ahead and
[14:32] proceed with that problem then
[14:34] okay yeah that sounds good um in that
[14:37] case
[14:37] um i'll just do a simple division to
[14:39] calculate the ratio
[14:42] um and we want
[14:45] to
[14:49] group by date um so that we
[14:53] return one user for each date
[14:57] and the other question is do we are we
[15:00] interested in returning um multiple
[15:04] users for each day if they have the same
[15:07] highest ratio
[15:08] for each day good question so in this
[15:10] case um
[15:11] let's let's presume that um it's just
[15:14] you just return one user in that case
[15:16] okay so any user in that alien user
[15:20] yeah okay yeah it sounds good um
[15:26] um i think in this case i want to do
[15:29] like a
[15:30] a window function so
[15:34] um i'll create
[15:38] another
[15:42] new variable which is
[15:51] let's call it rank
[16:03] and since you said that it's okay to
[16:07] just return one user i'll calculate row
[16:10] numbers
[16:12] over partition by
[16:15] date order by
[16:21] the ratio
[16:49] um
[16:53] oh actually i don't need to group by
[16:56] date
[16:57] um i just have to select
[17:04] all right because equal to one
[17:07] which is the highest um
[17:11] center received ratio but user what's
[17:14] the highest
[17:16] ratio um
[17:24] okay
[17:27] so final solution or do you want to make
[17:30] any kind of revision
[17:32] um
[17:36] yeah i think that's the final solution
[17:39] okay
[17:39] got it um so i'm going to give you
[17:42] another question
[17:44] so in this case
[17:48] um now let's just say that uh for each
[17:52] user return the first date
[17:53] when the user received zero message
[17:58] mm-hmm return the first date when the
[18:03] user received zero message
[18:06] and uh if the user never received
[18:09] zero message um
[18:13] do we then in that case like
[18:16] those users wouldn't wouldn't matter so
[18:18] basically for
[18:19] user we just want to see uh what
[18:23] so among the users who receive zero
[18:25] messages
[18:26] when when was it that they received that
[18:29] zero message for the first time got it
[18:32] yeah that makes sense
[18:34] um so i would select
[18:37] uh let's say we return username
[18:41] um
[18:46] messages which is database and
[18:49] we are only interested in cases where
[18:54] message received is equal to zero
[18:59] um and we also return the first day
[19:03] which is
[19:03] min date as
[19:07] um wait for each user
[19:12] um oh actually um
[19:15] sorry my bad we we only return one
[19:19] observation for each user so i'm gonna
[19:21] group
[19:22] my username assuming that both user id
[19:25] and username
[19:26] are unique
[19:30] okay yeah
[19:36] okay so what you're basically doing is
[19:38] you're aggregating at the user level
[19:40] uh after you apply the filter where
[19:42] you're only looking at the entries that
[19:44] have
[19:44] zero in the method you see um
[19:48] and then for each of the user you wanna
[19:50] you're extracting the minimum
[19:52] date yeah exactly okay got it
[19:56] um all right so that's uh that's pretty
[19:59] much it for the sql um let's move on to
[20:01] the next
[20:02] uh section which is on the analytic case
[20:04] study
[20:08] so this is
[20:11] so the so this this uh question
[20:14] is based on instagram and
[20:17] what instagram is trying to do is
[20:20] identify users who are influencers
[20:23] so how would you help instagram define
[20:26] um whom the who who which users are
[20:29] influencers or not
[20:33] yeah to kind of getting to to get
[20:35] started on this question i think the
[20:37] first
[20:38] um clarifying question maybe that i
[20:41] would ask is how
[20:42] we define a user as an influencer um and
[20:46] i think there might be
[20:47] several ways to defining them
[20:50] um definition
[20:54] we could determine that a user is an
[20:57] influencer if they have you know a huge
[20:59] amount of influence on instagram so
[21:01] maybe
[21:02] if their number of followers
[21:09] exceeds a threshold then
[21:13] we define them as an influencer or if
[21:16] they're
[21:19] if or if they have specific
[21:23] posts that are particularly popular so
[21:26] maybe
[21:27] not many people follow them but some of
[21:30] their posts went viral
[21:32] and so maybe the number of overall views
[21:35] of your posts could also be
[21:39] used as a criteria for determining
[21:41] whether an user is an influencer
[21:43] the other thing um that
[21:46] you know moving away from these
[21:48] definitions a little bit is whether a
[21:50] user is being paid for
[21:51] certain content that they post on
[21:53] instagram so
[21:55] um whether they do any paid ads
[21:59] um and maybe if they do we can define
[22:01] them as an influencer
[22:04] uh should i proceed with any particular
[22:07] one of these definitions
[22:08] or uh well i think so i think those are
[22:12] good so
[22:12] number of uh number of followers that
[22:14] they have number of
[22:16] uh overall views that they have on posts
[22:18] and then if they have any paid ads
[22:21] um those are the criteria criteria that
[22:24] you would use
[22:25] to um to identify the user as an
[22:28] influencer or not right
[22:30] yeah okay um now now
[22:33] uh so the so those are the measures now
[22:36] how would you actually
[22:38] bend the users into influencer or not
[22:41] bucket um yeah i guess
[22:45] in order to do that i would love to
[22:48] understand a little bit more
[22:50] about like what this definition is used
[22:53] for um so
[22:54] is is the team instagram interested in
[22:58] maybe
[22:59] getting more users into the influencer
[23:01] bucket
[23:02] to promote their business or um
[23:05] are we trying to cluster
[23:08] users into influencer versus not in
[23:11] order to
[23:11] do some kind of targeted experiment or
[23:14] targeted
[23:15] feature design or something like that
[23:18] in this in this in this um uh
[23:22] case uh we want so instagram
[23:25] um you know wants to promote um
[23:28] wants to match advertisers with
[23:30] influencers
[23:31] so uh we need to identify with the you
[23:34] know who the users are are they
[23:35] influencers or are they
[23:37] you know just regular consumers um this
[23:40] is where
[23:40] you need to help the team um define that
[23:45] yeah that's very helpful context um and
[23:48] so i guess
[23:50] in that case uh i can refine my
[23:53] previous criteria a little bit more so
[23:56] we
[23:56] are not primarily interested in
[23:59] who is being paid for ads um but
[24:03] instead like who has the potential to
[24:07] um serve as an influencer on instagram
[24:11] and generate ads revenue for advertisers
[24:14] um yeah and um
[24:17] sorry what was the sorry what was your
[24:20] previous question
[24:23] so so uh so like how would you actually
[24:26] define
[24:26] that criteria saying okay
[24:29] these are the users who are influencers
[24:33] yeah it's kind of like if you were
[24:36] building like a fraud model
[24:37] saying okay this is a buster or not
[24:40] mm-hmm
[24:40] yeah representative um so similarly how
[24:43] would you
[24:43] should do that for the users bucket them
[24:47] into influencer or not
[24:50] and have the model
[24:54] so i think there are two ways
[24:57] of approaching this problem and i would
[25:01] classify them into um you know the
[25:04] unsupervised approach
[25:08] uh versus supervised approach
[25:14] um in the unsupervised approach um we
[25:17] are
[25:17] interested in finding clusters within
[25:20] the
[25:21] user um within the list of users
[25:24] of instagram and trying to find the
[25:27] clusters that are
[25:30] that has a huge amount of influence in
[25:32] the supervised approach
[25:34] we would essentially try to
[25:37] obtain some type of labels on whether a
[25:40] user is currently
[25:42] an influencer um and try to classify
[25:45] the remaining users into having the
[25:48] potential to
[25:49] to become an influencer versus not okay
[25:52] yeah so and and i think the key
[25:54] distinction between these two approaches
[25:56] is that
[25:57] um in the supervised approach we have to
[25:59] come up with some ways
[26:00] of creating the label in the first place
[26:05] okay um so how would you go on about
[26:08] creating a label
[26:10] yeah so if we were proceeding with this
[26:13] um
[26:14] approach one way is to
[26:17] try to collect information on whether
[26:20] they have
[26:22] any paid ads in their um current
[26:25] in instagram posts okay and
[26:28] um i am not a hundred percent sure if
[26:32] this is true but i remember
[26:34] seeing some of the um influencer having
[26:37] these posts
[26:38] that are kind of labeled as
[26:39] advertisement
[26:41] and if instagram collects that sort of
[26:43] data then
[26:44] um that could serve as a useful label
[26:48] for this problem okay um
[26:52] all right now i'm gonna i have i have a
[26:54] follow-up
[26:55] um so now let's
[26:58] suppose that you do have this
[27:02] uh instagram influencer bucket
[27:05] now how would you go ahead and
[27:09] um and segment the influencer population
[27:12] so i'm going to paste the question here
[27:18] yeah and i imagine that
[27:21] the reason that we want to segment these
[27:24] influencers maybe
[27:26] to group them into different um
[27:29] categories
[27:30] so that advertisers with different
[27:33] needs can be matched to different groups
[27:35] of influencer is that right
[27:38] got it yeah and so
[27:41] i think you know what type of influence
[27:44] they have would be
[27:45] um really the prime the primary um
[27:49] variable of interest to us because we
[27:51] are interested in
[27:52] knowing what type of population they
[27:54] attract
[27:55] so if they are like a fashion blogger um
[28:00] let me write some potential categories
[28:05] um maybe they are like a fashion blogger
[28:08] or
[28:08] they are i am uh they post mainly
[28:12] political content
[28:14] um etc and so they their posts the
[28:17] content of their posts may say
[28:19] uh may wrap may generate a good signal
[28:22] for um what type of crowd they attract
[28:26] um so and so
[28:31] treating this as one of the features is
[28:34] um
[28:35] content uh
[28:38] content of posts and maybe
[28:42] we can do some computer vision type
[28:44] analysis or uh
[28:45] natural language processing analysis on
[28:48] the content of these posts to extract
[28:50] keywords and group them into categories
[28:52] um the other feature that i have in mind
[28:55] is
[28:56] the type of um users that follow them so
[28:59] they're
[28:59] followers um
[29:03] and if their users um
[29:06] [Music]
[29:07] you know label themselves and then you
[29:09] weigh on the
[29:11] instagram profile then we can get a
[29:14] pretty good sense of
[29:15] how what type of population they're
[29:19] attracting and the potential
[29:20] advertisement
[29:22] revenue they can generate
[29:29] yeah so these are the two main types of
[29:33] features that i can think of i don't
[29:35] care at this moment you identify the
[29:37] signals
[29:37] um now now with using the signals how
[29:41] would you actually
[29:42] perform the segmentation itself
[29:45] yeah um so say that
[29:48] we um use maybe some machine type of
[29:52] machine learning models to analyze their
[29:54] posts and
[29:55] the text that they post um and we can
[29:58] get uh sort of embeddings of
[30:02] um and we can get like
[30:05] embeddings of their content then we can
[30:08] perform
[30:10] a unsupervised clustering algorithm
[30:17] to try to group these influencers into
[30:20] different groups
[30:22] so one of the simplest models that we
[30:24] can i can think of is the k-means
[30:26] clustering
[30:26] okay there are many modifications of
[30:29] this that
[30:30] serves different purposes but yeah this
[30:33] may be a good
[30:35] starting point okay um and one last
[30:38] question and then we're done with the
[30:39] session
[30:40] um is how would you evaluate your
[30:43] cluster then
[30:46] um that's um that's a good question so
[30:51] evaluation um
[30:55] i think you know one way that i can
[30:58] think of on top of my head
[31:00] is if we get some human raiders
[31:03] human labelers to look at these
[31:05] influencers and then group them into
[31:07] categories
[31:09] and we can compare the human evaluation
[31:12] with the results that are generated from
[31:16] the algorithms okay got it
[31:19] got it all right yeah so that wraps up
[31:22] the session um thank you for
[31:24] uh being a participant as an interviewee
[31:27] for this mock interview
[31:28] um and i hope you have a good day
[31:32] yeah thank you so much for this question
[31:34] appreciate it
[31:35] yeah thank you

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
Write JSON only to: splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.json \
    --video transcripts/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24//video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.json --out splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.qa-split.json \
    --video transcripts/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24//video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.validation-report.md

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
video.md: transcripts/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/video.md

--- CHAPTER `00:00` — Statistics Questions ---
window: 00:00 .. 09:50
recognition_status: multiple (11 items)

ITEM #1
  interviewer_question: time=00:34 text='do you have any questions on that before we proceed'
  candidate_answer: time=00:38 text='no that sounds good thank you'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:40 text='okay awesome'
  question_topic: Communication

ITEM #2
  interviewer_question: time=00:55 text='can you can you explain to me um what is a beta coefficient of a multiplier regression'
  candidate_answer: time=01:02 text="uh yeah for sure so the beta if we um sorry let me think about how to frame it um so a multivariate regression describes the relationship between the left hand side variable the outcome and a series of right hand side variables let's call them the independent variables and the beta coefficient describes how the outcome changes in relationship to changes in the independent variables so if the independent variable changed by one and the beta coefficient is on that variable is beta for example then the outcome would change by beta"
  reference_answer: time=None text=None
  interviewer_feedback: time=01:52 text='is um that makes sense'
  question_topic: Statistics

ITEM #3
  interviewer_question: time=01:56 text='actually derive the coefficient of the uh of a linear model in this case'
  candidate_answer: time=02:02 text="um yeah there's a sort of a well-known solution um analytically which is that i can write it actually here which is that the beta beta vector is um x prime y um times x prime the inverse of x prime x and here the um the x is uh the here x represents the matrix the independent variables and y represents the vector of outcomes"
  reference_answer: time=None text=None
  interviewer_feedback: time=02:50 text='yeah okay that makes uh that makes perfect sense yeah so prime in this case would be your uh your transpose yeah exactly got it'
  question_topic: Statistics

ITEM #4
  interviewer_question: time=02:59 text="how would you um how would you estimate it without using so i believe what you're using the least squares approach but is there any other ways a different way of estimating the beta coefficient"
  candidate_answer: time=03:13 text='um yeah so we could use a maximum likelihood estimation for it um for example um and do like a optimization exercise on that to maximize the the likelihood function okay got it'
  reference_answer: time=None text=None
  interviewer_feedback: time=03:29 text="all right that makes it make sense all right so let's talk about the next question um now suppose that"
  question_topic: Statistics

ITEM #5
  interviewer_question: time=03:30 text="make sense all right so let's talk about the next question um now suppose that your target variable is inflated with zero um how would you actually going about approaching that problem um"
  candidate_answer: time=03:46 text="so if my data is um zero uh if my target variable is zero inflated i think the first question that i would ask is is there some type of censoring that is happening with um the target variable to cause these zeros or are these zeros like actually um the values of uh that we're interested in got it that's a really good"
  reference_answer: time=None text=None
  interviewer_feedback: time=04:14 text="got it that's a really good point"
  question_topic: Statistics

ITEM #6
  interviewer_question: time=04:16 text="in this case um it is an actual value um and let's see that the presence of zero so this is actually a non-negative um continuous distribution and um the presence of zero uh is uh has is it's about eighty percent of your um of your observations um in this case how would you how would your model uh model this type of data"
  candidate_answer: time=04:42 text="yeah that's a great question um i believe that there are statistical methods that help you deal with variables that are that follow distributions like this so the probit model or the tobit model for example can handle target variables that are particular like this one if we so that's that's sort of one statistical modeling approach that we can take alternatively i think just for like sanity checks and um understanding the data more we can also just model the target variable as being zero versus not running maybe a regression to see um how the beta coefficients look like and then proceeding with like the original modeling with the original variables okay got it all right that makes sense"
  reference_answer: time=None text=None
  interviewer_feedback: time=05:38 text="okay got it all right that makes sense um now let's move on to the next question"
  question_topic: Statistics

ITEM #7
  interviewer_question: time=05:44 text='um can you just can you um explain what a confidence interval is of a logistic regression model'
  candidate_answer: time=05:53 text="uh yeah so and the confidence interval meaning um the confidence intervals on the beta coefficients i'm assuming yeah yeah yeah so the confidence intervals um represents uh so let's say we have like a 95 percent confidence interval um and the statistical interpretation of that is that um they're like 95 of the time the actual beta coefficient will fall into the confidence interval that we estimated um and and that represents sort of um our our uncertainty around this this variable okay got it"
  reference_answer: time=None text=None
  interviewer_feedback: time=06:39 text='okay got it well now what if'
  question_topic: Statistics

ITEM #8
  interviewer_question: time=06:39 text="well now what if um so the the uh the beta coefficients of the logistic regression could either be in logos or alts ratio right um now let's presume that there's a presence of zero um in either one of those cases what does that mean presence of zero in the confidence interval then what would that mean in terms of the statistical significance of of its"
  candidate_answer: time=07:17 text="um you you're asking what does it mean if your confidence interval includes zero yes yes in either cases where it's either already in log odds or odds ratio uh beta coefficient because the logistic regression model can be in both forms yeah exactly um so i think my interpretation with that would be that the beta coefficients are not statistically distinguishable distinguishable from zero um and yeah uh if you were to do hypothesis testing on that coefficient then you would not reject the null hypothesis okay so if it's uh so if the coefficient"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Statistics

ITEM #9
  interviewer_question: time=08:03 text="is already it's in the log odds form um uh would it be possible to have a value of zero"
  candidate_answer: time=08:15 text="oh i see um right so yeah in that case i don't think that's possible right because it would be yeah sorry if the predictor doesn't is uncorrelated with the um outcome variable then the logos ratio should actually be one instead of zero um and it's not actually possible to have a zero value for that"
  reference_answer: time=None text=None
  interviewer_feedback: time=08:50 text="okay now what if it wasn't uh what if it was involved ratio"
  question_topic: Statistics

ITEM #10
  interviewer_question: time=08:50 text="okay now what if it wasn't uh what if it was involved ratio if the if the confidence interval has has um one what does that mean in terms of its uh statistical significance so let's just say that the odds ratio confidence interval falls somewhere between um point two four and point one uh one point two four what does it mean in terms of its statistical significance um"
  candidate_answer: time=09:25 text="then in in which case because it includes one it's uh if you were to do a hypothesis testing exercise you would not find that it's statistically significant"
  reference_answer: time=None text=None
  interviewer_feedback: time=09:37 text="okay got it all right thank you um okay so we're going to move on to the uh x sql question um"
  question_topic: Statistics

ITEM #11
  interviewer_question: time=09:45 text="so i'm going to go ahead and paste the table so this is a a basically a snippet of uh of the message um table set um and it contains your user id username the date and the message the number of message sent and the message the number of message received a given user on a day-to-day basis now go ahead and try to address the first question which is for each day return the name of the user or in this case you can return the user id who receive the highest message sent to message received ratio and this message ratio is your message sent divided by message received"
  candidate_answer: time=10:37 text="got it um yes i think the first question that i would or the first thing that i would check for in this data database would be whether there are missing values in either um in you know any of these columns and in the following analysis i'm just going to pre i'm just going to assume that there aren't any missing values and the second thing that i would think is important is whether message received could be zero because then you have a division by zero issue that may need to be addressed okay so i'm not select so so um so here i'm creating uh you know i'm selecting the user name variable and i'm also creating a new variable called uh sent to sent to received ratio which computes the ratio between message sent and message received and here i'm marking the message received variable as null if it's equal to zero so that the division will also result in a null okay um oh and i guess the question that i then want to ask is how we want to um treat these users do we um do we see them as having the highest ratio yeah like basically like okay for october 1st 2020 user xyz had the highest ratio i say so you actually want to set it to like a really high number um so that it would come on top when you sort um when you sort it precisely off of a given day so you want to you want to do some kind of screening on a given day got it okay in that case i think marking it as a null may not be the best idea um"
  reference_answer: time=None text=None
  interviewer_feedback: time=14:14 text="in that case i think marking it as a null may not be the best idea um let's actually kind of simplify this for a bit so let's just presume that um there is no zero in the denominator and it's already it's always populated so how would you go ahead and proceed with that problem then okay yeah that sounds good um in that case um i'll just do a simple division to calculate the ratio um and we want to group by date um so that we return one user for each date and the other question is do we are we interested in returning um multiple users for each day if they have the same highest ratio for each day good question so in this case um let's let's presume that um it's just you just return one user in that case okay so any user in that alien user yeah okay yeah it sounds good um um i think in this case i want to do like a a window function so um i'll create another new variable which is let's call it rank and since you said that it's okay to just return one user i'll calculate row numbers over partition by date order by the ratio um oh actually i don't need to group by date um i just have to select all right because equal to one which is the highest um center received ratio but user what's the highest ratio um okay so final solution or do you want to make any kind of revision um yeah i think that's the final solution okay got it um so i'm going to give you another question so in this case um now let's just say that uh for each user return the first date when the user received zero message mm-hmm return the first date when the user received zero message and uh if the user never received zero message um do we then in that case like those users wouldn't wouldn't matter so basically for user we just want to see uh what so among the users who receive zero messages when when was it that they received that zero message for the first time got it yeah that makes sense um so i would select uh let's say we return username um messages which is database and we are only interested in cases where message received is equal to zero um and we also return the first day which is min date as um wait for each user um oh actually um sorry my bad we we only return one observation for each user so i'm gonna group my username assuming that both user id and username are unique okay yeah okay so what you're basically doing is you're aggregating at the user level uh after you apply the filter where you're only looking at the entries that have zero in the method you see um and then for each of the user you wanna you're extracting the minimum date yeah exactly okay got it um all right so that's uh that's pretty much it for the sql um let's move on to the next uh section which is on the analytic case study so this is so the so this this uh question is based on instagram and what instagram is trying to do is identify users who are influencers so how would you help instagram define um whom the who who which users are influencers or not yeah to kind of getting to to get started on this question i think the first um clarifying question maybe that i would ask is how we define a user as an influencer um and i think there might be several ways to defining them um definition we could determine that a user is an influencer if they have you know a huge amount of influence on instagram so maybe if their number of followers exceeds a threshold then we define them as an influencer or if they're if or if they have specific posts that are particularly popular so maybe not many people follow them but some of their posts went viral and so maybe the number of overall views of your posts could also be used as a criteria for determining whether an user is an influencer the other thing um that you know moving away from these definitions a little bit is whether a user is being paid for certain content that they post on instagram so um whether they do any paid ads um and maybe if they do we can define them as an influencer uh should i proceed with any particular one of these definitions or uh well i think so i think those are good so number of uh number of followers that they have number of uh overall views that they have on posts and then if they have any paid ads um those are the criteria criteria that you would use to um to identify the user as an influencer or not right yeah okay um now now uh so the so those are the measures now how would you actually bend the users into influencer or not bucket um yeah i guess in order to do that i would love to understand a little bit more about like what this definition is used for um so is is the team instagram interested in maybe getting more users into the influencer bucket to promote their business or um are we trying to cluster users into influencer versus not in order to do some kind of targeted experiment or targeted feature design or something like that in this in this in this um uh case uh we want so instagram um you know wants to promote um wants to match advertisers with influencers so uh we need to identify with the you know who the users are are they influencers or are they you know just regular consumers um this is where you need to help the team um define that yeah that's very helpful context um and so i guess in that case uh i can refine my previous criteria a little bit more so we are not primarily interested in who is being paid for ads um but instead like who has the potential to um serve as an influencer on instagram and generate ads revenue for advertisers um yeah and um sorry what was the sorry what was your previous question so so uh so like how would you actually define that criteria saying okay these are the users who are influencers yeah it's kind of like if you were building like a fraud model saying okay this is a buster or not mm-hmm yeah representative um so similarly how would you should do that for the users bucket them into influencer or not and have the model so i think there are two ways of approaching this problem and i would classify them into um you know the unsupervised approach uh versus supervised approach um in the unsupervised approach um we are interested in finding clusters within the user um within the list of users of instagram and trying to find the clusters that are that has a huge amount of influence in the supervised approach we would essentially try to obtain some type of labels on whether a user is currently an influencer um and try to classify the remaining users into having the potential to to become an influencer versus not okay yeah so and and i think the key distinction between these two approaches is that um in the supervised approach we have to come up with some ways of creating the label in the first place okay um so how would you go on about creating a label yeah so if we were proceeding with this um approach one way is to try to collect information on whether they have any paid ads in their um current in instagram posts okay and um i am not a hundred percent sure if this is true but i remember seeing some of the um influencer having these posts that are kind of labeled as advertisement and if instagram collects that sort of data then um that could serve as a useful label for this problem okay um all right now i'm gonna i have i have a follow-up um so now let's suppose that you do have this uh instagram influencer bucket now how would you go ahead and um and segment the influencer population so i'm going to paste the question here yeah and i imagine that the reason that we want to segment these influencers maybe to group them into different um categories so that advertisers with different needs can be matched to different groups of influencer is that right got it yeah and so i think you know what type of influence they have would be um really the prime the primary um variable of interest to us because we are interested in knowing what type of population they attract so if they are like a fashion blogger um let me write some potential categories um maybe they are like a fashion blogger or they are i am uh they post mainly political content um etc and so they their posts the content of their posts may say uh may wrap may generate a good signal for um what type of crowd they attract um so and so treating this as one of the features is um content uh content of posts and maybe we can do some computer vision type analysis or uh natural language processing analysis on the content of these posts to extract keywords and group them into categories um the other feature that i have in mind is the type of um users that follow them so they're followers um and if their users um you know label themselves and then you weigh on the instagram profile then we can get a pretty good sense of how what type of population they're attracting and the potential advertisement revenue they can generate yeah so these are the two main types of features that i can think of i don't care at this moment you identify the signals um now now with using the signals how would you actually perform the segmentation itself yeah um so say that we um use maybe some machine type of machine learning models to analyze their posts and the text that they post um and we can get uh sort of embeddings of um and we can get like embeddings of their content then we can perform a unsupervised clustering algorithm to try to group these influencers into different groups so one of the simplest models that we can i can think of is the k-means clustering okay there are many modifications of this that serves different purposes but yeah this may be a good starting point okay um and one last question and then we're done with the session um is how would you evaluate your cluster then um that's um that's a good question so evaluation um i think you know one way that i can think of on top of my head is if we get some human raiders human labelers to look at these influencers and then group them into categories and we can compare the human evaluation with the results that are generated from the algorithms okay got it got it all right yeah so that wraps up the session um thank you for uh being a participant as an interviewee for this mock interview um and i hope you have a good day yeah thank you so much for this question appreciate it yeah thank you"
  question_topic: SQL

--- CHAPTER `09:50` — SQL Questions ---
window: 09:50 .. 20:00
recognition_status: multiple (2 items)

ITEM #12
  interviewer_question: time=14:22 text="let's actually kind of simplify this for a bit so let's just presume that um there is no zero in the denominator and it's already it's always populated so how would you go ahead and proceed with that problem then"
  candidate_answer: time=14:34 text="okay yeah that sounds good um in that case um i'll just do a simple division to calculate the ratio um and we want to group by date um so that we return one user for each date and the other question is do we are we interested in returning um multiple users for each day if they have the same highest ratio for each day good question so in this case um let's let's presume that um it's just you just return one user in that case okay so any user in that alien user yeah okay yeah it sounds good um um i think in this case i want to do like a a window function so um i'll create another new variable which is let's call it rank and since you said that it's okay to just return one user i'll calculate row numbers over partition by date order by the ratio um oh actually i don't need to group by date um i just have to select all right because equal to one which is the highest um center received ratio but user what's the highest ratio um okay so final solution or do you want to make any kind of revision um yeah i think that's the final solution"
  reference_answer: time=None text=None
  interviewer_feedback: time=17:27 text="so final solution or do you want to make any kind of revision um yeah i think that's the final solution okay"
  question_topic: SQL

ITEM #13
  interviewer_question: time=17:42 text="another question so in this case um now let's just say that uh for each user return the first date when the user received zero message mm-hmm return the first date when the user received zero message and uh if the user never received zero message um do we then in that case like those users wouldn't wouldn't matter so basically for user we just want to see uh what so among the users who receive zero messages when when was it that they received that zero message for the first time got it"
  candidate_answer: time=18:32 text="yeah that makes sense um so i would select uh let's say we return username um messages which is database and we are only interested in cases where message received is equal to zero um and we also return the first day which is min date as um wait for each user um oh actually um sorry my bad we we only return one observation for each user so i'm gonna group my username assuming that both user id and username are unique okay yeah"
  reference_answer: time=None text=None
  interviewer_feedback: time=19:36 text="okay so what you're basically doing is you're aggregating at the user level uh after you apply the filter where you're only looking at the entries that have zero in the method you see um and then for each of the user you wanna you're extracting the minimum date yeah exactly okay got it"
  question_topic: SQL

--- CHAPTER `20:00` — Case Questions ---
window: 20:00 .. конец
recognition_status: multiple (7 items)

ITEM #14
  interviewer_question: time=20:23 text='so how would you help instagram define um whom the who who which users are influencers or not'
  candidate_answer: time=20:33 text="yeah to kind of getting to to get started on this question i think the first um clarifying question maybe that i would ask is how we define a user as an influencer um and i think there might be several ways to defining them um definition we could determine that a user is an influencer if they have you know a huge amount of influence on instagram so maybe if their number of followers exceeds a threshold then we define them as an influencer or if they're if or if they have specific posts that are particularly popular so maybe not many people follow them but some of their posts went viral and so maybe the number of overall views of your posts could also be used as a criteria for determining whether an user is an influencer the other thing um that you know moving away from these definitions a little bit is whether a user is being paid for certain content that they post on instagram so um whether they do any paid ads um and maybe if they do we can define them as an influencer uh should i proceed with any particular one of these definitions"
  reference_answer: time=None text=None
  interviewer_feedback: time=22:08 text='or uh well i think so i think those are good so number of uh number of followers that they have number of uh overall views that they have on posts and then if they have any paid ads um those are the criteria criteria that you would use to um to identify the user as an influencer or not right'
  question_topic: Product Metrics

ITEM #15
  interviewer_question: time=22:33 text='uh so the so those are the measures now how would you actually bend the users into influencer or not'
  candidate_answer: time=22:45 text="in order to do that i would love to understand a little bit more about like what this definition is used for um so is is the team instagram interested in maybe getting more users into the influencer bucket to promote their business or um are we trying to cluster users into influencer versus not in order to do some kind of targeted experiment or targeted feature design or something like that in this in this in this um uh yeah that's very helpful context um and so i guess in that case uh i can refine my previous criteria a little bit more so we are not primarily interested in who is being paid for ads um but instead like who has the potential to um serve as an influencer on instagram and generate ads revenue for advertisers um yeah and um sorry what was the sorry what was your previous question"
  reference_answer: time=None text=None
  interviewer_feedback: time=23:22 text='case uh we want so instagram um you know wants to promote um wants to match advertisers with influencers so uh we need to identify with the you know who the users are are they influencers or are they you know just regular consumers um this is where you need to help the team um define that'
  question_topic: Product Metrics

ITEM #16
  interviewer_question: time=24:23 text="so so uh so like how would you actually define that criteria saying okay these are the users who are influencers yeah it's kind of like if you were building like a fraud model saying okay this is a buster or not mm-hmm yeah representative um so similarly how would you should do that for the users bucket them into influencer or not"
  candidate_answer: time=24:50 text='and have the model so i think there are two ways of approaching this problem and i would classify them into um you know the unsupervised approach uh versus supervised approach um in the unsupervised approach um we are interested in finding clusters within the user um within the list of users of instagram and trying to find the clusters that are that has a huge amount of influence in the supervised approach we would essentially try to obtain some type of labels on whether a user is currently an influencer um and try to classify the remaining users into having the potential to to become an influencer versus not okay'
  reference_answer: time=None text=None
  interviewer_feedback: time=25:52 text='yeah so and and i think the key distinction between these two approaches is that um in the supervised approach we have to come up with some ways of creating the label in the first place okay um so how would you go on about'
  question_topic: ML

ITEM #17
  interviewer_question: time=26:05 text='okay um so how would you go on about creating a label'
  candidate_answer: time=26:10 text='yeah so if we were proceeding with this um approach one way is to try to collect information on whether they have any paid ads in their um current in instagram posts okay and um i am not a hundred percent sure if this is true but i remember seeing some of the um influencer having these posts that are kind of labeled as advertisement and if instagram collects that sort of data then um that could serve as a useful label for this problem okay um'
  reference_answer: time=None text=None
  interviewer_feedback: time=26:52 text="all right now i'm gonna i have i have a follow-up um so now let's"
  question_topic: ML

ITEM #18
  interviewer_question: time=26:58 text="suppose that you do have this uh instagram influencer bucket now how would you go ahead and um and segment the influencer population so i'm going to paste the question here yeah and i imagine that"
  candidate_answer: time=27:38 text="got it yeah and so i think you know what type of influence they have would be um really the prime the primary um variable of interest to us because we are interested in knowing what type of population they attract so if they are like a fashion blogger um let me write some potential categories um maybe they are like a fashion blogger or they are i am uh they post mainly political content um etc and so they their posts the content of their posts may say uh may wrap may generate a good signal for um what type of crowd they attract um so and so treating this as one of the features is um content uh content of posts and maybe we can do some computer vision type analysis or uh natural language processing analysis on the content of these posts to extract keywords and group them into categories um the other feature that i have in mind is the type of um users that follow them so they're followers um and if their users um you know label themselves and then you weigh on the instagram profile then we can get a pretty good sense of how what type of population they're attracting and the potential advertisement revenue they can generate yeah so these are the two main types of features that i can think of i don't care at this moment you identify the"
  reference_answer: time=None text=None
  interviewer_feedback: time=27:38 text='got it yeah and so'
  question_topic: ML

ITEM #19
  interviewer_question: time=29:37 text='signals um now now with using the signals how would you actually perform the segmentation itself'
  candidate_answer: time=29:45 text='yeah um so say that we um use maybe some machine type of machine learning models to analyze their posts and the text that they post um and we can get uh sort of embeddings of um and we can get like embeddings of their content then we can perform a unsupervised clustering algorithm to try to group these influencers into different groups so one of the simplest models that we can i can think of is the k-means clustering okay there are many modifications of this that serves different purposes but yeah this may be a good'
  reference_answer: time=None text=None
  interviewer_feedback: time=30:35 text="starting point okay um and one last question and then we're done with the session"
  question_topic: ML

ITEM #20
  interviewer_question: time=30:40 text='um is how would you evaluate your cluster then'
  candidate_answer: time=30:46 text="um that's um that's a good question so evaluation um i think you know one way that i can think of on top of my head is if we get some human raiders human labelers to look at these influencers and then group them into categories and we can compare the human evaluation with the results that are generated from the algorithms okay got it"
  reference_answer: time=None text=None
  interviewer_feedback: time=31:19 text='got it all right yeah so that wraps up the session um thank you for uh being a participant as an interviewee for this mock interview um and i hope you have a good day'
  question_topic: ML

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/datainterview/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24/data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
