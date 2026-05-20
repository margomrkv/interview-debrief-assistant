<!-- PIPELINE_MANIFEST
{
  "version": 2,
  "basename": "system-design-senior-karpov-v3-2022-03-24",
  "transcript_folder": "transcripts/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24",
  "source_id": "system_design_senior_karpov_v3_2022_03_24",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 18:13:14 +0200",
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
    "json": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/timecodes.txt",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 18:13:14 +0200"
    },
    {
      "id": 2,
      "name": "qa_extraction",
      "llm": true,
      "model": "claude-sonnet-4-6",
      "inputs": [
        "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.pipeline-log.md#LLM_INPUT_STEP_2"
      ],
      "outputs": [
        "splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.json"
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
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 18:19:32 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 0.0,
      "notes": null,
      "finished_at": "2026-05-20 18:19:32 +0200"
    },
    {
      "id": 5,
      "name": "semantic_validation",
      "llm": true,
      "model": "claude-sonnet-4-6",
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.pipeline-log.md#LLM_INPUT_STEP_5"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 30.0,
      "notes": null,
      "finished_at": "2026-05-20 18:20:19 +0200"
    }
  ]
}
-->

# Pipeline log v2

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24`
- **Source ID:** `system_design_senior_karpov_v3_2022_03_24`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 18:13:14 +0200
- **Last updated:** 2026-05-20 18:20:30 +0200

Фильтр в IDE: `*system-design-senior-karpov-v3-2022-03-24.v2*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/timecodes.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.pipeline-log.md` | — | completed |
| 2 | qa_extraction | yes | claude-sonnet-4-6 | `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.pipeline-log.md#LLM_INPUT_STEP_2` | `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.json` | 180.0s | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.validation-report.md` | 0.0s | completed |
| 5 | semantic_validation | yes | claude-sonnet-4-6 | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.pipeline-log.md#LLM_INPUT_STEP_5` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.validation-report.md` | 30.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.pipeline-log.md`

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
SOURCE_ID: system_design_senior_karpov_v3_2022_03_24
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:02] жень привет это я рад тебя видеть мы как
[00:06] бы мог подумать в 2017 году когда мы
[00:08] вместе тащили осенью к рванут ирвинга
[00:10] что окажемся на двух стульях
[00:14] но оба нормальный будем с тобой
[00:17] обсуждать следующую историю расскажи
[00:20] тебя уже здесь спросили кто ты за na'vi
[00:24] тоже в 1 кто ты ну прямо сейчас я тимлид
[00:28] в команде машинного обучения в компания
[00:30] экспресс россия мы занимаемся матч янгом
[00:33] товаров то есть ищем наши товары которые
[00:36] есть на нашей площадке и находим такие
[00:37] же товары на площадках конкурентов вот
[00:41] непонятная монкада вариантов валик ну
[00:43] понятно те кто считают себя конкурентами
[00:46] или вот и соответственно передаем это
[00:49] тем людям уже которые занимаются
[00:50] выставлением хороших цен чтобы
[00:53] конкурентов и не было
[00:54] небезызвестный игорь котенков имеет
[00:58] отношение к этому да он вносит довольно
[01:01] значимый вклад то что это вся процедура
[01:04] происходит успешно у нас но я еще
[01:06] добавлю что женя по своей лени я так до
[01:09] сих пор не стал к белкам 500 грамм
[01:10] мастером хотя в него уже три золота и
[01:13] одно из них одно соло у тебя либо одно
[01:15] то на камеру это было в принципе на
[01:17] камере то есть ты не участвовал вместе
[01:19] со мной ильёй но и сам это было очень
[01:22] рисовать соревнования я там было по
[01:23] моему в топе лидер барда один и все
[01:26] остальные были в пятером да да в итоге
[01:28] на каком месте ты оказался тут опять
[01:32] на первый саммит и влетел в топ 3 пункт
[01:34] к ней было написано
[01:36] хорошо мы ты уже знаешь сегодня будем
[01:39] делать человек опытный system design
[01:41] тебе достается самая на мой взгляд
[01:42] сложная задача одна я сам сложно задач
[01:46] но я причем догадываюсь ты знаешь как
[01:49] ведет потому что эта структура данных
[01:51] задачу час от который висит игорю
[01:53] игорь привет за дизайне губер то есть
[01:57] это kolber сервис в котором люди
[01:59] вызывают такси садятся на него то есть
[02:01] нужно понимать где находится водитель
[02:03] при этом водитель может передвигаться
[02:06] где находится пользователь но
[02:09] пользователь может передвигаться на
[02:11] зачастую ну же из какое-то фиксированной
[02:12] точки вызывает
[02:14] он садится машинок он на них приезжает
[02:17] куда-то и заканчивается эта поездка есть
[02:20] пока водитель везет он недоступен для
[02:22] новых заказов а может быть и доступен в
[02:25] конце
[02:26] сервис работает по всему миру
[02:30] нагрузка
[02:32] высокая
[02:34] допустим пусть у нас будет
[02:38] он этот 500 пользователей и
[02:43] 5 миллионов водитель
[02:46] за дизайн пожалуйста нам систему но
[02:50] данное первое что сразу стоит заметить
[02:52] что в отличие от многих наверно других
[02:54] систем которые там какой-нибудь делаем
[02:56] какой-нибудь сервис twitter там youtube
[02:58] или еще что то то есть у нас сервис не
[03:01] глобальный в том смысле что когда мы
[03:02] пишем пост мы выпишем всем когда мы
[03:04] хотим как будто написать сообщение что
[03:06] ядрами мы пишем любому человеку в любой
[03:08] точке мира здесь же у нас основная
[03:11] особенно задача состоит в том что поиск
[03:14] водителя это локальность с точки зрения
[03:16] как дела локальная задачу то есть нам
[03:18] нужно найти водителя чтобы совершить
[03:20] поездку в каком-то месте естественно
[03:23] водитель должен именно из какой-то вот
[03:25] этой выборки
[03:26] водителей которые не очень далеко то
[03:28] есть нам не хочется ждать целый час
[03:30] водители сейчас бы там желтуха штук он
[03:32] отвез нас там десять минут я не поесть
[03:34] после этой записи
[03:37] вот спицын давайте поговорим сначала на
[03:40] требование к этой задачи которые мы
[03:42] хотим там рисовать до начала мы опишем
[03:45] функциональные требования что мы как
[03:48] пользователь мы умеем делать плюс здесь
[03:50] еще интересно что у нас пользователь на
[03:52] самом деле пользователь сервиса делятся
[03:54] на 2 категории потому что водители это
[03:56] тоже пользователь вот здесь у нас есть
[03:57] сервис с точки зрения пользователя есть
[04:00] сервис точки зрения водителя плюс сервис
[04:03] еще раз у нас разделен на скажем так
[04:05] real-time часть и но оффлайн то есть мы
[04:07] совершаем какую-то поездку в режиме
[04:10] реального времени и затем уже потом
[04:12] можем как-то отдельно послужить
[04:13] информацию то есть у нас будут две такие
[04:16] крупные части 300 которые происходят
[04:18] здесь и сейчас чтобы создать поездку
[04:20] отследить поездку завершить и затем уже
[04:22] сложить от какое-то for место поэтому
[04:25] опишем сначала функциональные требования
[04:27] что как пользователь как водитель мы
[04:30] можем делать с
[04:32] точки зрения пользователя
[04:36] пользователя которые именно пешеход
[04:38] будем считать значит первое что мы можем
[04:42] делать
[04:43] это указать
[04:46] то есть зайти в приложениям посмотреть
[04:48] сколько этом есть ли какие-то машины
[04:50] поблизости вбить какой-то адрес куда мы
[04:52] хотим поехать и затем начать поездку то
[04:55] есть первое вбить
[05:01] сбить порезку куда мы хотим наехать там
[05:04] второе найти водителя
[05:11] ну и затем у нас уже будет совершается
[05:14] поездка
[05:24] плюс там можно какой нибудь править
[05:26] информацию то есть условный профиль
[05:28] назову это например карты оплата менять
[05:31] что там ещё есть в яндексе там даже
[05:34] рейтинг сейчас есть и и пью райан
[05:37] творить
[05:38] 49 с копейками обычно
[05:44] так наверно из функциональные для
[05:46] пешехода боли меня все если что же тут а
[05:48] потом вспомним для водителя
[05:53] остается на водитель что он из
[05:56] пользователь совершает более такой
[05:58] разово действо водитель же он выходит из
[05:59] на смену и на смене он принимает
[06:01] заказывать то он может выйти на смену
[06:10] потом насколько понимаем этом прилетает
[06:13] такое уведомление что вот такой это
[06:14] заказ он может его принять или отклонить
[06:17] и по моему из за это штрафуют потом
[06:18] помоги деньгами к ментам социальным
[06:21] рейтингу принять повестку
[06:29] затем естественно происходит поездка
[06:38] в конце поездки статей пользователей
[06:41] водителями мама трейдинг поставить в
[06:42] конце там высвечиваются
[06:47] здесь тоже где то есть три с половиной
[06:51] ребенка после
[06:56] вот ну естественно на этом пск
[06:59] завершается он может вернуться либо на
[07:01] пункт 2 принять еще какой-то следующий
[07:04] заказ либо он может завершить мин на
[07:11] это с точки зрения мина функциональных
[07:13] требований какие функции наш сервис
[07:16] предоставляет пешеходам и водителям
[07:18] тем мы опишем
[07:21] не функциональные требования к зуб
[07:24] казалось бы причем здесь nrt
[07:29] нам как пешеходам не хочется ждать по 20
[07:33] минут когда на получится машина то есть
[07:35] хочется найти водителя поблизости
[07:47] ожидать недолго
[07:50] в целом это довольно пересекающийся
[07:52] вечер
[07:55] доступность конечно же все мы
[07:56] расстраиваемся когда нужно уехать падает
[07:59] яндекс такси не работает за ним
[08:01] старательно каскада начинают падать все
[08:03] остальные потому что ни к такому спайку
[08:04] не готовы
[08:06] поэтому доступность так но и с точки
[08:09] зрения водителя
[08:11] то есть как пошло от мы водитель с рядом
[08:15] мы его нашли ожидали не долго приехали
[08:18] вот но и всегда мы это можем сделать
[08:20] поэтому с точки зрения водителя ему
[08:24] хочется чтобы были заказы при этом
[08:25] заказа тоже были по близостью то есть
[08:27] строки для нервы заказывай поблизости у
[08:32] него не ждать недолго у него простая
[08:34] недолгий не хочется сидеть просто
[08:36] ношению
[08:42] но и доступность тоже как бы на него то
[08:45] есть если нам недоступно такси манометра
[08:48] поедем освободителю недоступным для xeon
[08:50] без денег будет сидеть
[08:57] у него с точки зрения не функциональных
[08:59] требований то есть и поездка там но это
[09:01] уже с точки зрения гео-локации наверно
[09:03] поиск совершается более-менее по
[09:04] оптимальному шутеру чтоб они жаловались
[09:06] что денег тратим много то есть
[09:09] оптимальность
[09:12] еще одно требование наверно которая бы
[09:15] выдвинул на котором даже яндекс такси не
[09:16] соответствует эту прозрачность
[09:18] вот почему если я проверил такси и
[09:22] обулся и она стала стоить 2 раза дороже
[09:24] хотелось бы объяснить это как-то ну я
[09:27] напишу это со звездочкой
[09:33] при этом если мы скажем водителя что
[09:35] что-то слишком дорого мы от них
[09:37] соответствующую историю в обратную
[09:39] сторону наверняка будем слушать в
[09:40] собственные через поездки
[09:44] но остается с точки зрения требований
[09:47] теперь давайте проговорим про наше
[09:49] эстимейт и того сколько все это место
[09:51] занимает какие прочность то что ты
[09:53] проговорил у нас есть сколько там 5 0 5
[09:57] миллионов пользователь родитель
[09:59] миллионов
[10:05] и 500 миллионов пешеходов
[10:11] понятно циклы здесь можно обсуждать
[10:13] может быть 301 в целом понятно что uber
[10:17] это как любой taxi service is помимо то
[10:19] что я посетил какую-то локальности в
[10:21] костре нет мы там вызываем заказ и нам
[10:23] нужен водитель который через 5 мы
[10:24] приедем понятно что мы скользящие будем
[10:26] ехать в рамках москвы там если мы здесь
[10:30] заказ возьмем и но и евро цена там не
[10:32] знаю такси в краснодар мы знаем вот
[10:34] поэтому все равно здесь ещё будет такая
[10:36] как бы первый уровень условно
[10:38] локальности это то что все равно сервис
[10:40] работает в каждом городе свой то есть
[10:41] когда мы подключаемся то есть мы сейчас
[10:43] только у них московском яндекс такси
[10:45] начинаю выбирать то есть мы можем в
[10:47] принципе вот это вот вещь сразу разбить
[10:49] то есть какой такой глобальный лот
[10:51] бенстер как который еще прям нашим
[10:53] клиентском приложении нас определяют что
[10:54] мы еще в таком-то городе и такси нам
[10:56] нужно искать исходя здесь например если
[10:59] мы возьмем
[11:00] крупную москву например то есть у нас
[11:03] есть
[11:04] 10 миллионов пешеходов и
[11:08] на миллион водители 500000 сколько их но
[11:12] здесь соотношение было один к ста ну
[11:14] значит будет столько водителей
[11:21] по поездкам мы будем считать что каждые
[11:24] 10 совершает поездку в конкретный день
[11:26] то есть есть один миллион
[11:30] или the fathers напишем но в целом там
[11:33] одну две три поездки то есть поездок
[11:34] принципе столько же ежедневно будет
[11:36] происходить но и вводить водителей до
[11:40] или актив ты достоин с у нас это будет и
[11:43] знаю но водителю почти все время
[11:46] работают на этом 50к да и для этих
[11:49] driver's
[11:51] будем считать это так это совершается
[11:54] если один миллион в день как у нас там
[11:57] сто тысяч секунд значит каждую
[11:58] конкретную секунду а у нас еще поездка
[12:01] длится сколько то в среднем там допустим
[12:04] 1 час москве когда все стоит то есть у
[12:08] нас есть 24 часа у нас один миллион
[12:10] поездок распадаются на 25 это получается
[12:14] 40000 одновременных поездок у нас
[12:23] поездок одновременно и поисков поездок
[12:27] тогда если на 100000 секунд миллион
[12:29] поездок еще мы секунд там 10 в среднем у
[12:32] нас получается сейчас
[12:36] секунду
[12:39] действенно времен на 10 секунд они
[12:41] занимают то есть то
[12:44] грубы 1 100 г рыбы
[12:48] инициируется стон 100 новых 100 каких на
[12:51] поиск водителю до что не значит поездка
[13:05] естественно происходит столько из них
[13:07] потом одновременно работают
[13:09] течение там правильно так и ставлю 10
[13:13] каире персик and is the connection of не
[13:16] что то есть мы как бы 10 секунд еще
[13:21] здесь кайри персиком потому что у нас
[13:24] один миллион доу и 100000 секунд это у
[13:28] нас миллион поездок
[13:32] но мы можем накинуть там условно его
[13:34] задал он и кажется какой то есть имеет
[13:37] припяти 100 миллионах всеобщего
[13:40] нет это я в рамках
[13:43] как даже самого крупного города тоже
[13:46] перу в целом
[13:53] мы можем перейти на потом на суммарную
[13:55] просто дам новый принцип целом там в 550
[13:59] раз поможет умножить будет получим
[14:02] суммарную так наверно это по требованием
[14:05] по
[14:06] то есть это по трафику смысле
[14:11] трафика именно количество пользователей
[14:13] соединение прочего
[14:15] вот мы потом наверно оценим
[14:18] сколько нам еще хранитель уже информации
[14:20] про пользователей про водителей потом
[14:22] складывать поездки куда-нибудь базу
[14:24] данных я думаю частную перейдем к
[14:26] какому-то вск уровнем и понимание как
[14:28] сервисом же работает будет а схемам
[14:30] потом еще дополнительные оценки уже по
[14:32] исходя из того что мы вообще будем
[14:34] хранить и записывать
[14:37] значит у нас есть 2 категория
[14:40] пользователей у нас есть пешеход
[14:44] есть водитель
[14:46] сказать на они каждую смотрят своя какой
[14:49] такой клиентов рейтинг приложения
[14:50] описанных он даже это разное
[14:56] то есть это драйвер сервис
[15:01] я пока без там логин серов и прочего
[15:05] дерево нет рядом ниц и и
[15:08] для сцены и
[15:13] как я уже сказал у нас получается у
[15:16] системы будет разбиваться на две части
[15:17] то есть
[15:18] как пешеход мы инициируем поездку мы
[15:22] хотим естественно это просто будет
[15:23] происходить водитель он и инициирует
[15:26] поиск ему находится то есть мы решаем
[15:28] какие страны задачу матч инга мы
[15:30] смачиваем водителя и пешехода и затем
[15:34] нам нужен какой-то сервис который будет
[15:35] поддерживать эту поездку во время того
[15:37] как она происходит водитель и пешеход
[15:38] как-то обмениваются их приложения
[15:41] информацией у нас есть какое-то там про
[15:44] промежуточный сервис который будет
[15:46] обмениваться с ними этой данные
[15:48] плюс у нас есть про пешеходы и про
[15:51] водителя у нас есть там базу данных
[15:53] собственно с этим профилем и всем прочим
[15:55] то есть где то там
[16:02] они в целом могут быть вообще разные не
[16:04] пересекаться может быть одна база данных
[16:06] вот затем то есть мы инициируем сервис
[16:10] есть какой-то connection сервис
[16:15] в которой собственницы рует между ними
[16:18] общение
[16:19] затем эта поездка происходит после как
[16:22] поездка заканчивается она складывается
[16:24] куда-то же как произошедшая поездкой
[16:26] плюс мы должны хандрить этом оплаты вот
[16:28] эти все истории
[16:29] то есть connection сервис он скорее
[16:32] всего когда ты поймешь что поездка
[16:34] завершилась не может ли до конца доехали
[16:36] бы раньше закрыли после этого он должен
[16:40] в какой-нибудь там роиться
[16:44] сервер собственно тот который будет
[16:46] ходить что вот там поездка завершилась и
[16:48] как ты ее нужно спорить
[16:50] для удобного масштабирования до капли
[16:53] нга разных вещей нашей системе я бы ввёл
[16:56] сразу system design какую-то вещь типа
[16:59] шины ивентах например ту же кафку чтобы
[17:02] можно было такие события складывать 12
[17:04] разные по части системы потом
[17:06] реагировали на то или иное действует она
[17:07] началась поездка значит он конечно
[17:10] сервис давай что-то выделяет ресурсы еще
[17:12] закончилась поездка значит нам нужно
[17:14] снять деньги из пользователя там
[17:16] накинуть танки тачки водителю
[17:19] вывести водители опять встроенное или
[17:22] снять отказался то есть наверное тот
[17:26] райт сервис он скидывает информацию
[17:30] какую-то кафку либо да можно настройках
[17:33] сообщений ну да мы с альбац брокер
[17:36] connection сервер сказать эту шину на
[17:38] этой шине у нас сидит сервис который
[17:40] видит что нам поездка заканчивалась или
[17:42] началась
[17:44] так естественно
[17:46] сейчас подумаю какие еще крупные такие
[17:49] на кино пили уже потом
[17:51] помимо баз данных для пользователя баз
[17:55] данных для водителя у нас должен быть
[17:57] еще собственно чем uber будет опять же
[17:59] отличаться
[18:00] от других систем у нас должен быть
[18:02] специальный белый локейшн сервис который
[18:04] собственно пай-мальчик такое
[18:05] пользователь рядом что такое они не
[18:07] рядом
[18:08] для
[18:11] нас должен быть какой-то отдельный
[18:15] dial-up
[18:17] гиа backend конечно зову
[18:20] с которым нам нужно общаться то есть для
[18:24] пользователя connection сервис должен
[18:26] через гигабайт понять какие водителя
[18:29] можно считать то то что они рядом для
[18:31] водителя нужно понять как бы чтобы он
[18:33] записался что он здесь и где пользование
[18:35] да и чтоб ему потом показали где где где
[18:38] пользователь то есть какие-то из
[18:39] принципе это принимать это интересно
[18:41] значит
[18:44] пока наверное какие-то крупные куски
[18:46] потом накину наверно про вот эту из
[18:49] интересная часть двое про него подробнее
[18:51] это как решать задачу найти кого-то кто
[18:55] у нас есть рядом есть разные структуры
[18:58] данных для этого в целом они похожи
[19:00] наверное такая более академично я
[19:02] простая для понимания записи есть такая
[19:04] штука называется quadtree
[19:06] какие еще есть гексагональная отвожу
[19:10] брать библиотека h3 с которой собственно
[19:13] позволяет на гексагональной карте там
[19:16] все разбиение поиски делать просто точки
[19:18] зрения
[19:20] простого простого разработчика квартире
[19:22] понятен тем что у тебя из иксы и игреки
[19:23] просто координаты для эти каждый
[19:26] квадратик можешь победить о ну давайте
[19:28] чуть подробнее
[19:29] расскажем отсутствие у нас есть грубо
[19:32] говоря карта мира понятно что она там
[19:35] для когда мы находимся яндекс такси
[19:37] москва у нас есть кусок то московской
[19:39] области и она разбита на какие-то
[19:42] квадрат крупные и
[19:45] нам нужно понимать что у нас убита по
[19:47] этой карте как катаются какие-то
[19:49] водителя при этом где-то водитель может
[19:51] быть больше где-то водитель может быть
[19:53] меньше то есть нас есть удается москва
[19:54] но здесь будет какой-то там лосиный
[19:56] остров огромные для водителей скорее
[19:58] всего нет
[19:59] если же у нас мы находимся где-то в
[20:01] центре томпсон сильные пробки нам нужно
[20:04] шины который прям очень рядом то есть
[20:07] там рядом она как бы меняется в
[20:09] зависимости от контекста где-то в центре
[20:11] от плотности то есть если мы где-то в
[20:14] центре рядом скорейшего желательно там
[20:16] несколько кварталов если мы там не знаю
[20:18] хотим уехать
[20:20] из красногорска то значит там можно
[20:22] взять машину 10 метров по мкаду на
[20:24] приедет к нам приедет нас заберет
[20:26] поэтому нам желательно для поиска мы
[20:30] можем чем мельче мы разбиваем тем более
[20:33] точно мы выбираем вот это вот понимание
[20:35] рядом при этом если мы разобьем просто
[20:37] всю карту слишком мелко нам пранк
[20:39] слишком много
[20:41] данные чтобы хранить вот эти вот все все
[20:44] все мелкие квадратики индексы да поэтому
[20:46] нам желательно адаптировать например что
[20:49] в каждом квадратики там было сколько-то
[20:50] ним небольшим сколько-то водителей вот и
[20:53] в зависимости от необходимости можем
[20:55] побить чуть сильнее 100 где наоборот или
[20:58] или или какие-то укрупнить если там
[21:00] танец мероприятие или пробка там прошла
[21:02] и уже не так важно поэтому мы можем
[21:05] адаптировать эту структуру то есть у нас
[21:07] есть какое-то и не шил разбиением для
[21:09] наших квадратиков затем если мы видим
[21:11] что у нас какие-то квадрат и выдают
[21:13] большей плотностью то мы можем разбить
[21:14] их на еще на 4 часть идет вопрос не то
[21:17] есть я пай пользователь нахожусь где в
[21:20] каком-то квадранте как сервис знает
[21:22] каком квадранте у
[21:23] нас есть приложение яндекс и которая
[21:26] использует gps поэтому у нас есть как бы
[21:28] в эти планки как выглядит запрос к базе
[21:32] данных
[21:34] с точки зрения пользователя то есть мы
[21:37] сообщаем связать идет вон тут ходим как
[21:39] бы в в этот гигант начинаем один нам
[21:42] свой сервис какой-то клайн fighting он
[21:44] зачем идет в г в бэг-энд что понять где
[21:46] мы находимся или затем найти машину и
[21:48] эти машины будут какой-то больше крупной
[21:51] структуре находиться вот в эти как 1 к 3
[21:53] то есть мы сообщаем lucky john кличут он
[21:56] нам нас маппет в какой-то большой
[21:58] квадрат затем мы сообщаем у нас еще пол
[22:02] во время поиску то потеряется радиус так
[22:04] же как в приложение напрямую даже как
[22:06] карта отделяется чтобы это
[22:07] проиллюстрировать то есть мы сначала
[22:09] ищем у нас есть какой-то там радиус там
[22:12] дельта окрестность
[22:14] мы находим те куб куб квадро деревья
[22:18] точнее кадра клеточки которые мы задели
[22:20] затем нас может быть попасть какие-то
[22:23] крупные куски какие-то мелкие если мы
[22:26] хотим радиус уточнить то есть мы видим
[22:27] что мы вот этот вот задели вроде бы
[22:30] давайте начнем подробнее мы вобьем еще
[22:32] на четыре части смотрим затем в какую из
[22:35] более мелких частей мы попали и тем
[22:37] самым мы как бы находимся все квадратики
[22:40] там как которые заполняют наш радиус
[22:44] поиска и при этом это наша система так
[22:47] как у нас есть довер сервис который
[22:49] сообщает что в каком месте у нас есть
[22:50] активные водители мы понимаем и начинаем
[22:53] прошивать то есть у нас и так есть
[22:55] connection сервис
[22:57] который работает из водитель из
[23:01] пешеходам и с водителями и он начинает
[23:03] водителям присылать им сетей что-то в
[23:05] зависимости от их приоритета их рейтинга
[23:08] и прочие плюс там накидывать
[23:11] стоимость если водитель и перестают
[23:14] отвечать
[23:15] самым накидывается общая там базовая
[23:17] стоимость для всех поездок средстве на
[23:19] какой-то водитель он тыкать что данная
[23:21] часть хорошо поездку и после этого
[23:23] устанавливается
[23:24] connection сервисом сообщает
[23:26] пользователю что до водитель согласился
[23:29] и поиск начинается дальше у нас может
[23:32] быть общение напрямую пир toupper между
[23:34] приложением пользователей водитель
[23:35] например я хочу изменить адресе это
[23:37] вбиваю водитель то там сразу приходит
[23:39] они там через какие-то промежуточные
[23:40] сервиса то есть это в этом нет
[23:43] необходимости то есть мы как бы между
[23:44] собой разруливает текущую поездку когда
[23:46] оно закончится уже это там сообщается в
[23:48] эту ширину поездок и там хоть раз сервис
[23:52] поездок уже определит что там
[23:53] происходило поэтому скорее всего здесь
[23:56] есть то есть помог an action service
[23:58] есть какой-нибудь
[23:59] отдельный под сервис там для winter в
[24:03] абсолют sockets хендлер то есть это
[24:04] штука которая позволяет нам как раз
[24:06] между приложением между над приложениями
[24:08] через посредника сохранять постоянно
[24:11] какую-то связь между собой чтобы мы
[24:13] видели что там
[24:15] добавил адрес пользователь водитель
[24:17] сразу это приходил он сразу маршрут
[24:19] изменила не ждал пока там
[24:21] пока весь сервис обработать довольно
[24:24] долго этот запросам может уже поворот
[24:26] пропустили нужный
[24:28] вот соответственно такая структура нам
[24:31] позволяет адаптироваться к частоте после
[24:33] понятно что если мы дошли до клетки в
[24:35] которой по всего три водителя моим всем
[24:37] трем уже скинни мыслим там очень много
[24:39] водителей и мы и там вот в этом квадрате
[24:42] много мы задеваем этот квадратик ему
[24:44] меньше водителей tank top 500 мы сдается
[24:48] начинаем делить этот квадратик попадаем
[24:50] в более мелкие и вы забираем уже только
[24:53] нужных водитель чтоб не опрашивает он
[24:54] все тысяч в радиусе 10 километров
[24:56] вот поэтому если когда там ситуации
[24:59] разгрузится к ночью дело близится
[25:01] водители становятся меньше мы начинаем
[25:03] укрупнять эти квадраты обратно в нашей
[25:05] структуре и постоянно пересчитываю над
[25:09] стана в таком постоянном и мы их держим
[25:11] сколько на память
[25:13] давайте посчитаем
[25:16] что ни будь то есть треть функциональные
[25:19] не функциями требования принципе помнить
[25:22] так на давайте возьмем например какой
[25:24] нибудь
[25:25] квадро дерево для москвы сколько бы она
[25:27] могла занимать у
[25:29] нас есть москва можем запасом взять
[25:33] например что у нас по ширине по высоте
[25:35] там будет сколько ни 40 километров
[25:39] этот квадрат
[25:42] 40 на 40 километров мы его разбиваем
[25:47] страстно для разбиения у нас получается
[25:50] чтобы уйти на один уровень глубже нам
[25:53] нужно 2 бита то есть и потом нолики
[25:55] книжка 0 книжка по высоте и ширине и
[26:01] затем то есть каждый раз когда мы
[26:03] укрупняются за каждый шаг мы добавляем
[26:06] плюс четыре бита чтобы сохранить именно
[26:08] нашу конкретную позицию либо можно
[26:11] чуть-чуть изменить то есть
[26:12] нельзя взять запасом чтобы еще отдельно
[26:16] описать ситуацию не нырять дальше на
[26:18] каждом уровне у нас становится в четыре
[26:20] раза больше
[26:22] мест где бить на 4 бита или нет
[26:25] вот и нарисовал сейчас у тебя ты
[26:27] потратил два бита здесь два бита здесь
[26:30] здесь уже получилось четыре квадранта и
[26:32] в каждом из них снова нужно по четыре
[26:34] бита правильно я сейчас
[26:36] даже , я массирую в этой ситуации что я
[26:40] иду в этот квадрат затем внутри этого
[26:42] квадрата я добавляю еще два бита чтобы
[26:44] сказать что я иду в эту награду еще два
[26:47] бита то есть за каждое разбиение я
[26:49] добавляю 2 бита либо я могу добавить там
[26:51] три чтобы ну на всякий случай и плюс
[26:55] им иметь возможность говорить что я не
[26:58] иду дальше что я уже достаточно
[27:00] владельцы ты два бита вот здесь разбил
[27:02] потом ты здесь два бита но и здесь
[27:04] добиты и здесь два бита и действий нет я
[27:06] сейчас описываю сколько занимает
[27:08] конкретный адрес а мая прошла то есть
[27:10] вот в этой системе теллера естественно
[27:13] каждый раз когда мы получаем на выбит мы
[27:14] уточняем в два раза то есть у нас было
[27:17] 40 километров до 140 тысяч метров каждый
[27:21] раз мы уменьшаем это в 2 раза точность
[27:23] получается сколько нам
[27:26] 250 это будет 1024
[27:29] наверное чуть по точнее хочется еще
[27:32] нормально ну или 40 путей 40 метров
[27:35] соответственно это
[27:38] делим на 2 в 10 получается 40 метров
[27:40] точностью на самом для именно поиск
[27:42] нормальными на позиционирование где стою
[27:45] это не очень
[27:48] вот два в 10 но если запасом взять там
[27:52] добавлять какой-нибудь дополнительный
[27:54] бит что точнее не надо
[27:56] либо можно запасным поддаваться ответить
[28:00] что что
[28:02] нет я просто хочу понимать как не
[28:05] кодировать что я просто остаюсь на эту
[28:07] муру женю 2 десятых 220 это огромная
[28:09] разница
[28:11] в тысяч раз
[28:15] love 12 мало и за пределы москвы выехал
[28:19] все-таки получаешь и 212 и позволить
[28:22] увеличить 40 километров до 160 ну да
[28:26] получается у нас
[28:27] эти 2 в двенадцатой то есть мы храним
[28:31] как бы руки и даже запасом два байта
[28:33] gepai то ли беда
[28:37] но 2 в двенадцатой это искал здесь
[28:40] начало 2 2 бита или не два байта это 2
[28:43] 12 у него точно поместится плюс еще
[28:45] какая-нибудь там инфа по я потому что
[28:47] игры все нужно 2 бита чтобы разбудить а
[28:49] сейчас ты горишь два байта до обито
[28:52] чтобы каждый шаг сделан когда то есть
[28:54] нам всего на 12 шагов и все вся весь наш
[28:58] маршрут занимает дома все весьма сильно
[29:01] полная наша позиция совета на эту
[29:03] позицию должны сохранять для всех
[29:06] водителей всех пешеходов чтобы не
[29:08] стесняться у нас получается даже если
[29:13] взять вот эту всю нашу церковную систему
[29:14] нас получает 5 мегабайт
[29:19] 10 мегабайт нас занимают водители и
[29:25] один гигабайт занимает позиция для
[29:28] пешеходов
[29:34] а как поиск фазе структуре происходит
[29:36] какая у него сложность
[29:39] получается каждого latitude ломтики
[29:42] правильно
[29:43] дамы получается то есть у нас есть
[29:45] дерево у
[29:47] нас фактический поиск пойдет как раз по
[29:50] деле у нас есть каждый раз четыре
[29:51] варианта куда пойти дальше мы понимаем
[29:55] что так у нас радиус такой то это
[29:57] примерно как задачи похоже получается
[29:59] просто на 2-мерное но в целом она похожа
[30:01] на одномерную задачу
[30:02] как как найти все числа в бинарном
[30:06] дереве поиска из нужного диапазона вот
[30:08] получается мы каждый раз отрезаем что
[30:10] если у нас какая-то ветка идет в большее
[30:14] число чем у нас наибольшее или наоброт
[30:18] из нас минимум больше чем наш максимум
[30:20] поиска или максимум дереве больше
[30:21] минимум то есть мы как бы обрезаем такой
[30:24] весь вес у нас получается что где-то мы
[30:26] идем глубже где где-то мы идем меньше но
[30:29] по факту 12 операций предельно но да то
[30:32] есть но сложность это гонителями танк на
[30:34] и время но в целом да тазик сложной
[30:36] все-таки от глубину а дерево в целом
[30:38] получается
[30:39] что поиск и быстро но эту штуку нужно
[30:42] постоянно на бы на обновлять то есть мы
[30:44] каждый раз там водителя говорите онлайн
[30:46] идём-идём-идём добавляем понимаем что у
[30:48] нас в этом листе уже на хочешь к много
[30:51] водитель начинаем его добить пополам
[30:52] либо наоборот водитель говорит я все на
[30:55] катался на сегодня видим что в листе
[30:57] осталось мало значит укрепляем она
[31:00] наоборот но ты такое дерево на
[31:02] динамически менять глубину получается ну
[31:04] в зависимости от того как поиски
[31:05] начинается заканчивается
[31:08] так
[31:11] хочется наверное побольше теперь вот
[31:13] сюда сюда чистили кидать вас на
[31:14] хэширование как-то можем здесь или не
[31:16] имеется
[31:19] я почему спрашиваю 12 операций это
[31:24] принципе не так чтобы много в этой 12
[31:27] раз больше чем одна операция мы можем
[31:29] сделать это наверно оптимизацию как в
[31:31] случае задача по
[31:34] по деревьям 5 же английского манчестер
[31:35] то есть понять в какой у нас общие
[31:38] региону двух вершин ты снова про также
[31:40] можем за 10 запросов секунду правда то
[31:43] есть если я знаю что у меня уже был
[31:45] запрос в это в этот лист в в течение
[31:49] каких-то последних пяти секунд может
[31:52] быть не выдать то же самое выродка у
[31:54] меня все покинули все водители а то про
[31:57] это немножко про другое процесс начал
[31:59] говорить ни одной а мой вопрос простой
[32:02] 12 операций можно провести но лоб лоб
[32:06] скажем 12 мы посчитали нас но ведь одна
[32:09] операция это в 12 раз быстрее чем 12
[32:14] можно ли как-то сделать здесь одну
[32:16] операцию я щас просто другую штуку
[32:19] говорил то есть как понять что водитель
[32:21] и пешеход попадают не делают этот полный
[32:24] полный поиск то есть мы можем выбрать из
[32:27] всех водителей только и тех у которых то
[32:29] есть когда мы кодируем вот этим вот
[32:30] двумя байтами позицию только тех у
[32:33] которых префиксов падает между собой так
[32:35] решается задача лист команд сестер в
[32:37] дереве если мы бинар на закодируем все
[32:39] наши пути лево право и так далее то у
[32:41] нас сделали ну да то у нас у двух вершин
[32:44] общая вершина будет иметь код к общей
[32:47] префикс плюсы 0 и
[32:49] вот здесь надо как-то похоже может быть
[32:51] история мы понимаем для
[32:54] нас есть пешеход у нас с радиус поездки
[32:57] поэтому нам нужно просто все водители с
[32:58] нужным префиксом зависимости от радиус
[33:00] радиус увеличивается префикс
[33:01] укорачивается водитель становится
[33:03] отвечать больше на это все это как
[33:05] [музыка]
[33:07] начальный шаг для поиска
[33:09] вот но за кэшировать результаты и еще
[33:13] один вопрос вот у нас здесь получается
[33:15] структура где ключом является позиция
[33:19] правильно ну и соответственно какие
[33:22] сколько водители условно говоря в этом
[33:25] квадранте
[33:26] с по каждому пользователю надцать
[33:29] позиции по водителю и для пользователя
[33:30] задача найти тех кто это символизм остро
[33:33] он проваливается в этот ли то можем ли
[33:34] мы быстро вытащить какой позиции
[33:37] находится водитель в каком
[33:39] квадранте ii нужно ли нам от
[33:43] ну когда он перемещается то есть у него
[33:45] квадрант с время сохраняется в целом
[33:47] если он едет перманентным периодически
[33:50] за ним человека им понять что он не
[33:51] может случайно перевалить про
[33:53] провалиться в какой-то случайный лист то
[33:56] есть он скорее всего из одного квадрата
[33:57] попадет в следующий с поэтому когда мы
[34:00] едем мы с например каширу им для каждого
[34:04] водителя на прям клиентской стороне в
[34:06] его приложение пределы квадрат в котором
[34:08] он сейчас находится когда мы начинаем
[34:10] приближаться к квадрат и мы решаем
[34:11] задачу в каком квадрате да тогда он
[34:13] сейчас следующем окажется вот и мы можем
[34:16] принципе легко это понять то есть у нас
[34:18] либо квадрат соседней в той же разбивки
[34:21] либо квадрат будет соседней там из
[34:23] какого-то уровня разбивки то есть мы
[34:24] поднимемся на сколько это и опустимся на
[34:27] другой то и соседних квадратов то есть
[34:29] чтобы не идти по всему дереву не 12
[34:31] операции скорее все это будет там 1 2 см
[34:33] и сокрытием как бы не не лагай она
[34:35] просто будет фактически константа скорее
[34:37] вся в среднем по больнице
[34:39] да самым можем main тренить как бы
[34:41] позиции наших водителей
[34:43] паку от дерева ну это пока все давайте
[34:46] вернемся к в общем нашего сервиса что
[34:50] еще какие нам частью нужны
[34:52] ты сказал что 20 мегабайт это занимает
[34:55] но это занимает именно индекса а
[34:57] ведь мы еще в листе хотим записать
[35:00] перемыто get в отдельным будем писать
[35:02] кто кто в этом и сейчас находится
[35:05] то есть для каждого листа хранить сет
[35:08] яичника в тех кто там сейчас в нем сидит
[35:10] как
[35:13] если я запросил вот я пользователь я
[35:16] упал в лист между нужной кто там
[35:18] находится еще
[35:21] правильно нужно из водителей а как я
[35:24] этого на если мы нигде не записали
[35:26] правильно сейчас я пока просто про ну да
[35:29] окей
[35:31] напишу
[35:35] то есть нам надо знать
[36:00] [музыка]
[36:02] так страстно сервис будет поддерживать
[36:04] вот это как раз
[36:06] вот так я нарисую
[36:09] как раз это квадро наше дерево с базы
[36:12] данных чем она будет частично ссылаться
[36:15] на
[36:15] вот вот этот вот и на вот это вот чтобы
[36:20] водители каких-то пыли идиш ники
[36:23] но будем считать что у нас там у
[36:26] пользователя и у водителя есть какой
[36:28] нибудь типа int64
[36:29] хищник не стану для драйвера
[36:33] для страны и
[36:38] в нашем собственно этом дерево то есть
[36:41] помимо того как мы делаем запрос именно
[36:43] к вере когда пользователь приходит и
[36:45] попадаете в клеточку в этой клеточки нам
[36:47] нужно собственно записывать
[36:49] сохранить сет из тех водителей которые
[36:53] там находятся
[36:54] вот если у нас
[36:58] причем это динамическое то есть словно
[37:00] все водители они будут как раз размещены
[37:02] по всей этой таблички и для то есть
[37:05] суммарное количество элементов всех
[37:07] цветов во всем куда берию это будет
[37:09] просто количество водителей которые
[37:11] существуют на лекторы онлайн хотя бы на
[37:13] получать сценическая 4 то есть вот у нас
[37:16] восемь байт на
[37:24] сколько у нас тут сто сто тысяч пять
[37:28] минут всего было здесь
[37:32] 5 миллионов
[37:34] получается 40 40 мегабайт будет хранить
[37:38] информацию для куда дерево то вам
[37:41] наверное сел бы в памяти между и даже
[37:44] пользователи пусть они добавят причем
[37:46] опять же мы это глобально для всех
[37:47] посчитали а мы говорю что ходим локаль
[37:49] именно дату сможем использовать армию
[37:51] помада дителей вся вся эта штука это
[37:54] просто россии написанными история но по
[37:57] факту внутри которая позволяет посчитать
[37:59] в квадранте ii всегда квадрант радовать
[38:01] а потом еще какая-то ассоциация где
[38:03] структура данных уже какой гридо той
[38:05] стану листе у нас хранится постоянно
[38:07] водители плюс водитель говорит
[38:08] заканчивать мы удаляем из сета или когда
[38:11] он за границу пересекает нужно из одного
[38:13] предложения друг и только что мы сейчас
[38:15] обсудили как раз все отлично вот так да
[38:18] то есть нас 50 сервис драйве сервисе так
[38:21] ван хельсинг и это приложение у нас есть
[38:23] как бы какая-то db для собственной
[38:26] информации по переходу по информации
[38:29] есть база данных табличка персонал
[38:31] тыкать информация по водителю для этого
[38:34] скорее всего можем что-то использовать
[38:36] кнопкой бы простоя типа майский этом
[38:38] какой-то обычные дмс
[38:40] продолжение которое нам бесплатно дает
[38:43] как бы и сид теорема выполнение значение
[38:46] интерес и 10 свои сложные ряда
[38:48] выполняется вот в целом как бы это нам
[38:51] хорошо то есть мы это мы заменяем
[38:53] профиль ничего не теряем как бы все все
[38:55] условия на плюс но поездок будет много
[38:59] происходить их как бы нужно тоже куда-то
[39:01] складывать что потом производить
[39:02] аналитику но в целом хранить информацию
[39:04] по поездка из пока поездка происходит мы
[39:07] общаемся с к нашим сервисом и записываем
[39:10] у нас должна быть отдельно наверное
[39:12] более доступной база данных текущих
[39:13] поездок что подписывать там какой-то
[39:15] маршрут запоминать что сейчас происходит
[39:16] если вдруг поиск прервется потому что то
[39:18] страшное случится на узнаем какой
[39:20] водители с каким пешеходам куда ехал что
[39:22] с ним происходило с нас искать табличка
[39:24] с текущим поездка есть табличка
[39:26] отдельная на отдельно базу с история
[39:29] поездок которые мы используем для после
[39:31] последующие аналитики для текущей
[39:33] таблички наверное можно поддерживать
[39:35] какой-нибудь оля радист с какой-то мере
[39:38] сторож который бы позволял быстро
[39:40] общаться быстро обновлять данные
[39:41] принципы всю историю может сохранить
[39:43] какой-нибудь список из патентов стоим
[39:47] стоим память чем-то таким но в принципе
[39:48] вроде с лист или легко можно складывать
[39:50] по у нас когда генерируется поездка
[39:53] создается новый ключ для поездки у неё
[39:56] свойство какой водитель какой пешеход и
[39:59] какой у них маршрут своим с темпами
[40:01] что-то информация в принципе немного
[40:03] потому чуть подробнее описать вот
[40:06] настраивать сервис который общается с
[40:08] нашим высоким менеджером который
[40:10] общается с водителями драйверами он
[40:12] записываю в какой-то и номер старик
[40:14] radisson ну да условный родис
[40:18] снята какие-то текущие поездки
[40:22] плюс по 100 как поездка завершается у
[40:25] нас отравить сервис положит в историю но
[40:28] будем считать что это либо там кассандра
[40:29] любишь bass то есть там просто много
[40:31] очень данных либо клик house тоже можно
[40:34] записывать у него до дало ночную важную
[40:36] до коллаж на базу данных в целом как бы
[40:38] считается что там либо ибо если бы
[40:40] кассандра зависит этого если вас hadoop
[40:42] на самом деле в той же сегодня уже
[40:44] упоминал спасаться теореме и кассандре
[40:46] лишь бы и супом по разным веткам одна из
[40:49] них выбирает consist in сиди там и там
[40:51] другая наоборот там даже закаленных
[40:53] дефолтные настройки про сразу но да ну
[40:55] либо можно их просто адаптировать но в
[40:57] целом дату словно условные кассандрой
[40:59] она станет ходу по
[41:02] которой эти все чаще и чаще случается да
[41:06] хоть я слышал я в одной конторе
[41:08] переходит на ходу
[41:10] в одной конторе из миф о том что
[41:13] когда-то все таки перейдут так
[41:16] history затем когда мы и вот в эту
[41:20] history опять же . да мы записываем то
[41:22] что мы кладем она еще у нас на самолет
[41:24] вот так вот выглядит у нас все вся шина
[41:28] через который мы общения правка сервис
[41:30] пишет что вот поиска завершилась либо
[41:32] поездка началась и мы ее как-то хэндом
[41:34] через наш текущая данный либо поиска
[41:37] завершилась положили сюда плюс когда
[41:39] поиска завершилась надо деньги чтобы
[41:41] забрать конева пользователей
[41:43] цель для этого кстати мы опять
[41:45] вспоминаем что она же rdbms и поэтому у
[41:47] нас как бы есть выполняется оказали
[41:49] когда есть денежки как бы это сразу
[41:52] начатое сид и нам надо нам нужно
[41:55] было решено как базу данных которые это
[41:57] все нам дает если нам нужно просто там
[42:00] поскольку это историю даже если что-то
[42:01] может быть потеряется здесь не хотелось
[42:04] бы конечно следственно томкинс крики и
[42:06] просмотр еще может что-то можно потерять
[42:08] ну давай просто вам просто куда-то
[42:10] сложить какую-то не очень
[42:11] структурированно данные для этого
[42:13] набираем кого ночную таблицу весна нужно
[42:15] что-то важное там какие то монетки и
[42:17] деньги рачки и так далее как-то между
[42:20] собой хиндли там выбирая вилла и шиндо
[42:23] этот компонент какой-то лишь на базу
[42:25] данных обычно прикрас вот поэтому так же
[42:29] плюс если у нас есть кассандра также
[42:33] может быть у нас есть какие-нибудь
[42:35] доказательства которых мы нанимали и у
[42:38] них скорее все-таки есть какой-то
[42:39] божественный hadoop
[42:42] для того чтобы радикулит аналитику там
[42:44] устанавливается розы родственники выдать
[42:46] его цены безумные придумывать как бы
[42:48] формула для их подсчитывая на основе
[42:50] истории поездок и прочего поэтому мы
[42:53] можем из кафки сразу писать еще куда то
[42:55] здесь может какой-то части ходу по будем
[42:59] считать частью ходу пока он еще может
[43:01] быть парк streaming например в который в
[43:03] режиме онлайн чат какой-то анализ
[43:04] проводят что вот на деньги цены поднять
[43:06] что здесь слишком много поездок стала но
[43:09] и в целом месяц как бы ходу кластер то
[43:11] есть х tf слот записывается та же
[43:13] история поездок с кассандрой как бы с
[43:15] более прямым доступом без вот этой всей
[43:17] игры hadoop вычислениями и так далее по
[43:22] ходу контекстами
[43:23] подключение прикрас контекста и прочее у
[43:26] тебя часов нет а я то знаю что одна
[43:28] минута осталась
[43:33] что мы сделали плохо on давай тогда есть
[43:36] одна минута в целом про redundancy
[43:38] доступность вот это все прочее во-первых
[43:40] между нашим сервисами клайн facing up у
[43:43] нас всегда есть контент был интер
[43:46] который во первых у нас то что скала из
[43:49] глобальный лот бензин приносит в москве
[43:50] нам нужно в московской через сервис эти
[43:52] с мужа и про парте церовани из любого
[43:54] или самом начале то есть целом нас конь
[43:56] может быть 2 уровне лот beyonce то есть
[43:58] именно сначала ротик куда в нужную этом
[44:00] подсветку в какой местный географически
[44:02] затем уже лот балансы которые стреляют
[44:03] нагрузку можем выбирать зависимости там
[44:06] от того где больше соединений как как
[44:10] который там быстрее отвечает где там
[44:12] были какие-то файлы нет и так далее
[44:13] целом между любыми двумя сервисами для
[44:16] максимального как
[44:18] разделение их чтобы каждый из них можно
[44:20] выбирать независимо мы отдельно
[44:21] выставляем лот bouncer и не каждый из
[44:24] них независимо масштабируем в
[44:26] зависимости от того какую нам нагрузку
[44:27] нужно держать для relation баз данных
[44:30] нам нужно иметь как минимум не только
[44:32] как main копию но и
[44:35] оффлайн как бы реплики которые можно
[44:37] было поднять вместо них если что плюс
[44:39] для увеличения readonly нагрузки нам
[44:41] нужно добавить больше копий именно
[44:43] readonly копий плюс можем
[44:46] воспользоваться правилом
[44:47] 2086 20 процентов нагрузки как бы вас
[44:50] данных гинер у этого средства нагрузки
[44:52] мы можем исходя из этого поставить перед
[44:55] ним еще тоже это редис каши для
[44:58] ну кассандра соответственно мы выбираем
[45:00] количество там тоже реплики и
[45:03] сортирования просто до плюс для
[45:06] собственного bouncer еще может
[45:08] использовать
[45:10] определить кому нам нужно пойти чтоб мы
[45:12] все время ходили в одно и то же место и
[45:14] какую-то поддерживали вот эти вот
[45:15] соединение прочим можем использовать как
[45:18] бы fishing при этом применять кости
[45:19] стенах чтобы приходили все время в одно
[45:22] и то же место из этого и балансире
[45:23] хранит соответственно диапазон дат если
[45:26] там часть отваливается мы используем на
[45:28] качественно чтобы сейчас сервисов
[45:29] отвалилась не стучался к группе перекос
[45:32] нагрузки в какой-то один из наших
[45:34] сервисах
[45:35] так ну стандарт для базы нам нужно
[45:38] резонансе больше копий для доступности и
[45:41] быстрой скорости чтения лот был инсульт
[45:44] перед каждым сервисом каждый сервис
[45:45] независимо масштабируется кафка
[45:47] соответственно тоже там worker и
[45:49] масштабируется в зависимости от нагрузки
[45:51] и quot три последние осталось
[45:54] его как мори догнать просто добавляем
[45:57] кучу копии храним то есть у нас есть
[45:59] мини сервису которым собственно только
[46:01] одна штука может вертеться танцоров
[46:03] куберы делаем много кодов есть один из
[46:06] них отвалился тут же переключились на
[46:07] другой как можно посчитали информацию
[46:10] находиться немного то есть это просто
[46:12] дамп нам делать принципе не надо ну то
[46:14] есть какой то просто сервис на головы у
[46:16] нас всегда есть какое-то количество пота
[46:18] в которых которые его поддерживают офиса
[46:21] жизнь спасибо большое мне очень
[46:23] понравилось спасибо собственно ну я бы
[46:26] поставил х или стран ха я пожал 1 когда
[46:30] вы поставил эту оценку на этих интервью
[46:32] два момента про которые нужно один
[46:35] момент это мы забыли но потом вспомнили
[46:38] с подсказкой что в код 3 нужно еще
[46:40] учитывать и айдишники но этот индастриал
[46:43] обсудили именно как найти враги шарманку
[46:46] же побежали не учли это потому что у нас
[46:49] от этого могло сильно поменяться благо
[46:50] айдишники немного места занимали но если
[46:53] бы они занимались словно не 40 мегабайт
[46:54] и 400 гигабайт уже было бы возможно
[46:57] другое решение и
[46:58] паст момент который часто забывают о
[47:01] нужно сайт и он очень простой мониторинг
[47:04] мониторинг сервиса то есть бордель
[47:06] grafana либо равен графа ну следим за
[47:09] такими то метриками gps перцентиле все
[47:12] такая полировка так все отлично какие
[47:15] базы данных asset как redundancy делать
[47:20] а вот три
[47:23] сожалению тайминг в голове не держалась
[47:26] на это тяжело том что обычно когда ты
[47:28] проводишь свои часы с модели с что-либо
[47:30] в углу в три ноты откровенно говоря
[47:33] около укладывался то есть ты про все
[47:34] рассказал покрыла 3-дан дэнси написал
[47:37] функциональные требования на
[47:38] функционирование кажется мы чуть больше
[47:40] уже не потратили чем нужно было то есть
[47:41] например уже можно было сказать так
[47:43] значит про рейтинге проще не говорим вот
[47:45] борьба за базовый функционал уж на это
[47:47] ушло на минут наверно 78 тусит хороший
[47:50] подход ну вот я бы на 3 функционал
[47:52] функционально устраивайте мы
[47:54] функциональность у меня бы устроило
[47:56] честно говорят на на третьем потому что
[47:57] мы видишь мы все равно не нашли не дошли
[47:59] даже до рейтинга то есть мы дальше
[48:01] скажем мы можем накручивать сюда ну она
[48:03] даст как бы накидывать свечей который
[48:05] тебя прямо сейчас приходят голову на
[48:07] потому церовани хватит время папа всем
[48:08] пунктами дара годится каждый зале хочу
[48:11] покрыть из моего опыта фейсбуке но
[48:14] обычно у тебя тоже был опыт фейсбуке
[48:15] положительный они таки не значит кафка
[48:19] так system design спрашивает а я нет
[48:21] никакого кафка вид что такое кафка
[48:24] message broker все
[48:27] понимаю но я в свою защиту писал на
[48:30] слайдах именно прим просто whirlwind
[48:32] босую а еще там же теперь лучше не
[48:35] говорить про мастерски но это пропарим
[48:37] праймари секунды
[48:38] доложны были все те говорят masters life
[48:41] уверяю по прежнему крайне редко но мне
[48:45] нечего сок добавить то есть никакого
[48:47] разбора я не вижу смысла здесь делать
[48:49] понять что дальше можно углубляться как
[48:52] ranking тоже туда праве парк stream но
[48:56] эта вещь весьма лет а вот эту сторону
[48:58] добавляем еще одну стрелочку нагружено
[49:01] эрнольд system design нужно еще нужно
[49:03] квадратик собственно ты сказал основное
[49:05] упущенные квадрате график хана и куча
[49:07] куча стрелы к из него
[49:09] таскать есть графа нам и оттуда кидаем
[49:13] неважно чем не очень понравилось у меня
[49:15] вопросов нет здесь вопрос что-то
[49:18] обсудить я думаю что вы забыли вопрос
[49:21] где мы будем есть стоит
[49:22] спасибо
[49:24] 7

FEEDBACK_MD:
---
section: "Feedback"
start: "46:20"
end: "49:27"
start_seconds: 2780
end_seconds: 2967
---

жизнь спасибо большое мне очень понравилось спасибо собственно ну я бы поставил х или стран ха я пожал 1 когда вы поставил эту оценку на этих интервью два момента про которые нужно один момент это мы забыли но потом вспомнили с подсказкой что в код 3 нужно еще учитывать и айдишники но этот индастриал обсудили именно как найти враги шарманку же побежали не учли это потому что у нас от этого могло сильно поменяться благо айдишники немного места занимали но если бы они занимались словно не 40 мегабайт и 400 гигабайт уже было бы возможно другое решение и паст момент который часто забывают о нужно сайт и он очень простой мониторинг мониторинг сервиса то есть бордель grafana либо равен графа ну следим за такими то метриками gps перцентиле все такая полировка так все отлично какие базы данных asset как redundancy делать а вот три сожалению тайминг в голове не держалась на это тяжело том что обычно когда ты проводишь свои часы с модели с что-либо в углу в три ноты откровенно говоря около укладывался то есть ты про все рассказал покрыла 3-дан дэнси написал функциональные требования на функционирование кажется мы чуть больше уже не потратили чем нужно было то есть например уже можно было сказать так значит про рейтинге проще не говорим вот борьба за базовый функционал уж на это ушло на минут наверно 78 тусит хороший подход ну вот я бы на 3 функционал функционально устраивайте мы функциональность у меня бы устроило честно говорят на на третьем потому что мы видишь мы все равно не нашли не дошли даже до рейтинга то есть мы дальше скажем мы можем накручивать сюда ну она даст как бы накидывать свечей который тебя прямо сейчас приходят голову на потому церовани хватит время папа всем пунктами дара годится каждый зале хочу покрыть из моего опыта фейсбуке но обычно у тебя тоже был опыт фейсбуке положительный они таки не значит кафка так system design спрашивает а я нет никакого кафка вид что такое кафка message broker все понимаю но я в свою защиту писал на слайдах именно прим просто whirlwind босую а еще там же теперь лучше не говорить про мастерски но это пропарим праймари секунды доложны были все те говорят masters life уверяю по прежнему крайне редко но мне нечего сок добавить то есть никакого разбора я не вижу смысла здесь делать понять что дальше можно углубляться как ranking тоже туда праве парк stream но эта вещь весьма лет а вот эту сторону добавляем еще одну стрелочку нагружено эрнольд system design нужно еще нужно квадратик собственно ты сказал основное упущенные квадрате график хана и куча куча стрелы к из него таскать есть графа нам и оттуда кидаем неважно чем не очень понравилось у меня вопросов нет здесь вопрос что-то обсудить я думаю что вы забыли вопрос где мы будем есть стоит спасибо 7

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
Write JSON only to: splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. system-design-senior-karpov-v3-2022-03-24.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.json \
    --video transcripts/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.json --out splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.qa-split.json \
    --video transcripts/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.validation-report.md

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
video.md: /Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/video.md

--- CHAPTER `01:37` — Problem Statement ---
window: 01:37 .. 02:50
recognition_status: single (1 items)

ITEM #1
  interviewer_question: time=01:37 text='Задача: спроектируй Uber-like сервис такси — где водитель и пассажир, поездки, глобально, ~500 млн пассажиров и ~5 млн водителей.'
  candidate_answer: time=02:50 text='Главная особенность — локальный матчинг: искать водителя рядом с точкой вызова, а не глобально как в Twitter.'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Product Metrics

--- CHAPTER `04:24` — Functional Requirements ---
window: 04:24 .. 07:20
recognition_status: single (1 items)

ITEM #2
  interviewer_question: time=04:24 text='Опиши функциональные требования для пешехода и водителя.'
  candidate_answer: time=04:42 text='Пешеход: указать адрес, найти водителя, поездка, профиль/оплата. Водитель: выйти на смену, принять/отклонить заказ, поездка, рейтинг, снова принять или завершить смену.'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Communication

--- CHAPTER `07:20` — Non-Functional Requirements ---
window: 07:20 .. 09:50
recognition_status: single (1 items)

ITEM #3
  interviewer_question: time=07:20 text='Какие нефункциональные требования?'
  candidate_answer: time=07:29 text='Низкая латентность поиска машины, высокая доступность, для водителя — заказы рядом, оптимальный маршрут/стоимость, прозрачность цены.'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Product Metrics

--- CHAPTER `09:50` — Estimate (preliminary assessment in terms of space and durability) ---
window: 09:50 .. 14:17
recognition_status: single (1 items)

ITEM #4
  interviewer_question: time=09:50 text='Сделай estimate: трафик, одновременные поездки, RPS.'
  candidate_answer: time=12:48 text='Порядка 1 млн поездок/день → ~10 RPS на инициацию; поездка ~1 ч → ~40k одновременных поездок; с учётом гео-поиска — сотни RPS на matching.'
  reference_answer: time=None text=None
  interviewer_feedback: time=14:15 text='Перейдём к оценке хранения информации.'
  question_topic: Product Metrics

--- CHAPTER `14:17` — Information Storage Assessment ---
window: 14:17 .. 18:49
recognition_status: single (1 items)

ITEM #5
  interviewer_question: time=14:17 text='Сколько места нужно для хранения профилей, поездок и данных сервиса?'
  candidate_answer: time=16:02 text='Отдельные сервисы: pedestrian, driver, matching/connection, trip history, payments; профили в БД, поездки в DWH/Kafka; гео-данные — отдельный location service.'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Data Modeling

--- CHAPTER `18:49` — GEO: How to Tell if a User and Driver are Nearby ---
window: 18:49 .. 25:22
recognition_status: single (1 items)

ITEM #6
  interviewer_question: time=18:49 text='GEO: как понять, что пользователь и водитель рядом?'
  candidate_answer: time=18:20 text='Нужен geo backend: хранить координаты водителей, быстро искать ближайших к точке заказа; не реляционная БД — KV/гео-индекс.'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Data Modeling

--- CHAPTER `25:22` — Quadtree Calculation for Moscow ---
window: 25:22 .. 29:35
recognition_status: single (1 items)

ITEM #7
  interviewer_question: time=25:22 text='Расчёт quadtree для Москвы — сколько уровней, сколько ячеек?'
  candidate_answer: time=25:22 text='Делим карту на квадранты рекурсивно; для Москвы оцениваем глубину дерева и число листьев в зависимости от требуемой точности и числа водителей в ячейке.'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Data Modeling

--- CHAPTER `29:35` — Description of Tree Search and Its Complexity ---
window: 29:35 .. 31:14
recognition_status: single (1 items)

ITEM #8
  interviewer_question: time=29:35 text='Опиши поиск по дереву и его сложность.'
  candidate_answer: time=29:35 text='Спуск по quadtree до нужной ячейки — O(log N) по глубине; в листе — список водителей; обновление позиции — пересчёт ячейки.'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Data Modeling

--- CHAPTER `31:14` — Can Search Be Hashed? ---
window: 31:14 .. 33:13
recognition_status: single (1 items)

ITEM #9
  interviewer_question: time=31:14 text='Можно ли захэшировать поиск?'
  candidate_answer: time=31:14 text='Хэш по координатам не заменяет гео-поиск — нужна структура по близости; кэшировать можно результаты запроса в hot-зонах.'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Data Modeling

--- CHAPTER `33:13` — Can we quickly see the driver's current position? ---
window: 33:13 .. 34:52
recognition_status: single (1 items)

ITEM #10
  interviewer_question: time=33:13 text='Можем ли быстро получить текущую позицию водителя?'
  candidate_answer: time=33:13 text='Да — частые обновления GPS в location service, in-memory индекс или quadtree с TTL; read по driver_id или по гео-запросу.'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Data Modeling

--- CHAPTER `43:36` — Redundancy and availability ---
window: 43:36 .. 46:20
recognition_status: single (1 items)

ITEM #12
  interviewer_question: time=43:36 text='Redundancy и availability — как обеспечить отказоустойчивость?'
  candidate_answer: time=43:36 text='Репликация geo и stateful сервисов, несколько AZ, health checks, graceful degradation при падении matching; Kafka для асинхронных side-effects.'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Data Modeling

SAVE JSON: вставьте ответ в конец файла /Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/system-design-senior-karpov-v3-2022-03-24/system-design-senior-karpov-v3-2022-03-24.v2.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
