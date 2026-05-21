<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "data-scientist-senior-doordash-commentary-datainterview-2021-02-15",
  "transcript_folder": "transcripts/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/",
  "source_id": "data_scientist_senior_doordash_commentary_datainterview_2021_02_15",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:05:20 +0200",
  "updated_at": "2026-05-20 21:12:36 +0200",
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
    "json": "splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15//timecodes.txt",
        "en",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.pipeline-log.md"
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
        "splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.pipeline-log.md#LLM_INPUT_STEP_2"
      ],
      "outputs": [
        "splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.json"
      ],
      "status": "completed",
      "duration_sec": 180.0,
      "notes": null,
      "finished_at": "2026-05-20 21:12:36 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:12:35 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15//video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:12:36 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/`
- **Source ID:** `data_scientist_senior_doordash_commentary_datainterview_2021_02_15`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:05:20 +0200
- **Last updated:** 2026-05-20 21:12:36 +0200

Фильтр в IDE: `*data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15//timecodes.txt`<br>`en`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.pipeline-log.md` | — | completed |
| 2 | qa_extraction | yes | claude-sonnet-4-6 | `splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.pipeline-log.md#LLM_INPUT_STEP_2` | `splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.json` | 180.0s | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15//video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.validation-report.md` | 1.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.pipeline-log.md`

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
SOURCE_ID: data_scientist_senior_doordash_commentary_datainterview_2021_02_15
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/
INTERVIEW_LANGUAGE: en
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:01] hello candidates my name is dan lee
[00:04] i'm a data scientist interview coach at
[00:05] topdies.org in the next couple minutes
[00:08] we're going to go over a product data
[00:10] scientist mock interview
[00:12] at doordash the video itself is going to
[00:14] be about 10 minutes
[00:16] and i'm going to drop in some
[00:17] commentaries here and there to provide
[00:20] some suggestions in terms of what the
[00:21] candidate did well
[00:23] and what are some areas of improvement i
[00:25] really hope that you find this video
[00:26] helpful for your upcoming mock interview
[00:29] hello hi
[00:32] so this is the doordash mock interview
[00:35] um thank you for attending this call
[00:37] um what we're gonna do is we're gonna
[00:39] spend about 30-40 minutes going through
[00:41] some
[00:41] product data science questions um and
[00:45] the first five to ten minutes are going
[00:47] to be focused on statistics questions
[00:49] and then we'll spend the remaining uh 40
[00:52] 30
[00:53] 40 minutes just going through some case
[00:54] study questions covering a b testing
[00:56] analytics does that sound good
[01:00] sounds quick okay awesome all right so
[01:02] what i'm going to do is i'm going to
[01:03] paste
[01:04] questions um one at a time on the
[01:06] quarter pad
[01:07] and feel free to use it as your as a
[01:10] scratch sheet you know
[01:11] jot down your ideas and so forth and
[01:13] along the way if you have any questions
[01:15] um feel free to ask
[01:18] okay okay cool here's a quick helpful
[01:22] tip
[01:22] for candidates who have upcoming
[01:24] interviews keep in mind
[01:26] that a lot of the interviews during
[01:28] coven are virtual
[01:30] this means that you'll gain access to
[01:32] quarter pad or word document
[01:35] and when you're in a situation where you
[01:37] have to solve a case problem
[01:40] it's recommended that you actually flesh
[01:42] out the ideas
[01:44] by writing down your points rather than
[01:46] just overly explaining it
[01:48] this is going to be helpful in two
[01:50] fronts one
[01:51] it's going to be helpful for you to
[01:53] brainstorm ideas
[01:55] and two it helps the interviewer see
[01:57] your thought process
[01:59] so when you have an upcoming interview
[02:01] please use your
[02:02] use decoder pad and word document as a
[02:05] place to actually drop down your ideas
[02:08] all right so let's start with the first
[02:09] status questions what does 90
[02:11] statistical power mean
[02:15] um so uh so it's 90
[02:19] statistical power uh so statistical
[02:22] power
[02:22] is basically uh linked to the type one
[02:25] type of two errors
[02:26] which means uh what is the probability
[02:28] of
[02:29] uh finding a right observation when it
[02:32] uh
[02:32] when it doesn't exist or finding an
[02:34] observation uh
[02:36] or or saying that we found enough uh we
[02:38] did not found an
[02:39] observation when it exists so 90
[02:42] statistical power means the the
[02:45] probability
[02:46] of uh finding an observation
[02:50] which uh of not finding an observation
[02:54] which exists
[02:54] is 90 notice how the interview started
[02:58] the interviewer asked a fundamental
[03:00] question in statistics
[03:02] this is actually pretty typical in phone
[03:04] screening and on-site rounds
[03:07] an interviewer will kind of pepper
[03:10] various questions on the fundamentals of
[03:13] statistics and machine learning theory
[03:15] in order to assess whether the candidate
[03:18] grasps
[03:19] a basic knowledge in data science and
[03:21] machine learning engineering
[03:24] so let's think about the question itself
[03:27] the question is
[03:28] what is what does 90 power mean
[03:32] now ninety percent power is the
[03:35] probability
[03:36] of rejecting the null hypothesis given
[03:38] that the alternative is true
[03:41] this is actually not the same as what
[03:44] the candidate said
[03:45] so what the candidate said was it is the
[03:48] probability of not
[03:49] finding an observation when it exists
[03:53] in slightly off way i think what the
[03:56] candidate was conveying
[03:57] was that it's a type 2 error which is
[04:00] actually not the same as power
[04:02] so in this case the candidate's response
[04:05] was incorrect
[04:07] now as as you're preparing for your
[04:11] interview
[04:12] you want to make sure that you brush up
[04:14] on these fundamental concepts
[04:16] because there's no room for
[04:18] interpretation when you're asked
[04:19] questions like these it's either you're
[04:22] right or wrong you're wrong
[04:23] so what i would recommend is that you
[04:26] create an
[04:26] index card and you type you basically
[04:29] put down
[04:31] the term and the definition in the back
[04:34] and you go through these index cards
[04:36] as a way to practice explaining these
[04:39] basic concepts
[04:40] in statistics and machine learning
[04:43] theory
[04:45] okay all right
[04:48] next question how do you determine the
[04:51] practical significance in a
[04:53] in an experiment so when it depends on
[04:57] the type of experiment we run
[04:59] and the kind of metric we are looking at
[05:01] so matrix can be
[05:03] uh like mean um like mean is a metric or
[05:07] a rate can be a vector
[05:08] and metric can also be proportions right
[05:11] so
[05:12] it can be percentage of users that click
[05:15] on a particular link or things like that
[05:18] so
[05:19] in these both of these cases we do some
[05:21] kind of statistical tests
[05:23] like a two sided t test or
[05:26] a test of proportions uh and practical
[05:28] significant and the significance of
[05:30] those
[05:30] is determined by p value uh which in
[05:33] general it's
[05:34] if it's below 0.05 we say it's
[05:37] significant
[05:38] now that is just the statistical part if
[05:40] you wanna
[05:41] uh look at the practical part we would
[05:43] also look have to look at
[05:45] the business metrics for example the
[05:47] kind of lift that we have seen
[05:49] and that will depend on the cost benefit
[05:51] analysis so let's say
[05:53] uh a five percent increase in uh ltv
[05:56] of a consumer on a particular app
[06:00] would be profitable for us and that
[06:02] would be the break-even point and
[06:03] anything above that
[06:04] would be useful whereas anything below
[06:07] that would not be useful
[06:08] so if so if we look at that
[06:11] uh basically what we are seeing what we
[06:14] are saying is
[06:15] even if the results are significant
[06:18] statistically only if they make business
[06:21] sense
[06:21] then it would be practically significant
[06:24] and then there is one more aspect which
[06:26] is
[06:26] movement of multiple metrics so let's
[06:29] say
[06:30] we do an experimentation on one
[06:32] particular metric
[06:33] but and that comes out to be significant
[06:35] but the other metrics
[06:37] move along with it in the experiment uh
[06:40] and
[06:40] that can be like detrimental to our
[06:43] experiment so
[06:44] we will have to use that as well in our
[06:47] uh stating the practical significance of
[06:49] the experiment
[06:50] let's break down the question number two
[06:52] in regards to the practical significance
[06:54] in an experimentation
[06:56] what the candidate mentioned are two
[06:58] things first
[07:00] the candidate mentioned the cost-benefit
[07:02] analysis of launching a product
[07:04] and secondly the candidate mentioned on
[07:06] multiple metrics
[07:07] so looking at let's just say the primary
[07:10] metric and guard rail nature
[07:12] now in this case the candidate has a
[07:14] right understanding
[07:15] about the practical significance of an
[07:17] experimentation
[07:19] in an experimentation typically there's
[07:21] a socialization that happens upfront
[07:23] with the business stakeholder to
[07:25] determine
[07:26] what is a meaningful experimental result
[07:30] so just because an experimentation
[07:32] achieved
[07:34] um successful significance so p-value is
[07:38] less than alpha
[07:39] it doesn't mean that the treatment
[07:41] itself
[07:42] should replace the controller because it
[07:45] might not provide a necessary
[07:47] return on investment to actually launch
[07:50] that new future
[07:51] for instance the cost of actually
[07:54] building out
[07:54] the future for the wider audience to use
[07:58] might be more costly than the benefit or
[08:00] the
[08:01] or the additional revenue that you would
[08:03] gain by launching
[08:05] that in future and so the candidate here
[08:09] had the right concept about the
[08:12] practical significance of an
[08:14] experimentation
[08:16] okay so how would you handle it's such a
[08:18] case then
[08:19] if one of the metric is practically
[08:21] significant
[08:23] but the other one isn't uh
[08:26] there can be a couple of ways to handle
[08:28] it one can be
[08:30] changing the design of experiment so
[08:33] making the experiment
[08:34] uh you know a bit narrowed down in terms
[08:37] of
[08:37] the users that are going into the
[08:39] experiment uh
[08:41] that can make sure that we that we only
[08:44] move one metric and not the other metric
[08:46] uh and then we can also look at
[08:48] correlation or causation of the true
[08:50] matrix so if one metric is correlated to
[08:52] the other
[08:53] or one metric is a result of a causal
[08:55] inference from the other
[08:57] uh we can we would we should assume that
[08:59] the metric would
[09:00] move but if that is not the case then
[09:03] maybe we can you know
[09:04] put some controls uh in place and
[09:08] then run the experiment again to get a
[09:10] better significance
[09:11] okay got it all right i'll ask the next
[09:14] question
[09:16] now how do you calculate type 1 and type
[09:18] your errors of your statistical tests
[09:24] okay so um
[09:28] one and type two errors uh
[09:31] can be calculated by uh use english
[09:37] can calculate it by um
[09:42] i mean by by using like uh
[09:46] you know uh i'm not really sure about
[09:49] this
[09:50] uh so probably
[09:54] uh by let's see do you want to start by
[09:56] explaining what type one type of error
[09:59] error rates are sure um
[10:02] a time for an error is basically uh
[10:05] nothing but a false positive
[10:07] so uh so it happens when
[10:10] uh the experiment incorrectly rejects
[10:13] the true null hypothesis uh and
[10:17] you know in which actually it should not
[10:20] so then a type one error occurs uh a
[10:22] type two error on the other hand it's
[10:24] a false negative it happens when an
[10:27] experiment
[10:28] does not reject the null hypothesis but
[10:30] it's uh but
[10:32] you know but the result is actually
[10:33] false so it should reject the hypothesis
[10:35] okay
[10:36] got it so in this case um what would be
[10:39] your
[10:39] type 1 error rate
[10:42] uh so type 1 error rate uh
[10:46] you know in this case would be uh
[10:51] you know uh so basically let's say we
[10:54] have a null hypothesis
[10:56] uh that you know there is no significant
[11:00] change in the click-through rate uh of
[11:02] two types of users
[11:04] so there will be a type one uh error
[11:06] where you know
[11:08] this hypothesis will be rejected and and
[11:11] we
[11:11] find the results that there is a
[11:14] significant
[11:15] uh difference between the two uh you
[11:17] know
[11:18] the the two sides and one way of
[11:21] controlling that i can think of
[11:22] is using the power so
[11:26] power is nothing but uh statistical
[11:29] power is nothing but
[11:30] beta uh and that's the probability of
[11:32] making like
[11:33] say a type two error so power of
[11:36] of the set of three tests is one minus
[11:39] beta so
[11:40] you know we can adjust for that value
[11:42] okay
[11:43] so i'm going to interject there um
[11:45] because i think i want to kind of give
[11:46] you some hint here so let's just suppose
[11:48] that alpha is 0.05
[11:50] and your beta is
[11:53] uh let's just let's just suppose that
[11:56] your power
[11:57] is um 0.8 then in that case how would
[12:01] you actually calculate your
[12:02] type 1 error type 1 and type tap to
[12:04] error rates
[12:07] uh sure uh so the problem so you
[12:09] mentioned b
[12:10] beta is 20 power power is point eight
[12:15] power and your alpha is point zero five
[12:18] okay so if power is point eight it means
[12:21] a power is one minus beta so your beta
[12:24] would be 0.2
[12:25] so the probability of making a type 2
[12:27] error would be
[12:28] 0.2 um and alpha you mentioned is 0.05
[12:33] right
[12:34] so alpha is 0.05 and i think that's the
[12:38] uh probability of committing a type one
[12:41] error so it's like a five percent
[12:42] probability of committing a type one
[12:44] okay okay awesome notice how the
[12:48] candidate struggled a little bit in the
[12:49] beginning
[12:50] eventually the candidate recovered
[12:52] because the interviewer gave
[12:54] the candidate a couple hits now in order
[12:57] to calculate the type 1 error rate
[12:58] type 2 error rate let's just think about
[13:00] what the definitions of those two are
[13:03] type 1 error rate is a probability of
[13:05] rejecting the null hypothesis
[13:08] when it is true type of errate
[13:11] is the rejecting of not rejecting the
[13:14] null hypothesis
[13:15] when the alternative is true
[13:19] how do you actually calculate tempo and
[13:21] error rate and type 2 error rate
[13:23] so type 1 error rate is essentially your
[13:25] alpha so whatever your alpha
[13:27] you set so typically in successful
[13:29] testing it still be 0.05
[13:33] um sorry i meant to say at least in
[13:35] product
[13:36] experimentation it's typically 0.05
[13:39] and so that is actually going to be the
[13:41] type on error rate
[13:43] now for tattoo air rate it is actually
[13:46] the complement of power
[13:48] so suppose that power is eighty percent
[13:51] then in that case peptide rate is going
[13:53] to be the complement of that
[13:55] which is going to be 20 i hope you
[13:58] enjoyed
[13:59] a sample of this mock interview with
[14:01] some commentaries
[14:02] this is just a sample of what's more to
[14:04] come in the near future
[14:06] in the near future i'll publish more
[14:08] videos like this
[14:09] that will cover rounds focused on
[14:11] statistics
[14:12] sql statistical coding machine learning
[14:16] engineering and product sense
[14:19] if you like this video please subscribe
[14:23] like and share with others and that's
[14:25] going to encourage me
[14:26] to continue to provide more videos like
[14:28] this thank you

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
Write JSON only to: splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.json \
    --video transcripts/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15//video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.json --out splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.qa-split.json \
    --video transcripts/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15//video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.validation-report.md

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
video.md: transcripts/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/video.md

--- CHAPTER `02:10` — What Does 90 Statistical Power Mean ---
window: 02:10 .. 04:50
recognition_status: single (1 items)

ITEM #3
  interviewer_question: time=04:48 text='next question how do you determine the practical significance in a in an experiment'
  candidate_answer: time=04:53 text="so when it depends on the type of experiment we run and the kind of metric we are looking at so matrix can be uh like mean um like mean is a metric or a rate can be a vector and metric can also be proportions right so it can be percentage of users that click on a particular link or things like that so in these both of these cases we do some kind of statistical tests like a two sided t test or a test of proportions uh and practical significant and the significance of those is determined by p value uh which in general it's if it's below 0.05 we say it's significant now that is just the statistical part if you wanna uh look at the practical part we would also look have to look at the business metrics for example the kind of lift that we have seen and that will depend on the cost benefit analysis so let's say uh a five percent increase in uh ltv of a consumer on a particular app would be profitable for us and that would be the break-even point and anything above that would be useful whereas anything below that would not be useful so if so if we look at that uh basically what we are seeing what we are saying is even if the results are significant statistically only if they make business sense then it would be practically significant and then there is one more aspect which is movement of multiple metrics so let's say we do an experimentation on one particular metric but and that comes out to be significant but the other metrics move along with it in the experiment uh and that can be like detrimental to our experiment so we will have to use that as well in our uh stating the practical significance of the experiment"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Experimentation

--- CHAPTER `04:50` — How Do You Determine the Practical Significance in a in an Experiment ---
window: 04:50 .. 10:39
recognition_status: multiple (4 items)

ITEM #4
  interviewer_question: time=08:16 text="okay so how would you handle it's such a case then if one of the metric is practically significant but the other one isn't"
  candidate_answer: time=08:23 text='uh there can be a couple of ways to handle it one can be changing the design of experiment so making the experiment uh you know a bit narrowed down in terms of the users that are going into the experiment uh that can make sure that we that we only move one metric and not the other metric uh and then we can also look at correlation or causation of the true matrix so if one metric is correlated to the other or one metric is a result of a causal inference from the other uh we can we would we should assume that the metric would move but if that is not the case then maybe we can you know put some controls uh in place and then run the experiment again to get a better significance'
  reference_answer: time=None text=None
  interviewer_feedback: time=09:11 text="okay got it all right i'll ask the next question"
  question_topic: Experimentation

ITEM #5
  interviewer_question: time=09:16 text='now how do you calculate type 1 and type your errors of your statistical tests'
  candidate_answer: time=09:24 text="okay so um one and type two errors uh can be calculated by uh use english can calculate it by um i mean by by using like uh you know uh i'm not really sure about this uh so probably"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Statistics

ITEM #6
  interviewer_question: time=09:54 text='do you want to start by explaining what type one type of error error rates are sure'
  candidate_answer: time=10:02 text="um a time for an error is basically uh nothing but a false positive so uh so it happens when uh the experiment incorrectly rejects the true null hypothesis uh and you know in which actually it should not so then a type one error occurs uh a type two error on the other hand it's a false negative it happens when an experiment does not reject the null hypothesis but it's uh but you know but the result is actually false so it should reject the hypothesis"
  reference_answer: time=None text=None
  interviewer_feedback: time=10:35 text='okay'
  question_topic: Statistics

ITEM #7
  interviewer_question: time=10:36 text='got it so in this case um what would be your type 1 error rate'
  candidate_answer: time=10:42 text="uh so type 1 error rate uh you know in this case would be uh you know uh so basically let's say we have a null hypothesis uh that you know there is no significant change in the click-through rate uh of two types of users so there will be a type one uh error where you know this hypothesis will be rejected and and we find the results that there is a significant uh difference between the two uh you know the the two sides and one way of controlling that i can think of is using the power so power is nothing but uh statistical power is nothing but beta uh and that's the probability of making like say a type two error so power of of the set of three tests is one minus beta so you know we can adjust for that value"
  reference_answer: time=None text=None
  interviewer_feedback: time=11:42 text='okay'
  question_topic: Statistics

--- CHAPTER `10:39` — Type 1 Error Rate ---
window: 10:39 .. конец
recognition_status: single (1 items)

ITEM #8
  interviewer_question: time=11:43 text="so i'm going to interject there um because i think i want to kind of give you some hint here so let's just suppose that alpha is 0.05 and your beta is uh let's just let's just suppose that your power is um 0.8 then in that case how would you actually calculate your type 1 error type 1 and type tap to error rates"
  candidate_answer: time=12:07 text="uh sure uh so the problem so you mentioned b beta is 20 power power is point eight power and your alpha is point zero five okay so if power is point eight it means a power is one minus beta so your beta would be 0.2 so the probability of making a type 2 error would be 0.2 um and alpha you mentioned is 0.05 right so alpha is 0.05 and i think that's the uh probability of committing a type one error so it's like a five percent probability of committing a type one"
  reference_answer: time=None text=None
  interviewer_feedback: time=12:44 text='okay okay awesome'
  question_topic: Statistics

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/datainterview/data-scientist-senior-doordash-commentary-datainterview-2021-02-15/data-scientist-senior-doordash-commentary-datainterview-2021-02-15.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
