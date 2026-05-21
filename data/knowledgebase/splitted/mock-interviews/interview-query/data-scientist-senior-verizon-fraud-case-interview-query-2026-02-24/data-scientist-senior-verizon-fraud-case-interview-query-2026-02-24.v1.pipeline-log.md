<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24",
  "transcript_folder": "transcripts/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24",
  "source_id": "data_scientist_senior_verizon_fraud_case_interview_query_2026_02_24",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:18:03 +0200",
  "updated_at": "2026-05-20 21:32:24 +0200",
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
    "json": "splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/timecodes.txt",
        "en",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.pipeline-log.md"
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
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:32:23 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:32:24 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24`
- **Source ID:** `data_scientist_senior_verizon_fraud_case_interview_query_2026_02_24`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:18:03 +0200
- **Last updated:** 2026-05-20 21:32:24 +0200

Фильтр в IDE: `*data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/timecodes.txt`<br>`en`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.pipeline-log.md` | — | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.validation-report.md` | 1.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.pipeline-log.md`

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
SOURCE_ID: data_scientist_senior_verizon_fraud_case_interview_query_2026_02_24
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24
INTERVIEW_LANGUAGE: en
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00] How are you still distinguishing between
[00:02] like actual fraud and abuse versus just
[00:05] like normal, you know, high usage
[00:08] because, you know, it's 8:00 p.m. now
[00:09] and, you know, I'm an individual user
[00:11] and now I'm like streaming, you know,
[00:13] Netflix.
[00:16] So, the first question is, let's say
[00:19] that Verizon launches a wireless plan
[00:21] that offers unlimited data after 8:00
[00:23] p.m. each night, and you notice some
[00:26] customers are suddenly using 10x more
[00:28] data during that window than the average
[00:30] user. How would you distinguish between
[00:32] fraud and product abuse in this
[00:34] scenario? And how might your findings
[00:35] shape future product or policy
[00:37] decisions?
[00:39] So just to clarify, we are assuming that
[00:42] this spike is only during like post 8:00
[00:45] p.m. and during the unlimited window or
[00:48] does it also extend into regular paid
[00:50] hours?
[00:51] >> Yeah, let's say that this is
[00:52] specifically um happening uh after the
[00:56] 8:00 p.m. window.
[00:58] >> Okay. All right. So the first thing I
[01:01] I'd say is uh in that case I'd start by
[01:04] clarifying whether the spike represents
[01:06] deliberate manipulation or just users uh
[01:10] maximizing within the plan's rules. Uh
[01:12] then I analyze basically user level
[01:15] patterns like device sharing unusual
[01:17] location changes or VPN uh usage uh to
[01:22] separate basically genuine heavy users
[01:24] from potential frauds.
[01:27] Uh the second basically this is like the
[01:30] aspect that I'll investigate. So fraud
[01:33] for example fraudulent users
[01:36] like fraudinal users then I'd segment
[01:39] accounts by usage intensity and behavior
[01:42] patterns to basically compare them
[01:44] against um like normal baselines that we
[01:47] have seen across uh a historical trend
[01:50] just to basically flag statistically
[01:51] significant outliers for deeper. So
[01:54] wait, what what are fraudulent users?
[01:56] Can you go back and maybe define that
[01:58] first?
[02:00] >> Sure. So the key like the key metrics
[02:03] that I'd use like to understand what are
[02:06] fraud who are fraud like basically
[02:08] fraudsters are those exploiting the plan
[02:11] beyond the intended use like reselling
[02:14] the bandwidth to people like by sharing
[02:16] the internet tethering to like multiple
[02:19] devices or using automation or VPN
[02:22] setups to bypass limits rather than just
[02:24] consuming more data personally. So
[02:27] basically sharing data with multiple
[02:30] users is the biggest signal
[02:33] uh with respect to how fraudsters do use
[02:35] this and how we can see this is I I
[02:38] believe a telecom companies have access
[02:41] to where uh that particular data is
[02:44] being shared to and to what IP address.
[02:46] So if there are multiple IP addresses
[02:48] where that data is being shared to that
[02:51] means that there could be some
[02:52] fraudulent usage over here. What I mean
[02:55] by multiple is much more above than 10.
[02:58] So the account is likely being used to
[02:59] distribute data externally rather than
[03:01] for personal use.
[03:03] >> Okay. And what's the net consequence of
[03:06] fraudulent usage here? Just so that
[03:09] maybe we have a definition and an
[03:11] understanding of what the business
[03:12] impact
[03:14] uh is and why it even matters.
[03:17] >> Sure. So the net consequence I see over
[03:20] here is the revenue leakage and network
[03:22] strain because since these users consume
[03:24] disproportionate amount of bandwidth
[03:27] without paying more which can degrade
[03:30] the service quality for other users and
[03:32] reduce profitability on that plan as
[03:34] well. So that's I would say that's the
[03:36] primary
[03:38] u business impact that would have like
[03:40] over because within a telecom
[03:42] architecture customer feedback or
[03:44] customer experience really matters as if
[03:48] they I mean on a day-to-day basis as
[03:51] well I would say that if we have a drop
[03:53] in the data data speed or services we
[03:57] usually tend to go to our friends or we
[03:59] tend to ask them that hey how is your
[04:01] internet working and if it happened to
[04:03] be that they're on another network and
[04:04] it's working then there's an incentive
[04:07] for me to move to that network as well
[04:09] given that most of the other
[04:11] characteristics of the plan are same so
[04:14] I'd have to switch networks which
[04:16] directly impacts churn and long-term
[04:18] customer retention
[04:20] >> I see okay so we know that it's bad
[04:22] because of those reasons right you're
[04:24] saying uh it affects people also in the
[04:27] network right that are not fraudulent
[04:29] right there's also the aspect of um
[04:33] potentially we gave them this 8:00 p.m.,
[04:35] you know, 10x plan, right? And they feel
[04:37] like they're being throttled
[04:39] potentially, which means like, you know,
[04:40] the policy doesn't actually work, right?
[04:42] It's like, oh, I was promised, you know,
[04:45] unlimited data, but then it's like being
[04:47] throttled and it's not very good and so,
[04:50] uh, I'm just going to switch to, you
[04:51] know, AT&T instead of Verizon, right?
[04:54] Okay, there's that. And then is there
[04:56] also a cost aspect or is that not really
[04:58] an issue you think with Verizon?
[05:01] >> Right. like when I would say that the
[05:04] cost aspect does come into play also
[05:07] because for example if there are too
[05:09] many legitimate fe uh users that feel
[05:12] throttled um by the plan design itself
[05:16] and basically basically making the
[05:18] adjustment by capping extreme outliers.
[05:20] So there's definitely a cost aspect for
[05:24] like two since higher nighttime usage
[05:26] increases uh network load infrastructure
[05:30] costs like bandwidth maintenance and
[05:32] without corresponding revenue growth
[05:34] right so definitely there's a cost uh
[05:36] there's a cost driver here as well uh
[05:39] with respect to the telecom
[05:40] infrastructure like we would have to
[05:42] invest in more uh route not routers but
[05:45] basically networks in order to ensure
[05:48] for example uh maximum minimum
[05:50] connectivity or basically ensuring
[05:52] additional capacity uh to provision that
[05:55] surge.
[05:56] >> Okay, got it. So we understand the net
[06:00] benefits sorry we understand the net
[06:02] consequences here of actually you know
[06:05] why we want to do this. So, let's dive
[06:08] back into you said that there's a couple
[06:10] different ways that you can investigate,
[06:11] right? You can look at device sharing,
[06:13] you can look at, you know, um traffic
[06:16] signatures, VPN, uh tethering, other
[06:19] things like that. Um what else can we
[06:22] kind of do? And then once you're given
[06:24] all these different usage patterns, what
[06:26] actually like would you do in a certain
[06:29] scenario, right? like how would you
[06:31] actually like basically I would say
[06:35] answer the question and um you know what
[06:38] would you actually implement in this
[06:39] case depending on different scenarios
[06:42] >> uh we could also implement I mean we all
[06:45] like I mentioned the earlier aspects but
[06:47] um we could also implement real-time
[06:49] monitoring rules like flagging as soon
[06:52] as there's a traffic spike beyond
[06:54] expected human behavior um repeated
[06:57] device uh authentication failure
[07:01] or adapt the product policies based on
[07:03] whether the dominant pattern is abuse or
[07:05] actual fraud. For example, if we are
[07:09] seeing regular usage of like 30GB
[07:13] okay and
[07:15] the plan right now we we assume that uh
[07:18] the course of in within this course of
[07:20] time we saw that uh it was 20GB usually.
[07:23] So we might we could also further think
[07:26] whether we see like this whether this
[07:29] jump uh within the same window is is a
[07:33] sudden jump or whether it's a deviation
[07:34] that would trigger an alert for review
[07:37] to check if uh it's a legitimate usage
[07:39] or it's potential misuse. So primarily I
[07:42] would say real time monitoring is
[07:45] something that should be given more
[07:47] emphasis because a lot of companies do
[07:48] have access to that. The only problem
[07:50] with that is when it comes to real-time
[07:52] monitoring the cost associated to create
[07:56] a real time platform is much expensive
[07:59] because telecom companies usually get
[08:02] these services from other uh third party
[08:05] providers like one example is Huawei
[08:08] another example is um I think mobile
[08:12] um these are few companies basically
[08:15] that allow you to get realtime insights
[08:18] from your systems because when you
[08:20] upgrade to a better system definitely
[08:22] you'll have the reports being generated
[08:24] on a more regular basis. So again
[08:27] there's a cost associated to it. So the
[08:29] infrastructure tier those providers
[08:31] charge significantly more for continuous
[08:33] data streaming and low latency
[08:35] processing which is why many telecoms
[08:37] still rely on batch analysis instead of
[08:39] full realtime systems let's say. Okay, I
[08:43] understand that. But I guess there's
[08:44] still kind of this question of like how
[08:46] are you still distinguishing between
[08:48] like actual fraud and abuse versus just
[08:51] like normal, you know, high usage
[08:53] because, you know, it's 8:00 p.m. now
[08:55] and, you know, I'm an individual user
[08:57] and now I'm like streaming, you know,
[08:59] Netflix, right, at night and uh I get an
[09:02] alert that, you know, I can now stream
[09:04] Netflix uh right um at like, you know,
[09:07] 4K or something like that, right? So
[09:09] you're you have all this data right and
[09:12] you have all these like heruristics that
[09:13] you were mentioning right but how are
[09:16] you actually like determining you know
[09:18] the actual usage here and what's
[09:20] actually abuse and what's not
[09:23] >> right so I would say like per system
[09:26] metrics so so to me like there are
[09:29] certain metrics that we'll have to track
[09:31] that includes for example precision
[09:33] whether the true fraud flags um
[09:36] basically comparing the true fraud flags
[09:38] with the total uh total flagged amounts,
[09:41] the recall rate and the false positive
[09:44] rate as well at the same time. So these
[09:47] these particular metrics would at least
[09:49] help us understand whether like for
[09:52] example false positive rate which
[09:54] basically measures how many legitimate
[09:55] users were incorrectly flagged. So
[09:58] balancing these three helps fine-tune
[10:00] thresholds and improve uh like uh
[10:03] improve the overall model reliability
[10:05] because there's no there's no like we
[10:07] cannot we can never within like within
[10:10] the architecture we are operating in in
[10:11] my opinion uh there's always a tra
[10:14] trade-off between catching more fraud
[10:16] and keeping customer experience smooth.
[10:18] So finding the balance is the key to
[10:20] maintaining both trust and efficiency.
[10:22] So maintaining all these three like
[10:24] these three parameters that I mentioned
[10:27] about system performing metrics such as
[10:30] precision, recall and false positive
[10:32] rate. All
[10:33] >> what goes into those? Right. Cuz I have
[10:36] no idea what how you catch like a false
[10:39] positive or how you even know that it is
[10:42] positive. Right.
[10:43] >> Right.
[10:43] >> You've said that there's maybe device
[10:45] sharing and there's VPN use, but like
[10:48] you know normal people use VPNs anyway.
[10:50] So, is this like um someone switching a
[10:53] VPN like multiple times and then you
[10:56] investigate and then you determine it's
[10:58] fraud, let's say. How do you know it's
[11:00] fraud, right? What if it's just a normal
[11:02] user just switching VPNs all the time?
[11:04] Like, do you have a designation for what
[11:06] fraud is in this case?
[11:08] >> Yeah. So
[11:11] I'd say that we only classify it as a
[11:16] fraud if VPN switching coincides with
[11:19] other red flags like simultaneous login
[11:22] from locations like multiple locations
[11:25] because we have a geo flag also that
[11:27] basically identifies from which location
[11:29] this is being accessed or whether data
[11:32] whether the data is being routed to
[11:34] multiple external IPs basically
[11:36] indicating coordinated misuse rather
[11:39] than normal privacy behavior. And coming
[11:42] back to what I mentioned earlier about
[11:44] um so the precision me like what what
[11:46] precision measures is how many of the
[11:49] flagged cases were actually fraud.
[11:52] Recall basically would measure how many
[11:54] total fraud cases we have successfully
[11:56] caught in the in I would say in terms of
[11:59] his historical data and the false
[12:01] positive rate would basically measure
[12:03] how many users were incorrect
[12:05] incorrectly charged. So what manually
[12:08] goes into this is a false positive. We
[12:10] had manually review a flagged account
[12:12] using additional context like billing
[12:13] history, device consistency, prior
[12:17] complaint rec records since VPN use
[12:20] alone isn't enough. So it's a
[12:23] combination of multiple anomal sorry
[12:26] anomalies that um that uh signals real
[12:31] real fraud. So,
[12:32] >> but you're basically building that model
[12:34] off of something, right? Like you can't
[12:37] just just have those heruristics and
[12:40] then call it fraud, right? Someone
[12:42] likely is going in
[12:44] >> and they probably view the activity
[12:46] history
[12:48] >> for like a customer over like 15 minutes
[12:51] and they do all this work, right? And
[12:53] they're like, "All right, this is
[12:55] definitely fraud, right?" And my
[12:57] internal model is just saying that,
[12:59] right? But additionally, what you're
[13:01] saying is that like all that stuff can't
[13:03] really be done in real time because it's
[13:05] extremely difficult, right? And so, um,
[13:09] just because they use like, you know, an
[13:11] above average amount of gigabytes of
[13:13] data doesn't mean that it's like
[13:14] automatically fraud, right? There has to
[13:16] be like
[13:17] >> a signal that then kind of has the
[13:19] person go in and do the investigative
[13:21] work, which evidently takes a lot of
[13:24] time,
[13:25] >> right?
[13:27] It does because that's where the
[13:28] costsensitive approach helps by
[13:31] basically weighing high value fraud more
[13:33] heavily in the model's loss function and
[13:35] then we can afford a few extra false
[13:37] positives on low value like on low value
[13:41] cases while ensuring expensive frauds
[13:43] are definitely caught early. So the goal
[13:45] here is to go go big or go home um idly
[13:50] because if we catch the bigger frauds,
[13:52] we're idly preventing
[13:55] a greater like the bigger loss or the
[13:58] bigger picture instead of catching the
[14:01] um the the lower ones because if it
[14:03] means like basically the extra false
[14:06] positives on low value cases if it means
[14:08] catching the high impact frauds earlier
[14:11] and reducing overall financial loss. So
[14:14] we protect a larger portion of revenue
[14:17] and then we can justify the
[14:18] investigation cost also whereas missing
[14:20] them would have had a dispos
[14:22] disproportionate
[14:24] um financial impact.
[14:27] >> Okay. So let's just talk about the
[14:29] product and policy side
[14:31] >> now and uh just kind of quickly
[14:33] summarize you know the last bit of the
[14:35] question was you know how would your
[14:37] findings actually shape future product
[14:39] or policy decisions here?
[14:43] Mhm.
[14:44] >> I just like a moment just to uh bring
[14:47] all the parts together.
[14:50] >> Yeah. So I think these findings would
[14:52] basically guide policy updates like
[14:55] introducing fair use gaps uh revising
[14:59] plan eligibility like how you whether
[15:01] you're eligible for this unlimited plan
[15:03] for example or adding tiered pricing for
[15:07] heavy users. And on the product side
[15:09] basically they inform clear
[15:11] communication about limits to manage
[15:13] expectations and reduce the churn. So
[15:16] one of the main one of the main things I
[15:18] would say on policy transformation is
[15:20] like how we are looking at this how we
[15:23] looking at a user to be eligible for
[15:26] this particular plan like that really
[15:28] matters and that would ideally be
[15:31] witnessed or basically checked through
[15:33] their historical behavior and for
[15:36] example if it's a new user then this
[15:38] plan should not be in like for a new
[15:41] user this should not exactly be a plan
[15:43] that should be immediately offered and
[15:45] if it is And uh a lot of companies have
[15:47] this uh have this have this model which
[15:51] is known as like a three-month program.
[15:53] For example, Mint Mint has Mint has this
[15:56] program where they have a 3month um
[15:58] discounted uh unlimited data program for
[16:01] the first 3 months. And after the first
[16:04] 3 months they have these catered
[16:07] um like basically what they do is that
[16:09] they check they look at the customer
[16:11] behavior uh whether their usage in these
[16:15] three months was within what tier and
[16:19] based on that they would suggest that
[16:20] tier or they would push that tier to
[16:22] that customer in the most effective way
[16:25] by campaigning it through a little um
[16:28] little lower than the market price or
[16:31] provide additional benefits. It's like
[16:33] maybe
[16:34] five international calls per month
[16:37] ideally just to incentivize the customer
[16:40] to focus on the particular plan that
[16:42] they would like them like or basically a
[16:44] bonus that they would like uh the
[16:47] customer to uh to basically re retain
[16:51] towards while aligning usage with the
[16:54] right plan tier.
[16:56] >> Okay, got it. Um, all right. So, I'm
[17:00] going to give you some feedback on this
[17:01] because I actually think that'd be
[17:02] helpful for the overall like
[17:06] understanding here and for our audiences
[17:08] kind of watching
[17:09] >> on YouTube. Um, so first off, I want to
[17:13] ask you like what do you think you did
[17:14] well? What do you think you did badly in
[17:16] this interview?
[17:18] I'd say that I think I have all the
[17:21] knowledge but I like um a little a
[17:24] little bit of my structuring was um was
[17:29] going off course at times I would say
[17:31] because in the end how you present the
[17:34] solution is what matters more than how I
[17:39] basically but how I I could have been
[17:40] more concise in a few parts and tied my
[17:42] examples back to the main question
[17:44] faster just to be in a short in a
[17:46] shorter note.
[17:48] Yeah. Yeah. I would say that's um very
[17:52] very uh good analysis there, right?
[17:55] Because I think the one thing that I was
[17:57] pushing you in the very beginning was
[17:59] like defining what the key terms are
[18:01] because that's always kind of the
[18:03] problem with most interviews is that
[18:05] people have different understandings of
[18:08] what the definitions are, right? What
[18:10] does fraud mean, right? in this example,
[18:12] what does uh like product uh high
[18:16] product usage mean for example? And then
[18:19] what's the downsides in both cases,
[18:21] right? Like why are we doing this thing?
[18:24] Like what is the point of actually
[18:27] investigating into this, right? Because
[18:29] if we put our time and energy into
[18:31] investigating something, there's
[18:32] obviously some sort of like, you know,
[18:34] money that we're being paid to look into
[18:37] this, right? and a business case for
[18:39] like why we care about you know
[18:41] implementing something like this right
[18:43] so marketing at the end of the day or
[18:45] the product team right at the end of the
[18:47] day is creating like a unlimited data
[18:49] after 8 p.m. night and at the end of the
[18:51] day it's also about like costs right
[18:54] like we are doing this to acquire new
[18:56] customers likely or to incentivize their
[18:58] existing customers to stay with us with
[19:00] Verizon but at the same time we want to
[19:02] minimize the cost and fraudulent users
[19:05] likely are creating bad experiences as
[19:07] you said really well right for other
[19:09] users on telecom networks right but also
[19:12] um they're probably racking up you know
[19:14] costs of data usage that's not just free
[19:17] right uh and so like really defining
[19:19] that is kind of like the center point to
[19:22] everything. And I think you really need
[19:23] to emphasize that a lot more in the very
[19:25] beginning. And then really coming to
[19:29] like a concrete conclusion as well in
[19:31] terms of a solution is then really the
[19:34] second point that um really needs to be
[19:37] done, right? This means like actually
[19:38] providing examples of like showcasing
[19:41] the differences between fraud and like
[19:43] what regular product I product usage
[19:45] looks like and what normal behavior
[19:46] looks like and then showcasing you know
[19:49] if fraud was XYZ then we do this if
[19:52] fraud is actually uh ABC then we do that
[19:56] right um and so I think one of the tough
[19:59] things here about solo was like you
[20:01] didn't kind of come to like a definitive
[20:03] like this is what we should be doing you
[20:06] know and you know it's obviously hard in
[20:07] an open-ended question, but the easiest
[20:09] way to do that in an open-ended question
[20:11] is to actually have like a 100% like
[20:15] illustrated example that you can
[20:17] essentially explain to the interviewer
[20:22] that then um you know within that
[20:25] example you can easily kind of be like
[20:27] all right and this is like the best
[20:28] solution for right so I think that's the
[20:32] major improvement that kind of needs to
[20:33] be done in terms of a structured
[20:35] perspective
[20:36] um in terms of like really feeling like
[20:39] a takeaway that like you know this is a
[20:41] great solution and you like really
[20:42] understand the material here
[20:45] >> that makes sense. I mean having a
[20:47] concrete illustrated example would make
[20:49] it easier to anchor my reasoning and
[20:52] basically also show exactly how the
[20:55] decision process works in practice. So
[20:59] like having a flowchart like approach
[21:01] basically the first this is how the
[21:04] business case was defined what would the
[21:06] model score this risk whether if it's
[21:09] low medium or high and based on that the
[21:12] different investigations that would
[21:13] require so definitely a structured
[21:15] approach to it would create a higher
[21:18] business impact and um focus more
[21:22] towards the recommended actions.
[21:25] Yeah, absolutely.
[21:27] Okay, cool. Talk to you later.
[21:29] >> Thank you so much. Have a good day.

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
Write JSON only to: splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.json \
    --video transcripts/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.json --out splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.qa-split.json \
    --video transcripts/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.validation-report.md

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
video.md: transcripts/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/video.md

--- CHAPTER `00:00` — Verizon fraud case mock interview ---
window: 00:00 .. конец
recognition_status: multiple (10 items)

ITEM #1
  interviewer_question: time=00:16 text="So, the first question is, let's say that Verizon launches a wireless plan that offers unlimited data after 8:00 p.m. each night, and you notice some customers are suddenly using 10x more data during that window than the average user. How would you distinguish between fraud and product abuse in this scenario? And how might your findings shape future product or policy decisions?"
  candidate_answer: time=00:39 text="So just to clarify, we are assuming that this spike is only during like post 8:00 p.m. and during the unlimited window or does it also extend into regular paid hours? Okay. All right. So the first thing I'd say is uh in that case I'd start by clarifying whether the spike represents deliberate manipulation or just users uh maximizing within the plan's rules. Uh then I analyze basically user level patterns like device sharing unusual location changes or VPN uh usage uh to separate basically genuine heavy users from potential frauds. Uh the second basically this is like the aspect that I'll investigate. So fraud for example fraudulent users like fraudinal users then I'd segment accounts by usage intensity and behavior patterns to basically compare them against um like normal baselines that we have seen across uh a historical trend just to basically flag statistically significant outliers for deeper."
  reference_answer: time=None text=None
  interviewer_feedback: time=00:51 text="Yeah, let's say that this is specifically um happening uh after the 8:00 p.m. window."
  question_topic: Product Metrics

ITEM #2
  interviewer_question: time=01:54 text='wait, what what are fraudulent users? Can you go back and maybe define that first?'
  candidate_answer: time=02:00 text="So the key like the key metrics that I'd use like to understand what are fraud who are fraud like basically fraudsters are those exploiting the plan beyond the intended use like reselling the bandwidth to people like by sharing the internet tethering to like multiple devices or using automation or VPN setups to bypass limits rather than just consuming more data personally. So basically sharing data with multiple users is the biggest signal uh with respect to how fraudsters do use this and how we can see this is I I believe a telecom companies have access to where uh that particular data is being shared to and to what IP address. So if there are multiple IP addresses where that data is being shared to that means that there could be some fraudulent usage over here. What I mean by multiple is much more above than 10. So the account is likely being used to distribute data externally rather than for personal use."
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Product Metrics

ITEM #3
  interviewer_question: time=03:03 text="Okay. And what's the net consequence of fraudulent usage here? Just so that maybe we have a definition and an understanding of what the business impact uh is and why it even matters."
  candidate_answer: time=03:17 text="Sure. So the net consequence I see over here is the revenue leakage and network strain because since these users consume disproportionate amount of bandwidth without paying more which can degrade the service quality for other users and reduce profitability on that plan as well. So that's I would say that's the primary u business impact that would have like over because within a telecom architecture customer feedback or customer experience really matters as if they I mean on a day-to-day basis as well I would say that if we have a drop in the data data speed or services we usually tend to go to our friends or we tend to ask them that hey how is your internet working and if it happened to be that they're on another network and it's working then there's an incentive for me to move to that network as well given that most of the other characteristics of the plan are same so I'd have to switch networks which directly impacts churn and long-term customer retention"
  reference_answer: time=None text=None
  interviewer_feedback: time=04:20 text="I see okay so we know that it's bad because of those reasons right you're saying uh it affects people also in the network right that are not fraudulent right there's also the aspect of um potentially we gave them this 8:00 p.m., you know, 10x plan, right? And they feel like they're being throttled potentially, which means like, you know, the policy doesn't actually work, right? It's like, oh, I was promised, you know, unlimited data, but then it's like being throttled and it's not very good and so, uh, I'm just going to switch to, you know, AT&T instead of Verizon, right? Okay, there's that."
  question_topic: Product Metrics

ITEM #4
  interviewer_question: time=04:54 text='And then is there also a cost aspect or is that not really an issue you think with Verizon?'
  candidate_answer: time=05:01 text="Right. like when I would say that the cost aspect does come into play also because for example if there are too many legitimate fe uh users that feel throttled um by the plan design itself and basically basically making the adjustment by capping extreme outliers. So there's definitely a cost aspect for like two since higher nighttime usage increases uh network load infrastructure costs like bandwidth maintenance and without corresponding revenue growth right so definitely there's a cost uh there's a cost driver here as well uh with respect to the telecom infrastructure like we would have to invest in more uh route not routers but basically networks in order to ensure for example uh maximum minimum connectivity or basically ensuring additional capacity uh to provision that surge."
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Product Metrics

ITEM #5
  interviewer_question: time=06:00 text="Okay, got it. So we understand the net consequences here of actually you know why we want to do this. So, let's dive back into you said that there's a couple different ways that you can investigate, right? You can look at device sharing, you can look at, you know, um traffic signatures, VPN, uh tethering, other things like that. Um what else can we kind of do? And then once you're given all these different usage patterns, what actually like would you do in a certain scenario, right? like how would you actually implement in this case depending on different scenarios"
  candidate_answer: time=06:42 text="uh we could also implement I mean we all like I mentioned the earlier aspects but um we could also implement real-time monitoring rules like flagging as soon as there's a traffic spike beyond expected human behavior um repeated device uh authentication failure or adapt the product policies based on whether the dominant pattern is abuse or actual fraud. For example, if we are seeing regular usage of like 30GB okay and the plan right now we we assume that uh the course of in within this course of time we saw that uh it was 20GB usually. So we might we could also further think whether we see like this whether this jump uh within the same window is is a sudden jump or whether it's a deviation that would trigger an alert for review to check if uh it's a legitimate usage or it's potential misuse. So primarily I would say real time monitoring is something that should be given more emphasis because a lot of companies do have access to that. The only problem with that is when it comes to real-time monitoring the cost associated to create a real time platform is much expensive because telecom companies usually get these services from other uh third party providers like one example is Huawei another example is um I think mobile um these are few companies basically that allow you to get realtime insights from your systems because when you upgrade to a better system definitely you'll have the reports being generated on a more regular basis. So again there's a cost associated to it. So the infrastructure tier those providers charge significantly more for continuous data streaming and low latency processing which is why many telecoms still rely on batch analysis instead of full realtime systems let's say."
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Product Metrics

ITEM #6
  interviewer_question: time=08:43 text="But I guess there's still kind of this question of like how are you still distinguishing between like actual fraud and abuse versus just like normal, you know, high usage because, you know, it's 8:00 p.m. now and, you know, I'm an individual user and now I'm like streaming, you know, Netflix, right, at night and uh I get an alert that, you know, I can now stream Netflix uh right um at like, you know, 4K or something like that, right? So you're you have all this data right and you have all these like heruristics that you were mentioning right but how are you actually like determining you know the actual usage here and what's actually abuse and what's not"
  candidate_answer: time=09:23 text="right so I would say like per system metrics so so to me like there are certain metrics that we'll have to track that includes for example precision whether the true fraud flags um basically comparing the true fraud flags with the total uh total flagged amounts, the recall rate and the false positive rate as well at the same time. So these these particular metrics would at least help us understand whether like for example false positive rate which basically measures how many legitimate users were incorrectly flagged. So balancing these three helps fine-tune thresholds and improve uh like uh improve the overall model reliability because there's no there's no like we cannot we can never within like within the architecture we are operating in in my opinion uh there's always a tra trade-off between catching more fraud and keeping customer experience smooth. So finding the balance is the key to maintaining both trust and efficiency. So maintaining all these three like these three parameters that I mentioned about system performing metrics such as precision, recall and false positive rate. All"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #7
  interviewer_question: time=10:33 text="what goes into those? Right. Cuz I have no idea what how you catch like a false positive or how you even know that it is positive. Right. You've said that there's maybe device sharing and there's VPN use, but like you know normal people use VPNs anyway. So, is this like um someone switching a VPN like multiple times and then you investigate and then you determine it's fraud, let's say. How do you know it's fraud, right? What if it's just a normal user just switching VPNs all the time? Like, do you have a designation for what fraud is in this case?"
  candidate_answer: time=11:08 text="Yeah. So I'd say that we only classify it as a fraud if VPN switching coincides with other red flags like simultaneous login from locations like multiple locations because we have a geo flag also that basically identifies from which location this is being accessed or whether data whether the data is being routed to multiple external IPs basically indicating coordinated misuse rather than normal privacy behavior. And coming back to what I mentioned earlier about um so the precision me like what what precision measures is how many of the flagged cases were actually fraud. Recall basically would measure how many total fraud cases we have successfully caught in the in I would say in terms of his historical data and the false positive rate would basically measure how many users were incorrect incorrectly charged. So what manually goes into this is a false positive. We had manually review a flagged account using additional context like billing history, device consistency, prior complaint rec records since VPN use alone isn't enough. So it's a combination of multiple anomal sorry anomalies that um that uh signals real real fraud. So,"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #8
  interviewer_question: time=12:32 text='but you\'re basically building that model off of something, right? Like you can\'t just just have those heruristics and then call it fraud, right? Someone likely is going in and they probably view the activity history for like a customer over like 15 minutes and they do all this work, right? And they\'re like, "All right, this is definitely fraud, right?" And my internal model is just saying that, right? But additionally, what you\'re saying is that like all that stuff can\'t really be done in real time because it\'s extremely difficult, right? And so, um, just because they use like, you know, an above average amount of gigabytes of data doesn\'t mean that it\'s like automatically fraud, right? There has to be like a signal that then kind of has the person go in and do the investigative work, which evidently takes a lot of time,'
  candidate_answer: time=13:27 text="It does because that's where the costsensitive approach helps by basically weighing high value fraud more heavily in the model's loss function and then we can afford a few extra false positives on low value like on low value cases while ensuring expensive frauds are definitely caught early. So the goal here is to go go big or go home um idly because if we catch the bigger frauds, we're idly preventing a greater like the bigger loss or the bigger picture instead of catching the um the the lower ones because if it means like basically the extra false positives on low value cases if it means catching the high impact frauds earlier and reducing overall financial loss. So we protect a larger portion of revenue and then we can justify the investigation cost also whereas missing them would have had a dispos disproportionate um financial impact."
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #9
  interviewer_question: time=14:27 text="Okay. So let's just talk about the product and policy side now and uh just kind of quickly summarize you know the last bit of the question was you know how would your findings actually shape future product or policy decisions here?"
  candidate_answer: time=14:44 text="I just like a moment just to uh bring all the parts together. Yeah. So I think these findings would basically guide policy updates like introducing fair use gaps uh revising plan eligibility like how you whether you're eligible for this unlimited plan for example or adding tiered pricing for heavy users. And on the product side basically they inform clear communication about limits to manage expectations and reduce the churn. So one of the main one of the main things I would say on policy transformation is like how we are looking at this how we looking at a user to be eligible for this particular plan like that really matters and that would ideally be witnessed or basically checked through their historical behavior and for example if it's a new user then this plan should not be in like for a new user this should not exactly be a plan that should be immediately offered and if it is And uh a lot of companies have this uh have this have this model which is known as like a three-month program. For example, Mint Mint has Mint has this program where they have a 3month um discounted uh unlimited data program for the first 3 months. And after the first 3 months they have these catered um like basically what they do is that they check they look at the customer behavior uh whether their usage in these three months was within what tier and based on that they would suggest that tier or they would push that tier to that customer in the most effective way by campaigning it through a little um little lower than the market price or provide additional benefits. It's like maybe five international calls per month ideally just to incentivize the customer to focus on the particular plan that they would like them like or basically a bonus that they would like uh the customer to uh to basically re retain towards while aligning usage with the right plan tier."
  reference_answer: time=None text=None
  interviewer_feedback: time=14:43 text='Mhm.'
  question_topic: Product Metrics

ITEM #10
  interviewer_question: time=17:00 text="Okay, got it. Um, all right. So, I'm going to give you some feedback on this because I actually think that'd be helpful for the overall like understanding here and for our audiences kind of watching on YouTube. Um, so first off, I want to ask you like what do you think you did well? What do you think you did badly in this interview?"
  candidate_answer: time=17:18 text="I'd say that I think I have all the knowledge but I like um a little a little bit of my structuring was um was going off course at times I would say because in the end how you present the solution is what matters more than how I basically but how I I could have been more concise in a few parts and tied my examples back to the main question faster just to be in a short in a shorter note. that makes sense. I mean having a concrete illustrated example would make it easier to anchor my reasoning and basically also show exactly how the decision process works in practice. So like having a flowchart like approach basically the first this is how the business case was defined what would the model score this risk whether if it's low medium or high and based on that the different investigations that would require so definitely a structured approach to it would create a higher business impact and um focus more towards the recommended actions."
  reference_answer: time=None text=None
  interviewer_feedback: time=17:48 text="Yeah. Yeah. I would say that's um very very uh good analysis there, right? Because I think the one thing that I was pushing you in the very beginning was like defining what the key terms are because that's always kind of the problem with most interviews is that people have different understandings of what the definitions are, right? What does fraud mean, right? in this example, what does uh like product uh high product usage mean for example? And then what's the downsides in both cases, right? Like why are we doing this thing? Like what is the point of actually investigating into this, right? Because if we put our time and energy into investigating something, there's obviously some sort of like, you know, money that we're being paid to look into this, right? and a business case for like why we care about you know implementing something like this right so marketing at the end of the day or the product team right at the end of the day is creating like a unlimited data after 8 p.m. night and at the end of the day it's also about like costs right like we are doing this to acquire new customers likely or to incentivize their existing customers to stay with us with Verizon but at the same time we want to minimize the cost and fraudulent users likely are creating bad experiences as you said really well right for other users on telecom networks right but also um they're probably racking up you know costs of data usage that's not just free right uh and so like really defining that is kind of like the center point to everything. And I think you really need to emphasize that a lot more in the very beginning. And then really coming to like a concrete conclusion as well in terms of a solution is then really the second point that um really needs to be done, right? This means like actually providing examples of like showcasing the differences between fraud and like what regular product I product usage looks like and what normal behavior looks like and then showcasing you know if fraud was XYZ then we do this if fraud is actually uh ABC then we do that right um and so I think one of the tough things here about solo was like you didn't kind of come to like a definitive like this is what we should be doing you know and you know it's obviously hard in an open-ended question, but the easiest way to do that in an open-ended question is to actually have like a 100% like illustrated example that you can essentially explain to the interviewer that then um you know within that example you can easily kind of be like all right and this is like the best solution for right so I think that's the major improvement that kind of needs to be done in terms of a structured perspective um in terms of like really feeling like a takeaway that like you know this is a great solution and you like really understand the material here"
  question_topic: Communication

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/interview-query/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24/data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
