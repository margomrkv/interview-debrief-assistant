<!-- PIPELINE_MANIFEST
{
  "version": 2,
  "basename": "system-design-senior-karpov-v1-2022-01-19",
  "transcript_folder": "transcripts/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19",
  "source_id": "system_design_senior_karpov_v1_2022_01_19",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 18:13:13 +0200",
  "updated_at": "2026-05-20 18:20:30 +0200",
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
    "json": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/timecodes.txt",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.pipeline-log.md"
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
        "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.pipeline-log.md#LLM_INPUT_STEP_2"
      ],
      "outputs": [
        "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.json"
      ],
      "status": "completed",
      "duration_sec": 180.0,
      "notes": null,
      "finished_at": "2026-05-20 18:20:30 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 18:19:30 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 0.0,
      "notes": null,
      "finished_at": "2026-05-20 18:19:30 +0200"
    },
    {
      "id": 5,
      "name": "semantic_validation",
      "llm": true,
      "model": "claude-sonnet-4-6",
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.pipeline-log.md#LLM_INPUT_STEP_5"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 30.0,
      "notes": null,
      "finished_at": "2026-05-20 18:20:18 +0200"
    }
  ]
}
-->

# Pipeline log v2

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19`
- **Source ID:** `system_design_senior_karpov_v1_2022_01_19`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 18:13:13 +0200
- **Last updated:** 2026-05-20 18:20:30 +0200

Фильтр в IDE: `*system-design-senior-karpov-v1-2022-01-19.v2*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/timecodes.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.pipeline-log.md` | — | completed |
| 2 | qa_extraction | yes | claude-sonnet-4-6 | `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.pipeline-log.md#LLM_INPUT_STEP_2` | `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.json` | 180.0s | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.validation-report.md` | 0.0s | completed |
| 5 | semantic_validation | yes | claude-sonnet-4-6 | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.pipeline-log.md#LLM_INPUT_STEP_5` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.validation-report.md` | 30.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.pipeline-log.md`

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
SOURCE_ID: system_design_senior_karpov_v1_2022_01_19
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:01] так алексей привет
[00:03] меня зовут валера сегодня с тобой
[00:06] пройдем замечательность на самом деле
[00:08] больше чем 45 минут 45 минут будет у
[00:10] зрителей возможно чуть больше а мостовой
[00:12] проведем может быть час с копейками по
[00:15] дизайнам какую-нибудь штуку интересно но
[00:17] прежде чем мы начнем дизайн какую-то
[00:20] штуку расскажи вообще почему ты здесь
[00:22] что-то делаешь
[00:27] заявки вы принимали на собеседовании
[00:29] просто было скучно на уроке я решил
[00:32] отправить где сейчас учительница не ну
[00:35] ты не искал какой урок поэтому
[00:36] учительница
[00:37] не узнают да и неплохо на я написала то
[00:40] что
[00:42] стал победителем
[00:44] соревнования и джорни до который в этом
[00:48] году проходила а что там делал формально
[00:50] там
[00:51] международный конкурс по искусственному
[00:53] интеллекту для детей так и делать о том
[00:56] что у нас была задача у
[00:59] нас было две задачи я построил модель и
[01:03] проверять гипотезы чистил данные все
[01:06] такая задачка к да надо называлась
[01:09] официально подбор персонала у нас есть
[01:11] данные как описание вакансии
[01:14] вот заголовок вакансии какие-то еще
[01:17] табличные данные и надо было сначала
[01:20] предсказать что это за профессия а уже
[01:23] затем
[01:24] какую зарплату
[01:27] могут ожидать люди из этой вакансии
[01:30] забавно потому что в шестнадцатом году
[01:32] мы в команде в которое у нас тоже были
[01:35] школьники но сейчас он уже не школьник
[01:37] тоже учатся ли в хакатоне на вот точно
[01:40] такую же тему видишь прошло пять лет
[01:42] задачах которых не изменились видимо эта
[01:45] проблема еще нормально не решена во
[01:47] первых когда мы так и не сказать чем
[01:50] nexia занимается алексей заниматься тем
[01:52] что у час вадинском классе и заканчивает
[01:54] школу но понятно уже мы видим как он
[01:56] учиться на уроках что
[01:58] браузер в интернете подает заявки в
[02:02] разные места побеждает конкурсах что на
[02:05] сегодня собеседование обычно вообще на и
[02:08] собеседование приходят люди сеньор на
[02:11] уровне или которые думают сеньор но
[02:12] уровни но мы решили попробовать конце
[02:14] концов что мы теряем
[02:15] получаем какой-то мы будем дизайне
[02:20] систему с технической точки зрения то
[02:23] есть не про м.л. а
[02:24] что в не должно быть какие компоненты
[02:26] какие сервисы как аниме что мы должны
[02:29] общаться сколько мы должны
[02:32] железо подкопать какие базы данных и так
[02:35] далее так далее так далее
[02:36] для меня это было одно из самых
[02:39] интересных то же время сложных
[02:41] собеседований потому что она бесконечно
[02:42] длинное а сложно насчет тем что тебе
[02:45] придется здесь солировать то есть я
[02:47] задаю вопрос даю какието водные а дальше
[02:51] на 40 минут я в идеальном случае
[02:53] замолкаю идеально случае никогда не
[02:56] будет и вишь ты немножко брикс все будет
[03:00] хорошо
[03:01] поэтому предлагается разно чать не
[03:04] тратить много времени задача следующий
[03:08] сервис который делает короткие ссылки то
[03:13] есть человек приходит
[03:15] тайне url или short url я не знаю
[03:18] пользоваться и тогда сервисами которые
[03:19] сокращают ты заходишь или пользователь
[03:22] заходит кидает длинную ссылку не удается
[03:25] короткая ссылка то есть он кидает
[03:27] условно их нибудь 100 символов ему
[03:30] выдается тайне url slash какое-то
[03:35] количество небольшой символов и дальше
[03:38] когда другой человек в этой ссылке
[03:39] кликай товаре директная оригинальный url
[03:42] ну и собственно что еще можно сказать
[03:46] это все будем считать что это глобальный
[03:49] сервис которым пользуются по всему миру
[03:51] нужно чтобы человек мог зайти крикну
[03:53] посылки его на эту ссылку и директ на
[03:55] оригинальную либо человек мог получить
[03:57] сокращенную ссылку
[04:00] я сразу вы пользователь сможет
[04:02] пользоваться
[04:04] что съесть получается
[04:08] с длинной ссылки
[04:14] мы должны получить короткую да и при
[04:18] этом короткая будет начинаться будет
[04:21] принадлежать по идее
[04:25] наши базе данных что ночь будет общий
[04:30] вот той не будет той неверно например
[04:36] the ural у нас будут для каждой ссылки
[04:38] да ну да и потом идет слеш и дальше уже
[04:42] наша
[04:45] укороченная версия
[04:48] что мы из этого понимаем у нас есть вся
[04:52] мы по сути любая ссылка
[04:55] мы должны перенаправить каким-то образом
[04:58] перенаправить в нашу базу данных
[05:01] но таким образом чтобы не понятно будет
[05:05] у каждого индивидуально я
[05:06] получается
[05:08] приезжает любая ссылка каким-то образом
[05:12] шифруется как-то переставляются наши
[05:15] символы дается в более укороченным видим
[05:18] значит
[05:22] понятно что если будут две одинаковые
[05:25] ссылки
[05:26] ну каждой длинной ссылки со должна
[05:28] соответственно соответствовать короткая
[05:31] ссылка каждая короткая ссылка
[05:32] если только не
[05:35] введены какие-то ограничения по времени
[05:38] хороший вопрос пусть пусть у нас живет
[05:41] каждая короткая целка не более двух лет
[05:44] ограничения по времени
[05:52] два года у нас
[05:55] значит по истечению двух лет вот этот
[05:59] наш
[06:01] какая-то последовательность уникальная
[06:04] освобождается и может занять в общем
[06:07] другой какой-то адрес
[06:09] это хорошо
[06:11] значит у нас будет
[06:14] [музыка]
[06:16] мы
[06:19] можем рассчитывать на
[06:21] то что наша база данных будет конечно
[06:25] увеличиваться но не так быстро
[06:28] то есть хранить ничего не надо
[06:30] бесконечно и получается что мы
[06:37] сможем использовать эти
[06:39] последовательности которые уже ранее
[06:40] были за но это тоже не плохо значит
[06:45] сможем
[06:48] использовать
[06:54] ну скажем просто старую ссылку скажем
[06:57] так
[06:59] ссылку снова
[07:01] короткую суп до
[07:07] короткую а
[07:10] если задуматься над короткой ссылки
[07:12] интересует только последние уникальные
[07:15] значению продавить все остальное у нее
[07:17] одинаково . да ну то есть они
[07:19] естественно да мы говорим вот про эту
[07:22] часть наших назовем это ключом
[07:24] хорошо кибу и
[07:29] значит у нас
[07:34] понятно что будет укороченную ссылка но
[07:36] насколько
[07:38] насколько укорочены в нашем интернете
[07:43] может быть
[07:44] любой длины ссылка а здесь если мы
[07:48] делаем более короткую версию то мы можем
[07:51] вставить ограничение не то что ключ
[07:55] любой ключ должен быть 20 или
[07:59] уменьшать количество по счету если мы же
[08:02] мы же четко можем сказать сколько
[08:03] символов нам позволяет сколько
[08:05] уникальный ключ и создать правду да и
[08:08] выбрать алфавит и там после этого все
[08:10] такое понятно вот в каком смысле
[08:12] короткая то что она будет короче чем то
[08:17] понятно но
[08:19] длинный тоже бывают разные если там
[08:22] 10-10 не длинная допустим 20
[08:25] здесь длина ключа это длинное и 100 а
[08:29] тут сайте ключи так здесь домен тоже
[08:32] является ключом здесь как минимум домен
[08:34] будет плюс все что угодно после домена
[08:37] так что она может быть очень длинная да
[08:40] вот здесь у нас разные длины
[08:44] вот о чем надо подумать в каком смысле
[08:49] будет короткой в относительном или в
[08:51] абсолютном то есть мы можем либо для вот
[08:57] допустим для ссылки с в 100 символов
[09:00] делать допустим короткую u20 это будет
[09:04] carrot пусть будет у нас всегда ключ
[09:06] одинаковые 1 хорошо значит у ключа мы
[09:11] знаем
[09:13] вопрос какой
[09:16] фиксированная длина
[09:19] теперь
[09:21] вопрос в том как нам
[09:26] кодировать вот эти разные длины в
[09:31] последовательность в разные
[09:32] последовательности уже одинаковой длины
[09:36] до
[09:38] надо премьер взять если у нас но тут
[09:42] пусть будет да сто и двадцать
[09:47] мы должны преобразовать в уникальной
[09:52] [музыка]
[09:53] уникальные
[09:57] в уникальные ссылки но уже одинаковой
[10:01] длины пусть будет дан
[10:06] как мы это можем сделать
[10:09] у нас есть разные длинные как гомер как
[10:13] зная компьютер сайнс ты можешь
[10:15] привести любую вещь не фиксированные
[10:19] длины в вещь фиксированной длины
[10:26] не у нас есть не фиксированная длина
[10:30] мы делаем фиксированные значит мы что-то
[10:33] вычленяем
[10:36] дам из данных
[10:38] знаком ли ты с таким понятием как хэш
[10:41] функция хеширования
[10:44] мы можем про хэшировать и тогда
[10:47] кэширование у нас выдает всегда
[10:49] фиксированную длину
[10:51] мы произведем хэширование да и тогда у
[10:54] нас будет
[10:57] 5
[11:07] вот пусть как функции
[11:11] мы получаем действительно одинаковую
[11:14] длину и а какую
[11:18] вот я сейчас не вспомню ну ладно скажем
[11:21] так md5 хэш выдает нам
[11:24] 128 бит
[11:28] за двадцать восемь бит
[11:30] хорошо
[11:32] мы получили фиксированную наши длину
[11:35] теперь мы получили для каждого
[11:39] уникальная функция но здесь мы еще не
[11:41] совсем мы получили но 128 бит если это
[11:45] чисел кай выдавать это ну
[11:48] большая чисел k может быть можем ли мы
[11:51] как-то еще ужать это
[11:54] то есть я и я посоветую следующим
[11:57] образом мы мы с тобой сейчас не знаем
[12:00] какая нагрузка сколько она вообще нужна
[12:02] уникальных ключей 10100 1000 миллион
[12:05] миллиардов а вид я думаю нужно подумать
[12:08] сначала с того насколько же нам какая же
[12:10] у нас нагрузка ты сколько нам вообще
[12:13] нужно ключей в пределе
[12:17] мы можем это вычислить так предполагаем
[12:21] что у нас
[12:23] мы можем очередь это
[12:27] подумаем сколько у нас за прошлый день
[12:30] может быть
[12:32] ну вообще у нас есть два типа запросов
[12:36] во-первых начнем центру у нас может быть
[12:38] сопровождаться то можно воспользоваться
[12:41] поэтому мы сейчас говорим для начала про
[12:43] создать ссылку то есть у нас есть райт
[12:45] request когда мы записываем что-то эрид
[12:48] когда мы что-то считываем первый вопрос
[12:51] у нас сервис
[12:54] какую сторону смещен у нас
[12:56] преимущественно в рай 3 квест или редре
[12:57] квеста
[12:59] понятно что чаще переходить
[13:02] перед хайве хорошо это мы знаем это мы
[13:06] запомним
[13:09] получается да чаще переходим по ссылке
[13:13] но сначала про нагрузку общую подумать
[13:15] то есть у нас есть райт нагрузка ритм
[13:16] нагрузка подумал к ним
[13:19] если у нас считывается ссылка то что
[13:23] получается мы нажимаем на вот эту
[13:25] сначала подумать сколько мы ссылок
[13:27] создаем в день
[13:29] прикинуть числа допустим миллион миллион
[13:33] ссылку хорошо миллион целый день мы
[13:36] знаем что мы храним два года
[13:38] правильно
[13:40] то есть сколько у нас в базе должно быть
[13:43] ключей минимум миллион допустим пусть
[13:47] будет тысяча четыреста дней в году так у
[13:50] нас
[13:51] знаете сотру вот это у нас понятно у
[13:58] нас миллион да ссылок в день ну пусть
[14:02] будет
[14:04] типа год 400 дней для простоты
[14:07] вычислений и
[14:09] умножаем на 2 года получается у нас 10
[14:14] примерно такой
[14:21] ссылок у нас в базе данных
[14:25] ну и собственно за два года столько
[14:27] ссылок мы создадим
[14:30] получается для каждого
[14:32] до отвести свое место и как раз такие
[14:35] вот каждая ссылка будет у нас уникальный
[14:36] а теперь вопрос сколько места под это
[14:39] нужно да и ну допустим хотя зависит
[14:43] размер ключа на ключ у нас будет
[14:47] какой-то она обычно бывает ну примерно
[14:49] 15 подожди подожди не спешит смотрим
[14:53] прежде чем быть 1510 или восемь нас уже
[14:55] есть цифра 8 на 10 8 правда
[14:58] то есть мы в принципе уже знаем сколько
[15:01] у нас
[15:02] ключей в базе данных будет мы бы хотели
[15:05] конечно иметь некоторый запас то есть у
[15:07] нас одно из ограничений наш ключ должен
[15:11] поддерживать
[15:12] уникальный что многое зги не ровать этих
[15:14] уникальных ключей как минимум не меньше
[15:16] чем вот это количество
[15:18] нато если мы можем всего тренировать
[15:20] уникальных 10 6 ключей это наверно не
[15:22] хорошо
[15:23] если ты говоришь 15 символов сколько это
[15:26] уникальных ключей
[15:29] посчитай во-первых какой уфа вид как ты
[15:32] не раз говорил
[15:33] так мы должны прикинуть сколько у нас
[15:36] бит на один символ но пусть будет
[15:42] они там должно быть число определенную
[15:46] допустим я тебе дам подсказку что есть
[15:48] base64 encoding который позволяет тебе
[15:53] каждый символ имевшихся четыре варианта
[15:55] соответственно четыре варианта то это 2
[15:57] в шестой то есть это 6 бит рос бит у нас
[16:01] дано каждому на если у нас d64 теперь
[16:04] представим допустим у нас в этом до 64
[16:06] ключи 10 символов
[16:08] сколько это у нас вариаций у нас в ключе
[16:11] 10 символов у нас круче 10 символов
[16:14] каждый по 6 бит каждый до 64 позиция
[16:17] имеет к ну понятно если он имеется
[16:20] четыре вариации этого 640 не надо
[16:24] подождать
[16:25] из да у нас на каждый символ 664
[16:30] варианты значит 64 у нас 10 степи 10
[16:34] минут запишись от 450
[16:37] при
[16:39] ключа 10
[16:41] при ключе
[16:44] нашим
[16:49] 10 символом
[16:55] и 6 бит на символ
[17:03] 64
[17:04] 10 но это 2 в 60
[17:09] ну и сравним вот с этим например 2 60
[17:14] уникальных
[17:16] последовательностей
[17:19] 2 в 60 мы знаем что есть
[17:25] 82 в 3 до 10 8 у нас
[17:32] неплохо будет сравнить я рассчитаю не
[17:34] четыре в 10 читали очень хорошо но я
[17:37] точно знаю что 16 больше чем 10 правда
[17:41] но 16 больше чем 10 конечно значит а 16
[17:45] это 2 в четвёртой
[17:48] значит и 260 ты можешь представить как 2
[17:50] 4 еще в какой-то степени правда ну да да
[17:53] да то есть разбить это у нас будет 16 в
[17:57] 15 а тут у тебя 10 8
[18:02] ну то есть здесь прям сильно сильно
[18:05] больше
[18:10] сильно-сильно больше сильно сидим мы
[18:12] можем всех зачем нам нужно
[18:15] хорошо оставляем кодирование таким
[18:17] какого я найду это точно в даже от этого
[18:19] не станет у этого есть некоторые до 100
[18:21] грамм надо оптимизировать количество
[18:23] символов в
[18:25] нашей короткой ссылки
[18:29] тогда мы получим
[18:31] приемлемый для нас вариант
[18:33] ну что мы можем сделать мы можем просто
[18:37] подобрать
[18:38] например 8 сколько у нас тогда будет да
[18:41] у нас
[18:43] 4 8 это 16-го 2 4 у нас будет 64 до 8
[18:52] это у нас будет
[18:56] два в 48 то есть
[19:01] 16 в 12 но это тоже больше но уже лучше
[19:07] смотри ты уже у уменьшил количество
[19:09] место которое нам нужно на 20 процентов
[19:12] и при этом утечка падая
[19:14] что нам теперь для ключа нужно не не 10
[19:17] а 8 символов а
[19:19] это
[19:21] сокращение 20 процентов ну хорошо
[19:24] допустим мы подберем пусть 8
[19:27] удалит тут мы можем дальше уходить да
[19:31] зачем
[19:32] давайте пусть у нас
[19:34] длина
[19:36] нашего ключа будет восьмерка допустим и
[19:40] тогда у 82 больше 8б с 64 запиши чтобы
[19:44] мы не забыли до что у нас тренировка то
[19:47] что может это восемь бит и мы тоже не 8
[19:49] бит правда это скорее 48 бит
[19:54] хорошо мы
[19:56] подготовили нашу базу данных
[20:00] мы знаем то что у нас все будет
[20:05] нормально с количеством ссылок
[20:07] нужно ли как кодировать ну то есть при
[20:10] помощи кэширования устраивать мы не
[20:13] совсем знание делегировать еще почему
[20:16] потому что мы посмотрим у нас удается
[20:17] 128 бит а
[20:19] берем мышцы от 4
[20:22] даже читать 448
[20:25] потому что писали что им до 5 даёт нам
[20:28] 128 md5 md5 хэш а потом мы берем боишься
[20:33] 4 а нам относят 4 нужно всего 48 бит
[20:36] нужно всего лишь 48 бить но мы можем
[20:40] использовать другой тип расширении мы
[20:41] любим пошел сможет взять 1 48 бит или
[20:44] просто dotech не нужен но это
[20:47] увеличивает риск коллизий
[20:48] запишем пока это перейдем к этому
[20:52] что можем увидеть риска литий ну понятно
[20:56] что если мы хэш как-то обрезаем хэш сам
[21:00] по себе имеет возможность коллизий если
[21:03] хошь еще уменьшать но представь что мы
[21:06] хэш берем один бит понятно что у нас
[21:08] может быть много ходить закончить
[21:12] эти при урезанном хэширование мы вообще
[21:15] при любом на урезанная просто повышает
[21:17] этот риск
[21:27] а вот мы с тобой это делаем на лету то
[21:30] есть нам приходит какая-то ссылка
[21:31] мы ее через хэш мы верим от него 1 48
[21:34] бит переводим это в 60 боишься 4 и
[21:38] говорим это уникальный ключ ну и пихаем
[21:41] потом наверное как искал в себе в базу
[21:42] данных а
[21:45] затем как 4 это другой вопрос но этому
[21:50] придем а можно ли вот эту всю систему
[21:53] обряд нас есть риск ализе то есть к лизе
[21:56] их нужно как-то решать это неприятно а
[21:59] вот если задуматься а можем ли мы как-то
[22:02] заранее подготовиться и на летун
[22:05] генерировать ключ а
[22:07] просто что-то уже заранее подготовлено
[22:10] использовать можно использовать
[22:12] структуру дерева возможно и не ты ты
[22:17] куда-то в сложные вещи уходят как
[22:20] подготовиться заранее когда вот и ты
[22:22] ключ на ли тут же с генерируешь к мужу
[22:24] начинали ту мы взяли хэш от
[22:26] оригинального урла
[22:28] от этого хэша взяли первые 48 бит эти
[22:32] первые 48 бит превратили в себя 4
[22:34] прилепили сказали это ключ но есть риск
[22:37] alizee здесь правда ведь потому что
[22:39] может быть так что два разных url они
[22:42] могут по md5 в коллизию попасть ну а мы
[22:45] говорим по первым 48 у них еще выше
[22:47] может даже посчитать на сколько раз выше
[22:49] риск ализе
[22:50] многократно но можно ли как-то
[22:53] подготовиться так чтобы на лету не
[22:55] считать и коллизии миновать если мы не
[22:58] считаем на лету это значит по сути нам
[23:01] по сути мы не используем хэширования это
[23:04] сразу
[23:06] почему нет
[23:10] потому что это
[23:12] самый первый вариант ну хорошо представь
[23:15] я посчитал заранее тысячах и шеи вверх
[23:18] могу заранее посчитать тысячам просто
[23:20] генерировать какие-то последовательности
[23:22] 60 через 48 бит а
[23:25] потом просто каждый раз брать
[23:28] этот ключ кидать его брате кидать брать
[23:32] кидать врачи дать на той сумме 100
[23:34] ключей меня по меня просят генерирует
[23:36] ссылку я беру первый ключ вычеркиваю его
[23:38] потом не просят сгенирировать ссылку я
[23:40] беру второй ключ с у меня уже где-то эти
[23:42] ключи лежала мы сначала сгенерировали
[23:45] вот у нас есть уже какие-то ключи но мы
[23:48] можем мы же сможем брызги не ровать
[23:49] любые последователи включи правда вопрос
[23:52] мы делаем рандомный генератор конечно и
[23:55] кидаем откуда-то то есть заранее мы
[23:59] знаем что там будут приходить ну вообще
[24:01] лучше записывать хэш сразу ну по
[24:05] надобности а почему помнить базу данных
[24:08] ну
[24:09] сколько вот это будет занятие допустим
[24:11] мы захотим section хранить заранее все
[24:14] ключи сколько это место займет займет
[24:16] все места которые нас есть сколько
[24:18] посчитаем сколько места можно у нас ключ
[24:20] занимает 48 бит сейчас до 48 у нас
[24:27] шесть байт занимает на символ шесть байт
[24:30] до 8 символов по шесть байт 48г шесть
[24:35] байт он занимает сразу же есть 40 а у
[24:37] нас есть смотрю нас прежде на 8 6 бит 0
[24:42] до 6 байт ну ладно только запиши 66 b6
[24:47] байта марок на один ключ таблицы
[24:51] но если получается у нас настолько то
[24:56] ссылок мы посчитаем сколько нужно просто
[24:58] сколько нам нужно хранить место
[25:03] мы должны занять все так 66 дней на
[25:07] жопами который у нас есть шесть байт
[25:09] умножаем на 10 в 8 на 8 это получает
[25:12] сорок восемь байт на 10 8 правильно
[25:14] сколько это место
[25:18] в каком смысле ну сколько памяти мне
[25:21] нужно чтобы хранить все эти ключи
[25:24] столько посчитаем 48 на 10 8 байт это у
[25:30] нас что сколько это кино ну допустим это
[25:32] у нас хорошо прикинем 50 на 50
[25:37] получаем у нас
[25:40] пятеркой 90 и интер мы должны с излишком
[25:44] хранить окажи сколько это у нас
[25:46] получается
[25:49] то очень много вот сколько много сколько
[25:52] это килобайт просто и разделе опять на
[25:56] 10 6 правда особо мире обалдения еще
[25:59] делим 5 на 10 в 3 то есть это что 5
[26:02] гигабайт
[26:04] на все ссылки но не выглядит как при
[26:07] реальных конечно громить и правда ведь
[26:08] мы можем же использовать меньше так
[26:11] зачем 5 гигабайт слушают можно на
[26:13] macbook хранить оперативки
[26:16] ну при задержке а ну да если у нас будет
[26:20] система даже одновременно использоваться
[26:22] с миллионами пользователей то
[26:24] поиск по базе данных будет
[26:28] это мы про это близко там уже вот вот
[26:30] вот эти 5 гигабайт кажется что но можно
[26:32] держать прям где угодно при желании это
[26:35] вообще я по нему это было пять петабайт
[26:37] но мы сейчас от него нечестным делать но
[26:40] это миллион раз меньше чем пять петабайт
[26:43] в принципе не что нам не мешает заранее
[26:46] же делать сгенерировать все ключи и но
[26:49] допустим мы сделали все ключи что нам
[26:50] нужно с ним делать теперь нужно каждый
[26:53] каждому ключу присвоить
[26:56] значение которое нам вводится ну по сути
[26:59] записать там словарь допустим снимал но
[27:03] нам вот эти ключи нам нужно наверно их
[27:05] хранить в двух местах в двух состояниях
[27:08] правда ведь у нас может быть ключ что
[27:11] может быть ключем сделан ключ у нас
[27:13] создается мы можем переходить на него то
[27:18] есть мы можем его либо использовать
[27:20] лениво либо он еще свободный да то есть
[27:22] нам это тоже нужно фиксировать каких-то
[27:24] таблицах
[27:26] здесь мы же не можем дать занятый ключ
[27:28] ссылки про конечно
[27:30] мы не можем это сделать
[27:34] почему бы не хранить что значит двух
[27:37] состояниях ну вот вот свободные и заняты
[27:41] ну да у нас будет получается
[27:43] дополнительно какой-то
[27:46] дополнительный тип данных который
[27:48] обозначает ну там есть дополнительный
[27:50] дополнительная ячейка то говорил равна
[27:52] таблицы заняты до занят ли адрес занят
[27:57] ли наш ключ или нет ячейка или все-таки
[27:59] 2 разных таблиц нам нужны не а
[28:05] это влияет значительно подумаем в чем в
[28:09] чем в чем плюсы в чем минус если это
[28:11] одна таблица но там есть какая-то ячейка
[28:13] на таблице у нас получается могут быть в
[28:16] ключи и
[28:17] состоянии то занят не занят так допустим
[28:20] это так тогда и мне нужно выдать новый
[28:22] ключ что я делаю я иду по всей таблице
[28:25] пока не встречая 1 незанятый ключ для
[28:27] это неэффективно а это соответственно
[28:29] карта как это будет у меня каждый раз на
[28:32] n операции где и на то количество уже
[28:34] созданных ссылок
[28:36] ну а
[28:38] если у меня есть табличка где я знаю что
[28:41] у меня все ключи не занята я получаю до
[28:44] туда могу брать первый ключ
[28:46] день а табличка ночи у нас есть 1 2 3 и
[28:51] ну допустим вот так вот надо производить
[28:54] линейный поиск да да и ну скорее всего
[28:57] мы будем то есть мы можем просто из
[28:59] таблички если ключи там все свободно
[29:02] брать всегда первый ключ делать констант
[29:05] на операцию то есть вмещать не занятые
[29:08] ключицу достаточно просто их за 1
[29:11] таблички убирать и
[29:12] сохранить власть во вторую торгуйся
[29:15] соответствие нам хранить и сделать
[29:17] только таблицу незанятых
[29:23] да ты у нас просто будет там
[29:28] хранится
[29:32] допустим этот самый ключ noise там
[29:35] хранится какие-то ключи и точно также
[29:37] есть таблица занятых да есть таблицы
[29:39] занятых но разве
[29:44] получается если у нас
[29:48] если у нас есть вся таблица про ключи мы
[29:52] можем разлить либо хранить две таблицы
[29:54] занятых незанятых и бы мы можем просто
[29:57] хранить одну огромную таблицу всех
[30:00] ключей и там таблицу незанятых допустим
[30:03] нас нет разницы если мы хранили зачем
[30:06] нам хранить отдано таблица всех ключей и
[30:08] одну таблицу не заняты ключи это тогда
[30:10] дублирование информации
[30:11] да просто вот тогда они заняты у нас
[30:14] самом начале будет
[30:16] будут все ключ к потом при заполнении
[30:19] нас проходит какое-то время и
[30:21] постепенно пополняются таблицы занятых
[30:24] так более того мы когда таблицу занятых
[30:26] мы что еще можем записать туда в таблицу
[30:29] занятыми мы можем да мы еще учитываем
[30:33] время и и
[30:36] и чем он занят да и как раз таки нашу
[30:41] ссылку то есть у нас тут получается уже
[30:44] дополнительные есть
[30:48] ячейке у нас будет самый ключ
[30:52] самый ключ у нас будет будет время и
[30:59] будет изначальная ссылка
[31:02] которая есть
[31:05] вот пусть bass будет названо
[31:08] затем
[31:12] хорошо но сейчас когда приходит запрос
[31:15] мы знаем какую таблицу идти с короткой
[31:19] ссылки на оригинал оправдают
[31:21] сkоро туда это понятно знаем там у нас
[31:25] спокойно мы смотрим по времени да и
[31:29] когда время заканчивается мы возвращаем
[31:31] в нашу исходную таблицу с этим у нас все
[31:36] отлажено ну хорошо попробуй теперь общую
[31:39] картинку нарисовать
[31:47] это мы учите когда у нас
[31:50] в таблице незанятых у нас все
[31:52] сгенерированные допустим в целом мы
[31:55] знаем 5 гигабайт да и
[31:58] когда у нас производится запись мы про
[32:01] ну понятно что мы делаем мы
[32:05] соответствие проводим с изначально нашей
[32:08] совы которые хотим закодировать на
[32:10] проводим с временем когда она была
[32:11] закодируем закодированы потому что у нас
[32:14] ограничено по времени это ссылка и так
[32:18] заполняется таблица занятых потом как у
[32:21] нас может обновляться таблицы незанятых
[32:23] нас убираются ключи либо добавляются те
[32:26] время которых уже прошло и
[32:29] при этом
[32:33] когда считывают когда считываются то
[32:37] просто
[32:38] считываются если коротким на ссылки на
[32:41] этом мы сразу переходим в таблицу
[32:42] занятых и потом переходим просто на bass
[32:48] только вот коллизий так к лизе у нас уже
[32:52] нет и
[32:54] поэтому все ключи сгенерировали заранее
[32:56] можно генерировать их без калязине как
[32:58] раз таки чтобы
[33:00] мы выровняли где мы мы сделали как раз
[33:04] таки заранее наш наше число которое мы
[33:08] прикинули и
[33:10] [музыка]
[33:12] получили хороший массив который у нас не
[33:15] будет никак
[33:17] выдавать какие-то ошибки и затем просто
[33:19] в таблицу заняты я просто перепроверяли
[33:22] себя вы теперь получаешь все хорошо ты
[33:24] знаешь в какую таблица брать ключ ты
[33:26] знаешь в какую то bluetooth тебе идти
[33:28] для redirect а
[33:32] попробуем расписать общей service pack
[33:34] верхнего уровня
[33:36] так что у нас есть
[33:39] изначально я ссылка
[33:41] с точки зрения того как пользователь
[33:44] будет но есть пользователи у него есть 2
[33:47] 2 2 10 которые может захотеть сделать
[33:52] эти пользователь
[33:56] он у нас может что сделать вещь сделать
[34:01] ссылку
[34:07] либо считать перейти по ссылке считай
[34:12] короткую
[34:15] тогда
[34:17] если он делает ссылку то у него у нас
[34:22] есть он к нам приходит на какой-то
[34:23] сервер все равно в любом случае он
[34:25] придет на один сервер правда рисуем
[34:27] сервер
[34:31] вот и у нас здесь есть значит таблица не
[34:34] не здесь у нас ничего нет таблицы у нас
[34:37] в какой-то базе данных банк данных может
[34:40] быть на этом сервере не может не быть на
[34:42] этой базы данных от отдельная сущность
[34:47] как он переходит допустим к серверу он
[34:50] обращается к серверу
[34:53] хорошо сервер ты все нормально рисовал
[34:56] нарисует что какой-то зергов
[35:00] все делает сервер
[35:02] значит каким образом он отвечает
[35:07] если он здесь делает ссылку то в этом с
[35:11] этим сервером
[35:13] что он получает от пользователя наш
[35:15] сервер
[35:17] исходную ссылку
[35:20] допустим
[35:22] назовем ее так он получает нашу исходную
[35:25] ссылку
[35:27] дальше это исходная ссылка на рисуем
[35:31] верхнюю равнину то есть можно не писать
[35:32] до исходной ссылки на сервер пойдет куда
[35:35] что сделать базу данных в 1 из 2
[35:41] а
[35:43] вот сделаем вот так
[35:46] обращается либо он будет писать либо
[35:48] читать правда ведь
[35:51] значит что у нас делает сервер сервер
[35:54] отправляет команду в базу данных именно
[35:58] в нашу
[36:00] таблицу ключей до ключей либо в таблицу
[36:04] занятых ключи ключи у нас незанятых
[36:08] здесь будет
[36:14] получается
[36:17] читать
[36:20] ну если не заняты то здесь на самом деле
[36:23] жаждать здесь на самом деле будет
[36:25] делаться
[36:26] райт request то есть он сначала ключ и
[36:29] забирает а потом он пива за раз а потом
[36:32] он пишет в таблицу и уже из таблицы он
[36:38] сейчас найти удобнее напишу
[36:45] еще нас пользователь
[36:48] если сделать ссылку либо считать
[36:51] короткую
[36:55] он отправляет запрос у себя на сервер
[36:58] наш ну и соответственно считать он идет
[37:00] в таблицу занятых правда да здесь
[37:03] конечно нас быть таблицы
[37:06] ключей которые уже заняты
[37:14] затем давайте сначала здесь
[37:19] записать у нас то есть надо сделать
[37:21] соответствии с незанятых ключей в наши
[37:24] ключи заняты добавить
[37:28] давайте запишем это добавить
[37:31] я вот так вот сделал у
[37:33] нас
[37:36] должен выдаваться ключ пользователем
[37:41] ключ пользователь ну вот наша ссылка
[37:45] не суть важно и
[37:48] тот же самый ключ у нас будет
[37:51] записываться в уже таблицу занятых да то
[37:54] есть но как именно будет записываться
[37:56] наш ключ
[37:58] будет записываться время и
[38:04] исходная ссылка
[38:06] [музыка]
[38:09] на это при помощи
[38:12] нет мы это сделали до этого хэширования
[38:15] поэтому здесь уже когда пользователь
[38:17] использовать наш сервер то этого нет так
[38:21] смотрю на все есть верхний уровневый
[38:22] сервис верхние уровни он он плюс-минус
[38:26] работает ясно пойдем чуть глубже на
[38:29] первый момент который нам еще нужно
[38:30] затронуть мы ж с тобой посчитали сколько
[38:33] нам нужно памяти место для таблицы
[38:36] ключей да но ведь для таблицы занятых
[38:39] ключей нам нужно совершенно другое
[38:41] количество места правда ведь почему и
[38:43] сколько места нам нужны она занимает
[38:46] занимает память еще время и исходная
[38:49] ссылка которая сколь ранить
[38:54] если мы там отправляем сколько было у
[38:57] нас
[38:58] над голубым сила 8 на 10 8 запросов 8 на
[39:02] 10 8 запросов за 2 года до
[39:06] и
[39:07] ну и рано или поздно нас таблица занятых
[39:09] заполнится как раз этим количеством
[39:10] правда надо полностью мы должны это она
[39:14] должна быть даже желательно чуть больше
[39:15] у
[39:16] нас будет добавляться наш ключ по памяти
[39:19] который обнимает ну ключ-ключ время
[39:24] знаем ключи это уже 5 гигабайт да у нас
[39:27] есть можно должны мы еще оставить место
[39:29] для времени и для исходной шилки
[39:32] исходная ссылка у нас сколько будет
[39:34] занимать среднем если у нас занимает
[39:37] короткая сколько на почитали шесть байт
[39:40] часть байт давно занимает короткая а
[39:42] исходная сколько может среднюю занимать
[39:44] и надо разобрать средние но мы можем
[39:48] предусматривать что какое-то
[39:49] максимальное количество мне-то какая
[39:52] разница все мы мы мы мы же сейчас
[39:54] оцениваем не схему данных и мы говорим
[39:57] там хранится строка строка может
[39:59] произвольной длины правдой но нам же
[40:02] нужен пример сколько нам памяти нужно
[40:03] под базу то есть если мы сейчас точно и
[40:05] что нужно пять терабайт окажется пять
[40:07] петабайт это проблема ну вот у нас эта
[40:11] строка в среднем сколько можно занимать
[40:14] опустим
[40:15] тридцатку 30 байт или больше
[40:21] пусть 100 байт ну вот мы должны взять я
[40:26] как хотел должны ведь максимальное ну
[40:28] визуально может быть и 500 байт эти
[40:30] такой но в средам же в среднем нужно на
[40:33] живот 8 на 10 8 будет этих сук ну ссылки
[40:36] 500 байт
[40:38] со всякие те метки переходы тогда если
[40:41] мы верим в средней этому уравновешено но
[40:43] если у нас произойдет там какая-то атак
[40:47] а вот про это мы поговорим
[40:49] но если дать ему не успеем уже по
[40:51] говорится вот 100 байт средняя ссылку на
[40:53] flash с тобой сколько нам нужно место
[40:56] вступает у нас на
[40:58] одну ссылку да у нас столько запросов
[41:03] мужчин рассмотреть получше проще
[41:05] посчитать его как мы знаем что у тебя 5
[41:08] гигабайт это при ссылке в шесть байт
[41:10] правда
[41:11] ну и соответственно нас тобой да у нас
[41:14] больше это но в 7 раз допустим но не в
[41:17] 717
[41:18] если 100 разделить на 6 получается 16.6
[41:23] получается поэтому 17 на 5 17 у нас
[41:27] сколько
[41:29] 8 5 гигов + 5 получаем 90 но это еще
[41:34] никита без времени время сколько
[41:36] занимает время что мы должны
[41:40] допустим с момент вот сделаем отсчет
[41:44] времени у нас
[41:47] с того момента времени когда первый
[41:50] пользователь наш новый имидж unix тайме
[41:52] хранится делаешь петрограда можем
[41:54] сэкономить ну вот что ты жадный сколько
[41:57] хорошо вот uniq ставим сколько это
[41:58] займет
[42:00] ну сколько
[42:02] указываете вниз то я не значит ну
[42:04] сколько четыре байта да пусть 8 найти 10
[42:08] лет здесь ну ладно это еще 10 гигов да
[42:13] не так критична ну то есть суммарно
[42:15] печали 100 гигов на мгновение
[42:18] так все мы знаем что это 100 гигов
[42:24] на таблицу занятых ключей нет на общем
[42:28] на таблицу на нет ключей на общее 5
[42:31] гигов нужен на незанятых
[42:33] ну смысле у нас было 5 гигабайт 155 одна
[42:38] таблица единство другая
[42:41] но она мы же будем записывать постепенно
[42:44] почему у нас будет 5 гигабайт незанятая
[42:48] таблицы и ключи было столько же там
[42:51] занимать мы же будем
[42:53] короля те заодно и сохранять другую
[42:56] конечно можно сказать что мы хотим
[42:57] сэкономить 5 гигабайт ладно это может
[43:00] конечно суммарно 100 гигабайт потому что
[43:01] мы из одной перезаписываем другое но
[43:03] допустим хорошо
[43:05] с допустим мы сэкономили бы
[43:09] получили 100
[43:12] вообще-то также можно хранить на компе
[43:15] до сих пор нет ну отдельно купить какой
[43:19] то комп и подниму все хранить но
[43:23] мы сейчас с тобой нарисовали эту
[43:25] картинку это у нас как раз реализовано
[43:28] ровно на одном компе
[43:31] теперь представьте что она же может быть
[43:33] это реализовано до инфраструктуры для
[43:35] нас больше одного компа потому что мы
[43:38] например я сейчас хочу сказать у нас мы
[43:41] до сих пор не знаем как у нас запросов в
[43:43] секунду
[43:46] поэтому мы можем это посчитать
[43:49] еще нас да просто прикинем тут
[43:53] ты ж сам сказал сколько у нас там в день
[43:56] запрос
[43:57] миллион на создание на миллион на
[44:03] создана запись миллион на запись
[44:04] миллиона записи на сколько секунд но
[44:06] 100000 пусть будет 86 лет четыреста и
[44:09] любишь округлять ладно пусть 100 тыс у
[44:11] нас будет более 100 тыс секунд
[44:14] до так и сколько запросов в секунду
[44:17] значит если
[44:19] если у нас столько запросов 100000 это у
[44:22] нас есть 5 на получаем 8 тысяч за просто
[44:26] че это за два года у нас в день таскал
[44:28] миллион а в день у нас точно ошибся в
[44:32] день у нас миллион вопросов и получаем
[44:34] 10 запросов в секунду так 10 запросов на
[44:37] запись запиши
[44:39] но ты мне сказал что у нас это рид
[44:42] хайдер то есть у нас на чтение будет
[44:44] больше запрос
[44:45] да
[44:49] на считывание
[44:53] это у нас на запись сделать
[44:57] короткую ссылку
[44:59] отсчитывать мы как часто будем считывать
[45:04] получается у нас один пользователь
[45:07] делится вообще всем
[45:09] создают одну ссылку и кто ты сам стал
[45:12] что мы чувствуем гораздо больше чем да
[45:13] да насколько просто это будет получается
[45:18] по всему
[45:20] окружению допустим идти ну пусть 100
[45:23] запросов на 100 раз чаще не до 1000
[45:26] запросов в секунду
[45:27] 1000 куб с
[45:30] напишите пия зачем приперся концы забрал
[45:34] у нас gps и
[45:37] можно поставить слеш r
[45:40] назад на на чтение точно также кпс w
[45:44] согласить гораздо быстрее так писать не
[45:48] gps на
[45:50] g5 от друга и
[45:55] ну вообще это возникает вопрос и сколько
[45:57] один сервер способен держать connection
[45:59] of
[46:02] участь мы должны держать все подключения
[46:04] у нас и на записи на считывания 3 второй
[46:07] момент ты не спросила меня на эти скажу
[46:10] что мы хотим чтобы latency было у нас
[46:13] небольшая 200 миллисекунд донецка но
[46:17] будет би си джи из этой посылки 10
[46:19] секунд переходит
[46:21] но если у нас производится задержка 10
[46:24] секунд мнимых нас это будет бесить этим
[46:26] 200 миллисекунд 200
[46:28] хорошо у
[46:30] нас 200 миллисекунд получается мы можем
[46:34] делать у
[46:38] нас получается когда мы переходим уже
[46:41] посылки то есть это относится к
[46:44] считыванию у нас до их записи
[46:48] каким быстро персонально просто мои
[46:50] пишешь быстро записать
[46:51] в целом их этим сервисом работать
[46:54] довольно быстро понятно но мы можем в
[46:58] принципе человек когда переходит по
[47:00] ссылке может не так много времени
[47:03] может подождать побольше времени к этому
[47:06] записывала запись допустим хорошо но 200
[47:09] миллисекунд мы хотим нарядить там чуть
[47:10] побольше не будет хотя с другой стороны
[47:13] мы знаем что нас считывают 100 раз чаще
[47:15] и
[47:21] мы
[47:23] получили нашу задержку так на этом мы
[47:26] сейчас тогда уже не успеем 145 не
[47:27] заканчивается будем сейчас разбирать
[47:30] садись расслабляйся молодец что мы
[47:34] сделали с тобой мы с тобой записали
[47:36] система для одной машины правильно в
[47:39] принципе 0 пользователь что-то там
[47:41] делает куда-то обращается теперь
[47:44] подумаем если бы мы хотели она во-первых
[47:47] я записал некоторые советы тебе на жизнь
[47:51] но сначала 1 мне понравилось я
[47:54] думаю тебе нет на кратно говорили что
[47:56] когда я был в твоем возрасте и такого не
[47:59] делал говорили такой час калека ну как
[48:02] понятно когда как иногда говорят разные
[48:04] вещи на говорили тебе такое конечно ну
[48:06] вот не буду тогда повторяться
[48:09] в целом значит первое что нужно всегда
[48:11] сделать когда ты дизайнер системы есть
[48:14] такая вещь как cup теорема не все с ней
[48:18] согласна есть на самом деле
[48:21] адаптированы весе по царь теорема она
[48:24] заключается в том что мы когда строим
[48:26] сервис мы задумаемся какие вещи не
[48:28] должны быть constic консистентной
[48:31] доступность или надежность каким-то
[48:34] разрывом
[48:35] соответственно это тоже ну что
[48:37] разговорить мы хотим чтобы у нас была
[48:39] высокая доступность
[48:41] быстрая скорость ну и про консистентная
[48:45] для нас это не столь важно хотя тоже
[48:48] было бы неплохо себя по данной ссылке
[48:50] человек переходил в одно и то же место
[48:51] ты тоже нужно как-то
[48:54] организовать и
[48:56] мы с тобой производили расчетах хук нам
[48:59] нужно место и прочего в самом самом
[49:00] самом конце уже какую ссылку на запрос а
[49:03] вот мы сейчас считаем сколько запросов в
[49:05] секунду сколько нужно памяти поэтому
[49:07] первое что ты спрашиваешь это условно
[49:09] нужно cup ограничение но это прям
[49:12] буквально одну секунду потом ты
[49:15] производишь
[49:17] расчеты а
[49:19] расчеты какие какой куб с
[49:22] сколько памяти все это и водный
[49:27] соответственно 5 гигабайт сразу понимаем
[49:29] а можем хранить не можем хранить дима
[49:30] это обще можем хранить
[49:32] дальше я сама переходим к вопросу о
[49:35] масштабируемости то от нас есть
[49:37] пользователь а
[49:39] мы с тобой обсудили что он может быть
[49:43] много где
[49:44] соответственно глобально по миру
[49:46] раскидано для того чтобы обеспечить 200
[49:49] миллисекунд у наверное хотим чтобы
[49:52] пользователи из аргентины работал
[49:54] сервером южной америки не будет работать
[49:56] сервером сервером в европе то мы можем
[49:59] посчитать что только на это у нас идет
[50:01] какая какое-то количество времени потому
[50:03] что есть даже скорости рст ранения
[50:06] сигнала как ограничение соответственно у
[50:09] нас пользователь должен идти наверно
[50:10] какой то
[50:11] load balancer
[50:14] балансировщик нагрузки
[50:16] знакомый тебе это понять конечно воды
[50:19] соответственно понять что убил enter на
[50:20] самом деле ни один их так я нарисую что
[50:22] их несколько
[50:23] дальше у нас есть
[50:26] какой-то сервер и соответственно у нас
[50:28] есть как мы сказали у нас есть райт
[50:31] request и у нас есть
[50:34] ридриг вес так запишем дальше у нас есть
[50:36] сервер
[50:41] новый понятно что он тоже у нас
[50:44] несколько
[50:45] возникает вопрос этот сервер если он
[50:48] что-то считывает если мы считаем это из
[50:51] таблицы мы из этой таблицы
[50:55] считывать будем если это какая-то
[50:58] сирийской аль таблица но летчика 2 за
[51:01] можем долго это считывать поэтому мы это
[51:03] каширу им
[51:04] в принципе мы вообще посчитали что можем
[51:07] все кэшировать на самом деле нам в
[51:09] принципе
[51:10] стол столько памяти что мы можем все все
[51:13] в кэш пихать поэтому первое что он идет
[51:16] он идет в кэш
[51:18] это если ридриг вас правда ведь понятно
[51:22] что райтер квеста не может войти в кэше
[51:23] он
[51:24] пошел в кэш
[51:26] если он в кэш конечному либо возвращает
[51:30] что-то и он возвращает либо как говорит
[51:34] ничего нет и
[51:35] тогда мы мы можем из кэша идти можем
[51:39] отсюда идти на
[51:43] на что мы идем вот у нас редре квест в
[51:47] кэше этого нет мы идем в нашу таблицу
[51:59] вопрос какая у нас должна быть таблица в
[52:01] таблицу мы идем по ключу же правильно
[52:04] соответственно нам не нужна какая-то
[52:06] реляционная база данных нас устроит
[52:07] какая то но у сиквел система киви лью но
[52:13] даже люди любой это может быть тайным а
[52:15] это может быть те кассандра все что
[52:18] угодно
[52:19] идем сюда
[52:22] но проблема в том что в принципе
[52:28] мы ведь можем здесь найти
[52:32] рид request а можем и не найти правда
[52:35] ведь потому что может быть не существует
[52:37] это орла
[52:39] поэтому дальше мы когда из базы данных
[52:42] если мы его достаём его кидаем в кэш
[52:48] ну и обратно отправляем либо
[52:52] либо мы отправляем
[52:56] not found может же такое быть
[53:02] теперь у нас есть какой-то key key
[53:05] generator сервис
[53:08] ноги генератор сервиса тоже таблиц
[53:11] поэтому мы чтобы не делать
[53:14] мы будем из него допустим н ключей брать
[53:20] ты хоть и в какой-то
[53:22] memory и
[53:25] уже из этой memory мы будем забирать
[53:30] почему это сделано потому что представь
[53:32] если у нас пошло в
[53:35] 10 в секунду может произойти коллизия
[53:38] могут захотеть захватить один и тот же
[53:40] ключ
[53:40] поэтому один тут же клим и ключи сначала
[53:43] выгрузим сюда и в оперативке будем лог
[53:46] ставить на ключ
[53:47] то есть мы делаем блок 1 снимает log
[53:51] если он
[53:53] идет дальше
[53:57] всё соответствует это более сложная
[54:00] система
[54:01] но
[54:03] она если ты посмотришь особо-то ну не
[54:06] отличается от того что я писал на одной
[54:08] картинке есть здесь добавился лот
[54:10] балансир дальше можно справить задать
[54:11] вопрос а данные как мы будем партиции
[54:15] ровать у нас же сервера мы в принципе в
[54:19] нашем случае можем вообще все хранить
[54:22] везде
[54:23] потому что у нас весь раздел весь размер
[54:27] бас таких что нам даже птицы ровать
[54:29] ничего не нужно
[54:30] 100 гигабайт на 100 гигабайт мы будем и
[54:33] 200 от 6 гигов оперативы поставить
[54:35] вообще не проблема терабайт 2 терабайта
[54:37] можно поставить там мы тут говорим про
[54:39] 100 гигабайт на все то есть мы вполне
[54:41] можем это держать каких-то базах данных
[54:43] каких-то серваках
[54:45] это держать как постоянное хранилище
[54:47] понятно что
[54:49] мы здесь нужно будет держать какой-то
[54:52] реплику но в принципе мы каждый раз
[54:55] можем накажем серваке все это держать
[54:56] оперативки при необходимости и если мы в
[55:00] принципе все держим оперативки нам может
[55:03] быть вот особой конечно нужен потому что
[55:05] у нас все сразу оперативки лежит то есть
[55:08] я могу сказать вполне а мне и конечно не
[55:10] нужен узнаете
[55:12] почему мне конечно не нужен потому что у
[55:14] меня все все в кэш или же сразу все
[55:16] убрали лишний слой но мы можем это
[55:19] сказать только если мы знаем что на 100
[55:20] гигабайт поэтому горе вот у меня есть
[55:23] база данных я сначала записываю в нее из
[55:25] неё кидаю в кэш из-за меня машина
[55:27] ломается я
[55:29] просто перекидываю возникает вопрос
[55:34] значит нужно как-то синхронизировать мой
[55:37] вот здесь кэш если я все держу кгс или
[55:39] нет вот наверное вот эту часть я так и
[55:40] оставлю потому что это некий бушу я из
[55:43] таблицы подгружает периодически
[55:46] в оперативку и из нее уже всюду раздаю
[55:51] ну и соответственно я могу даже на
[55:55] каждую точку выгружать какие-то
[55:57] определенные ключи чтобы не было между
[56:00] ними никаких race conditions of ты
[56:02] словно говоря я могу еще вести
[56:04] дополнительную колонку
[56:06] в на какую тачку я какие ключи будут
[56:09] кидать в оперативку из нее выгружать
[56:11] правда ведь прикольно но я смогу так
[56:14] сделать соответственно мне что мне нужно
[56:16] просто из базы каждый раз на 1 каждую
[56:19] машину выгружать уникальные ключи и
[56:22] тогда у меня никакого лог скорее ну блок
[56:26] может по-прежнему нужно держать может не
[56:28] нужна простая к серверу к сервису этому
[56:30] достучался тут жизнь его выгрузил
[56:33] единственное что мне нужно потом сказать
[56:35] базе что база я вот эти оба за уже знает
[56:39] кстати база уже знает она уже эти ключи
[56:41] от себя вычеркнул а потому что мы уже
[56:44] загрузили сюда единственное что когда
[56:46] ключ был использован нужно будет
[56:48] сообщить
[56:50] вот этой базе
[56:52] соедините и ссылкой
[56:54] машина может упасть тогда те ключи
[56:57] которые не оперативки записаны
[57:00] пропадут но это не страшно будем здесь
[57:02] мы держать и допустим
[57:04] сколько ты говоришь тебе нужно 10 в
[57:07] секунду здесь можем держать
[57:09] на одном circus на здесь серваков мы
[57:13] пусть на одном серваке держим 10 тысяч
[57:14] ключей то нам на три часа хватит
[57:16] запаса каждый час мы еще подгружаем по
[57:20] по 3000 по 4
[57:23] ну собственно все в общем тебе нужно
[57:28] сначала еще узнавать про ограничения
[57:32] потом расчеты проводить сразу потому что
[57:35] дальше эти расчеты влияют на дизайн ну а
[57:38] дальше на самом деле здесь вот lancer то
[57:41] можно ставить здесь откровенно говоря
[57:44] уже даже не делал балансире может быть и
[57:46] на базу данных нужно может быть и нужны
[57:47] может быть мы хотим сказать что у нас
[57:48] будет несколько баз на разных машинах и
[57:52] мы будем их между собой синхронизировать
[57:54] но решать какой момент с какой из них
[57:56] достучаться и нам нужно будет еще один
[57:58] блок балансир вот здесь который уже
[58:00] будет дальше решать куда нам и тут у
[58:01] таки
[58:03] ну неплохо
[58:06] не знаю как тебе
[58:09] не понравилось
[58:13] 2
[58:16] ну что спасибо что пришел пасибо надеюсь
[58:20] не было и подругой на то здесь не было
[58:22] слишком большого стресса
[58:24] скорой встречи

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
Write JSON only to: splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. system-design-senior-karpov-v1-2022-01-19.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.json \
    --video transcripts/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.json --out splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.qa-split.json \
    --video transcripts/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.validation-report.md

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
video.md: /Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/video.md

--- CHAPTER `10:12` — Hash функции ---
window: 10:12 .. 11:55
recognition_status: single (1 items)

ITEM #2
  interviewer_question: time=10:12 text='Знаком ли ты с хэш-функцией? Как привести URL переменной длины к ключу фиксированной длины?'
  candidate_answer: time=10:44 text='Можно захэшировать URL — хэш всегда фиксированной длины (например MD5 даёт 128 бит). Дальше можно ужать до нужного числа бит и закодировать в base64.'
  reference_answer: time=None text=None
  interviewer_feedback: time=11:54 text='MD5 — 128 бит. Можем ли ещё ужать?'
  question_topic: Data Modeling

--- CHAPTER `11:55` — Расчёт нагрузки ---
window: 11:55 .. 19:55
recognition_status: single (1 items)

ITEM #3
  interviewer_question: time=11:55 text='Сколько ссылок создаём в день, сколько ключей в базе за два года хранения? Преимущественно read или write?'
  candidate_answer: time=12:59 text='~1 млн ссылок в день, храним 2 года → порядка 10^8 ключей в БД. Чаще переходят по ссылке (read-heavy), чем создают.'
  reference_answer: time=None text=None
  interviewer_feedback: time=13:06 text='Перед хайвей — хорошо, запомним. Сначала про общую нагрузку.'
  question_topic: Product Metrics

--- CHAPTER `19:55` — Про риски коллизии при хэшиовании ---
window: 19:55 .. 21:59
recognition_status: single (1 items)

ITEM #4
  interviewer_question: time=19:55 text='Есть риск коллизий при хэшировании и обрезании хэша. Можно ли заранее подготовить ключи и не генерировать на лету?'
  candidate_answer: time=22:10 text='При урезанном хэше риск коллизий растёт. Можно заранее сгенерировать пул ключей (например base64-последовательности) и выдавать по одному при создании ссылки — коллизий не будет.'
  reference_answer: time=None text=None
  interviewer_feedback: time=23:15 text='Представь: заранее посчитал тысячи ключей, при запросе берёшь первый свободный.'
  question_topic: Data Modeling

--- CHAPTER `21:59` — Альтернативный способ присвоения ключей ---
window: 21:59 .. 28:07
recognition_status: single (1 items)

ITEM #5
  interviewer_question: time=21:59 text='Альтернатива хэшу: как хранить свободные и занятые ключи — одна таблица с флагом или две таблицы?'
  candidate_answer: time=29:17 text='Две таблицы эффективнее: незанятые ключи — брать первый за O(1); занятые — ключ, время, исходный URL. Линейный поиск по всей таблице неэффективен.'
  reference_answer: time=None text=None
  interviewer_feedback: time=29:05 text='Просто убирать из таблицы незанятых и писать в занятые — константная операция.'
  question_topic: Data Modeling

--- CHAPTER `28:07` — Хранение ключей ---
window: 28:07 .. 33:33
recognition_status: single (1 items)

ITEM #6
  interviewer_question: time=28:07 text='Как устроить хранение: сколько памяти на пул ключей, нужен ли отдельный статус занятости?'
  candidate_answer: time=25:14 text='Ключ ~8 символов base64 → ~48 бит → ~6 байт на ключ; на 10^8 ключей ~5 ГБ. Можно держать все ключи заранее; при записи переносить из free в occupied с URL и timestamp.'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Data Modeling

--- CHAPTER `33:33` — Описание сервиса ---
window: 33:33 .. 38:28
recognition_status: single (1 items)

ITEM #7
  interviewer_question: time=33:33 text='Нарисуй верхнеуровневый сервис: пользователь создаёт или переходит по короткой ссылке — что делает сервер и БД?'
  candidate_answer: time=34:17 text='Пользователь → сервер → БД: при создании — взять ключ из незанятых, записать в занятые (ключ, время, исходный URL), вернуть короткую ссылку; при чтении — lookup в занятых и redirect на original URL.'
  reference_answer: time=None text=None
  interviewer_feedback: time=38:26 text='Верхний уровень плюс-минус ясен. Пойдём глубже — память для занятых ключей.'
  question_topic: Data Modeling

--- CHAPTER `38:28` — Расчёт места для занятых ключей ---
window: 38:28 .. 43:41
recognition_status: single (1 items)

ITEM #8
  interviewer_question: time=38:28 text='Сколько места нужно для таблицы занятых ключей (URL, время) при 10^8 ссылок?'
  candidate_answer: time=42:15 text='Исходная ссылка ~100 байт в среднем, время ~4–8 байт; на 10^8 записей порядка ~100 ГБ суммарно (ключи ~5 ГБ + URL + время).'
  reference_answer: time=None text=None
  interviewer_feedback: time=42:18 text='Суммарно ~100 ГБ на всё — можно хранить даже на одном компе.'
  question_topic: Product Metrics

--- CHAPTER `43:41` — Расчёт количества запросов в секунду ---
window: 43:41 .. 45:55
recognition_status: single (1 items)

ITEM #9
  interviewer_question: time=43:41 text='Сколько запросов в секунду на запись и на чтение?'
  candidate_answer: time=44:37 text='~1 млн write/день → ~10 write RPS; read примерно в 100 раз чаще → ~1000 read RPS.'
  reference_answer: time=None text=None
  interviewer_feedback: time=44:39 text='10 запросов на запись — запиши. Read-heavy.'
  question_topic: Product Metrics

--- CHAPTER `45:55` — Расчёт нагрузки на сервер ---
window: 45:55 .. 47:33
recognition_status: single (1 items)

ITEM #10
  interviewer_question: time=45:55 text='Latency ~200 мс, глобальный сервис — как масштабировать на несколько машин: load balancer, кэш, key generator?'
  candidate_answer: time=55:00 text='Load balancer → несколько серверов; read идёт в кэш, при miss — KV по ключу; write — key generator выдаёт блок ключей в RAM с lock, чтобы избежать гонок; ~100 ГБ данных можно реплицировать на все ноды.'
  reference_answer: time=None text=None
  interviewer_feedback: time=57:28 text='Сначала CAP и расчёты, потом масштабирование. Неплохо.'
  question_topic: Data Modeling

SAVE JSON: вставьте ответ в конец файла /Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v1-2022-01-19/system-design-senior-karpov-v1-2022-01-19.v2.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
