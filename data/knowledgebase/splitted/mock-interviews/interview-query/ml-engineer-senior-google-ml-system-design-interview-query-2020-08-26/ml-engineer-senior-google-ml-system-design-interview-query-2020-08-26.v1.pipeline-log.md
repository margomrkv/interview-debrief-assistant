<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26",
  "transcript_folder": "transcripts/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26",
  "source_id": "ml_engineer_senior_google_ml_system_design_interview_query_2020_08_26",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:18:03 +0200",
  "updated_at": "2026-05-20 21:30:43 +0200",
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
    "json": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/timecodes.txt",
        "en",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 21:18:03 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 2.0,
      "notes": null,
      "finished_at": "2026-05-20 21:30:42 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 2.0,
      "notes": null,
      "finished_at": "2026-05-20 21:30:43 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26`
- **Source ID:** `ml_engineer_senior_google_ml_system_design_interview_query_2020_08_26`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:18:03 +0200
- **Last updated:** 2026-05-20 21:30:43 +0200

Фильтр в IDE: `*ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/timecodes.txt`<br>`en`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.pipeline-log.md` | — | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.xlsx` | 2.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.validation-report.md` | 2.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.pipeline-log.md`

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
SOURCE_ID: ml_engineer_senior_google_ml_system_design_interview_query_2020_08_26
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26
INTERVIEW_LANGUAGE: en
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00] [Music]
[00:04] hi everyone
[00:05] today i'm doing a mock interview with
[00:07] dan
[00:08] uh which we have done before and i
[00:10] wanted to get into
[00:12] more of the uh kind of surroundings
[00:15] around
[00:16] uh what we're trying to go on about uh
[00:19] system design and machine learning
[00:20] interviews
[00:21] uh and so dan who needs no introduction
[00:24] is
[00:24] a general expert in this field and i
[00:27] think uh
[00:27] talking to him more about these problems
[00:30] uh will really kind of open up
[00:32] what things that are really good for
[00:35] interviewing
[00:36] and just general data science as well
[00:38] right so
[00:39] dan thanks for being here again
[00:42] totally yeah glad to do it yeah so today
[00:45] um i wanted to talk about a kind of
[00:48] recommendations interview question and
[00:49] so we can kind of dive right into it
[00:51] uh but uh the question is uh
[00:54] so let's say that you're basically a
[00:56] machine learning engineer
[00:58] um on youtube right and this is uh
[01:01] you're tasked with basically building
[01:03] the youtube
[01:04] uh video recommendation algorithm how
[01:07] would you go about and start like this
[01:09] uh process for building it uh yeah so
[01:12] i do have the advantage of having heard
[01:14] this question before
[01:16] uh and thinking about it i think it's uh
[01:18] it's
[01:19] just such a huge scope i mean youtube
[01:21] with
[01:22] billions of videos billions of or
[01:25] millions of users and accounts
[01:26] um they certainly have a difficult task
[01:29] ahead of them
[01:30] how do i recommend the right video to
[01:33] the right user at the right time
[01:34] in the right context yes um and so i
[01:37] think there's like multiple approaches
[01:39] there's the idea of you know starting
[01:41] what if youtube weren't as big as it is
[01:43] right now
[01:44] and it started small and we had maybe
[01:46] 100 videos
[01:47] and 10 users and then how do we scale
[01:50] that up
[01:50] to the youtube of 2020 and i think
[01:53] another approach is like hey
[01:56] it's youtube 2020 and we need to build
[01:58] the recommendation engine from scratch
[01:59] to be able to work
[02:00] across the entire corpus of of content
[02:04] on youtube
[02:05] and i think both of those are worthy of
[02:08] discussing and maybe meet in the middle
[02:10] a little bit about the approaches here
[02:12] but i'm just going to kind of brainstorm
[02:14] the various ideas i have around this
[02:17] so initially if you want to do this on a
[02:20] small
[02:21] data set uh how would you recommend the
[02:23] right
[02:24] video to the right user well what you
[02:26] can do is you can start with
[02:28] uh just saying okay what do users
[02:30] initially think
[02:31] about the videos they've seen so you can
[02:35] see uh user a
[02:37] saw video number one and watched uh 100
[02:40] of it a 15 minute video watched all of
[02:42] it
[02:43] and then user b also watched video
[02:45] number one and watched all of it
[02:46] okay so now we can maybe reason that
[02:49] user a
[02:50] and user b uh maybe have similar tastes
[02:53] and so that might be used to predict
[02:55] whether a video that user a
[02:58] watched uh perhaps video two uh
[03:01] watched in its entirety now youtube
[03:04] might recommend
[03:05] that video number two to user b
[03:08] because well we've determined that user
[03:11] b
[03:11] is similar to user a um by some model
[03:15] that i can get into in a bit
[03:16] and we've determined that user a likes
[03:19] video number two so let's recommend
[03:22] video number two
[03:23] to that paired user and similarly if
[03:27] a user doesn't like a video
[03:30] then another user similar to them we
[03:32] might not recommend
[03:33] that video to them so is this technique
[03:36] the
[03:37] uh the collaborative filtering technique
[03:39] where it's based on
[03:40] exactly yeah general neighbors right and
[03:42] so
[03:43] the definition as i know it is that uh
[03:46] users who
[03:47] watch the same thing would likely uh
[03:50] like the similar types of movies and so
[03:53] or videos right so you recommend the
[03:55] same videos that
[03:57] they might have liked and then users who
[03:59] are inherently themselves the same
[04:02] like demographically or something might
[04:04] like the same videos as well
[04:05] right so it's based on activity and then
[04:07] also attributes
[04:09] is that exactly yeah uh yeah and you can
[04:11] take
[04:12] a number of features to put into that
[04:15] model
[04:16] of collaborative filtering user user
[04:18] collaborative filtering
[04:20] we could take the demographics of the
[04:21] user their age and locale
[04:23] we could also take what they what
[04:25] they've been watching
[04:26] and not only what they've been watching
[04:28] like historically did they like this
[04:30] video at some point in time
[04:32] but also waiting more heavily what
[04:34] they've seen recently
[04:35] and i've certainly noticed for myself if
[04:38] i'm watching
[04:38] a series of videos in one topic well
[04:41] guess what the next video recommends to
[04:43] me
[04:44] is gonna be along that topic and i'm
[04:47] sure there's other
[04:48] features going into that but i think
[04:49] it's for the most part
[04:51] uh comparing like for this you know fat
[04:54] corner
[04:55] of the recommendation system uh
[04:58] it's going to be comparing hey this user
[05:00] liked this other video
[05:02] and i like the same things this user
[05:04] does so let's recommend it to them
[05:06] gotcha um
[05:09] sorry this is on a small scale right and
[05:12] so uh this is like youtube when it's
[05:14] very beginning right and so
[05:16] um when you were kind of jumping into it
[05:19] uh i guess one thing i wanted to add was
[05:22] uh how does youtube
[05:23] then kind of start this prediction
[05:25] algorithm
[05:27] if they don't like have any data to like
[05:29] start out with right
[05:30] um because we're assuming that um maybe
[05:33] this is like the very first
[05:34] recommendation ever
[05:36] and so like can you even show anything
[05:39] or
[05:40] uh like basically how would you ever
[05:42] just show anything at all if uh you
[05:44] don't really know what
[05:45] any activity from any of the users uh is
[05:47] in our data set at all
[05:49] sure um so uh in
[05:53] most of my experience uh the the builder
[05:56] of the system is lucky to have
[05:58] you know a corpus of data like 100 users
[06:01] have watched these hundred videos
[06:02] but if that's not available uh perhaps
[06:04] you could use uh some sort of
[06:06] abstraction
[06:07] or a a reference or an approximation
[06:10] that'll be like well
[06:11] you know this is a popular video or this
[06:14] is a recently released video
[06:16] or just have some other metric that'll
[06:18] say this is what we're going to start
[06:19] with recommend
[06:20] recommending videos to these users and
[06:22] then we can
[06:23] shift more towards a user's taste based
[06:26] on how well that initial model performs
[06:28] and you could even use a constantly live
[06:31] updating model
[06:32] to receive feedback as it goes say hey
[06:34] we predicted this video and we were
[06:35] pretty sure you would like it
[06:37] but you didn't watch it okay now we're
[06:39] gonna update our features of this model
[06:41] uh and the next time not recommend a
[06:44] video that we thought you would like for
[06:45] the same reason
[06:47] gotcha okay cool uh awesome
[06:50] so uh the next point that you're going
[06:52] at before i cut you off
[06:54] uh yeah so i am a huge fan
[06:57] uh when building a model like or a
[06:59] system like this to have different
[07:01] models that work to lab together
[07:04] collaboratively as
[07:05] kind of like a symphony that will say
[07:08] hey this model from user user uh
[07:11] collaborative filtering
[07:12] says that you will pre you will predict
[07:14] you will like the video
[07:15] and this other model from item item or
[07:19] like comparing videos to each other
[07:20] rather than comparing users to each
[07:22] other
[07:23] that will predict that this video is
[07:25] similar to another video that you liked
[07:27] not comparing across users but comparing
[07:29] across videos
[07:30] and therefore recommend it to you for
[07:32] that reason okay and so that's a
[07:34] completely different uh parallel perhaps
[07:37] vector we could attack on to say uh
[07:41] yeah this video is similar to this other
[07:42] video you've seen
[07:44] based on the features of the video
[07:47] perhaps the
[07:48] hierarchy of the videos content creator
[07:52] or
[07:52] the tags of the hashtags of the video
[07:55] or the release date or other things like
[07:58] that could be used to compare
[08:00] even if that video has doesn't have many
[08:03] views yet
[08:04] and we can't compare it to a similar
[08:06] user similar to you
[08:07] gotcha okay so uh
[08:11] given this like system if we were to
[08:12] scale it out and let's say that we're
[08:15] now focusing the problem on the youtube
[08:18] of
[08:18] uh 2020 right um how would
[08:22] the kind of problem scope change and
[08:25] how would you like begin to approach the
[08:26] problem because uh now it's like
[08:29] let's say that you just joined youtube
[08:31] and this is like basically your task
[08:33] with building like the new
[08:35] uh you know youtube recommendation
[08:37] system plus algorithm
[08:39] how would you kind of start from that
[08:41] yeah
[08:42] uh so i want to be careful with how i
[08:44] present this
[08:45] because the first thing i want to share
[08:47] is interesting but not necessarily the
[08:50] final solution
[08:51] okay uh so when initially thinking about
[08:54] this you take a user feature vector
[08:57] and condense that down to one dimension
[09:00] and now you have a you have a subset of
[09:03] all the videos on youtube and i'll go
[09:05] into more detail on how we construct
[09:07] which videos we'll compare it with and
[09:09] that subset on
[09:11] videos we will condense that down into a
[09:15] one one dimension matrix uh
[09:18] vector as well and so now we have our
[09:21] output our prediction of
[09:22] will this single user like or should
[09:25] they be recommended
[09:27] this single video we have a one by one
[09:30] multiplication now if we want to scale
[09:32] that out to say hey
[09:34] will this single user like any of these
[09:37] videos in an array
[09:38] if it like if we want to compare it to n
[09:40] videos now we have that one user times
[09:43] an n uh length n that n
[09:46] vectors into a now a 2d matrix yeah okay
[09:50] well now what if we
[09:51] want to speed that up a little bit we
[09:53] can do
[09:54] comparing a number of users to a number
[09:58] of
[09:58] videos and that will save us time
[10:01] because now
[10:03] uh you know we're multiplying a single
[10:05] two matrices together
[10:07] once to get the output for a bunch of
[10:09] users
[10:10] and a bunch of videos but the downside
[10:12] is we still have to perform all those
[10:14] uh computations uh one thing i've found
[10:17] that wasn't initially obvious to me but
[10:19] i think it's worth experimenting with to
[10:21] measure performance
[10:22] is that it is uh using modern day gpus
[10:25] or uh you can use a clever strategy when
[10:28] multiplying these two matrices
[10:30] uh to get much faster results at least
[10:32] than i would expect
[10:34] uh so multiplying two matrices is faster
[10:37] than doing each operation
[10:38] and times if that makes sense it's
[10:41] faster to
[10:41] to combine the problem and do it all at
[10:43] once and
[10:45] you're amortizing the time across all of
[10:47] your users rather than doing it one at a
[10:49] time
[10:49] okay so uh i guess taking a step back
[10:52] here
[10:53] um so we're assuming that there are now
[10:55] let's say
[10:56] uh multi like millions of users right
[11:00] and then millions of videos now right um
[11:02] and so
[11:03] i guess within the frame of the scope is
[11:06] uh
[11:07] is this um potentially the problem for
[11:10] where
[11:10] a new user joins a platform and then
[11:13] sees like the youtube page where they
[11:15] recommended you
[11:16] uh that like eight byte two like kind of
[11:19] youtube panel
[11:20] of different videos you can select or is
[11:21] this more like
[11:23] uh you've watched a video and then you
[11:25] get recommended like another one that
[11:26] auto plays
[11:28] um immediately so i guess in terms of
[11:30] like figuring out the scope
[11:32] um i guess that's probably like first
[11:34] question is um
[11:35] uh which one does that formula kind of
[11:37] apply to
[11:38] or the matrix multiplication yeah yeah
[11:41] uh it's gonna be
[11:42] more applicable to when you've already
[11:44] seen a video you just you've been using
[11:46] youtube for a while
[11:47] you're a user who has been and you have
[11:49] an established
[11:51] uh you know corpus of this is what these
[11:53] are the types of videos i like
[11:55] these are the types of videos i don't
[11:56] like don't interact with
[11:58] and therefore you're able to construct a
[12:02] not quite uni or a distinct 1d
[12:06] user vector so that way we can actually
[12:09] save
[12:10] time by mult by combining many users who
[12:13] have
[12:14] also spent a lot of time on youtube and
[12:17] now we're saying okay
[12:18] for user a do they like video x for user
[12:21] b do they like video y
[12:23] and doing all the same time the opposite
[12:25] side of that problem uh we got a bunch
[12:27] of new users
[12:28] and most of them don't have a lot of
[12:32] well they haven't generated the data for
[12:34] youtube youtube doesn't know quite yet
[12:36] what kind of videos they like that's i'd
[12:39] say a different kind of problem because
[12:40] then you don't have so much data
[12:42] so you could is recommend them videos
[12:45] that new users tend to like
[12:47] or you could just say hey these are the
[12:48] most popular videos across all of them
[12:50] that's maybe good enough um i think
[12:53] those are different approaches but they
[12:54] don't solve
[12:55] the same meat of the problem as what i'm
[12:58] suggesting
[12:59] of combining multiple users in multiple
[13:01] videos in order to amortize your time
[13:04] to come to perform one calculation it's
[13:07] a huge calculation you're multiplying
[13:08] some pretty big matrices
[13:10] um but you're saving time by not doing
[13:13] it one by one
[13:14] gotcha so does that mean that each user
[13:16] then gets bucketed into like a bigger
[13:18] group
[13:19] of users that has that like similar
[13:21] preferences so we can
[13:23] reduce the dimension or is it uh
[13:26] so that's the next thing i want to get
[13:27] into the what i'll call more of a final
[13:29] solution
[13:30] because uh in this initial case we're
[13:33] assuming
[13:33] we can't bucket things yet it's just
[13:36] saying hey we have some raw data
[13:37] bucket and bucketing is not an easy
[13:39] problem so maybe we could iteratively
[13:41] then add bucketing to this as another
[13:44] uh vector of attack uh if our first our
[13:47] first formulations were user user
[13:49] uh collaborative filtering and our
[13:51] second iteration our second
[13:53] component of this uh multi
[13:56] multi-level model is uh item item
[13:59] collaborative filtering
[14:00] and then the third uh the third
[14:03] uh generation technique i want to point
[14:06] out
[14:07] is is what you mentioned reducing
[14:09] dimensions dimensionality of
[14:11] cardinality of the user vector
[14:15] so you can perform uh perhaps
[14:17] unsupervised
[14:18] uh k-means clustering to say hey this is
[14:21] uh this is the type of user that likes
[14:24] uh videos about movies and this is the
[14:26] type of user that likes
[14:28] videos about sports and you can cluster
[14:30] them into two separate buckets
[14:32] similar uh on on a lower dimensional
[14:35] space
[14:36] than the um than the entire user vector
[14:40] similarly actually it turns out you can
[14:44] reduce the cardinality on and map onto
[14:46] the same domain
[14:48] the vector of the feature vector of the
[14:51] videos of the items that you're
[14:52] classifying
[14:53] so that way you can actually take the
[14:57] proximity of a user to
[15:00] a video without having to compare it to
[15:03] any additional models
[15:04] each user outputs is now reduced to a
[15:07] lower dimension that is on the same
[15:09] space
[15:10] as the item or as the video and
[15:12] therefore you can compute
[15:14] the distance and you can compute the
[15:16] likelihood
[15:17] of that this user will like this video
[15:19] just based on distance
[15:21] it becomes a little more complicated
[15:23] when you want to take into account
[15:25] recency of other videos they've seen if
[15:27] i'm watching a lot of
[15:28] you know silly funny compilations or
[15:31] whatever
[15:33] then it'll be more likely to suggest
[15:35] that one next
[15:36] so it might take a a time displaced
[15:40] series of oh yesterday dan liked these
[15:43] kind of videos
[15:44] and today he likes these kind of videos
[15:46] so this is how we're going to weight
[15:47] them differently
[15:48] in the sorting algorithm okay
[15:51] so i guess going back there because i
[15:54] think i got lost for a bit
[15:56] um when you're thinking about the
[15:58] dimensionality
[16:00] is this basically reducing uh
[16:03] a person's like users or features into
[16:05] like some sort of vector
[16:07] kind of in the way that like word devec
[16:09] works in
[16:10] natural language processing where you
[16:11] take like a sentence um
[16:13] or a word and you like basically reduce
[16:16] it into like the similarity between
[16:18] uh different words or is it more so just
[16:21] making
[16:22] like a uh or like i guess like yeah is
[16:25] that
[16:25] kind of a similar idea there um yeah
[16:28] it's definitely a similar idea
[16:29] i'm hesitant to come to compare them
[16:31] directly just because word to vec is so
[16:34] there's a lot to unpack there and i'm
[16:36] sure it contains a lot of
[16:38] a lot of things that i'm overlooking but
[16:40] it's just uh
[16:42] so not only are we reducing cardinality
[16:44] reducing cardinality is
[16:46] is kind of a bonus of this process uh
[16:49] the the
[16:50] main thing i want to get at is that
[16:51] we're mapping the user vector and the
[16:53] item vector onto the same space
[16:55] so that they can be compared directly
[16:57] just using a cartesian distance formula
[17:00] gotcha okay okay that makes sense that
[17:03] makes more
[17:04] sense i think and so uh
[17:07] what would make them i guess comparably
[17:10] similar and what would make them like
[17:11] comparably
[17:12] distant from each other uh what would it
[17:14] feel yeah i guess
[17:16] yeah uh it would be completely tastes of
[17:18] the user and categorization of the item
[17:21] um uh just to back up a little bit i
[17:24] thought of an example so i think
[17:26] uh comparing uh
[17:29] comparing this to word to vec would be
[17:31] similar to
[17:33] mapping a word in one language to evac
[17:36] that maps to the same space as the same
[17:38] word in a different language
[17:39] and you can compare whether or not they
[17:42] are indeed the same word
[17:44] by uh comparing the proximity of those
[17:46] two words
[17:47] onto the word to vac mapped space
[17:50] gotcha if that makes sense okay um
[17:54] yeah uh so now rolling forward
[17:58] uh can you remind me again what uh your
[18:01] your your ass is your question oh yeah
[18:03] so basically now that we've gone this
[18:06] uh kind of like general um comparison
[18:09] are we kind of like finalized are we
[18:11] using that
[18:12] as like the final way to compute um
[18:14] would it
[18:15] scale towards the fact of like uh
[18:18] working for like all these users that
[18:19] have new videos loading up um would it
[18:22] work
[18:23] for our algorithm i guess also in terms
[18:26] of
[18:27] um youtube's like kind of like goal as
[18:30] well in terms of
[18:31] uh you know producing the best content
[18:33] for the user
[18:35] um are there any other considerations
[18:36] that we have to take into place
[18:38] or just general edge cases that might uh
[18:41] come up
[18:42] yeah there's uh two or three that
[18:44] specifically come to mind uh so
[18:47] uh first of all this is that uh
[18:50] the reduction i've done though i've
[18:52] certainly simplified it on there's a lot
[18:54] of edge cases that
[18:55] you know come up as you performing this
[18:57] uh
[18:58] one that comes to mind is what you
[18:59] mentioned about a new user like we don't
[19:01] have a lot of data on this person
[19:03] how do we generate content or how do we
[19:05] recommend content for them
[19:07] but the one of the biggest problems in
[19:09] my mind is how do you do this
[19:10] on a billion videos you can't
[19:14] really map a billion videos onto a
[19:17] cartesian plane and another several
[19:20] hundred million
[19:20] users user profiles onto that same plane
[19:24] and then try to do nearest neighbor
[19:26] algorithms that's not going to scale
[19:27] very well
[19:28] yeah so one thing you could do
[19:32] and there's many ways to do this is
[19:34] filtering
[19:35] what videos get um
[19:38] get generated as candidates to even be
[19:41] possibly
[19:43] put into this real time function i want
[19:46] to get recommendations now
[19:47] so i'll say okay well this video is
[19:50] about sports
[19:51] is sports even remotely close to this
[19:55] user's profile
[19:56] and if so then okay we'll put the bucket
[19:58] of sports videos that
[19:59] hopefully we conveniently have somewhere
[20:02] accessible by
[20:03] hierarchy that map is going to be super
[20:06] complicated but i think
[20:08] that could be the way to do it and now
[20:09] once we've filtered not only do we have
[20:12] a domain of
[20:13] sports videos let's say we can even
[20:15] filter
[20:16] i understand that just random selection
[20:19] has
[20:19] performed quite well in generating uh
[20:22] the recommendations for
[20:24] for any system let's continue relating
[20:26] it to youtube
[20:27] uh so if we just randomly sample the
[20:30] newest sports videos that have been
[20:31] released on youtube in the past
[20:33] six hours and plug a portion of those
[20:36] into our model
[20:37] then we're gonna get some pretty good
[20:38] results in a lot better time than if we
[20:41] put the entire library in or perform an
[20:44] initial
[20:45] calculation uh on on
[20:48] request load um you know just reducing
[20:51] that sample size
[20:52] is going to be crucial for getting this
[20:54] to be performance at all
[20:56] okay and so let's assume that we
[21:00] have like these videos also tagged right
[21:02] like i know users can tag these videos
[21:04] as sports
[21:05] um there's probably like a channel
[21:08] classifier as well where we classify
[21:10] each person's
[21:11] channel into like several categories as
[21:13] well and so we have all these like
[21:15] vectors floating around
[21:16] right um and so once we filtered it down
[21:19] in terms of the recommendation um how do
[21:22] we decide
[21:23] uh i guess what other features do we
[21:26] care about
[21:27] um in terms of uh
[21:30] bringing forward uh like the newest
[21:32] video like
[21:34] uh because i know like we don't want any
[21:36] like random sports video right like if i
[21:39] you know upload a picture like a video
[21:41] of my niece you know hitting a
[21:43] baseball obviously that probably won't
[21:45] be
[21:46] like what people want for like most of
[21:48] their recommendations right and so
[21:50] i'm assuming that there has to be some
[21:52] sort of like general
[21:53] heuristic tier also when it comes to
[21:56] recommending like the next video
[21:58] um that is maybe built off of a model or
[22:01] just built off of general like
[22:03] um kind of heuristics
[22:07] yeah uh so that was exactly the very
[22:09] next thing i was going to mention
[22:11] uh so i i would recommend doing this in
[22:14] two layers
[22:15] having a first uh initial pass filter
[22:18] that will say hey from the entire corpus
[22:20] of videos
[22:21] of billions we're gonna select say maybe
[22:24] a hundred or 200
[22:25] that match the requirements we're
[22:27] looking for
[22:28] and maybe those 100 to 200 will include
[22:31] that video of your niece hitting
[22:32] uh hitting the baseball and maybe it'll
[22:35] include
[22:36] uh you know the currently trending video
[22:38] that is much more likely to actually
[22:40] get get bubbled up onto the user's queue
[22:43] but we're going to return them both just
[22:44] the same at the end of this initial pass
[22:46] filter
[22:47] maybe we'll attach scores to it but
[22:49] that's not so necessary because the
[22:50] second
[22:51] filter the second layer in this model
[22:55] uh will be a what i'll call ranking
[22:58] model
[22:58] and that'll be more rigorous and use the
[23:00] same techniques that i've mentioned
[23:02] before
[23:03] um but it'll actually ha it'll be a much
[23:05] lower corpus so you'll be able to
[23:07] perform the more intense calculations in
[23:09] a performance amount of time
[23:10] on a much lower number of videos 100 or
[23:12] 200 and then it can say okay
[23:15] we will now we have these hundred videos
[23:18] let's cut
[23:19] maybe 50 of them from the list at all
[23:21] and then the next 50 we can actually
[23:22] attach a number to them
[23:23] so they can easily easily be sorted
[23:26] where that number is the likelihood
[23:27] that you will watch the video and
[23:30] something i actually learned
[23:32] while uh while poking around is that
[23:35] youtube
[23:36] apparently wants to not necessarily
[23:38] maximize
[23:39] either the top video or top videos it
[23:41] recommends
[23:42] i understand it doesn't want to
[23:43] necessarily maximize the likelihood that
[23:45] you'll like the video
[23:46] but it wants to maximize your time spent
[23:49] watching
[23:50] the video so if you have a 15 minute
[23:53] video and a five minute video
[23:54] it knows you'll like the five minute
[23:56] video more
[23:58] but you'll probably watch them both in
[24:00] its entirety it'll bubble up that 15
[24:02] minute video
[24:03] higher up the queue and i understand a
[24:05] lot of youtube content creators are
[24:08] or had been i don't know complaining
[24:09] about longer videos get bubbled up
[24:12] on youtube's algorithm more frequently
[24:14] well it does
[24:15] specifically on that ranking step as i
[24:17] understand it but not in the filtering
[24:19] step
[24:19] so sure it'll be recommended to you even
[24:21] if it's a short video but it'll just be
[24:23] much lower down the queue
[24:25] gotcha um that makes a lot of sense and
[24:28] i think it kind of brings up more
[24:30] of why youtube is
[24:33] trying to uh push content because i
[24:36] think
[24:37] uh is there some sort of then metric in
[24:40] which
[24:40] they are finding that like the more um
[24:44] videos or the longer amount of time that
[24:46] you spend watching a video
[24:48] uh the you know the longer that you
[24:51] might stay on the platform
[24:52] for or come back to the platform later
[24:55] um i'm not entirely sure if that's the
[24:57] case
[24:57] but i kind of make sense for how much
[25:00] money youtube could make over time
[25:02] uh given that you know if it only
[25:03] recommended like you know 10 second like
[25:06] tick tock videos then maybe you're gonna
[25:08] quit after like
[25:09] 10 videos versus like one long video
[25:11] that's 20 minutes
[25:13] right exactly exactly it's a measure
[25:15] it's one metric for engage

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
Write JSON only to: splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.json \
    --video transcripts/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.json --out splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.qa-split.json \
    --video transcripts/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.validation-report.md

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
video.md: transcripts/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/video.md

--- CHAPTER `00:55` — Youtube Recommendations Interview Question ---
window: 00:55 .. 03:35
recognition_status: single (1 items)

ITEM #2
  interviewer_question: time=03:33 text="so is this technique the uh the collaborative filtering technique where it's based on"
  candidate_answer: time=03:40 text="exactly yeah general neighbors right and so the definition as i know it is that uh users who watch the same thing would likely uh like the similar types of movies and so or videos right so you recommend the same videos that they might have liked and then users who are inherently themselves the same like demographically or something might like the same videos as well right so it's based on activity and then also attributes is that exactly yeah uh yeah and you can take a number of features to put into that model of collaborative filtering user user collaborative filtering we could take the demographics of the user their age and locale we could also take what they what they've been watching and not only what they've been watching like historically did they like this video at some point in time but also waiting more heavily what they've seen recently and i've certainly noticed for myself if i'm watching a series of videos in one topic well guess what the next video recommends to me is gonna be along that topic and i'm sure there's other features going into that but i think it's for the most part uh comparing like for this you know fat corner of the recommendation system uh it's going to be comparing hey this user liked this other video and i like the same things this user does so let's recommend it to them"
  reference_answer: time=None text=None
  interviewer_feedback: time=05:09 text="gotcha um sorry this is on a small scale right and so uh this is like youtube when it's very beginning right and so"
  question_topic: ML

--- CHAPTER `03:35` — Collaborative Filtering ---
window: 03:35 .. 10:50
recognition_status: multiple (3 items)

ITEM #3
  interviewer_question: time=05:16 text="um when you were kind of jumping into it uh i guess one thing i wanted to add was uh how does youtube then kind of start this prediction algorithm if they don't like have any data to like start out with right um because we're assuming that um maybe this is like the very first recommendation ever and so like can you even show anything or uh like basically how would you ever just show anything at all if uh you don't really know what any activity from any of the users uh is in our data set at all"
  candidate_answer: time=05:49 text="sure um so uh in most of my experience uh the the builder of the system is lucky to have you know a corpus of data like 100 users have watched these hundred videos but if that's not available uh perhaps you could use uh some sort of abstraction or a a reference or an approximation that'll be like well you know this is a popular video or this is a recently released video or just have some other metric that'll say this is what we're going to start with recommend recommending videos to these users and then we can shift more towards a user's taste based on how well that initial model performs and you could even use a constantly live updating model to receive feedback as it goes say hey we predicted this video and we were pretty sure you would like it but you didn't watch it okay now we're gonna update our features of this model uh and the next time not recommend a video that we thought you would like for the same reason"
  reference_answer: time=None text=None
  interviewer_feedback: time=06:47 text='gotcha okay cool uh awesome'
  question_topic: ML

ITEM #4
  interviewer_question: time=06:50 text="so uh the next point that you're going at before i cut you off"
  candidate_answer: time=06:54 text="uh yeah so i am a huge fan uh when building a model like or a system like this to have different models that work to lab together collaboratively as kind of like a symphony that will say hey this model from user user uh collaborative filtering says that you will pre you will predict you will like the video and this other model from item item or like comparing videos to each other rather than comparing users to each other that will predict that this video is similar to another video that you liked not comparing across users but comparing across videos and therefore recommend it to you for that reason okay and so that's a completely different uh parallel perhaps vector we could attack on to say uh yeah this video is similar to this other video you've seen based on the features of the video perhaps the hierarchy of the videos content creator or the tags of the hashtags of the video or the release date or other things like that could be used to compare even if that video has doesn't have many views yet and we can't compare it to a similar user similar to you"
  reference_answer: time=None text=None
  interviewer_feedback: time=08:07 text='gotcha okay so uh'
  question_topic: ML

ITEM #5
  interviewer_question: time=08:11 text="given this like system if we were to scale it out and let's say that we're now focusing the problem on the youtube of uh 2020 right um how would the kind of problem scope change and how would you like begin to approach the problem because uh now it's like let's say that you just joined youtube and this is like basically your task with building like the new uh you know youtube recommendation system plus algorithm how would you kind of start from that"
  candidate_answer: time=08:42 text="yeah uh so i want to be careful with how i present this because the first thing i want to share is interesting but not necessarily the final solution okay uh so when initially thinking about this you take a user feature vector and condense that down to one dimension and now you have a you have a subset of all the videos on youtube and i'll go into more detail on how we construct which videos we'll compare it with and that subset on videos we will condense that down into a one one dimension matrix uh vector as well and so now we have our output our prediction of will this single user like or should they be recommended this single video we have a one by one multiplication now if we want to scale that out to say hey will this single user like any of these videos in an array if it like if we want to compare it to n videos now we have that one user times an n uh length n that n vectors into a now a 2d matrix yeah okay well now what if we want to speed that up a little bit we can do comparing a number of users to a number of videos and that will save us time because now uh you know we're multiplying a single two matrices together once to get the output for a bunch of users and a bunch of videos but the downside is we still have to perform all those uh computations uh one thing i've found that wasn't initially obvious to me but i think it's worth experimenting with to measure performance is that it is uh using modern day gpus or uh you can use a clever strategy when multiplying these two matrices uh to get much faster results at least than i would expect uh so multiplying two matrices is faster than doing each operation and times if that makes sense it's faster to to combine the problem and do it all at once and you're amortizing the time across all of your users rather than doing it one at a time"
  reference_answer: time=None text=None
  interviewer_feedback: time=10:49 text='okay so uh i guess taking a step back here'
  question_topic: ML

--- CHAPTER `10:50` — Cold Start Problem? ---
window: 10:50 .. конец
recognition_status: multiple (7 items)

ITEM #6
  interviewer_question: time=10:53 text="um so we're assuming that there are now let's say uh multi like millions of users right and then millions of videos now right um and so i guess within the frame of the scope is uh is this um potentially the problem for where a new user joins a platform and then sees like the youtube page where they recommended you uh that like eight byte two like kind of youtube panel of different videos you can select or is this more like uh you've watched a video and then you get recommended like another one that auto plays um immediately so i guess in terms of like figuring out the scope um i guess that's probably like first question is um uh which one does that formula kind of apply to or the matrix multiplication"
  candidate_answer: time=11:38 text="yeah yeah uh it's gonna be more applicable to when you've already seen a video you just you've been using youtube for a while you're a user who has been and you have an established uh you know corpus of this is what these are the types of videos i like these are the types of videos i don't like don't interact with and therefore you're able to construct a not quite uni or a distinct 1d user vector so that way we can actually save time by mult by combining many users who have also spent a lot of time on youtube and now we're saying okay for user a do they like video x for user b do they like video y and doing all the same time the opposite side of that problem uh we got a bunch of new users and most of them don't have a lot of well they haven't generated the data for youtube youtube doesn't know quite yet what kind of videos they like that's i'd say a different kind of problem because then you don't have so much data so you could is recommend them videos that new users tend to like or you could just say hey these are the most popular videos across all of them that's maybe good enough um i think those are different approaches but they don't solve the same meat of the problem as what i'm suggesting of combining multiple users in multiple videos in order to amortize your time to come to perform one calculation it's a huge calculation you're multiplying some pretty big matrices um but you're saving time by not doing it one by one"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #7
  interviewer_question: time=13:14 text='gotcha so does that mean that each user then gets bucketed into like a bigger group of users that has that like similar preferences so we can reduce the dimension or is it uh'
  candidate_answer: time=13:26 text="so that's the next thing i want to get into the what i'll call more of a final solution because uh in this initial case we're assuming we can't bucket things yet it's just saying hey we have some raw data bucket and bucketing is not an easy problem so maybe we could iteratively then add bucketing to this as another uh vector of attack uh if our first our first formulations were user user uh collaborative filtering and our second iteration our second component of this uh multi multi-level model is uh item item collaborative filtering and then the third uh the third uh generation technique i want to point out is is what you mentioned reducing dimensions dimensionality of cardinality of the user vector so you can perform uh perhaps unsupervised uh k-means clustering to say hey this is uh this is the type of user that likes uh videos about movies and this is the type of user that likes videos about sports and you can cluster them into two separate buckets similar uh on on a lower dimensional space than the um than the entire user vector similarly actually it turns out you can reduce the cardinality on and map onto the same domain the vector of the feature vector of the videos of the items that you're classifying so that way you can actually take the proximity of a user to a video without having to compare it to any additional models each user outputs is now reduced to a lower dimension that is on the same space as the item or as the video and therefore you can compute the distance and you can compute the likelihood of that this user will like this video just based on distance it becomes a little more complicated when you want to take into account recency of other videos they've seen if i'm watching a lot of you know silly funny compilations or whatever then it'll be more likely to suggest that one next so it might take a a time displaced series of oh yesterday dan liked these kind of videos and today he likes these kind of videos so this is how we're going to weight them differently in the sorting algorithm"
  reference_answer: time=None text=None
  interviewer_feedback: time=15:48 text='okay'
  question_topic: ML

ITEM #8
  interviewer_question: time=15:51 text="so i guess going back there because i think i got lost for a bit um when you're thinking about the dimensionality is this basically reducing uh a person's like users or features into like some sort of vector kind of in the way that like word devec works in natural language processing where you take like a sentence um or a word and you like basically reduce it into like the similarity between uh different words or is it more so just making like a uh or like i guess like yeah is that kind of a similar idea there"
  candidate_answer: time=16:25 text="um yeah it's definitely a similar idea i'm hesitant to come to compare them directly just because word to vec is so there's a lot to unpack there and i'm sure it contains a lot of a lot of things that i'm overlooking but it's just uh so not only are we reducing cardinality reducing cardinality is is kind of a bonus of this process uh the the main thing i want to get at is that we're mapping the user vector and the item vector onto the same space so that they can be compared directly just using a cartesian distance formula"
  reference_answer: time=None text=None
  interviewer_feedback: time=17:00 text='gotcha okay okay that makes sense that makes more sense i think and so uh'
  question_topic: ML

ITEM #9
  interviewer_question: time=17:07 text='what would make them i guess comparably similar and what would make them like comparably distant from each other uh what would it feel yeah i guess'
  candidate_answer: time=17:16 text='yeah uh it would be completely tastes of the user and categorization of the item um uh just to back up a little bit i thought of an example so i think uh comparing uh comparing this to word to vec would be similar to mapping a word in one language to evac that maps to the same space as the same word in a different language and you can compare whether or not they are indeed the same word by uh comparing the proximity of those two words onto the word to vac mapped space'
  reference_answer: time=None text=None
  interviewer_feedback: time=17:50 text='gotcha if that makes sense okay um yeah uh so now rolling forward'
  question_topic: ML

ITEM #10
  interviewer_question: time=18:03 text="so basically now that we've gone this uh kind of like general um comparison are we kind of like finalized are we using that as like the final way to compute um would it scale towards the fact of like uh working for like all these users that have new videos loading up um would it work for our algorithm i guess also in terms of um youtube's like kind of like goal as well in terms of uh you know producing the best content for the user um are there any other considerations that we have to take into place or just general edge cases that might uh come up"
  candidate_answer: time=18:42 text="yeah there's uh two or three that specifically come to mind uh so uh first of all this is that uh the reduction i've done though i've certainly simplified it on there's a lot of edge cases that you know come up as you performing this uh one that comes to mind is what you mentioned about a new user like we don't have a lot of data on this person how do we generate content or how do we recommend content for them but the one of the biggest problems in my mind is how do you do this on a billion videos you can't really map a billion videos onto a cartesian plane and another several hundred million users user profiles onto that same plane and then try to do nearest neighbor algorithms that's not going to scale very well yeah so one thing you could do and there's many ways to do this is filtering what videos get um get generated as candidates to even be possibly put into this real time function i want to get recommendations now so i'll say okay well this video is about sports is sports even remotely close to this user's profile and if so then okay we'll put the bucket of sports videos that hopefully we conveniently have somewhere accessible by hierarchy that map is going to be super complicated but i think that could be the way to do it and now once we've filtered not only do we have a domain of sports videos let's say we can even filter i understand that just random selection has performed quite well in generating uh the recommendations for for any system let's continue relating it to youtube uh so if we just randomly sample the newest sports videos that have been released on youtube in the past six hours and plug a portion of those into our model then we're gonna get some pretty good results in a lot better time than if we put the entire library in or perform an initial calculation uh on on request load um you know just reducing that sample size is going to be crucial for getting this to be performance at all"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #11
  interviewer_question: time=21:00 text="okay and so let's assume that we have like these videos also tagged right like i know users can tag these videos as sports um there's probably like a channel classifier as well where we classify each person's channel into like several categories as well and so we have all these like vectors floating around right um and so once we filtered it down in terms of the recommendation um how do we decide uh i guess what other features do we care about um in terms of uh bringing forward uh like the newest video like uh because i know like we don't want any like random sports video right like if i you know upload a picture like a video of my niece you know hitting a baseball obviously that probably won't be like what people want for like most of their recommendations right and so i'm assuming that there has to be some sort of like general heuristic tier also when it comes to recommending like the next video um that is maybe built off of a model or just built off of general like um kind of heuristics"
  candidate_answer: time=22:07 text="yeah uh so that was exactly the very next thing i was going to mention uh so i i would recommend doing this in two layers having a first uh initial pass filter that will say hey from the entire corpus of videos of billions we're gonna select say maybe a hundred or 200 that match the requirements we're looking for and maybe those 100 to 200 will include that video of your niece hitting uh hitting the baseball and maybe it'll include uh you know the currently trending video that is much more likely to actually get get bubbled up onto the user's queue but we're going to return them both just the same at the end of this initial pass filter maybe we'll attach scores to it but that's not so necessary because the second filter the second layer in this model uh will be a what i'll call ranking model and that'll be more rigorous and use the same techniques that i've mentioned before um but it'll actually ha it'll be a much lower corpus so you'll be able to perform the more intense calculations in a performance amount of time on a much lower number of videos 100 or 200 and then it can say okay we will now we have these hundred videos let's cut maybe 50 of them from the list at all and then the next 50 we can actually attach a number to them so they can easily easily be sorted where that number is the likelihood that you will watch the video and something i actually learned while uh while poking around is that youtube apparently wants to not necessarily maximize either the top video or top videos it recommends i understand it doesn't want to necessarily maximize the likelihood that you'll like the video but it wants to maximize your time spent watching the video so if you have a 15 minute video and a five minute video it knows you'll like the five minute video more but you'll probably watch them both in its entirety it'll bubble up that 15 minute video higher up the queue and i understand a lot of youtube content creators are or had been i don't know complaining about longer videos get bubbled up on youtube's algorithm more frequently well it does specifically on that ranking step as i understand it but not in the filtering step so sure it'll be recommended to you even if it's a short video but it'll just be much lower down the queue"
  reference_answer: time=None text=None
  interviewer_feedback: time=24:25 text='gotcha um that makes a lot of sense and i think it kind of brings up more of why youtube is'
  question_topic: ML

ITEM #12
  interviewer_question: time=24:33 text="trying to uh push content because i think uh is there some sort of then metric in which they are finding that like the more um videos or the longer amount of time that you spend watching a video uh the you know the longer that you might stay on the platform for or come back to the platform later um i'm not entirely sure if that's the case"
  candidate_answer: time=25:13 text="right exactly exactly it's a measure it's one metric for engage"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Product Metrics

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/interview-query/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26/ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
