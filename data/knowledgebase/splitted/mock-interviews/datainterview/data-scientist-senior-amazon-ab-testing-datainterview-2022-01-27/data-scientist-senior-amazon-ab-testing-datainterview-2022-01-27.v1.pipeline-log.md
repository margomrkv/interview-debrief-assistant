<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27",
  "transcript_folder": "transcripts/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/",
  "source_id": "data_scientist_senior_amazon_ab_testing_datainterview_2022_01_27",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:05:20 +0200",
  "updated_at": "2026-05-20 21:12:30 +0200",
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
    "json": "splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27//timecodes.txt",
        "en",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 21:05:20 +0200"
    },
    {
      "id": 2,
      "name": "qa_extraction",
      "llm": true,
      "model": "claude-sonnet-4-6",
      "inputs": [
        "splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.pipeline-log.md#LLM_INPUT_STEP_2"
      ],
      "outputs": [
        "splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.json"
      ],
      "status": "completed",
      "duration_sec": 180.0,
      "notes": null,
      "finished_at": "2026-05-20 21:12:30 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:12:30 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27//video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:12:30 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/`
- **Source ID:** `data_scientist_senior_amazon_ab_testing_datainterview_2022_01_27`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:05:20 +0200
- **Last updated:** 2026-05-20 21:12:30 +0200

Фильтр в IDE: `*data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27//timecodes.txt`<br>`en`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.pipeline-log.md` | — | completed |
| 2 | qa_extraction | yes | claude-sonnet-4-6 | `splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.pipeline-log.md#LLM_INPUT_STEP_2` | `splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.json` | 180.0s | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27//video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.validation-report.md` | 1.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.pipeline-log.md`

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
SOURCE_ID: data_scientist_senior_amazon_ab_testing_datainterview_2022_01_27
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/
INTERVIEW_LANGUAGE: en
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00] hey sarah how's it going today good how
[00:02] are you i'm good thanks for
[00:04] participating as a mock interview
[00:06] candidate for this walking dead call
[00:08] based on amazon's
[00:10] data scientists interview and in this
[00:12] interview we're going to cover a b
[00:14] testing questions does that sound good
[00:16] with you oh yes
[00:18] okay all right so i'm going to start
[00:20] with some questions i'm going to ask and
[00:21] then
[00:22] um you know after you provide the
[00:24] responses
[00:26] um you know i'll probably take about
[00:28] five to ten minutes give you some
[00:30] assessment
[00:31] and then um uh you know and hopefully
[00:33] that the tips that i provide in this
[00:35] marketing recall is gonna be really
[00:36] helpful for your
[00:38] um upcoming interviews at fan companies
[00:41] okay sounds good thank you
[00:42] great all right so starting with the
[00:44] first question
[00:46] what i'd like to ask you whoops i just
[00:48] based in the wrong spot is how do you
[00:50] measure the effectiveness of a
[00:52] recommender system
[00:55] okay so before i dive into uh this
[00:59] question so
[01:01] uh
[01:02] i have a few clarified ques uh
[01:04] clarifying question that i want to ask
[01:06] uh the first question is uh so are you
[01:08] talking about the recommend recommended
[01:11] system uh in amazon web specifically
[01:15] yes
[01:16] okay sounds good and uh in terms of uh
[01:21] effectiveness uh
[01:24] can you uh tell me a little bit about
[01:27] what you mean by effectiveness
[01:30] you could perhaps think about it in
[01:32] terms of maybe the quality of the uh
[01:36] recommendation
[01:37] quality of the recommended system
[01:41] okay so maybe uh
[01:44] how accurate
[01:46] uh the recommended recommended system
[01:49] can
[01:50] predict uh the user's preference
[01:53] when they purchase products in amazon
[01:55] web
[01:57] do you think that's a fair assumption
[01:58] yep
[01:59] okay sounds good so essentially is a
[02:03] predictive
[02:08] the recommender
[02:12] system
[02:15] okay
[02:16] sounds good uh
[02:18] so a few
[02:20] things uh that i can think of is
[02:25] that like we just
[02:27] mentioned uh
[02:29] the percentage
[02:31] of uh
[02:34] products uh uh let's see
[02:39] number of uh product
[02:43] purchases
[02:45] out of a number of uh
[02:49] product
[02:51] recommended
[02:54] so right now i'm just coming up with a
[02:56] metrics that we can use to measure the
[02:59] effectiveness effectiveness of a
[03:01] recommender system
[03:03] and i think the number of products
[03:06] purchased out of all the product
[03:08] recommended
[03:10] will be an indicator to tell us how
[03:13] uh
[03:14] how
[03:15] uh
[03:16] how the recommended system can uh
[03:19] actively predict users preferences
[03:22] because the more product that they
[03:24] purchase uh the higher this percentage
[03:27] the more likely that uh the users are
[03:30] interested in the products that
[03:32] recommend the system is recommending
[03:38] and then
[03:39] the second metric that i can think of
[03:43] is
[03:45] the time
[03:47] the amount of time spent
[03:49] that
[03:51] users
[03:54] have spent on
[03:56] purchasing
[03:59] purchasing on the platform
[04:04] uh the reason so in this case uh i would
[04:08] say
[04:09] if the recommended system is doing its
[04:13] job it is likely that uh the user
[04:17] spend less time on uh picking the right
[04:20] product
[04:22] uh picking the products that they are
[04:24] interested
[04:25] because uh so when whenever users go to
[04:28] amazon right they have a product in mind
[04:30] that they want to purchase
[04:31] and if the recommended system is doing
[04:34] its job then it's likely that the time
[04:37] span in their purchase is low
[04:40] uh
[04:41] and the third one that i can think of is
[04:44] uh the
[04:46] uh
[04:47] average
[04:50] revenue
[04:51] uh
[04:53] average purchase
[04:56] uh revenue
[04:59] uh per user
[05:01] uh and i think if
[05:04] this is also a good indicator because
[05:07] revenue is the north star metrics that
[05:10] amazon wants to optimize
[05:12] and if the recommender system is uh
[05:14] effective it is most like
[05:17] likely that the average purchase revenue
[05:19] per user is high so these are the three
[05:21] metrics that i can i can come up with to
[05:24] measure the effectiveness of a
[05:25] recommended system okay got it all right
[05:28] so segue over to this is um suppose that
[05:31] a new recommended system is proposed how
[05:34] do you know if this new version should
[05:35] be used
[05:37] sounds good so
[05:40] in order to
[05:42] uh
[05:44] in order to understand whether we
[05:47] should launch this new version system
[05:50] the best way that we can do is do an ap
[05:53] test
[05:54] where the control group uh
[05:57] uh will
[05:59] will have uh the old other existing
[06:04] recommender system
[06:07] whereas the treatment group
[06:10] will have the new uh
[06:14] version of the
[06:18] recommender
[06:19] system
[06:21] uh and then the metrics
[06:24] that we can measure um
[06:27] is uh the number of uh
[06:30] like the number of product purchase
[06:33] out of the number of products
[06:35] recommended
[06:37] so
[06:38] let's say if the
[06:41] average
[06:44] number of product purchases
[06:47] the number of products recommended
[06:50] per user
[06:52] uh
[06:53] is uh increasing in the treatment group
[06:57] then we can conclude that the new
[07:00] version system can be used so do you
[07:03] have any questions uh
[07:06] based on uh the the control groups and
[07:10] treatment groups and the metrics that i
[07:12] have list so far if not then i can go on
[07:14] with the experimental framework that we
[07:17] can use
[07:19] when you're saying the number of product
[07:21] recommended um
[07:24] do you see any potential problem with
[07:25] that as a denominator
[07:28] the number of product recommended uh
[07:34] oh uh
[07:37] oh uh so yeah so
[07:40] the number of product recommended um
[07:43] based on
[07:44] the search
[07:47] words
[07:48] that
[07:49] the user has entered
[07:55] okay
[07:56] but what if a user has multiple search
[07:58] sessions
[08:00] right uh so yeah so i think what you're
[08:03] suggesting is that if they have multiple
[08:07] search
[08:08] sections uh
[08:10] what we can do is
[08:13] uh
[08:15] what we can do is
[08:18] oh good questions let me
[08:21] think about this
[08:25] oh if they have a multiple section then
[08:28] we will only account the first sections
[08:30] uh that
[08:32] uh they they enter because if we account
[08:35] multiple sections then it will violate
[08:38] uh the assumptions of a t-test
[08:42] where the uh the observation should be
[08:44] independent and identically distributed
[08:49] okay
[08:53] um sorry and your proposal for making
[08:55] independent is what again i'm sorry
[08:58] yeah so my recommendation is we only
[09:01] account for the first sections okay
[09:06] got it
[09:07] all right um okay so proceed
[09:11] okay so
[09:12] in terms of the experimental framework
[09:14] uh we can use uh so one thing that we
[09:18] need to consider is the
[09:20] alpha so in this case i set the alpha
[09:24] equals to 0.05 essentially what alpha is
[09:28] is uh the
[09:30] the type 1 error rate uh it is the risk
[09:32] that the company is willing to
[09:35] to take in order to detect an effect in
[09:38] this experiment so i'm using 0.05 in
[09:42] this case because uh
[09:45] i felt like
[09:48] it is a good alpha that we can use to uh
[09:51] to do the experiment it but if the
[09:54] if amazon believes that uh the risk is
[09:57] too high they are they can load the
[09:59] alpha to 0.01
[10:02] and the
[10:04] power that we can set in this case is
[10:07] uh 0.8 so it is the probability of
[10:11] protecting an effect if there's truly an
[10:14] effect exist
[10:17] and the minimum detectable effect that
[10:19] we
[10:20] can use in this case is one percent
[10:24] so um
[10:26] so
[10:27] because uh amazon has
[10:29] such huge uh user base
[10:32] with uh
[10:34] uh with a one percent increase will be
[10:37] uh significant uh for us to launch this
[10:41] uh
[10:42] new version of uh recommended system
[10:46] okay
[10:48] what else
[10:49] okay so with the alpha power and minimum
[10:52] detectable effect we can estimate uh the
[10:57] sample size
[10:58] that we can use uh for this experiment
[11:02] so uh
[11:04] and with the sample size in mind then we
[11:07] can
[11:08] set up our test
[11:09] which in this case i will use a t-test
[11:14] and
[11:14] um
[11:17] with uh so with the t-test then we will
[11:20] need to estimate the experimentation
[11:22] time
[11:24] which
[11:25] i
[11:26] proposed to one to two weeks
[11:31] and so let's say we launched this test
[11:34] and then the result that we get is uh
[11:37] p-value the
[11:39] p-value is less than or equal to alpha
[11:43] then we will reject the null hypothesis
[11:46] uh
[11:48] reject the null
[11:51] hypothesis
[11:52] and conclude that the new version of
[11:55] recommended system uh has significantly
[11:59] increased the average number of product
[12:01] purchase out of the number of products
[12:04] recommended
[12:06] per user
[12:11] all right um
[12:13] so i have some like two follow-up
[12:14] questions for you so the first follow-up
[12:16] question i have for you is
[12:18] um
[12:19] how do you know
[12:21] what your
[12:22] uh statistical power should be so
[12:25] um so you set it at eighty percent
[12:28] um but are there any instances where you
[12:30] might want to increase the power
[12:32] yeah so let's say uh we
[12:35] run this test with 80 power
[12:38] and then the test result is
[12:40] insignificant which is p value is
[12:43] greater than alpha but uh our pm insists
[12:46] that oh there uh there should be an
[12:50] effect uh with this new version of
[12:52] recommended system then what we can do
[12:55] is to increase the power to maybe 90
[12:58] percent
[12:59] uh which
[13:01] like if we increase the power it will
[13:03] require more sample size and longer
[13:06] experimentation time but
[13:08] increasing the power will give us a high
[13:10] probability of detecting an effect if
[13:13] the effects truly exist
[13:16] and what is that effect you're talking
[13:18] about oh the effects that i'm talking
[13:22] about
[13:23] is uh
[13:25] the difference between uh the metrics
[13:28] so essentially it is the effect size
[13:31] what if what if the effect is negative
[13:35] uh if so let's say if we
[13:38] run this experimentation and the effect
[13:40] is negative uh something that we can do
[13:43] is first we need to check whether our
[13:46] experimentation setup is correct
[13:49] and then secondly we can check
[13:52] some internal and external factors for
[13:54] example in terms of internal factors we
[13:57] can check whether there are bugs in the
[13:59] newer new versions of the recommended
[14:01] system
[14:02] and
[14:03] for the external factors we want to make
[14:06] sure that
[14:08] our competitors is not launching some
[14:11] events that can influence the results in
[14:14] this experiment
[14:16] this experiment results
[14:18] or there is no holiday effect that might
[14:22] potentially
[14:23] uh
[14:24] affect
[14:25] uh the result as well
[14:29] okay got it
[14:31] um
[14:32] and another question i have for you is
[14:35] um
[14:37] what do you think would happen if you
[14:38] were to run the experiment less than one
[14:40] week
[14:42] so if it is if we
[14:46] run it less than one week it is very
[14:49] likely that
[14:50] uh we might get a significant result but
[14:54] this is not true because at the
[14:56] beginning when we have a low sample size
[14:59] it is very likely that our metric is
[15:02] fluctuating
[15:04] uh
[15:05] in between the significant area and the
[15:08] insignificant area so it is very
[15:10] important to uh make sure that we
[15:15] uh launch
[15:16] the experiment for
[15:18] uh
[15:19] for a certain number of days given
[15:23] uh our sample size that is calculated
[15:26] that is calculated using alpha power and
[15:28] minimum detectable effect
[15:35] okay just taking notes here
[15:39] okay okay all right so that is the um
[15:42] end of the question portion now let's
[15:45] actually dive into the feedback but
[15:47] before i start um i just want to mention
[15:49] that in terms of the um the feedback
[15:52] portion of this this is actually going
[15:53] to be available as part of the mock
[15:55] interview video recording
[15:57] in the um in the monthly subscription
[15:59] course so for those who are preparing
[16:02] for a b testing interviews in general i
[16:04] would definitely recommend that you
[16:05] check out thedatantv.com
[16:08] check out the courses and the coaching
[16:09] services that will give you some of the
[16:11] access to these mock interview videos

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
Write JSON only to: splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.json \
    --video transcripts/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27//video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.json --out splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.qa-split.json \
    --video transcripts/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27//video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.validation-report.md

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
video.md: transcripts/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/video.md

--- CHAPTER `00:50` — Recommender System Metrics ---
window: 00:50 .. 05:38
recognition_status: single (1 items)

ITEM #2
  interviewer_question: time=05:28 text='so segue over to this is um suppose that a new recommended system is proposed how do you know if this new version should be used'
  candidate_answer: time=05:37 text="sounds good so in order to uh in order to understand whether we should launch this new version system the best way that we can do is do an ap test where the control group uh uh will will have uh the old other existing recommender system whereas the treatment group will have the new uh version of the recommender system uh and then the metrics that we can measure um is uh the number of uh like the number of product purchase out of the number of products recommended so let's say if the average number of product purchases the number of products recommended per user uh is uh increasing in the treatment group then we can conclude that the new version system can be used so do you have any questions uh based on uh the the control groups and treatment groups and the metrics that i have list so far if not then i can go on with the experimental framework that we can use"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Experimentation

--- CHAPTER `05:38` — AB Testing Recommender System ---
window: 05:38 .. конец
recognition_status: multiple (9 items)

ITEM #3
  interviewer_question: time=07:19 text="when you're saying the number of product recommended um do you see any potential problem with that as a denominator"
  candidate_answer: time=07:28 text='the number of product recommended uh oh uh oh uh so yeah so the number of product recommended um based on the search words that the user has entered'
  reference_answer: time=None text=None
  interviewer_feedback: time=07:55 text='okay'
  question_topic: Experimentation

ITEM #4
  interviewer_question: time=07:56 text='but what if a user has multiple search sessions'
  candidate_answer: time=08:00 text="right uh so yeah so i think what you're suggesting is that if they have multiple search sections uh what we can do is uh what we can do is oh good questions let me think about this oh if they have a multiple section then we will only account the first sections uh that uh they they enter because if we account multiple sections then it will violate uh the assumptions of a t-test where the uh the observation should be independent and identically distributed"
  reference_answer: time=None text=None
  interviewer_feedback: time=08:49 text='okay'
  question_topic: Experimentation

ITEM #5
  interviewer_question: time=08:53 text="um sorry and your proposal for making independent is what again i'm sorry"
  candidate_answer: time=08:58 text='yeah so my recommendation is we only account for the first sections okay'
  reference_answer: time=None text=None
  interviewer_feedback: time=09:06 text='got it'
  question_topic: Experimentation

ITEM #6
  interviewer_question: time=09:07 text='all right um okay so proceed'
  candidate_answer: time=09:11 text="okay so in terms of the experimental framework uh we can use uh so one thing that we need to consider is the alpha so in this case i set the alpha equals to 0.05 essentially what alpha is is uh the the type 1 error rate uh it is the risk that the company is willing to to take in order to detect an effect in this experiment so i'm using 0.05 in this case because uh i felt like it is a good alpha that we can use to uh to do the experiment it but if the if amazon believes that uh the risk is too high they are they can load the alpha to 0.01 and the power that we can set in this case is uh 0.8 so it is the probability of protecting an effect if there's truly an effect exist and the minimum detectable effect that we can use in this case is one percent so um so because uh amazon has such huge uh user base with uh with a one percent increase will be uh significant uh for us to launch this uh new version of uh recommended system"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Experimentation

ITEM #7
  interviewer_question: time=10:48 text='what else'
  candidate_answer: time=10:49 text="okay so with the alpha power and minimum detectable effect we can estimate uh the sample size that we can use uh for this experiment so uh and with the sample size in mind then we can set up our test which in this case i will use a t-test and um with uh so with the t-test then we will need to estimate the experimentation time which i proposed to one to two weeks and so let's say we launched this test and then the result that we get is uh p-value the p-value is less than or equal to alpha then we will reject the null hypothesis uh reject the null hypothesis and conclude that the new version of recommended system uh has significantly increased the average number of product purchase out of the number of products recommended per user"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Experimentation

ITEM #8
  interviewer_question: time=12:13 text='so i have some like two follow-up questions for you so the first follow-up question i have for you is um how do you know what your uh statistical power should be so um so you set it at eighty percent um but are there any instances where you might want to increase the power'
  candidate_answer: time=12:32 text="yeah so let's say uh we run this test with 80 power and then the test result is insignificant which is p value is greater than alpha but uh our pm insists that oh there uh there should be an effect uh with this new version of recommended system then what we can do is to increase the power to maybe 90 percent uh which like if we increase the power it will require more sample size and longer experimentation time but increasing the power will give us a high probability of detecting an effect if the effects truly exist"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Experimentation

ITEM #9
  interviewer_question: time=13:16 text="and what is that effect you're talking about"
  candidate_answer: time=13:18 text="oh the effects that i'm talking about is uh the difference between uh the metrics so essentially it is the effect size"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Experimentation

ITEM #10
  interviewer_question: time=13:31 text='what if what if the effect is negative'
  candidate_answer: time=13:35 text="uh if so let's say if we run this experimentation and the effect is negative uh something that we can do is first we need to check whether our experimentation setup is correct and then secondly we can check some internal and external factors for example in terms of internal factors we can check whether there are bugs in the newer new versions of the recommended system and for the external factors we want to make sure that our competitors is not launching some events that can influence the results in this experiment this experiment results or there is no holiday effect that might potentially uh affect uh the result as well"
  reference_answer: time=None text=None
  interviewer_feedback: time=14:29 text='okay got it'
  question_topic: Experimentation

ITEM #11
  interviewer_question: time=14:32 text='and another question i have for you is um what do you think would happen if you were to run the experiment less than one week'
  candidate_answer: time=14:42 text='so if it is if we run it less than one week it is very likely that uh we might get a significant result but this is not true because at the beginning when we have a low sample size it is very likely that our metric is fluctuating uh in between the significant area and the insignificant area so it is very important to uh make sure that we uh launch the experiment for uh for a certain number of days given uh our sample size that is calculated that is calculated using alpha power and minimum detectable effect'
  reference_answer: time=None text=None
  interviewer_feedback: time=15:35 text='okay just taking notes here'
  question_topic: Experimentation

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/datainterview/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27/data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
