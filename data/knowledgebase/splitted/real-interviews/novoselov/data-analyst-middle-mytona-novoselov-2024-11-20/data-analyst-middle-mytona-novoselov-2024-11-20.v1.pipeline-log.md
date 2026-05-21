<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "data-analyst-middle-mytona-novoselov-2024-11-20",
  "transcript_folder": "transcripts/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20",
  "source_id": "data_analyst_middle_mytona_novoselov_2024_11_20",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:21:48 +0200",
  "updated_at": "2026-05-20 21:27:50 +0200",
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
    "json": "splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.json",
    "xlsx": "splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/timecodes.txt",
        "ru",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 21:21:48 +0200"
    },
    {
      "id": 2,
      "name": "qa_extraction",
      "llm": true,
      "model": "claude-sonnet-4-6",
      "inputs": [
        "splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.pipeline-log.md#LLM_INPUT_STEP_2"
      ],
      "outputs": [
        "splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.json"
      ],
      "status": "completed",
      "duration_sec": 60.0,
      "notes": null,
      "finished_at": "2026-05-20 21:24:51 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 2.0,
      "notes": null,
      "finished_at": "2026-05-20 21:26:22 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 2.0,
      "notes": null,
      "finished_at": "2026-05-20 21:26:23 +0200"
    },
    {
      "id": 5,
      "name": "llm_validation",
      "llm": true,
      "model": "claude-sonnet-4-6",
      "inputs": [
        "splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.pipeline-log.md#LLM_INPUT_STEP_5"
      ],
      "outputs": [
        "splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 30.0,
      "notes": null,
      "finished_at": "2026-05-20 21:27:50 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20`
- **Source ID:** `data_analyst_middle_mytona_novoselov_2024_11_20`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:21:48 +0200
- **Last updated:** 2026-05-20 21:27:50 +0200

Фильтр в IDE: `*data-analyst-middle-mytona-novoselov-2024-11-20.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/timecodes.txt`<br>`ru`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.pipeline-log.md` | — | completed |
| 2 | qa_extraction | yes | claude-sonnet-4-6 | `splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.pipeline-log.md#LLM_INPUT_STEP_2` | `splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.json` | 60.0s | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.xlsx` | 2.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.validation-report.md` | 2.0s | completed |
| 5 | llm_validation | yes | claude-sonnet-4-6 | `splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.pipeline-log.md#LLM_INPUT_STEP_5` | `splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.validation-report.md` | 30.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.json`
- **xlsx:** `splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.pipeline-log.md`

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
SOURCE_ID: data_analyst_middle_mytona_novoselov_2024_11_20
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20
INTERVIEW_LANGUAGE: ru
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00] Давненько У нас не было слитых со бесов
[00:01] на аналитика друзья точнее их вообще
[00:03] никогда не было это первое собеседование
[00:05] такое и мне всегда было интересно что
[00:07] спрашивают у них на собеседованиях и
[00:09] оказалось что стать аналитиком гораздо
[00:11] проще чем кажется и вот вкратце что вам
[00:13] нужно знать что мы обращаем Внимание это
[00:15] именно на сам продуктовый подход да то
[00:17] есть именно на опыт человека в
[00:19] продуктовой аналитике работал ли он
[00:21] когда-нибудь непосредственно с этим Да
[00:24] анализировал ли РФ в принципе Понимает
[00:27] ли Какие метрики могут быть считаются Да
[00:31] конечно же это знания SQL дальше скорее
[00:34] всего вам начнут задавать какие-нибудь
[00:35] глупые вопросы скажи пожалуйста про себя
[00:37] про свою опыт работы и можешь вспомнить
[00:39] были ли у тебя какие-то кейсы когда тебе
[00:41] удалось проявить инициативу в компании а
[00:44] по процессам что-нибудь улучшали ты
[00:48] замечал спор про ваш опыт А ты вот как
[00:50] сам Работаешь с ДХ напрямую Да можешь ли
[00:54] ещ как-нибудь подсказать Какого типа
[00:56] анализы ты делаешь и наконец переду к
[00:59] самому собеседование знаешь ли ты что
[01:01] такое ошибки первого и второго рода
[01:03] ошибкой первого рода в статистике
[01:05] называют ложно положительное заключение
[01:07] то есть ситуацию когда нулевая гипотеза
[01:09] была ложно отвергнута Другими словами
[01:12] это ложная тревога Вот это ложная
[01:15] тревога а ошибкой второго рода
[01:17] называется ложноположительные заключения
[01:20] То есть когда была принята Неверная
[01:21] нулевая гипотеза и другими словами это
[01:23] такой пропуск события если по аналогии
[01:25] смотреть В чём отличие одностороннего
[01:27] двухстороннего критерия Что такое тест
[01:30] это во-первых конечно же нулевая
[01:31] гипотеза это какая-то альтернативная
[01:34] гипотеза это какая-то функция и
[01:36] распределение этой функции при условии
[01:38] того что нулевая гипотеза верна И также
[01:40] у нас есть какая-то выборка мы применяем
[01:42] нашу функцию то есть нашу статистику да
[01:44] эту функцию называют статистика к нашей
[01:46] выборке и смотрим в какую область
[01:48] распределения попадают наши значения и
[01:50] если эти значения попадают в достаточно
[01:52] маловероятной область то мы отвергаем
[01:54] нулевую гипотезу как маловероятно И если
[01:57] при этом мы смотрим только на левый край
[01:59] распределения или только на правый то
[02:01] такой тест называется односторонним А
[02:03] если мы смотрим на оба края
[02:04] распределения то это двусторонний тест
[02:06] дорогие друзья те кто смотрит это видео
[02:08] У меня есть обучающая программа которая
[02:10] называется офер подключ на ней я не
[02:11] только Обучаю тебя проходить
[02:13] собеседование не только даю тебе новые
[02:15] знания но ещё и помогаю устроиться на
[02:18] работу и также пройти испытательный срок
[02:20] и только после этого ты уже платишь мне
[02:22] денежку в отличие от курсов которые не
[02:24] дают тебе никакую гарантию поступив на
[02:26] нашу программу ты получаешь гарантию
[02:28] того что ты трудоустроится если сделаешь
[02:30] всё что Конечно тебе скажет наш ментор и
[02:32] более того ты потратишь на нашу
[02:34] программу не 1-2 года Как это ты
[02:36] потратил бы на курсах А всего за
[02:37] несколько месяцев ты станешь уровнем
[02:39] midle и устроишься на работу Поэтому
[02:41] ссылочка будет в описании а более
[02:43] подробно про то как устроена эта
[02:45] программа вот в этом вот видео можете
[02:46] нажать и посмотреть с первой задача У
[02:48] нас есть две таблички Да в первой
[02:50] табличке есть два столбца в первом
[02:53] столбце это userid уникальный
[02:55] идентификатор игрока а во втором столбце
[02:58] его ка код во второй табличке У нас два
[03:01] столбца Первое - это User ID а второе -
[03:04] это Чи identificate то есть
[03:06] идентификатор читера как ты будешь
[03:09] быстро доставать игроков из первой
[03:11] таблицы у которых нет идентификатора
[03:13] читера во второй таблице для решение
[03:16] этой задачи можно сделать подзапрос ко
[03:17] второй таблице и достать оттуда всех
[03:19] читеров а затем сделать запрос к первой
[03:21] таблице и достать всех юзеров которые не
[03:23] входят в этот список читеров А второй
[03:25] вариант решения - это сделать Left Join
[03:27] первой и второй таблицы и просто обычным
[03:29] селек там достать всех пользователей
[03:31] которые не читеры вот вопрос Какой из
[03:33] этих вариантов быстрее ответ напишите в
[03:34] комментариях теперь я хотела показать
[03:36] тебе вторую задачу У нас также есть две
[03:39] таблицы Первая таблица логит время
[03:42] выигрыша конкретного уровня То есть ты
[03:44] как раз рассказывал какую-то похожий
[03:46] таск который делал Да User ID там есть
[03:48] тайм штам есть и level на Угу во второй
[03:51] таблице purchases логи все покупки
[03:54] игроков выглядит как User ID Таш и Price
[03:57] и нужно выяснить На каком уровне игроки
[03:59] чаще всего конверти в первую покупку А
[04:02] вот эта задача уже сложнее для её
[04:03] решения нужно сделать две под таблицы Т1
[04:06] и Т2 кстати такая форма записи Swiss
[04:08] называется cte то есть Common Table
[04:10] Expression таблица Т1 содержит
[04:12] информацию о пройденных уровнях каждым
[04:14] пользователем А вот это вот оконная
[04:16] функция вычисляет время предыдущего
[04:17] события для каждого пользователя а в
[04:19] таблице Т2 Мы выбираем минимальное время
[04:22] каждой покупки для каждого пользователя
[04:23] в таблице purchase А дальше мы просто
[04:26] группируя по User ID и это нам позволяет
[04:28] определить время первой по покупки для
[04:30] каждого пользователя Ну и основной
[04:31] запрос выглядит так что мы просто делаем
[04:33] inner Join по нужным задачи формулам и
[04:36] дальше Просто группируя по уровнем чтобы
[04:38] получить количество Хорошо тогда у меня
[04:40] вопросы по идее закончились Юля в целом
[04:43] вот такое вот короткое получилось
[04:45] собеседование Напишите в комментарии
[04:46] обязательно Нравится ли вам такой формат
[04:48] разборов и хотели ли бы вы чтобы на моём
[04:50] канале выходило больше собеседований на
[04:52] Data аналитика Не забывайте
[04:53] подписываться на все Мои соцсети и
[04:55] платформы например в телеге я выкладываю
[04:57] лай контент А в инсте я пощу какие-то
[04:59] мемы и полезную информацию а ролики
[05:01] выкладываю конечно же на тубе рутубе и
[05:03] ВК а также у меня есть сайт со всеми
[05:05] моими образовательными проектами это
[05:07] офер подключ База знаний и it сообщество
[05:10] обязательно заходите и смотрите по
[05:11] ссылочки в описании либо по этому QR
[05:14] коду Ну а с вами я прощаюсь друзья Желаю
[05:15] вам жирных офферов и до новых встреч
[05:18] Всем пока
[05:20] [музыка]

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
Write JSON only to: splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.json \
    --video transcripts/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.json --out splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.qa-split.json \
    --video transcripts/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/video.md \
    --tolerance 120 \
    --out splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.validation-report.md

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
video.md: /Users/mm/projects/ds-final-project/transcripts/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/video.md

--- CHAPTER `00:33` — Базовые вопросы от HR ---
window: 00:33 .. 00:49
recognition_status: multiple (2 items)

ITEM #1
  interviewer_question: time=00:35 text='скажи пожалуйста про себя про свою опыт работы и можешь вспомнить были ли у тебя какие-то кейсы когда тебе удалось проявить инициативу в компании а по процессам что-нибудь улучшали ты замечал'
  candidate_answer: time=None text=None
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Ownership

ITEM #2
  interviewer_question: time=00:48 text='А ты вот как сам Работаешь с ДХ напрямую'
  candidate_answer: time=00:50 text='Да'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Data Modeling

--- CHAPTER `00:49` — Вопросы про опыт ---
window: 00:49 .. 01:01
recognition_status: multiple (2 items)

ITEM #3
  interviewer_question: time=00:54 text='можешь ли ещё как-нибудь подсказать Какого типа анализы ты делаешь'
  candidate_answer: time=None text=None
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Product Metrics

ITEM #4
  interviewer_question: time=00:59 text='знаешь ли ты что такое ошибки первого и второго рода'
  candidate_answer: time=None text=None
  reference_answer: time=01:03 text='ошибкой первого рода в статистике называют ложно положительное заключение то есть ситуацию когда нулевая гипотеза была ложно отвергнута Другими словами это ложная тревога Вот это ложная тревога а ошибкой второго рода называется ложноположительные заключения То есть когда была принята Неверная нулевая гипотеза и другими словами это такой пропуск события если по аналогии смотреть'
  interviewer_feedback: time=None text=None
  question_topic: Statistics

--- CHAPTER `01:01` — Что такое ошибка первого и второго рода? ---
window: 01:01 .. 01:25
recognition_status: not_recognized (0 items)

(no items extracted)
--- CHAPTER `01:25` — В чём отличие одностороннего от двустороннего критерия? ---
window: 01:25 .. 02:06
recognition_status: single (1 items)

ITEM #5
  interviewer_question: time=01:25 text='В чём отличие одностороннего двухстороннего критерия Что такое тест'
  candidate_answer: time=None text=None
  reference_answer: time=01:30 text='это во-первых конечно же нулевая гипотеза это какая-то альтернативная гипотеза это какая-то функция и распределение этой функции при условии того что нулевая гипотеза верна И также у нас есть какая-то выборка мы применяем нашу функцию то есть нашу статистику да эту функцию называют статистика к нашей выборке и смотрим в какую область распределения попадают наши значения и если эти значения попадают в достаточно маловероятной область то мы отвергаем нулевую гипотезу как маловероятно И если при этом мы смотрим только на левый край распределения или только на правый то такой тест называется односторонним А если мы смотрим на оба края распределения то это двусторонний тест'
  interviewer_feedback: time=None text=None
  question_topic: Statistics

--- CHAPTER `02:49` — Задача по SQL №1 ---
window: 02:49 .. 03:35
recognition_status: single (1 items)

ITEM #6
  interviewer_question: time=03:06 text='как ты будешь быстро доставать игроков из первой таблицы у которых нет идентификатора читера во второй таблице'
  candidate_answer: time=None text=None
  reference_answer: time=03:16 text='для решение этой задачи можно сделать подзапрос ко второй таблице и достать оттуда всех читеров а затем сделать запрос к первой таблице и достать всех юзеров которые не входят в этот список читеров А второй вариант решения - это сделать Left Join первой и второй таблицы и просто обычным селек там достать всех пользователей которые не читеры'
  interviewer_feedback: time=03:33 text='вот вопрос Какой из этих вариантов быстрее ответ напишите в комментариях'
  question_topic: SQL

--- CHAPTER `03:35` — Задача по SQL №2 ---
window: 03:35 .. 04:38
recognition_status: single (1 items)

ITEM #7
  interviewer_question: time=03:57 text='нужно выяснить На каком уровне игроки чаще всего конверти в первую покупку'
  candidate_answer: time=None text=None
  reference_answer: time=04:02 text='для её решения нужно сделать две под таблицы Т1 и Т2 кстати такая форма записи Swiss называется cte то есть Common Table Expression таблица Т1 содержит информацию о пройденных уровнях каждым пользователем А вот это вот оконная функция вычисляет время предыдущего события для каждого пользователя а в таблице Т2 Мы выбираем минимальное время каждой покупки для каждого пользователя в таблице purchase А дальше мы просто группируя по User ID и это нам позволяет определить время первой по покупки для каждого пользователя Ну и основной запрос выглядит так что мы просто делаем inner Join по нужным задачи формулам и дальше Просто группируя по уровнем чтобы получить количество'
  interviewer_feedback: time=None text=None
  question_topic: SQL

SAVE JSON: вставьте ответ в конец файла /Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-analyst-middle-mytona-novoselov-2024-11-20/data-analyst-middle-mytona-novoselov-2024-11-20.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
