<!-- PIPELINE_MANIFEST
{
  "version": 2,
  "basename": "data-scientist-middle-karpov-ml-2022-06-26",
  "transcript_folder": "transcripts/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26",
  "source_id": "data_scientist_middle_karpov_ml_2022_06_26",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 18:07:30 +0200",
  "updated_at": "2026-05-20 18:11:52 +0200",
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
    "json": "splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/timecodes.txt",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 18:07:30 +0200"
    },
    {
      "id": 2,
      "name": "qa_extraction",
      "llm": true,
      "model": "claude-sonnet-4-6",
      "inputs": [
        "splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.pipeline-log.md#LLM_INPUT_STEP_2"
      ],
      "outputs": [
        "splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.json"
      ],
      "status": "completed",
      "duration_sec": 180.0,
      "notes": null,
      "finished_at": "2026-05-20 18:11:19 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 2.0,
      "notes": null,
      "finished_at": "2026-05-20 18:11:18 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 18:11:18 +0200"
    },
    {
      "id": 5,
      "name": "semantic_validation",
      "llm": true,
      "model": "claude-sonnet-4-6",
      "inputs": [
        "splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.pipeline-log.md#LLM_INPUT_STEP_5"
      ],
      "outputs": [
        "splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 90.0,
      "notes": null,
      "finished_at": "2026-05-20 18:11:52 +0200"
    }
  ]
}
-->

# Pipeline log v2

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26`
- **Source ID:** `data_scientist_middle_karpov_ml_2022_06_26`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 18:07:30 +0200
- **Last updated:** 2026-05-20 18:11:52 +0200

Фильтр в IDE: `*data-scientist-middle-karpov-ml-2022-06-26.v2*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/timecodes.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.pipeline-log.md` | — | completed |
| 2 | qa_extraction | yes | claude-sonnet-4-6 | `splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.pipeline-log.md#LLM_INPUT_STEP_2` | `splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.json` | 180.0s | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.xlsx` | 2.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.validation-report.md` | 1.0s | completed |
| 5 | semantic_validation | yes | claude-sonnet-4-6 | `splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.pipeline-log.md#LLM_INPUT_STEP_5` | `splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.validation-report.md` | 90.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.pipeline-log.md`

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
SOURCE_ID: data_scientist_middle_karpov_ml_2022_06_26
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00:00] у
[00:00:02] нас будет
[00:00:05] мог интервью давай но прежде чем мы
[00:00:09] вообще начнем какую-то такую
[00:00:11] официальную вещь
[00:00:14] нужно ответить тебе на несколько
[00:00:16] вопросов
[00:00:19] нас мы друг друга знаем
[00:00:22] ты у меня работала на основной на
[00:00:27] последних по вековых работах был
[00:00:30] небольшой промежуток времени когда-то
[00:00:31] создания работал мы не будем смотреть
[00:00:35] так время расскажи немножко о себе
[00:00:38] кем ты сейчас работаешь и
[00:00:44] как тебе вообще пришла
[00:00:46] ну или как тебе уговорили участвовать
[00:00:50] участвовать собеседованием на самом деле
[00:00:53] очень классная штука существо что я у
[00:00:57] меня странный программу если я пришла из
[00:01:00] академической среды и вообще по
[00:01:02] образованию химик и наверное это немного
[00:01:05] странно людям которые пришли смотреть
[00:01:08] собеседования на
[00:01:10] специальность вот но уже какое-то время
[00:01:13] я обработала и вот мое первое такое в
[00:01:17] продакшн работа была анастаса компании
[00:01:20] x5 занимались всякими
[00:01:23] интересными вещами и потом еще раз
[00:01:26] поработали в другой компании пошли
[00:01:28] работал стас то можно дать название
[00:01:29] компании конечно грех ну в общем потом
[00:01:33] мы повторили этот мув не аптеки
[00:01:35] это очень разные компании но и сделал
[00:01:38] по-своему прикольно сейчас я работаю
[00:01:41] продолжу работы аптеки
[00:01:43] продолжаю поддерживать вещи которые
[00:01:45] станислав успел сделать как это их
[00:01:48] дорабатывать или flock 3 и плюс
[00:01:50] разрабатываю там еще пресете продуктовые
[00:01:52] штучек которые связаны с
[00:01:53] рекомендательными системами и
[00:01:56] с анализом выкуп они выкупают законы
[00:02:02] решен а слушай
[00:02:07] формально наша собеседование будет
[00:02:10] состоять из 4 частей но так как ты со
[00:02:13] мной проводила эти с беседами
[00:02:17] ты в принципе уже знакомо и для тебя их
[00:02:21] будет не так чтобы очень сложно вот
[00:02:26] 4 4 части первая часть будет про
[00:02:32] мои дизайн и человек у нас с опытом
[00:02:37] соответственно должна уметь отвечать на
[00:02:40] вопрос поймать и зайду
[00:02:42] вторая часть будет наверное по бетону и
[00:02:45] папе там будут достаточно тяжелые
[00:02:48] вопросики на 10 и хорошо kotova вот
[00:02:53] затем будет эта ценность и в основном
[00:02:57] это сайт части мы поговорим про какие-то
[00:03:00] практические вещи и
[00:03:04] наверное потом не знаю умение работать с
[00:03:07] данными или обрезка подумаю что я выберу
[00:03:11] посмотрим как ты будешь отвечать
[00:03:16] ему заранее скажу что ничего в этом
[00:03:19] страшного нет
[00:03:22] на самом деле ты моя не первая попытка
[00:03:25] записи человека именно там на металл
[00:03:29] уровень
[00:03:30] вот я пробовал записываться с двумя
[00:03:34] людьми к средине воздушные думали не
[00:03:38] публикуется нет
[00:03:41] не пошло но я надеюсь вот эта часть и
[00:03:45] эта вырежут потом паспорта
[00:03:57] [музыка]
[00:04:03] нет я выкладывать не буду естественно
[00:04:06] естественно
[00:04:07] сам интересное ко мне приходил парень
[00:04:12] которому этого мы вдвоем с беседовали и
[00:04:17] к сожалению на второй раз он отвечал не
[00:04:20] так хорошо как то первый раз
[00:04:22] да но потому что у меня сильно поднялись
[00:04:26] вопросы честно говоря и
[00:04:28] и я немного другого ожидал от его
[00:04:31] ответов соответственно все прошло не
[00:04:33] очень хорошо но мы не будем
[00:04:35] так
[00:04:37] еще два я от себя замечу что даст осей
[00:04:42] мы
[00:04:43] работали несколько раз вместе честно
[00:04:47] говоря анастасию мне привел дархан
[00:04:50] это тоже очень важный человек в моей
[00:04:52] жизни
[00:04:53] надеюсь и в твоей ность тоже потому что
[00:04:57] через по сути своей дархан а я
[00:05:01] познакомился снасти
[00:05:02] реинвест работал и в x5 египте
[00:05:06] вот
[00:05:09] начнем с дизайна если ты непротив
[00:05:14] задачу я дам ту которую меня одна
[00:05:18] компания не так давно в собеседованиях
[00:05:21] вот задача про
[00:05:25] он тебе и предсказанием тебе
[00:05:30] интересно то что я
[00:05:34] честно говоря не очень хорошо снова как
[00:05:36] решается такая задача но то есть я
[00:05:39] что-то слышу и видел с опытом
[00:05:44] знал что такую задачу в целом решает
[00:05:47] множество различных компаний вот но для
[00:05:50] себя решил что
[00:05:52] постараюсь сделать какое-то интересное
[00:05:54] решение
[00:05:55] предложить какое-то интересное решение и
[00:05:58] подсказать что это будет в общем
[00:06:02] он тебе
[00:06:05] важно то
[00:06:06] это lcd мы предсказываем тебе это like
[00:06:10] them were на всякий случай для тех людей
[00:06:12] кто не знает что это такое а тебе это
[00:06:14] лифтинга по сути своей
[00:06:17] оценка пользователя с точки зрения того
[00:06:20] сколько денег он может принести к нам в
[00:06:23] будущем это всегда farkas на будущее
[00:06:26] очень часто
[00:06:29] вот
[00:06:30] горизонт вот этого предсказания
[00:06:32] он такие тем или иным образом
[00:06:35] ограничивается но в нашем случае это
[00:06:37] ограничение будет на полгода вперед
[00:06:41] то есть мы заранее забиваемся на то что
[00:06:43] мы считаем активе центре горизонт
[00:06:45] прогнозирования полгода сперва и
[00:06:47] что то что прогнозировать дальше чем
[00:06:52] полугода мне вообще не нужно нет не
[00:06:55] нужно но ты должна понимать что
[00:07:02] есть свои нюансы в том что ты прогноз
[00:07:05] штангу год вперед
[00:07:08] условно ну давай возьмем
[00:07:10] сентябре прошлого года
[00:07:13] и вот мама ее лишнего года мы живем в
[00:07:16] парадигме что есть anomaly
[00:07:19] сейчас мы живем в парадигме что есть мир
[00:07:22] который изменяется начнем с это хорошо
[00:07:26] мир который леди меняется и
[00:07:31] мы пытаемся спрогнозировать нужно ли нам
[00:07:34] посчитать и lateview с учетом в пол года
[00:07:37] максимально границ полгода сейчас
[00:07:40] сегодня и зафиксировать его пусть на
[00:07:42] этом и у тебя будет принят какие-то
[00:07:44] решения сейчас очень важные или можем
[00:07:46] пересчитывать и активе хотите по каждый
[00:07:48] день и смотреть как она меняется для
[00:07:51] каждого клиента ну по сути это вопрос
[00:07:53] про душ самой аномалию какой-то который
[00:07:55] может произойти или любые другие
[00:07:57] какие-то факторы
[00:07:58] [музыка]
[00:07:59] промо нагрузках какое-то возросла и мы
[00:08:02] стали больше получать клиентов что-то в
[00:08:06] короче могу ли я пересчитывать или я
[00:08:09] буду считать метрику типа важно ли
[00:08:11] как-то попытаться границы
[00:08:16] оптимистичные и пессимистичные на берегу
[00:08:20] давай так да на основе твоего прогноза
[00:08:24] бизнес будет принимать какие-то решения
[00:08:26] в том числе
[00:08:28] [музыка]
[00:08:30] стоит ли с этим человеком продолжать
[00:08:33] работать или не стоит то есть
[00:08:36] использовать его в коммуникации не
[00:08:38] используйте так далее то есть я должна
[00:08:39] понимать что
[00:08:41] твой прогноз он естественно существенно
[00:08:44] влияет на бизнес и
[00:08:49] на все остальное как именно это будешь
[00:08:52] считать
[00:08:54] различные варианты сценариев
[00:08:56] наверное я хотел бы чтобы ты рассказала
[00:08:58] об этом поподробнее
[00:09:02] сделаю предположение
[00:09:03] очень во-первых мы 71 его просьбу крюшо
[00:09:07] что и у тебя будет ли у меня граница
[00:09:09] маккейна есть то есть мы точно знаем что
[00:09:12] пол года
[00:09:15] ограниченный
[00:09:17] и
[00:09:17] какой бизнес кстати
[00:09:23] что еще раз это контрактный бизнес когда
[00:09:26] у нас есть там подписки есть точный флаг
[00:09:28] того что там клиент ушел или это покупки
[00:09:31] какой-то retail где мы точно не знаем
[00:09:33] куплен с нами до сих пор или нет это все
[00:09:35] тех это фильм тех это значит то что
[00:09:40] нам нужно чтобы человек
[00:09:47] он занимается допустим покупкой продажи
[00:09:50] акций
[00:09:51] или валюты какой-то или криптовалюту
[00:09:54] какой-то и так далее то есть короче
[00:09:56] нигде так де сак у нас никому просто
[00:09:58] двумя какие-то действия и нам нужно
[00:10:01] самим принимать решения там ушел эмили
[00:10:02] еще нет
[00:10:06] ну во первых то есть тут у нас встает
[00:10:10] вопрос сколько человек будет приносить
[00:10:11] денег и сколько он будет жить из-за тех
[00:10:14] двух факторов мы можем управлять
[00:10:17] прогнозировать all these
[00:10:19] это как не очень довольна смотришь в
[00:10:21] общем если что останавливаю не визаране
[00:10:27] поэтому есть короче я собственно вы
[00:10:31] кстати когда работал и не с тобой как
[00:10:33] времени я снимала с тем что работала с
[00:10:36] оттоком предлагала бы и знаем какие то
[00:10:39] алгоритмы для идентификации людей
[00:10:41] которые обтекают не там в принципе не
[00:10:43] плохо себя вели такие простые штуки как
[00:10:46] rfm анализ достичь ее на ресницы
[00:10:49] frequency переменных можно с помощью
[00:10:54] распределений учить распределение чтобы
[00:10:57] понять остается человек с нами грубо
[00:10:59] говоря прогнозировать вероятность того
[00:11:01] что человек сюжет покупку какой-то брюс
[00:11:03] жутко ремни в принципе ну а на моём
[00:11:07] такому описи когда работает просто был
[00:11:10] ритейл что похоже по модели поэтому и
[00:11:13] спрашиваю если нас подписка елена нужно
[00:11:15] оценивать
[00:11:16] мне кажется довольно удачная штука для
[00:11:19] того чтобы использовать
[00:11:21] выхода этих алгоритмов статистических
[00:11:27] я дальнейшего прогноза короче
[00:11:29] статистический алгоритм они во-первых
[00:11:30] умеют и прогнозировать на самом деле eu
[00:11:33] te vi
[00:11:35] но
[00:11:37] может право делать что-то сложное мой
[00:11:40] ответ что я бы попробовала применить
[00:11:42] известный меня библиотека это рисовала
[00:11:45] книги и она довольно простая не
[00:11:48] нагружает из там нет какой беды и с
[00:11:51] производительностью и но непростой
[00:11:53] подходят которые хорошо интерпретируется
[00:11:55] предам там есть свои проблемы и логика
[00:11:59] довольно просто поэтому наверное
[00:12:01] возможно потом бизнес захотела бы что-то
[00:12:03] более сложное
[00:12:05] вот поэтому короче за быть моим берем
[00:12:08] какие-то а мы и хотим тесто проводить
[00:12:11] как-то развивать мы сразу хотим пришлось
[00:12:15] сделать
[00:12:18] давай так
[00:12:20] в рамках и молиться зайна
[00:12:23] предполагается что ты ответишь на там
[00:12:25] несколько ключевых вопросов
[00:12:28] хотелось бы знать что ты вот в руках
[00:12:31] моризо нереально на них ответишь
[00:12:35] каких-либо ничего set
[00:12:37] короче если бы делала я я бы предложила
[00:12:42] 1 быть line модель то есть хотя бы хоть
[00:12:45] как-то прогнозировать и вины не показать
[00:12:47] какие-то метрики и
[00:12:50] обсудить с бизнесом достаточно ли это
[00:12:53] качество прогноза или рамки в которых
[00:12:55] она прогнозирует они слишком широкий для
[00:12:57] них и мы на этом точно не
[00:12:59] останавливаются ни какие песни у пилота
[00:13:01] и ни во что не идем хотя тут
[00:13:02] пилотировать довольно сложно скорее
[00:13:04] всего на потому что с период полугода
[00:13:07] скорее и вот в полгода не будет и я бы
[00:13:11] вы лидера валось просто на отложенных
[00:13:14] тайские валидации показывал бы бизнесом
[00:13:17] результаты отважные выборки то есть дети
[00:13:20] потом несколько раз казино что это все
[00:13:22] воспроизводится то есть одни полугода к
[00:13:25] полугоду со смещениями с окнами модели
[00:13:28] примерный знак ушек клик
[00:13:30] вот какую ошибку но поскольку у нас а у
[00:13:33] тебя какая метрику лиц
[00:13:37] это
[00:13:38] [музыка]
[00:13:42] важно ли нам
[00:13:45] короче бизнес я бы узнал у бизнеса важно
[00:13:48] ли им что лучше перепроверь и
[00:13:51] прогнозировать или нет и прогнозировать
[00:13:53] дает ли бизнес не ответный выброс но
[00:13:57] скорее всего нет а прогноз не до прогноз
[00:14:00] лучше да но не хочется быть совсем
[00:14:03] оптимистичной окей тогда можно
[00:14:07] попробовать какие-то метрики
[00:14:09] и мы сне
[00:14:12] нет
[00:14:14] можно попробовать и более сложные как
[00:14:16] раз и несимметричный не только который
[00:14:19] ты очень любишь
[00:14:20] разный коэффициент на пире прогнозами до
[00:14:23] продлевать принципе все можно начать
[00:14:25] считать и если бизнес настаивает что у
[00:14:27] него
[00:14:28] приоритеты кто что ему важнее то можно
[00:14:31] использовать начнут речную просто с
[00:14:33] различным углом наклона
[00:14:36] штрафа с
[00:14:39] зависимости от знака в общем ошибки
[00:14:43] так но я запишу себе
[00:14:52] наверно будет то думает что у тиражные
[00:14:56] выбросы я прям буду смотреть на
[00:15:00] конкретную клиенту часто или я будет
[00:15:03] смотреть в сумах
[00:15:05] чаще и
[00:15:06] конкретного клиента
[00:15:08] ну вообще это тебе прогноз нужно сделать
[00:15:12] для каждого клиента
[00:15:16] ну давай я буду читать его съел
[00:15:19] я для себя решил с этим из всех в
[00:15:22] качестве и буду варьироваться на ней
[00:15:26] [музыка]
[00:15:29] так я покажу
[00:15:32] ну собственно вот больную горит мы идем
[00:15:35] к бизнесу показываемся метрики объясняем
[00:15:37] что за метрика что она читает и
[00:15:39] наверное даже ним и съела нужно брать
[00:15:43] rms я потому что бизнес будет сложно
[00:15:46] оценить
[00:15:47] квадратах наклонения лучше наверное
[00:15:51] показывать
[00:15:52] тех значения которые ну короче понятнее
[00:15:56] никотине квадраты корни
[00:16:01] [музыка]
[00:16:03] должны рынок долях было бы понять некий
[00:16:07] процент наверняка не на цены чтобы они
[00:16:11] видели а не конкретные значения все-таки
[00:16:14] мирные процентов не было бы так удобно
[00:16:15] показан в процентов
[00:16:17] ошибку
[00:16:19] так поэтому
[00:16:22] в общем если я бизнес не устраивает и мы
[00:16:26] не хотим а это использовать google и
[00:16:28] катить пока что мы видим что это более
[00:16:31] сложно это я бы сюда привлекала какую-то
[00:16:34] дополнительную информацию клиенту
[00:16:35] который меня есть об истории того что
[00:16:37] они делали потому что эти алгоритмы
[00:16:40] листиках они знают только recency
[00:16:43] frequency то есть по сути это время
[00:16:44] жизни клиент этому
[00:16:47] время его жизни сейчас
[00:16:49] сколько покупок он совершал не там время
[00:16:52] с последней покупки это довольно мало
[00:16:54] данных хотя практика показывает просто
[00:16:57] хорошо описывает таких моделях но
[00:16:59] давайте добавляете тогда любой
[00:17:01] информации клиента который у нас есть
[00:17:03] например с какими если ты финн тех начну
[00:17:08] покупает акции и придает белью
[00:17:11] на скорее всего есть какие-то категории
[00:17:15] акции ну компании с которыми он
[00:17:17] взаимодействует можно построить какой-то
[00:17:19] профиль клиента в зависимости от того
[00:17:22] какие операции он совершал на какие
[00:17:24] суммы он что-то делал но правильным
[00:17:28] сумок операции его
[00:17:30] [музыка]
[00:17:31] есть сектор компании навернео браво не
[00:17:34] стоит наверное брать компании конкретный
[00:17:36] построить брайтон энергетика дайте еще
[00:17:40] что то какие то большие сектора причем
[00:17:42] наверно стоит побить возможности по
[00:17:44] государством или там как-то пока
[00:17:47] мастером государство вкладывает
[00:17:49] если вы что-то российской рассматриваем
[00:17:51] вернет большая разница укладывается
[00:17:53] российский эти компании или
[00:17:55] зарубежный анти сектор вот научно
[00:17:59] собрать профи клиента для того чтобы
[00:18:01] использовать какой-то другой модели
[00:18:06] в модели возможно это можно назвать
[00:18:09] моделью типа второго уровня если мы
[00:18:10] пишем небольшой подходит из поединком
[00:18:13] прозван горит мы получаем от туда и
[00:18:15] печенье из
[00:18:16] ресницы frequency в этот анализ дает нам
[00:18:20] там эффектов или не язык на самом деле
[00:18:22] они могут и тени прочитать можно идти
[00:18:25] некуда запихнуть что эти алгоритмы могут
[00:18:28] дать можем использовать в качестве печей
[00:18:30] для алгоритма второго уровня и
[00:18:33] туда же добавить фичи клиента и
[00:18:39] сделал такой
[00:18:44] и как болгария если
[00:18:47] хочешь к спросить какую модель втором
[00:18:49] уровне skillet
[00:18:53] например если мне нужно прогнозировать
[00:18:56] или тени
[00:18:58] ну я бы честно говоря
[00:19:04] но поскольку я могу посчитать так
[00:19:07] время прогнозное время жизни этого
[00:19:10] клиента
[00:19:11] мне уже как бы тоже не нужны никакие
[00:19:14] день мериды потому что у меня уже есть
[00:19:16] как бы прогнозы вот сколько он проживет
[00:19:19] я бы взяла просто какой-нибудь busting
[00:19:22] например который будет а если мне меня
[00:19:25] важно интерпретируем
[00:19:31] верно первых этапах до важно будет ну а
[00:19:34] затем
[00:19:35] пожара но затем можно глупым после
[00:19:40] какого-то там условно после какой-то
[00:19:43] итерации можем переходить на таки
[00:19:47] интерпретируем модели долго вообще нас
[00:19:50] конечно
[00:19:53] нет на самом деле есть я все равно
[00:19:55] хотела сказать что я бы наверное для
[00:19:57] себя ямасиро в первую очередь попробовал
[00:19:59] и ну я посмотрел сколько фичей
[00:20:00] получается конечно если не очень много
[00:20:02] то можно было бы попробовать каким-то
[00:20:05] линейными алгоритмами чтобы было
[00:20:07] интерпретируем как раз но если много
[00:20:10] печей и непонятного
[00:20:13] как они должны влиять я бы наверное все
[00:20:15] равно
[00:20:16] попробовал бы сделать гусь тенге
[00:20:19] посмотрела бы что получается короче я
[00:20:21] буду водила gustin гамме модель для того
[00:20:23] чтобы была минимальной ошибка
[00:20:26] смотрел об этом глазами чего получается
[00:20:29] и
[00:20:30] потом уже если вы не сказали два
[00:20:32] интерпретировать я бы уже прибегла к
[00:20:34] методам специальный интернет sender
[00:20:39] внутри можно было бы попробовать линейку
[00:20:41] чтобы оно было сразу петером и но
[00:20:45] ну такой первый подход из линейка
[00:20:47] прокатило вы хорошо на ней божественное
[00:20:50] здесь мы сравнили бы с бусинками
[00:20:52] получается или прирост качества если
[00:20:54] просто качество нет то осваивались на
[00:20:55] линейке это проще объяснять и не
[00:20:58] посчитать вот если
[00:21:02] бусин дает сильный лучше результаты там
[00:21:05] сколько больше возможностей всего так и
[00:21:07] будет то хотя хочу заметить что у меня
[00:21:12] есть переменные которые скорее всего
[00:21:14] очень сильные предиктор или много шума у
[00:21:17] переменной хороший предикторы имею ввиду
[00:21:19] это переменные выходы
[00:21:21] статистических вот этих моделях скорее
[00:21:23] всего не очень сильно будет
[00:21:24] коррелировать с метр переменной поэтому
[00:21:27] возможно линейка здесь правда было бы
[00:21:29] хорошо какой-то маленький лес имели бы
[00:21:32] экичи клиента и
[00:21:34] кстати о макроэкономические фичи тоже
[00:21:36] можно было бы добавить
[00:21:38] это я про это не сказал а но я
[00:21:41] перебывает валюту и сейчас добавляю
[00:21:44] какие-нибудь я бы попробовал добавить
[00:21:46] какие-нибудь мы же взять информация
[00:21:50] компания сто процентов есть какая-то
[00:21:51] аналитика по рынку и наверное хранится и
[00:21:54] легко было бы достать даже внутри
[00:21:56] компании своих данных какой-то ситуацию
[00:22:00] на рынке там курсы какие-то индексы и не
[00:22:04] очень хорошо разбирающихся в тени и
[00:22:05] скорее всего есть какие-то индексы в
[00:22:08] экономике индустрии что-нибудь такое
[00:22:10] человек скорее всего была бы к его
[00:22:12] использовать это было погрозила
[00:22:14] насколько в общем люди он вообще
[00:22:16] привлекательно основе сейчас работать
[00:22:18] если там что падает мирное людям тоже не
[00:22:20] очень интересно
[00:22:21] так я из-за данный вопрос как бы я
[00:22:26] интерпретировал модель которые они не
[00:22:28] рекрутируются
[00:22:32] давай так не совсем так я
[00:22:35] [музыка]
[00:22:38] задавал вопрос какие способы
[00:22:39] интерпретации есть но давай сейчас
[00:22:42] ты закончила ответы и мы уже переходим к
[00:22:46] вопросам или есть еще что-то что-то не
[00:22:49] покрыла в рамках мы редизайн и хочешь
[00:22:52] сказать о какой-то блок
[00:22:55] так на смотри очень сейчас я пытаюсь
[00:22:57] подытожить ничего ли не забыла за одну я
[00:23:01] смотрю что у нее с по данным как долго у
[00:23:05] меня в принципе живут клиенты и полгода
[00:23:09] короче если честно я бы первые да если
[00:23:12] мне сказали точно полгода
[00:23:15] прогнозирую его я бы все-таки попробую
[00:23:17] проверить так часто клиенты уходят на
[00:23:19] полгода потом возвращаются что это такое
[00:23:22] что это нормальный нормальная границы
[00:23:26] для как назвать и если клиент полгода не
[00:23:29] возвращается что он правду шел что такое
[00:23:32] был бы определить вроде тем я бы перешла
[00:23:35] к подготовке печей для
[00:23:39] статистических моделей посчитала бы ими
[00:23:42] 75 показатели они это умеют и ути
[00:23:45] мечтать и
[00:23:46] отток считать до сикст iv не актив на
[00:23:50] какую-то дату
[00:23:51] довольно большой горизонт
[00:23:54] наверное я бы посчитала для входа во
[00:23:56] второй алгоритм возможно стоило бы
[00:23:59] посчитать не на горизонт полгода она
[00:24:01] несколько горизонтах прогнать этих
[00:24:03] алгоритмов но там из мультика нервности
[00:24:06] надо было поработать чем возможно это
[00:24:09] хорошая идея возможно не очень но это
[00:24:11] можно проверить по ходу нужно
[00:24:13] сгенерировать как готов побороться с
[00:24:15] чем-то плохим
[00:24:16] так далее делаю первые вот эти алгоритмы
[00:24:20] с над моделью до обогащаю их выходы
[00:24:23] печами клиента печальные
[00:24:25] макроэкономическими запускаю это все в
[00:24:28] линейку
[00:24:31] запускаю бусинки смотрю что там кофе
[00:24:34] чтим возможно иногда кит убирать
[00:24:36] смотрю
[00:24:41] приемлемыми для метрики вы лидирую с
[00:24:44] бизнесом что
[00:24:45] эмболизацию модельные истории проходят
[00:24:47] вот так достаточно ли это для вас
[00:24:49] метрика или нет если дают зелёный
[00:24:51] светофор грубо говоря то все это
[00:24:54] допиливает не делаем ансамбль нормальный
[00:25:01] и если надо интерпретацию этот дойдем
[00:25:03] интерпретацию
[00:25:05] хорошо
[00:25:07] давай вопросы например
[00:25:13] мы говорили правил
[00:25:15] мы еще очень плотно будем говорить про
[00:25:18] метрики позже давай так и я вот для себя
[00:25:21] понял что скорее всего мы посвятим эта
[00:25:23] работа
[00:25:26] с этим метрикам
[00:25:29] ds часть давай поговорю пробовала друга
[00:25:32] и с какими проблемами ты можешь возник
[00:25:35] столкнуться во время прогноз на полгода
[00:25:39] вперед l2 для людей
[00:25:41] ну собственно проблемы которые мы с
[00:25:44] тобой в первую очередь обсуждали
[00:25:46] проблему китай аномалии и непонятных
[00:25:48] скачков которые в обучении модель их не
[00:25:51] было и какойте сезонности что такое даже
[00:25:55] не сезонность полгода это вообще такая
[00:25:57] это даже неполный год
[00:26:01] нужен я думаю что проблема сезонности от
[00:26:03] самый простой что можно решить проблему
[00:26:06] какой-то резкой аномалии
[00:26:09] нерешаемой на nintendo леру я не считаю
[00:26:13] поэтому это только объяснить заказчику
[00:26:16] что если что-то произойдет то нам нужно
[00:26:19] будет быстренько быть перестроить модели
[00:26:22] пересчитать это с учетом есть грубо
[00:26:25] говоря дуальном или и мы пользуемся
[00:26:26] результатами
[00:26:28] например три месяца у нас было пасторе
[00:26:31] модели а потом мы делаем перерасчет с
[00:26:34] учетом этой аномалии смотрим насколько
[00:26:36] мы ошибаемся туда куда вы нас смещение
[00:26:38] идет если она всех пользователей
[00:26:40] например мы видим смещение этого не до
[00:26:42] прогноз и принес то
[00:26:46] перестроить
[00:26:48] модель .
[00:26:51] обновите и там для последующего уже
[00:26:55] расчет используем новому да
[00:26:58] хорошо давай еще один наводящий вопрос
[00:27:02] что будет с новым пользователем
[00:27:07] кажется что feed которые ты
[00:27:10] перечислял это
[00:27:14] вольно для людей с которыми ты долго а
[00:27:16] для новых пользователей как-то деле
[00:27:19] будешь делать прогноз у нас есть
[00:27:21] какие-то анкетные данные
[00:27:23] есть
[00:27:26] какие-либо пол возраст
[00:27:28] ну допустим есть какой-то создаем есть
[00:27:32] даже возможно там стоишь зачастую в
[00:27:35] таких приложениях есть и trial периоды
[00:27:37] когда людей учат чему-то предлагают
[00:27:41] пройти обучение у тебя
[00:27:44] какой-то опыт с
[00:27:47] ним опыт
[00:27:49] есть какие то данные по поводу того как
[00:27:52] человек проходил обучение ну если у нас
[00:27:55] есть какой-то период обучения или правил
[00:27:58] период это клёво потому что оттуда можно
[00:28:01] все-таки какие-то паторны поведение
[00:28:04] например там насколько и рисковыми и не
[00:28:07] рискованны
[00:28:09] мувы он делает
[00:28:12] можно
[00:28:13] собрать статистику его посещения сайта
[00:28:16] какими разделами но если носить какие-то
[00:28:20] информационные например разделы ничего
[00:28:21] что такое на сайте мы можем пробовать
[00:28:24] любите туда информацию в интересах
[00:28:26] пользователя
[00:28:27] создан плюс
[00:28:30] [музыка]
[00:28:31] чистоту его он захода даже если он не
[00:28:34] делал каких-то
[00:28:37] операции не проводил к возможным заходил
[00:28:40] читал можем посчитать попробовать
[00:28:43] почитать эти метрики
[00:28:44] как часто и как и разделом заходит ну
[00:28:48] это же самости а собственно только для
[00:28:49] новых а для тех конечно хорошо хорошо
[00:28:52] это я понял
[00:28:54] теперь по поводу модели наверное
[00:28:59] правильно я понимаю что это будет единая
[00:29:01] модель какая-то самом начале это будет
[00:29:04] единая линия как правильно ну целом я
[00:29:07] предполагал что да
[00:29:10] если
[00:29:12] но мы можем новых пользователей отдельно
[00:29:15] вынести как раз потому что для них нет
[00:29:17] дальше софи через что мы пойдем это того
[00:29:19] что новый пользователь ну короче
[00:29:22] прогнозировать пытаться для нового
[00:29:24] пользователя и для
[00:29:25] [музыка]
[00:29:26] тех с кем мы давно я для кого достаточно
[00:29:29] данных разными моделями которые в одной
[00:29:31] есть данные много данных об их поведению
[00:29:35] и другой нет рассматривать этих людей
[00:29:37] как разных собственно разные модели ней
[00:29:42] супер супер и теперь наверно последний
[00:29:44] вопрос и что я еще подумала что возможно
[00:29:47] в качестве фичи и можно закладывать
[00:29:49] где связь люди если вы имею информацию о
[00:29:52] том когда люди и когда понятного имеем
[00:29:55] информации люди были привлечены а какие
[00:29:57] то если были акции пример мы знаем что
[00:30:01] люди были привлечены с помощью какой он
[00:30:04] там промокод какой вводили например
[00:30:06] реферальную ссылку с какого-то блогера
[00:30:10] счет чего то мы можем их выделить такие
[00:30:13] тени вк аборты по времени в когорты по
[00:30:17] такие группы по
[00:30:18] способу того что им интересны и что что
[00:30:22] у них влиял
[00:30:24] возможно это для малого количества
[00:30:26] пользователей доступны
[00:30:29] только на же нет и меньше ну типа того
[00:30:32] да если можно отследить потому что не
[00:30:35] всегда можно если дельфин тех скорее
[00:30:36] всего этом был переход по ссылке можно
[00:30:39] было бы это где-то сохранить понятно что
[00:30:41] на истории возможно на стены не хранятся
[00:30:48] нашу супер и давай вот про последнюю
[00:30:52] часть на самом деле зачастую но самое
[00:30:56] важное это про то как ты будешь
[00:30:58] рассказывать ну по сути своей вот тебе
[00:31:01] нужно к тебе пришел бизнес сказал
[00:31:04] сделаны модели lte
[00:31:06] ты не пошла сделала и теперь тебе нужно
[00:31:10] как-то защитить от модели для бизнеса
[00:31:12] как именно вот не до конца я понял как
[00:31:14] именно ты будешь показывать performance
[00:31:17] своей модели насколько я хорош и плохая
[00:31:20] здесь вот такой момент который кажется
[00:31:24] что ты не до конца
[00:31:26] хорошо осветила
[00:31:28] нас внутри я исходя из того что с
[00:31:31] довольно большой период прогнозированию
[00:31:34] и лайкам выигрывает такая штука
[00:31:38] я не могла бы поставить какой-то пилоте
[00:31:41] к на месяц для того чтобы показать их
[00:31:44] умы с этой модели все бы не могла
[00:31:46] показать что на работе trail to you
[00:31:47] хорошо но я могу прожить на истории
[00:31:50] насколько она ошибается могу показать
[00:31:53] что она там делает маленькую ошибку
[00:31:57] ну например наверное все таки моим бы
[00:32:00] использовал тех на приближение
[00:32:03] [музыка]
[00:32:06] показала бы что проценты ветка не
[00:32:08] невелик наверное показал бы на каких
[00:32:11] кейсах где она ошибается почему это если
[00:32:14] бизнес хочет слушать какие могут быть
[00:32:16] нюансы что мне кажется что залог успеха
[00:32:19] всегда показать
[00:32:21] ограничить как бы сразу
[00:32:23] [музыка]
[00:32:26] режим в котором модель работает хорошо
[00:32:29] область определение короче где модели
[00:32:32] можно верить ну дать понять что какие-то
[00:32:36] странные вещи страны пользователь и мы
[00:32:38] вряд ли сможем предугадать но таких
[00:32:41] например очень мало чем попробовала бы
[00:32:43] найти какие-то кейсы где это прям
[00:32:45] наглядно выглядело бы что работает
[00:32:48] хорошо на истории я взяла бы таких
[00:32:51] клиентов сказала бы вот так вот
[00:32:54] человечек выглядит и вот с такой
[00:32:57] точностью мы прогнозируем и воевать или
[00:32:58] потом показала бы вообще метрику в
[00:33:00] принципе мы ошибаемся
[00:33:04] супер супер суши отлично думаю больше
[00:33:08] вопросов я тебе задавать не буду в
[00:33:11] рамках такого короткого эмаль дизайна
[00:33:14] зачастую мазай на самом деле длиться
[00:33:16] дольше
[00:33:18] но в целом у
[00:33:20] нас было вот это как раз полчасика за
[00:33:24] полчасика ты рассказал как решал эту
[00:33:27] задачу целом неплохо давай поговорим про
[00:33:31] про что-то больше хочешь чтобы мы
[00:33:33] поговорили про от adsense сейчас и потом
[00:33:36] питон работа странными и nameless
[00:33:40] наверное сразу пока мы разговариваем
[00:33:42] потом откроем уже
[00:33:43] хорошо давай давай давай скинемся точно
[00:33:47] не просто сейчас принципе начали
[00:33:48] продается
[00:33:49] да дам тебе вопрос конечно конечно
[00:33:54] конечно есть у меня есть вопросы по
[00:33:57] метрикам
[00:33:58] честно-честно для меня одну и в рамках
[00:34:01] вот такой быстро обратной связи
[00:34:04] для меня несколько странного ты говоришь
[00:34:06] про то что могут быть сильно на марии и
[00:34:09] при этом за минуты
[00:34:12] первое что ты предложил и это mc
[00:34:15] соответственно давай-ка вспомним
[00:34:18] как она сама съел ее проблемы с
[00:34:22] выбросами да как раз и я поэтому и
[00:34:25] подумала что нежить аномалии мне же
[00:34:27] дважды их учитывается я подумал
[00:34:30] использовать к я его съем который очень
[00:34:31] сильно
[00:34:32] не штрафует занимали в принципе как не
[00:34:37] надо делать потому что я буду скакать во
[00:34:40] время хорошо очень плохо оцениваете
[00:34:43] мышьяка раз потому что на выбросах будут
[00:34:45] неадекватно изучение метрики
[00:34:48] и выбросили бы надо удалять очень и
[00:34:51] смотреть на них вообще считать и на
[00:34:52] стену в принципе мы все тут вообще плохо
[00:34:54] потому что мне важно наверное и какую
[00:34:57] сторону мы дальше боится и как я сказала
[00:35:00] [музыка]
[00:35:01] что бизнеса будет очень сложно
[00:35:03] показывать у нас я тут в общем вообще
[00:35:05] нет достоинства использовать я домой что
[00:35:08] бизнеса надо знаете знак
[00:35:10] того когда мы ошибаемся я считаю и
[00:35:14] кажется что когда мы считаем деньги тут
[00:35:17] важнее
[00:35:19] проценты на которые мы ошибаемся
[00:35:22] для конкретного человека что люди разные
[00:35:24] и у них могут быть очень разные
[00:35:29] ну короче денежки которые мы с ним
[00:35:31] получаем они могут варьировать очень
[00:35:33] сильно кого-то за 100 рублей с кого это
[00:35:36] 100000 рублей и какая-то средняя ошибка
[00:35:40] [музыка]
[00:35:43] тысяч рублей она для них
[00:35:45] очень разные этих линий поэтому мы
[00:35:48] гораздо лучше использовать какие-то
[00:35:51] метрики которые все-таки относительные
[00:35:53] считают
[00:35:54] тушенка хорошо дальше ты говорила про
[00:35:58] несимметричные метрики можно привести
[00:36:00] пару примеров
[00:36:01] то как это работает и
[00:36:04] в идеале
[00:36:06] затем в каких моделях это используются
[00:36:11] вопрос на котла
[00:36:15] не обмен на самом деле знаю метрику
[00:36:18] который
[00:36:21] от мерный кванта голос я не уверена я
[00:36:24] знаю что она выглядит как у нас есть два
[00:36:26] интервала если у вас нету прогноз то у
[00:36:27] нас
[00:36:29] угол наклона альфа если у нас
[00:36:32] перепрыгнул что долго на колонке единица
[00:36:34] минус альфа и наборы можем мы просто
[00:36:37] варьирует угол наклона
[00:36:39] отклонения и здесь не стать его знака а
[00:36:43] вот ну собственно плюсы этой метрики как
[00:36:46] раз в том когда нам супер важно куда мы
[00:36:49] идем в спросе часто наверно используется
[00:36:56] из модели с просто короче когда у нас
[00:36:59] есть или логистики что нам нужно довести
[00:37:01] определенное количество товара если у
[00:37:02] нас не будет этого товара мы будем
[00:37:04] потерять деньги нам нужно довести в
[00:37:06] идеале чуть чуть больше чем нужно и
[00:37:10] тогда модель будет хорошо справляться со
[00:37:12] своей задачей для бизнеса вольт ну
[00:37:17] кажется что
[00:37:17] [музыка]
[00:37:19] в принципе мы можем мы можем свою
[00:37:22] метрику задать как угодно я считаю я вот
[00:37:25] эти коэффициенты можем просто
[00:37:29] на варьировать но смысле они виду что
[00:37:32] эта метрика это как бы вот эти
[00:37:34] несимметричные метрики наверное они
[00:37:37] важны на последней стадии оценке модели
[00:37:41] за что-то свое придумывать
[00:37:44] вот интересно
[00:37:48] какой угодно ветврач ну честно говоря я
[00:37:52] очень интересная идея но давай поговорим
[00:37:54] про хватаю вот ты и собственно у
[00:37:59] больного да ты немного про то что мы там
[00:38:03] по разным штрафом в зависимость разогнан
[00:38:05] до
[00:38:06] можешь привести в чем проблема вот этого
[00:38:10] колонтаево вас видеть и это не что иное
[00:38:12] как мая и
[00:38:15] вот в чем в чем проблема
[00:38:20] может быть почти правильный ответ
[00:38:23] неправильный вопрос может быть что в ней
[00:38:27] такого интересного в этой
[00:38:30] это медики
[00:38:32] в этом 8
[00:38:36] поведи не могли ему
[00:38:38] еще раз поведение в ее ну там перегиб на
[00:38:42] в принципе с этим вроде как можно
[00:38:43] бороться
[00:38:44] расскажи поподробнее шедшего ну ну что
[00:38:50] такого плохого в 0 происходит но не
[00:38:53] дифференцируема эмулировать как потому
[00:38:55] что перегиб и у нас мыли выкладки . вы
[00:38:59] произвольным и мы не сможем ее
[00:39:02] использовать вот как есть но я точно
[00:39:04] знаю что
[00:39:05] можно как не помнить таким методом
[00:39:07] сделать
[00:39:08] может наверное можно было бы прекратить
[00:39:12] ниже и убиралась которая
[00:39:16] кусочно замена
[00:39:19] и она задана как раз в 0 и она задана
[00:39:22] квадратичной функции там нет никакого
[00:39:23] перегиба нет никакого кого и там
[00:39:26] производной есть и как раз юбер воз она
[00:39:29] хорошо там перестает скакать до боли при
[00:39:32] обучении для ее плюс и при этом не
[00:39:35] переобучаться на выбросы я не видела
[00:39:38] чтобы quando i lose как-то так делали
[00:39:41] невозможно можно пороге сверло сделать
[00:39:45] какой-то
[00:39:46] кусок который будет заднем квадратично
[00:39:49] и потом будут хвосты с различными
[00:39:51] наклонами куда
[00:39:53] развесила дожди раз ты не видел и
[00:39:56] отдавая себе реальный пример и то
[00:39:59] [музыка]
[00:40:01] есть прям отдельная тема с тем как
[00:40:04] работает и
[00:40:06] just регрессор
[00:40:10] и про то что в игре саре нету по дефолту
[00:40:15] панталасса по крайней мере какое-то
[00:40:17] долгое время его не было по дефолту но
[00:40:20] была там реализация которая позволяла
[00:40:23] делать
[00:40:24] значит
[00:40:26] отсюда мы переходим
[00:40:28] к следующей теме да вот мы поговорим
[00:40:32] немножко про метрики давая поговорим про
[00:40:33] регрессоры и конкретно гридин кастинг
[00:40:36] регресс да вот как именно он работает
[00:40:41] вообще как ты можешь начать с того как
[00:40:44] регрессор работает точнее как деревянный
[00:40:48] регрессор работает затем как предельный
[00:40:52] busting регрессор работает и затем в чем
[00:40:55] же там прикол почему квантов вас им было
[00:40:58] сложно
[00:40:59] мотивы же я дойду мы может быть и не
[00:41:02] найду
[00:41:03] даже деревянный регрессор ну ты меньше
[00:41:06] как строится дерево решение как вы
[00:41:08] делали графе
[00:41:11] нови-саде деревья решений они делают и
[00:41:13] классификацию играет и репрессию решает
[00:41:16] задачу принципе аналогично мы пытаемся
[00:41:20] выбрать самое оптимальное разбиение при
[00:41:23] котором получаем там не больше падением
[00:41:25] берпи или прирост информации в узлах
[00:41:27] наберем состоянии
[00:41:31] соединенная почву узла пытаемся делать
[00:41:34] сделать сплит
[00:41:36] обычного дерева и
[00:41:38] считаем ведь наши
[00:41:41] показатели того насколько
[00:41:44] зашумлен и данные насколько смешанные
[00:41:46] классы читаем в дочерних узлов и в
[00:41:49] родительском узле и считаем прирос нашей
[00:41:51] информации снижение энтропии вот и таким
[00:41:54] образом продолжаем пока не построено
[00:41:56] куда длинное огромное дерево по крайней
[00:41:58] не достигнем как при переустановке
[00:42:00] обычно там критерии установки может быть
[00:42:03] на длину дерево на количество листьев
[00:42:05] можно его строить сразу в глубину можно
[00:42:10] его строить идя по уровням то есть
[00:42:12] достраивать каждый уровень до конца
[00:42:14] потому спускаться еще на уровень ниже
[00:42:17] вольт можно
[00:42:20] останавливаться и не достраивать
[00:42:22] достигнув какой-то радость питаться
[00:42:24] выбрать не лучше стрип и потом
[00:42:28] сравнивать гейн который мы получаем от
[00:42:30] времени шенген с каким-то контентом
[00:42:32] значениями понимать что мы четко кто же
[00:42:34] тут слишком хорошо все поделили большого
[00:42:37] прироста не ты перестала делить это как
[00:42:40] что проник налитого
[00:42:44] хорошо подтверждено с регрессией как мы
[00:42:49] разделяем
[00:42:52] и считаем пускай там был учитель и
[00:42:54] регрессе регрессор у нас дереве какое-то
[00:42:58] не будут прям одинаковое значение
[00:43:01] какой-то проект переменный рез будет
[00:43:03] какой-то набор с распределение в каждом
[00:43:05] узле и
[00:43:08] мы берем там средние в этом узле
[00:43:11] назначение которое мы будем определить
[00:43:14] хорошо с какими проблемами можно
[00:43:16] столкнуться во время
[00:43:18] вот обрезка займа до момента
[00:43:22] использования до модели но он ограничен
[00:43:25] собственного из-за того что мы берем вот
[00:43:27] это среднее на границах интервалов
[00:43:29] которые были в обучающей выборке мы
[00:43:31] перестаем прогнозировать мы перестаем
[00:43:34] экстраполировать короче вовне
[00:43:37] обучающей выборке дело нужно
[00:43:40] спрогнозировать там 500 миллионов а
[00:43:41] максимум было 300 мы будем
[00:43:43] прогнозировать трясти
[00:43:44] хорошо и грузин boosting тряс
[00:43:48] garden бусин трисс это ансамбль над
[00:43:52] деревьями
[00:43:53] который не просто голосование деревья
[00:43:58] участвуют независимые каждое дерево до
[00:44:01] обучается на
[00:44:02] ошибки предыдущего таким образом мы
[00:44:05] делаем кредитный спуска деревья входят с
[00:44:09] какой-то следим коэффициентами короче
[00:44:13] это сумма функций
[00:44:17] конечная функция эта сумма наших функций
[00:44:20] которые дают каждое дерево с каким-то
[00:44:22] весов при этом там каждое последующее
[00:44:25] дерево мы учитываем все меньшим
[00:44:28] коэффициентом
[00:44:30] чтобы не скакать но это как с тем чтобы
[00:44:34] все таки сходиться куда-то несколько
[00:44:36] оттуда сюда
[00:44:38] хорошо сына ну как бы плюс в том что мы
[00:44:41] ансамбль используемый ни одно дерево
[00:44:45] или обучиться
[00:44:47] также как перевели к
[00:44:49] следующей вопросик это
[00:44:52] твой вопрос со звездочкой чем и джим
[00:44:56] русло gm и как просто отличается только
[00:44:58] другом
[00:45:00] большой
[00:45:03] вроде бы ну в общем то что я точно помню
[00:45:06] что это просто недавно как раз смотрела
[00:45:10] ты готовилась что
[00:45:13] во-первых can boost классно работает с
[00:45:15] печальными речами потому что у него
[00:45:17] сложная система кодирования древних
[00:45:20] учений и он сам как в этом суть это
[00:45:22] делает довольно сложным способом и
[00:45:25] делать это руками было бы принципе
[00:45:27] нереально и я считаю
[00:45:29] прости пожалуйста а что же там такого не
[00:45:31] реального делает смысле кодированию
[00:45:34] реальных печей когда там разбиение
[00:45:38] происходит на под выборках исход выборов
[00:45:42] ну то есть мне кажется что она манить
[00:45:44] обучение это довольно сложно было бы
[00:45:46] делать когда ты перри обучаешься много
[00:45:49] раз моделей на разных сэмплах там
[00:45:52] несколько раз выделяются различные
[00:45:55] сэмплы рисунки руются
[00:46:00] так хорошо
[00:46:02] и трудозатрат на обычную в общем с черт
[00:46:05] про различия можно предугадать
[00:46:07] вроде как вроде как они все используют
[00:46:11] англии 100 грамм на разделении бином
[00:46:13] вроде как тут отвлечение потому что или
[00:46:16] же boost тоже это использую
[00:46:18] отличие в том что их жабу стучится в
[00:46:21] ширину у дерева и точен и говорил при
[00:46:23] древе про способы обучения он учит по
[00:46:25] слоям
[00:46:27] light дбм учиться
[00:46:30] и этом вроде как можно проверить легче
[00:46:32] чуть-чуть потому что слой и можно там
[00:46:35] разойтись
[00:46:36] лдпм
[00:46:39] он учит как бы в глубину сначала человек
[00:46:44] узла
[00:46:46] как boost я естественно того как
[00:46:50] готовилась к этому совету я не знал
[00:46:52] этого факта вашей маме но это очень
[00:46:55] прикольно короче я узнала о такой
[00:46:57] классный вид штукой boost
[00:47:00] имеет множество каких-то плюсов
[00:47:03] производительности и в том как хранить
[00:47:06] модель том что нет вот этого перекоса
[00:47:09] что дерево может быть не понятно и не
[00:47:11] сбалансированы и на прогнозе буковски
[00:47:13] проблема со временем вычисления для
[00:47:15] каких-то объектов а для каких то все
[00:47:17] быстро работает потому что как boost
[00:47:19] использует я забыла слова котором
[00:47:21] обязательно это деревья
[00:47:23] симметричные и они используются то есть
[00:47:27] сплит одинаковые по всем узлам на каждом
[00:47:29] уровне это один сплит одинаковый
[00:47:32] и в принципе кажется что это идет
[00:47:36] вразрез с концепцией вообще решающего
[00:47:38] дерево но круто что это работает потому
[00:47:41] что насколько я понимаю решает некоторые
[00:47:43] проблемы
[00:47:45] с скоростью прогноза
[00:47:48] из хранение модель что не нужно хранить
[00:47:51] куча сплитов
[00:47:53] слушай что значит идет вразрез общем
[00:47:57] общие идеи построение дерева ну она идет
[00:48:00] разрез потому что ты в каждом узле
[00:48:02] например представим какую-то идеальную
[00:48:04] ситуацию в которой ты
[00:48:06] сделала разбиение у тебя там уже
[00:48:09] отсортированы объекты или то мне не
[00:48:12] нужно по какой-то фиче вот кричал один
[00:48:15] мы сделали первое разбиение на втором
[00:48:17] свою мы выбрали лучшие разбиение и все
[00:48:20] равно в каком-то узле мы может быть
[00:48:21] будем делать что-то лишнее будет
[00:48:23] неоптимальным
[00:48:26] на моменте построение дерева мы как бы
[00:48:29] выбираем в этом узле конкретно в данной
[00:48:31] точке лучше разбиение отпустит не
[00:48:34] происходит потому что мы рассматриваем
[00:48:36] все узлы и
[00:48:37] кажется что это лишнее операции как бы
[00:48:40] возможно
[00:48:42] но здесь нужно поспорить на самом деле
[00:48:45] можно поспорить потому что в зависимости
[00:48:47] от того но кажется что вот и найдя один
[00:48:52] сплит и достаточно быстро ты можешь
[00:48:54] поиск сплитов за параллели и тебя один
[00:48:58] раз его сделать и применить сразу на
[00:49:00] весь мир и типа идти дальше ты скорость
[00:49:03] построение дерева ношу ну да да я имею
[00:49:06] ввиду что вот как раз
[00:49:07] в дереве же в самом алгоритме просто
[00:49:10] немного другая идея довольно на каждый
[00:49:14] сплит ты прогоняешь именно для этого
[00:49:16] узла для конкретных объектов федоровский
[00:49:18] есть так не происходит но крыму что это
[00:49:21] работа потому что действительно
[00:49:22] насколько я понимаю берёт большой
[00:49:24] прирост производительности не за счет
[00:49:26] это
[00:49:28] какой ступени а еще там разные сейчас
[00:49:32] прости нас давай вот эту часть тоже
[00:49:35] закрылось ты молодец давай я перейду
[00:49:38] водка вопрос который задавал изначально
[00:49:41] то что
[00:49:43] ну вот ту же сказала что есть проблема с
[00:49:49] подсчетом производной в клиент для канта
[00:49:52] и лосса и
[00:49:55] теперь вопрос ну то есть ты рассказала
[00:49:58] про i just
[00:50:03] я тебе
[00:50:07] есть же градиент
[00:50:11] вот проблема с лоссов
[00:50:13] что же что же такого зачем нам нужны
[00:50:17] какие-то
[00:50:18] дифференцируемые внутри функции зачем и
[00:50:21] почему мы не можем использовать какие то
[00:50:24] другие
[00:50:27] там вообще в принципе
[00:50:29] [музыка]
[00:50:31] мышь как таковой градиенты не считаю
[00:50:33] пусть инге мы считаем ошибку вычитаю ну
[00:50:37] как бы
[00:50:41] предельно мне важно что не будет
[00:50:42] существовать произвольным и сингер я
[00:50:45] возможно ещё что-то ужасно говоря это
[00:50:47] касава не поняла
[00:50:49] но кажется что там бусин зэк но он как
[00:50:52] бы над ошибкой пункте функционала
[00:50:55] качества как мы считаем 2 функционала
[00:50:58] качество если нам типа ошибки нету
[00:51:01] там и этот объект просто можем
[00:51:04] не брать там выборку лично что это такое
[00:51:07] наверное это не супер важный
[00:51:09] мне так сейчас кажется потому что мы
[00:51:12] считаем
[00:51:14] качество не знаю мэй пмс она мы считаем
[00:51:18] что когда и лозы хорошо бы что река want
[00:51:20] to yes no какого-то объекта там 0 и не
[00:51:24] вижу что тоже на градиент для этого
[00:51:27] они уже верны предсказаны мы можем не
[00:51:30] брать его последующего следующие дерева
[00:51:32] и все
[00:51:33] они же подстраиваются то есть мы
[00:51:35] отбираем объекты которые имеют большие
[00:51:37] градиент это большие ошибки
[00:51:40] допустим кому каждое дерево выбираем
[00:51:42] объекты которые имеют большой ошибки но
[00:51:45] вообще градиенты и их забираем следующие
[00:51:48] дерево чтобы пытаться обучиться на этих
[00:51:50] ошибках на этих именно объектах и
[00:51:52] объектах которых нет общие ошибки
[00:51:56] можно их вообще не брать
[00:52:00] можно их братья на в каком-то
[00:52:02] соотношение но я не вижу как они могут
[00:52:04] все сломать часть моря
[00:52:06] хорошо давай я тебе задам вопрос
[00:52:08] по-другому
[00:52:10] выпусти именно в капусте есть своя
[00:52:15] особенность стильного сами которые можно
[00:52:17] использовать в пасти почему используются
[00:52:20] вот именно такие волосы
[00:52:23] они другие
[00:52:26] м сильная подсказка я знаю только что
[00:52:29] это boost или как
[00:52:32] у меня сериале регуляризации были
[00:52:35] мне кажется это никак не связано не
[00:52:38] очень-то больше не могут вспомнить
[00:52:39] лечить зубы статусами можешь
[00:52:43] хорошо окей окей
[00:52:46] давай тогда поговорим про регуляризации
[00:52:49] в ну раз уж ты вспомнил регуляризация вы
[00:52:53] даже будет 100 в посте в лакеями в
[00:52:56] капусте что как это вообще работает
[00:53:01] но у нас есть 102 как обычно
[00:53:06] доставай найди нормы и плюс есть еще
[00:53:11] а там член который будет считать
[00:53:13] количество
[00:53:14] листьев например
[00:53:18] угости то
[00:53:19] же одна сложность моделях сути тоже его
[00:53:21] можно использовать как
[00:53:23] функция народа канал для регуляризации
[00:53:29] но релизе 02 как обычно есть леса это
[00:53:32] скорее в каких-то листьев если каждого
[00:53:35] объекта есть скоро мы можем посчитать
[00:53:39] [музыка]
[00:53:40] квадрата суммы квадратов или
[00:53:42] комсомольского
[00:53:45] хорошо
[00:53:47] простой вопрос как l1 l2 регуляризации
[00:53:49] работают
[00:53:51] что они делают с весами
[00:53:54] или один
[00:53:56] это не квадратичная форма это линейная
[00:53:59] то есть an issue мансов она может
[00:54:02] длительным весах которые не важны или
[00:54:05] если они коллинеарны очень если не важны
[00:54:07] а если у нас есть
[00:54:09] зависимые переменные
[00:54:15] здесь очень переменная году из них
[00:54:17] заземляют струю используют с каким-то
[00:54:19] весов
[00:54:20] за счет формы от этого функционала
[00:54:25] люди мы добиваемся и на зануление ан-2
[00:54:27] просто уменьшают весам не дает им расти
[00:54:30] бесконечно
[00:54:32] хорошо смотреть какие что еще интересно
[00:54:36] регуляризации которые ты знаешь
[00:54:39] нет
[00:54:42] суши знаешь ли здесь еще ты можешь мне
[00:54:45] рассказать
[00:54:46] слушай но так как норм много
[00:54:49] типа л1 и л2 это нормы и ты можешь
[00:54:53] представить любую норму и
[00:54:56] соответственно на
[00:54:58] по-разному будет штрафовать
[00:55:02] такое и типа можно задать эту норму да
[00:55:05] конечно да погас типа можно в модельку
[00:55:08] передать не самописный можно передать и
[00:55:10] мин функционал норма ну
[00:55:14] придется залезть под капот но в целом
[00:55:16] дальнем не занят на маме хорошо слушай
[00:55:20] наверное единственное чем мы с тобой
[00:55:22] говорили то есть мы говорили про метрики
[00:55:26] поговорили про
[00:55:27] эти модельки
[00:55:30] где-то
[00:55:35] наверное хотелось бы поговорить с тобой
[00:55:37] о вещь которые не так часто спрашивают
[00:55:41] нас о бесах это
[00:55:45] работа с понижением
[00:55:48] размерность
[00:55:50] вот какие подход понижения размерности
[00:55:52] что знаешь
[00:55:55] ты к этому не готовилась я просто ну как
[00:56:00] я знаю страны имеют понижения
[00:56:02] размерности потому что с этим было
[00:56:03] связано моя
[00:56:04] [музыка]
[00:56:05] работа над кандидатской диссертации что
[00:56:09] ты забыла завален пойду это тот образ
[00:56:19] возможно я в заднице мне помог
[00:56:23] нет на самом деле я не уверен как бы я
[00:56:27] занималась этим только вот тогда научном
[00:56:31] сообществе возможно это немного смешно
[00:56:34] от того что желают у саши на
[00:56:36] исследования но я расскажу знаю
[00:56:40] там есть области которых у нас очень
[00:56:43] [музыка]
[00:56:45] высоко высоко размерность признаков
[00:56:48] который мы хотим пользоваться иногда я
[00:56:49] тушу иногда они там и примерные нужно
[00:56:54] очень много усилий битва приложить для
[00:56:56] того чтобы каким то образом выделить
[00:56:59] важные это не хочется терять что-то еще
[00:57:02] и по сути методы которые делают проекции
[00:57:06] сильно могут помочь например там самый
[00:57:09] простой записи и построить смотреть
[00:57:12] какой процент информации и сей описывает
[00:57:15] способны объяснить выбрать какое-то
[00:57:18] количество главный компонент
[00:57:22] можно использовать мой любимый мёд все
[00:57:27] время несущихся карт кохонена на то же
[00:57:29] место появление пространство такая
[00:57:32] простая не еронко
[00:57:34] она помогает скорее для визуализации для
[00:57:39] того чтобы построить какие-то сложные
[00:57:41] визуализации
[00:57:42] многомерном пространстве есть это я не
[00:57:44] только метод для того чтобы новые фичи
[00:57:46] получить кстати классный способ не
[00:57:48] только заменить свое большое
[00:57:50] пространство какими-то вещами совсем а
[00:57:55] может быть можно дополнить посмотреть
[00:57:57] что там будет skynet ностью
[00:57:59] конечно независимо будут потому что
[00:58:03] может быть можно перейти там квадратуру
[00:58:05] короче по генерит фичей способ на
[00:58:07] генерить новые фичи верных
[00:58:10] зависимые говорю через него вопрос это
[00:58:14] не буду зависим потом выбрать что работы
[00:58:17] тут вот или это классно способ для того
[00:58:21] чтобы сделать какие-то
[00:58:23] консультации по нижнему пространства или
[00:58:27] визуализировать если мы снижаемся до
[00:58:30] двумерного трехмерного пространства
[00:58:36] cher
[00:58:37] еще какие методы
[00:58:41] но
[00:58:44] любые методы и это по сути
[00:58:49] главные компоненты ну короче ты можно
[00:58:51] задавать какие-то
[00:58:54] нетривиальной поверхности не плоскости и
[00:58:57] на них тоже проектировать
[00:59:02] а где это из пользуется тебе много
[00:59:05] власти есть такое есть такой подход ну я
[00:59:08] читала про это статьи исключительно вот
[00:59:11] моей научной области потому что они были
[00:59:13] коллеги которые
[00:59:14] курировались они работали писали свой
[00:59:18] песни в критике
[00:59:20] где генерал под по графику мы и
[00:59:25] одни использовали названием или фолд
[00:59:29] универсальный mifold и который
[00:59:32] проецировали но по сути это просто
[00:59:34] проекция на подбираемые
[00:59:37] подбираю мою сложную поверхность
[00:59:40] конь-огонь
[00:59:42] хорошо слушай ну
[00:59:44] ты хочешь сказать но здесь не вспомнить
[00:59:50] ничего про понижению
[00:59:53] честно говоря самое первое что приходит
[00:59:55] на ум вот вот прям но если я отвечаю я
[00:59:59] бы сказала ну естественно
[01:00:02] мы с помощью не день нужен просто
[01:00:06] зафигачить большую часть признаков
[01:00:08] оставить те которые реально что то
[01:00:10] значит у яндекса не сводится подожди они
[01:00:12] сходятся ли это по сути практически и
[01:00:14] миссией у
[01:00:16] типа главный компонент утвержденных
[01:00:19] монетами знаешь думу по сути своей зоны
[01:00:23] зрения что это ли но дело в том что чаще
[01:00:27] чем дожди здесь есть очень важный момент
[01:00:29] что когда я использовать интриг
[01:00:31] утилизации у меня остаются признаки
[01:00:33] полностью интерпретируемые
[01:00:41] ты сохраняешь большую
[01:00:44] сохранять получалось но в целом как бы
[01:00:49] когда мы говорим про pesel мы говорим
[01:00:51] про то что вот так хранить информацию
[01:00:53] как вы сохраните форма
[01:00:56] дисперсии до
[01:00:58] значений то есть их разлет какую еще
[01:01:04] информацию интересно было бы сохранен на
[01:01:06] самом деле вот отношение между двумя
[01:01:09] точками в 1 раз представим себе что у
[01:01:11] нас был какой-то по огромным
[01:01:12] пространствам хотела что я 300 я не
[01:01:15] сохраняются чтобы отрезок больше чем
[01:01:18] меньше отрезок да собственно вот снг
[01:01:22] подход он не блин да ну она наверное
[01:01:26] самый интересный самый крутой а вообще
[01:01:30] когда-то давно когда я был молод и юм я
[01:01:35] помню как я пришел на
[01:01:38] выступление ведь и ермакова короче и
[01:01:42] пить я тогда уже был я только-только
[01:01:44] стал один ли дом опять уже был тем рядов
[01:01:47] знать что он рассказывал про юнеп и
[01:01:50] и в представлении вообще очень
[01:01:53] интересный фильм
[01:01:57] рассказывает еда
[01:02:01] представляешь насколько сильно вот вам
[01:02:03] не вот осталось это что
[01:02:07] настолько клёвый настолько интересно
[01:02:10] было там по сути своей тоже идет
[01:02:12] сохранение но даже перевод в какое-то
[01:02:15] другое пространство не интерпретировано
[01:02:16] и но идет сохранение вот как раз
[01:02:18] отношений и за счет этого можно иногда
[01:02:21] очень интересные картинки получать и
[01:02:24] я пробовал в кластеризация пользователей
[01:02:29] можно было увидеть как одна группа
[01:02:31] пользователей которые смотрят один
[01:02:33] контент есть группа пользователей
[01:02:34] которые смотреть несколько контентов
[01:02:36] есть группа пользователей которые другой
[01:02:39] контент и вот есть такая вот ручеек
[01:02:42] между одним облаком людей
[01:02:45] которые смотрят один контент другое
[01:02:48] облако людей которые смотрят другой
[01:02:50] контент на есть ручью которую типа между
[01:02:52] ними что вот этого пользователя которые
[01:02:55] смотрели этот рукой карта
[01:02:56] честно очень интересное представление
[01:02:59] очень такое нестандартные прикольные и
[01:03:03] ну красиво красивой и даже интерпретирую
[01:03:07] за счет того что ты прям видишь то что
[01:03:09] вот эти вот люди на самом деле вот эти
[01:03:11] два облака они близки друг другу за счет
[01:03:14] того что есть этот вот связь реальных
[01:03:16] пользователей которые смотрели то есть
[01:03:18] это похоже и контент и но условно похожа
[01:03:21] да и можно пробовать делать
[01:03:24] перенос контента то есть одним людям
[01:03:27] предлагать посмотреть этот контента этим
[01:03:29] людям предлагать посмотрите контент то
[01:03:33] есть даже с этой вещью можем придумать
[01:03:35] какое-то применение вот это очень
[01:03:39] интересно каждого и ночную заберу
[01:03:51] сердечко там сердечки
[01:04:00] это уж больно да нет
[01:04:05] ну ладно
[01:04:07] бульоне уводит

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
Write JSON only to: splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. data-scientist-middle-karpov-ml-2022-06-26.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.json \
    --video transcripts/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.json --out splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.qa-split.json \
    --video transcripts/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.validation-report.md

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
video.md: /Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/video.md

--- CHAPTER `00:05:09` — Вопрос по ML-дизайну ---
window: 00:05:09 .. 00:06:09
recognition_status: single (1 items)

ITEM #1
  interviewer_question: time=00:05:09 text='начнем с дизайна если ты непротив задачу я дам ту которую меня одна компания не так давно в собеседованиях вот задача про он тебе и предсказанием тебе интересно то что я честно говоря не очень хорошо снова как решается такая задача но то есть я что-то слышу и видел с опытом знал что такую задачу в целом решает множество различных компаний вот но для себя решил что постараюсь сделать какое-то интересное решение предложить какое-то интересное решение и подсказать что это будет в общем он тебе важно то это lcd мы предсказываем тебе это like them were на всякий случай для тех людей кто не знает что это такое а тебе это лифтинга по сути своей оценка пользователя с точки зрения того сколько денег он может принести к нам в будущем это всегда farkas на будущее очень часто вот горизонт вот этого предсказания он такие тем или иным образом ограничивается но в нашем случае это ограничение будет на полгода вперед то есть мы заранее забиваемся на то что мы считаем активе центре горизонт прогнозирования полгода сперва и что то что прогнозировать дальше чем полугода мне вообще не нужно нет не нужно но ты должна понимать что есть свои нюансы в том что ты прогноз штангу год вперед условно ну давай возьмем сентябре прошлого года и вот мама ее лишнего года мы живем в парадигме что есть anomaly сейчас мы живем в парадигме что есть мир который изменяется начнем с это хорошо мир который леди меняется и мы пытаемся спрогнозировать нужно ли нам посчитать и lateview с учетом в пол года максимально границ полгода сейчас сегодня и зафиксировать его пусть на этом и у тебя будет принят какие-то решения сейчас очень важные или можем пересчитывать и активе хотите по каждый день и смотреть как она меняется для каждого клиента ну по сути это вопрос про душ самой аномалию какой-то который может произойти или любые другие какие-то факторы промо нагрузках какое-то возросла и мы стали больше получать клиентов что-то в короче могу ли я пересчитывать или я буду считать метрику типа важно ли как-то попытаться границы оптимистичные и пессимистичные на берегу давай так да на основе твоего прогноза бизнес будет принимать какие-то решения в том числе стоит ли с этим человеком продолжать работать или не стоит то есть использовать его в коммуникации не используйте так далее то есть я должна понимать что твой прогноз он естественно существенно влияет на бизнес и на все остальное как именно это будешь считать различные варианты сценариев наверное я хотел бы чтобы ты рассказала об этом поподробнее'
  candidate_answer: time=00:09:02 text='сделаю предположение очень во-первых мы 71 его просьбу крюшо что и у тебя будет ли у меня граница маккейна есть то есть мы точно знаем что пол года ограниченный и какой бизнес кстати что еще раз это контрактный бизнес когда у нас есть там подписки есть точный флаг того что там клиент ушел или это покупки какой-то retail где мы точно не знаем куплен с нами до сих пор или нет это все тех это фильм тех это значит то что нам нужно чтобы человек он занимается допустим покупкой продажи акций или валюты какой-то или криптовалюту какой-то и так далее то есть короче нигде так де сак у нас никому просто двумя какие-то действия и нам нужно самим принимать решения там ушел эмили еще нет ну во первых то есть тут у нас встает вопрос сколько человек будет приносить денег и сколько он будет жить из-за тех двух факторов мы можем управлять прогнозировать all these это как не очень довольна смотришь в общем если что останавливаю не визаране поэтому есть короче я собственно вы кстати когда работал и не с тобой как времени я снимала с тем что работала с оттоком предлагала бы и знаем какие то алгоритмы для идентификации людей которые обтекают не там в принципе не плохо себя вели такие простые штуки как rfm анализ достичь ее на ресницы frequency переменных можно с помощью распределений учить распределение чтобы понять остается человек с нами грубо говоря прогнозировать вероятность того что человек сюжет покупку какой-то брюс жутко ремни в принципе ну а на моём такому описи когда работает просто был ритейл что похоже по модели поэтому и спрашиваю если нас подписка елена нужно оценивать мне кажется довольно удачная штука для того чтобы использовать выхода этих алгоритмов статистических я дальнейшего прогноза короче статистический алгоритм они во-первых умеют и прогнозировать на самом деле eu te vi но может право делать что-то сложное мой ответ что я бы попробовала применить известный меня библиотека это рисовала книги и она довольно простая не нагружает из там нет какой беды и с производительностью и но непростой подходят которые хорошо интерпретируется предам там есть свои проблемы и логика довольно просто поэтому наверное возможно потом бизнес захотела бы что-то более сложное вот поэтому короче за быть моим берем какие-то а мы и хотим тесто проводить как-то развивать мы сразу хотим пришлось сделать давай так в рамках и молиться зайна предполагается что ты ответишь на там несколько ключевых вопросов хотелось бы знать что ты вот в руках моризо нереально на них ответишь каких-либо ничего set короче если бы делала я я бы предложила 1 быть line модель то есть хотя бы хоть как-то прогнозировать и вины не показать какие-то метрики и обсудить с бизнесом достаточно ли это качество прогноза или рамки в которых она прогнозирует они слишком широкий для них и мы на этом точно не останавливаются ни какие песни у пилота и ни во что не идем хотя тут пилотировать довольно сложно скорее всего на потому что с период полугода скорее и вот в полгода не будет и я бы вы лидера валось просто на отложенных тайские валидации показывал бы бизнесом результаты отважные выборки то есть дети потом несколько раз казино что это все воспроизводится то есть одни полугода к полугоду со смещениями с окнами модели примерный знак ушек клик вот какую ошибку но поскольку у нас а у тебя какая метрику лиц это важно ли нам короче бизнес я бы узнал у бизнеса важно ли им что лучше перепроверь и прогнозировать или нет и прогнозировать дает ли бизнес не ответный выброс но скорее всего нет а прогноз не до прогноз лучше да но не хочется быть совсем оптимистичной окей тогда можно попробовать какие-то метрики и мы сне нет можно попробовать и более сложные как раз и несимметричный не только который ты очень любишь разный коэффициент на пире прогнозами до продлевать принципе все можно начать считать и если бизнес настаивает что у него приоритеты кто что ему важнее то можно использовать начнут речную просто с различным углом наклона штрафа с зависимости от знака в общем ошибки так но я запишу себе наверно будет то думает что у тиражные выбросы я прям буду смотреть на конкретную клиенту часто или я будет смотреть в сумах чаще и конкретного клиента ну вообще это тебе прогноз нужно сделать для каждого клиента ну давай я буду читать его съел я для себя решил с этим из всех в качестве и буду варьироваться на ней так я покажу ну собственно вот больную горит мы идем к бизнесу показываемся метрики объясняем что за метрика что она читает и наверное даже ним и съела нужно брать rms я потому что бизнес будет сложно оценить квадратах наклонения лучше наверное показывать тех значения которые ну короче понятнее никотине квадраты корни должны рынок долях было бы понять некий процент наверняка не на цены чтобы они видели а не конкретные значения все-таки мирные процентов не было бы так удобно показан в процентов ошибку так поэтому в общем если я бизнес не устраивает и мы не хотим а это использовать google и катить пока что мы видим что это более сложно это я бы сюда привлекала какую-то дополнительную информацию клиенту который меня есть об истории того что они делали потому что эти алгоритмы листиках они знают только recency frequency то есть по сути это время жизни клиент этому время его жизни сейчас сколько покупок он совершал не там время с последней покупки это довольно мало данных хотя практика показывает просто хорошо описывает таких моделях но давайте добавляете тогда любой информации клиента который у нас есть например с какими если ты финн тех начну покупает акции и придает белью на скорее всего есть какие-то категории акции ну компании с которыми он взаимодействует можно построить какой-то профиль клиента в зависимости от того какие операции он совершал на какие суммы он что-то делал но правильным сумок операции его есть сектор компании навернео браво не стоит наверное брать компании конкретный построить брайтон энергетика дайте еще что то какие то большие сектора причем наверно стоит побить возможности по государством или там как-то пока мастером государство вкладывает если вы что-то российской рассматриваем вернет большая разница укладывается российский эти компании или зарубежный анти сектор вот научно собрать профи клиента для того чтобы использовать какой-то другой модели в модели возможно это можно назвать моделью типа второго уровня если мы пишем небольшой подходит из поединком прозван горит мы получаем от туда и печенье из ресницы frequency в этот анализ дает нам там эффектов или не язык на самом деле они могут и тени прочитать можно идти некуда запихнуть что эти алгоритмы могут дать можем использовать в качестве печей для алгоритма второго уровня и туда же добавить фичи клиента и сделал такой и как болгария если хочешь к спросить какую модель втором уровне skillet например если мне нужно прогнозировать или тени ну я бы честно говоря но поскольку я могу посчитать так время прогнозное время жизни этого клиента мне уже как бы тоже не нужны никакие день мериды потому что у меня уже есть как бы прогнозы вот сколько он проживет я бы взяла просто какой-нибудь busting например который будет а если мне меня важно интерпретируем верно первых этапах до важно будет ну а затем пожара но затем можно глупым после какого-то там условно после какой-то итерации можем переходить на таки интерпретируем модели долго вообще нас конечно нет на самом деле есть я все равно хотела сказать что я бы наверное для себя ямасиро в первую очередь попробовал и ну я посмотрел сколько фичей получается конечно если не очень много то можно было бы попробовать каким-то линейными алгоритмами чтобы было интерпретируем как раз но если много печей и непонятного как они должны влиять я бы наверное все равно попробовал бы сделать гусь тенге посмотрела бы что получается короче я буду водила gustin гамме модель для того чтобы была минимальной ошибка смотрел об этом глазами чего получается и потом уже если вы не сказали два интерпретировать я бы уже прибегла к методам специальный интернет sender внутри можно было бы попробовать линейку чтобы оно было сразу петером и но ну такой первый подход из линейка прокатило вы хорошо на ней божественное здесь мы сравнили бы с бусинками получается или прирост качества если просто качество нет то осваивались на линейке это проще объяснять и не посчитать вот если бусин дает сильный лучше результаты там сколько больше возможностей всего так и будет то хотя хочу заметить что у меня есть переменные которые скорее всего очень сильные предиктор или много шума у переменной хороший предикторы имею ввиду это переменные выходы статистических вот этих моделях скорее всего не очень сильно будет коррелировать с метр переменной поэтому возможно линейка здесь правда было бы хорошо какой-то маленький лес имели бы экичи клиента и кстати о макроэкономические фичи тоже можно было бы добавить это я про это не сказал а но я перебывает валюту и сейчас добавляю какие-нибудь я бы попробовал добавить какие-нибудь мы же взять информация компания сто процентов есть какая-то аналитика по рынку и наверное хранится и легко было бы достать даже внутри компании своих данных какой-то ситуацию на рынке там курсы какие-то индексы и не очень хорошо разбирающихся в тени и скорее всего есть какие-то индексы в экономике индустрии что-нибудь такое человек скорее всего была бы к его использовать это было погрозила насколько в общем люди он вообще привлекательно основе сейчас работать если там что падает мирное людям тоже не очень интересно так я из-за данный вопрос как бы я интерпретировал модель которые они не рекрутируются давай так не совсем так я задавал вопрос какие способы интерпретации есть но давай сейчас ты закончила ответы и мы уже переходим к вопросам или есть еще что-то что-то не покрыла в рамках мы редизайн и хочешь сказать о какой-то блок так на смотри очень сейчас я пытаюсь подытожить ничего ли не забыла за одну я смотрю что у нее с по данным как долго у меня в принципе живут клиенты и полгода короче если честно я бы первые да если мне сказали точно полгода прогнозирую его я бы все-таки попробую проверить так часто клиенты уходят на полгода потом возвращаются что это такое что это нормальный нормальная границы для как назвать и если клиент полгода не возвращается что он правду шел что такое был бы определить вроде тем я бы перешла к подготовке печей для статистических моделей посчитала бы ими 75 показатели они это умеют и ути мечтать и отток считать до сикст iv не актив на какую-то дату довольно большой горизонт наверное я бы посчитала для входа во второй алгоритм возможно стоило бы посчитать не на горизонт полгода она несколько горизонтах прогнать этих алгоритмов но там из мультика нервности надо было поработать чем возможно это хорошая идея возможно не очень но это можно проверить по ходу нужно сгенерировать как готов побороться с чем-то плохим так далее делаю первые вот эти алгоритмы с над моделью до обогащаю их выходы печами клиента печальные макроэкономическими запускаю это все в линейку запускаю бусинки смотрю что там кофе чтим возможно иногда кит убирать смотрю приемлемыми для метрики вы лидирую с бизнесом что эмболизацию модельные истории проходят вот так достаточно ли это для вас метрика или нет если дают зелёный светофор грубо говоря то все это допиливает не делаем ансамбль нормальный и если надо интерпретацию этот дойдем интерпретацию хорошо'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:25:07 text='давай вопросы например мы говорили правил'
  question_topic: ML

--- CHAPTER `00:25:14` — Какие могут возникнуть проблемы при планировании LTV на полгода вперед? ---
window: 00:25:14 .. 00:26:59
recognition_status: single (1 items)

ITEM #2
  interviewer_question: time=00:25:14 text='мы еще очень плотно будем говорить про метрики позже давай так и я вот для себя понял что скорее всего мы посвятим эта работа с этим метрикам ds часть давай поговорю пробовала друга и с какими проблемами ты можешь возник столкнуться во время прогноз на полгода вперед l2 для людей'
  candidate_answer: time=00:25:41 text='ну собственно проблемы которые мы с тобой в первую очередь обсуждали проблему китай аномалии и непонятных скачков которые в обучении модель их не было и какойте сезонности что такое даже не сезонность полгода это вообще такая это даже неполный год нужен я думаю что проблема сезонности от самый простой что можно решить проблему какой-то резкой аномалии нерешаемой на nintendo леру я не считаю поэтому это только объяснить заказчику что если что-то произойдет то нам нужно будет быстренько быть перестроить модели пересчитать это с учетом есть грубо говоря дуальном или и мы пользуемся результатами например три месяца у нас было пасторе модели а потом мы делаем перерасчет с учетом этой аномалии смотрим насколько мы ошибаемся туда куда вы нас смещение идет если она всех пользователей например мы видим смещение этого не до прогноз и принес то перестроить модель . обновите и там для последующего уже расчет используем новому да хорошо давай еще один наводящий вопрос'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `00:26:59` — Как делать прогноз для новых пользователей? ---
window: 00:26:59 .. 00:28:54
recognition_status: single (1 items)

ITEM #3
  interviewer_question: time=00:27:02 text='хорошо давай еще один наводящий вопрос что будет с новым пользователем кажется что feed которые ты перечислял это вольно для людей с которыми ты долго а для новых пользователей как-то деле будешь делать прогноз у нас есть какие-то анкетные данные есть какие-либо пол возраст ну допустим есть какой-то создаем есть даже возможно там стоишь зачастую в таких приложениях есть и trial периоды когда людей учат чему-то предлагают пройти обучение у тебя какой-то опыт с ним опыт'
  candidate_answer: time=00:27:49 text='есть какие то данные по поводу того как человек проходил обучение ну если у нас есть какой-то период обучения или правил период это клёво потому что оттуда можно все-таки какие-то паторны поведение например там насколько и рисковыми и не рискованны мувы он делает можно собрать статистику его посещения сайта какими разделами но если носить какие-то информационные например разделы ничего что такое на сайте мы можем пробовать любите туда информацию в интересах пользователя создан плюс чистоту его он захода даже если он не делал каких-то операции не проводил к возможным заходил читал можем посчитать попробовать почитать эти метрики как часто и как и разделом заходит ну это же самости а собственно только для новых а для тех конечно хорошо'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:28:52 text='хорошо это я понял теперь по поводу модели наверное правильно я понимаю что это будет единая модель какая-то самом начале это будет единая линия как правильно ну целом я предполагал что да если но мы можем новых пользователей отдельно вынести как раз потому что для них нет дальше софи через что мы пойдем это того что новый пользователь ну короче прогнозировать пытаться для нового пользователя и для тех с кем мы давно я для кого достаточно данных разными моделями которые в одной есть данные много данных об их поведению и другой нет рассматривать этих людей как разных собственно разные модели ней супер супер и теперь наверно последний вопрос и что я еще подумала что возможно в качестве фичи и можно закладывать где связь люди если вы имею информацию о том когда люди и когда понятного имеем информации люди были привлечены а какие то если были акции пример мы знаем что люди были привлечены с помощью какой он там промокод какой вводили например реферальную ссылку с какого-то блогера счет чего то мы можем их выделить такие тени вк аборты по времени в когорты по такие группы по способу того что им интересны и что что у них влиял возможно это для малого количества пользователей доступны только на же нет и меньше ну типа того да если можно отследить потому что не всегда можно если дельфин тех скорее всего этом был переход по ссылке можно было бы это где-то сохранить понятно что на истории возможно на стены не хранятся нашу супер и давай вот про последнюю'
  question_topic: ML

--- CHAPTER `00:33:58` — Обоснование выбора MSE ---
window: 00:33:58 .. 00:35:58
recognition_status: single (1 items)

ITEM #5
  interviewer_question: time=00:33:58 text='честно-честно для меня одну и в рамках вот такой быстро обратной связи для меня несколько странного ты говоришь про то что могут быть сильно на марии и при этом за минуты первое что ты предложил и это mc соответственно давай-ка вспомним как она сама съел ее проблемы с выбросами'
  candidate_answer: time=00:34:22 text='да как раз и я поэтому и подумала что нежить аномалии мне же дважды их учитывается я подумал использовать к я его съем который очень сильно не штрафует занимали в принципе как не надо делать потому что я буду скакать во время хорошо очень плохо оцениваете мышьяка раз потому что на выбросах будут неадекватно изучение метрики и выбросили бы надо удалять очень и смотреть на них вообще считать и на стену в принципе мы все тут вообще плохо потому что мне важно наверное и какую сторону мы дальше боится и как я сказала что бизнеса будет очень сложно показывать у нас я тут в общем вообще нет достоинства использовать я домой что бизнеса надо знаете знак того когда мы ошибаемся я считаю и кажется что когда мы считаем деньги тут важнее проценты на которые мы ошибаемся для конкретного человека что люди разные и у них могут быть очень разные ну короче денежки которые мы с ним получаем они могут варьировать очень сильно кого-то за 100 рублей с кого это 100000 рублей и какая-то средняя ошибка тысяч рублей она для них очень разные этих линий поэтому мы гораздо лучше использовать какие-то метрики которые все-таки относительные считают'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:35:54 text='тушенка хорошо дальше ты говорила про несимметричные метрики можно привести пару примеров то как это работает и в идеале затем в каких моделях это используются'
  question_topic: ML

--- CHAPTER `00:35:58` — Примеры несимметричных метрик ---
window: 00:35:58 .. 00:40:26
recognition_status: single (1 items)

ITEM #6
  interviewer_question: time=00:35:58 text='несимметричные метрики можно привести пару примеров'
  candidate_answer: time=00:35:59 text='то как это работает и в идеале затем в каких моделях это используются вопрос на котла не обмен на самом деле знаю метрику который от мерный кванта голос я не уверена я знаю что она выглядит как у нас есть два интервала если у вас нету прогноз то у нас угол наклона альфа если у нас перепрыгнул что долго на колонке единица минус альфа и наборы можем мы просто варьирует угол наклона отклонения и здесь не стать его знака а вот ну собственно плюсы этой метрики как раз в том когда нам супер важно куда мы идем в спросе часто наверно используется из модели с просто короче когда у нас есть или логистики что нам нужно довести определенное количество товара если у нас не будет этого товара мы будем потерять деньги нам нужно довести в идеале чуть чуть больше чем нужно и тогда модель будет хорошо справляться со своей задачей для бизнеса вольт ну кажется что в принципе мы можем мы можем свою метрику задать как угодно я считаю я вот эти коэффициенты можем просто на варьировать но смысле они виду что эта метрика это как бы вот эти несимметричные метрики наверное они важны на последней стадии оценке модели за что-то свое придумывать вот интересно какой угодно ветврач ну честно говоря я очень интересная идея но давай поговорим про хватаю вот ты и собственно у больного да ты немного про то что мы там по разным штрафом в зависимость разогнан до можешь привести в чем проблема вот этого колонтаево вас видеть и это не что иное как мая и вот в чем в чем проблема может быть почти правильный ответ неправильный вопрос может быть что в ней такого интересного в этой это медики в этом 8 поведи не могли ему еще раз поведение в ее ну там перегиб на в принципе с этим вроде как можно бороться расскажи поподробнее шедшего ну ну что такого плохого в 0 происходит но не дифференцируема эмулировать как потому что перегиб и у нас мыли выкладки . вы произвольным и мы не сможем ее использовать вот как есть но я точно знаю что можно как не помнить таким методом сделать может наверное можно было бы прекратить ниже и убиралась которая кусочно замена и она задана как раз в 0 и она задана квадратичной функции там нет никакого перегиба нет никакого кого и там производной есть и как раз юбер воз она хорошо там перестает скакать до боли при обучении для ее плюс и при этом не переобучаться на выбросы я не видела чтобы quando i lose как-то так делали невозможно можно пороге сверло сделать какой-то кусок который будет заднем квадратично и потом будут хвосты с различными наклонами куда развесила дожди раз ты не видел и отдавая себе реальный пример и то есть прям отдельная тема с тем как работает и just регрессор и про то что в игре саре нету по дефолту панталасса по крайней мере какое-то долгое время его не было по дефолту но была там реализация которая позволяла делать значит'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Statistics

--- CHAPTER `00:43:46` — Gradient-boosted trees ---
window: 00:43:46 .. 00:44:50
recognition_status: single (1 items)

ITEM #8
  interviewer_question: time=00:43:46 text='хорошо и грузин boosting тряс как именно он работает'
  candidate_answer: time=00:43:48 text='garden бусин трисс это ансамбль над деревьями который не просто голосование деревья участвуют независимые каждое дерево до обучается на ошибки предыдущего таким образом мы делаем кредитный спуска деревья входят с какой-то следим коэффициентами короче это сумма функций конечная функция эта сумма наших функций которые дают каждое дерево с каким-то весов при этом там каждое последующее дерево мы учитываем все меньшим коэффициентом чтобы не скакать но это как с тем чтобы все таки сходиться куда-то несколько оттуда сюда хорошо сына ну как бы плюс в том что мы ансамбль используемый ни одно дерево или обучиться'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:44:52 text='твой вопрос со звездочкой чем и джим русло gm и как просто отличается только другом'
  question_topic: ML

--- CHAPTER `00:44:50` — Вопрос со звёздочкой ---
window: 00:44:50 .. 00:55:36
recognition_status: single (1 items)

ITEM #9
  interviewer_question: time=00:44:50 text='твой вопрос со звездочкой чем и джим русло gm и как просто отличается только другом большой'
  candidate_answer: time=00:45:03 text='вроде бы ну в общем то что я точно помню что это просто недавно как раз смотрела ты готовилась что во-первых can boost классно работает с печальными речами потому что у него сложная система кодирования древних учений и он сам как в этом суть это делает довольно сложным способом и делать это руками было бы принципе нереально и я считаю прости пожалуйста а что же там такого не реального делает смысле кодированию реальных печей когда там разбиение происходит на под выборках исход выборов ну то есть мне кажется что она манить обучение это довольно сложно было бы делать когда ты перри обучаешься много раз моделей на разных сэмплах там несколько раз выделяются различные сэмплы рисунки руются так хорошо и трудозатрат на обычную в общем с черт про различия можно предугадать вроде как вроде как они все используют англии 100 грамм на разделении бином вроде как тут отвлечение потому что или же boost тоже это использую отличие в том что их жабу стучится в ширину у дерева и точен и говорил при древе про способы обучения он учит по слоям light дбм учиться и этом вроде как можно проверить легче чуть-чуть потому что слой и можно там разойтись лдпм он учит как бы в глубину сначала человек узла как boost я естественно того как готовилась к этому совету я не знал этого факта вашей маме но это очень прикольно короче я узнала о такой классный вид штукой boost имеет множество каких-то плюсов производительности и в том как хранить модель том что нет вот этого перекоса что дерево может быть не понятно и не сбалансированы и на прогнозе буковски проблема со временем вычисления для каких-то объектов а для каких то все быстро работает потому что как boost использует я забыла слова котором обязательно это деревья симметричные и они используются то есть сплит одинаковые по всем узлам на каждом уровне это один сплит одинаковый и в принципе кажется что это идет вразрез с концепцией вообще решающего дерево но круто что это работает потому что насколько я понимаю решает некоторые проблемы с скоростью прогноза из хранение модель что не нужно хранить куча сплитов слушай что значит идет вразрез общем общие идеи построение дерева ну она идет разрез потому что ты в каждом узле например представим какую-то идеальную ситуацию в которой ты сделала разбиение у тебя там уже отсортированы объекты или то мне не нужно по какой-то фиче вот кричал один мы сделали первое разбиение на втором свою мы выбрали лучшие разбиение и все равно в каком-то узле мы может быть будем делать что-то лишнее будет неоптимальным на моменте построение дерева мы как бы выбираем в этом узле конкретно в данной точке лучше разбиение отпустит не происходит потому что мы рассматриваем все узлы и кажется что это лишнее операции как бы возможно но здесь нужно поспорить на самом деле можно поспорить потому что в зависимости от того но кажется что вот и найдя один сплит и достаточно быстро ты можешь поиск сплитов за параллели и тебя один раз его сделать и применить сразу на весь мир и типа идти дальше ты скорость построение дерева ношу ну да да я имею ввиду что вот как раз в дереве же в самом алгоритме просто немного другая идея довольно на каждый сплит ты прогоняешь именно для этого узла для конкретных объектов федоровский есть так не происходит но крыму что это работа потому что действительно насколько я понимаю берёт большой прирост производительности не за счет это какой ступени а еще там разные сейчас прости нас давай вот эту часть тоже закрылось ты молодец давай я перейду водка вопрос который задавал изначально то что ну вот ту же сказала что есть проблема с подсчетом производной в клиент для канта и лосса и теперь вопрос ну то есть ты рассказала про i just я тебе есть же градиент вот проблема с лоссов что же что же такого зачем нам нужны какие-то дифференцируемые внутри функции зачем и почему мы не можем использовать какие то другие там вообще в принципе мышь как таковой градиенты не считаю пусть инге мы считаем ошибку вычитаю ну как бы предельно мне важно что не будет существовать произвольным и сингер я возможно ещё что-то ужасно говоря это касава не поняла но кажется что там бусин зэк но он как бы над ошибкой пункте функционала качества как мы считаем 2 функционала качество если нам типа ошибки нету там и этот объект просто можем не брать там выборку лично что это такое наверное это не супер важный мне так сейчас кажется потому что мы считаем качество не знаю мэй пмс она мы считаем что когда и лозы хорошо бы что река want to yes no какого-то объекта там 0 и не вижу что тоже на градиент для этого они уже верны предсказаны мы можем не брать его последующего следующие дерева и все они же подстраиваются то есть мы отбираем объекты которые имеют большие градиент это большие ошибки допустим кому каждое дерево выбираем объекты которые имеют большой ошибки но вообще градиенты и их забираем следующие дерево чтобы пытаться обучиться на этих ошибках на этих именно объектах и объектах которых нет общие ошибки можно их вообще не брать можно их братья на в каком-то соотношение но я не вижу как они могут все сломать часть моря хорошо давай я тебе задам вопрос по-другому выпусти именно в капусте есть своя особенность стильного сами которые можно использовать в пасти почему используются вот именно такие волосы они другие м сильная подсказка я знаю только что это boost или как у меня сериале регуляризации были мне кажется это никак не связано не очень-то больше не могут вспомнить лечить зубы статусами можешь хорошо окей окей давай тогда поговорим про регуляризации в ну раз уж ты вспомнил регуляризация вы даже будет 100 в посте в лакеями в капусте что как это вообще работает но у нас есть 102 как обычно доставай найди нормы и плюс есть еще а там член который будет считать количество листьев например угости то же одна сложность моделях сути тоже его можно использовать как функция народа канал для регуляризации но релизе 02 как обычно есть леса это скорее в каких-то листьев если каждого объекта есть скоро мы можем посчитать квадрата суммы квадратов или комсомольского хорошо простой вопрос как l1 l2 регуляризации работают что они делают с весами или один это не квадратичная форма это линейная то есть an issue мансов она может длительным весах которые не важны или если они коллинеарны очень если не важны а если у нас есть зависимые переменные здесь очень переменная году из них заземляют струю используют с каким-то весов за счет формы от этого функционала люди мы добиваемся и на зануление ан-2 просто уменьшают весам не дает им расти бесконечно хорошо смотреть какие что еще интересно регуляризации которые ты знаешь нет суши знаешь ли здесь еще ты можешь мне рассказать слушай но так как норм много типа л1 и л2 это нормы и ты можешь представить любую норму и соответственно на по-разному будет штрафовать такое и типа можно задать эту норму да конечно да погас типа можно в модельку передать не самописный можно передать и мин функционал норма ну придется залезть под капот но в целом дальнем не занят на маме хорошо слушай наверное единственное чем мы с тобой говорили то есть мы говорили про метрики поговорили про эти модельки где-то наверное хотелось бы поговорить с тобой'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `00:55:36` — Работа с понижением размерности ---
window: 00:55:36 .. конец
recognition_status: single (1 items)

ITEM #10
  interviewer_question: time=00:55:36 text='о вещь которые не так часто спрашивают нас о бесах это работа с понижением размерность вот какие подход понижения размерности'
  candidate_answer: time=00:55:52 text='что знаешь ты к этому не готовилась я просто ну как я знаю страны имеют понижения размерности потому что с этим было связано моя работа над кандидатской диссертации что ты забыла завален пойду это тот образ возможно я в заднице мне помог нет на самом деле я не уверен как бы я занималась этим только вот тогда научном сообществе возможно это немного смешно от того что желают у саши на исследования но я расскажу знаю там есть области которых у нас очень высоко высоко размерность признаков который мы хотим пользоваться иногда я тушу иногда они там и примерные нужно очень много усилий битва приложить для того чтобы каким то образом выделить важные это не хочется терять что-то еще и по сути методы которые делают проекции сильно могут помочь например там самый простой записи и построить смотреть какой процент информации и сей описывает способны объяснить выбрать какое-то количество главный компонент можно использовать мой любимый мёд все время несущихся карт кохонена на то же место появление пространство такая простая не еронко она помогает скорее для визуализации для того чтобы построить какие-то сложные визуализации многомерном пространстве есть это я не только метод для того чтобы новые фичи получить кстати классный способ не только заменить свое большое пространство какими-то вещами совсем а может быть можно дополнить посмотреть что там будет skynet ностью конечно независимо будут потому что может быть можно перейти там квадратуру короче по генерит фичей способ на генерить новые фичи верных зависимые говорю через него вопрос это не буду зависим потом выбрать что работы тут вот или это классно способ для того чтобы сделать какие-то консультации по нижнему пространства или визуализировать если мы снижаемся до двумерного трехмерного пространства cher еще какие методы но любые методы и это по сути главные компоненты ну короче ты можно задавать какие-то нетривиальной поверхности не плоскости и на них тоже проектировать а где это из пользуется тебе много власти есть такое есть такой подход ну я читала про это статьи исключительно вот моей научной области потому что они были коллеги которые курировались они работали писали свой песни в критике где генерал под по графику мы и одни использовали названием или фолд универсальный mifold и который проецировали но по сути это просто проекция на подбираемые подбираю мою сложную поверхность конь-огонь хорошо слушай ну ты хочешь сказать но здесь не вспомнить ничего про понижению честно говоря самое первое что приходит на ум вот вот прям но если я отвечаю я бы сказала ну естественно мы с помощью не день нужен просто зафигачить большую часть признаков оставить те которые реально что то значит у яндекса не сводится подожди они сходятся ли это по сути практически и миссией у типа главный компонент утвержденных монетами знаешь думу по сути своей зоны зрения что это ли но дело в том что чаще чем дожди здесь есть очень важный момент что когда я использовать интриг утилизации у меня остаются признаки полностью интерпретируемые ты сохраняешь большую сохранять получалось но в целом как бы когда мы говорим про pesel мы говорим про то что вот так хранить информацию как вы сохраните форма дисперсии до значений то есть их разлет какую еще информацию интересно было бы сохранен на самом деле вот отношение между двумя точками в 1 раз представим себе что у нас был какой-то по огромным пространствам хотела что я 300 я не сохраняются чтобы отрезок больше чем меньше отрезок да собственно вот снг подход он не блин да ну она наверное самый интересный самый крутой а вообще когда-то давно когда я был молод и юм я помню как я пришел на выступление ведь и ермакова короче и пить я тогда уже был я только-только стал один ли дом опять уже был тем рядов знать что он рассказывал про юнеп и и в представлении вообще очень интересный фильм рассказывает еда представляешь насколько сильно вот вам не вот осталось это что настолько клёвый настолько интересно было там по сути своей тоже идет сохранение но даже перевод в какое-то другое пространство не интерпретировано и но идет сохранение вот как раз отношений и за счет этого можно иногда очень интересные картинки получать и я пробовал в кластеризация пользователей можно было увидеть как одна группа пользователей которые смотрят один контент есть группа пользователей которые смотреть несколько контентов есть группа пользователей которые другой контент и вот есть такая вот ручеек между одним облаком людей которые смотрят один контент другое облако людей которые смотрят другой контент на есть ручью которую типа между ними что вот этого пользователя которые смотрели этот рукой карта честно очень интересное представление очень такое нестандартные прикольные и ну красиво красивой и даже интерпретирую за счет того что ты прям видишь то что вот эти вот люди на самом деле вот эти два облака они близки друг другу за счет того что есть этот вот связь реальных пользователей которые смотрели то есть это похоже и контент и но условно похожа да и можно пробовать делать перенос контента то есть одним людям предлагать посмотреть этот контента этим людям предлагать посмотрите контент то есть даже с этой вещью можем придумать какое-то применение вот это очень интересно каждого и ночную заберу сердечко там сердечки это уж больно да нет ну ладно'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

SAVE JSON: вставьте ответ в конец файла /Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-scientist-middle-karpov-ml-2022-06-26/data-scientist-middle-karpov-ml-2022-06-26.v2.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
