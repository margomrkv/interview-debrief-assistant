<!-- PIPELINE_MANIFEST
{
  "version": 2,
  "basename": "system-design-senior-karpov-v2-2022-02-28",
  "transcript_folder": "transcripts/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28",
  "source_id": "system_design_senior_karpov_v2_2022_02_28",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 18:13:13 +0200",
  "updated_at": "2026-05-20 18:19:09 +0200",
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
    "json": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/timecodes.txt",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 18:13:13 +0200"
    },
    {
      "id": 2,
      "name": "qa_extraction",
      "llm": true,
      "model": "claude-sonnet-4-6",
      "inputs": [
        "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.pipeline-log.md#LLM_INPUT_STEP_2"
      ],
      "outputs": [
        "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.json"
      ],
      "status": "completed",
      "duration_sec": 180.0,
      "notes": null,
      "finished_at": "2026-05-20 18:17:53 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 18:18:55 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 18:18:55 +0200"
    },
    {
      "id": 5,
      "name": "llm_validation",
      "llm": true,
      "model": "claude-sonnet-4-6",
      "inputs": [
        "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.pipeline-log.md#LLM_INPUT_STEP_5"
      ],
      "outputs": [
        "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.validation-report.md#SEMANTIC_VALIDATION"
      ],
      "status": "completed",
      "duration_sec": 90.0,
      "notes": null,
      "finished_at": "2026-05-20 18:19:09 +0200"
    }
  ]
}
-->

# Pipeline log v2

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28`
- **Source ID:** `system_design_senior_karpov_v2_2022_02_28`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 18:13:13 +0200
- **Last updated:** 2026-05-20 18:19:09 +0200

Фильтр в IDE: `*system-design-senior-karpov-v2-2022-02-28.v2*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/timecodes.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.pipeline-log.md` | — | completed |
| 2 | qa_extraction | yes | claude-sonnet-4-6 | `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.pipeline-log.md#LLM_INPUT_STEP_2` | `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.json` | 180.0s | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.validation-report.md` | 1.0s | completed |
| 5 | llm_validation | yes | claude-sonnet-4-6 | `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.pipeline-log.md#LLM_INPUT_STEP_5` | `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.validation-report.md#SEMANTIC_VALIDATION` | 90.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.pipeline-log.md`

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
SOURCE_ID: system_design_senior_karpov_v2_2022_02_28
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:01] алиф привет авиация рад тебя видеть
[00:04] приятно давишь немножко напряжен с wapsi
[00:08] на век возможно не каждый день ты
[00:10] окружён людьми с камерами света в
[00:12] микрофонами понимаю ситуация не можете
[00:15] привычный быть расскажи немножко про
[00:18] себя чем-то занимаешься что-то делаешь
[00:20] да я вот имею трехлетний опыт в
[00:23] аналитике как работают с инцестом в
[00:27] яндексе
[00:28] толока о какой полезный сервис а что ты
[00:33] делаешь когда сантис тавтологии расскажи
[00:37] я бы опустил бы
[00:39] [смех]
[00:42] не будем это поминать ну ладно как ты
[00:45] как ты оказался на этом стуле я да
[00:48] просто правил энтузиазм
[00:50] решил сходить
[00:52] будь будет ли твой начальник смотреть
[00:55] наверное может быть каждый начальник
[00:57] стать ему что я узнаю
[00:59] может быть слышал валлаби раков
[01:03] валентин бирюков да да ну вот он мой
[01:06] одноклассник
[01:06] про легко одноклассник твой начальник
[01:08] так сложилось в этой дебюта в высшей
[01:11] школы экономики пошел а кто-то на мехмат
[01:13] пошел ну не могу сказать что он пошел
[01:16] высшей школы экономики
[01:17] хорошо мостовые встретились на непростом
[01:21] собеседование должен сказать что за все
[01:23] время имели дизайна систем дизайна один
[01:27] человек вопрошал и эта запись еще не
[01:29] вышла величайшая сидит в студии но не на
[01:34] камерах посмотрим получится ли это
[01:36] изменить но даже если не получится здесь
[01:38] же вы не для того чтобы пройти не пройти
[01:40] правда для того чтобы поучиться и
[01:42] посмотреть и как раз такие вещи и
[01:45] развивают так что можно сказать что
[01:46] человек который прошел ни в чем просто
[01:48] не развился зря потратил свое время
[01:51] задачка простая но не оч
[01:55] за дизайне instagram
[01:57] что такое instagram от сервис которым
[01:59] пользуется на пусть и миллиард с
[02:01] копейками людей и там есть следующая
[02:04] функциональность эти прям даже скажу
[02:05] какая можно
[02:07] загрузить или скачать или посмотреть
[02:10] фотку можно
[02:13] поискать фотку
[02:16] как в инстаграме сергей можно фолловить
[02:20] других юзеров соответственно к тебя
[02:23] могут половить или фолловить понятно
[02:26] какой здесь ударение ставить но и
[02:28] четвертое что есть instagram feed то
[02:30] есть должны тебе показываться
[02:32] последние фотки тех кого ты
[02:36] добавил друзья те камилович
[02:39] окей
[02:42] ладно чтобы начать
[02:46] мы подумаем для начала
[02:49] какая у нас будет нагрузка на сервис ok
[02:52] начнем с этого мы знаем сколько у нас
[02:54] пользователю в предлагаю тебе встать у
[02:56] доски так будет гораздо легче где
[02:58] прикинуть а сколько у нас мы знаем что
[03:00] нас фотки будут загружаться и
[03:01] скачиваться правда ведь можно начать с
[03:04] этого сколько мы будем загружать и
[03:06] скачивать фоток как долго мы будем
[03:08] хранить и сколько это будет занимать
[03:10] место и запросов в секунду
[03:15] значит ну давайте прикинем сколько
[03:18] [музыка]
[03:20] инстаграм и юзеров полтора миллиарда вот
[03:23] так вот доставят
[03:26] use of окей хорошо весь instagram
[03:30] конечно
[03:32] но не регулярно пользуюсь ну как ты не
[03:35] регулярно загружать вот конечно за
[03:37] осмотришь конечно поэтому надо учитывать
[03:41] и то что скорее всего это какой нибудь
[03:42] такое типа будет большая нагрузка на рид
[03:46] составляющую
[03:48] чем на null out загрузку файла
[03:52] ok затем надо пойти на сколько людей и
[03:55] загружают фотографии в день ну наверное
[03:59] там 2 3 фотки в день каждый человек
[04:03] каждый но среднем ты же не загружаю но я
[04:06] не загружаю но мож кто-то там по 10
[04:08] фоток шлет
[04:10] есть такие люди да все мы знаем все мы
[04:14] знаем их да какие две фотки две фотки в
[04:17] день
[04:18] это у нас
[04:21] нам нагрузка какая нужно не позже 3
[04:24] миллиарда фоток на в день получает до
[04:25] 3000000 пишем 3 миллиардов у то есть это
[04:29] сколько в секунду входа грузится
[04:33] окей это
[04:36] удобнее писать сразу как 3 умноженное на
[04:39] 10 как сейчас так все так
[04:42] примерно 10 в
[04:45] девятой я правда тут с одним делала
[04:48] system design его обманул сказал что 10
[04:50] миллиардов это 10 или он меня уже даже
[04:53] не помню так мы и стали все считать в
[04:56] 100 раз больше
[04:57] окей это
[04:59] давайте приблизительно
[05:02] поделим на 30
[05:04] почему отрицать но 24 часа в день .
[05:08] сколько секунду вне
[05:10] но все говорят 100000 на самом деле это
[05:12] 86400 по моему
[05:15] предшественниц
[05:18] 261 864
[05:23] ok
[05:27] вам
[05:31] давайте это
[05:32] всё да да да 100 тысяч какие 10 конечно
[05:36] ну окей
[05:38] 39 на дефить 1 4 секунду до юпс
[05:46] отлично это и the right it right
[05:51] но смотрят то чаще чем вы конечно ларри
[05:54] саммерс коп исход видится
[05:56] не знаю но лента прокручиваю достаточно
[05:59] глубоко окей тогда это right
[06:04] вот нагрузка наверно на рид это
[06:09] блин ну пусть тысячу раз тяжелее конечно
[06:14] если можно не думать зачем
[06:17] 1
[06:24] take care of shiva мы теперь знаем
[06:27] сколько у нас грузиться в день фоток
[06:28] значит мы можем терпеть сколько нам
[06:30] нужно место для них в день и как мы
[06:34] будем эта храни ok но фотка там пять
[06:37] мегабайт на
[06:39] 5 мегабайт на фото китаец телефон
[06:42] открываешь нам надо сразу 20 вот так
[06:43] можно посмотреть да ну прикончишь канал
[06:46] 100 мегабайт секунду отличается нет я
[06:49] думал под общим сейчас мы хотим не ну
[06:53] вот мамед под подошла мы мы вынуждены
[06:57] сидеть вот едет охранника не надо давать
[06:59] мы за день и храним 3 миллиардов атака
[07:01] за 10 лет у нас будет столько то фоток
[07:03] да смотри сколько нам нужно место по
[07:06] dota цифровое фото мегабайт в год или
[07:10] сколько но не думаю что будет ну сколько
[07:12] нам нужно вообще на 10 ли хранилище
[07:14] какой нужно на 10 ли аспиратор хоккей на
[07:17] 5 х 5 х шар опять на 10 проще
[07:21] окей давай так
[07:25] значит на вход к 1 весит сколько на 5
[07:28] мегабайт
[07:31] 2 ты водитель играм фотки передал когда
[07:34] же говорят не передавайте фотки через
[07:36] telegram передавать файлами потому что
[07:37] она сжимает окей окей 2 мегабайт наверно
[07:41] я не знаю сколько фото количество ну
[07:43] пусть 500 килобайт окей 500 килобайт
[07:55] это одна фотка у нас фоток в день 3 на
[07:58] 10 9 3 на 10 в 9 в день
[08:03] так это у нас если мы перейдем это в
[08:05] какие-нибудь другие единицы сколько
[08:07] получается это
[08:10] сколько
[08:12] 500 мегабайт 110 6 до
[08:18] на 10 6 до 3 на 10 6 окей я понял сейчас
[08:26] мегабайт гигабайт 10 раз в 3
[08:32] еще 10 в 3 это получает свой работа
[08:36] терабайт окей 500 гбайт еще на три вещи
[08:41] натрия вот получается полтора петабайт а
[08:45] что
[08:47] [музыка]
[08:49] вы же еще или цифр
[08:53] немало это задний каток день на
[09:01] отлично а за 10 за 10 за ну вот
[09:06] получается надо
[09:08] полтора петабайт а на
[09:12] 10 до
[09:15] 360
[09:21] окей
[09:23] 15 на на 40
[09:31] а
[09:33] 40
[09:37] вот столько
[09:39] из я не ошибся
[09:42] это что у нас будет это черта вот
[09:47] мы полтора петабайт умножаем на 3600
[09:50] правильно на 3600 если мы умножаем на
[09:54] 1000 туна становится полтора экзабайт он
[09:56] уже на 36 правильно значит полтора на 36
[09:59] это четыре с половиной плюс 09 хотелось
[10:02] 5 4 5 4 экзабайт
[10:06] но это притом что мы взяли фотку за 500
[10:09] килобайт на самом деле фотка может быть
[10:10] 200 килобайт надо смотреть как там уже
[10:13] мая распределение до хвоста можно и
[10:15] ужать
[10:16] так хорошо мы теперь знаем сколько она
[10:19] все фотки на 10 лет нужно хранить
[10:22] прекрасно мы знаем нагрузку на right in
[10:26] a ride
[10:27] теперь у
[10:29] нас какой функционал нам нужно загрузить
[10:32] фотку посмотреть фотку да нам нужен
[10:35] какой-то fit и нам нужно поиск поиск в
[10:39] конце ставим таки попробуем сейчас
[10:42] нарисовать схему как это будет выглядеть
[10:45] на верхнюю равнину словно на одной
[10:48] машине таки одна машина
[10:51] наверное нам нужно как-нибудь типа
[10:53] хранилище фоточек для чего начнем вообще
[10:56] какой-то хранилищ
[10:58] такой вот значечек и
[11:00] наверно нам нужно оформить
[11:02] хранилище именно под фоточки то здесь
[11:05] там условно метаданных методом а тут а
[11:09] нам какая-нибудь там не знаю не знаю
[11:12] какого знака назначить и пускай будет
[11:14] это вот фоточки туда the lake ну да вот
[11:18] проще пусть это будет
[11:20] мета а это будет иметь строить
[11:25] как компания
[11:32] значит у нас есть человечек
[11:37] него есть
[11:39] наверное
[11:41] да то есть скорее все это будет как-то
[11:44] два сервиса один норовит один на grid
[11:48] разделим их и
[11:53] возможно на то чтобы ride ну о чем идея
[11:57] какая в том что
[11:59] я листаю например не всюду ленту до
[12:02] конца там полтора годового скорее всего
[12:04] нужно только часть лента поэтому нам
[12:07] нужен какой-то там типа кошек которые
[12:10] почти уже пошел в плохие верхней уровне
[12:12] нарисую смотрели верхние уровни во
[12:15] идет
[12:18] собственно верхнем уровне от вины по
[12:20] нарисовал уже
[12:23] сюда и сюда открепляется
[12:30] это понятно что и raider ли ты туда и
[12:32] дается дойти до да так все верхние
[12:35] уровни у нас есть то есть мы можем что
[12:36] можем загрузить мы можем прочитать и
[12:39] наверно там где прочитать можем и поиск
[12:41] когда по таким когда он вообще хорошо
[12:44] все таки
[12:46] теперь мы знаем что у нас пользователи
[12:49] больше одного да и у нас
[12:52] разный могут связи с этим штуки тем
[12:54] попробуем теперь нарисовать схемку уже
[12:57] очень более детальные подумать какие в
[12:59] ней должны быть момент причем ее
[13:00] нарисуем ok в общем начнем с того что я
[13:04] упомянул наверное это наверное сделать
[13:06] эффектный вид
[13:07] зачем-то нужна пешек на рид чего лента
[13:11] на вид ленты фондах загрузки идея какая
[13:14] наверное чтобы разгрузить немножечко вот
[13:17] именно вот эту вот стрелочку
[13:20] так она будет меня жирненькая
[13:23] the cash
[13:27] это будет побольше стрелочка
[13:30] то есть мы отгружаем из сервиса какой-то
[13:34] кэше он считается
[13:36] теперь нужно подумать прежде чем считать
[13:38] какие-то кэш и какие у нас вообще должны
[13:41] быть таблички
[13:42] окей и прозрачность ok но нам нужна
[13:47] сотри верхняя но уже загар 5 внизу
[13:50] просто 54 экзабайт запомнили и запросы
[13:53] выведи куда ты-то что думаешь
[13:55] начинали заново
[13:57] [музыка]
[14:03] значит нам нужно какие-то сущности
[14:05] сущности наверное это будет какой-нибудь
[14:07] юзер
[14:09] юзер так хорошо но для него то наверно
[14:13] комментам информация то его ключ
[14:16] что еще нам нужно локейшн пока подумай
[14:21] какие на вообще вверх уровне могли вьюер
[14:23] покидающего шанс use
[14:29] наверное лента но потом они лето милена
[14:32] карно это делается это комбинация список
[14:36] фоточек ну ты же кого-то фолловишь а то
[14:40] есть нужно понимать кого-то файле и
[14:41] чтобы строить ленс ограждена точно ноги
[14:44] это типа отношения user user
[14:47] [музыка]
[14:52] то есть типа
[14:54] признак так так сказать
[15:00] fauzer полу туда useful параличу и дира
[15:03] узнаешь колода начал давать правда ведь
[15:06] и
[15:08] что то еще или хватит еще фоточки
[15:11] фоточки то есть какую фоточку какой юзер
[15:14] загрузил города
[15:16] получается да
[15:20] отлично теперь нам нужно наверное какие
[15:22] то там атрибуты верно нужно прикинуть чё
[15:24] там будет этих таблицах сколько вы
[15:26] вместо они займут да окей юзер ключ его
[15:36] наверное еще какие-нибудь данные типа
[15:38] его месторасположения тебя
[15:42] не знаю что нибудь еще там на сколько
[15:45] нам это нужно но если мы планируем
[15:48] масштабироваться наверное мы можем
[15:50] разгружать сервер но сервис на разную
[15:54] географию и а как он этот логично
[15:57] определяется записывать каждый раз tiger
[15:59] опять а печник они каждый раз
[16:00] перезаписывают моему нет маму один раз
[16:03] записываемого пищи мощными буллинга
[16:05] ладно согласен тогда ошибочка то есть
[16:08] зачем это в таблице записывать и за это
[16:09] на входе определять окей через через что
[16:12] какой-нибудь там online streaming and
[16:15] look better make it an orgy
[16:20] что еще одна фотка это ключ и
[16:25] юзера
[16:28] мы еще сама
[16:30] фото pov ну
[16:33] айдишник да в общем то скорее всего
[16:37] просто фото паса и все
[16:39] лишнее ключ
[16:43] чтобы считать его с
[16:45] и матче тораджа окей теперь
[16:49] юзер юзер как-то можно похоронить а что
[16:54] нам нужно вам хранить но там нам нужно
[16:56] просто
[16:58] блин ну то есть нам нужно там хранить
[17:01] либо два ключа
[17:03] каждый как-то тяжеловато magic оторвал
[17:06] вот представьте на питоне пишешь для
[17:09] вазов вот тебе нужно вытащить для одного
[17:12] юзера всех кого он провода все и понятно
[17:15] тогда лучше организовать и тогда aктepы
[17:17] юзера его список фолловеров понятно
[17:20] юзер и там это тебе сразу помогает
[17:23] ответить на то какую базу данных те
[17:25] нужно использовать память и реляционные
[17:27] базы данных здесь
[17:28] ну потому что китай что меняя их первым
[17:31] киви или то есть а
[17:34] для фотки какая база данных нужно нужно
[17:37] реляционной
[17:41] ну ладно
[17:45] окей да себя какое отношение тоже киви
[17:48] он у меня здесь да ну то есть хорошо тут
[17:52] тут так же вы возможно и не стрельцы он
[17:54] на и отношению те есть это юзер ну и
[17:57] дальше вопрос насколько тебе важно
[18:02] насколько важно в как часто будем к ней
[18:05] запрашивать враги и зла димона сейчас
[18:08] подумаю так но теперь подумаем другое
[18:11] лучших сколько нас каждый зритель bass
[18:13] пусть место занимать
[18:18] хорошо надо плюс-минус оценить сколько
[18:21] весит там
[18:23] каждая
[18:28] каждый ключа кей ключ юзера можете
[18:33] какая-то мета это
[18:37] оставляя на ну хорошо нажмем на 4 начнем
[18:41] на фильм начнем user user что там у нас
[18:44] как мы юзеры хранить юзер маханием какой
[18:47] нибудь типа там не знаю а славно шишек
[18:50] да пусть будет интер считаем вот и
[18:54] тех кого он фолловит мы храним тоже как
[18:57] списком правда да но сколько в среднем
[18:59] будет у человека у кого он положит
[19:05] но 34 нет нет больше
[19:10] читая это но пусть в 34 ok мне оказалось
[19:14] после той 4000 34 сколько ты фолловишь у
[19:17] меня немножко насколько на стоны ноту
[19:21] меня тоже ведется только а у кого-то 0
[19:24] потому что у кого-то вообще не окей 100
[19:26] and часа 4
[19:31] кей фоточка
[19:34] она с юзерам определить м-64 на а
[19:38] фоточка это должна сначала посчитать
[19:41] сколько на базу и там окей сколько на
[19:44] базу у нас полтора 1000 полтора
[19:46] миллиарда блин полтора миллиарда до
[19:52] 5 10 и 9 10 и 9 на что на сколько байт
[19:57] на
[19:58] 88 на
[20:02] нашел
[20:05] но и .
[20:11] ким получается 12 на 10-12 часа почему
[20:15] умножаем на 100 юношеству пользователю
[20:17] каждого да если на них тоже нужно тут
[20:20] все так да я просто думал таки
[20:26] хорошо
[20:29] по 2 на 8 это но это 12 запишем это как
[20:35] 12 и
[20:37] десяточку вынесен на 10 10 10 12 это
[20:44] байт
[20:45] теперь тройка убираем это что становится
[20:49] килобайт она окей я помутило мега
[20:55] вещь giga giga terra r12 терабайт
[21:07] очень
[21:08] это вот follow .
[21:12] под фотки мы уже плюс-минус потянули на
[21:17] самом деле уже во сколько нам
[21:19] охраняющему
[21:20] но этот дурак записали с учетом того что
[21:23] нас новых пользователь не будет
[21:24] появляться да да да
[21:26] сможем добавить еще какой-то с учетом
[21:28] что какие-то новые будут появляться надо
[21:30] новый поток никакие да это понятно может
[21:32] быть это будет и завышена кнопка нет нас
[21:35] вы словно заниженный оценка получилось
[21:37] для этой штуки
[21:39] окей так теперь что-то еще
[21:45] так теперь фотки фотки фотки мы
[21:49] хранилище посчитали нам нужно только
[21:51] получается все равно что то какая то
[21:54] инфа да только не очень-то комета
[21:56] информацию это
[21:57] условно юзер который я запустил 64 и еще
[22:03] тоже какой-то там и печник фотки нам
[22:06] тоже не чудище наверно когда запустим уж
[22:08] к этим последней фотке фиде выдавать
[22:09] прожив точно
[22:13] какие-то там дата
[22:20] фото все
[22:22] 4.4
[22:26] того 3
[22:30] на 10
[22:33] 64
[22:37] 10 смотри тут есть одна одна проблема
[22:39] если найдем в келью у нас ключом будет
[22:42] являться что фото или юзер
[22:45] я понял
[22:47] наверное так и так надо да это тоже про
[22:51] нее
[22:53] ну мы можем объединить очень задачами
[22:57] может разуметь две таблицы 1 1 user
[22:59] ключи его фотки
[23:01] то есть так окей я понял я просто думал
[23:05] что можно сделать что-то типа объединить
[23:07] ключи это будет ключ пор упругой и
[23:10] большой палец был я тоже
[23:12] поэтому я думал что типа окей мы
[23:14] объединяем фото паз и юзер и прописываем
[23:17] они просто я так понимаю основной
[23:18] основная суть и вылью хранили что ты по
[23:20] ключу к чему-то дохода конечно это можно
[23:22] как-то перья наверное используют такие
[23:24] ключи ниш не храня доб
[23:26] что-то
[23:31] сделаем 2 так надежно
[23:38] очень получается x2
[23:48] а 10 что все 4
[23:56] 10
[24:01] на 8
[24:06] на
[24:09] 10 по
[24:14] точно действует не на
[24:17] 10 лет кладно еще на 10
[24:21] 10 господин себя четыре что 4 до 8 бар
[24:25] до
[24:28] сколько
[24:30] 84 там где-то потеряли вот это мы сейчас
[24:33] про фотки говорим да да да вот так мы
[24:35] грузим сколько мы писали 3 на 10 в 9 до
[24:38] 30 это секунду те три миллиарда
[24:42] вспомнить до 3 на 10 это в секунду в
[24:46] секунду дарят и в этот день мы ну нам же
[24:48] нужно на 10 лет посуда да еще на то есть
[24:53] 3 на 10 в 9 на минут это все
[24:58] еще в 9
[25:01] на
[25:11] 1005 к чему
[25:14] ты
[25:17] 624
[25:19] тыс от 5 и
[25:23] надеюсь еще ok
[25:28] поехали
[25:35] 11 12
[25:43] 730
[25:54] 4
[25:59] ки
[26:00] mt5
[26:04] вот
[26:19] ты часть
[26:33] key
[26:39] 150 на 10 короче сделаем это группа
[26:44] максимально грубо
[26:50] 10 в
[26:52] 13
[26:58] вот на арифметики то все его лица проще
[27:01] капец сказал
[27:06] кей 10
[27:10] попробуем еще раз на завод к носок от мы
[27:13] мы грузим 3 на 10 9 правда фотки мы еще
[27:16] что идем мы даем когда она соуса создана
[27:21] то есть пишем 3 на 10 9 надень на 3 на 3
[27:24] на 10 9 на 10 на 306 5
[27:29] 3 на 10 будут окей с нуля давай 3 на 10
[27:33] 9 т.е. на 10 с 9 на 10 на 10 на 365 тыс
[27:39] теперь это все умножается еще на что-то
[27:42] в скобочках в скобочках у нас пусть
[27:44] будет фото
[27:46] айди
[27:48] пусть будет фото иди которые мы просто
[27:51] отойди пусть у нас будет 8 байт
[27:53] юзера и digo sim white и дата восемь
[27:56] байт из фруктов восемь байт то есть
[27:59] двадцать четыре байт окей 24 правим на 8
[28:03] на 3 умножить на 8 над на 1 или на 24
[28:08] 8 на 3 на так дальше
[28:12] [музыка]
[28:14] значит 10 в 10 здесь умножить на 3 и 6
[28:21] умножить на 10 во 2 умножить на 3
[28:25] умножить
[28:28] на 2 . 4
[28:31] умножить на 10 то есть это 10 в 13
[28:40] умножить на 7 и 2 умножить на 36
[28:45] правильно то
[28:48] внутри 6 7 и 2 на 3 это 21 6
[28:53] правильно 26 + по пусть пусть от этого
[28:57] будет
[28:59] 4 то есть ну пусть будет 26 26 умножить
[29:04] на 10 13 это 2 и 6 можно 10 в 14 но 2 6
[29:10] тысячи четырнадцатый байт
[29:13] мы погнали
[29:15] ok снова
[29:18] мега-мега
[29:20] начал кило яблоки в его 11 мега-мега 9 8
[29:26] гигов
[29:28] 5 5 терьера
[29:32] 2222 исключается
[29:34] 260 терабайт
[29:41] total
[29:43] но терпимо
[29:52] окей мы посчитали того под хранилище
[29:56] фоток под юзера с фулловым
[30:03] так ну забыть видео vip вы где то выхожу
[30:07] это на чем это
[30:14] вот то стоит
[30:26] и
[30:27] что мы ещё один два терабайта followers
[30:30] of weeks 1 2 3
[30:41] так ну и хорошо но и по юзерам у нас
[30:44] тоже какая-то табличка будет но она тоже
[30:46] будет такая
[30:48] типа порядков а lovers да ну как не боль
[30:53] не больше . дашина даже скорее всего
[30:56] меньше потому что у нас по fall over 100
[30:59] полей как users за оттуда нас этих полей
[31:02] пусть будет 10 она будет находиться 20
[31:04] гигов а то еще меньше ну пусть 122 все
[31:08] остальное стирай
[31:14] так мы с тобой система уже на одной
[31:16] машине нарисовали правда теперь нам
[31:19] нужно подумать
[31:21] как нам вести надежность и
[31:26] передан денси
[31:28] макей
[31:31] значит
[31:33] ладно но это же думаю серетид да да это
[31:36] я буду сейчас все переделать
[31:39] в общем и донбассе на первое мы можем
[31:43] сделать для надежности это мастер своих
[31:47] типа условная
[31:49] это хорошо как мы сначала смычок
[31:53] понимаешь нас тут будет определенная
[31:54] система учит мечтам и данные будем
[31:56] как-то сортировать партиции ровать надо
[31:58] ты же в яндексе работаешь на и налить
[32:01] регулярно ходит верни гости какой-то
[32:03] пользователь девятого уровня нет игроков
[32:07] наверное таком 5 ну как к наверное
[32:09] сколько яндексе работаешь меньше года но
[32:13] чуть меньше q но
[32:16] пляж нарекания чительно мастер выйти и
[32:19] пользователей киев
[32:22] ты что своей чести не знаешь ты не
[32:25] хочешь над доставка ходишь хожу конечно
[32:27] регулярно на свой
[32:32] других слов глен
[32:35] скорее всего 5 важного портирование ты
[32:38] знаешь соответственно подумал как мы
[32:40] можем здесь profits и ровать полый
[32:41] почему то есть у нас будет много
[32:44] серверов правильно да нагрузка между
[32:46] ними мы хотим чтобы было распределено
[32:47] при смене да даже мы можем сделать
[32:49] окей первая по гиа на верном пути позор
[32:57] так по гиа вот такая мысль типа вот юзер
[33:01] здесь делает запрос ok давайте его в
[33:04] инстаграме кого из известных людей
[33:06] фолловишь ну окей например американских
[33:09] людей у кого-то фолловишь instagrammers
[33:11] ты стесняешься сказать хоть я скажу к
[33:14] выехал я же не помню
[33:17] нижней вполне на звезды не зафолловят
[33:20] ладно друзей друзей такие друзья не
[33:25] интересно
[33:26] представь фолловят сколько в максимуму
[33:30] самых популярных чуваков инстаграме
[33:33] последователи ok но 2 миллиона где то
[33:35] есть
[33:37] супер твист python не самый популярный
[33:39] они эти великие 200 миллионов
[33:44] без ты предлагаешь по географии и
[33:47] держать то есть вот я пользователь я
[33:49] зашел на какой сервак мне нужно достичь
[33:52] посмотреть загрузить фотку правильно я
[33:54] понял make
[33:56] как мы будем от гарнировать партиции
[33:59] ровать
[34:03] если сам скала сном популярные
[34:05] американцы то да тогда будет все
[34:08] ломается нет я просто думаю что например
[34:12] еще собирался партиции ровать момента да
[34:16] это просто очень много дан потребуется
[34:18] типа место в уже понял что многомерности
[34:22] оттуда эти 4 заповедь если окей так хочу
[34:25] когда же 5 4 экзабайт африке скупки
[34:27] машин нужно на но сколько
[34:29] прикинем сколько
[34:31] машина может хранить несколько
[34:35] терабайтов
[34:39] 10 точно может помочь ли что может
[34:42] фатально дарий стоек кучу хорошо то есть
[34:45] 100 терабайт может машинах радиальный
[34:47] сколько машин нужно под супер обед
[34:50] 5
[34:52] миллионов что до неба бог с тобой петард
[34:55] и пастора боится значит тысячи машин это
[34:57] 100 петабайт правильно да значит
[35:01] 10 тысяч подожди я спешила репликация
[35:05] нам нужна какая конечно ну да еще типа
[35:08] то есть еще до это кажется
[35:14] h150 то есть машина у нас нормально в
[35:17] принципе нам же банально хранить где-то
[35:19] это нужно это да а чтобы такое хранить
[35:22] по-моему там же есть какая связь между
[35:24] количеством ядерным процессором эту тем
[35:26] сколько у тебя может быть
[35:27] что оперативки что жесткого диска или я
[35:31] ошибаюсь ну ладно я тоже ну с
[35:34] оперативкой точно и взаимосвязь да
[35:37] хорошо хорошо как же мы шарди рование
[35:41] будет ванна вариантов не много на самом
[35:44] деле то есть первое это
[35:48] либо
[35:50] мы
[35:53] разбиваем по
[35:57] локации запроса получается только
[36:01] подумаем у нас мы доступ к чему и делаем
[36:05] мы делаем таблицы users
[36:07] мы когда отправлен запрос на сервер серы
[36:10] в итоге что нам будет скачивать картин
[36:12] картиночку да как дальше у нас мы знаем
[36:15] бывают очень популярны и пользователя до
[36:17] которые могут иметь 200 миллионов
[36:20] последовательно теперь представь что мы
[36:25] стиви у этого пользователя кладем на
[36:27] один сервер
[36:29] он падает до нем поместиться на будет
[36:34] тяжело
[36:37] вообще вообще на самом деле я бы сделал
[36:39] здесь двойной уровень шапки даже не
[36:42] шарнирами то есть я бы скажем так
[36:44] раскидывал по почему ключа по юзер кей
[36:48] нью-йорке то что у нас арсенале нет я я
[36:52] имел ввиду как можно уменьшить нагрузку
[36:54] на еще уменьшить пользователь картинка
[36:58] то есть по картинке
[37:00] то есть если я захожу на условного
[37:03] пользователя половлю которую 200-ми на
[37:05] пользователей я скачиваю картинки на
[37:07] озере раз разных да а если еще дальше
[37:11] подумать то я же могу вот дальше то есть
[37:12] я захожу меня перекидывает на какой-то
[37:15] условный сервак который дальше меня еще
[37:18] внутри себя балансит на другие серваке
[37:20] правда ты словно говоря у меня эта
[37:23] картинка находится на каких-то 5
[37:25] серваках и между этими н серваках и
[37:27] между этим сервака меня перекидывает
[37:29] зависит от того какая там нагрузка но
[37:31] изначально меня кидает по картинке у
[37:34] нас смогли единица нагрузки картинка
[37:37] оттенка
[37:40] которые я уже дальше могу реплицировать
[37:42] на
[37:43] 3 сервера то есть как минимум если мы
[37:46] про репликацию подарили x3 а дальше
[37:49] можем же водить если картинками
[37:50] популярное скачивается больше роста мы и
[37:53] в принципе можем за хэши как ok правда
[37:57] да да
[38:00] ok это пока
[38:03] пока так
[38:05] ну теперь вот у нас значит что подумают
[38:10] мы моем у нас такие как как я псих как
[38:13] как кошелек номер
[38:20] в плане как какие в хэш-функции можно
[38:23] применить как от некоторые хэшировать
[38:25] для проецирования dapper тестирование
[38:30] procon стон fishing consist in gas
[38:33] vacancies я тоже мне сделать короче
[38:35] ладно то я попробую нарисовать он
[38:37] осталось немного времени нарисуем
[38:38] систему уже с учетом редант ниц и что у
[38:40] нас есть
[38:43] хоккей у нас есть
[38:46] хранилища и не начни с пользователем
[38:49] окей давай оттуда пришел пользователь
[38:52] пришел юзер него есть мак мобилочка так
[38:56] дальше а запрос отсылается запрос
[38:58] приходит куда до запрос отсылается
[39:00] куда-то куда он приходит в
[39:03] [музыка]
[39:05] вот балансе блуд делать
[39:09] который говорит такие лет либо вид
[39:12] запрос либо райт запрос
[39:15] допустимо to ride запрос на
[39:23] ok если это и запрос то тогда что нам
[39:27] нужно он учится в базу данных followers
[39:30] ну точнее скажем так мы допустим ленту
[39:33] хотим посмотреть города значит лента
[39:35] может быть уже при компьютер быть правда
[39:37] да все так то есть он бьется какой-то
[39:40] cash
[39:44] cash окей
[39:46] так конеч нас понятно откуда считывается
[39:50] а
[39:53] еще
[39:55] какая же у нас считывает что он читает у
[39:58] нас табличку но дед на какой-то сервис
[40:01] который читает табличку followers да
[40:04] берет из нее users из этого users он
[40:06] берет картинки берет top н последний
[40:10] когда и отсюда
[40:13] идет стучится в торгую хранилище
[40:16] получается картинок и выгружает
[40:19] но мы можем
[40:21] типа как обсудили тут немножечко так
[40:24] сказать чтобы погружалась
[40:28] но это вот нам уже у нас уже не будет
[40:30] времени сейчас учесть да короче здесь
[40:32] можно по словам расправились загрузку
[40:34] картинки и
[40:36] ну вы не параллели за счет того что у
[40:38] нас в принципе все будет раскидано по
[40:40] разным точкам правда ведь природа
[40:44] окей пост на самом деле мы же можем
[40:48] разные вещи делать картинках загрузку
[40:51] картинок им одним образом партиции ruim
[40:54] потом дальше мы протестируем загрузку
[40:57] ленты другим образом
[40:59] ok никто что не мешает и не брал не
[41:03] сразу в плане доступности до можно так
[41:07] сделать ты мне сначала ну так я зашел
[41:10] юзер юзера определили хэш по хорошо
[41:12] понятно на каком ти ракетка хранится его
[41:15] кэш дальше я стучусь если кэш есть все
[41:18] выдаем этот кэш и если его нет или он
[41:21] обновляется он дальше то делает этот
[41:23] сервак стучится по ключу юзера уже
[41:28] известно потому что он всегда стучится
[41:30] он же ему известно носитель он стучится
[41:32] берет фолловеров все так от фолловеров
[41:34] он стучится а в картинке отваров он
[41:38] стучится в
[41:39] yuserg yuserg yuserg
[41:42] фото а фото дальше известно хранится на
[41:46] каких тачках да потому что тоже хранится
[41:49] через consist in hearing у
[41:51] него есть внутри адрес на книгу каждый
[41:53] сервис на кастинг 1 будет почитать что
[41:56] такое у него есть внутри адресная книга
[41:59] которая говорит какой диапазон ну ответь
[42:03] отвечает какая машина
[42:06] да окей
[42:09] таким образом мы распределили загрузку
[42:12] картиночки ну тут можно все это короче
[42:14] mute это считывание картиночки дамы
[42:17] расстроили теперь про про
[42:20] запись картин , девочки тоже самое
[42:22] только там никакого конечно быть не
[42:24] должно ну да то есть мы просто сразу
[42:27] мощи наверное да мы можем сразу напрямую
[42:30] как-то запись ядер записывает картинку
[42:33] то есть у него что уже есть у него есть
[42:37] айдишник этого юзеров мы его записываем
[42:40] в юзер фото а фото мы берем хаяши кидаем
[42:44] на какую-то тачку не нужна ли нам
[42:48] промежуток между
[42:51] молитесь и вот здесь я думал она нужна
[42:55] мне кажется она стремится и закончу
[42:57] поэтому разберем какие принципе я думаю
[42:59] что часть мы уже разобрали то есть из
[43:01] моих советов ты вначале не знал что
[43:04] делать
[43:04] ты и вот просто стула shows for поэтому
[43:09] я тебе помогал первое что ты делаешь
[43:11] всегда это ты социально требования были
[43:14] даны ты начинаешь списывать нагрузку
[43:16] коко запросов в секунду сколько мне
[43:18] нужно хранилища какие у меня связи с
[43:20] функциями требуемыми отношения сколько
[43:22] хранилище нужно для них
[43:24] отсюда ты понимаешь как те машин нужно
[43:26] дальше ты рисуешь общую схему для работы
[43:29] на одной машине да и в принципе написал
[43:31] потом мы начинаем думать а как же нам
[43:34] улучшить и даже не улучшить обеспечить
[43:37] доступность намного major'а ну и и тут
[43:39] возник самый важный вопрос это как
[43:41] партиции ровать в принципе понятно как
[43:44] проецировать по юзеру
[43:46] даст условно говоря подгружать для юзера
[43:48] ленту где ее подгружена хранить но здесь
[43:50] просто по юзеру но как уже эту ленту
[43:53] генерировать где для нее
[43:55] фотки откуда выгружать то есть ну
[43:57] понятно что если к одной фотки начинают
[43:59] стучаться
[44:00] 200 миллионов потому что условный скала
[44:03] отдавал фоточку со своей дочкой и просто
[44:07] все побежали снова сервер или скачивать
[44:08] от сервер ляжет
[44:10] скорее всего точнее даже то даже так
[44:13] скажем таскала добавил какой-то
[44:15] решеточки все начали эти фоточки цекало
[44:17] искать другой вопрос как еще это эта
[44:18] проблема решить может быть нам обновлять
[44:20] лента дочь популярно польза не у всех
[44:22] сразу вас какой-то вещью либо нам как то
[44:26] значит это популярный пользователей и
[44:27] кидать на лад балансер от них запроса и
[44:31] уже этот вот балансер там допустим для
[44:34] них фактор ли прикреплю кации делать не
[44:35] 31 а 10 или 20
[44:40] вот эти моменты то есть вот на этом
[44:42] моменте у нас был ступор а как нам
[44:45] проецировать по юзеру ляжет сразу им
[44:48] если вы хранили и хранение фоток
[44:50] проецировать по юзеру
[44:52] все у нас будет где очень густо где
[44:56] очень пуст поэтому будем раскидывать
[44:58] фотки и
[45:00] здесь у нас по повышена наверное даже не
[45:03] ляжет от одной фотки вот но если 10
[45:05] фоток начнут загружать только примешь
[45:07] нагрузка 10 раз они же еще любят
[45:10] выкладывать сразу по 10 на 1 3 4
[45:16] видео какой то может
[45:18] понятно что это все можно попробовать
[45:21] как-то за кашель вытащить из кэша
[45:23] использует какие-то поэтому of present
[45:25] кулисе dnn но
[45:28] сидел и седина но это во первых нужно
[45:33] знать
[45:35] ну и дальше тут на самом деле можно еще
[45:37] к чему у тебя
[45:39] какая скорость скачивания нужно а какая
[45:41] скорость очень и может отдельной машинах
[45:43] какая скорость записи водку допустим вот
[45:45] мы поговорили сколько нам нужно место и
[45:47] сколько нам нужно от этого машин а может
[45:50] быть мы не успеваем с таким количеством
[45:51] машин записывать эту насколько в секунду
[45:54] записывается
[45:58] 100 мегабайт в секунду
[46:02] вот на тоже надо это вот дальше другие
[46:05] вопросы можно задавать допустим вот
[46:06] сколько можно записывать на их где диск
[46:09] в секунду на рейд массив
[46:13] вопросик вопрос да какая скорость и
[46:16] дальше какая скорость скачивания и
[46:19] сколько сколько сервак один может
[46:21] держать сколько connection of можно
[46:23] держать его как эти connection а делать
[46:24] что там какой фланг пол не long пол как
[46:28] обновлять ленту
[46:29] ну вот и ему всему нужно
[46:32] взять меня но в целом смотри как только
[46:34] ты вышел из табора пошло плюс-минус
[46:36] нормально то есть ты не понимала что
[46:39] делать начали да а но теперь ты знаешь
[46:42] что вначале ты расписываешь за роста
[46:44] сколько места мне нужен
[46:47] как тебе опыт был прикольно ну приходить
[46:50] следующий раз спасибо был рад пообщаться
[46:53] я пожар и получай десят уровень
[46:56] мастерства новой киеве стали будет
[47:00] сделан

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
Write JSON only to: splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. system-design-senior-karpov-v2-2022-02-28.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.json \
    --video transcripts/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.json --out splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.qa-split.json \
    --video transcripts/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.validation-report.md

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
video.md: /Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/video.md

--- CHAPTER `02:55` — Расчет нагрузки на систему ---
window: 02:55 .. 10:41
recognition_status: single (1 items)

ITEM #2
  interviewer_question: time=10:29 text='теперь у нас какой функционал нам нужно загрузить фотку посмотреть фотку да нам нужен какой-то fit и нам нужно поиск поиск в конце ставим таки попробуем сейчас нарисовать схему как это будет выглядеть на верхнюю равнину словно на одной машине таки одна машина'
  candidate_answer: time=10:51 text='наверное нам нужно как-нибудь типа хранилище фоточек для чего начнем вообще какой-то хранилищ такой вот значечек и наверно нам нужно оформить хранилище именно под фоточки то здесь там условно метаданных методом а тут а нам какая-нибудь там не знаю не знаю какого знака назначить и пускай будет это вот фоточки туда the lake ну да вот проще пусть это будет мета а это будет иметь строить как компания значит у нас есть человечек него есть наверное да то есть скорее все это будет как-то два сервиса один норовит один на grid разделим их и возможно на то чтобы ride ну о чем идея какая в том что я листаю например не всюду ленту до конца там полтора годового скорее всего нужно только часть лента поэтому нам нужен какой-то там типа кошек которые почти уже пошел в плохие верхней уровне нарисую смотрели верхние уровни во идет собственно верхнем уровне от вины по нарисовал уже сюда и сюда открепляется это понятно что и raider ли ты туда и дается дойти до да так все верхние уровни у нас есть то есть мы можем что можем загрузить мы можем прочитать и наверно там где прочитать можем и поиск когда по таким когда он вообще хорошо все таки'
  reference_answer: time=None text=None
  interviewer_feedback: time=12:44 text='все таки'
  question_topic: Data Modeling

--- CHAPTER `10:41` — Верхнеуровневая схема работы ---
window: 10:41 .. 12:47
recognition_status: single (1 items)

ITEM #3
  interviewer_question: time=12:46 text='теперь мы знаем что у нас пользователи больше одного да и у нас разный могут связи с этим штуки тем попробуем теперь нарисовать схемку уже очень более детальные подумать какие в ней должны быть момент причем ее нарисуем ok в общем начнем с того что я упомянул наверное это наверное сделать эффектный вид зачем-то нужна пешек на рид чего лента на вид ленты фондах загрузки идея какая наверное чтобы разгрузить немножечко вот именно вот эту вот стрелочку'
  candidate_answer: time=13:23 text='the cash это будет побольше стрелочка то есть мы отгружаем из сервиса какой-то кэше он считается теперь нужно подумать прежде чем считать какие-то кэш и какие у нас вообще должны быть таблички окей и прозрачность ok но нам нужна сотри верхняя но уже загар 5 внизу просто 54 экзабайт запомнили и запросы выведи куда ты-то что думаешь начинали заново'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Data Modeling

--- CHAPTER `12:47` — Более детальная схема ---
window: 12:47 .. 14:03
recognition_status: not_recognized (0 items)

(no items extracted)
--- CHAPTER `18:09` — Объемы памяти для хранения баз ---
window: 18:09 .. 31:19
recognition_status: single (1 items)

ITEM #6
  interviewer_question: time=31:14 text='так мы с тобой система уже на одной машине нарисовали правда теперь нам нужно подумать как нам вести надежность и передан денси макей'
  candidate_answer: time=31:33 text='значит ладно но это же думаю серетид да да это я буду сейчас все переделать в общем и донбассе на первое мы можем сделать для надежности это мастер своих типа условная это хорошо как мы сначала смычок понимаешь нас тут будет определенная система учит мечтам и данные будем как-то сортировать партиции ровать надо ты же в яндексе работаешь на и налить регулярно ходит верни гости какой-то пользователь девятого уровня нет игроков наверное таком 5 ну как к наверное сколько яндексе работаешь меньше года но чуть меньше q но пляж нарекания чительно мастер выйти и пользователей киев ты что своей чести не знаешь ты не хочешь над доставка ходишь хожу конечно регулярно на свой других слов глен скорее всего 5 важного портирование ты знаешь соответственно подумал как мы можем здесь profits и ровать полый почему то есть у нас будет много серверов правильно да нагрузка между ними мы хотим чтобы было распределено при смене да даже мы можем сделать окей первая по гиа вот такая мысль типа вот юзер здесь делает запрос ok давайте его в инстаграме кого из известных людей фолловишь ну окей например американских людей у кого-то фолловишь instagrammers ты стесняешься сказать хоть я скажу к выехал я же не помню нижней вполне на звезды не зафолловят ладно друзей друзей такие друзья не интересно представь фолловят сколько в максимуму самых популярных чуваков инстаграме последователи ok но 2 миллиона где то есть супер твист python не самый популярный они эти великие 200 миллионов без ты предлагаешь по географии и держать то есть вот я пользователь я зашел на какой сервак мне нужно достичь посмотреть загрузить фотку правильно я понял make как мы будем от гарнировать партиции ровать если сам скала сном популярные американцы то да тогда будет все ломается нет я просто думаю что например еще собирался партиции ровать момента да это просто очень много дан потребуется типа место в уже понял что многомерности оттуда эти 4 заповедь если окей так хочу когда же 5 4 экзабайт африке скупки машин нужно на но сколько прикинем сколько машина может хранить несколько терабайтов 10 точно может помочь ли что может фатально дарий стоек кучу хорошо то есть 100 терабайт может машинах радиальный сколько машин нужно под супер обед 5 миллионов что до неба бог с тобой петард и пастора боится значит тысячи машин это 100 петабайт правильно да значит 10 тысяч подожди я спешила репликация нам нужна какая конечно ну да еще типа то есть еще до это кажется h150 то есть машина у нас нормально в принципе нам же банально хранить где-то это нужно это да а чтобы такое хранить по-моему там же есть какая связь между количеством ядерным процессором эту тем сколько у тебя может быть что оперативки что жесткого диска или я ошибаюсь ну ладно я тоже ну с оперативкой точно и взаимосвязь да хорошо хорошо как же мы шарди рование будет ванна вариантов не много на самом деле то есть первое это либо мы разбиваем по локации запроса получается только подумаем у нас мы доступ к чему и делаем мы делаем таблицы users мы когда отправлен запрос на сервер серы в итоге что нам будет скачивать картин картиночку да как дальше у нас мы знаем бывают очень популярны и пользователя до которые могут иметь 200 миллионов последовательно теперь представь что мы стиви у этого пользователя кладем на один сервер он падает до нем поместиться на будет тяжело вообще вообще на самом деле я бы сделал здесь двойной уровень шапки даже не шарнирами то есть я бы скажем так раскидывал по почему ключа по юзер кей нью-йорке то что у нас арсенале нет я я имел ввиду как можно уменьшить нагрузку на еще уменьшить пользователь картинка то есть по картинке то есть если я захожу на условного пользователя половлю которую 200-ми на пользователей я скачиваю картинки на озере раз разных да а если еще дальше подумать то я же могу вот дальше то есть я захожу меня перекидывает на какой-то условный сервак который дальше меня еще внутри себя балансит на другие серваке правда ты словно говоря у меня эта картинка находится на каких-то 5 серваках и между этими н серваках и между этим сервака меня перекидывает зависит от того какая там нагрузка но изначально меня кидает по картинке у нас смогли единица нагрузки картинка оттенка которые я уже дальше могу реплицировать на 3 сервера то есть как минимум если мы про репликацию подарили x3 а дальше можем же водить если картинками популярное скачивается больше роста мы и в принципе можем за хэши как ok правда да да ok это пока пока так ну теперь вот у нас значит что подумают мы моем у нас такие как как я псих как как кошелек номер в плане как какие в хэш-функции можно применить как от некоторые хэшировать для проецирования dapper тестирование procon стон fishing consist in gas vacancies я тоже мне сделать короче ладно то я попробую нарисовать он'
  reference_answer: time=None text=None
  interviewer_feedback: time=32:49 text='окей первая по гиа вот такая мысль'
  question_topic: Data Modeling

--- CHAPTER `31:19` — Надежность и redundancy ---
window: 31:19 .. 38:36
recognition_status: not_recognized (0 items)

(no items extracted)
--- CHAPTER `38:36` — Система с учетом redundancy ---
window: 38:36 .. 42:45
recognition_status: single (1 items)

ITEM #7
  interviewer_question: time=38:37 text='осталось немного времени нарисуем систему уже с учетом редант ниц и что у нас есть'
  candidate_answer: time=38:43 text='хоккей у нас есть хранилища и не начни с пользователем окей давай оттуда пришел пользователь пришел юзер него есть мак мобилочка так дальше а запрос отсылается запрос приходит куда до запрос отсылается куда-то куда он приходит в вот балансе блуд делать который говорит такие лет либо вид запрос либо райт запрос допустимо to ride запрос на ok если это и запрос то тогда что нам нужно он учится в базу данных followers ну точнее скажем так мы допустим ленту хотим посмотреть города значит лента может быть уже при компьютер быть правда да все так то есть он бьется какой-то cash cash окей так конеч нас понятно откуда считывается а еще какая же у нас считывает что он читает у нас табличку но дед на какой-то сервис который читает табличку followers да берет из нее users из этого users он берет картинки берет top н последний когда и отсюда идет стучится в торгую хранилище получается картинок и выгружает но мы можем типа как обсудили тут немножечко так сказать чтобы погружалась но это вот нам уже у нас уже не будет времени сейчас учесть да короче здесь можно по словам расправились загрузку картинки и ну вы не параллели за счет того что у нас в принципе все будет раскидано по разным точкам правда ведь природа окей пост на самом деле мы же можем разные вещи делать картинках загрузку картинок им одним образом партиции ruim потом дальше мы протестируем загрузку ленты другим образом ok никто что не мешает и не брал не сразу в плане доступности до можно так сделать ты мне сначала ну так я зашел юзер юзера определили хэш по хорошо понятно на каком ти ракетка хранится его кэш дальше я стучусь если кэш есть все выдаем этот кэш и если его нет или он обновляется он дальше то делает этот сервак стучится по ключу юзера уже известно потому что он всегда стучится он же ему известно носитель он стучится берет фолловеров все так от фолловеров он стучится а в картинке отваров он стучится в yuserg yuserg yuserg фото а фото дальше известно хранится на каких тачках да потому что тоже хранится через consist in hearing у него есть внутри адрес на книгу каждый сервис на кастинг 1 будет почитать что такое у него есть внутри адресная книга которая говорит какой диапазон ну ответь отвечает какая машина да окей таким образом мы распределили загрузку картиночки ну тут можно все это короче mute это считывание картиночки дамы расстроили теперь про про запись картин , девочки тоже самое только там никакого конечно быть не должно ну да то есть мы просто сразу мощи наверное да мы можем сразу напрямую как-то запись ядер записывает картинку то есть у него что уже есть у него есть айдишник этого юзеров мы его записываем в юзер фото а фото мы берем хаяши кидаем на какую-то тачку не нужна ли нам промежуток между молитесь и вот здесь я думал она нужна мне кажется она стремится и закончу поэтому разберем'
  reference_answer: time=42:59 text="какие принципе я думаю что часть мы уже разобрали то есть из моих советов ты вначале не знал что делать ты и вот просто стула shows for поэтому я тебе помогал первое что ты делаешь всегда это ты социально требования были даны ты начинаешь списывать нагрузку коко запросов в секунду сколько мне нужно хранилища какие у меня связи с функциями требуемыми отношения сколько хранилище нужно для них отсюда ты понимаешь как те машин нужно дальше ты рисуешь общую схему для работы на одной машине да и в принципе написал потом мы начинаем думать а как же нам улучшить и даже не улучшить обеспечить доступность намного major'а ну и и тут возник самый важный вопрос это как партиции ровать в принципе понятно как проецировать по юзеру даст условно говоря подгружать для юзера ленту где ее подгружена хранить но здесь просто по юзеру но как уже эту ленту генерировать где для нее фотки откуда выгружать то есть ну понятно что если к одной фотки начинают стучаться 200 миллионов потому что условный скала отдавал фоточку со своей дочкой и просто все побежали снова сервер или скачивать от сервер ляжет скорее всего точнее даже то даже так скажем таскала добавил какой-то решеточки все начали эти фоточки цекало искать другой вопрос как еще это эта проблема решить может быть нам обновлять лента дочь популярно польза не у всех сразу вас какой-то вещью либо нам как то значит это популярный пользователей и кидать на лад балансер от них запроса и уже этот вот балансер там допустим для них фактор ли прикреплю кации делать не 31 а 10 или 20"
  interviewer_feedback: time=None text=None
  question_topic: Data Modeling

SAVE JSON: вставьте ответ в конец файла /Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v2-2022-02-28/system-design-senior-karpov-v2-2022-02-28.v2.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
