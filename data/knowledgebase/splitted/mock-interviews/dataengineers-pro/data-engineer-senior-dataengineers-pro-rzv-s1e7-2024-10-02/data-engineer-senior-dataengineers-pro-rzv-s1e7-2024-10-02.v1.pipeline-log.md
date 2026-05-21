<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02",
  "transcript_folder": "transcripts/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/",
  "source_id": "data_engineer_senior_dataengineers_pro_rzv_s1e7_2024_10_02",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 20:45:07 +0200",
  "updated_at": "2026-05-20 20:54:38 +0200",
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
    "json": "splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02//timecodes.txt",
        "ru",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 20:45:07 +0200"
    },
    {
      "id": 2,
      "name": "qa_extraction",
      "llm": true,
      "model": "claude-sonnet-4-6",
      "inputs": [
        "splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.pipeline-log.md#LLM_INPUT_STEP_2"
      ],
      "outputs": [
        "splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.json"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 20:49:42 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 20:54:38 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02//video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 20:54:38 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/`
- **Source ID:** `data_engineer_senior_dataengineers_pro_rzv_s1e7_2024_10_02`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 20:45:07 +0200
- **Last updated:** 2026-05-20 20:54:38 +0200

Фильтр в IDE: `*data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02//timecodes.txt`<br>`ru`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.pipeline-log.md` | — | completed |
| 2 | qa_extraction | yes | claude-sonnet-4-6 | `splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.pipeline-log.md#LLM_INPUT_STEP_2` | `splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.json` | — | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02//video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.validation-report.md` | 1.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.pipeline-log.md`

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
SOURCE_ID: data_engineer_senior_dataengineers_pro_rzv_s1e7_2024_10_02
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/
INTERVIEW_LANGUAGE: ru
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00:06] Всем привет очередной выпуск МОК бесов в
[00:00:09] СНГ Я Алексей разводов напротив меня
[00:00:12] напротив виртуального стола сегодня
[00:00:14] Анастасия и мы проведём ещё один
[00:00:18] сес правила примерно такие же как обычно
[00:00:21] сегодня будет несколько новинок Так что
[00:00:24] оставайтесь не переключайтесь
[00:00:28] и до день Анастасия а Удобно ли перейти
[00:00:33] на тыву да Удобно хорошо собственно я
[00:00:37] сегодня представляю Дато инженеров
[00:00:39] компании X название компании и проект в
[00:00:42] основном под N который предложат
[00:00:45] подписать если пройдёшь этот этап
[00:00:49] поэтому давай постараемся сделать его
[00:00:51] интересным так чтобы провели на это
[00:00:54] время сейчас не
[00:00:55] зря и я собственно начинаем
[00:01:00] Расскажи про опыт который
[00:01:05] есть на текущий момент чем
[00:01:08] занималась Так ну начну наверное с
[00:01:11] самого первого места работы само пер на
[00:01:14] саты я работала как аналитик то есть в
[00:01:18] основном 80% моей работы было связано с
[00:01:21] Power Bi мы там настраивали различные
[00:01:23] отч для заказчиков работали с данными
[00:01:26] подключались к различным внешним
[00:01:28] источникам
[00:01:30] от и визуал
[00:01:32] встроены на этом месте работы
[00:01:34] соответственно вся компания и все
[00:01:36] сотрудники у нас работали исключительно
[00:01:38] с Power с моей стороны исходила
[00:01:41] некоторая инициатива по разработке Я на
[00:01:45] тот момент ещё училась в университете и
[00:01:47] писала диплом соответственно для диплома
[00:01:49] я использовала Python Ну и у нас была
[00:01:52] такая небольшая история что нам нужно
[00:01:55] было получать данные я
[00:01:58] ложила для Python мы его написали и
[00:02:01] внедрили это пошло хорошо а к сожалению
[00:02:04] примерно через 7-8 месяцев работы у
[00:02:07] компании пошли дела не очень и компания
[00:02:10] соответственно закрылась На следующее
[00:02:12] место работы я уже устроилась как Дато
[00:02:16] инженер а а в компанию занимающуюся Как
[00:02:20] продуктовой так и коммерческой
[00:02:21] разработкой а Вот соответственно у нас в
[00:02:25] компании не сильно-то большой на текущем
[00:02:26] месте это есть второе место работы штат
[00:02:28] дата инженеров соответственно Только я и
[00:02:31] мой руководитель А на текущем месте
[00:02:33] работы изначально м меня брали на
[00:02:36] коммерческий проект мм коммерческий
[00:02:39] проект э связан с таким холдингом
[00:02:42] который обслуживает э несколько тысяч
[00:02:45] различных компаний а соответственно все
[00:02:47] эти компании предоставляют данные по
[00:02:49] различным VPN сервисам и их
[00:02:51] пользователям и соответственно вот а с
[00:02:54] такими данными и приходилось работать а
[00:02:57] данные у нас хранились непосредственно
[00:02:59] кри
[00:03:00] ещё использовали в работе airflow для их
[00:03:04] обработки у нас строились
[00:03:09] [музыка]
[00:03:12] пайплайн То есть дата
[00:03:15] Марты
[00:03:17] так через некоторое время на текущем
[00:03:20] меся работы я перешла в продуктовую
[00:03:22] команду продуктовой команде мы
[00:03:24] занимались разработкой собственно Дато
[00:03:26] платформы в рамках продуктовой команды Я
[00:03:29] уже работа спарм в частности
[00:03:31] спарм на паспар мне довелось реализовать
[00:03:35] несколько экстракторов экстракторы к
[00:03:38] таким
[00:03:39] типам Ну к Цион базам данных
[00:03:42] это это экстракт
[00:03:47] экстрактор экстрактор КФ ИК Одис Ну
[00:03:51] подди я буду иметь в виду подключение по
[00:03:55] проколу для
[00:03:59] предусмотренны как бач так и микро бач
[00:04:02] режимы а для Кафки есть ещё и стриминг
[00:04:05] ну м я Почему разделяю микроба и
[00:04:07] стриминг потому что под микро бачо я
[00:04:09] понимаю это именно обработку через Spice
[00:04:11] Park а для стриминга мы использовали Уже
[00:04:14] именно чистые там кавка конектор и кавка
[00:04:17] коннекты Вот соответственно как-то так А
[00:04:20] ещё
[00:04:22] м в рамках Дато платформы у нас были
[00:04:26] реализованы трансформаторы Ну то есть в
[00:04:29] контексте процессов то что я
[00:04:30] рассказывала раньше это у нас как раз
[00:04:31] было буква как экстракторы А по
[00:04:33] трансформатору у нас подразумевали
[00:04:36] преобразования также бач и микроба Ну
[00:04:39] чое преобразование в принципе тут всё
[00:04:41] как обычно всё понятно а для микро Бача
[00:04:44] мы использовали
[00:04:47] ба Так ну и несколько лоде в принципе к
[00:04:51] тем же типам источников только список
[00:04:54] несколько урезанный
[00:04:56] в урезанный список у нас входит опять же
[00:05:01] И вот как-то так Ну и по-прежнему
[00:05:03] оставались задачи СФУ под airf Я
[00:05:07] подразумеваю то что мы там писали свой
[00:05:09] Да генератор для того чтобы вот
[00:05:13] приходящие от пользователей таски
[00:05:14] корректно обрабатывать и выстраивать их
[00:05:17] как Так
[00:05:19] а ну и несколько кастомных операторов
[00:05:25] необходимых Угу довольно много всего
[00:05:29] как-то так Расскажи побольше про
[00:05:31] хранилище какая там была модель как
[00:05:33] раскладывали данные Почему именно эта
[00:05:36] модель А ну хранилище у нас
[00:05:41] на у нас было несколько слоёв у нас был
[00:05:45] сурой слой и СН слой Ну особо как бы
[00:05:49] особого многообразия слоёв не было
[00:05:52] А по поводу разложения данных зависело
[00:05:55] ну в основном от типов задач и от
[00:05:58] необходимости пользователя то есть
[00:05:59] насколько они там между собой связаны в
[00:06:01] основном все задачи которые А ну точнее
[00:06:04] все данные которые получались
[00:06:05] посредством м выполнение экстрактов тасо
[00:06:08] они у нас все лежали в сыром
[00:06:13] слое если происходили какие-то
[00:06:15] дальнейшей трансформации то
[00:06:16] соответственно они уже переезжали дальше
[00:06:19] Угу То есть были витрины которые
[00:06:21] строились в том числе на сыром слое да
[00:06:24] да именно так а вот как понимаешь какие
[00:06:26] есть плюсы минусы Почему иногда стоит
[00:06:28] выбирать такой
[00:06:30] это может быть Почему именно у вас так
[00:06:33] выбрали Ну сырой слой как минимум
[00:06:36] позволяет хранить некоторую историчность
[00:06:39] данных ну то есть оставлять их такими
[00:06:41] какие они есть до преобразования Потому
[00:06:43] что если изначально встроены а какие-то
[00:06:46] преобразования и мы забираем данные Ну
[00:06:48] то есть пользователь видит данные
[00:06:50] которые он в итоге получает не S как они
[00:06:53] хранятся в источнике с некоторыми
[00:06:54] преобразованиями Возможно есть
[00:06:56] вероятность что вот эти преобразования
[00:06:58] могут вносить а ну не шум А скажем так
[00:07:01] есть вероятность что человек который Их
[00:07:03] делал мог накосячить как минимум вот а
[00:07:07] то есть если происходит какая-то ошибка
[00:07:10] как минимум это позволяет сразу пойти на
[00:07:12] сырой слой и посмотреть а если там в
[00:07:14] порядке значит ошибка пошла уже после об
[00:07:17] прощение дебаггинг О'кей Да Да А так м
[00:07:23] ну ещё может быть такой вариант что если
[00:07:27] это допустим какая-то историче
[00:07:30] исторические данные мы во втором слое
[00:07:32] храним полностью всю информацию а уже
[00:07:34] дальше мы собираем некоторую агрегацию
[00:07:37] которая вот актуаль именно в данный
[00:07:39] момент допустим для тех же аналитиков
[00:07:41] которые строят по ней отчёт А сколько
[00:07:44] табличек было на скидку на ром слое
[00:07:47] каких-то отдельных объектов
[00:07:50] Ну несколько
[00:07:56] тысяч Впечатляет
[00:07:59] они скажем так несколько тысяч ну потому
[00:08:03] что ну местами они друг друга
[00:08:05] дублировали скажем с разными названиями
[00:08:07] и тому подобные вещи местами это
[00:08:09] какие-то тестовые таблицы именно вот
[00:08:11] которые прямо использовались
[00:08:13] использовались ну скажем уже порядок по
[00:08:15] порядок будет поменьше около
[00:08:18] сотни О'кей то я уже испугался Как вы в
[00:08:22] тысячи объектов как-то разбирались с
[00:08:24] учётом того что там часть друг друга
[00:08:26] дублировали и здесь как раз
[00:08:29] Мне кажется мог бы помочь ещё какой-то
[00:08:31] слой ладно окей да возможно вот как бы
[00:08:35] для себя обозначила Где проходит грань
[00:08:37] между микро бачин
[00:08:47] гомстеди к которому все стремятся Ну так
[00:08:49] или иначе это
[00:08:51] нетай микро пач кажется где-то очень
[00:08:54] рядом Да микроба где-то рядом но тут
[00:08:57] зависит от того сколько
[00:09:01] Сколько может этот самый микроба процесс
[00:09:04] процеси в единицу времени Ну или какой у
[00:09:07] него отклик ожидания сколько секунд или
[00:09:11] миллисекунд если это допустим Ну вот как
[00:09:13] у нас было микроба использование Ну тут
[00:09:16] сразу стоит обозначить то что у нас
[00:09:18] впаке есть И если процеси каждую строку
[00:09:22] то ждёт когда соберётся объём для
[00:09:24] определённого Бача и он скажем Ну может
[00:09:27] не сразу собраться это уже точно и
[00:09:29] стриминг это уже точно отсылка к микро
[00:09:34] бачу Окей А витрины получается были
[00:09:36] также на С3 вот как выглядел
[00:09:38] презентационный слой с чем работали
[00:09:40] аналитики там дата сатанисты и подобные
[00:09:44] люди Ну у нас таких не было с ними не ну
[00:09:47] Дато саентистом не было были аналитики
[00:09:49] аналитики работали уже с конечными
[00:09:51] таблицами
[00:09:52] приведёнными к определённому виду Ну
[00:09:55] видимо не с историческими данными более
[00:09:58] агрегированные просто через deb селек
[00:10:00] или или был какой-то Bi Инструмент там
[00:10:03] какой-то другой
[00:10:04] доступ Ну у B дела был Bi инструмент
[00:10:08] Power Bi но я не работала с Bi
[00:10:11] инструментами конкретно я но вообще у
[00:10:13] нас в принципе есть развёрнутый суперсет
[00:10:15] но мы от него немножко ушли Потому что
[00:10:17] развернули рядом терла и в основном было
[00:10:20] удобнее пользоваться
[00:10:22] им Да чувствуется что есть определённый
[00:10:26] уровень подготовки у спецов что готов
[00:10:28] работать через jl клёво
[00:10:31] А так вот расскажи С какими трудностями
[00:10:36] сталкивалась когда обрабатывала
[00:10:38] стриминг именно трансформ на
[00:10:42] кафке Ну
[00:10:45] а а стриминг для Кафки
[00:10:48] Угу Ну как минимум базово просто
[00:10:51] прочитать через Space Park не получится
[00:10:54] приходилось Кать а там же у нас есть K
[00:10:57] value изначально приходит и вот
[00:11:02] узна пото что там внутри может ни напри
[00:11:05] дновский обе его нужно распарсить Скажем
[00:11:08] на несколько колонок сходу Вот это могу
[00:11:10] вспомнить
[00:11:12] а так ну есть ещё такой момент то что
[00:11:16] для того что нужно определённым образом
[00:11:20] конфигурировать саму кафку и топик при
[00:11:23] его создании чтобы к нему в принципе
[00:11:24] можно было подключиться и читать я
[00:11:26] конкретную опцию не назову но вот такой
[00:11:28] момент тоже был
[00:11:32] пом наверное всё что сходу могу
[00:11:36] вспомнить Окей А с какими-нибудь
[00:11:40] джоми на лету не сталкивалась Может быть
[00:11:44] какие-то как раз хотела рассказать но я
[00:11:46] с ними сталкивалась не с какой вот уже
[00:11:48] конкретно когда мы делали преобразование
[00:11:51] ну после экстракта Ну как минимум Джона
[00:11:54] первое с чем я столкнулась что если мы
[00:11:56] используем Джони уже не полу
[00:11:59] поэтому мы ушли к потому что через в
[00:12:03] принципе дж отрабатывают и на этом пока
[00:12:06] я остановились на такой
[00:12:10] реализации А вот может быть знала там
[00:12:14] смотрела как-то в других компаниях Как
[00:12:16] делают в других командах Можно ли
[00:12:18] всё-таки как-то
[00:12:20] стримить Точнее можно ли как-то дживы
[00:12:23] стриминговые данные какие-то может быть
[00:12:25] есть вариант реализации какие есть
[00:12:27] особенности
[00:12:31] сходу не вспомню
[00:12:34] смотрела именно для пайс парка и вот
[00:12:38] таким образом и нашла фары ба когда
[00:12:41] изначально столкнулись с этой проблемой
[00:12:44] и ранее На нём было принято решение
[00:12:47] временно приостановиться Окей В каком
[00:12:50] формате хранили на
[00:12:54] S3 в паркете у
[00:12:59] Почему в
[00:13:03] нём не могу ответить на этот вопрос не
[00:13:06] принимала такое
[00:13:11] решение
[00:13:13] А какие может быть есть альтернатива бы
[00:13:16] там читала
[00:13:18] интересовалась пошло ли дальше развитие
[00:13:20] в каких-то форматах
[00:13:25] хранения по поводу в плане
[00:13:29] паркета
[00:13:30] хранить Ну CSV кто-то хранит но мне
[00:13:34] кажется эта идея ещё хуже чем паркет
[00:13:50] А ну может знаю но сходу наверное не
[00:13:53] вспомню
[00:13:54] вот с дельтой айсбергом худи не
[00:13:58] сталкивалась
[00:13:59] да Вообще мы работаем с айсбергом То
[00:14:02] есть у нас таблицы как раз хранятся в
[00:14:03] АБЕ в АБЕ в айсбергов ском формате Угу
[00:14:07] некоторые Ну вот мы не так давно на него
[00:14:09] перешли
[00:14:11] А какие плюшки использовать в айсберге
[00:14:15] какие функции
[00:14:18] А сейчас
[00:14:26] помню вообще я наверное сходу больше
[00:14:30] назову проблему чем плюшку Потому что с
[00:14:32] проблемой я столкнулась тоже раньше в
[00:14:34] общем сейчас Есть такая тема то что у
[00:14:36] спарка и у айсберга различаются
[00:14:37] некоторые типы данных Угу например
[00:14:41] айдини по-моему листы то есть местами у
[00:14:45] них нейминг просто разный А есть такие
[00:14:47] типы которые например в спарке есть в
[00:14:48] айсберге их нет Или наоборот в айсберге
[00:14:50] они есть в спарке их нет такая была
[00:14:52] последняя проблема а
[00:15:00] Ну ещё если используешь Айсберг и Ну
[00:15:03] обязательно нужно дописывать при
[00:15:05] создании таблицы US АБЕ как минимум Но
[00:15:08] это просто не проблема Это такая
[00:15:11] особенность Ну из плюсов наверное может
[00:15:15] быть версионность то что отслеживаются
[00:15:18] изменения в
[00:15:23] таблице Ну
[00:15:25] вот это Тае основно
[00:15:29] я могу так
[00:15:30] вспомнить остальные Так я с чтобы время
[00:15:34] не тянуть Да хорошо А подскажи
[00:15:40] вот так получается АБЕ
[00:15:44] на3 А в качестве какого-то
[00:15:59] Ну да у него же есть айсбергов ский
[00:16:01] местор Да он есть как раз
[00:16:04] айсбергов Да
[00:16:07] Окей там тоже была такая проблема то что
[00:16:11] мы обновляли в один момент Айсберг
[00:16:15] и по-моему получилось так то что мы
[00:16:18] Обновили сам Айсберг а местор не
[00:16:20] Обновили То есть он остался старый но
[00:16:23] сами таблицы физические у нас ушли в
[00:16:25] одну из баз А и они Короче не просто
[00:16:29] ушли А там же есть несколько каталогов
[00:16:32] там есть СР каталог и есть обычный
[00:16:34] каталог дефолтный какой-то и общем они
[00:16:37] как бы физически у нас ушли но они
[00:16:39] остались жить в определённом каталоге
[00:16:41] если просто делаешь Show T и там
[00:16:44] определённое датабаза то он не
[00:16:45] показывает этой таблицы но когда
[00:16:47] пытаешься её удалить он её не удаляет
[00:16:49] Потому что говорит что в стори она не
[00:16:53] прописана то есть мы просто обновляли а
[00:16:55] просто обновили
[00:16:59] както Да Дада всё подсоса что нужно и
[00:17:02] всё
[00:17:08] заработало так Окей вообще конечно
[00:17:12] интересный проект столько разных
[00:17:14] технологий Подскажи
[00:17:18] Зай есть ли какой-то опыт по
[00:17:20] масштабированию Есть ли понимание Как
[00:17:23] можно вот
[00:17:26] подготовить какие-то джипы там какие-то
[00:17:28] топить
[00:17:29] к тому чтобы через этото лилось там не
[00:17:31] знаю в 10 раз больше сообщений чем
[00:17:33] сегодня в 1.000 раз больше нет
[00:17:35] масштабированием я не занималась
[00:17:38] а не читал ничего
[00:17:44] м именно про масштабирование самих
[00:17:47] данных или ресурсов Я знаю про
[00:17:49] вертикальное горизонтальное
[00:17:51] масштабирование но здесь скорее какие
[00:17:54] есть абстракции в кафке которые могут
[00:17:57] помочь Нет точно например несколько
[00:17:59] коров подключать к одному
[00:18:03] топику Нет точно не отвечу
[00:18:06] у
[00:18:11] Окей
[00:18:14] Так расскажи Зачем нужно было писать
[00:18:17] кастомные операторы на
[00:18:19] airflow ни же уже написаны
[00:18:23] тысячи Ну у нас была такая конкретная
[00:18:26] необходимость за счёт изза входного
[00:18:29] формата данных и в принципе у нас была
[00:18:31] разработана Ну как реализован свой
[00:18:35] отдельный пакет а для того чтобы
[00:18:38] корректно парсить конфиг приходящий То
[00:18:40] есть у нас airflow был настроен на Дис в
[00:18:42] дис прилетали определённые конфиги их
[00:18:45] нужно было распарсить нашей кастомной
[00:18:46] библиотекой ещё их внутри рекурсивно
[00:18:49] шаблони Зро то есть некоторые а фильтры
[00:18:52] airflow они были Ну примерно на третьем
[00:18:56] слое хранящегося в редисе
[00:19:00] Угу нужно было их вот рекурсивно нить
[00:19:04] это вот как раз про генерацию
[00:19:06] да
[00:19:08] да Зачем так
[00:19:11] сложно тава была
[00:19:14] необходимость так исторически сложили да
[00:19:18] да так исторически
[00:19:21] сложилось
[00:19:22] Ясно ну просто есть кажется какие-то
[00:19:25] варианты с там тем что парт Я файлы
[00:19:28] подают вход Ну он был не совсем прямо
[00:19:30] кастомный то есть это был Наследник спар
[00:19:33] кубернетес оператора просто немножечко
[00:19:35] долинный угу вот как работало с airflow
[00:19:40] в губере Как там логи читала как
[00:19:42] подключалась были ли какие-то трудности
[00:19:45] или это всё вот как-то настроили Оно
[00:19:47] просто работало
[00:19:50] Ну базовый ответ настроили Оно просто
[00:19:53] работало не базовые иногда возникали
[00:19:55] некоторые проблемы с адресацией то есть
[00:19:57] внешний внутренний адрес Например
[00:20:00] Раз везде полу внутре ГТО стами забыли
[00:20:04] что-то прокиды Он оставался внутренним А
[00:20:07] так в принципе всё было
[00:20:09] настроено бы заведены коне определённые
[00:20:13] на
[00:20:15] чере ну и соответственно кубовский конф
[00:20:17] тоже туда прокиды поэтому Они между
[00:20:19] собой хорошо общались
[00:20:28] соответственно для airflow был отдельный
[00:20:30] mes Space там для бэнда отдельный mes
[00:20:32] Space и просто в name Space airflow все
[00:20:34] логи очень хорошо доходили все читались
[00:20:36] Угу Ну вот как физически это выглядело
[00:20:39] что это просто подтягивались в юай и там
[00:20:41] можно было это всё читать или надо было
[00:20:43] как-то в по для пользователей для
[00:20:46] пользователей Да потя делалась юай то
[00:20:48] есть всё стандартно заходишь в Дак там
[00:20:50] есть определённые таски жмёшь на таку и
[00:20:54] читаешь логи а для
[00:20:56] разработчика ну Смотря как если ты
[00:21:00] локально
[00:21:01] разрабатывает то Ну в дебаг режиме
[00:21:04] запускаешь смотришь что кого не так
[00:21:06] пошло А если ты хочешь посмотреть что-то
[00:21:08] что на прозе было то опять же заходишь в
[00:21:10] контейнер читаешь логи смотришь что
[00:21:14] конкретно уехала airflow у нас как
[00:21:16] работал
[00:21:17] он общался с парком который был в
[00:21:19] кубернетес и соответственно на каждую
[00:21:21] задачу делал сабмит оператор и самил
[00:21:25] саму таку в отдельный Space с парковский
[00:21:28] а И следующий следующая итерация в тас
[00:21:31] была уже мониторинг под мониторингом я
[00:21:33] понимаю непосредственно исполнение самой
[00:21:35] джаббы
[00:21:38] Угу О'кей А как эта вся система общалась
[00:21:42] с какими-то внешними источниками Ну вот
[00:21:44] есть там
[00:21:46] I например или может быть э м было ли
[00:21:51] такое что какую-то часть интерфейса
[00:21:54] прокиды наружу из кубера
[00:21:59] нет такого то есть мы можем без проблем
[00:22:02] подключаться к каким-то внешним
[00:22:05] источникам если Ну это скажем источник
[00:22:08] данных какой-то внешний Да это всё
[00:22:10] корректно работало
[00:22:13] необходимости интегрироваться Ну не в
[00:22:16] качестве источника данных а так с
[00:22:18] каким-то внешним Ну вроде как не
[00:22:20] возникало или если возникало то это было
[00:22:22] до меня и я скажем не наслышана а не
[00:22:25] смотрела Как именно это было реализовано
[00:22:28] то есть А что именно что со стороны
[00:22:31] кубера и как нужно настроить чтобы он
[00:22:34] начал общаться с внешним миром и был
[00:22:37] скажем увидел какой-то внешний
[00:22:41] сервис нет нет в эту сторону не
[00:22:49] смотрела так Окей Было
[00:22:53] ли так получается что сами таски
[00:22:57] запускались в каких-то отдельных подах
[00:22:59] вот этом кубернетес под
[00:23:02] оператор бы раз в каких-то соседних
[00:23:06] подах то есть всё всё в кубе было
[00:23:09] А да всё было в кубе то есть на каждую
[00:23:12] спарко вскую ДБУ у нас имелся свой
[00:23:14] собственный пот драйвер
[00:23:17] Фло на каждую отдельную таку мы
[00:23:19] получается на каждый Дак тоже свой
[00:23:22] отдельный под уже в другом на спейсе
[00:23:24] эском поэтому оно всё очень хорошо между
[00:23:26] собой разделяло Угу и отслеживал есть Ну
[00:23:29] вот например с точки зрения разработки и
[00:23:32] попытки понять где была ошибка всё так
[00:23:35] как живёт в раздельных найм спейсах это
[00:23:37] всё не путается между собой и довольно
[00:23:39] просто найти по соответствию Что именно
[00:23:42] пошло не
[00:23:46] так угу А вот здесь Расскажешь
[00:23:49] чего-нибудь
[00:23:51] про м скейлинг то есть было ли такое что
[00:23:55] для какой-то таски нужно было больше
[00:23:57] выделять ресурсов чем другим как
[00:23:59] управляли вот этой приоритизации тем
[00:24:01] кому сколько ресурсов
[00:24:05] раздавать Да были некоторые задачи была
[00:24:09] Басовская база с довольно большой
[00:24:12] таблицей которую Ну которую который
[00:24:16] нужно было подключить через экстрактор
[00:24:18] Ну её просто прочитать и вторая задача
[00:24:20] была интервально прочитать и вот когда
[00:24:22] была фува её перегрузка просто в
[00:24:24] хранилище как она есть там Возникала
[00:24:27] проблема и увеличивали ресурсы Как раз
[00:24:32] за счёт увеличения ресурсов проблема
[00:24:34] ушла
[00:24:35] как а в
[00:24:37] конфиге с парковской прописывали а
[00:24:40] больше памяти выделяли на
[00:24:47] экю и получается Если там вот лову
[00:24:50] загрузку нужно сделать один раз то
[00:24:52] добавляли памяти потом переходила на
[00:24:54] инкремент и убирали память Угу
[00:25:00] Окей А вот Расскажи про инкрементальные
[00:25:03] загрузки как это всё работало с S3 там
[00:25:07] вроде бы не очень хорошо работает с
[00:25:08] дописывая в какой-то файлик
[00:25:11] А ну с инкремента загрузкой Да у нас был
[00:25:15] такой тип реализован то есть получается
[00:25:16] он работал Так что
[00:25:18] А ну загружаешь какой-то источник данных
[00:25:22] хочешь его прочитать инкремента и если в
[00:25:27] мере
[00:25:28] нет указания для этой таблицы то что
[00:25:30] ранее она перегружать инкремента то
[00:25:33] ставишь Ну пользователь как с этим
[00:25:35] работал со стороны пользователь наверно
[00:25:36] объясню будет немножко попроще
[00:25:38] пользователь выбирает какую-то колонку
[00:25:40] если это реляционная база в которой
[00:25:42] например содержится АШК Ну предусмотрено
[00:25:45] то что это айдини если в место нет
[00:25:47] информации по этой таблице что она ранее
[00:25:49] инкремента перегружать то она
[00:25:50] перегружается целиком то есть самого
[00:25:52] первого шника до такого который она есть
[00:25:55] допустим это всё устроено как Да который
[00:25:57] у нас запускается
[00:25:59] у на завра и скажем в эту таблиц кто-то
[00:26:01] е дописал данные наступает следующий
[00:26:04] день у нас снова запускается э таска и
[00:26:06] видно то
[00:26:08] что появились следующие Аники после того
[00:26:11] максимального который
[00:26:13] прописан берём строки именно вот по этим
[00:26:16] очникам и их через описываем к уже
[00:26:18] существующей таблице
[00:26:28] капот делами занимался Айсберг и всё
[00:26:32] просто
[00:26:33] работал ну почему вот э логику с с тем
[00:26:38] чтобы Сходи в местор Посмотри какой там
[00:26:40] айдини прописан это это не Айсберг это
[00:26:44] приходилось Ну
[00:26:48] разрабатывать просто интересно как это
[00:26:50] на уровне файлов
[00:26:52] работало Ну файл оставался тем же самым
[00:26:55] Просто он больше по объёму становился за
[00:26:57] счёт того что туда что-то Вась именно
[00:26:59] вот с точки зрения файла с точки зрения
[00:27:02] если ну его как таблицу читать потому
[00:27:05] что они в формате обычных таблиц
[00:27:07] сохранялись то Ну это просто таблица в
[00:27:08] которые добавлялись добавлялась строк
[00:27:12] или не
[00:27:13] добавлялась если изменений не было
[00:27:15] Расскажи про партицирование
[00:27:17] Было ли в системе как с этим работали
[00:27:21] а да Было такое Было изначально Так что
[00:27:25] У пользователя есть возможность
[00:27:27] самостоятельно выбрать колонки
[00:27:28] порционирования и скажем задать если
[00:27:32] пользователь этого не задаёт то в
[00:27:34] процессе уже выполнения скобы
[00:27:36] анализировала что туда
[00:27:38] пришло брался определённый лимит то есть
[00:27:41] первые 100 строк из таблицы если она
[00:27:43] большая по этим строкам
[00:27:46] определялся сейчас вос произведу
[00:27:51] [музыка]
[00:27:53] определялась нет не так не так было Это
[00:27:56] было позже
[00:28:00] типы которые туда приходят там и
[00:28:04] строковые и если был скажем какой-то или
[00:28:07] тип ID его выбирали
[00:28:11] как
[00:28:13] илита это всё прямо совсем автоматически
[00:28:17] работало Ну это было реализовано уже в
[00:28:20] самом то есть мы это сами
[00:28:21] реализовывали Ну это я понял да просто
[00:28:24] это кажется довольно важное решение с
[00:28:26] точки зрения дальнейшей работы с
[00:28:28] таблицей каким-то объектом с тем как это
[00:28:31] всё будет дальше жить как это будет
[00:28:33] вариться и получается это всё по
[00:28:36] автоматике было при том что у вас было
[00:28:37] там Примерно 100 родовых объектов Вот
[00:28:40] расскажи Почему решили настолько глубоко
[00:28:42] это всё
[00:28:45] автоматизировать ну потому что
[00:28:47] изначально подразумевалось что этим
[00:28:49] будут пользоваться люди которые не
[00:28:52] сильно в это
[00:28:53] погружены и скажем так им по специфике
[00:28:57] их работы ну то есть они не должны про
[00:28:58] это знать изначально подразумевал что
[00:29:00] этим будут пользоваться люди у которых
[00:29:02] нет нет таких базы знаний просто потому
[00:29:05] что её не должно у них быть и если мы
[00:29:08] можем там автоматически предложить им
[00:29:10] какое-то более-менее оптимальное решение
[00:29:12] за них то это будет хорошо потому что
[00:29:14] всё-таки это людям поможет за счёт того
[00:29:16] что это будет немножечко быстрее О'кей я
[00:29:19] понял расскажи какие есть плюсы и минусы
[00:29:22] У того чтобы пользователям отдавать
[00:29:24] права вот принимать решения в таких
[00:29:26] моментах допустим мы разрабатываем
[00:29:29] какой-то интерфейс какой-то инструмент
[00:29:31] который может сконфигурировать новый
[00:29:34] поток загрузку из какого-то нового
[00:29:35] источника он сформирует табличку
[00:29:37] табличку можно будет подцепить к
[00:29:40] витринам и потом над этих над этими
[00:29:43] витринами там строить какие-нибудь
[00:29:45] графики какую-то аналитику Вот какие
[00:29:48] есть плюсы минусы таких подходов плюсы с
[00:29:50] точки зрения вот допустим предоставлять
[00:29:52] пользователю право выбирать там колонки
[00:29:54] партиционирование и количество партиции
[00:29:56] то что ну не очень хорошо звучит Но это
[00:29:59] становится ответственностью пользователя
[00:30:01] если он выбрал что-то не оптимальное то
[00:30:03] есть ну как бы ты сам это выбрал это
[00:30:04] становится твоей ответственностью минус
[00:30:06] банальный в том что это может быть
[00:30:08] выбрано не оптимально и это будет очень
[00:30:10] неплохо так жрать ресурсы когда могло бы
[00:30:13] жрать не так сильно А как минимум Вот
[00:30:15] это также Ну из плюсов можно сказать то
[00:30:18] что а скорее всего м так как
[00:30:21] пользователь самостоятельно завозит себе
[00:30:23] соединение в системе Ну то есть на
[00:30:24] какой-то источник с которым он знаком он
[00:30:26] более погружён и
[00:30:28] в контексте предметную область самого
[00:30:30] этого источника То есть у него знаний о
[00:30:32] НМ Побольше чем если я скажем приду и
[00:30:36] пытаться там за час что-то горящее
[00:30:38] решить то есть
[00:30:40] пользователь больше в контексте И за
[00:30:43] счёт его контекста если он там ну скажем
[00:30:46] представим что он там интересуется этим
[00:30:48] что он посмотрел всё-таки Что такое
[00:30:49] партиционирование когда всё это увидел
[00:30:51] есть вероятно что примет правильно
[00:30:56] рение именно вот конкретно ему под его
[00:30:59] задачу Угу А
[00:31:02] вот Окей
[00:31:05] принимается Я сейчас так подумал а где в
[00:31:07] этой всей системе кури или он был на
[00:31:10] первом проекте а кури был на первом
[00:31:12] проекте который был не продуктовый
[00:31:18] Угу Так Окей как бы описала В чём
[00:31:22] разница между какой и ра битом а
[00:31:26] [музыка]
[00:31:29] Ну в рете очереди в кафке топике кавка
[00:31:34] больше подходит для стриминга чем Потому
[00:31:40] что ну просто кавка больше подходит для
[00:31:44] стриминга зря
[00:31:47] сказала сказала потому что
[00:31:50] вот ну как минимум потому что допустим
[00:31:53] если использовать какие-нибудь конек
[00:31:59] коннектора нет но можно данные которые
[00:32:01] хранятся в очереди реб бита через кавка
[00:32:03] коннектор перезаписать в кафку Угу и
[00:32:07] тогда уже их оттуда
[00:32:11] стриминговая не микроба это будет уже ну
[00:32:14] более приближённая прямо к самому
[00:32:16] настоящему стриминга Тогда вопрос зачем
[00:32:19] Т Ну у пользователь есть необходимость
[00:32:22] пользоваться изначально ртом скажем так
[00:32:24] как источником данных вот он хочет ребит
[00:32:28] Угу очень много власти у ваших
[00:32:31] пользователей было возможности влиять на
[00:32:33] это
[00:32:34] всё даже прямо завидую всё для
[00:32:37] них
[00:32:40] О'кей А вот э навеяно Этой темой
[00:32:45] Расскажи
[00:32:46] про доставку сообщений в распределённых
[00:32:49] системах Какие могут быть трудности
[00:32:52] может быть какие есть три основных
[00:32:55] подхода к тому как это можно
[00:32:57] организовать
[00:33:00] могу нено вот этих ключевых слов если
[00:33:04] будет надо ага Да это наверное
[00:33:08] пригодится потому что я этим особо почти
[00:33:10] не занималась но скорее всего трудность
[00:33:12] может быть в том что а сообщение или
[00:33:15] часть сообщений может потеряться в
[00:33:17] какой-то момент из какой-то очереди и
[00:33:20] во-первых первый пункт Это плохо что они
[00:33:22] в принципе потерялись второй пункт нужно
[00:33:25] понять В какой момент Они потерялись
[00:33:27] какого Ну то есть именно вот интервал
[00:33:30] потери
[00:33:32] чтобы ну его определить и понять масштаб
[00:33:35] вообще в принципе А так
[00:33:39] а третье
[00:33:44] А ну так встретим пока Притормози Ну вот
[00:33:49] с точки зрения допустим работы через
[00:33:51] Айсберг чтение ивки А как минимум есть
[00:33:55] чекпоинты
[00:33:58] чекпоинты в принципе в этом могут помочь
[00:34:00] если что-то свалится то останется
[00:34:02] чекпоинт и он Старт Вот именно с этого
[00:34:04] чекпоинта в следующий раз
[00:34:07] Окей Ну возможно ещё с этим может помочь
[00:34:11] какая-нибудь
[00:34:16] репликация Ну тогда оно может во всех
[00:34:20] репликах пропасть сначала на глав
[00:34:24] потом этоже
[00:34:27] во всех репликах хорошо Хорошо
[00:34:30] согласен Вот есть доставка как минимум
[00:34:34] один раз как максимум один раз и точно
[00:34:37] один
[00:34:39] раз Слышала про них А да да слышала Вот
[00:34:45] какая например в кафке или там какая
[00:34:48] была ва у вас в системе
[00:34:51] и как думаешь что могло повлиять на
[00:35:00] [музыка]
[00:35:01] так
[00:35:03] exactly и at least правильно
[00:35:09] Да какая у нас была я не
[00:35:12] скажу Ну по-моему наиболее
[00:35:16] востребованный из этих трёх - это
[00:35:18] [музыка]
[00:35:21] а at least Если не ошибаюсь
[00:35:30] ой если простыми
[00:35:31] словами это значит что у нас могут
[00:35:33] данные задули и это нормально мы как-то
[00:35:37] с этим
[00:35:38] работаем значит что мы можем иногда
[00:35:40] терять данные Но если Они доходят Тони
[00:35:42] доходят максимум один раз И когда мы
[00:35:45] гарантируем что мы ничего не теряем и
[00:35:47] ничего не дублируем Ну третий вариант
[00:35:50] звучит слишком
[00:35:56] идеального дублируются но они дойдут А
[00:35:59] как работать с дубликате это скажем так
[00:36:01] другой вопрос но он вероятно решаемый То
[00:36:04] есть это порождает новую проблему но
[00:36:06] решает проблему
[00:36:08] с с потерей данных Да как многие
[00:36:13] какие-то решени в инженерном
[00:36:16] мире хорошо а
[00:36:19] вот как можно из at least получить EX
[00:36:28] Ну брать дупликации Угу
[00:36:33] хорошо
[00:36:39] так вот как бы Ты оценила Чем отличается
[00:36:43] постгрес и
[00:36:46] mssql Ну они обе реляционные базы
[00:36:49] банально Не
[00:36:51] множе синтаксисом даже в самых простых
[00:36:56] запросах скажем при работе с датами есть
[00:36:59] там некоторые нюансы
[00:37:02] А ну в msq есть инстансы в постгрес их
[00:37:10] нет А что такое инс
[00:37:13] в Ну банально если подключаешься не знаю
[00:37:18] через какой-нибудь вивер или dat grip то
[00:37:21] для MS обязательно нужно указывать
[00:37:23] instance для поса достаточно именно базу
[00:37:26] прописать
[00:37:29] Угу то есть в MS скиле может быть
[00:37:32] несколько баз данных рядом в постгрес
[00:37:35] такого не может
[00:37:38] быть Ну несколько инстан сов может быть
[00:37:41] может быть в MS сле Ну вот instance база
[00:37:45] данных схема таблица Типа такая
[00:37:47] вложенность Да да да А чем тогда
[00:37:50] отличается инс от какого-то конкретного
[00:37:53] сервера на котором развернут MS Skill
[00:38:01] Ну возможно что на instance могут быть
[00:38:04] разные права вообще и на базе могут быть
[00:38:07] разные права но видимо вот на таком же
[00:38:10] уровне то что У какого-то пользователя
[00:38:12] есть право там на все допустим истан А у
[00:38:14] другого только на инс X например
[00:38:18] ещё чего добавишь
[00:38:21] А больше ничего не
[00:38:25] добавлю Окей
[00:38:33] так вот давай немного предложу
[00:38:37] порассуждать если мы берём базу типа там
[00:38:41] того же поса то там большое
[00:38:45] такое внимание уделено индексам тому как
[00:38:49] их там правильно
[00:38:56] уза если мы берём какие-то Дато
[00:38:58] инженерные задачи Вот те же самые ула
[00:39:02] базы то там индексы вспоминают намного
[00:39:05] реже если в принципе вспоминают как бы
[00:39:08] ты проинтерпретировать
[00:39:10] объяснила почему индексы практически не
[00:39:14] востребованы в olab хранилищах и может
[00:39:16] быть что вместо
[00:39:19] них так Ну получается allp oltp - это у
[00:39:24] нас транзакционные ну transaction а
[00:39:27] больше
[00:39:28] аналитические Так ну sotp требуется
[00:39:32] более быстрый ответ как я понимаю ну вот
[00:39:35] допустим насколько я знаю то что в
[00:39:37] банках где-нибудь используется ltp Ну
[00:39:39] там например когда деньги переводишь
[00:39:40] транзакция должна быть либо полностью
[00:39:42] совершена либо полностью не совершена то
[00:39:44] есть она не может быть совершена
[00:39:46] частично скажем
[00:39:49] А ну поэтому как раз используются
[00:39:52] индексы индексы же предназначены в
[00:39:54] принципе для ускорения именно чтения
[00:39:57] чтение из базы Ну была кажется тоже было
[00:40:00] бы полезно побыстрее
[00:40:02] читать
[00:40:05] м было бы полезно но
[00:40:21] а ну из названия Если oltp
[00:40:26] транзакционный то алап - это
[00:40:27] аналитический
[00:40:29] Угу Ну если он аналитический Может есть
[00:40:32] необходимость их как-то а данные сами по
[00:40:37] себе ну ну нет наверное имела в виду то
[00:40:41] что в плане с разных сторон
[00:40:42] рассматривать и не делать привязку в
[00:40:45] таблице каким-то конкретным
[00:40:48] индексом потому что это более гибко
[00:40:50] скажем
[00:40:51] так потребность их смены может часто
[00:40:54] меняться О'кей идея понятна
[00:40:58] Есть ли
[00:41:02] ещё Ну может быть приоритеты у в
[00:41:08] принципе у таких типов хранилищ Ну в
[00:41:10] плане приоритеты как операции базовые
[00:41:13] чтение и запись Угу если в ltp
[00:41:16] преимущественно записывать что вот
[00:41:18] допустим пользователь там перевёл
[00:41:19] другому 100 руб
[00:41:21] да то в лапе наоборот нужно в основном в
[00:41:25] основном из них читаю чем туда пи чтение
[00:41:27] хорошо подходят индексы разве нет ну
[00:41:30] вообще да индексы как раз для чтения
[00:41:33] лучше чем для
[00:41:35] записи Ну вот м давай немного поглубже
[00:41:39] берём какую-нибудь пагр берём вот
[00:41:42] какой-нибудь классический индекс
[00:41:44] кластерный как он выглядит ну скажем
[00:41:49] немного ближе к вот уровню файлов данных
[00:41:53] страниц чего-то такого Какая структура
[00:41:55] данных
[00:41:58] Ну индекс если он есть он же как раз Ну
[00:42:01] вот по страницам делит и ищет в каждой
[00:42:03] странице определённые совпадение на
[00:42:06] основе
[00:42:07] выстроено а делит Ну на основе того как
[00:42:11] сформирован как сформированный индекс Ну
[00:42:14] и какая у него там селективность с точки
[00:42:15] зрения запроса Ну хорошо А ну в постгрес
[00:42:18] очень много индексов я думаю что ни я ни
[00:42:21] ты не хотим туда очень глубоко сейчас
[00:42:24] закапывать если брать там не знаю
[00:42:27] какое-то вот это вот дерево классическое
[00:42:29] V3 Ага
[00:42:32] То что у тебя на
[00:42:34] выходе когда ты отправляешь какой-то
[00:42:37] запрос вот индекс Верни мне там что-то
[00:42:39] вот это что-то Это
[00:42:42] что
[00:42:45] мм Ну какая-то запись в таблице если это
[00:42:48] реляционная база ну возвращается
[00:42:50] соответственно Ну вообще по факту
[00:42:52] возвращается тоже реляционная таблица
[00:42:54] просто ограниченная там
[00:42:58] забираем кокрок
[00:43:01] и если мы берём какой-то типичный алап
[00:43:04] запрос типа вот постройка мне отчёт за
[00:43:07] месяц то там сколько таких операций
[00:43:10] нужно сделать чтобы все нужные строки
[00:43:18] достать Ну больше чем Ну построить отчёт
[00:43:22] за
[00:43:25] месяц Ну как минимум нам сгруппировать
[00:43:27] нужно видимо по определённому месяцу
[00:43:30] Возможно есть определённая фильтрация
[00:43:34] Угу Ну и вы если мы применяем индексы то
[00:43:37] нам нужно получается каждую строчку
[00:43:39] вернуть то есть понять там допустим у
[00:43:42] нас вот есть этот месяц и пробежаться по
[00:43:44] индексу вот каждый раз возвращая по вот
[00:43:47] этой одной строчке
[00:43:48] А сейчас сможешь
[00:43:51] прикинуть с точки зрения алгоритмической
[00:43:55] сложности
[00:43:57] сколько бы занимала такая операция для
[00:43:59] одной строки и в каких случаях
[00:44:03] оптимизатор может отказаться от
[00:44:04] использования индекса Даже даже если он
[00:44:06] есть и там пройти просто сверху вниз по
[00:44:10] всей
[00:44:12] таблице использования индекса может если
[00:44:15] таблица маленькая сама по себе то есть
[00:44:17] там ну она сама по себе небольшая первый
[00:44:21] случай ВТО случай может ин
[00:44:26] выре активность скажем если это какая-то
[00:44:29] таблица там с данными про людей а в
[00:44:32] качестве индекса например выбран пол
[00:44:34] мужской или женский А ну и Ну
[00:44:37] предположим предположим что там примерно
[00:44:39] поровну мужчин и женщин то использование
[00:44:41] индекса вообще смысла в данном случае
[00:44:43] особенно му не име не Ну почему сначала
[00:44:45] срезаем половину таблицы потом по
[00:44:47] остальной половине таблицы проходим
[00:44:50] сверху вниз кажется в два раза Быстрее
[00:44:52] Всё равно
[00:44:54] неплохо Ну вообще я проверяла как раз
[00:44:57] работала с подобной таблицей когда
[00:44:58] изучала индексы и делала индекс именно
[00:45:00] на пол и он был Ну примерно результат
[00:45:03] был примерно такой же как без индекса
[00:45:05] Угу это особо никакого привеса не
[00:45:08] принесло а не смотрела Там план запроса
[00:45:10] он вообще
[00:45:12] использовался А я смотрела через Алай и
[00:45:15] индекс как раз вообще ну не использовал
[00:45:18] Ну не использовался скорее
[00:45:24] Угу Ну вот с точки
[00:45:28] зрения как-то сможешь сейчас
[00:45:31] прокомментировать или затрудняешься
[00:45:34] вот
[00:45:37] которы не услышала Последнее
[00:45:41] А если мы берём Ну там вот эти два
[00:45:44] случая когда мы вытаскиваем строку через
[00:45:49] индекс сколько это будет занимать в там
[00:45:52] каком-то среднем в предельном
[00:45:54] варианте Ну по вот это вот о от
[00:45:59] и в каком случае невыгодно будет идти
[00:46:03] этим путём и лучше просто просканировать
[00:46:06] всю таблицу сверху
[00:46:09] вниз Ну я уже называла случаи когда
[00:46:13] использовать индекс может быть нелогично
[00:46:16] скажем с точки зрения математики вот там
[00:46:19] можно
[00:46:20] вывести Две таких зависимости и они
[00:46:23] будут пересекаться в какой-то точке и
[00:46:25] потом одна там продолжит расти А вторая
[00:46:27] будет примерно Вот вот так вот
[00:46:29] уходить Ну то есть одна будет
[00:46:31] экспоненциальная
[00:46:34] видимо плюс-минус
[00:46:37] а вторая Ну если продолжит расти то
[00:46:40] видимо
[00:46:42] Линейная А может ли быть там где-то
[00:46:44] логарифмическая
[00:46:46] Да может быть логарифмическая и
[00:46:50] квадратная может
[00:46:52] быть да может быть квадратная вот каки
[00:46:57] из этих четырёх два случая
[00:47:00] здесь ну квадратная и логарифмическая
[00:47:04] скорее а Почему
[00:47:08] квадратная Ну наверное всё-таки не
[00:47:10] квадратная а степень будет зависеть от
[00:47:17] А в индексе Может быть как раз ивик же
[00:47:22] может быть составным
[00:47:24] Угу любопытно
[00:47:28] Ну возможно совсем неправильно Давай
[00:47:31] пойдём
[00:47:33] дальше когда ты работала с B quy вот как
[00:47:38] бы ты описала какие есть особенности у
[00:47:41] этой базы Что нужно учитывать когда ты с
[00:47:44] ней
[00:47:52] работаешь Ну особых каких-то
[00:47:54] синтаксических особенностей
[00:47:56] при работе с кри Ну именно в запросах я
[00:47:59] не выявила каких-то существенных разниц
[00:48:03] А по особенностям
[00:48:08] работы ну то что как это Облачно было
[00:48:14] так в принципе как на улице А как это
[00:48:16] проявлялось что это Облачно вот какая
[00:48:18] разница между тем что запрос кри
[00:48:20] отправляешь между тем что ты его
[00:48:21] отправляешь где-нибудь там на он Прими
[00:48:24] железе
[00:48:29] [музыка]
[00:48:30] а ну если на железе то может быть
[00:48:34] зависить
[00:48:37] от от ресурсов компа например которым
[00:48:41] это
[00:48:42] отправляется Ну то есть может ли он
[00:48:44] обработать этот запрос Ну и в принципе
[00:48:45] база на железе То есть она получается
[00:48:47] хранится физически
[00:48:49] где-то Занимает место если база например
[00:48:52] большая Окей А облачные они где-то
[00:48:54] метафизические хранятся
[00:48:57] Ну ну нет они хранятся всё равно
[00:48:59] физически просто в
[00:49:02] Облаке Ну мы об этом не знаем хорошо Ну
[00:49:06] там есть некоторые оптимизации по-моему
[00:49:08] за счёт Гугла потому что это гугловский
[00:49:10] сервис при работе с
[00:49:13] бику Окей вот как пользователь может
[00:49:16] влиять на эти оптимизации Какие он может
[00:49:18] магические слова добавлять чтобы сильно
[00:49:21] сокращать чек затраты на это
[00:49:25] всё там очень классный в интерфейсе есть
[00:49:28] указатель Там сверху справа Если не
[00:49:30] ошибаюсь о том сколько данных нужно
[00:49:34] будет перелопатила
[00:49:37] в окошке Вот изучало как это тору то что
[00:49:43] ну это очень это Достаточно давно было
[00:49:45] когда я работала с кри но я понимаю в
[00:49:47] чём суть всего этого Про то
[00:49:49] что А ну при работе со всем этим платишь
[00:49:53] же За ресурсы если используешь меньше
[00:49:55] ресурсов соответственно че Постав
[00:49:58] меньше А вот знаешь термин как это
[00:50:02] называется в облачной
[00:50:07] среде Нет скорее всего не назову Ну
[00:50:11] что-нибудь
[00:50:12] типа какая-нибудь
[00:50:15] аара
[00:50:17] ой хорошая
[00:50:20] догадка Да
[00:50:22] ТМ поводу
[00:50:25] индексов если собрать всё что мы сейчас
[00:50:29] обсудили если перейти к лабазе то что
[00:50:32] там используется вместо индексов для тех
[00:50:35] же
[00:50:44] целей вместо индексов
[00:50:57] сейчас попробую
[00:51:02] подумать Ну может просто в
[00:51:07] принципе Согласно самой сути Опа Ну то
[00:51:10] что там уже хранится
[00:51:12] что-то более структурированная но пусть
[00:51:15] будет термин агрегированная
[00:51:19] Ну там много данных может
[00:51:23] храниться прям очень много и невыгодно
[00:51:27] каждый раз с ними работать со всеми если
[00:51:30] нам нужно только может юшки какие-то
[00:51:32] есть а хорошо что я здесь хотел услышать
[00:51:36] это партицирование ну или там
[00:51:38] секционирование партиционирование кто
[00:51:40] как
[00:51:42] называет если собирают какой-нибудь
[00:51:44] отчёт за месяц если данные хранятся
[00:51:46] партиции за месяц то Это намного быстрее
[00:51:50] работает чем читать всю эту таблицу за
[00:51:53] там несколько лет
[00:51:59] О'кей А если говорить про какие-то Лав
[00:52:03] системы Подскажи
[00:52:07] м слышал ли что-нибудь про гнп Если да
[00:52:11] то
[00:52:13] что ну слышала но сама по себе не
[00:52:16] работала Ну что
[00:52:22] слышала Ну в принципе
[00:52:28] что
[00:52:39] тут Ну читала то что в принципе тоже
[00:52:42] хорошо подходит если используется
[00:52:44] довольно большой объём данных для
[00:52:47] хранения и
[00:52:48] обработки А есть верхни предел
[00:52:51] какой-то ещё раз Ну там не знаю 100
[00:52:54] петабайт можно хранить
[00:52:59] не смогу ответить потому что я не
[00:53:01] сталкивалась сама не проверяла и такой
[00:53:03] информации не находила
[00:53:07] Угу Да
[00:53:14] продолжай Ну вроде как читала что там
[00:53:17] есть э какой-то улучшенный анализатор
[00:53:22] запросов Ну
[00:53:24] допустим хорошо
[00:53:30] и всё это поверх постгрес номер там
[00:53:34] 9.4 когда актуальный пог
[00:53:37] 16 поэтому насколько он там на состоянии
[00:53:41] 2024 года улучшены Это такой большой
[00:53:44] вопрос но когда-то да когда-то они с
[00:53:47] этой стороны себя
[00:53:49] рекламировали Угу
[00:53:51] а
[00:53:53] О'кей А вот
[00:54:06] Давай может быть ещё про Спарк Немного
[00:54:08] поговорим напоследок
[00:54:10] А
[00:54:14] расскажи что делало когда не хватало
[00:54:16] памяти Ну там были какие-то
[00:54:20] спилы как это
[00:54:24] решал Ну как я уже раньше говорила то
[00:54:27] что увеличивали количество памяти
[00:54:29] которую отдавали экзектор в
[00:54:34] принципе ну один из вариантов но кажется
[00:54:38] что его довольно дорого применять
[00:54:40] абсолютно в каждом случае
[00:54:48] да вот В каких
[00:54:51] случаях может не хватать памяти То есть
[00:54:53] почему там в одной зада подо гиба эте а
[00:54:58] для другой хватит
[00:55:02] двух Ну зависит от самой задачи что в
[00:55:06] него входит Ну из чего состоит задача
[00:55:09] тогда да Из чего состоит задача Ну и
[00:55:13] какие операции используются вообще в
[00:55:16] принципе как бы раздели То есть если там
[00:55:26] группировку Ну вот Даже те же
[00:55:34] джоны мы можем например Ну вот избежание
[00:55:38] Если уж я заговорила
[00:55:39] про позиционирование то А ну например
[00:55:45] если увеличить количество партиции Угу
[00:55:49] то в принципе это может помочь Угу
[00:55:56] ли ты когда-нибудь Part by в таких
[00:55:59] задачах
[00:56:01] А да по-моему
[00:56:03] использовала Ну точно когда-то
[00:56:06] использовала Ой а помнишь как выбирала
[00:56:08] ключ для вот этого
[00:56:13] распределения Ну смотрела на данные сами
[00:56:17] по себе что они из себя представляют
[00:56:18] если это Например какая-то таблица где
[00:56:21] есть даты скажем то можно выбрать в
[00:56:23] принципе дату чтобы разбивать по дням
[00:56:25] Угу
[00:56:39] а смотрела ли На физическом уровне на
[00:56:43] уровне взаимодействия с файлами Как
[00:56:44] работает СРК когда ему нужно например
[00:56:46] поджо неть две
[00:56:48] таблички имеешь в виду вот эти имеете в
[00:56:51] виду физические джоны а которые хэш и N
[00:56:56] можно и про них тогда есть Большая
[00:56:58] таблица есть маленькая здесь скорее про
[00:57:01] вот есть какой-то кусочек данных не знаю
[00:57:04] там
[00:57:05] про города и он как-то там разложен
[00:57:09] распределён по разным ном есть какой-то
[00:57:11] там не знаю объект про продажи и вот
[00:57:16] нужно как-то посчитать сколько продаж
[00:57:18] было в каждом городе и вынести какую-то
[00:57:21] иото та
[00:57:26] маленькая то я насколько понимаю она
[00:57:28] целиком копируется по ном Ну потому что
[00:57:30] она маленькая и в принципе это можно
[00:57:31] себе позволить а та которая большая та
[00:57:34] как она разделена кусками она так и
[00:57:36] остаётся кусками а маленькая копируется
[00:57:38] каждому куску большой и они уже
[00:57:41] непосредственно Джой хорошо А если у нас
[00:57:44] две большие таблицы
[00:57:46] а а если у нас две большие таблицы
[00:57:52] то Сейчас постараюсь помнить
[00:57:59] ну их тоже нужно будет разделять на
[00:58:01] части как минимум Они и так остаются
[00:58:03] разделённые
[00:58:08] Аа И вероятно эти
[00:58:12] части как-то двигать по нодом скорее
[00:58:15] всего одной какой-то таблицы перемещать
[00:58:18] согласен А как понять какую условную
[00:58:21] строчку на какую ноду нужно закинуть
[00:58:24] Какое здесь условие
[00:58:37] м вот есть шал вот эта операция которая
[00:58:41] как раз выполняет это перераспределение
[00:58:43] данных по нодом А как она решает Какую
[00:58:46] строчку куда отправлять какие там есть
[00:58:48] стратегии
[00:58:58] Ну скорее всего если их несколько то
[00:59:01] есть какая-нибудь случайная стратегия
[00:59:03] Наверняка
[00:59:04] есть
[00:59:11] такая может быть можно как-то хаширова
[00:59:15] за счёт того что они большие Наверное
[00:59:17] это было бы удобно что-то в памяти
[00:59:19] сохранять и хаширова объекты
[00:59:23] перемещать так именно перемещать ные
[00:59:26] обекты А как из них потом доставать
[00:59:28] оригинальные
[00:59:30] данные Ну за счёт того что они хаширова
[00:59:33] у них видимо есть
[00:59:35] ключ можно вот по этому ключу например
[00:59:38] отсортировать Угу И потом вот уже по
[00:59:42] отсортированных ключам их разбить Ну
[00:59:45] пример на равные части между нодами и ну
[00:59:48] в равных пропорциях их
[00:59:50] разделять потом
[00:59:53] перемещать Ну хорошая догадка и до этого
[00:59:56] ещё был broadcast когда данные
[00:59:58] копируются целиком на все ноды без
[01:00:01] распределения
[01:00:04] хорошо
[01:00:06] принимается похожу там есть Чуть более
[01:00:10] короткий подход на тот который ты описал
[01:00:12] думаю тоже будет
[01:00:13] работать идея в целом
[01:00:17] понятна хорошо Я думаю что я выяснил что
[01:00:20] хотел Может быть есть какой-то вопрос Ну
[01:00:24] скажем ко мне я к сожалению далеко не на
[01:00:27] сеча смогу
[01:00:30] ответить Ну компания осталась очень
[01:00:33] Туманной Потому что так и не поняла чем
[01:00:36] конкретно занимается да компания какие у
[01:00:38] неё технологии но видимо раз это большая
[01:00:41] коммерческая тайна то наверное особого
[01:00:43] смысла про это спрашивать нет А ещё Ну
[01:00:47] всегда интересует вопрос команды Сколько
[01:00:49] человек в неё входит Каде у них
[01:00:51] позиции от 10 до 20 в основном
[01:00:54] сеньоры от 10 до ДТИ довольно большие
[01:00:57] команды на самом деле
[01:01:03] Угу Ну и как человека который поработал
[01:01:07] и в продуктовом и в коммерческом
[01:01:08] направлении меня всегда интересует
[01:01:09] вопрос это коммерческая разработка или
[01:01:11] продуктовую А как ты разделяешь для себя
[01:01:14] эти понятия Ну для меня коммерческий
[01:01:17] проект он чаще всего он может быть
[01:01:19] долгосрочный Но рано или поздно он
[01:01:21] скорее всего закончится и ну будешь
[01:01:24] искать себе новый проект а продуктовое
[01:01:26] это как своё для компании что-то и
[01:01:29] скорее всего Оно ориентировано на очень
[01:01:32] долгосрочное развитие я понял
[01:01:36] продукт Да мне очень нравится работать
[01:01:40] на продукте на самом
[01:01:42] деле Ну это были в принципе все основные
[01:01:46] вопросы Хорошо тогда с мой стороны тоже
[01:01:50] всё большое спасибо за уделённое
[01:01:52] время колле верну с обратной связ те
[01:01:56] дней и тогда Хорошего вечера
[01:01:59] пятницу Спасибо
[01:02:02] [музыка]

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
Write JSON only to: splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.json, v2, ... except the target path above).
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
INTERVIEW_LANGUAGE: ru (обязательно для этого прогона)
- Все поля text в JSON — дословные фрагменты из PRIMARY_TRANSCRIPT на русском. Без перевода на английский.
- Запрещены пересказы («кандидат рассказал о…», «The candidate…»).
- Метки question_type / question_topic / interview_stage — enum на английском (схема), тексты Q&A — только русский ASR.


======================================================================
OUTPUT PATHS (post-processing)
======================================================================
Save JSON to: splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.json \
    --video transcripts/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02//video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.json --out splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.qa-split.json \
    --video transcripts/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02//video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.validation-report.md

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
video.md: transcripts/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/video.md

--- CHAPTER `00:01:10` — Про опыт ---
window: 00:01:10 .. 00:05:31
recognition_status: single (1 items)

ITEM #2
  interviewer_question: time=00:05:29 text='Расскажи побольше про хранилище какая там была модель как раскладывали данные Почему именно эта'
  candidate_answer: time=00:05:36 text='модель А ну хранилище у нас на у нас было несколько слоёв у нас был сурой слой и СН слой Ну особо как бы особого многообразия слоёв не было А по поводу разложения данных зависело ну в основном от типов задач и от необходимости пользователя то есть насколько они там между собой связаны в основном все задачи которые А ну точнее все данные которые получались посредством м выполнение экстрактов тасо они у нас все лежали в сыром слое если происходили какие-то дальнейшей трансформации то соответственно они уже переезжали дальше'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:06:19 text='Угу То есть были витрины которые строились в том числе на сыром слое да'
  question_topic: Data Modeling

--- CHAPTER `00:05:31` — Про хранилище, слои ---
window: 00:05:31 .. 00:08:35
recognition_status: multiple (3 items)

ITEM #3
  interviewer_question: time=00:06:24 text='да именно так а вот как понимаешь какие есть плюсы минусы Почему иногда стоит выбирать такой это может быть Почему именно у вас так'
  candidate_answer: time=00:06:33 text='выбрали Ну сырой слой как минимум позволяет хранить некоторую историчность данных ну то есть оставлять их такими какие они есть до преобразования Потому что если изначально встроены а какие-то преобразования и мы забираем данные Ну то есть пользователь видит данные которые он в итоге получает не S как они хранятся в источнике с некоторыми преобразованиями Возможно есть вероятность что вот эти преобразования могут вносить а ну не шум А скажем так есть вероятность что человек который Их делал мог накосячить как минимум вот а то есть если происходит какая-то ошибка как минимум это позволяет сразу пойти на сырой слой и посмотреть а если там в порядке значит ошибка пошла уже после об'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:07:17 text="прощение дебаггинг О'кей Да Да А так м"
  question_topic: Data Modeling

ITEM #4
  interviewer_question: time=00:07:44 text='табличек было на скидку на ром слое каких-то отдельных объектов'
  candidate_answer: time=00:07:50 text='Ну несколько тысяч Впечатляет они скажем так несколько тысяч ну потому что ну местами они друг друга дублировали скажем с разными названиями и тому подобные вещи местами это какие-то тестовые таблицы именно вот которые прямо использовались использовались ну скажем уже порядок по порядок будет поменьше около'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:08:18 text="сотни О'кей то я уже испугался Как вы в"
  question_topic: Data Modeling

ITEM #5
  interviewer_question: time=00:08:22 text='тысячи объектов как-то разбирались с учётом того что там часть друг друга дублировали и здесь как раз'
  candidate_answer: time=00:08:29 text='Мне кажется мог бы помочь ещё какой-то слой ладно окей да возможно вот как бы'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:08:31 text='слой ладно окей да возможно вот как бы'
  question_topic: Data Modeling

--- CHAPTER `00:08:35` — Microbatch vs Streaming ---
window: 00:08:35 .. 00:09:35
recognition_status: single (1 items)

ITEM #6
  interviewer_question: time=00:08:49 text='или иначе это нетай микро пач кажется где-то очень рядом Да микроба где-то рядом но тут зависит от того сколько'
  candidate_answer: time=00:09:01 text='Сколько может этот самый микроба процесс процеси в единицу времени Ну или какой у него отклик ожидания сколько секунд или миллисекунд если это допустим Ну вот как у нас было микроба использование Ну тут сразу стоит обозначить то что у нас впаке есть И если процеси каждую строку то ждёт когда соберётся объём для определённого Бача и он скажем Ну может не сразу собраться это уже точно и стриминг это уже точно отсылка к микро'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:09:34 text='бачу Окей А витрины получается были'
  question_topic: Data Modeling

--- CHAPTER `00:09:35` — Презентационный слой, DA, DS ---
window: 00:09:35 .. 00:10:35
recognition_status: multiple (2 items)

ITEM #7
  interviewer_question: time=00:09:36 text='также на С3 вот как выглядел презентационный слой с чем работали аналитики там дата сатанисты и подобные'
  candidate_answer: time=00:09:44 text='люди Ну у нас таких не было с ними не ну Дато саентистом не было были аналитики аналитики работали уже с конечными таблицами приведёнными к определённому виду Ну видимо не с историческими данными более агрегированные просто через deb селек или или был какой-то Bi Инструмент там какой-то другой доступ Ну у B дела был Bi инструмент Power Bi но я не работала с Bi инструментами конкретно я но вообще у нас в принципе есть развёрнутый суперсет но мы от него немножко ушли Потому что развернули рядом терла и в основном было удобнее пользоваться'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:10:22 text='им Да чувствуется что есть определённый уровень подготовки у спецов что готов работать через jl клёво'
  question_topic: Data Modeling

ITEM #8
  interviewer_question: time=00:10:31 text='А так вот расскажи С какими трудностями сталкивалась когда обрабатывала стриминг именно трансформ на'
  candidate_answer: time=00:10:42 text='кафке Ну а а стриминг для Кафки Угу Ну как минимум базово просто прочитать через Space Park не получится приходилось Кать а там же у нас есть K value изначально приходит и вот узна пото что там внутри может ни напри дновский обе его нужно распарсить Скажем на несколько колонок сходу Вот это могу вспомнить а так ну есть ещё такой момент то что для того что нужно определённым образом конфигурировать саму кафку и топик при его создании чтобы к нему в принципе можно было подключиться и читать я конкретную опцию не назову но вот такой момент тоже был пом наверное всё что сходу могу'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:11:36 text='вспомнить Окей А с какими-нибудь'
  question_topic: Data Modeling

--- CHAPTER `00:10:35` — Трансформ на Kafka ---
window: 00:10:35 .. 00:12:22
recognition_status: multiple (2 items)

ITEM #9
  interviewer_question: time=00:11:40 text='джоми на лету не сталкивалась Может быть какие-то как раз хотела рассказать но я с ними сталкивалась не с какой вот уже'
  candidate_answer: time=00:11:44 text='какие-то как раз хотела рассказать но я с ними сталкивалась не с какой вот уже конкретно когда мы делали преобразование ну после экстракта Ну как минимум Джона первое с чем я столкнулась что если мы используем Джони уже не полу поэтому мы ушли к потому что через в принципе дж отрабатывают и на этом пока я остановились на такой'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:12:10 text='реализации А вот может быть знала там'
  question_topic: Data Modeling

ITEM #10
  interviewer_question: time=00:12:14 text='смотрела как-то в других компаниях Как делают в других командах Можно ли всё-таки как-то стримить Точнее можно ли как-то дживы стриминговые данные какие-то может быть есть вариант реализации какие есть особенности'
  candidate_answer: time=00:12:31 text='сходу не вспомню смотрела именно для пайс парка и вот таким образом и нашла фары ба когда изначально столкнулись с этой проблемой и ранее На нём было принято решение'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:12:47 text='временно приостановиться Окей В каком'
  question_topic: Data Modeling

--- CHAPTER `00:12:22` — Джойны стриминговых данных ---
window: 00:12:22 .. 00:12:50
recognition_status: not_recognized (0 items)

(no items extracted)
--- CHAPTER `00:12:50` — Формат хранения на S3, почему ---
window: 00:12:50 .. 00:13:14
recognition_status: multiple (3 items)

ITEM #11
  interviewer_question: time=00:12:50 text='формате хранили на'
  candidate_answer: time=00:12:54 text='S3 в паркете у'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:12:59 text='Почему в'
  question_topic: Data Modeling

ITEM #12
  interviewer_question: time=00:12:59 text='Почему в'
  candidate_answer: time=00:13:03 text='нём не могу ответить на этот вопрос не принимала такое'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Data Modeling

ITEM #13
  interviewer_question: time=00:13:13 text='А какие может быть есть альтернатива бы там читала интересовалась пошло ли дальше развитие в каких-то форматах'
  candidate_answer: time=00:13:25 text='хранения по поводу в плане паркета хранить Ну CSV кто-то хранит но мне кажется эта идея ещё хуже чем паркет А ну может знаю но сходу наверное не вспомню вот с дельтой айсбергом худи не'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:13:58 text='сталкивалась да Вообще мы работаем с айсбергом То'
  question_topic: Data Modeling

--- CHAPTER `00:13:14` — Альтернативы паркету ---
window: 00:13:14 .. 00:14:13
recognition_status: single (1 items)

ITEM #14
  interviewer_question: time=00:14:11 text='А какие плюшки использовать в айсберге какие функции'
  candidate_answer: time=00:14:18 text='А сейчас помню вообще я наверное сходу больше назову проблему чем плюшку Потому что с проблемой я столкнулась тоже раньше в общем сейчас Есть такая тема то что у спарка и у айсберга различаются некоторые типы данных Угу например айдини по-моему листы то есть местами у них нейминг просто разный А есть такие типы которые например в спарке есть в айсберге их нет Или наоборот в айсберге они есть в спарке их нет такая была последняя проблема а Ну ещё если используешь Айсберг и Ну обязательно нужно дописывать при создании таблицы US АБЕ как минимум Но это просто не проблема Это такая особенность Ну из плюсов наверное может быть версионность то что отслеживаются изменения в таблице Ну вот это Тае основно я могу так'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:15:30 text='вспомнить остальные Так я с чтобы время не тянуть Да хорошо А подскажи'
  question_topic: Data Modeling

--- CHAPTER `00:14:13` — Что используете в Iceberg ---
window: 00:14:13 .. 00:17:15
recognition_status: single (1 items)

ITEM #15
  interviewer_question: time=00:15:40 text='вот так получается АБЕ на3 А в качестве какого-то'
  candidate_answer: time=00:15:59 text='Ну да у него же есть айсбергов ский местор Да он есть как раз айсбергов Да Окей там тоже была такая проблема то что мы обновляли в один момент Айсберг и по-моему получилось так то что мы Обновили сам Айсберг а местор не Обновили То есть он остался старый но сами таблицы физические у нас ушли в одну из баз А и они Короче не просто ушли А там же есть несколько каталогов там есть СР каталог и есть обычный каталог дефолтный какой-то и общем они как бы физически у нас ушли но они остались жить в определённом каталоге если просто делаешь Show T и там определённое датабаза то он не показывает этой таблицы но когда пытаешься её удалить он её не удаляет Потому что говорит что в стори она не прописана то есть мы просто обновляли а просто обновили както Да Дада всё подсоса что нужно и всё'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:17:08 text='заработало так Окей вообще конечно интересный проект столько разных технологий Подскажи'
  question_topic: Data Modeling

--- CHAPTER `00:17:15` — Масштабирование Kafka ---
window: 00:17:15 .. 00:18:15
recognition_status: multiple (2 items)

ITEM #16
  interviewer_question: time=00:17:18 text='Зай есть ли какой-то опыт по масштабированию Есть ли понимание Как можно вот подготовить какие-то джипы там какие-то топить к тому чтобы через этото лилось там не знаю в 10 раз больше сообщений чем сегодня в 1.000 раз больше нет'
  candidate_answer: time=00:17:35 text='масштабированием я не занималась а не читал ничего м именно про масштабирование самих данных или ресурсов Я знаю про вертикальное горизонтальное масштабирование но здесь скорее какие есть абстракции в кафке которые могут помочь Нет точно например несколько коров подключать к одному топику Нет точно не отвечу'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:18:06 text='у Окей'
  question_topic: Data Modeling

ITEM #17
  interviewer_question: time=00:18:14 text='Так расскажи Зачем нужно было писать кастомные операторы на airflow ни же уже написаны'
  candidate_answer: time=00:18:23 text='тысячи Ну у нас была такая конкретная необходимость за счёт изза входного формата данных и в принципе у нас была разработана Ну как реализован свой отдельный пакет а для того чтобы корректно парсить конфиг приходящий То есть у нас airflow был настроен на Дис в дис прилетали определённые конфиги их нужно было распарсить нашей кастомной библиотекой ещё их внутри рекурсивно шаблони Зро то есть некоторые а фильтры airflow они были Ну примерно на третьем слое хранящегося в редисе Угу нужно было их вот рекурсивно нить это вот как раз про генерацию да'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:19:08 text='да Зачем так'
  question_topic: Data Modeling

--- CHAPTER `00:18:15` — Кастомные операторы Airflow ---
window: 00:18:15 .. 00:19:39
recognition_status: multiple (2 items)

ITEM #18
  interviewer_question: time=00:19:08 text='да Зачем так сложно тава была'
  candidate_answer: time=00:19:14 text='необходимость так исторически сложили да да так исторически сложилось'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:19:22 text='Ясно ну просто есть кажется какие-то варианты с там тем что парт Я файлы подают вход Ну он был не совсем прямо кастомный то есть это был Наследник спар кубернетес оператора просто немножечко'
  question_topic: Data Modeling

ITEM #19
  interviewer_question: time=00:19:35 text='долинный угу вот как работало с airflow в губере Как там логи читала как подключалась были ли какие-то трудности или это всё вот как-то настроили Оно'
  candidate_answer: time=00:19:47 text='просто работало Ну базовый ответ настроили Оно просто работало не базовые иногда возникали некоторые проблемы с адресацией то есть внешний внутренний адрес Например Раз везде полу внутре ГТО стами забыли что-то прокиды Он оставался внутренним А так в принципе всё было настроено бы заведены коне определённые на чере ну и соответственно кубовский конф тоже туда прокиды поэтому Они между собой хорошо общались соответственно для airflow был отдельный mes Space там для бэнда отдельный mes Space и просто в name Space airflow все логи очень хорошо доходили все читались Угу Ну вот как физически это выглядело что это просто подтягивались в юай и там можно было это всё читать или надо было как-то в по для пользователей для пользователей Да потя делалась юай то есть всё стандартно заходишь в Дак там есть определённые таски жмёшь на таку и читаешь логи а для разработчика ну Смотря как если ты локально разрабатывает то Ну в дебаг режиме запускаешь смотришь что кого не так пошло А если ты хочешь посмотреть что-то что на прозе было то опять же заходишь в контейнер читаешь логи смотришь что конкретно уехала airflow у нас как работал он общался с парком который был в кубернетес и соответственно на каждую задачу делал сабмит оператор и самил саму таку в отдельный Space с парковский а И следующий следующая итерация в тас была уже мониторинг под мониторингом я понимаю непосредственно исполнение самой джаббы'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:21:38 text="Угу О'кей А как эта вся система общалась"
  question_topic: Data Modeling

--- CHAPTER `00:19:39` — Работа с Airflow в k8s ---
window: 00:19:39 .. 00:25:02
recognition_status: multiple (3 items)

ITEM #20
  interviewer_question: time=00:21:42 text='с какими-то внешними источниками Ну вот есть там I например или может быть э м было ли такое что какую-то часть интерфейса прокиды наружу из кубера нет такого то есть мы можем без проблем подключаться к каким-то внешним источникам если Ну это скажем источник данных какой-то внешний Да это всё корректно работало необходимости интегрироваться Ну не в качестве источника данных а так с каким-то внешним Ну вроде как не возникало или если возникало то это было до меня и я скажем не наслышана а не смотрела Как именно это было реализовано то есть А что именно что со стороны кубера и как нужно настроить чтобы он начал общаться с внешним миром и был скажем увидел какой-то внешний'
  candidate_answer: time=00:21:59 text='нет такого то есть мы можем без проблем подключаться к каким-то внешним источникам если Ну это скажем источник данных какой-то внешний Да это всё корректно работало необходимости интегрироваться Ну не в качестве источника данных а так с каким-то внешним Ну вроде как не возникало или если возникало то это было до меня и я скажем не наслышана а не смотрела Как именно это было реализовано то есть А что именно что со стороны кубера и как нужно настроить чтобы он начал общаться с внешним миром и был скажем увидел какой-то внешний сервис нет нет в эту сторону не'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:22:49 text='смотрела так Окей Было'
  question_topic: Data Modeling

ITEM #21
  interviewer_question: time=00:22:53 text='ли так получается что сами таски запускались в каких-то отдельных подах вот этом кубернетес под'
  candidate_answer: time=00:23:02 text='оператор бы раз в каких-то соседних подах то есть всё всё в кубе было А да всё было в кубе то есть на каждую спарко вскую ДБУ у нас имелся свой собственный пот драйвер Фло на каждую отдельную таку мы получается на каждый Дак тоже свой отдельный под уже в другом на спейсе эском поэтому оно всё очень хорошо между собой разделяло Угу и отслеживал есть Ну вот например с точки зрения разработки и попытки понять где была ошибка всё так как живёт в раздельных найм спейсах это всё не путается между собой и довольно просто найти по соответствию Что именно пошло не'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:23:46 text='так угу А вот здесь Расскажешь'
  question_topic: Data Modeling

ITEM #22
  interviewer_question: time=00:23:49 text='чего-нибудь про м скейлинг то есть было ли такое что для какой-то таски нужно было больше выделять ресурсов чем другим как управляли вот этой приоритизации тем кому сколько ресурсов'
  candidate_answer: time=00:24:05 text='раздавать Да были некоторые задачи была Басовская база с довольно большой таблицей которую Ну которую который нужно было подключить через экстрактор Ну её просто прочитать и вторая задача была интервально прочитать и вот когда была фува её перегрузка просто в хранилище как она есть там Возникала проблема и увеличивали ресурсы Как раз за счёт увеличения ресурсов проблема ушла как а в конфиге с парковской прописывали а больше памяти выделяли на экю и получается Если там вот лову загрузку нужно сделать один раз то добавляли памяти потом переходила на инкремент и убирали память Угу'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:25:00 text='Окей А вот Расскажи про инкрементальные'
  question_topic: Data Modeling

--- CHAPTER `00:25:02` — Инкрементальные загрузки в S3 ---
window: 00:25:02 .. 00:27:16
recognition_status: multiple (2 items)

ITEM #23
  interviewer_question: time=00:25:03 text='загрузки как это всё работало с S3 там вроде бы не очень хорошо работает с дописывая в какой-то файлик'
  candidate_answer: time=00:25:11 text='А ну с инкремента загрузкой Да у нас был такой тип реализован то есть получается он работал Так что А ну загружаешь какой-то источник данных хочешь его прочитать инкремента и если в мере нет указания для этой таблицы то что ранее она перегружать инкремента то ставишь Ну пользователь как с этим работал со стороны пользователь наверно объясню будет немножко попроще пользователь выбирает какую-то колонку если это реляционная база в которой например содержится АШК Ну предусмотрено то что это айдини если в место нет информации по этой таблице что она ранее инкремента перегружать то она перегружается целиком то есть самого первого шника до такого который она есть допустим это всё устроено как Да который у нас запускается у на завра и скажем в эту таблиц кто-то е дописал данные наступает следующий день у нас снова запускается э таска и видно то что появились следующие Аники после того максимального который прописан берём строки именно вот по этим очникам и их через описываем к уже существующей таблице капот делами занимался Айсберг и всё просто работал ну почему вот э логику с с тем чтобы Сходи в местор Посмотри какой там айдини прописан это это не Айсберг это приходилось Ну разрабатывать просто интересно как это на уровне файлов работало Ну файл оставался тем же самым Просто он больше по объёму становился за счёт того что туда что-то Вась именно вот с точки зрения файла с точки зрения если ну его как таблицу читать потому что они в формате обычных таблиц сохранялись то Ну это просто таблица в которые добавлялись добавлялась строк или не добавлялась если изменений не было'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:27:12 text='или не добавлялась если изменений не было'
  question_topic: Data Modeling

ITEM #24
  interviewer_question: time=00:27:15 text='Расскажи про партицирование Было ли в системе как с этим работали'
  candidate_answer: time=00:27:21 text='а да Было такое Было изначально Так что У пользователя есть возможность самостоятельно выбрать колонки порционирования и скажем задать если пользователь этого не задаёт то в процессе уже выполнения скобы анализировала что туда пришло брался определённый лимит то есть первые 100 строк из таблицы если она большая по этим строкам определялся сейчас вос произведу определялась нет не так не так было Это было позже'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:28:00 text='типы которые туда приходят там и строковые и если был скажем какой-то или тип ID его выбирали как илита это всё прямо совсем автоматически работало Ну это было реализовано уже в самом то есть мы это сами реализовывали Ну это я понял да просто это кажется довольно важное решение с точки зрения дальнейшей работы с таблицей каким-то объектом с тем как это всё будет дальше жить как это будет вариться и получается это всё по автоматике было при том что у вас было там Примерно 100 родовых объектов Вот'
  question_topic: Data Modeling

--- CHAPTER `00:27:16` — Партицирование ---
window: 00:27:16 .. 00:29:20
recognition_status: single (1 items)

ITEM #25
  interviewer_question: time=00:28:40 text='расскажи Почему решили настолько глубоко это всё'
  candidate_answer: time=00:28:45 text="автоматизировать ну потому что изначально подразумевалось что этим будут пользоваться люди которые не сильно в это погружены и скажем так им по специфике их работы ну то есть они не должны про это знать изначально подразумевал что этим будут пользоваться люди у которых нет нет таких базы знаний просто потому что её не должно у них быть и если мы можем там автоматически предложить им какое-то более-менее оптимальное решение за них то это будет хорошо потому что всё-таки это людям поможет за счёт того что это будет немножечко быстрее О'кей я"
  reference_answer: time=None text=None
  interviewer_feedback: time=00:29:19 text='понял расскажи какие есть плюсы и минусы'
  question_topic: Data Modeling

--- CHAPTER `00:29:20` — Self serivce аналитика ---
window: 00:29:20 .. 00:31:07
recognition_status: multiple (2 items)

ITEM #26
  interviewer_question: time=00:29:22 text='У того чтобы пользователям отдавать права вот принимать решения в таких моментах допустим мы разрабатываем какой-то интерфейс какой-то инструмент который может сконфигурировать новый поток загрузку из какого-то нового источника он сформирует табличку табличку можно будет подцепить к витринам и потом над этих над этими витринами там строить какие-нибудь графики какую-то аналитику Вот какие есть плюсы минусы таких подходов плюсы с точки зрения вот допустим предоставлять пользователю право выбирать там колонки партиционирование и количество партиции'
  candidate_answer: time=00:29:50 text='точки зрения вот допустим предоставлять пользователю право выбирать там колонки партиционирование и количество партиции то что ну не очень хорошо звучит Но это становится ответственностью пользователя если он выбрал что-то не оптимальное то есть ну как бы ты сам это выбрал это становится твоей ответственностью минус банальный в том что это может быть выбрано не оптимально и это будет очень неплохо так жрать ресурсы когда могло бы жрать не так сильно А как минимум Вот это также Ну из плюсов можно сказать то что а скорее всего м так как пользователь самостоятельно завозит себе соединение в системе Ну то есть на какой-то источник с которым он знаком он более погружён и в контексте предметную область самого этого источника То есть у него знаний о НМ Побольше чем если я скажем приду и пытаться там за час что-то горящее решить то есть пользователь больше в контексте И за счёт его контекста если он там ну скажем представим что он там интересуется этим что он посмотрел всё-таки Что такое партиционирование когда всё это увидел есть вероятно что примет правильно рение именно вот конкретно ему под его задачу Угу А'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:31:02 text='вот Окей'
  question_topic: Data Modeling

ITEM #27
  interviewer_question: time=00:31:05 text='принимается Я сейчас так подумал а где в этой всей системе кури или он был на первом проекте а кури был на первом проекте который был не продуктовый'
  candidate_answer: time=00:31:10 text='первом проекте а кури был на первом проекте который был не продуктовый'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:31:18 text='Угу Так Окей как бы описала В чём'
  question_topic: Data Modeling

--- CHAPTER `00:31:07` — BigQuery ---
window: 00:31:07 .. 00:31:22
recognition_status: single (1 items)

ITEM #28
  interviewer_question: time=00:31:18 text='Угу Так Окей как бы описала В чём разница между какой и ра битом а'
  candidate_answer: time=00:31:29 text='Ну в рете очереди в кафке топике кавка больше подходит для стриминга чем Потому что ну просто кавка больше подходит для стриминга зря сказала сказала потому что вот ну как минимум потому что допустим если использовать какие-нибудь конек коннектора нет но можно данные которые хранятся в очереди реб бита через кавка коннектор перезаписать в кафку Угу и тогда уже их оттуда стриминговая не микроба это будет уже ну более приближённая прямо к самому настоящему стриминга Тогда вопрос зачем Т Ну у пользователь есть необходимость пользоваться изначально ртом скажем так как источником данных вот он хочет ребит Угу очень много власти у ваших пользователей было возможности влиять на это всё даже прямо завидую всё для них'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:32:37 text="них О'кей А вот э навеяно Этой темой"
  question_topic: Data Modeling

--- CHAPTER `00:31:22` — Kafka vs RabbitMQ ---
window: 00:31:22 .. 00:32:48
recognition_status: single (1 items)

ITEM #29
  interviewer_question: time=00:32:45 text='Расскажи про доставку сообщений в распределённых системах Какие могут быть трудности может быть какие есть три основных подхода к тому как это можно'
  candidate_answer: time=00:33:00 text='могу нено вот этих ключевых слов если будет надо ага Да это наверное пригодится потому что я этим особо почти не занималась но скорее всего трудность может быть в том что а сообщение или часть сообщений может потеряться в какой-то момент из какой-то очереди и во-первых первый пункт Это плохо что они в принципе потерялись второй пункт нужно понять В какой момент Они потерялись какого Ну то есть именно вот интервал потери чтобы ну его определить и понять масштаб вообще в принципе А так а третье'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:33:44 text='А ну так встретим пока Притормози Ну вот'
  question_topic: Data Modeling

--- CHAPTER `00:32:48` — Доставка сообщений в распределённых системах ---
window: 00:32:48 .. 00:36:41
recognition_status: multiple (5 items)

ITEM #30
  interviewer_question: time=00:34:30 text='согласен Вот есть доставка как минимум один раз как максимум один раз и точно один'
  candidate_answer: time=None text=None
  reference_answer: time=00:34:30 text='согласен Вот есть доставка как минимум один раз как максимум один раз и точно один'
  interviewer_feedback: time=None text=None
  question_topic: Data Modeling

ITEM #31
  interviewer_question: time=00:34:39 text='раз Слышала про них А да да слышала Вот какая например в кафке или там какая была ва у вас в системе'
  candidate_answer: time=00:34:51 text='и как думаешь что могло повлиять на так exactly и at least правильно'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:35:09 text='Да какая у нас была я не'
  question_topic: Data Modeling

ITEM #32
  interviewer_question: time=00:35:09 text='Да какая у нас была я не скажу Ну по-моему наиболее востребованный из этих трёх - это а at least Если не ошибаюсь'
  candidate_answer: time=00:35:12 text='скажу Ну по-моему наиболее востребованный из этих трёх - это а at least Если не ошибаюсь ой если простыми словами это значит что у нас могут данные задули и это нормально мы как-то с этим работаем значит что мы можем иногда терять данные Но если Они доходят Тони доходят максимум один раз И когда мы гарантируем что мы ничего не теряем и ничего не дублируем Ну третий вариант звучит слишком идеального дублируются но они дойдут А как работать с дубликате это скажем так другой вопрос но он вероятно решаемый То есть это порождает новую проблему но решает проблему с с потерей данных Да как многие какие-то решени в инженерном мире хорошо а'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:36:13 text='какие-то решени в инженерном мире хорошо а'
  question_topic: Data Modeling

ITEM #33
  interviewer_question: time=00:36:19 text='вот как можно из at least получить EX'
  candidate_answer: time=00:36:28 text='Ну брать дупликации Угу'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:36:33 text='хорошо'
  question_topic: Data Modeling

ITEM #34
  interviewer_question: time=00:36:39 text='так вот как бы Ты оценила Чем отличается постгрес и'
  candidate_answer: time=00:36:46 text='mssql Ну они обе реляционные базы банально Не множе синтаксисом даже в самых простых запросах скажем при работе с датами есть там некоторые нюансы А ну в msq есть инстансы в постгрес их'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:37:10 text='нет А что такое инс'
  question_topic: Data Modeling

--- CHAPTER `00:36:41` — PostgreSQL vs MSSQL ---
window: 00:36:41 .. 00:38:39
recognition_status: multiple (3 items)

ITEM #35
  interviewer_question: time=00:37:10 text='нет А что такое инс'
  candidate_answer: time=00:37:13 text='в Ну банально если подключаешься не знаю через какой-нибудь вивер или dat grip то для MS обязательно нужно указывать instance для поса достаточно именно базу прописать'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:37:29 text='Угу то есть в MS скиле может быть несколько баз данных рядом в постгрес такого не может быть Ну несколько инстан сов может быть может быть в MS сле Ну вот instance база данных схема таблица Типа такая вложенность Да да да А чем тогда отличается инс от какого-то конкретного сервера на котором развернут MS Skill Ну возможно что на instance могут быть разные права вообще и на базе могут быть разные права но видимо вот на таком же уровне то что У какого-то пользователя есть право там на все допустим истан А у другого только на инс X например'
  question_topic: Data Modeling

ITEM #36
  interviewer_question: time=00:38:18 text='ещё чего добавишь А больше ничего не'
  candidate_answer: time=00:38:21 text='А больше ничего не добавлю Окей'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:38:33 text='так вот давай немного предложу'
  question_topic: Data Modeling

ITEM #37
  interviewer_question: time=00:38:33 text='так вот давай немного предложу порассуждать если мы берём базу типа там того же поса то там большое такое внимание уделено индексам тому как их там правильно уза если мы берём какие-то Дато инженерные задачи Вот те же самые ула базы то там индексы вспоминают намного реже если в принципе вспоминают как бы ты проинтерпретировать'
  candidate_answer: time=00:39:10 text="объяснила почему индексы практически не востребованы в olab хранилищах и может быть что вместо них так Ну получается allp oltp - это у нас транзакционные ну transaction а больше аналитические Так ну sotp требуется более быстрый ответ как я понимаю ну вот допустим насколько я знаю то что в банках где-нибудь используется ltp Ну там например когда деньги переводишь транзакция должна быть либо полностью совершена либо полностью не совершена то есть она не может быть совершена частично скажем А ну поэтому как раз используются индексы индексы же предназначены в принципе для ускорения именно чтения чтение из базы Ну была кажется тоже было бы полезно побыстрее читать м было бы полезно но а ну из названия Если oltp транзакционный то алап - это аналитический Угу Ну если он аналитический Может есть необходимость их как-то а данные сами по себе ну ну нет наверное имела в виду то что в плане с разных сторон рассматривать и не делать привязку в таблице каким-то конкретным индексом потому что это более гибко скажем так потребность их смены может часто меняться О'кей идея понятна"
  reference_answer: time=None text=None
  interviewer_feedback: time=00:40:58 text='Есть ли'
  question_topic: Data Modeling

--- CHAPTER `00:38:39` — Индексы в OLAP, что вместо ---
window: 00:38:39 .. 00:47:35
recognition_status: multiple (8 items)

ITEM #38
  interviewer_question: time=00:41:02 text='ещё Ну может быть приоритеты у в принципе у таких типов хранилищ Ну в плане приоритеты как операции базовые чтение и запись Угу если в ltp'
  candidate_answer: time=00:41:08 text='принципе у таких типов хранилищ Ну в плане приоритеты как операции базовые чтение и запись Угу если в ltp преимущественно записывать что вот допустим пользователь там перевёл другому 100 руб да то в лапе наоборот нужно в основном в основном из них читаю чем туда пи чтение хорошо подходят индексы разве нет ну вообще да индексы как раз для чтения лучше чем для'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:41:35 text='записи Ну вот м давай немного поглубже'
  question_topic: Data Modeling

ITEM #39
  interviewer_question: time=00:41:39 text='берём какую-нибудь пагр берём вот какой-нибудь классический индекс кластерный как он выглядит ну скажем немного ближе к вот уровню файлов данных страниц чего-то такого Какая структура данных Ну индекс если он есть он же как раз Ну вот по страницам делит и ищет в каждой странице определённые совпадение на основе'
  candidate_answer: time=00:41:58 text='Ну индекс если он есть он же как раз Ну вот по страницам делит и ищет в каждой странице определённые совпадение на основе выстроено а делит Ну на основе того как сформирован как сформированный индекс Ну и какая у него там селективность с точки зрения запроса Ну хорошо А ну в постгрес'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:42:18 text='очень много индексов я думаю что ни я ни ты не хотим туда очень глубоко сейчас закапывать если брать там не знаю какое-то вот это вот дерево классическое V3 Ага'
  question_topic: Data Modeling

ITEM #40
  interviewer_question: time=00:42:32 text='То что у тебя на выходе когда ты отправляешь какой-то запрос вот индекс Верни мне там что-то вот это что-то Это что'
  candidate_answer: time=00:42:45 text='мм Ну какая-то запись в таблице если это реляционная база ну возвращается соответственно Ну вообще по факту возвращается тоже реляционная таблица просто ограниченная там забираем кокрок'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:43:01 text='и если мы берём какой-то типичный алап'
  question_topic: Data Modeling

ITEM #41
  interviewer_question: time=00:43:01 text='и если мы берём какой-то типичный алап запрос типа вот постройка мне отчёт за месяц то там сколько таких операций нужно сделать чтобы все нужные строки'
  candidate_answer: time=00:43:18 text='достать Ну больше чем Ну построить отчёт за месяц Ну как минимум нам сгруппировать нужно видимо по определённому месяцу Возможно есть определённая фильтрация Угу Ну и вы если мы применяем индексы то нам нужно получается каждую строчку вернуть то есть понять там допустим у нас вот есть этот месяц и пробежаться по индексу вот каждый раз возвращая по вот этой одной строчке А сейчас сможешь'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:43:51 text='прикинуть с точки зрения алгоритмической сложности'
  question_topic: Data Modeling

ITEM #42
  interviewer_question: time=00:43:51 text='прикинуть с точки зрения алгоритмической сложности сколько бы занимала такая операция для одной строки и в каких случаях оптимизатор может отказаться от использования индекса Даже даже если он есть и там пройти просто сверху вниз по всей'
  candidate_answer: time=00:44:12 text='таблице использования индекса может если таблица маленькая сама по себе то есть там ну она сама по себе небольшая первый случай ВТО случай может ин выре активность скажем если это какая-то таблица там с данными про людей а в качестве индекса например выбран пол мужской или женский А ну и Ну предположим предположим что там примерно поровну мужчин и женщин то использование индекса вообще смысла в данном случае особенно му не име не Ну почему сначала срезаем половину таблицы потом по остальной половине таблицы проходим сверху вниз кажется в два раза Быстрее Всё равно неплохо Ну вообще я проверяла как раз работала с подобной таблицей когда изучала индексы и делала индекс именно на пол и он был Ну примерно результат был примерно такой же как без индекса Угу это особо никакого привеса не принесло а не смотрела Там план запроса он вообще использовался А я смотрела через Алай и индекс как раз вообще ну не использовал Ну не использовался скорее'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:45:24 text='Угу Ну вот с точки'
  question_topic: Data Modeling

ITEM #43
  interviewer_question: time=00:45:28 text='зрения как-то сможешь сейчас прокомментировать или затрудняешься вот которы не услышала Последнее'
  candidate_answer: time=00:45:37 text='которы не услышала Последнее А если мы берём Ну там вот эти два случая когда мы вытаскиваем строку через индекс сколько это будет занимать в там каком-то среднем в предельном варианте Ну по вот это вот о от и в каком случае невыгодно будет идти этим путём и лучше просто просканировать всю таблицу сверху'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:46:09 text='вниз Ну я уже называла случаи когда использовать индекс может быть нелогично скажем с точки зрения математики вот там можно'
  question_topic: Data Modeling

ITEM #44
  interviewer_question: time=00:46:20 text='вывести Две таких зависимости и они будут пересекаться в какой-то точке и потом одна там продолжит расти А вторая будет примерно Вот вот так вот уходить Ну то есть одна будет экспоненциальная видимо плюс-минус'
  candidate_answer: time=00:46:09 text='вниз Ну я уже называла случаи когда использовать индекс может быть нелогично скажем с точки зрения математики вот там можно вывести Две таких зависимости и они будут пересекаться в какой-то точке и потом одна там продолжит расти А вторая будет примерно Вот вот так вот уходить Ну то есть одна будет экспоненциальная видимо плюс-минус а вторая Ну если продолжит расти то видимо Линейная А может ли быть там где-то логарифмическая Да может быть логарифмическая и квадратная может быть да может быть квадратная вот каки из этих четырёх два случая здесь ну квадратная и логарифмическая скорее а Почему квадратная Ну наверное всё-таки не квадратная а степень будет зависеть от А в индексе Может быть как раз ивик же может быть составным Угу любопытно'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:47:28 text='Ну возможно совсем неправильно Давай пойдём'
  question_topic: Data Modeling

ITEM #45
  interviewer_question: time=00:47:33 text='дальше когда ты работала с B quy вот как бы ты описала какие есть особенности у этой базы Что нужно учитывать когда ты с'
  candidate_answer: time=00:47:52 text='работаешь Ну особых каких-то синтаксических особенностей при работе с кри Ну именно в запросах я не выявила каких-то существенных разниц А по особенностям работы ну то что как это Облачно было так в принципе как на улице А как это проявлялось что это Облачно вот какая разница между тем что запрос кри отправляешь между тем что ты его отправляешь где-нибудь там на он Прими железе а ну если на железе то может быть зависить от от ресурсов компа например которым это отправляется Ну то есть может ли он обработать этот запрос Ну и в принципе база на железе То есть она получается хранится физически где-то Занимает место если база например большая Окей А облачные они где-то метафизические хранятся Ну ну нет они хранятся всё равно физически просто в Облаке Ну мы об этом не знаем хорошо Ну'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:49:06 text='там есть некоторые оптимизации по-моему за счёт Гугла потому что это гугловский сервис при работе с'
  question_topic: Data Modeling

--- CHAPTER `00:47:35` — BigQuery part 2 ---
window: 00:47:35 .. 00:50:22
recognition_status: multiple (2 items)

ITEM #46
  interviewer_question: time=00:49:13 text='бику Окей вот как пользователь может влиять на эти оптимизации Какие он может магические слова добавлять чтобы сильно сокращать чек затраты на это'
  candidate_answer: time=00:49:25 text='всё там очень классный в интерфейсе есть указатель Там сверху справа Если не ошибаюсь о том сколько данных нужно будет перелопатила в окошке Вот изучало как это тору то что ну это очень это Достаточно давно было когда я работала с кри но я понимаю в чём суть всего этого Про то что А ну при работе со всем этим платишь же За ресурсы если используешь меньше ресурсов соответственно че Постав меньше А вот знаешь термин как это'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:50:02 text='называется в облачной'
  question_topic: Data Modeling

ITEM #47
  interviewer_question: time=00:50:02 text='называется в облачной'
  candidate_answer: time=None text=None
  reference_answer: time=00:50:11 text='что-нибудь типа какая-нибудь аара ой хорошая догадка Да'
  interviewer_feedback: time=None text=None
  question_topic: Product Metrics

--- CHAPTER `00:50:22` — Индексы в OLAP, что вместо part 2 ---
window: 00:50:22 .. 00:52:10
recognition_status: multiple (2 items)

ITEM #48
  interviewer_question: time=00:50:25 text='индексов если собрать всё что мы сейчас обсудили если перейти к лабазе то что там используется вместо индексов для тех же'
  candidate_answer: time=None text=None
  reference_answer: time=00:51:36 text='это партицирование ну или там секционирование партиционирование кто как'
  interviewer_feedback: time=00:51:36 text='это партицирование ну или там секционирование партиционирование кто как называет если собирают какой-нибудь отчёт за месяц если данные хранятся партиции за месяц то Это намного быстрее работает чем читать всю эту таблицу за там несколько лет'
  question_topic: Data Modeling

ITEM #49
  interviewer_question: time=00:51:59 text="О'кей А если говорить про какие-то Лав системы Подскажи м слышал ли что-нибудь про гнп Если да то"
  candidate_answer: time=00:52:13 text='что ну слышала но сама по себе не работала Ну что слышала Ну в принципе что тут Ну читала то что в принципе тоже хорошо подходит если используется довольно большой объём данных для хранения и обработки А есть верхни предел какой-то ещё раз Ну там не знаю 100 петабайт можно хранить не смогу ответить потому что я не сталкивалась сама не проверяла и такой информации не находила'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:53:07 text='Угу Да'
  question_topic: Data Modeling

--- CHAPTER `00:52:10` — Greenplum ---
window: 00:52:10 .. 00:54:08
recognition_status: single (1 items)

ITEM #50
  interviewer_question: time=00:53:14 text='продолжай Ну вроде как читала что там есть э какой-то улучшенный анализатор запросов Ну допустим хорошо'
  candidate_answer: time=00:53:14 text="продолжай Ну вроде как читала что там есть э какой-то улучшенный анализатор запросов Ну допустим хорошо и всё это поверх постгрес номер там 9.4 когда актуальный пог 16 поэтому насколько он там на состоянии 2024 года улучшены Это такой большой вопрос но когда-то да когда-то они с этой стороны себя рекламировали Угу а О'кей А вот"
  reference_answer: time=None text=None
  interviewer_feedback: time=00:54:06 text='Давай может быть ещё про Спарк Немного поговорим напоследок А'
  question_topic: Data Modeling

--- CHAPTER `00:54:08` — Spark оптимизации ---
window: 00:54:08 .. 00:56:40
recognition_status: multiple (5 items)

ITEM #51
  interviewer_question: time=00:54:14 text='расскажи что делало когда не хватало памяти Ну там были какие-то спилы как это'
  candidate_answer: time=00:54:24 text='решал Ну как я уже раньше говорила то что увеличивали количество памяти которую отдавали экзектор в принципе ну один из вариантов но кажется что его довольно дорого применять абсолютно в каждом случае'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:54:48 text='да вот В каких'
  question_topic: Data Modeling

ITEM #52
  interviewer_question: time=00:54:51 text='случаях может не хватать памяти То есть почему там в одной зада подо гиба эте а для другой хватит'
  candidate_answer: time=00:55:02 text='двух Ну зависит от самой задачи что в него входит Ну из чего состоит задача тогда да Из чего состоит задача Ну и какие операции используются вообще в принципе как бы раздели То есть если там группировку Ну вот Даже те же джоны мы можем например Ну вот избежание Если уж я заговорила про позиционирование то А ну например если увеличить количество партиции Угу'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:55:49 text='то в принципе это может помочь Угу'
  question_topic: Data Modeling

ITEM #53
  interviewer_question: time=00:55:56 text='ли ты когда-нибудь Part by в таких задачах А да по-моему использовала Ну точно когда-то использовала Ой а помнишь как выбирала'
  candidate_answer: time=00:56:01 text='А да по-моему использовала Ну точно когда-то использовала Ой а помнишь как выбирала ключ для вот этого распределения Ну смотрела на данные сами по себе что они из себя представляют если это Например какая-то таблица где есть даты скажем то можно выбрать в принципе дату чтобы разбивать по дням'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:56:25 text='Угу'
  question_topic: Data Modeling

ITEM #54
  interviewer_question: time=00:56:08 text='ключ для вот этого'
  candidate_answer: time=00:56:13 text='распределения Ну смотрела на данные сами по себе что они из себя представляют если это Например какая-то таблица где есть даты скажем то можно выбрать в принципе дату чтобы разбивать по дням'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:56:25 text='Угу'
  question_topic: Data Modeling

ITEM #55
  interviewer_question: time=00:56:39 text='а смотрела ли На физическом уровне на уровне взаимодействия с файлами Как работает СРК когда ему нужно например поджо неть две таблички имеешь в виду вот эти имеете в виду физические джоны а которые хэш и N'
  candidate_answer: time=00:56:48 text='таблички имеешь в виду вот эти имеете в виду физические джоны а которые хэш и N можно и про них тогда есть Большая таблица есть маленькая здесь скорее про вот есть какой-то кусочек данных не знаю там про города и он как-то там разложен распределён по разным ном есть какой-то там не знаю объект про продажи и вот нужно как-то посчитать сколько продаж было в каждом городе и вынести какую-то иото та маленькая то я насколько понимаю она целиком копируется по ном Ну потому что она маленькая и в принципе это можно себе позволить а та которая большая та как она разделена кусками она так и остаётся кусками а маленькая копируется каждому куску большой и они уже непосредственно Джой хорошо А если у нас'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:57:41 text='непосредственно Джой хорошо А если у нас две большие таблицы'
  question_topic: Data Modeling

--- CHAPTER `00:56:40` — Spark физические join'ы ---
window: 00:56:40 .. конец
recognition_status: multiple (2 items)

ITEM #56
  interviewer_question: time=00:57:44 text='А если у нас две большие таблицы'
  candidate_answer: time=00:57:52 text='то Сейчас постараюсь помнить ну их тоже нужно будет разделять на части как минимум Они и так остаются разделённые Аа И вероятно эти части как-то двигать по нодом скорее всего одной какой-то таблицы перемещать'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:58:18 text='согласен А как понять какую условную'
  question_topic: Data Modeling

ITEM #57
  interviewer_question: time=00:58:21 text='строчку на какую ноду нужно закинуть Какое здесь условие'
  candidate_answer: time=00:58:37 text='м вот есть шал вот эта операция которая как раз выполняет это перераспределение данных по нодом А как она решает Какую строчку куда отправлять какие там есть стратегии Ну скорее всего если их несколько то есть какая-нибудь случайная стратегия Наверняка есть такая может быть можно как-то хаширова за счёт того что они большие Наверное это было бы удобно что-то в памяти сохранять и хаширова объекты перемещать так именно перемещать ные обекты А как из них потом доставать оригинальные данные Ну за счёт того что они хаширова у них видимо есть ключ можно вот по этому ключу например отсортировать Угу И потом вот уже по отсортированных ключам их разбить Ну пример на равные части между нодами и ну в равных пропорциях их разделять потом'
  reference_answer: time=00:59:53 text='перемещать Ну хорошая догадка и до этого ещё был broadcast когда данные копируются целиком на все ноды без распределения'
  interviewer_feedback: time=01:00:04 text='хорошо принимается похожу там есть Чуть более короткий подход'
  question_topic: Data Modeling

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/dataengineers-pro/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02/data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
