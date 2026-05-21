<!-- PIPELINE_MANIFEST
{
  "version": 2,
  "basename": "ml-engineer-junior-karpov-2023-03-09",
  "transcript_folder": "transcripts/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09",
  "source_id": "ml_engineer_junior_karpov_2023_03_09",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 18:13:12 +0200",
  "updated_at": "2026-05-20 18:16:35 +0200",
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
    "json": "splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/timecodes.txt",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 18:13:12 +0200"
    },
    {
      "id": 2,
      "name": "qa_extraction",
      "llm": true,
      "model": "claude-sonnet-4-6",
      "inputs": [
        "splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.pipeline-log.md#LLM_INPUT_STEP_2"
      ],
      "outputs": [
        "splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.json"
      ],
      "status": "completed",
      "duration_sec": 180.0,
      "notes": null,
      "finished_at": "2026-05-20 18:15:47 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 2.0,
      "notes": null,
      "finished_at": "2026-05-20 18:15:50 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 18:15:50 +0200"
    },
    {
      "id": 5,
      "name": "llm_validation",
      "llm": true,
      "model": "claude-sonnet-4-6",
      "inputs": [
        "splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.pipeline-log.md#LLM_INPUT_STEP_5"
      ],
      "outputs": [
        "splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 90.0,
      "notes": null,
      "finished_at": "2026-05-20 18:16:35 +0200"
    }
  ]
}
-->

# Pipeline log v2

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09`
- **Source ID:** `ml_engineer_junior_karpov_2023_03_09`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 18:13:12 +0200
- **Last updated:** 2026-05-20 18:16:35 +0200

Фильтр в IDE: `*ml-engineer-junior-karpov-2023-03-09.v2*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/timecodes.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.pipeline-log.md` | — | completed |
| 2 | qa_extraction | yes | claude-sonnet-4-6 | `splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.pipeline-log.md#LLM_INPUT_STEP_2` | `splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.json` | 180.0s | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.xlsx` | 2.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.validation-report.md` | 1.0s | completed |
| 5 | llm_validation | yes | claude-sonnet-4-6 | `splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.pipeline-log.md#LLM_INPUT_STEP_5` | `splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.validation-report.md` | 90.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.pipeline-log.md`

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
SOURCE_ID: ml_engineer_junior_karpov_2023_03_09
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00:03] Всем привет моё имя Богдан я автор
[00:00:07] симулятор инженера машинного обучения
[00:00:09] место где вы можете получить опыт работы
[00:00:13] менеджера до того как устроитесь Мэри
[00:00:16] инженером либо же получить
[00:00:17] дополнительный опыт Если вы уже
[00:00:19] работаете либо мене инженером либо на
[00:00:22] другой специальности И хотите укоренять
[00:00:26] свои навыки и сегодня мы проводим мог
[00:00:30] интервью открыто собеседование с Вадимом
[00:00:33] одним из
[00:00:36] инженеров которые участвуют в симуляторе
[00:00:41] Привет Привет расскажи вообще вкратце
[00:00:44] симулятор и про свой опыт
[00:00:49] Мне кажется в симулятор попадает многие
[00:00:51] после окончания курсов
[00:00:55] я не был исключением То есть я пошел
[00:00:58] учиться на startml и я понял что не
[00:01:03] хватает каких-то практических знаний и
[00:01:05] вот то что запустили симулятором или это
[00:01:09] было прям супер вовремя и я не
[00:01:12] раздумываюсь пошел туда и даже больше
[00:01:14] скажу что я после окончания курса Я
[00:01:19] понял что совмещать параллельно
[00:01:22] работу и учебу качественно учиться
[00:01:25] невозможно поэтому я принял решение
[00:01:27] уволиться и пойти целиком
[00:01:30] симулятор для того чтобы лучше впитать
[00:01:35] все знания
[00:01:37] прошлому опыту он никак не связан сойти
[00:01:40] Я последнее время Работал главным
[00:01:42] специалистом авторского надзора Если ты
[00:01:46] знаешь что такое авторский надзор Если
[00:01:47] нет могу сказать
[00:01:50] это когда Проектный институт то есть
[00:01:54] какая-то проектная организация выпускает
[00:01:56] свои чертежи проекты
[00:01:59] и они непосредственно воплощаются в
[00:02:02] жизнь то
[00:02:03] выделяется там человек или группа
[00:02:05] специалистов которые непосредственно
[00:02:06] находится на стройке и решает либо на
[00:02:10] месте вопросы либо как-то пытаются их
[00:02:12] дистанционно решить
[00:02:14] задействовав ресурс со стороны из
[00:02:18] организации и вот я как раз таки работал
[00:02:20] главный специалистом а наш Проектный
[00:02:23] институт проектировал метрополитен Я в
[00:02:26] Москве строил можно сказать
[00:02:29] метро построить метро Мне кажется задача
[00:02:32] тоже сложно за дизайнеть как это все
[00:02:34] будет выглядеть Да
[00:02:36] это было Это было непросто но это было
[00:02:40] интересно и очень сильно прокачал свои
[00:02:42] софты очень сильно прокачался в поиске и
[00:02:45] навыки решения опроса собеседника потому
[00:02:48] что не каждый человек может грамотно
[00:02:51] изложить сразу свои мысли и суть
[00:02:52] проблемы такое было хороший тренажер я у
[00:02:56] тебя в резюме видел пролив моделирование
[00:02:59] через трансформацию классов да было
[00:03:03] такое Это было как тестовое задание
[00:03:06] на кегли там мы сколько там месяцев
[00:03:09] соревновались Вот и на самом деле я
[00:03:14] скажем так не вошел в топ но для меня
[00:03:16] это был хороший урок потому что я с
[00:03:20] агрегировал скажем так все знания
[00:03:22] которые были получены во время курса
[00:03:24] Старт тоннель в таком в практическом
[00:03:27] русле уже и у меня так они устаканились
[00:03:29] и было понятно уже как что нужно
[00:03:33] какие-то нужно делать для того чтобы
[00:03:35] модельку построить
[00:03:38] обучаешь сразу знания
[00:03:44] а расскажи вообще что за такая задача
[00:03:47] отлив моделирования и что за классы там
[00:03:51] трансформируются
[00:03:53] задача полив моделирования состоит в том
[00:03:56] чтобы предсказать кому из клиентов Да
[00:04:00] допустим направить как на кого из
[00:04:03] клиентов по воздействовать для того
[00:04:05] чтобы они совершили дополнительную
[00:04:07] продажу то есть лифт Это разница между
[00:04:10] теми клиентами кому направится какой-то
[00:04:13] воздействие я не купят и если этого не
[00:04:17] совершить вот разница это вот как раз
[00:04:19] таки Apple
[00:04:20] вот
[00:04:22] трансформации Клиент купил и так и так
[00:04:27] трансформация классов Да они учитываются
[00:04:29] то есть у нас вот из этой матрички там
[00:04:32] четыре варианта мы
[00:04:34] классу один присвоему те кто у нас не
[00:04:37] купит если мы не отправим СМСку и те кто
[00:04:41] купит если
[00:04:44] мы отправим им и они не купят не надо на
[00:04:49] них тратить деньги
[00:04:50] [музыка]
[00:04:52] наоборот Наоборот
[00:04:54] 11 это кто у нас купит и так мы на них
[00:04:59] деньги не тратим А на тех кто
[00:05:01] если мы не отправим не купят на них
[00:05:05] тратим деньги хорошо получается В какой
[00:05:08] задаче на обучение мы свели
[00:05:11] моделирование здесь
[00:05:13] классификацию верно А что если у нас в
[00:05:18] качестве
[00:05:20] выхода не купит не купит А сколько денег
[00:05:24] Сколько денег тогда это регрессивная
[00:05:27] будет задача
[00:05:32] тогда это уже будет задача не через
[00:05:36] трансформацию классов а допустим через
[00:05:38] тоже дерево
[00:05:40] которое кстати есть на симуляторе медлей
[00:05:44] Я пытался и я пока не могу
[00:05:50] допустим представим ситуацию к нам
[00:05:53] приходит маркетологи говорят
[00:05:56] хотим модель тока
[00:06:00] для чего
[00:06:03] это халтурка на недельку справишься
[00:06:08] что какие твои действия
[00:06:14] Ну во-первых я подойду к маркетологам
[00:06:18] там или позвоню им Да там и спрошу для
[00:06:20] чего им нужна модель оттока что они в
[00:06:22] итоге хотят получить Ну то есть на что
[00:06:25] повоздействовать там да там то есть
[00:06:28] понять хотя бы что мы будем там
[00:06:32] оптимизировать Да там или на что мы
[00:06:34] будем влиять от этого подобрать уже
[00:06:36] какую-то свою метрику для задачи
[00:06:39] вообще как вот относится задача
[00:06:42] моделирования и прогноза тока Я помню
[00:06:45] смотрел видео Валерия Бабушкина я забыл
[00:06:50] по-моему
[00:06:52] я помню что Валерий говорит модели
[00:06:55] только она не нужна
[00:06:59] две задачи с помощью модели оттока по
[00:07:04] моему также пытаются найти тех людей на
[00:07:07] которых нужно по воздействию для того
[00:07:08] чтобы они остались
[00:07:10] в облифте Мы также воздействуем людей но
[00:07:13] только чтобы они купили то есть в этом и
[00:07:15] в этом случае мы пытаемся
[00:07:17] дозаработать скажем так на своей
[00:07:19] аудитории Ладно меня решаем задачу тока
[00:07:22] получили некоторую на выходе
[00:07:24] вероятность что пользователь течет как
[00:07:28] бы мы
[00:07:29] учитывая то что исходная задача Ну как
[00:07:32] бы было только не было бинарное как мы
[00:07:37] вот имея вероятности можем обработать
[00:07:40] выходы модели чтобы что-то Дальше сами
[00:07:42] делать принимать решение Я думаю что
[00:07:45] можно установить какой-нибудь trashold
[00:07:48] отсечку по которой мы будем
[00:07:50] говорить что
[00:07:52] человек скорее всего уйдет допустим это
[00:07:55] может быть там 50 процентов да там
[00:07:57] уверенность 0,5 так далее И только по
[00:08:01] достижению этой отсечки воздействия этих
[00:08:04] пользователей которые превышает ее Какие
[00:08:07] метрики обычно используются
[00:08:09] оттекают понятно дело
[00:08:12] не ровно половина пользова здесь есть
[00:08:16] дисбаланс классов Какие метрики ты
[00:08:19] знаешь для дисбаланса классов для
[00:08:22] дисбаланса классов Я думаю здесь может
[00:08:25] подойти Взвешенный F1 мира и может
[00:08:29] подойти
[00:08:31] Rock PR это когда там precision recal
[00:08:33] расскажи подробнее Вот как можно
[00:08:37] подбирать отсечку для
[00:08:41] Ну вот пиар состоит у нас с каких метрик
[00:08:44] precision recola мы получили
[00:08:48] вероятность оттока или какой-то скоро
[00:08:52] тока и мы хотим перейти к
[00:08:56] названным метрикам классификации вот как
[00:08:59] мы можем отсечку здесь подбирать
[00:09:02] За что каждый Метрика отвечает из этих
[00:09:05] двух и какая между ними вообще
[00:09:08] закономерность я начну чуть-чуть
[00:09:12] шага назад что у нас когда
[00:09:16] когда мы используем классификацию то у
[00:09:19] нас
[00:09:20] появляется так называемая Матрица ошибок
[00:09:22] когда у нас есть
[00:09:25] значение таргета и значение
[00:09:29] [музыка]
[00:09:31] непосредственной модели То которое нам
[00:09:33] предсказывает и
[00:09:35] Матрица ошибок у нас по диагонали если
[00:09:39] мы берем то это у нас правильно
[00:09:42] предсказанный положительный класс
[00:09:43] правильно предсказанный отрицательный
[00:09:45] класс и по другой диагонали Это
[00:09:49] неправильно сказано положительно
[00:09:50] неправильно предсказанный отрицательный
[00:09:52] соответственно у нас прессижен это так
[00:09:56] называемая точность предсказание То есть
[00:09:59] это отношение
[00:10:02] Используйте то есть правильно
[00:10:05] предсказанных положительного класса
[00:10:10] на сумму Позитив плюс
[00:10:13] Представьте менеджер который не проходил
[00:10:16] Старт Мэри симулятор не знаю ничего ты
[00:10:20] мне
[00:10:21] объясняешь что вообще
[00:10:25] точность это у нас
[00:10:28] что мы предсказали положительный класс и
[00:10:30] как можно меньше в этом ошиблись
[00:10:32] А recola это полнота это что мы как
[00:10:35] можно больше объектов положительного
[00:10:37] класса предсказали можно покрыли свои
[00:10:41] модели покрыли свои модели
[00:10:44] престижение нам важно чтобы
[00:10:47] мы не ошибились на первом классе
[00:10:50] положительных срабатываний а приколе Ну
[00:10:54] то есть мы например можем взять просто
[00:10:56] топ-5 но они Точно Вот все относятся к
[00:10:59] нашему нас классу а приколе Главное
[00:11:02] чтобы покрытие было больше А там если мы
[00:11:05] какие-то лишнее задеваем это уже не так
[00:11:09] и соответственно
[00:11:11] возвращаясь к рок PR кривой Это
[00:11:13] получается что мы по различным вот этим
[00:11:17] трешолдам замеряем присяжные рекол и
[00:11:20] строим их на графике
[00:11:23] и соответственно Метрика PR ой Rock PR
[00:11:27] это будет площадь вот под кривой
[00:11:31] Допустим мы приходим К менеджеру говорим
[00:11:34] вот у нас площадь подберет кривой 1.9
[00:11:38] такой четкое значение Он спрашивает А
[00:11:43] как мы можем Ну вот быть уверенным что
[00:11:46] завтра не будет там один из темы после
[00:11:49] завтра там два и два Вот как можно
[00:11:53] какое-то оценить диапазон в котором
[00:11:55] болтается
[00:11:56] во-первых я могу конечно ошибаться но
[00:11:59] по-моему
[00:12:00] больше единицы не может быть не попался
[00:12:04] хорошо второе мы можем построить
[00:12:08] доверительный интервал
[00:12:10] э для
[00:12:12] изучения Рог но он у нас допустим же
[00:12:16] есть выборка на которой мы обучались
[00:12:19] и мы можем с помощью бутстропа
[00:12:22] повытаскивать
[00:12:24] и проитрироваться Да там несколько там
[00:12:27] тысяч раз и за счет этого построить
[00:12:30] доверительный интервал метро
[00:12:35] расскажи вообще как работает
[00:12:39] у нас допустим есть выборка
[00:12:42] она пришла к нам из генеральной
[00:12:45] совокупности Мы про которую мы ничего не
[00:12:47] знаем И у нас есть только вот эта
[00:12:48] выборка мы можем вытаскивать часть
[00:12:51] значений
[00:12:52] из
[00:12:54] доступных выборки считать необходимые по
[00:12:57] ней там статистики и возвращать обратно
[00:12:59] значение
[00:13:02] сколько значение вытаскивает Можно Все
[00:13:05] можно все
[00:13:08] значений я вот этот момент
[00:13:12] не готов
[00:13:15] Я помню там есть нюанс какой-то
[00:13:18] но я себе в пометках ставил что я бы
[00:13:22] брал чуть меньше значение по количеству
[00:13:24] выборки Ну то есть чуть меньше чем
[00:13:27] основная выборка
[00:13:29] много раз дальше
[00:13:35] и мы получаем
[00:13:38] мы делаем с помощью быстро по вычисляем
[00:13:41] вычисляем какую-то статистику заносим ее
[00:13:44] естественно куда-нибудь там сохраняем
[00:13:45] Вот это количество раз и мы статистика
[00:13:49] на нас
[00:13:50] озвучена задача интересует
[00:13:53] рок пиар
[00:13:55] Ну то есть мы достаем выборку обучаем на
[00:13:59] ней модель замеряем на нейрок пиар
[00:14:01] сохраняем результат Так мы повторяем
[00:14:04] повторяем мы еще раз обучаем модель
[00:14:07] делаем предсказание
[00:14:10] сказание на неё одна модель но мы
[00:14:13] несколько раз
[00:14:18] потому что тогда получается 10 тысяч раз
[00:14:22] обучать модель да и это уже получится по
[00:14:25] моему
[00:14:29] возможно
[00:14:31] так вот мы достаем с помощью
[00:14:37] мы делаем предсказание модели замеряем
[00:14:41] рок PR и сохраняем его так мы повторяем
[00:14:44] много-много раз и получаем какой-то
[00:14:48] распределение нашей пиар значение
[00:14:53] и по
[00:14:55] [музыка]
[00:14:57] о данной выборки мы уже можем
[00:15:00] [музыка]
[00:15:01] вычислить доверительный интервал То есть
[00:15:04] если заданной точности То есть если мы
[00:15:06] берем там 95 процентов доверительный
[00:15:10] интервал то получается что нам нужно
[00:15:14] понтилям то есть по два с половиной 97,5
[00:15:19] контилия взять
[00:15:21] интервал и в нем будет находиться наша
[00:15:24] значение пиар кривой Да хорошо сразу
[00:15:27] тогда дам обратную страху все правильно
[00:15:31] кроме вот то что ты не уточнил размер
[00:15:34] выборки правильно брать столько же
[00:15:37] сколько данных выборки у нас
[00:15:41] повторениями то есть какой-то элемент
[00:15:43] будет там два раза три какой-то ноль раз
[00:15:45] но каждый раз тоже размер потому что
[00:15:48] иначе мы смещенную какую-то метрику
[00:15:51] будем оценивать а нет уже которая нас
[00:15:52] интересует Я может уточнить Правильно ли
[00:15:55] я понял что
[00:15:57] вот мы берем всю выборку но Допустим мы
[00:16:00] берем условно 10 процентов мы из него
[00:16:02] выкидываем И эти 10 процентов замещаем
[00:16:04] повторами вот взятой выбор
[00:16:07] не так мы
[00:16:11] берем выборку
[00:16:14] 1000 элементов
[00:16:16] мы сэмплим по тысяче элементов Но это
[00:16:20] вот Случайный из тысячи То есть какой-то
[00:16:23] когда мы так случайно сэмплим
[00:16:25] несколько раз какой-то ноль раз там и
[00:16:28] так далее и каждый раз немножко будет
[00:16:30] перекос свою сторону и мы таким образом
[00:16:32] расшатываем нашу метрику получаем
[00:16:34] некоторую такую оценку потому что у нас
[00:16:37] выборка которую мы имеем это просто
[00:16:41] лучше самое большее что мы знаем о
[00:16:45] генеральной совокупности и мы по сути
[00:16:47] воспроизводим как бы мы сэмплились
[00:16:48] совокупности
[00:16:52] такой вопрос Если у нас нет возможности
[00:16:55] сэмплить тысячи раз у нас есть например
[00:16:59] посчитаны есть
[00:17:03] 5 моделей 5 фолдов и
[00:17:07] наша метрикой которую мы хотим оценить
[00:17:10] исходя из того что ты сказал холды я
[00:17:12] могу предположить что можно их сравнить
[00:17:15] с помощью
[00:17:16] кроссволидации замерить их качество но
[00:17:20] этих моделей если вам просто усредним
[00:17:23] опять получим просто одну оценку нам
[00:17:25] нужно выбрать из пяти моделей одну лучше
[00:17:28] одна модель
[00:17:31] обычно 5 раз на разных
[00:17:36] и у нас на 5 разных болтах есть оценки
[00:17:40] наши метрики
[00:17:43] дал ответ то что
[00:17:47] кросс валидация такой
[00:17:49] игрушечные
[00:17:51] маленьких размерах но тоже за счет того
[00:17:55] что у нас разные холды мы получаем
[00:17:57] распределение и учитывая то что Ну в
[00:18:02] принципе
[00:18:03] на метрике
[00:18:04] в каком-то виде метрики усреднения в
[00:18:07] силу известная теорема которую ты мне
[00:18:09] поможешь назвать симметрики Да
[00:18:14] что-то там усредняют Поэтому даже
[00:18:19] у такого маленького сэмплов будет
[00:18:24] асимптотически все сходиться к тому что
[00:18:27] у нас нормальных людей
[00:18:30] все
[00:18:32] можно оценивать
[00:18:37] я если правильно понял ты говоришь про
[00:18:40] Центральный предельную теорему
[00:18:41] собеседование
[00:18:54] Мне нужно воспроизвести
[00:18:56] Дания Я верю а
[00:19:00] возможно ты знаешь такой Адванс Вопрос
[00:19:04] какие бывают схемы
[00:19:08] распорядации Ну вот не в рамках разных
[00:19:11] задач А в рамках вот просто насколько
[00:19:12] бить сколько повторений делать разбиение
[00:19:16] и как это влияет на какую-то там
[00:19:21] точность оценки наши метрики мы можем
[00:19:23] воспользоваться просто методом
[00:19:25] отложенной выборки самый простой
[00:19:26] тестовый кино Да там и на нем замерять
[00:19:29] качество Когда же мы используем
[00:19:31] непосредственно кросс фалидацию у нас Я
[00:19:35] знаю три варианта проведения кросс
[00:19:37] валидации обычно
[00:19:38] дефолт когда мы разбиваем на какое-то
[00:19:41] количество солтов равных и по очереди
[00:19:45] это все модель обучается на минус одном
[00:19:49] фалде и замеряется качественном хобби
[00:19:54] Это хороший вариант Когда у нас нет
[00:19:57] временной зависимости в данных Когда у
[00:19:59] нас есть временная зависимость это у нас
[00:20:01] уже там Сири Сплит идёт мы в ней у нас
[00:20:05] нет временной зависимости у нас
[00:20:07] keefold и мы хотим определить сколько
[00:20:10] насколько Fall of Beats вот как мы
[00:20:13] принимаем решение на количество холодов
[00:20:17] насколько я помню
[00:20:20] когда вот как раз таки Я учился что есть
[00:20:22] такой момент что в идеале конечно чтобы
[00:20:25] количество фолдов равнялось количество
[00:20:28] элементов у нас наши выборки
[00:20:41] вот и это самый лучший вариант но он
[00:20:44] естественно очень для чего для точной
[00:20:48] оценки потому что интересует неточная
[00:20:51] оценка мы сравниваем несколько моделей
[00:20:54] точность оценки Как по-другому
[00:20:56] называется Я возможно путаю конечно
[00:20:58] возможно
[00:21:05] а бас Да А какой еще есть свойство
[00:21:11] разброса
[00:21:12] между ними как раз таки проблема вот
[00:21:16] например если мы хотим замерить
[00:21:18] финальное качество модели нас интересует
[00:21:22] схема валидации с меньшей с меньшим
[00:21:26] смещением или с меньшим разбросом когда
[00:21:29] мы сравниваем модели между собой Да мы
[00:21:31] хотим финальное качество модели
[00:21:32] посчитать
[00:21:34] тогда я думаю что это должно быть
[00:21:37] все-таки
[00:21:37] смещение у нас важно потому что нам
[00:21:40] важно
[00:21:41] как можно ближе оценивать наш параметр
[00:21:45] метрику
[00:21:48] довольно похожие модели Вот мы что-то
[00:21:51] там поменяли добавили набор новых вещей
[00:21:53] или там оптимизировали параметры и хотим
[00:21:57] сравнить и у них точность точнее
[00:22:00] смещение примерно одинаковое правильно
[00:22:03] Вот Но в таком случае нам нужно обращать
[00:22:06] внимание на разброс
[00:22:08] потому что Чем выше разброс тем у нас
[00:22:12] дальше могут улетать значения от
[00:22:15] истинного но здесь не про значение от
[00:22:18] истинного чем больше у нас разброс тем
[00:22:22] менее
[00:22:24] чувствительная схема валидации и мы если
[00:22:27] сравниваем две модели одно лучше другой
[00:22:29] Она может быть просто в рамках их
[00:22:32] погрешности и мы на самом деле принимаем
[00:22:34] решение можно сказать по кофейной гуще а
[00:22:37] не на каком-то
[00:22:41] значимым уровне кстати про распределение
[00:22:46] право смещение Расскажи про
[00:22:51] Ну допустим мы построили нашу модель
[00:22:56] оплета у нас есть какая-то старая ручная
[00:23:01] подборка пользователей
[00:23:03] на которых мы воздействовать есть новая
[00:23:07] такая
[00:23:08] крутые машины обучением
[00:23:11] и мы проводим
[00:23:14] Расскажи Из каких основных компонентов
[00:23:17] состоит аб-тест Я помню в резюме было
[00:23:20] как раз ты соболезненно освоился
[00:23:23] Да я решил эту задачу на симуляторе Ну
[00:23:28] значит в первую очередь мы выбираем
[00:23:30] метрику по которой мы будем делать
[00:23:32] выводы что у нас есть различия либо нет
[00:23:35] различий
[00:23:37] далее мы дизайнер уже сам эксперимент Мы
[00:23:42] сначала устанавливаем выбираем ошибку
[00:23:45] первого рода
[00:23:49] Но это ложноположительная ошибка это с
[00:23:52] частотой с которой мы
[00:23:54] будем фиксировать изменения тогда когда
[00:23:58] на самом деле этого изменения нет также
[00:24:00] после того как мы установили уровень
[00:24:03] значимости Да он обычно опять берет 05
[00:24:06] берется
[00:24:08] мы устанавливаем ошибку второго рода это
[00:24:12] ложная отрицательное это тогда когда мы
[00:24:15] говорим что нулевая гипотеза верна тогда
[00:24:19] когда на самом деле есть изменения
[00:24:21] [музыка]
[00:24:23] группа А и Б обе ошибки играют роль Но
[00:24:28] ты все верно говоришь просто хочу чтобы
[00:24:30] ты приземлил это теперь на
[00:24:34] [музыка]
[00:24:36] Вот именно на метрике по группам можно
[00:24:40] положительная ошибка то есть ошибка
[00:24:41] первого рода это мы говорим что у нас
[00:24:45] новый алгоритм лучше хотя на самом деле
[00:24:49] он не лучше ошибка второго рода наоборот
[00:24:51] мы говорим что старые лучше не изменился
[00:24:55] когда на самом деле второй оказался
[00:24:57] лучше так лучше или не изменился мы не
[00:25:00] замечаем что наш новый алгоритм он на
[00:25:03] самом деле лучший и принимаем Что старые
[00:25:07] все-таки лучше чем новый То есть это
[00:25:10] ошибка второго рода когда фактически
[00:25:13] Ну там Ну опять ты сказала что лучше на
[00:25:16] самом деле что со значимой разница между
[00:25:19] ними Нет хорошо потому что
[00:25:23] например можем заметить в том числе со
[00:25:26] значимую разницу и она будет Ну когда
[00:25:30] например второй алгоритм хуже и он тоже
[00:25:33] будет со значимая отличаться и мы
[00:25:36] поймаем это или не понимаем
[00:25:41] например Расскажи что такое пивалью
[00:25:45] нулевая гипотеза вот эти все вещи
[00:25:48] это у нас вероятность
[00:25:51] [музыка]
[00:25:52] встретить такой же или более
[00:25:55] экстремально отклонение в данных про
[00:25:58] гипотезы это мы проверяем допустим
[00:26:01] какие-то если у нас различия в
[00:26:03] алгоритмах или нет И у нас нулевая
[00:26:06] гипотеза это то что у нас различий
[00:26:08] алгоритмах нет альтернативный гипотеза
[00:26:10] что есть и вот когда мы провели
[00:26:13] эксперименты замеряем метрики и
[00:26:16] сравниваем их между собой и высчитываем
[00:26:17] пиво или так называемый который нам
[00:26:20] говорит о том что вот ту разницу которая
[00:26:23] мы видим между двумя алгоритмами с какой
[00:26:26] вероятностью мы можем встретить такую же
[00:26:28] или более еще значимую разницу более
[00:26:31] экстремальная более сильная и вот если
[00:26:34] она
[00:26:38] меньше чем наш заданный уровень ошибки
[00:26:42] первого рода то тогда можем сказать что
[00:26:45] у нас есть основания на то чтобы
[00:26:47] Отклонить в любой гипотезу и принять
[00:26:50] альтернативную почти все верно но можно
[00:26:54] еще более
[00:26:57] наговорить ты говоришь про разницу
[00:26:59] заметить разницу такой экстремальную на
[00:27:02] самом деле
[00:27:03] есть у любой статистики у любого теста
[00:27:08] не обязательно на
[00:27:10] разницу средних
[00:27:14] можно
[00:27:17] что Мы заметили такое значение
[00:27:19] статистики или более экстремальное
[00:27:22] Да ну тут просто мне в терминах разницы
[00:27:25] проще воспринимать А как мы в тесте
[00:27:29] определяем сколько нам данных нужно и
[00:27:33] какую разницу можем задать насколько я
[00:27:37] помню Мы это можем проверить с помощью
[00:27:40] а-теста не проверить посчитать посчитать
[00:27:44] посчитать с помощью теста это такой тест
[00:27:47] Когда у нас есть две одинаковые выборки
[00:27:50] и мы по ним итеративно считаем
[00:27:54] статистики И сравниваем между собой ты
[00:27:58] сейчас говоришь про симуляцию
[00:28:02] я говорил про Как мы можем посчитать
[00:28:04] по-моему если у нас есть
[00:28:07] если мы знаем что наши данные пришли из
[00:28:11] нормального распределения тогда мы можем
[00:28:13] использовать формулу
[00:28:14] [музыка]
[00:28:16] наверное сейчас я не воспроизведу но с
[00:28:18] помощью нее можно вычислить и минимально
[00:28:21] значимый
[00:28:24] размер выборки средний дисперсия
[00:28:28] нас интересует
[00:28:31] Если мы если мы считаем
[00:28:34] минимальный значимый эффект размер
[00:28:37] выборки если размер выборки мы считаем
[00:28:39] то у нас должен присутствовать еще
[00:28:45] мы договорились Сегодня могу догадаться
[00:28:47] что Ошибка первого рода и второго рода
[00:28:51] Но на самом деле Да есть такая формула и
[00:28:54] она не только есть для нормального
[00:28:56] распределения есть также там для других
[00:29:00] феноменов и так далее
[00:29:03] а то что ты говоришь про
[00:29:06] интерактивно проведем тест это уже про
[00:29:09] действительно можно оценивать
[00:29:12] если мы не хотим искать формулу через
[00:29:15] симуляции
[00:29:17] Но обычно через них в конце уже
[00:29:20] проверяют действительно мы все правильно
[00:29:23] посчитали и
[00:29:25] выдерживаем
[00:29:27] заявленные уровни ошибок первого рода
[00:29:30] Расскажи
[00:29:32] как проводится симуляции И как понять
[00:29:35] что все правильно все готово
[00:29:39] недавно начал что у нас есть две выборки
[00:29:42] они одинаковые
[00:29:45] Ну мы можем просто взять нашу выборку на
[00:29:48] исторических данных которые задают
[00:29:51] Только желательно
[00:29:53] чтобы на них по моему не было
[00:29:55] экспериментов чтобы не вызывать какие-то
[00:29:57] дополнительные шумы в данных берем одну
[00:29:59] выборку Да там между ними
[00:30:04] умножим на два
[00:30:07] мы считаем различаются ли между ними то
[00:30:11] есть мы считаем по ним статистики такого
[00:30:13] размера выборку Мы берем достаточно
[00:30:15] чтобы детектировать эффект различия
[00:30:19] между
[00:30:21] хорошо Мы только что брать сказали что
[00:30:24] мы по формуле посчитали размер
[00:30:26] минимальный размер необходимый выборки
[00:30:30] такого размера
[00:30:32] дальше
[00:30:34] вот
[00:30:36] мы взяли выборки считаем по ним
[00:30:38] статистики И с помощью
[00:30:41] статистического критериев проверяем Если
[00:30:45] разница между выборками или нет И у нас
[00:30:49] доля того что у нас есть различия в этих
[00:30:54] выборках не должна превышать тот уровень
[00:30:57] значимости который мы изначально перед
[00:31:00] экспериментом поставили как будет
[00:31:02] выглядеть
[00:31:04] распределение равномерно
[00:31:06] [музыка]
[00:31:09] а как мы проверим теперь и какие мы
[00:31:12] здесь ошибки можем посчитать Ну вот мы
[00:31:14] посчитали здесь ошибку первого рода еще
[00:31:17] можно проверить
[00:31:19] ошибку второго рода мощность как это мы
[00:31:23] делаем Что такое мощность
[00:31:25] мощность это обратная величина обратной
[00:31:29] ошибки второго рода а нет мощность
[00:31:32] симуляциях будто проверяем мощность мы
[00:31:35] сделаем симуляцию
[00:31:37] берем две
[00:31:39] заведомо различающиеся выборки
[00:31:44] мы можем из одной выборки взять части
[00:31:47] возьмем к одной выборке прибавим тот
[00:31:51] минимальный значимый эффект который мы
[00:31:53] посчитали по формуле
[00:31:55] И тем самым у нас будет различие выборки
[00:31:59] и вот уже эти две выборки мы будем
[00:32:02] сравнивать на бтесте симуляционно и
[00:32:07] посмотрим детектируем ли мы с
[00:32:10] необходимую мощность
[00:32:11] нужно вероятностью
[00:32:17] и что мы там ожидаем и какое
[00:32:19] распределение в этот раз мы ожидаем
[00:32:22] здесь увидеть количество долек
[00:32:25] количество случаев когда мы детектируем
[00:32:27] различия должна
[00:32:30] быть столько же или больше чем мощность
[00:32:33] То есть это единица минус ошибка второе
[00:32:36] все правильно
[00:32:40] градиентный бустинг самая любимая тема
[00:32:45] как он работает Почему градиентный
[00:32:47] градиентный Бусик это такой вид
[00:32:50] сомблирования моделей
[00:32:53] базовых Когда у нас ошибки
[00:32:59] предыдущей модели является таргетами для
[00:33:01] последующей и
[00:33:03] так далее и так далее и так далее это
[00:33:06] все
[00:33:07] считается Градиент здесь Потому что
[00:33:12] Мы берем
[00:33:14] производную
[00:33:18] считаем разницу между таргетом и
[00:33:24] предсказанием первой модели
[00:33:27] модель
[00:33:29] там допустим я берут самую простую
[00:33:32] которая там можно среднюю по всем
[00:33:34] таргетам поставили Вот и
[00:33:39] берут первый производную Да этого это
[00:33:43] получается что Градиент у нас Мы берем
[00:33:46] производную подставляем туда разницу
[00:33:48] между таргетом и отступа модели далее мы
[00:33:53] считаем
[00:33:55] коэффициент для второй модели для того
[00:33:59] чтобы минимизировать так скажем уже
[00:34:03] ошибку и дальше это поступает следующую
[00:34:08] модель и в следующую модель так и так
[00:34:10] далее Что за коэффициент
[00:34:12] пропустил
[00:34:14] Ну такой поправочный коэффициент скажем
[00:34:17] весовой для того чтобы не будешь с
[00:34:22] другой
[00:34:23] моделью бустинга
[00:34:26] [музыка]
[00:34:29] в простом бустинге этого нету а в
[00:34:32] градиентным подбираются коэффициент
[00:34:35] что же такое Нет ты все верно говоришь
[00:34:39] что мы считаем Градиент ошибки и ты
[00:34:44] хорошо что потом сказал что Градиент
[00:34:46] ошибки они просто
[00:34:47] как-то вначале говорил и мы добавляем
[00:34:50] новую модель с фиксированным весом
[00:34:54] которые
[00:34:56] обозначаются как Learning Raid Это и так
[00:34:59] далее чтобы это если мы градиентом
[00:35:02] бустинге берем первое дерево Не совсем
[00:35:05] понял вопроса Что будет у нас есть
[00:35:08] ансамбль где суммируются какими-то
[00:35:11] весами деревья
[00:35:13] каждый из них нам на что-то свое
[00:35:15] обучается после предыдущего И что если
[00:35:19] мы убираем первое дерево из этого
[00:35:21] ансамбре складываем все остальное если
[00:35:24] мы убираем первое дерево или выбираем
[00:35:26] убираем
[00:35:28] убираем первое дерево делаем
[00:35:30] предсказание смотрим на что-то там то
[00:35:34] есть это самый первый алгоритм по
[00:35:36] которому
[00:35:36] который делал предсказание потом отступы
[00:35:40] которого дальше уже практимировать
[00:35:41] правильно понимаю Не совсем ты верно
[00:35:44] сказал что мы берем средние по таргету
[00:35:47] первое приближение место базы модели А
[00:35:52] ну в этом случае если первое дерево
[00:35:55] будет то там оно сильно же переобучиться
[00:35:58] под данной нет мы же уже ничего не
[00:36:01] обучаем но хорошо Я тебя запутал Да как
[00:36:04] правильно сказала Мы сначала берем
[00:36:06] средние подарки то потом считаем
[00:36:09] градиенты потом строим первое дерево
[00:36:10] потом второе дерево на том что на
[00:36:14] границе от ошибки предсказания среднего
[00:36:18] первого дерева и так далее первое дерево
[00:36:20] оно дает довольно большой
[00:36:24] модель
[00:36:26] А уже если убираем последнее дерево оно
[00:36:30] уже и там шумы какие-то маленькие
[00:36:33] остаточки обучаются и она не сильно
[00:36:35] уровне метрику ну и соответственно
[00:36:37] что-то промежуточное средних там
[00:36:42] большой вес первой модели передается
[00:36:45] такой вопрос Вот есть у нас с разными
[00:36:48] акции
[00:36:50] ВУЗ целая jbm капуст может быть знаешь
[00:36:54] как принцип построения дерева у них
[00:36:57] различается в двух словах
[00:37:01] [музыка]
[00:37:02] капуст это
[00:37:05] детище Яндекса его особенностью
[00:37:08] заключается в том что оно из коробки
[00:37:11] может категориальная фичи обрабатывать у
[00:37:14] их же Boost у него по-моему идет
[00:37:26] одно дерево там есть принципиальное
[00:37:29] различие
[00:37:30] Я знаю что их же буста у него помимо
[00:37:34] первой производной есть еще вторая
[00:37:35] производная когда
[00:37:41] давай вот именно про Дерево у Lite jbm
[00:37:44] он строится
[00:37:45] Ну то есть обрезается листы Ну то есть
[00:37:48] они только в одну сторону расширяется и
[00:37:50] он быстро быстрее работает
[00:37:54] ну то есть у него у нас есть только там
[00:37:58] один ответ это обрезанное дерево такое
[00:38:00] правильную сторону немножко
[00:38:03] округляешь
[00:38:05] некорректно в терминологии
[00:38:07] тоже некорректно Ты про правильно
[00:38:10] подумал Но то как Ты объясняешь Он
[00:38:14] работает
[00:38:15] Как же быть строятся дерево одно есть
[00:38:19] прям даже два слова я не вспомню
[00:38:29] нет но могу по предположить что это
[00:38:33] связано с глубиной и либо с размером с
[00:38:36] количеством листьев но можно сказать да
[00:38:39] в их же быть все мы как строим вот у нас
[00:38:43] есть разбиение в каком-то признаку мы
[00:38:46] получаем например две группы
[00:38:49] элементов дальше мы к не разбили на две
[00:38:53] каждый из этих групп мы дальше не
[00:38:56] двигаемся А в LG beami У нас вот разбили
[00:39:00] на две У нас две новые ноды потом мы
[00:39:03] среди всех выбираем какую разбить
[00:39:06] разбили это на 2 теперь выбираем из этих
[00:39:08] трех Может быть сейчас лучше разбить еще
[00:39:11] эту на две а может быть лучше Вот это
[00:39:13] разбить мы как бы всех одинаково
[00:39:17] принимаем и а это идет к тому что могут
[00:39:21] быть очень сильно асимметричные А их же
[00:39:25] будете они все ну вот
[00:39:28] сайте как зависит количество листьев от
[00:39:31] Глубины в их же пустеп Вайс деревьях они
[00:39:38] два в степени
[00:39:44] нас если глубина глубина 2 то у нас
[00:39:50] будет Два листа
[00:39:53] на 3 забьются еще будут 4 и так далее
[00:40:01] Вопросик Как можем тоже это
[00:40:08] что там много неуверенных своих моделях
[00:40:10] вот хотим сделали предсказание
[00:40:13] как-то оценить
[00:40:15] вот новых данных модель делает
[00:40:18] предсказания хотим оценить насколько
[00:40:20] модель уверенно или не уверена своих
[00:40:22] предсказаниях модель регрессии
[00:40:24] градиентным бустинг регрессивный То есть
[00:40:27] как можем У нас есть метрики но Метрика
[00:40:31] это что-то про всю модель в целом а мы
[00:40:34] хотим именно на уровне одного объекта
[00:40:36] понять это объект который
[00:40:40] модели сильно понятно как предсказывает
[00:40:43] и хорошо В таких вот сейчас разбирается
[00:40:46] какой-то объект или это объект
[00:40:48] совершенно новый и типа предсказания
[00:40:51] которые она сделала она очень такой
[00:40:53] шаткое что мы можем сделать как можем
[00:40:56] какую-то оценку уверен с неуверенность
[00:41:01] [музыка]
[00:41:05] Но я могу ошибаться но мне единственное
[00:41:08] что приходит на ум это вот посмотреть
[00:41:12] дисперсию насколько она изменилась
[00:41:15] [музыка]
[00:41:17] Ну у нас допустим когда дерево строится
[00:41:22] Да мы там разбиваем
[00:41:25] на признаки и смотрим насколько
[00:41:28] у нас изменилось допустим если мы
[00:41:31] говорим про регрессию насколько сильно
[00:41:32] изменилась у нас
[00:41:34] дисперсия то есть разброс пока еще не
[00:41:38] понимаю
[00:41:42] обычная модель на новых данных она
[00:41:45] делает предсказание как мы здесь
[00:41:47] какой-то дисперсию
[00:41:50] мы не знаем реальные Таргет найти просто
[00:41:54] хотим например отследить что чуваки на
[00:41:57] этих данных мы уверены что модель
[00:42:00] знает что предсказала на этих есть
[00:42:04] сомнения Будьте Аккуратнее Ну возможно
[00:42:06] не знаю вызвать этот метод фьючером
[00:42:10] потенции
[00:42:12] Это не по объектам Ну хорошо сразу тогда
[00:42:17] подскажу есть задача третьего уровня
[00:42:20] симуляторе называется Бусинка
[00:42:25] Как можно оценивать уверенность
[00:42:29] предсказание модели в случае градиентов
[00:42:31] если совсем вермитрия такая вот у нас
[00:42:35] модель Как делать предсказания если
[00:42:37] модель уверена в этом объекте у нас
[00:42:40] деревья друг друга исправляют и если то
[00:42:45] она уже на первых стадиях на первых там
[00:42:48] десяти стать
[00:42:50] нужным ответа следующий будет какой-то
[00:42:53] косметику вносить А если модель не
[00:42:56] уверена то от дерева к дереву на таких
[00:42:59] объектах и будет ворошить и можем там с
[00:43:03] каким -то какие-то такие Под ансамбли
[00:43:07] посмотреть как у них
[00:43:10] есть разногласия
[00:43:12] или нет И посчитать
[00:43:18] разброс и Мы это можем сделать на новых
[00:43:22] объектах спокойно по объекту то есть
[00:43:25] Можем Конечно все это сделать
[00:43:27] но таким образом
[00:43:30] точно оценить модели с такими объектами
[00:43:36] хорошо работает плохо работает
[00:43:45] Дальше
[00:43:47] расскажи про диплои Маша и сервисов
[00:43:52] как-то вообще происходит что это такое
[00:43:54] зачем это нужно диплоид насколько
[00:43:56] понимаю это вывод Продакшен это уже
[00:44:00] непосредственно
[00:44:01] запуск модели и я так понимаю что еще
[00:44:06] автоматически до обучения модели можно
[00:44:09] сделать на новых данных которые
[00:44:12] происходят допустим у нас модель мы
[00:44:16] вручную обучать хотя бы просто как мы ее
[00:44:19] вводим в продакш и здесь есть элементы
[00:44:22] шаги подводные камни это задача
[00:44:27] но непосредственно у нас я еще не дошел
[00:44:33] к сожалению
[00:44:34] могут так порассуждать какие есть этапы
[00:44:38] рассуждают Да что
[00:44:41] первое что нам самое главное это Нужны
[00:44:44] хорошие данные
[00:44:46] правильные без
[00:44:49] ошибок пропусков и так далее
[00:44:51] То есть пусть у нас хорошие данные уже
[00:44:56] Кстати
[00:44:57] как называется Может быть шаг может быть
[00:45:02] специальность которая занимается
[00:45:05] качественными данными
[00:45:12] Да ну допустим мы уже на стадии
[00:45:15] моделирования проконтролировали что
[00:45:17] данные хорошие все источники
[00:45:21] Вот именно сам тепло и как происходит
[00:45:24] что вообще мы делаем Ну у нас допустим
[00:45:27] модель висит где-нибудь
[00:45:30] в Облаке в том же да там или на серваке
[00:45:33] что такое висит
[00:45:35] Ну находится
[00:45:39] Что такое находится Ну то есть как я
[00:45:43] понимаю что на каком-то сервере
[00:45:46] развернута Ну то есть там есть
[00:45:48] как сервис такой
[00:45:51] допустим
[00:45:53] какой-нибудь стажер обучил клевую
[00:45:56] модельку ноутбуке
[00:45:59] а как сделать так чтобы хорошая модель
[00:46:02] коллектив ноутбуке вдруг начала
[00:46:04] приносить деньги Ну то есть она должна
[00:46:08] выдавать там какие-то предсказания то
[00:46:10] есть по запросу к ней поступают данные в
[00:46:12] эту модель
[00:46:15] Ну как общается сервер клиент с помощью
[00:46:18] пул квест
[00:46:23] И что это за такие интересные ключевые
[00:46:27] слова
[00:46:29] путь когда мы что-то вносим я вот
[00:46:33] сомневаюсь может быть некорректно его
[00:46:35] называю
[00:46:38] Да
[00:46:40] чувствуется
[00:46:42] когда мы пытаемся что-то изменить на
[00:46:46] севере либо в нашу модель то есть мы
[00:46:47] туда приносим где-то мы что-то забираем
[00:46:51] оттуда получаем какие-то предсказания
[00:46:53] там или еще вот и таким образом Когда у
[00:46:58] нас модель где-то
[00:47:00] висит в Облаке на сервере не поступают
[00:47:06] какие-то данные она их обрабатывает
[00:47:10] выдает предсказание мы забираем ее по
[00:47:12] гету по запросу и уже эти
[00:47:17] данные использую
[00:47:20] Какие ты знаешь
[00:47:27] [музыка]
[00:47:29] что угодно просто первое что приходит на
[00:47:31] ум это
[00:47:35] не орк это некоторые методология Как
[00:47:40] правильно вот эти самые запросы
[00:47:43] оформлять структурировать
[00:47:49] библиотека по-моему так называется
[00:47:50] request Если я правильно помню Ну не
[00:47:54] совсем
[00:47:55] это еще не фреймворк это именно
[00:48:07] [музыка]
[00:48:08] сейчас
[00:48:14] как фиксируется версия библиотек
[00:48:18] а вдруг там обновление вышло и вдруг
[00:48:21] что-то может пойти не так ну Мне на ум
[00:48:24] приходит здесь только гид
[00:48:26] версионирование какие-то именно проход А
[00:48:29] вот в колледже используется много
[00:48:31] библиотек так и версия ты имеешь ввиду
[00:48:35] что когда мы допустим делаем модель мы
[00:48:37] там
[00:48:38] Файлик рекламируем
[00:48:40] версии библиотек фиксируем
[00:48:44] нас нужен Где используется Ну мы
[00:48:48] допустим можем установить виртуальное
[00:48:51] окружение с помощью
[00:48:54] команды с этого файлика закачать все вот
[00:48:57] эти библиотеки именно в тех версиях
[00:49:00] которых мы проектировали и это будет
[00:49:04] гарантировать то что у нас не будет
[00:49:05] каких-то там ошибок не будет конфликтов
[00:49:08] с новыми версиями
[00:49:10] Потому что
[00:49:12] когда что-то где-то библиотека не
[00:49:15] фиксирована обновляется Потом что-то
[00:49:17] падает
[00:49:18] и
[00:49:20] день выяснять
[00:49:29] сервис deployds docker контейнере в
[00:49:32] котором
[00:49:34] фиксируется всю нужное окружение Все
[00:49:37] нужно там база данных библиотек чтобы
[00:49:42] наш наша модель или наш другой сервис
[00:49:45] жил зафиксированном таком
[00:49:48] аквариуме окружение контейнере и здесь
[00:49:52] мотор от того что там меня обновляется в
[00:49:54] мире
[00:49:55] мы были уверены что она будет работать
[00:49:58] через год
[00:50:01] а за какими вот когда мы сервис уже с
[00:50:05] диплоили он работает метриками можем
[00:50:06] следить такие технические Может там
[00:50:09] пару-тройку назовёшь наверное время
[00:50:11] приема и время забора сигнала Ну ответа
[00:50:15] насколько там у нас велик этот Pink
[00:50:18] Насколько быстро работает сервис
[00:50:21] [музыка]
[00:50:23] видимо еще можно количество запросов
[00:50:26] [музыка]
[00:50:27] фиксировать тоже
[00:50:30] я думаю да потому что допустим
[00:50:34] если мы не фиксируем
[00:50:38] количество там запросов Да к модели и
[00:50:42] вдруг там что-то упадет
[00:50:44] мы можем посмотреть
[00:50:47] мы можем не узнать что был какой-нибудь
[00:50:50] пиковый скачок Да там в запросах из-за
[00:50:53] этого модель упала это была именно в
[00:50:56] этом причина не в чем-то другом
[00:51:00] что если у нас нет требования на
[00:51:05] реакцию
[00:51:11] Нужно ли нам
[00:51:16] Ну в таком случае мне кажется Ну то есть
[00:51:19] естественно тут все цели зависит сначала
[00:51:25] для чего нам Для чего у нас используется
[00:51:28] этот сервис в каком месте наша бизнес
[00:51:32] цепочки по последний вопрос перед
[00:51:35] кодинг завершением вот допустим у нас по
[00:51:40] каким-то причинам вдруг модель не
[00:51:43] посчитала предсказание
[00:51:45] у нас Real Time сервис и Ответ нужен
[00:51:48] быстро что мы тогда можем сделать
[00:51:55] можно
[00:51:57] [музыка]
[00:51:59] найти похожий запрос и выдать по нему
[00:52:03] вот эти вот ответ такой либо просто
[00:52:06] предыдущий какой-нибудь
[00:52:09] допустим как вот
[00:52:13] сказать если Бывает так что во временных
[00:52:17] рядах
[00:52:18] bestline это то что у нас ничего не
[00:52:21] поменялось то есть какие у нас запросы
[00:52:22] были да то они примерно такие же дальше
[00:52:25] будут и на основании этого можно
[00:52:28] предположить что либо поискать похожие
[00:52:30] запрос из недавних Да там либо просто
[00:52:32] последний такой же какой-нибудь выдать
[00:52:33] похоже поискать это звучит как какая-то
[00:52:37] тоже
[00:52:39] задача
[00:52:41] тоже можно что-то пойти не так Может
[00:52:44] тоже довольно долго занимать
[00:52:51] только ты сказал про предыдущий вот
[00:52:54] ответ на запрос но скорее ты имел ввиду
[00:52:58] предыдущие какие-то значения
[00:53:05] действительно какое-то
[00:53:09] там упрощенная там кстати ты например
[00:53:13] делаешь модель предсказания какого-то
[00:53:18] временного ряда например прогноз спроса
[00:53:20] простой случай и
[00:53:23] вот чего бы ты начинал моделировать
[00:53:25] каких моделей таких подходов Я бы
[00:53:29] наверное выбрал
[00:53:31] регрессию
[00:53:33] линейную в этом случае потому что она
[00:53:37] которая умеет
[00:53:40] в тренды Ну то есть она умеет
[00:53:43] еще проще
[00:53:46] Может проще линейной регрессии
[00:53:49] Я думаю что ну либо простой быдлайн то
[00:53:53] же самое что и было Вот энтом какое-то
[00:53:56] окно назад то есть Может там медиану
[00:53:59] средняя там Макс меню То есть ты дай
[00:54:03] даже
[00:54:04] есть какие-то признаки ты можешь просто
[00:54:07] подарки взять предыдущие
[00:54:09] и уже вот такой модели достаточно и для
[00:54:14] Full Back ответов сервисе и чтобы
[00:54:16] посмотреть что тебя
[00:54:20] работает все как бы нигде не падает и
[00:54:24] потом уже
[00:54:25] Линейная модель это усложнение
[00:54:29] уже там
[00:54:30] дополнительные вещи которые там с
[00:54:33] агрегатом потому что только потом если
[00:54:36] игра стоит
[00:54:38] переходить к
[00:54:41] любимом бустингом тем более чем то еще
[00:54:44] более сложному То есть это условно такое
[00:54:47] итеративное усложнение У нас есть
[00:54:50] некоторый такой в голове всегда график
[00:54:53] вот типа время затраты вот там точность
[00:54:56] условно вот там Сколько денег можно
[00:54:58] принести и мы можем принести Ну как бы
[00:55:01] уже супер базой моделью Там просто
[00:55:04] средняя на агрегатах Линейная уже
[00:55:08] настолько много что там вот дальше
[00:55:11] период осложнения там с помощью бусингов
[00:55:14] он там не стоит свечи мы там за неделю
[00:55:17] сделаем чем он там возиться очень долго
[00:55:20] с чем-то сложным что не такой большой
[00:55:22] прирост
[00:55:24] супер Давай тогда откроем
[00:55:27] Google и что-нибудь в этом духе сделаем
[00:55:32] простую задачку думаю за 5-10 минут это
[00:55:34] здание я
[00:55:36] многим давал собеседование многих она
[00:55:39] завалило
[00:55:41] задание очень простое Сейчас я вас спалю
[00:55:45] называется графики нет
[00:55:50] а напиши пожалуйста функцию ты можешь
[00:55:54] даже кстати в макдауне эти условия
[00:55:56] прописать Напиши пожалуйста функцию
[00:55:59] которая
[00:56:01] выводит числа от одного до n Но если
[00:56:07] число делится на 3 вместо числа нужно
[00:56:10] выводить из
[00:56:12] Fi Z если число делится на 5 место числа
[00:56:18] нужно вводить баз
[00:56:20] и
[00:56:23] если число делится и на 3 на 5 нужно
[00:56:27] выводить из вас
[00:56:30] так если внутри
[00:56:32] [музыка]
[00:56:41] если на 5
[00:56:50] если оба числа
[00:57:01] так и
[00:57:03] и на 3 на 5
[00:57:08] у нас фисбас
[00:57:13] супер
[00:57:22] Значит нужно писать такую
[00:57:32] мы принимаем сюда число какой-то да
[00:57:35] [музыка]
[00:57:49] по-моему так
[00:57:52] если у нас внутри есть у нас на 5 Ну
[00:57:55] можно здесь попробовать такое
[00:57:58] в лоб решение что
[00:58:01] допустим
[00:58:03] как я здесь написал слова если у нас
[00:58:06] делится без остатка на 3 но при этом у
[00:58:11] нас не делится
[00:58:12] без остатка на 5 то там выводить и так
[00:58:16] далее
[00:58:19] третий и получится что если делится это
[00:58:23] тогда
[00:58:27] [музыка]
[00:58:33] [музыка]
[00:58:46] [музыка]
[00:58:48] то
[00:58:53] [музыка]
[00:58:55] мы выводим просто бас
[00:59:00] просто
[00:59:12] [музыка]
[00:59:19] у нас он уже не должен делиться
[00:59:24] на три но при этом
[00:59:27] делится на 5
[00:59:51] просто здесь можно написать
[01:00:04] [музыка]
[01:00:10] сейчас я пытаюсь просто вспомнить
[01:00:18] Мне просто кажется надо задать я сейчас
[01:00:21] думал о том что если я сейчас выведу как
[01:00:24] бы els чтобы напишу Принт физбасс то он
[01:00:30] во всех случаях кроме этих будет
[01:00:32] выводить Принт это будет неверно Тогда
[01:00:35] здесь нужно
[01:00:37] сделать или
[01:01:11] единственное я
[01:01:12] [музыка]
[01:01:13] с этим моментом
[01:01:16] немного сомневаюсь Правильно ли выставил
[01:01:19] обозначение что
[01:01:22] принимаемые у нас тип аргумента должен
[01:01:25] быть винтовый
[01:01:31] запустил
[01:01:46] [музыка]
[01:01:56] не совсем так я ожидал
[01:02:08] случайно поставил троечку вместо
[01:02:12] ожидаемое поведение теперь
[01:02:17] Но я же сказал что нужно вывести число
[01:02:20] от 1 до n а оно выводит только одну
[01:02:23] строчку А так я прошу прощения Я когда
[01:02:29] писал
[01:02:30] сконцентрироваться на этих так еще раз
[01:02:33] если
[01:02:34] делится на три без остатка то получается
[01:02:38] мы выводим физ и и плюс числа Повтори
[01:02:45] пожалуйста задание мы вводим числа от 1
[01:02:49] до n если число делится на 3 выводим
[01:02:53] вместо числа
[01:03:00] при вот в данном примере которые сделал
[01:03:04] при числе 15 у нас должно было вывести
[01:03:09] [музыка]
[01:03:11] один два если тройка то это должно
[01:03:15] вывести
[01:03:15] [музыка]
[01:03:17] физ потом
[01:03:19] 45-65
[01:03:24] [музыка]
[01:03:26] здесь тогда это нужно
[01:03:29] делать в цикле получается
[01:03:32] мы будем продвигаться от 0 до
[01:03:37] а N у нас кстати мы включительно или не
[01:03:40] включительно мы
[01:03:42] от одного до
[01:03:45] нет то есть мы если 15 Значит надо от 1
[01:03:48] до плюс 1
[01:03:53] Ну просто если мы делаем цикл
[01:03:57] Все я понял in Range нужно от единицы до
[01:04:03] n + 1 правильно таком случае где
[01:04:08] но если мы хотим 15 включить в наш
[01:04:11] диапазон
[01:04:20] дальше
[01:04:23] мы выводим на каждом мы проверяем сейчас
[01:04:48] тогда получается может быть нам здесь
[01:04:51] просто нужно выводить и
[01:05:05] нам а нам нужно вывести именно
[01:05:07] последовательность все от одного по
[01:05:10] полностью То есть у нас тогда здесь у
[01:05:13] нас Нам нужно поменять и
[01:05:17] нужно поменять и
[01:05:22] правильно но проблема будет в том
[01:05:25] насколько я помню что
[01:05:28] у нас цикл прервется когда одно из этих
[01:05:33] действий выполнится насколько я помню
[01:05:50] [музыка]
[01:05:54] Салам выглядит правильно
[01:05:57] на самом деле у этой задачи есть
[01:06:01] несколько
[01:06:03] еще шагов которые мы уже не успеваем
[01:06:08] которые уже не успеваем перейти но того
[01:06:12] что написал уже достаточно чтобы
[01:06:13] некоторых связь сдать да будем уже
[01:06:18] продвигаться к завершению целом прошел
[01:06:22] интервью довольно хорошо
[01:06:24] довольно уверенно были до моменты
[01:06:32] но в целом хорошо рассказал про модели
[01:06:36] про сдача певца
[01:06:38] про тепло тоже можно больше
[01:06:46] деталей
[01:06:49] прошивки Да не запутался можно сказать
[01:06:51] поймал меня на
[01:06:54] руках больше единицы
[01:06:59] Но вот в коде Да к сожалению
[01:07:02] [музыка]
[01:07:04] есть куда расти есть еще много задач
[01:07:09] нерешенных видов стимуляторе
[01:07:11] например да вот вначале стайпингом
[01:07:14] запутался но хорошо что вообще про него
[01:07:16] знаешь и исправился правильно а
[01:07:20] Пеппа 8 не соблюдаешь отступала два
[01:07:23] вместо четырех Да можно говорить что там
[01:07:27] вот в голове по дефолту 2 Но
[01:07:30] если у тебя был бы вот именно
[01:07:35] работа руками
[01:07:37] большой опыт
[01:07:42] вопреки или там поменял в настройках
[01:07:44] делал чтобы
[01:07:47] просто было все это потом пробелы
[01:07:51] некоторые тоже
[01:07:53] там с операторами
[01:08:01] то есть тоже
[01:08:03] хорошо
[01:08:10] Блэком чтобы обычно Просто извини что
[01:08:14] перебиваю я просто обычно грязно сначала
[01:08:16] пишу а потом уже почищаю да
[01:08:20] грязно нужно писать В смысле именно
[01:08:23] имплементации то есть алгоритмическая то
[01:08:25] есть то что ты начал просто первое что в
[01:08:27] голову пришло именно в лоб решить это
[01:08:30] типа вообще хорошо и нормально но
[01:08:33] например если мы будем именно
[01:08:36] анализировать алгоритмически то вот у
[01:08:39] тебя
[01:08:40] 35 я их в условии назвал по одному разу
[01:08:45] А здесь они в коде хардкорно написаны
[01:08:49] значит если я поменяю какое-то одно
[01:08:51] условие нужно будет менять код в трех
[01:08:54] разных местах что не хорошо что не
[01:08:57] делает код гибким и адаптивным к
[01:09:00] меняющимся
[01:09:01] бизнес-требованием например
[01:09:03] могу слово поменять место физ поставить
[01:09:06] там фуз и тоже нужно в двух местах
[01:09:09] менять Хотя одно условие по тоже
[01:09:11] какие-то такие вот моменты можно делать
[01:09:14] гибче оптимальнее сразу думать наперед
[01:09:17] То есть как вообще
[01:09:19] делать так чтобы твой код можно было
[01:09:22] легко и просто там модифицировать
[01:09:27] изменять а не переписывать с нуля там
[01:09:30] под новую без логику нужно закладывать
[01:09:33] такие элементы Ну и то что пишет что же
[01:09:36] видно типа не бегала тоже нужно работать
[01:09:40] и Ну это просто практикой нарабатывается
[01:09:47] может получить У нас знаешь
[01:09:52] стиль поэтому тоже этому ты скажи
[01:09:56] пожалуйста
[01:09:57] не бегает Что значит это не вслепую
[01:10:01] смысле
[01:10:04] что ты очень быстро пишешь не
[01:10:07] задумываешься вообще типа как там Какой
[01:10:10] оператор называется второй этаппинг
[01:10:11] называется и у тебя уже в голове Как
[01:10:14] таблица умножения все это все эти
[01:10:17] возможности
[01:10:18] просто скорость написания по сути Ну я
[01:10:23] знаю что мне нужно еще расти в именно в
[01:10:27] питоне Я знаю свои проблемы
[01:10:30] Да как вот некоторые говорят
[01:10:32] Hard skills или
[01:10:36] в профессии поэтому на самом деле ты
[01:10:40] довольно хорошо прошел довольно уверенно
[01:10:42] как и сказал То есть в плане теории
[01:10:46] довольно
[01:10:48] хороший уровень
[01:10:52] Я советую Вадима
[01:10:56] пару недель пару месяцев симулятора
[01:10:59] будет просто боец
[01:11:01] куда Что нового Ты узнал
[01:11:07] ради этого мог интервью сам
[01:11:11] самое
[01:11:13] интересное что я запомнил это про
[01:11:18] бустинги и про уверенность их
[01:11:21] предсказание нового какого-то значения
[01:11:26] Потому что я в симуляторе этого не нашел
[01:11:30] не дошел до тут еще и
[01:11:35] интересная очень Такой тонкий момент
[01:11:37] может быть ты чего-то там боялся перед
[01:11:39] собеседованием А тут оказалось не так
[01:11:42] страшно дом местами даже пострашнее в
[01:11:45] принципе
[01:11:47] я всегда волнуюсь
[01:11:49] [музыка]
[01:11:53] Да и поэтому мне что-то сейчас вспомнить
[01:11:56] из того что мы с тобой поговорили это
[01:11:58] будет сложно потому что эмоции такие
[01:12:01] являются
[01:12:05] сложно мне сложно проходил непроходимым
[01:12:08] чтобы ты посоветовал другим кандидатом
[01:12:11] который может быть не вызвались
[01:12:13] попробовать принципе все возможно вопрос
[01:12:17] приложимости усилий и времени
[01:12:19] [музыка]
[01:12:22] Я бы все равно бы рекомендовал бы вот
[01:12:25] нашим ребятам попробовать обязательно
[01:12:26] потому что это во-первых практический
[01:12:28] опыт во вторых все равно
[01:12:31] повторяю участь вы
[01:12:34] знания все равно так скажем трамбуете в
[01:12:39] своей голове То есть это дополнительная
[01:12:41] такая практика и тренировка вот Ну и
[01:12:44] наверное самое
[01:12:46] важное в обучении это системность и
[01:12:50] отдых наверное Вот это
[01:12:53] правильно расставить
[01:12:56] обучение графика обучения отдыха Вот это
[01:12:59] залог долгосрочный такой цели достижения
[01:13:04] цели
[01:13:06] спасибо
[01:13:09] на этом тогда Спасибо большое
[01:13:15] [музыка]
[01:13:17] интересное полезно
[01:13:19] Желаю дальнейших
[01:13:22] успехов решения задач прохождения
[01:13:24] реальных собеседований Спасибо Спасибо

FEEDBACK_MD:
---
section: "Обратная связь по бутстрапу"
start: "00:15:26"
end: "00:16:52"
start_seconds: 926
end_seconds: 1012
---

тогда дам обратную страху все правильно кроме вот то что ты не уточнил размер выборки правильно брать столько же сколько данных выборки у нас повторениями то есть какой-то элемент будет там два раза три какой-то ноль раз но каждый раз тоже размер потому что иначе мы смещенную какую-то метрику будем оценивать а нет уже которая нас интересует Я может уточнить Правильно ли я понял что вот мы берем всю выборку но Допустим мы берем условно 10 процентов мы из него выкидываем И эти 10 процентов замещаем повторами вот взятой выбор не так мы берем выборку 1000 элементов мы сэмплим по тысяче элементов Но это вот Случайный из тысячи То есть какой-то когда мы так случайно сэмплим несколько раз какой-то ноль раз там и так далее и каждый раз немножко будет перекос свою сторону и мы таким образом расшатываем нашу метрику получаем некоторую такую оценку потому что у нас выборка которую мы имеем это просто лучше самое большее что мы знаем о генеральной совокупности и мы по сути воспроизводим как бы мы сэмплились совокупности

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
Target version for this run: v2 only.
Write JSON only to: splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. ml-engineer-junior-karpov-2023-03-09.v1.qa-split.json, v2, ... except the target path above).
- Reuse items[] or field text from older splitter runs because validation passed before.

REQUIRED on step 2:
- Extract Q&A solely from PRIMARY_TRANSCRIPT in this LLM_INPUT_STEP_2 block.
- Do NOT read video.md or YouTube chapter titles (validation-only; absent in real interviews).
- Full fresh extraction; overwrite the target JSON completely.
- interviewer_feedback: interviewer speech only; candidate continuation -> candidate_answer or null feedback.
- Truncated interviewer ASR: merge adjacent interviewer lines in the transcript; do not paraphrase from external outlines.


======================================================================
OUTPUT PATHS (post-processing)
======================================================================
Save JSON to: splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.json \
    --video transcripts/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.json --out splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.qa-split.json \
    --video transcripts/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.validation-report.md

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
Language for notes: Russian. Keep notes short and actionable. Leave notes as "" when both flags are true.

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
video.md: /Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/video.md

--- CHAPTER `00:02:55` — Uplift-моделирование ---
window: 00:02:55 .. 00:05:50
recognition_status: single (1 items)

ITEM #1
  interviewer_question: time=00:02:55 text='я у тебя в резюме видел пролив моделирование через трансформацию классов. а расскажи вообще что за такая задача отлив моделирования и что за классы там трансформируются'
  candidate_answer: time=00:02:59 text='через трансформацию классов да было такое Это было как тестовое задание на кегли там мы сколько там месяцев соревновались Вот и на самом деле я скажем так не вошел в топ но для меня это был хороший урок потому что я с агрегировал скажем так все знания которые были получены во время курса Старт тоннель в таком в практическом русле уже и у меня так они устаканились и было понятно уже как что нужно какие-то нужно делать для того чтобы модельку построить обучаешь сразу знания задача полив моделирования состоит в том чтобы предсказать кому из клиентов Да допустим направить как на кого из клиентов по воздействовать для того чтобы они совершили дополнительную продажу то есть лифт Это разница между теми клиентами кому направится какой-то воздействие я не купят и если этого не совершить вот разница это вот как раз таки Apple вот трансформации Клиент купил и так и так трансформация классов Да они учитываются то есть у нас вот из этой матрички там четыре варианта мы классу один присвоему те кто у нас не купит если мы не отправим СМСку и те кто купит если мы отправим им и они не купят не надо на них тратить деньги наоборот Наоборот 11 это кто у нас купит и так мы на них деньги не тратим А на тех кто если мы не отправим не купят на них тратим деньги хорошо получается В какой'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:04:20 text='вот трансформации Клиент купил и так и так трансформация классов Да они учитываются то есть у нас вот из этой матрички там четыре варианта мы классу один присвоему те кто у нас не купит если мы не отправим СМСку и те кто купит если мы отправим им и они не купят не надо на них тратить деньги наоборот Наоборот 11 это кто у нас купит и так мы на них деньги не тратим А на тех кто если мы не отправим не купят на них тратим деньги хорошо получается В какой'
  question_topic: ML

--- CHAPTER `00:05:50` — Модель оттока ---
window: 00:05:50 .. 00:08:06
recognition_status: single (1 items)

ITEM #2
  interviewer_question: time=00:05:50 text='допустим представим ситуацию к нам приходит маркетологи говорят хотим модель тока для чего это халтурка на недельку справишься что какие твои действия'
  candidate_answer: time=00:06:14 text='Ну во-первых я подойду к маркетологам там или позвоню им Да там и спрошу для чего им нужна модель оттока что они в итоге хотят получить Ну то есть на что повоздействовать там да там то есть понять хотя бы что мы будем там оптимизировать Да там или на что мы будем влиять от этого подобрать уже какую-то свою метрику для задачи вообще как вот относится задача моделирования и прогноза тока Я помню смотрел видео Валерия Бабушкина я забыл по-моему я помню что Валерий говорит модели только она не нужна две задачи с помощью модели оттока по моему также пытаются найти тех людей на которых нужно по воздействию для того чтобы они остались в облифте Мы также воздействуем людей но только чтобы они купили то есть в этом и в этом случае мы пытаемся дозаработать скажем так на своей аудитории Ладно меня решаем задачу тока получили некоторую на выходе вероятность что пользователь течет как бы мы учитывая то что исходная задача Ну как бы было только не было бинарное как мы вот имея вероятности можем обработать выходы модели чтобы что-то Дальше сами делать принимать решение Я думаю что можно установить какой-нибудь trashold отсечку по которой мы будем говорить что человек скорее всего уйдет допустим это может быть там 50 процентов да там уверенность 0,5 так далее И только по достижению этой отсечки воздействия этих пользователей которые превышает ее Какие'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:06:39 text='вообще как вот относится задача моделирования и прогноза тока Я помню смотрел видео Валерия Бабушкина я забыл по-моему я помню что Валерий говорит модели только она не нужна две задачи с помощью модели оттока по моему также пытаются найти тех людей на которых нужно по воздействию для того чтобы они остались в облифте Мы также воздействуем людей но только чтобы они купили то есть в этом и в этом случае мы пытаемся дозаработать скажем так на своей аудитории Ладно меня решаем задачу тока получили некоторую на выходе вероятность что пользователь течет как бы мы учитывая то что исходная задача Ну как бы было только не было бинарное как мы вот имея вероятности можем обработать выходы модели чтобы что-то Дальше сами делать принимать решение Я думаю что можно установить какой-нибудь trashold отсечку по которой мы будем говорить что человек скорее всего уйдет допустим это может быть там 50 процентов да там уверенность 0,5 так далее И только по достижению этой отсечки воздействия этих пользователей которые превышает ее Какие'
  question_topic: ML

--- CHAPTER `00:08:06` — Метрики для дисбаланса классов ---
window: 00:08:06 .. 00:11:32
recognition_status: single (1 items)

ITEM #3
  interviewer_question: time=00:08:06 text='Какие метрики обычно используются оттекают понятно дело не ровно половина пользова здесь есть дисбаланс классов Какие метрики ты знаешь для дисбаланса классов'
  candidate_answer: time=00:08:22 text='дисбаланса классов Я думаю здесь может подойти Взвешенный F1 мира и может подойти Rock PR это когда там precision recal расскажи подробнее Вот как можно подбирать отсечку для Ну вот пиар состоит у нас с каких метрик precision recola мы получили вероятность оттока или какой-то скоро тока и мы хотим перейти к названным метрикам классификации вот как мы можем отсечку здесь подбирать За что каждый Метрика отвечает из этих двух и какая между ними вообще закономерность я начну чуть-чуть шага назад что у нас когда когда мы используем классификацию то у нас появляется так называемая Матрица ошибок когда у нас есть значение таргета и значение непосредственной модели То которое нам предсказывает и Матрица ошибок у нас по диагонали если мы берем то это у нас правильно предсказанный положительный класс правильно предсказанный отрицательный класс и по другой диагонали Это неправильно сказано положительно неправильно предсказанный отрицательный соответственно у нас прессижен это так называемая точность предсказание То есть это отношение Используйте то есть правильно предсказанных положительного класса на сумму Позитив плюс Представьте менеджер который не проходил Старт Мэри симулятор не знаю ничего ты мне объясняешь что вообще точность это у нас что мы предсказали положительный класс и как можно меньше в этом ошиблись А recola это полнота это что мы как можно больше объектов положительного класса предсказали можно покрыли свои модели покрыли свои модели престижение нам важно чтобы мы не ошибились на первом классе положительных срабатываний а приколе Ну то есть мы например можем взять просто топ-5 но они Точно Вот все относятся к нашему нас классу а приколе Главное чтобы покрытие было больше А там если мы какие-то лишнее задеваем это уже не так и соответственно возвращаясь к рок PR кривой Это получается что мы по различным вот этим трешолдам замеряем присяжные рекол и строим их на графике и соответственно Метрика PR ой Rock PR это будет площадь вот под кривой Допустим мы приходим К менеджеру говорим'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:08:33 text='расскажи подробнее Вот как можно подбирать отсечку для Ну вот пиар состоит у нас с каких метрик precision recola мы получили вероятность оттока или какой-то скоро тока и мы хотим перейти к названным метрикам классификации вот как мы можем отсечку здесь подбирать За что каждый Метрика отвечает из этих двух и какая между ними вообще закономерность я начну чуть-чуть шага назад что у нас когда когда мы используем классификацию то у нас появляется так называемая Матрица ошибок когда у нас есть значение таргета и значение непосредственной модели То которое нам предсказывает и Матрица ошибок у нас по диагонали если мы берем то это у нас правильно предсказанный положительный класс правильно предсказанный отрицательный класс и по другой диагонали Это неправильно сказано положительно неправильно предсказанный отрицательный соответственно у нас прессижен это так называемая точность предсказание То есть это отношение Используйте то есть правильно предсказанных положительного класса на сумму Позитив плюс Представьте менеджер который не проходил Старт Мэри симулятор не знаю ничего ты мне объясняешь что вообще точность это у нас что мы предсказали положительный класс и как можно меньше в этом ошиблись А recola это полнота это что мы как можно больше объектов положительного класса предсказали можно покрыли свои модели покрыли свои модели престижение нам важно чтобы мы не ошибились на первом классе положительных срабатываний а приколе Ну то есть мы например можем взять просто топ-5 но они Точно Вот все относятся к нашему нас классу а приколе Главное чтобы покрытие было больше А там если мы какие-то лишнее задеваем это уже не так и соответственно возвращаясь к рок PR кривой Это получается что мы по различным вот этим трешолдам замеряем присяжные рекол и строим их на графике и соответственно Метрика PR ой Rock PR это будет площадь вот под кривой'
  question_topic: Statistics

--- CHAPTER `00:11:32` — Расчёт доверительного интервала площади под PR кривой ---
window: 00:11:32 .. 00:12:35
recognition_status: single (1 items)

ITEM #4
  interviewer_question: time=00:11:32 text='Допустим мы приходим К менеджеру говорим вот у нас площадь подберет кривой 1.9 такой четкое значение Он спрашивает А как мы можем Ну вот быть уверенным что завтра не будет там один из темы после завтра там два и два Вот как можно какое-то оценить диапазон в котором болтается'
  candidate_answer: time=00:11:56 text='во-первых я могу конечно ошибаться но по-моему больше единицы не может быть не попался хорошо второе мы можем построить доверительный интервал э для изучения Рог но он у нас допустим же есть выборка на которой мы обучались и мы можем с помощью бутстропа повытаскивать и проитрироваться Да там несколько там тысяч раз и за счет этого построить доверительный интервал метро'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:12:00 text='больше единицы не может быть не попался хорошо второе мы можем построить доверительный интервал э для изучения Рог но он у нас допустим же есть выборка на которой мы обучались и мы можем с помощью бутстропа повытаскивать и проитрироваться Да там несколько там тысяч раз и за счет этого построить доверительный интервал метро'
  question_topic: Statistics

--- CHAPTER `00:12:35` — Принцип работы бутстрапа ---
window: 00:12:35 .. 00:15:26
recognition_status: single (1 items)

ITEM #5
  interviewer_question: time=00:12:35 text='расскажи вообще как работает'
  candidate_answer: time=00:12:39 text='у нас допустим есть выборка она пришла к нам из генеральной совокупности Мы про которую мы ничего не знаем И у нас есть только вот эта выборка мы можем вытаскивать часть значений из доступных выборки считать необходимые по ней там статистики и возвращать обратно значение сколько значение вытаскивает Можно Все можно все значений я вот этот момент не готов Я помню там есть нюанс какой-то но я себе в пометках ставил что я бы брал чуть меньше значение по количеству выборки Ну то есть чуть меньше чем основная выборка много раз дальше и мы получаем мы делаем с помощью быстро по вычисляем вычисляем какую-то статистику заносим ее естественно куда-нибудь там сохраняем Вот это количество раз и мы статистика на нас озвучена задача интересует рок пиар Ну то есть мы достаем выборку обучаем на ней модель замеряем на нейрок пиар сохраняем результат Так мы повторяем повторяем мы еще раз обучаем модель делаем предсказание сказание на неё одна модель но мы несколько раз потому что тогда получается 10 тысяч раз обучать модель да и это уже получится по моему возможно так вот мы достаем с помощью мы делаем предсказание модели замеряем рок PR и сохраняем его так мы повторяем много-много раз и получаем какой-то распределение нашей пиар значение и по о данной выборки мы уже можем вычислить доверительный интервал То есть если заданной точности То есть если мы берем там 95 процентов доверительный интервал то получается что нам нужно понтилям то есть по два с половиной 97,5 контилия взять интервал и в нем будет находиться наша значение пиар кривой Да хорошо сразу'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:13:08 text='значений я вот этот момент не готов Я помню там есть нюанс какой-то но я себе в пометках ставил что я бы брал чуть меньше значение по количеству выборки Ну то есть чуть меньше чем основная выборка много раз дальше и мы получаем мы делаем с помощью быстро по вычисляем вычисляем какую-то статистику заносим ее естественно куда-нибудь там сохраняем Вот это количество раз и мы статистика на нас озвучена задача интересует рок пиар Ну то есть мы достаем выборку обучаем на ней модель замеряем на нейрок пиар сохраняем результат Так мы повторяем повторяем мы еще раз обучаем модель делаем предсказание сказание на неё одна модель но мы несколько раз потому что тогда получается 10 тысяч раз обучать модель да и это уже получится по моему возможно так вот мы достаем с помощью мы делаем предсказание модели замеряем рок PR и сохраняем его так мы повторяем много-много раз и получаем какой-то распределение нашей пиар значение и по о данной выборки мы уже можем вычислить доверительный интервал То есть если заданной точности То есть если мы берем там 95 процентов доверительный интервал то получается что нам нужно понтилям то есть по два с половиной 97,5 контилия взять интервал и в нем будет находиться наша значение пиар кривой Да хорошо сразу'
  question_topic: Statistics

--- CHAPTER `00:16:52` — Оценка метрики, если нет возможности брать выборки, но есть обученные модели и их оценки ---
window: 00:16:52 .. 00:19:00
recognition_status: single (1 items)

ITEM #6
  interviewer_question: time=00:16:52 text='такой вопрос Если у нас нет возможности сэмплить тысячи раз у нас есть например посчитаны есть 5 моделей 5 фолдов'
  candidate_answer: time=00:17:12 text='могу предположить что можно их сравнить с помощью кроссволидации замерить их качество но этих моделей если вам просто усредним опять получим просто одну оценку нам нужно выбрать из пяти моделей одну лучше одна модель обычно 5 раз на разных и у нас на 5 разных болтах есть оценки наши метрики дал ответ то что кросс валидация такой игрушечные маленьких размерах но тоже за счет того что у нас разные холды мы получаем распределение и учитывая то что Ну в принципе на метрике в каком-то виде метрики усреднения в силу известная теорема которую ты мне поможешь назвать симметрики Да что-то там усредняют Поэтому даже у такого маленького сэмплов будет асимптотически все сходиться к тому что у нас нормальных людей все можно оценивать я если правильно понял ты говоришь про Центральный предельную теорему собеседование Мне нужно воспроизвести Дания Я верю а'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:17:43 text='дал ответ то что кросс валидация такой игрушечные маленьких размерах но тоже за счет того что у нас разные холды мы получаем распределение и учитывая то что Ну в принципе на метрике в каком-то виде метрики усреднения в силу известная теорема которую ты мне поможешь назвать симметрики Да что-то там усредняют Поэтому даже у такого маленького сэмплов будет асимптотически все сходиться к тому что у нас нормальных людей все можно оценивать я если правильно понял ты говоришь про Центральный предельную теорему собеседование'
  question_topic: Statistics

--- CHAPTER `00:19:00` — Схемы кросс-валидации ---
window: 00:19:00 .. 00:20:55
recognition_status: single (1 items)

ITEM #7
  interviewer_question: time=00:19:00 text='возможно ты знаешь такой Адванс Вопрос какие бывают схемы распорядации'
  candidate_answer: time=00:19:23 text='воспользоваться просто методом отложенной выборки самый простой тестовый кино Да там и на нем замерять качество Когда же мы используем непосредственно кросс фалидацию у нас Я знаю три варианта проведения кросс валидации обычно дефолт когда мы разбиваем на какое-то количество солтов равных и по очереди это все модель обучается на минус одном фалде и замеряется качественном хобби Это хороший вариант Когда у нас нет временной зависимости в данных Когда у нас есть временная зависимость это у нас уже там Сири Сплит идёт мы в ней у нас нет временной зависимости у нас keefold и мы хотим определить сколько насколько Fall of Beats вот как мы принимаем решение на количество холодов насколько я помню когда вот как раз таки Я учился что есть такой момент что в идеале конечно чтобы количество фолдов равнялось количество элементов у нас наши выборки вот и это самый лучший вариант но он естественно очень для чего для точной оценки потому что интересует неточная оценка мы сравниваем несколько моделей точность оценки Как по-другому'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:19:25 text='отложенной выборки самый простой тестовый кино Да там и на нем замерять качество Когда же мы используем непосредственно кросс фалидацию у нас Я знаю три варианта проведения кросс валидации обычно дефолт когда мы разбиваем на какое-то количество солтов равных и по очереди это все модель обучается на минус одном фалде и замеряется качественном хобби Это хороший вариант Когда у нас нет временной зависимости в данных Когда у нас есть временная зависимость это у нас уже там Сири Сплит идёт мы в ней у нас нет временной зависимости у нас keefold и мы хотим определить сколько насколько Fall of Beats вот как мы принимаем решение на количество холодов насколько я помню когда вот как раз таки Я учился что есть такой момент что в идеале конечно чтобы количество фолдов равнялось количество элементов у нас наши выборки вот и это самый лучший вариант но он естественно очень для чего для точной оценки потому что интересует неточная оценка мы сравниваем несколько моделей'
  question_topic: ML

--- CHAPTER `00:20:55` — Влияние смещения и разброса на качество модели ---
window: 00:20:55 .. 00:22:43
recognition_status: single (1 items)

ITEM #8
  interviewer_question: time=00:20:55 text='точность оценки Как по-другому называется Я возможно путаю конечно возможно а бас Да А какой еще есть свойство разброса'
  candidate_answer: time=00:21:05 text='а бас Да А какой еще есть свойство разброса между ними как раз таки проблема вот например если мы хотим замерить финальное качество модели нас интересует схема валидации с меньшей с меньшим смещением или с меньшим разбросом когда мы сравниваем модели между собой Да мы хотим финальное качество модели посчитать тогда я думаю что это должно быть все-таки смещение у нас важно потому что нам важно как можно ближе оценивать наш параметр метрику довольно похожие модели Вот мы что-то там поменяли добавили набор новых вещей или там оптимизировали параметры и хотим сравнить и у них точность точнее смещение примерно одинаковое правильно Вот Но в таком случае нам нужно обращать внимание на разброс потому что Чем выше разброс тем у нас дальше могут улетать значения от истинного но здесь не про значение от истинного чем больше у нас разброс тем менее чувствительная схема валидации и мы если сравниваем две модели одно лучше другой Она может быть просто в рамках их погрешности и мы на самом деле принимаем решение можно сказать по кофейной гуще а не на каком-то значимым уровне кстати про распределение'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:21:16 text='например если мы хотим замерить финальное качество модели нас интересует схема валидации с меньшей с меньшим смещением или с меньшим разбросом когда мы сравниваем модели между собой Да мы хотим финальное качество модели посчитать тогда я думаю что это должно быть все-таки смещение у нас важно потому что нам важно как можно ближе оценивать наш параметр метрику довольно похожие модели Вот мы что-то там поменяли добавили набор новых вещей или там оптимизировали параметры и хотим сравнить и у них точность точнее смещение примерно одинаковое правильно Вот Но в таком случае нам нужно обращать внимание на разброс потому что Чем выше разброс тем у нас дальше могут улетать значения от истинного но здесь не про значение от истинного чем больше у нас разброс тем менее чувствительная схема валидации и мы если сравниваем две модели одно лучше другой Она может быть просто в рамках их погрешности и мы на самом деле принимаем решение можно сказать по кофейной гуще а не на каком-то значимым уровне кстати про распределение'
  question_topic: ML

--- CHAPTER `00:22:43` — Основные компоненты A/B теста ---
window: 00:22:43 .. 00:25:42
recognition_status: single (1 items)

ITEM #9
  interviewer_question: time=00:22:43 text='Расскажи Из каких основных компонентов состоит аб-тест Я помню в резюме было как раз ты соболезненно освоился'
  candidate_answer: time=00:23:28 text='значит в первую очередь мы выбираем метрику по которой мы будем делать выводы что у нас есть различия либо нет различий далее мы дизайнер уже сам эксперимент Мы сначала устанавливаем выбираем ошибку первого рода Но это ложноположительная ошибка это с частотой с которой мы будем фиксировать изменения тогда когда на самом деле этого изменения нет также после того как мы установили уровень значимости Да он обычно опять берет 05 берется мы устанавливаем ошибку второго рода это ложная отрицательное это тогда когда мы говорим что нулевая гипотеза верна тогда когда на самом деле есть изменения группа А и Б обе ошибки играют роль Но ты все верно говоришь просто хочу чтобы ты приземлил это теперь на Вот именно на метрике по группам можно положительная ошибка то есть ошибка первого рода это мы говорим что у нас новый алгоритм лучше хотя на самом деле он не лучше ошибка второго рода наоборот мы говорим что старые лучше не изменился когда на самом деле второй оказался лучше так лучше или не изменился мы не замечаем что наш новый алгоритм он на самом деле лучший и принимаем Что старые все-таки лучше чем новый То есть это ошибка второго рода когда фактически Ну там Ну опять ты сказала что лучше на самом деле что со значимой разница между ними Нет хорошо потому что например можем заметить в том числе со значимую разницу и она будет Ну когда например второй алгоритм хуже и он тоже будет со значимая отличаться и мы поймаем это или не понимаем например Расскажи что такое пивалью'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:24:23 text='группа А и Б обе ошибки играют роль Но ты все верно говоришь просто хочу чтобы ты приземлил это теперь на Вот именно на метрике по группам можно положительная ошибка то есть ошибка первого рода это мы говорим что у нас новый алгоритм лучше хотя на самом деле он не лучше ошибка второго рода наоборот мы говорим что старые лучше не изменился когда на самом деле второй оказался лучше так лучше или не изменился мы не замечаем что наш новый алгоритм он на самом деле лучший и принимаем Что старые все-таки лучше чем новый То есть это ошибка второго рода когда фактически Ну там Ну опять ты сказала что лучше на самом деле что со значимой разница между ними Нет хорошо потому что например можем заметить в том числе со значимую разницу и она будет Ну когда например второй алгоритм хуже и он тоже будет со значимая отличаться и мы поймаем это или не понимаем'
  question_topic: Experimentation

--- CHAPTER `00:25:42` — P-value и гипотезы ---
window: 00:25:42 .. 00:27:27
recognition_status: single (1 items)

ITEM #10
  interviewer_question: time=00:25:42 text='например Расскажи что такое пивалью нулевая гипотеза вот эти все вещи'
  candidate_answer: time=00:25:48 text='это у нас вероятность встретить такой же или более экстремально отклонение в данных про гипотезы это мы проверяем допустим какие-то если у нас различия в алгоритмах или нет И у нас нулевая гипотеза это то что у нас различий алгоритмах нет альтернативный гипотеза что есть и вот когда мы провели эксперименты замеряем метрики и сравниваем их между собой и высчитываем пиво или так называемый который нам говорит о том что вот ту разницу которая мы видим между двумя алгоритмами с какой вероятностью мы можем встретить такую же или более еще значимую разницу более экстремальная более сильная и вот если она меньше чем наш заданный уровень ошибки первого рода то тогда можем сказать что у нас есть основания на то чтобы Отклонить в любой гипотезу и принять альтернативную почти все верно но можно еще более наговорить ты говоришь про разницу заметить разницу такой экстремальную на самом деле есть у любой статистики у любого теста не обязательно на разницу средних можно что Мы заметили такое значение статистики или более экстремальное Да ну тут просто мне в терминах разницы проще воспринимать А как мы в тесте'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:26:50 text='альтернативную почти все верно но можно еще более наговорить ты говоришь про разницу заметить разницу такой экстремальную на самом деле есть у любой статистики у любого теста не обязательно на разницу средних можно что Мы заметили такое значение статистики или более экстремальное Да ну тут просто мне в терминах разницы'
  question_topic: Experimentation

--- CHAPTER `00:27:27` — Необходимое количество данных ---
window: 00:27:27 .. 00:29:31
recognition_status: single (1 items)

ITEM #11
  interviewer_question: time=00:27:27 text='А как мы в тесте определяем сколько нам данных нужно и какую разницу можем задать'
  candidate_answer: time=00:27:37 text='помню Мы это можем проверить с помощью а-теста не проверить посчитать посчитать посчитать с помощью теста это такой тест Когда у нас есть две одинаковые выборки и мы по ним итеративно считаем статистики И сравниваем между собой ты сейчас говоришь про симуляцию я говорил про Как мы можем посчитать по-моему если у нас есть если мы знаем что наши данные пришли из нормального распределения тогда мы можем использовать формулу наверное сейчас я не воспроизведу но с помощью нее можно вычислить и минимально значимый размер выборки средний дисперсия нас интересует Если мы если мы считаем минимальный значимый эффект размер выборки если размер выборки мы считаем то у нас должен присутствовать еще мы договорились Сегодня могу догадаться что Ошибка первого рода и второго рода Но на самом деле Да есть такая формула и она не только есть для нормального распределения есть также там для других феноменов и так далее а то что ты говоришь про интерактивно проведем тест это уже про действительно можно оценивать если мы не хотим искать формулу через симуляции Но обычно через них в конце уже проверяют действительно мы все правильно посчитали и выдерживаем заявленные уровни ошибок первого рода Расскажи'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:28:02 text='я говорил про Как мы можем посчитать по-моему если у нас есть если мы знаем что наши данные пришли из нормального распределения тогда мы можем использовать формулу наверное сейчас я не воспроизведу но с помощью нее можно вычислить и минимально значимый размер выборки средний дисперсия нас интересует Если мы если мы считаем минимальный значимый эффект размер выборки если размер выборки мы считаем то у нас должен присутствовать еще мы договорились Сегодня могу догадаться что Ошибка первого рода и второго рода Но на самом деле Да есть такая формула и она не только есть для нормального распределения есть также там для других феноменов и так далее а то что ты говоришь про интерактивно проведем тест это уже про действительно можно оценивать если мы не хотим искать формулу через симуляции Но обычно через них в конце уже проверяют действительно мы все правильно посчитали и выдерживаем заявленные уровни ошибок первого рода'
  question_topic: Experimentation

--- CHAPTER `00:29:31` — Проведение симуляций ---
window: 00:29:31 .. 00:32:40
recognition_status: single (1 items)

ITEM #12
  interviewer_question: time=00:29:31 text='Расскажи как проводится симуляции И как понять что все правильно все готово'
  candidate_answer: time=00:29:39 text='недавно начал что у нас есть две выборки они одинаковые Ну мы можем просто взять нашу выборку на исторических данных которые задают Только желательно чтобы на них по моему не было экспериментов чтобы не вызывать какие-то дополнительные шумы в данных берем одну выборку Да там между ними умножим на два мы считаем различаются ли между ними то есть мы считаем по ним статистики такого размера выборку Мы берем достаточно чтобы детектировать эффект различия между хорошо Мы только что брать сказали что мы по формуле посчитали размер минимальный размер необходимый выборки такого размера дальше вот мы взяли выборки считаем по ним статистики И с помощью статистического критериев проверяем Если разница между выборками или нет И у нас доля того что у нас есть различия в этих выборках не должна превышать тот уровень значимости который мы изначально перед экспериментом поставили как будет выглядеть распределение равномерно а как мы проверим теперь и какие мы здесь ошибки можем посчитать Ну вот мы посчитали здесь ошибку первого рода еще можно проверить ошибку второго рода мощность как это мы делаем Что такое мощность мощность это обратная величина обратной ошибки второго рода а нет мощность симуляциях будто проверяем мощность мы сделаем симуляцию берем две заведомо различающиеся выборки мы можем из одной выборки взять части возьмем к одной выборке прибавим тот минимальный значимый эффект который мы посчитали по формуле И тем самым у нас будет различие выборки и вот уже эти две выборки мы будем сравнивать на бтесте симуляционно и посмотрим детектируем ли мы с необходимую мощность нужно вероятностью и что мы там ожидаем и какое распределение в этот раз мы ожидаем здесь увидеть количество долек количество случаев когда мы детектируем различия должна быть столько же или больше чем мощность То есть это единица минус ошибка второе все правильно'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:31:12 text='здесь ошибки можем посчитать Ну вот мы посчитали здесь ошибку первого рода еще можно проверить ошибку второго рода мощность как это мы делаем Что такое мощность мощность это обратная величина обратной ошибки второго рода а нет мощность симуляциях будто проверяем мощность мы сделаем симуляцию берем две заведомо различающиеся выборки мы можем из одной выборки взять части возьмем к одной выборке прибавим тот минимальный значимый эффект который мы посчитали по формуле И тем самым у нас будет различие выборки и вот уже эти две выборки мы будем сравнивать на бтесте симуляционно и посмотрим детектируем ли мы с необходимую мощность нужно вероятностью и что мы там ожидаем и какое распределение в этот раз мы ожидаем здесь увидеть количество долек количество случаев когда мы детектируем различия должна быть столько же или больше чем мощность То есть это единица минус ошибка второе все правильно'
  question_topic: Experimentation

--- CHAPTER `00:32:40` — Градиентный бустинг ---
window: 00:32:40 .. 00:35:00
recognition_status: single (1 items)

ITEM #13
  interviewer_question: time=00:32:40 text='градиентный бустинг самая любимая тема как он работает Почему градиентный'
  candidate_answer: time=00:32:45 text='как он работает Почему градиентный градиентный Бусик это такой вид сомблирования моделей базовых Когда у нас ошибки предыдущей модели является таргетами для последующей и так далее и так далее и так далее это все считается Градиент здесь Потому что Мы берем производную считаем разницу между таргетом и предсказанием первой модели модель там допустим я берут самую простую которая там можно среднюю по всем таргетам поставили Вот и берут первый производную Да этого это получается что Градиент у нас Мы берем производную подставляем туда разницу между таргетом и отступа модели далее мы считаем коэффициент для второй модели для того чтобы минимизировать так скажем уже ошибку и дальше это поступает следующую модель и в следующую модель так и так далее Что за коэффициент пропустил Ну такой поправочный коэффициент скажем весовой для того чтобы не будешь с другой моделью бустинга в простом бустинге этого нету а в градиентным подбираются коэффициент что же такое Нет ты все верно говоришь что мы считаем Градиент ошибки и ты хорошо что потом сказал что Градиент ошибки они просто как-то вначале говорил и мы добавляем новую модель с фиксированным весом которые обозначаются как Learning Raid Это и так далее чтобы это если мы градиентом'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:33:32 text='которая там можно среднюю по всем таргетам поставили Вот и берут первый производную Да этого это получается что Градиент у нас Мы берем производную подставляем туда разницу между таргетом и отступа модели далее мы считаем коэффициент для второй модели для того чтобы минимизировать так скажем уже ошибку и дальше это поступает следующую модель и в следующую модель так и так далее Что за коэффициент пропустил Ну такой поправочный коэффициент скажем весовой для того чтобы не будешь с другой моделью бустинга в простом бустинге этого нету а в градиентным подбираются коэффициент что же такое Нет ты все верно говоришь что мы считаем Градиент ошибки и ты хорошо что потом сказал что Градиент ошибки они просто как-то вначале говорил и мы добавляем новую модель с фиксированным весом которые обозначаются как Learning Raid Это и так'
  question_topic: ML

--- CHAPTER `00:35:00` — Что произойдёт, если убрать первое дерево в градиентном бустинге ---
window: 00:35:00 .. 00:36:45
recognition_status: single (1 items)

ITEM #14
  interviewer_question: time=00:35:00 text='бустинге берем первое дерево Не совсем понял вопроса Что будет у нас есть ансамбль где суммируются какими-то весами деревья каждый из них нам на что-то свое обучается после предыдущего И что если мы убираем первое дерево из этого ансамбре'
  candidate_answer: time=00:35:05 text='понял вопроса Что будет у нас есть ансамбль где суммируются какими-то весами деревья каждый из них нам на что-то свое обучается после предыдущего И что если мы убираем первое дерево из этого ансамбре складываем все остальное если мы убираем первое дерево или выбираем убираем убираем первое дерево делаем предсказание смотрим на что-то там то есть это самый первый алгоритм по которому который делал предсказание потом отступы которого дальше уже практимировать правильно понимаю Не совсем ты верно сказал что мы берем средние по таргету первое приближение место базы модели А ну в этом случае если первое дерево будет то там оно сильно же переобучиться под данной нет мы же уже ничего не обучаем но хорошо Я тебя запутал Да как правильно сказала Мы сначала берем средние подарки то потом считаем градиенты потом строим первое дерево потом второе дерево на том что на границе от ошибки предсказания среднего первого дерева и так далее первое дерево оно дает довольно большой модель А уже если убираем последнее дерево оно уже и там шумы какие-то маленькие остаточки обучаются и она не сильно уровне метрику ну и соответственно что-то промежуточное средних там большой вес первой модели передается'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:35:15 text='обучается после предыдущего И что если мы убираем первое дерево из этого ансамбре складываем все остальное если мы убираем первое дерево или выбираем убираем убираем первое дерево делаем предсказание смотрим на что-то там то есть это самый первый алгоритм по которому который делал предсказание потом отступы которого дальше уже практимировать правильно понимаю Не совсем ты верно сказал что мы берем средние по таргету первое приближение место базы модели А ну в этом случае если первое дерево будет то там оно сильно же переобучиться под данной нет мы же уже ничего не обучаем но хорошо Я тебя запутал Да как правильно сказала Мы сначала берем средние подарки то потом считаем градиенты потом строим первое дерево потом второе дерево на том что на границе от ошибки предсказания среднего первого дерева и так далее первое дерево оно дает довольно большой модель А уже если убираем последнее дерево оно уже и там шумы какие-то маленькие остаточки обучаются и она не сильно уровне метрику ну и соответственно что-то промежуточное средних там большой вес первой модели передается'
  question_topic: ML

--- CHAPTER `00:36:45` — Различия в построении деревьев ---
window: 00:36:45 .. 00:40:10
recognition_status: single (1 items)

ITEM #15
  interviewer_question: time=00:36:45 text='такой вопрос Вот есть у нас с разными акции ВУЗ целая jbm капуст может быть знаешь как принцип построения дерева у них различается в двух словах'
  candidate_answer: time=00:36:50 text='ВУЗ целая jbm капуст может быть знаешь как принцип построения дерева у них различается в двух словах капуст это детище Яндекса его особенностью заключается в том что оно из коробки может категориальная фичи обрабатывать у их же Boost у него по-моему идет одно дерево там есть принципиальное различие Я знаю что их же буста у него помимо первой производной есть еще вторая производная когда давай вот именно про Дерево у Lite jbm он строится Ну то есть обрезается листы Ну то есть они только в одну сторону расширяется и он быстро быстрее работает ну то есть у него у нас есть только там один ответ это обрезанное дерево такое правильную сторону немножко округляешь некорректно в терминологии тоже некорректно Ты про правильно подумал Но то как Ты объясняешь Он работает Как же быть строятся дерево одно есть прям даже два слова я не вспомню нет но могу по предположить что это связано с глубиной и либо с размером с количеством листьев но можно сказать да в их же быть все мы как строим вот у нас есть разбиение в каком-то признаку мы получаем например две группы элементов дальше мы к не разбили на две каждый из этих групп мы дальше не двигаемся А в LG beami У нас вот разбили на две У нас две новые ноды потом мы среди всех выбираем какую разбить разбили это на 2 теперь выбираем из этих трех Может быть сейчас лучше разбить еще эту на две а может быть лучше Вот это разбить мы как бы всех одинаково принимаем и а это идет к тому что могут быть очень сильно асимметричные А их же будете они все ну вот сайте как зависит количество листьев от Глубины в их же пустеп Вайс деревьях они два в степени нас если глубина глубина 2 то у нас будет Два листа на 3 забьются еще будут 4 и так далее Вопросик Как можем тоже это что там много неуверенных своих моделях'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:38:07 text='тоже некорректно Ты про правильно подумал Но то как Ты объясняешь Он работает Как же быть строятся дерево одно есть прям даже два слова я не вспомню нет но могу по предположить что это связано с глубиной и либо с размером с количеством листьев но можно сказать да в их же быть все мы как строим вот у нас есть разбиение в каком-то признаку мы получаем например две группы элементов дальше мы к не разбили на две каждый из этих групп мы дальше не двигаемся А в LG beami У нас вот разбили на две У нас две новые ноды потом мы среди всех выбираем какую разбить разбили это на 2 теперь выбираем из этих трех Может быть сейчас лучше разбить еще эту на две а может быть лучше Вот это разбить мы как бы всех одинаково принимаем и а это идет к тому что могут быть очень сильно асимметричные А их же будете они все ну вот сайте как зависит количество листьев от Глубины в их же пустеп Вайс деревьях они два в степени нас если глубина глубина 2 то у нас будет Два листа на 3 забьются еще будут 4 и так далее Вопросик Как можем тоже это'
  question_topic: ML

--- CHAPTER `00:40:10` — Оценка предсказаний регрессионной модели ---
window: 00:40:10 .. 00:43:48
recognition_status: single (1 items)

ITEM #16
  interviewer_question: time=00:40:10 text='вот хотим сделали предсказание как-то оценить вот новых данных модель делает предсказания хотим оценить насколько модель уверенно или не уверена своих предсказаниях модель регрессии градиентным бустинг регрессивный'
  candidate_answer: time=00:40:15 text='вот новых данных модель делает предсказания хотим оценить насколько модель уверенно или не уверена своих предсказаниях модель регрессии градиентным бустинг регрессивный То есть как можем У нас есть метрики но Метрика это что-то про всю модель в целом а мы хотим именно на уровне одного объекта понять это объект который модели сильно понятно как предсказывает и хорошо В таких вот сейчас разбирается какой-то объект или это объект совершенно новый и типа предсказания которые она сделала она очень такой шаткое что мы можем сделать как можем какую-то оценку уверен с неуверенность Но я могу ошибаться но мне единственное что приходит на ум это вот посмотреть дисперсию насколько она изменилась Ну у нас допустим когда дерево строится Да мы там разбиваем на признаки и смотрим насколько у нас изменилось допустим если мы говорим про регрессию насколько сильно изменилась у нас дисперсия то есть разброс пока еще не понимаю обычная модель на новых данных она делает предсказание как мы здесь какой-то дисперсию мы не знаем реальные Таргет найти просто хотим например отследить что чуваки на этих данных мы уверены что модель знает что предсказала на этих есть сомнения Будьте Аккуратнее Ну возможно не знаю вызвать этот метод фьючером потенции Это не по объектам Ну хорошо сразу тогда подскажу есть задача третьего уровня симуляторе называется Бусинка Как можно оценивать уверенность предсказание модели в случае градиентов если совсем вермитрия такая вот у нас модель Как делать предсказания если модель уверена в этом объекте у нас деревья друг друга исправляют и если то она уже на первых стадиях на первых там десяти стать нужным ответа следующий будет какой-то косметику вносить А если модель не уверена то от дерева к дереву на таких объектах и будет ворошить и можем там с каким -то какие-то такие Под ансамбли посмотреть как у них есть разногласия или нет И посчитать разброс и Мы это можем сделать на новых объектах спокойно по объекту то есть Можем Конечно все это сделать но таким образом точно оценить модели с такими объектами хорошо работает плохо работает Дальше расскажи про диплои Маша и сервисов'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:42:17 text='подскажу есть задача третьего уровня симуляторе называется Бусинка Как можно оценивать уверенность предсказание модели в случае градиентов если совсем вермитрия такая вот у нас модель Как делать предсказания если модель уверена в этом объекте у нас деревья друг друга исправляют и если то она уже на первых стадиях на первых там десяти стать нужным ответа следующий будет какой-то косметику вносить А если модель не уверена то от дерева к дереву на таких объектах и будет ворошить и можем там с каким -то какие-то такие Под ансамбли посмотреть как у них есть разногласия или нет И посчитать разброс и Мы это можем сделать на новых объектах спокойно по объекту то есть Можем Конечно все это сделать но таким образом точно оценить модели с такими объектами хорошо работает плохо работает'
  question_topic: ML

--- CHAPTER `00:43:48` — Deploy ML-сервисов ---
window: 00:43:48 .. 00:47:20
recognition_status: single (1 items)

ITEM #17
  interviewer_question: time=00:43:48 text='расскажи про диплои Маша и сервисов как-то вообще происходит что это такое зачем это нужно'
  candidate_answer: time=00:43:54 text='зачем это нужно диплоид насколько понимаю это вывод Продакшен это уже непосредственно запуск модели и я так понимаю что еще автоматически до обучения модели можно сделать на новых данных которые происходят допустим у нас модель мы вручную обучать хотя бы просто как мы ее вводим в продакш и здесь есть элементы шаги подводные камни это задача но непосредственно у нас я еще не дошел к сожалению могут так порассуждать какие есть этапы рассуждают Да что первое что нам самое главное это Нужны хорошие данные правильные без ошибок пропусков и так далее То есть пусть у нас хорошие данные уже Кстати как называется Может быть шаг может быть специальность которая занимается качественными данными Да ну допустим мы уже на стадии моделирования проконтролировали что данные хорошие все источники Вот именно сам тепло и как происходит что вообще мы делаем Ну у нас допустим модель висит где-нибудь в Облаке в том же да там или на серваке что такое висит Ну находится Что такое находится Ну то есть как я понимаю что на каком-то сервере развернута Ну то есть там есть как сервис такой допустим какой-нибудь стажер обучил клевую модельку ноутбуке а как сделать так чтобы хорошая модель коллектив ноутбуке вдруг начала приносить деньги Ну то есть она должна выдавать там какие-то предсказания то есть по запросу к ней поступают данные в эту модель Ну как общается сервер клиент с помощью пул квест И что это за такие интересные ключевые слова путь когда мы что-то вносим я вот сомневаюсь может быть некорректно его называю Да чувствуется когда мы пытаемся что-то изменить на севере либо в нашу модель то есть мы туда приносим где-то мы что-то забираем оттуда получаем какие-то предсказания там или еще вот и таким образом Когда у нас модель где-то висит в Облаке на сервере не поступают какие-то данные она их обрабатывает выдает предсказание мы забираем ее по гету по запросу и уже эти данные использую'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:45:51 text='допустим какой-нибудь стажер обучил клевую модельку ноутбуке а как сделать так чтобы хорошая модель коллектив ноутбуке вдруг начала приносить деньги Ну то есть она должна выдавать там какие-то предсказания то есть по запросу к ней поступают данные в эту модель Ну как общается сервер клиент с помощью пул квест И что это за такие интересные ключевые слова путь когда мы что-то вносим я вот сомневаюсь может быть некорректно его называю Да чувствуется когда мы пытаемся что-то изменить на севере либо в нашу модель то есть мы туда приносим где-то мы что-то забираем оттуда получаем какие-то предсказания там или еще вот и таким образом Когда у нас модель где-то висит в Облаке на сервере не поступают какие-то данные она их обрабатывает выдает предсказание мы забираем ее по гету по запросу и уже эти данные использую'
  question_topic: ML

--- CHAPTER `00:47:20` — Web-фреймворки ---
window: 00:47:20 .. 00:48:13
recognition_status: single (1 items)

ITEM #18
  interviewer_question: time=00:47:20 text='Какие ты знаешь'
  candidate_answer: time=00:47:29 text='что угодно просто первое что приходит на ум это не орк это некоторые методология Как правильно вот эти самые запросы оформлять структурировать библиотека по-моему так называется request Если я правильно помню Ну не совсем это еще не фреймворк это именно сейчас'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:47:55 text='это еще не фреймворк это именно сейчас'
  question_topic: Python

--- CHAPTER `00:48:13` — Фиксация версии библиотек ---
window: 00:48:13 .. 00:50:00
recognition_status: single (1 items)

ITEM #19
  interviewer_question: time=00:48:13 text='как фиксируется версия библиотек а вдруг там обновление вышло и вдруг что-то может пойти не так'
  candidate_answer: time=00:48:24 text='приходит здесь только гид версионирование какие-то именно проход А вот в колледже используется много библиотек так и версия ты имеешь ввиду что когда мы допустим делаем модель мы там Файлик рекламируем версии библиотек фиксируем нас нужен Где используется Ну мы допустим можем установить виртуальное окружение с помощью команды с этого файлика закачать все вот эти библиотеки именно в тех версиях которых мы проектировали и это будет гарантировать то что у нас не будет каких-то там ошибок не будет конфликтов с новыми версиями Потому что когда что-то где-то библиотека не фиксирована обновляется Потом что-то падает и день выяснять сервис deployds docker контейнере в котором фиксируется всю нужное окружение Все нужно там база данных библиотек чтобы наш наша модель или наш другой сервис жил зафиксированном таком аквариуме окружение контейнере и здесь мотор от того что там меня обновляется в мире мы были уверены что она будет работать через год'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:48:31 text='библиотек так и версия ты имеешь ввиду что когда мы допустим делаем модель мы там Файлик рекламируем версии библиотек фиксируем нас нужен Где используется Ну мы допустим можем установить виртуальное окружение с помощью команды с этого файлика закачать все вот эти библиотеки именно в тех версиях которых мы проектировали и это будет гарантировать то что у нас не будет каких-то там ошибок не будет конфликтов с новыми версиями Потому что когда что-то где-то библиотека не фиксирована обновляется Потом что-то падает и день выяснять сервис deployds docker контейнере в котором фиксируется всю нужное окружение Все нужно там база данных библиотек чтобы наш наша модель или наш другой сервис жил зафиксированном таком аквариуме окружение контейнере и здесь мотор от того что там меня обновляется в мире мы были уверены что она будет работать'
  question_topic: Python

--- CHAPTER `00:50:00` — За какими метриками можно следить после deploy ---
window: 00:50:00 .. 00:51:33
recognition_status: single (1 items)

ITEM #20
  interviewer_question: time=00:50:00 text='а за какими вот когда мы сервис уже с диплоили он работает метриками можем следить такие технические Может там пару-тройку назовёшь'
  candidate_answer: time=00:50:23 text='видимо еще можно количество запросов фиксировать тоже я думаю да потому что допустим если мы не фиксируем количество там запросов Да к модели и вдруг там что-то упадет мы можем посмотреть мы можем не узнать что был какой-нибудь пиковый скачок Да там в запросах из-за этого модель упала это была именно в этом причина не в чем-то другом что если у нас нет требования на реакцию Нужно ли нам Ну в таком случае мне кажется Ну то есть естественно тут все цели зависит сначала для чего нам Для чего у нас используется этот сервис в каком месте наша бизнес цепочки по последний вопрос перед'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:50:30 text='я думаю да потому что допустим если мы не фиксируем количество там запросов Да к модели и вдруг там что-то упадет мы можем посмотреть мы можем не узнать что был какой-нибудь пиковый скачок Да там в запросах из-за этого модель упала это была именно в этом причина не в чем-то другом что если у нас нет требования на реакцию Нужно ли нам Ну в таком случае мне кажется Ну то есть естественно тут все цели зависит сначала для чего нам Для чего у нас используется этот сервис в каком месте наша бизнес'
  question_topic: Product Metrics

--- CHAPTER `00:51:33` — Как быть, если модель не посчитала предсказание, а ответ нужен быстро ---
window: 00:51:33 .. 00:53:12
recognition_status: single (1 items)

ITEM #21
  interviewer_question: time=00:51:33 text='вот допустим у нас по каким-то причинам вдруг модель не посчитала предсказание у нас Real Time сервис и Ответ нужен быстро что мы тогда можем сделать'
  candidate_answer: time=00:51:55 text='можно найти похожий запрос и выдать по нему вот эти вот ответ такой либо просто предыдущий какой-нибудь допустим как вот сказать если Бывает так что во временных рядах bestline это то что у нас ничего не поменялось то есть какие у нас запросы были да то они примерно такие же дальше будут и на основании этого можно предположить что либо поискать похожие запрос из недавних Да там либо просто последний такой же какой-нибудь выдать похоже поискать это звучит как какая-то тоже задача тоже можно что-то пойти не так Может тоже довольно долго занимать только ты сказал про предыдущий вот ответ на запрос но скорее ты имел ввиду предыдущие какие-то значения действительно какое-то там упрощенная там кстати ты например'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:52:37 text='тоже задача тоже можно что-то пойти не так Может тоже довольно долго занимать только ты сказал про предыдущий вот ответ на запрос но скорее ты имел ввиду предыдущие какие-то значения действительно какое-то там упрощенная там кстати ты например'
  question_topic: ML

--- CHAPTER `00:53:12` — Моделирование прогноза спроса ---
window: 00:53:12 .. 00:55:36
recognition_status: single (1 items)

ITEM #22
  interviewer_question: time=00:53:12 text='делаешь модель предсказания какого-то временного ряда например прогноз спроса простой случай и вот чего бы ты начинал моделировать каких моделей таких подходов'
  candidate_answer: time=00:53:25 text='каких моделей таких подходов Я бы наверное выбрал регрессию линейную в этом случае потому что она которая умеет в тренды Ну то есть она умеет еще проще Может проще линейной регрессии Я думаю что ну либо простой быдлайн то же самое что и было Вот энтом какое-то окно назад то есть Может там медиану средняя там Макс меню То есть ты дай даже есть какие-то признаки ты можешь просто подарки взять предыдущие и уже вот такой модели достаточно и для Full Back ответов сервисе и чтобы посмотреть что тебя работает все как бы нигде не падает и потом уже Линейная модель это усложнение уже там дополнительные вещи которые там с агрегатом потому что только потом если игра стоит переходить к любимом бустингом тем более чем то еще более сложному То есть это условно такое итеративное усложнение У нас есть некоторый такой в голове всегда график вот типа время затраты вот там точность условно вот там Сколько денег можно принести и мы можем принести Ну как бы уже супер базой моделью Там просто средняя на агрегатах Линейная уже настолько много что там вот дальше период осложнения там с помощью бусингов он там не стоит свечи мы там за неделю сделаем чем он там возиться очень долго с чем-то сложным что не такой большой прирост супер Давай тогда откроем Google и что-нибудь в этом духе сделаем простую задачку думаю за 5-10 минут это здание я'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:54:07 text='подарки взять предыдущие и уже вот такой модели достаточно и для Full Back ответов сервисе и чтобы посмотреть что тебя работает все как бы нигде не падает и потом уже Линейная модель это усложнение уже там дополнительные вещи которые там с агрегатом потому что только потом если игра стоит переходить к любимом бустингом тем более чем то еще более сложному То есть это условно такое итеративное усложнение У нас есть некоторый такой в голове всегда график вот типа время затраты вот там точность условно вот там Сколько денег можно принести и мы можем принести Ну как бы уже супер базой моделью Там просто средняя на агрегатах Линейная уже настолько много что там вот дальше период осложнения там с помощью бусингов он там не стоит свечи мы там за неделю сделаем чем он там возиться очень долго с чем-то сложным что не такой большой прирост'
  question_topic: ML

--- CHAPTER `00:55:36` — Практика ---
window: 00:55:36 .. 01:06:15
recognition_status: single (1 items)

ITEM #23
  interviewer_question: time=00:55:36 text='Напиши пожалуйста функцию которая выводит числа от одного до n Но если число делится на 3 вместо числа нужно выводить из Fi Z если число делится на 5 место числа нужно вводить баз и если число делится и на 3 на 5 нужно выводить из вас'
  candidate_answer: time=00:57:22 text='Значит нужно писать такую мы принимаем сюда число какой-то да по-моему так если у нас внутри есть у нас на 5 Ну можно здесь попробовать такое в лоб решение что допустим как я здесь написал слова если у нас делится без остатка на 3 но при этом у нас не делится без остатка на 5 то там выводить и так далее третий и получится что если делится это тогда то мы выводим просто бас просто у нас он уже не должен делиться на три но при этом делится на 5 просто здесь можно написать сейчас я пытаюсь просто вспомнить Мне просто кажется надо задать я сейчас думал о том что если я сейчас выведу как бы els чтобы напишу Принт физбасс то он во всех случаях кроме этих будет выводить Принт это будет неверно Тогда здесь нужно сделать или единственное я с этим моментом немного сомневаюсь Правильно ли выставил обозначение что принимаемые у нас тип аргумента должен быть винтовый запустил не совсем так я ожидал случайно поставил троечку вместо ожидаемое поведение теперь Но я же сказал что нужно вывести число от 1 до n а оно выводит только одну строчку А так я прошу прощения Я когда писал сконцентрироваться на этих так еще раз если делится на три без остатка то получается мы выводим физ и и плюс числа Повтори пожалуйста задание мы вводим числа от 1 до n если число делится на 3 выводим вместо числа при вот в данном примере которые сделал при числе 15 у нас должно было вывести один два если тройка то это должно вывести физ потом 45-65 здесь тогда это нужно делать в цикле получается мы будем продвигаться от 0 до а N у нас кстати мы включительно или не включительно мы от одного до нет то есть мы если 15 Значит надо от 1 до плюс 1 Ну просто если мы делаем цикл Все я понял in Range нужно от единицы до n + 1 правильно таком случае где но если мы хотим 15 включить в наш диапазон дальше мы выводим на каждом мы проверяем сейчас тогда получается может быть нам здесь просто нужно выводить и нам а нам нужно вывести именно последовательность все от одного по полностью То есть у нас тогда здесь у нас Нам нужно поменять и нужно поменять и правильно но проблема будет в том насколько я помню что у нас цикл прервется когда одно из этих действий выполнится насколько я помню Салам выглядит правильно на самом деле у этой задачи есть несколько еще шагов которые мы уже не успеваем которые уже не успеваем перейти но того что написал уже достаточно чтобы некоторых связь сдать да будем уже'
  reference_answer: time=None text=None
  interviewer_feedback: time=01:01:56 text='не совсем так я ожидал случайно поставил троечку вместо ожидаемое поведение теперь Но я же сказал что нужно вывести число от 1 до n а оно выводит только одну строчку А так я прошу прощения Я когда писал сконцентрироваться на этих так еще раз если делится на три без остатка то получается мы выводим физ и и плюс числа Повтори пожалуйста задание мы вводим числа от 1 до n если число делится на 3 выводим вместо числа при вот в данном примере которые сделал при числе 15 у нас должно было вывести один два если тройка то это должно вывести физ потом 45-65 здесь тогда это нужно делать в цикле получается мы будем продвигаться от 0 до а N у нас кстати мы включительно или не включительно мы от одного до нет то есть мы если 15 Значит надо от 1 до плюс 1 Ну просто если мы делаем цикл Все я понял in Range нужно от единицы до n + 1 правильно таком случае где но если мы хотим 15 включить в наш диапазон дальше мы выводим на каждом мы проверяем сейчас тогда получается может быть нам здесь просто нужно выводить и нам а нам нужно вывести именно последовательность все от одного по полностью То есть у нас тогда здесь у нас Нам нужно поменять и нужно поменять и правильно но проблема будет в том насколько я помню что у нас цикл прервется когда одно из этих действий выполнится насколько я помню Салам выглядит правильно на самом деле у этой задачи есть несколько еще шагов которые мы уже не успеваем которые уже не успеваем перейти но того что написал уже достаточно чтобы некоторых связь сдать да будем уже'
  question_topic: Python

SAVE JSON: вставьте ответ в конец файла /Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-engineer-junior-karpov-2023-03-09/ml-engineer-junior-karpov-2023-03-09.v2.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
