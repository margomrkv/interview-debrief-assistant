<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12",
  "transcript_folder": "transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12",
  "source_id": "ml_engineer_senior_meta_fraud_scam_interviewing_io_2025_08_12",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:18:05 +0200",
  "updated_at": "2026-05-20 21:31:15 +0200",
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
    "json": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/timecodes.txt",
        "en",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 21:18:05 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:31:14 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:31:15 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12`
- **Source ID:** `ml_engineer_senior_meta_fraud_scam_interviewing_io_2025_08_12`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:18:05 +0200
- **Last updated:** 2026-05-20 21:31:15 +0200

Фильтр в IDE: `*ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/timecodes.txt`<br>`en`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.pipeline-log.md` | — | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.validation-report.md` | 1.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.pipeline-log.md`

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
SOURCE_ID: ml_engineer_senior_meta_fraud_scam_interviewing_io_2025_08_12
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12
INTERVIEW_LANGUAGE: en
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00:00] [Music]
[00:00:03] I've never had a real job in my life. I
[00:00:05] have no real formal training in ML.
[00:00:06] >> We can say you did a really good job.
[00:00:09] Generally, this kind of thing I would
[00:00:10] expect from somebody who probably has at
[00:00:12] least like 7 to 8 years of experience.
[00:00:15] >> Hey everyone, welcome back to another
[00:00:16] episode of Whiteboard Confidential. I'm
[00:00:18] Adam from Interviewing IO and I'm
[00:00:19] excited to share today's replay with
[00:00:21] you. In this episode, our candidate was
[00:00:22] asked by an interviewer from Meta to
[00:00:24] design an ML system that detects
[00:00:26] fraudulent or scam content on Facebook.
[00:00:28] Now, this is an excellent example of the
[00:00:31] type of problem that a staff engineer at
[00:00:33] MEA would tackle day-to-day on the job.
[00:00:35] The candidate had no formal ML job
[00:00:37] experience yet delivers a design
[00:00:39] discussion at the level usually seen by
[00:00:41] IC5 to IC6 engineers. Now, this is a
[00:00:44] mustwatch if you want to get a deeper
[00:00:45] understanding on how to handle
[00:00:47] multimodal imbalanced or ambiguous data.
[00:00:49] All right, let's jump in.
[00:00:51] >> This will be a machine learning system
[00:00:53] design interview. Um the way generally
[00:00:57] uh it works is that I want to know a
[00:01:00] little bit more about you. Uh what's
[00:01:03] your background? Um and if you have any
[00:01:05] interviews coming up um
[00:01:08] and
[00:01:10] what companies might they be uh so I
[00:01:13] might be able to tailor um my feedback
[00:01:16] accordingly. Um and generally the system
[00:01:19] design part lasts around 40 45 minutes.
[00:01:23] Um and I can do some feedback post uh on
[00:01:28] that. Um or if you want um some people
[00:01:32] like to get feedback as we go. So um so
[00:01:37] yeah
[00:01:38] um yeah I'll give you a quick
[00:01:40] background. I um I have a uh PhD in
[00:01:44] physics. I graduated about three years
[00:01:47] ago and I have my on-site with Meta next
[00:01:50] Monday. Uh so that's what things are
[00:01:53] looking like. As for the feedback,
[00:01:56] um do you find one works better or other
[00:02:00] like during or after? Do you think one's
[00:02:02] better than the other?
[00:02:04] >> Um so it depends. So if you are if you
[00:02:07] feel that you are ready uh then it would
[00:02:12] make sense that we just kind of take it
[00:02:14] like an actual interview and then give
[00:02:15] you feedback in the end. But if you feel
[00:02:17] like you are not really sure what type
[00:02:20] of things might be asked or
[00:02:23] um you don't feel like very well
[00:02:26] prepared then generally uh it's better
[00:02:28] that if we take the feedback as we go so
[00:02:32] you don't waste time trying to just work
[00:02:35] through the problem uh without really
[00:02:39] feeling confident about it.
[00:02:41] >> Yeah, I understand. Um, maybe we'll try
[00:02:43] to wait for the end and if I change my
[00:02:45] mind partway through, I'll let you know.
[00:02:48] Also, um, I was hoping we could do um,
[00:02:52] as I understand there's two main
[00:02:54] problems, recommener systems and harmful
[00:02:56] content. Um, I've already done some rec
[00:02:59] Rexus um, mocks. So, if we could do
[00:03:02] something with harmful content, uh, that
[00:03:04] would be good.
[00:03:06] >> Okay. Yeah, that's that sounds good. Um,
[00:03:08] >> what did you have in mind, by the way?
[00:03:11] I
[00:03:11] >> had recommended system.
[00:03:13] >> Yeah, I don't know why I picked that.
[00:03:15] >> Yeah. No, but I thought harmful system
[00:03:17] is good because that's actually what I
[00:03:20] work on. So, uh this might be usually
[00:03:23] people don't get that type of a
[00:03:25] question. So, I don't really pick that
[00:03:27] but uh if you I've been seeing that
[00:03:31] trend that has been asked so I can pick
[00:03:34] up that question and uh we can uh go
[00:03:37] through it.
[00:03:38] >> All right. So, uh,
[00:03:39] >> one one quick question before I forget.
[00:03:41] Uh, what's the likelihood of each
[00:03:43] problem, would you say?
[00:03:46] >> Um,
[00:03:50] so it really depends on
[00:03:54] for example like uh who does who does
[00:03:57] your interview. Uh, you probably might
[00:03:59] have
[00:04:01] the the names of the people who are
[00:04:04] doing your system design interview. Mhm.
[00:04:07] >> Um if you look at their work what
[00:04:10] they're doing right now if they work
[00:04:13] with advertisement which is probably
[00:04:17] where
[00:04:19] most of the hiring is happening or if
[00:04:21] you uh they work within like Instagram
[00:04:23] or something then you can be more likely
[00:04:26] that you will get like a recommener
[00:04:28] system interview. Uh if you see somebody
[00:04:31] with like a description like um you know
[00:04:35] like working on content moderation or
[00:04:39] something like that uh or any type of
[00:04:44] content problems uh then then you will
[00:04:48] most likely are harmful because they
[00:04:50] want to kind of be asking questions that
[00:04:53] they are more familiar with.
[00:04:56] >> Got it. Yep. Sounds good.
[00:05:00] Okay. So, uh yeah. So, we can uh kind of
[00:05:05] start like a long blue line there. So,
[00:05:10] uh,
[00:05:35] good. So um this is kind of your job
[00:05:39] here is that uh you come in as a machine
[00:05:42] learning engineer and the first thing
[00:05:44] that uh you might want to end up doing
[00:05:46] is um you want to develop something that
[00:05:50] can pick up um let's say with
[00:05:55] some confidence that this might be a
[00:05:57] fraudulent or this might be uh a
[00:06:01] scam content uh so that uh the content
[00:06:04] can either to be taken down uh or
[00:06:11] be used um kind of for manual review um
[00:06:16] or just be like kind of not recommended
[00:06:19] to users depending on the use case uh
[00:06:23] and u the score that the classifier
[00:06:26] produces.
[00:06:28] >> All right. Um so should I go ahead and
[00:06:30] get started then?
[00:06:32] >> Mhm.
[00:06:32] >> Yeah. Okay. So we'll start off with some
[00:06:35] clarifying questions. So first let's
[00:06:38] just talk think of scale. Um how many
[00:06:41] you know users are there and how many
[00:06:46] posts per day and like um what's the
[00:06:48] like historic history of fraudulent
[00:06:51] posts per day.
[00:06:54] So um the history can be that there are
[00:06:58] approximately
[00:07:00] say um
[00:07:02] one from the past that we have seen
[00:07:04] using human sample let's say maybe like
[00:07:07] 2% of of the content is uh fall under
[00:07:11] like fraudulent or scam practices and
[00:07:15] the total volume of content is in on the
[00:07:18] daily basis can be in like in billions
[00:07:23] billions
[00:07:23] Okay.
[00:07:24] >> Yeah. Tens of billions of the total
[00:07:27] volume.
[00:07:27] >> Yeah. And 2% of back is is
[00:07:32] >> got it. Okay. And then for the latency
[00:07:35] um how fast does this need to perform?
[00:07:40] Um so for the latency we can uh assume
[00:07:47] uh that
[00:07:49] uh I would say like probably no more
[00:07:52] than um
[00:07:55] half a minute like 30 seconds
[00:07:58] 30 seconds. Okay.
[00:08:00] >> Yeah.
[00:08:01] >> Um and then um uh just a couple more
[00:08:04] quick questions regarding the data and
[00:08:06] the labels. So uh as far as the data is
[00:08:09] concerned are these like you know um
[00:08:13] posts like on Instagram or are they like
[00:08:16] something on like Facebook marketplace
[00:08:19] like what what's the context of this um
[00:08:22] like
[00:08:22] >> um so you can think about it this uh is
[00:08:25] on Facebook um and this would be posts
[00:08:30] um uh that the people do which includes
[00:08:34] like some type of media um and also um
[00:08:40] the comments that people leave,
[00:08:43] >> right?
[00:08:44] >> Yep.
[00:08:45] >> Yep.
[00:08:46] >> And so presumably there's going to be
[00:08:48] there can be like images, hyperlinks,
[00:08:52] um videos.
[00:08:54] >> Yeah.
[00:08:55] >> Text. Yeah. Okay. And then um for the
[00:08:58] labels um you know I can think of at
[00:09:01] least two ways to generate labels um you
[00:09:05] know from like user reports and
[00:09:09] human annotation. Um what um what's the
[00:09:14] um
[00:09:17] is that is uh that fine to assume I can
[00:09:19] use this to generate labels?
[00:09:22] >> Uh yes. So we do have uh some of the
[00:09:25] people who are hired to do the reviews
[00:09:30] um and we do also get user reported
[00:09:32] content. Um so um that is also a source
[00:09:38] um which can be used generally user
[00:09:41] reported content goes for a review like
[00:09:44] a manual review.
[00:09:46] >> Got it. All right. Well I think I think
[00:09:48] I'm ready to get started then. So just
[00:09:51] start off with some business objectives.
[00:09:53] So this one you know unlike the
[00:09:55] recommener system doesn't have as direct
[00:09:57] connection to to revenue but it still
[00:10:00] does have some right. So if you have a
[00:10:03] better system
[00:10:05] um that can reduce the need for human
[00:10:08] annotation. Uh so that's one way you can
[00:10:11] improve the revenue. The other is by
[00:10:12] promoting a safer environment um for
[00:10:16] advertisers, right? Like they don't want
[00:10:18] to advertise on a platform where there's
[00:10:20] a lot of you know negative content. The
[00:10:23] other is improve the you know trust and
[00:10:27] safety of the of the users. And finally,
[00:10:30] I can think of a third reason which is
[00:10:32] you know there could be some legal
[00:10:35] um you know things going on where
[00:10:38] harmful content not being suggested to
[00:10:42] um minors and things like that. Um so
[00:10:46] first I'll just give a kind of an
[00:10:48] outline of the um the system as a whole.
[00:10:51] I don't know if I can draw anywhere here
[00:10:54] like a whiteboard. Um, you can there's a
[00:10:57] power whiteboard. Uh, if if you want to
[00:10:59] just do like a rough boxes, that's fine.
[00:11:02] >> Uh, okay. Yeah, maybe I'll just draw it
[00:11:04] out real fast. You can see my screen,
[00:11:06] right?
[00:11:07] >> Yep, I see.
[00:11:08] >> Okay. So, you're going to have some, you
[00:11:10] know, user.
[00:11:12] They're going to interact with, you
[00:11:15] know, the client, which is, uh, Facebook
[00:11:19] to to to make a post. This is going to
[00:11:22] come down into this um you know service
[00:11:27] um
[00:11:31] right and um
[00:11:33] >> it's going to store
[00:11:36] um the post and the associated data the
[00:11:40] metadata and uh
[00:11:43] uh content
[00:11:45] uh in our feature store. And there will
[00:11:47] also be you know uh some trained model
[00:11:52] that it sends the the the features to
[00:11:57] um the the classifier which I'll I'll
[00:12:00] talk on in a second.
[00:12:02] >> And then um on the output end there's
[00:12:05] you know going to be a few different
[00:12:06] situations. So if the post is clean just
[00:12:10] send it back to Facebook
[00:12:13] uh post it uh so the user can see it.
[00:12:16] But then there's a few different
[00:12:17] situations. So you could have a
[00:12:19] situation where you have a post with um
[00:12:24] you know low confidence that it's
[00:12:26] harmful.
[00:12:28] Here there's a variety of things you can
[00:12:29] do. Um you can demote it to to limit the
[00:12:35] um the spread of it. Uh you you can flag
[00:12:39] it for further review by by humans. And
[00:12:43] I think maybe it might even make sense
[00:12:45] that when you retrain the model um
[00:12:48] actually maybe this will be not for low
[00:12:50] confidence. Let me come back to that
[00:12:51] point in a moment. Um but okay so that's
[00:12:54] for the low confidence ones.
[00:12:56] For the the um the uh the posts on which
[00:13:01] you're you know highly confident
[00:13:04] you can um just immediately
[00:13:08] remove. And um you know you also want to
[00:13:12] in this case um you know tell the user
[00:13:15] why it was removed. And also maybe I
[00:13:18] should have asked this in I I forgot to
[00:13:20] ask this in the clarifying section but
[00:13:23] um for the fraud aspect I'm assuming
[00:13:28] um and scam are there like different
[00:13:31] categories of these or is it just kind
[00:13:34] of can I just assume it's um one kind of
[00:13:37] fraud one kind of scam or are there like
[00:13:39] maybe crypto scams?
[00:13:41] Yeah, there are multiples. Like we can
[00:13:44] assume there are multiple but the type
[00:13:49] of them uh that shouldn't be of a
[00:13:52] concern. Uh but yes, there are multiple
[00:13:56] um
[00:13:58] scans and frauds.
[00:14:00] >> Okay. Yeah. So then in that case when
[00:14:02] you do you know identify the the that
[00:14:08] it's a scam or fraud
[00:14:10] we're going to notify the user for you
[00:14:12] know why that was the case. So that's
[00:14:14] kind of the highle
[00:14:16] design of what the system will look
[00:14:18] like. Let me just give a brief outline
[00:14:19] of some things I want to go over. So
[00:14:22] we're going to have the data. So you
[00:14:24] know features labels feature engineering
[00:14:28] right? Then we're going to have the um
[00:14:31] you know modeling aspect. So training
[00:14:36] it, evaluating it
[00:14:40] um and then deploying the model
[00:14:45] and monitoring the model. Feel like I'm
[00:14:49] forgetting something, but maybe I'll uh
[00:14:53] figure out as I go along.
[00:14:55] um
[00:14:57] data model. Yeah. So this is you know
[00:15:02] um this is um
[00:15:05] will look like. So let's think about
[00:15:07] what the data looks like. So we'll have
[00:15:12] um you know of course three sources.
[00:15:14] We'll have the user um and then this is
[00:15:18] this is some kind of Facebook post right
[00:15:21] for the item. And then we'll have user
[00:15:25] host interactions and we'll go through
[00:15:27] these um uh one by one. So for the user
[00:15:32] there's different kinds of um data
[00:15:36] associated with them. There's
[00:15:37] demographics, there's contextual
[00:15:39] information, there's also social
[00:15:41] information. So let's go through those.
[00:15:43] So we'll have the age,
[00:15:46] gender, location.
[00:15:48] Um
[00:15:51] what else? Date, finger, location.
[00:15:57] >> It's fine. You may imagine there's there
[00:16:00] Yeah. So we don't have to really they
[00:16:02] can collect all the features and
[00:16:04] >> Yeah. Um and so for the context we'll
[00:16:07] have device,
[00:16:10] time of day,
[00:16:12] um things like that. Um social. So, so
[00:16:18] this will include things like, you know,
[00:16:20] number of reports they've received in
[00:16:22] the past, right?
[00:16:25] >> Um, you know, a lot of B account or, you
[00:16:28] know, bad accounts tend to spam messages
[00:16:31] out. So, you could use a feature like
[00:16:34] number of messages sent in last, you
[00:16:38] know, n seconds where n can be, you
[00:16:41] know, varying. You could have one for
[00:16:44] the last 30 seconds, the last uh you
[00:16:46] know minute, last hour, whatever.
[00:16:48] Because I might expect that bad accounts
[00:16:50] that are spreading spam or not spam but
[00:16:54] um fraud and uh scams would be, you
[00:16:58] know, sending out a lot of messages in a
[00:16:59] short amount of time. Um, another one
[00:17:03] would be, you know, interactions with um
[00:17:07] um known offenders.
[00:17:11] And um let's see.
[00:17:14] I think I maybe I'll come back to this,
[00:17:16] but I think that should be enough to get
[00:17:18] started. Uh for the post, we're going to
[00:17:20] have uh you know, of course, some text
[00:17:24] associated, you know, like the the post
[00:17:27] itself, right? we're going to have an
[00:17:29] image associated with it or we can have
[00:17:32] an image rather um
[00:17:35] >> and you know here it's important that
[00:17:37] the image you know this can contain text
[00:17:39] itself you can extract via uh OCR so
[00:17:43] this is often the case in um you know
[00:17:45] memes uh there can be video
[00:17:49] audio I and then I'll just include one
[00:17:51] last one um so some kind of hyperlink
[00:17:55] um and then for the user post
[00:17:57] interactions Again, we could have number
[00:18:00] of of reports which um you know number
[00:18:03] of reports
[00:18:05] um um number of of comments,
[00:18:09] number of likes, the actual comments
[00:18:13] themselves and um I think that should be
[00:18:16] a good place to start.
[00:18:18] >> Okay. Um now let's go through and um
[00:18:25] uh process these these features for
[00:18:28] before we feed them to the model. So for
[00:18:30] the age um you can handle in a lot of
[00:18:33] different ways. One option is to
[00:18:34] bucketize it and then one hot encode it.
[00:18:37] So here you'd have you know 0 to 18 as a
[00:18:40] bucket, 18 to 24 and so on. Um and then
[00:18:44] want to hot encode it. Uh same with the
[00:18:46] gender. Uh location usually you get this
[00:18:50] as um you know latitude and longitude
[00:18:53] and you you definitely want to be aware
[00:18:55] of some some privacy concerns here. You
[00:18:58] don't want to have their exact location.
[00:19:00] But in any case um since there's going
[00:19:02] to be so many different locations, it
[00:19:05] might be best to use uh an embedding
[00:19:07] layer here for the device. you know
[00:19:11] whether or not it's um either on a
[00:19:13] mobile device or a laptop there
[00:19:16] shouldn't be a high cardality feature so
[00:19:17] you should be able to use one hot
[00:19:18] encoding time of day there's a few
[00:19:21] different things you could do you could
[00:19:22] of course one hot encode it for morning
[00:19:25] afternoon and night I think a better
[00:19:27] option is to use a a sinosidal transform
[00:19:30] here
[00:19:31] >> um because you know 11 p.m. is going to
[00:19:33] be closer to to 1:00 a.m. and that takes
[00:19:36] it into account. Um, number of reports.
[00:19:39] I think maybe the best way here would be
[00:19:43] um
[00:19:46] trying to think if it's going to have a
[00:19:47] skew is what's going through my mind
[00:19:50] right now. Um,
[00:19:54] maybe this might be best to just
[00:19:55] bucketize and uh, one hot code. So, you
[00:19:58] could have, you know, zero is not a lot
[00:20:01] of reports, one is a lot of reports and
[00:20:03] so on. You could also do something maybe
[00:20:04] like quantile binning here.
[00:20:07] >> Okay.
[00:20:08] >> Um
[00:20:11] let me um so number of messages sent in
[00:20:13] the last um n seconds. I think here
[00:20:17] probably just use some kind of um
[00:20:20] standardization
[00:20:22] and interactions with known offenders.
[00:20:25] Um you know maybe it's easest to just um
[00:20:29] have this as a one or a zero basically.
[00:20:32] So just one hunting code bat whether
[00:20:34] like one if they've interacted with
[00:20:36] known offender and zero zero otherwise.
[00:20:40] Okay. Um so now let's look at the the
[00:20:43] post itself. So um I guess I should have
[00:20:46] asked previously but um is this model
[00:20:50] you know global or multilingual?
[00:20:55] >> Um
[00:20:57] yes. So it generally works all across
[00:21:00] the world. uh but I think for starters
[00:21:03] let's say it's we are focusing on North
[00:21:06] America market uh and only on English.
[00:21:11] Got it. Okay. Well, in that case, um
[00:21:15] since um
[00:21:18] we only have to use English and since
[00:21:20] this is a social media platform, there's
[00:21:24] probably going to be a lot of emojis.
[00:21:26] And um in this case, using um some kind
[00:21:30] of pre-trained model that uses by parent
[00:21:34] coding um probably hand will handle the
[00:21:37] it will handle the emojis better. It
[00:21:40] usually works better with uh out of
[00:21:42] vocabulary stuff. So here could use um
[00:21:46] clip and um we could probably just
[00:21:49] combine the text in the image and also
[00:21:53] the text associated with the image and
[00:21:55] just pass them all through clip. So
[00:21:57] that'll take care of um
[00:22:00] these. Um and a few a few quick remarks
[00:22:04] on this. Um, so of course we're using
[00:22:06] pre-trained models which are are general
[00:22:08] purpose, but we can fine-tune if if we
[00:22:11] if we need to. All right, we should have
[00:22:14] enough data given the assumptions
[00:22:16] earlier. Um, and there's also some
[00:22:17] pre-processing we need to do, right? So
[00:22:20] um we need to um you know remove leading
[00:22:25] trailing white space
[00:22:27] um leatize things like that. We also
[00:22:30] need to tokenize and uh clip is a I
[00:22:34] believe it uses a bite parent coding for
[00:22:36] the tokenizer. So we need to use that.
[00:22:39] And then for the image aspect of it um
[00:22:43] I don't remember. I think it there's use
[00:22:45] some kind of vision transformer uh that
[00:22:47] uses for clip but I do know you in any
[00:22:50] case you're going to have to resize it.
[00:22:52] you're going have to normalize it and
[00:22:54] you're going to have to scale it um
[00:22:56] appropriate to the distribution it was
[00:22:59] trained on. Um now let's address the
[00:23:01] video. Um you can use um you know uh
[00:23:06] pre-trained models to just uh do the
[00:23:08] video directly. Um I think it might be
[00:23:11] better to just extract you know every
[00:23:13] images and you could treat it the
[00:23:15] hyperparameter. Um and then you know you
[00:23:19] could use clip maybe here you just use
[00:23:21] resonant. Um and again you know you have
[00:23:24] to resize normalize and scale the um the
[00:23:29] images and then aggregate them. Um so
[00:23:33] one option to aggregate them is just
[00:23:34] simply take the average but there's
[00:23:36] other options as well for the audio. uh
[00:23:39] wave tovec is a you know cuz if there's
[00:23:41] a video posted or you know maybe just a
[00:23:44] standalone audio file but there will
[00:23:45] also be often audio associated with the
[00:23:48] video that you want to pick up on. So
[00:23:50] here we can use wavetovec. I don't think
[00:23:52] you need to do a lot of pre-processing.
[00:23:54] I think the main thing uh is you just
[00:23:56] need to down sample it to
[00:23:59] 14 kHz. And then for the hyperlinks um
[00:24:02] this one's a little bit more difficult.
[00:24:05] So just starting off simply you could
[00:24:07] have a blacklist right so for sites that
[00:24:10] you you know are bad you can just use a
[00:24:12] rulebased approach here uh another
[00:24:14] option would be to use some tools like
[00:24:17] selenium beautiful soup to extract you
[00:24:21] know metadata and also like the homepage
[00:24:24] uh thumb you know image so you go to the
[00:24:26] site take a screenshot and then um you
[00:24:31] know uh uh use that image information.
[00:24:35] Also, another thing you could do here at
[00:24:37] this point is like um some kind of
[00:24:39] object detection. Maybe I'll have, you
[00:24:41] know, to identify actually no. Um yeah.
[00:24:46] So anyways, um and then for the user
[00:24:50] post interactions, so here
[00:24:52] Oh, I already have them. Oops. Um so
[00:24:55] yeah, for the number of reports, uh I
[00:24:57] think standardize,
[00:24:59] uh actually no, let's stick with what I
[00:25:01] did earlier. So, bucketize plus 100
[00:25:04] encoding actually. Yeah, whatever. Um,
[00:25:08] number of comments. Um,
[00:25:12] comments.
[00:25:15] Yeah, I expect this to actually be
[00:25:16] pretty skewed.
[00:25:18] I'd expect uh Yeah. So, here maybe do
[00:25:21] something like a a log transform. And um
[00:25:25] actually the same for for here, do a log
[00:25:28] transform. And then for the comments
[00:25:30] themselves,
[00:25:31] um just use
[00:25:35] um probably just use clip from earlier
[00:25:38] to um process all the comments and then
[00:25:43] um
[00:25:46] aggregate them. All right. So um that's
[00:25:49] enough for the the data. Now let's think
[00:25:52] about the actual model itself. So here
[00:25:55] we have a decision
[00:25:58] kind of immediately on whether or not to
[00:26:00] do early fusion versus late fusion. So
[00:26:03] late fusion is, you know, you have have
[00:26:06] a wait um actually you said there's
[00:26:10] different kinds of scans, right? Yeah.
[00:26:13] Multiple kinds.
[00:26:14] >> Yes.
[00:26:16] >> So yeah. Uh, so I guess if there's like
[00:26:17] a crypto scam versus like um I I'm
[00:26:21] drawing a blank on the other kinds of
[00:26:22] scams that could be maybe a bank scam or
[00:26:25] something like that, you could have a
[00:26:28] model for each kind, you know, crypto
[00:26:31] scam, maybe like a cash app um kind of
[00:26:35] scam and so on and so forth. Um and so
[00:26:39] you know the the pro of this is you you
[00:26:43] can train each model independently.
[00:26:47] Um but the con is you need to maintain
[00:26:51] many different um
[00:26:54] models which requires a lot of
[00:26:56] infrastructure and compute. You also
[00:26:58] have to dilute the data uh a bit across
[00:27:01] uh each each uh uh you should give me a
[00:27:06] second to think.
[00:27:11] Yeah. So um yeah so with late fusion you
[00:27:14] know you build a model to detect each
[00:27:16] each category and then combine the
[00:27:18] results at the end. Um but yeah so
[00:27:22] maintaining all these different models
[00:27:24] is going to require a lot of compute
[00:27:26] infrastructure. Um the other big
[00:27:28] drawback is that um
[00:27:31] you can't learn
[00:27:33] uh joint uh distributions.
[00:27:36] So um it could very well be the case
[00:27:38] that you know like maybe a tech the text
[00:27:42] alone is fine
[00:27:45] the um
[00:27:47] hyperlink or no no. How would that apply
[00:27:50] here?
[00:27:54] >> Give me a moment to think.
[00:28:14] H maybe that's what apply here.
[00:28:18] Um I'm I'm drawing a blank. Um maybe
[00:28:20] I'll ask you to step in actually for a
[00:28:22] moment. I changed my mind. is um is
[00:28:25] there the potential for like multiple
[00:28:28] things to interact to produce something
[00:28:31] harmful here? Uh what do you mean? So
[00:28:35] like in the case of um you know they're
[00:28:36] trying say if someone makes a Facebook
[00:28:38] post and you're trying to detect whether
[00:28:40] like um
[00:28:42] like if if you have a meme, right? So
[00:28:44] when you have a meme, the image by
[00:28:47] itself can be safe. the the text
[00:28:50] associated with the image can be safe by
[00:28:52] themselves, but when you combine them,
[00:28:54] it's bad, right?
[00:28:58] Okay. So, if you look at them in
[00:29:02] by themselves, they're fine. But when
[00:29:05] you combine them, then that becomes like
[00:29:08] a offending thing.
[00:29:10] >> Yeah. Let me give you an example. If
[00:29:12] there's text that says, "I hate these
[00:29:14] parasites," and the image is a bunch of
[00:29:16] parasites, well, then that's fine. But
[00:29:18] if the image is a person of a certain
[00:29:21] race, then you would deem it racist,
[00:29:24] right?
[00:29:25] >> Yep. So is there an analogous situation
[00:29:28] here?
[00:29:29] >> Um
[00:29:31] I I think yes. So there will be some
[00:29:34] type of a content where to just giving
[00:29:37] you an example like uh maybe somebody is
[00:29:41] offering uh maybe like you're a bank,
[00:29:43] right? and uh you're offering some loans
[00:29:48] to people, right? So, uh which is fine
[00:29:52] because you know you're a bank and you
[00:29:54] send messages or you post about like
[00:29:56] giving out loans. Um but then there
[00:30:00] might be a case where
[00:30:03] um
[00:30:05] there's a post about offering loans and
[00:30:10] the image just contains maybe like
[00:30:15] money in it. Uh and just says maybe like
[00:30:19] uh quick loans all approved but the text
[00:30:23] just says we are offering loans quick
[00:30:25] here to apply. Um, so I mean there can
[00:30:28] be cases where like the picture combined
[00:30:32] with the text might actually become a
[00:30:36] target but by themselves for example
[00:30:39] just like a picture of a lot of cash
[00:30:42] >> is fine.
[00:30:43] >> Y
[00:30:44] >> but if you are showing like people
[00:30:46] throwing cash in the air that's fine but
[00:30:47] if you're like I'm going to give you
[00:30:48] loan and then that's a picture
[00:30:50] associated with it and generally a bank
[00:30:53] wouldn't do that. Like that sounds like
[00:30:54] a scam. Yeah. Uh, great example. I I
[00:30:58] think that's pretty good. All right. So,
[00:31:00] um, I I'll continue on from there. So,
[00:31:02] okay, then in that case, um, you you
[00:31:05] wouldn't want to use late fusion then,
[00:31:06] uh, for that reason. Um, so you can't
[00:31:09] learn the joint distributions. Um, so,
[00:31:12] okay. So, um, then you have the option
[00:31:14] of early fusion. So, here, um, instead
[00:31:17] of training a model on each kind of
[00:31:19] scam,
[00:31:20] you, you know, concatenate all of the
[00:31:23] features above.
[00:31:26] uh immediately
[00:31:28] and then uh train a single model, right?
[00:31:34] Um and uh let go back to the whiteboard.
[00:31:39] So, uh start to kind of zoom in on the
[00:31:43] the model itself.
[00:31:45] So, um actually, let me just draw. So,
[00:31:48] there's a variety of different options
[00:31:50] as far as the model is concerned. So,
[00:31:53] um,
[00:31:54] you know, you could just have logistic
[00:31:57] regression.
[00:31:58] Um, there's problems with this at, uh,
[00:32:01] there's a few different problems with
[00:32:03] this. One is, um, you know, it's it's a
[00:32:06] binary classifier.
[00:32:08] So, it it can't identify the the kind of
[00:32:12] scam, which may, you know, may or may
[00:32:15] not be important.
[00:32:17] um uh when the there's you know
[00:32:20] colinearity
[00:32:23] in the features it's uh it's no it's
[00:32:26] known to struggle often it doesn't
[00:32:27] perform as strong as as other um uh
[00:32:32] models
[00:32:34] and um lastly uh it assumes the data is
[00:32:39] uh linearly separable which is often
[00:32:41] often not the case. it does have some
[00:32:43] pros. You know, it's fast, scales well,
[00:32:45] and so on. Um, you could instead
[00:32:48] consider something like a gradient
[00:32:50] boosted decision tree. Um, so some pros
[00:32:53] here include, you know, minimal feature
[00:32:56] processing.
[00:32:58] Um, you don't need to pre-process it
[00:32:59] like you do for the other ones. It's
[00:33:01] fast. It scale scales well. Um,
[00:33:05] but there are some cons. So, one con in
[00:33:08] particular is uh no online training. Uh
[00:33:11] so you have to retrain the entire model.
[00:33:12] You can't continuously train it which is
[00:33:14] a big drawback. Um another one is uh
[00:33:20] usually doesn't perform as good as
[00:33:23] something like a neural network when you
[00:33:25] have a lot of data which is is the case
[00:33:28] here. Um
[00:33:31] and then before I forget let me make a
[00:33:33] note for the
[00:33:36] cost and balance. So you want to
[00:33:38] probably use some kind of neural network
[00:33:39] approach. So it kind of alleviates a lot
[00:33:41] of the problems before. You're very free
[00:33:44] on the input layer is very flexible. You
[00:33:47] know, you can set it up to be
[00:33:50] multiclass, multilel, multitask, so on
[00:33:53] so forth. Um, you know, continuous
[00:33:56] learning. And of course, it performs
[00:33:59] well when you have
[00:34:01] a lot of data. Um, and so let's kind of
[00:34:06] briefly go over what the model might
[00:34:08] look like.
[00:34:10] So yeah,
[00:34:12] um
[00:34:14] okay.
[00:34:15] So you know, you're going to have
[00:34:19] the uh input features
[00:34:22] here. might make sense to
[00:34:25] run them through kind of a lightweight
[00:34:29] MLP
[00:34:31] um
[00:34:32] to pre-process them and then
[00:34:36] so um we talk about like a light light
[00:34:40] with MLP from the features. So these are
[00:34:43] the features that will be the embeddings
[00:34:47] that are coming out of the model that
[00:34:49] you described like slip or something
[00:34:50] like that.
[00:34:52] Oh yeah, sorry. I didn't mean for these
[00:34:54] this arrow to be em uh coming from the
[00:34:56] the feature store.
[00:35:03] But um sorry, what was your question
[00:35:05] again?
[00:35:06] >> Um yeah. Yeah, I just wanted to know
[00:35:08] like um what what are the inputs to this
[00:35:12] ML lightweight?
[00:35:13] >> Oh yeah, sorry. Sorry. Yeah, I guess it
[00:35:16] it could come from there. Uh the user
[00:35:18] features. Sorry, I wasn't clear about
[00:35:20] that. The post features and then the
[00:35:23] user post interaction features will be
[00:35:28] the the input to the model. Um
[00:35:32] and this will just learn some kind of
[00:35:34] embedding. And um from here I think kind
[00:35:39] of uh
[00:35:41] uh maybe the best way is to have
[00:35:45] do multitask
[00:35:47] where you have you know some kind of um
[00:35:51] you know head for each um kind of scam
[00:35:56] you know whether it's crypto scam, cash
[00:35:58] app scam, you know um whatever uh you
[00:36:04] know cash uh bank related,
[00:36:09] right? And um so you feed all these
[00:36:12] features uh feed these features to to
[00:36:15] each of these models.
[00:36:17] Um
[00:36:21] and then um
[00:36:24] so each class, let's talk about how to
[00:36:27] train it. So you're going to have some
[00:36:30] uh a sigmoid activation
[00:36:34] at the end. And then for the loss
[00:36:36] function could use something just um
[00:36:39] since this each one of these is a binary
[00:36:42] classifier detecting
[00:36:45] um you could use something like binary
[00:36:47] cross entropy or you know normalized
[00:36:49] cross entropy which is just binary cross
[00:36:51] entropy dividing by the the average. Um
[00:36:55] but there is a class imbalance. Um, so
[00:36:58] there's a few different ways we can
[00:36:59] handle it here. So for the imbalance,
[00:37:02] you can use um class weights. So like
[00:37:05] you said, 2% of the post will be will be
[00:37:07] bad. So you could use class weights, you
[00:37:10] could win the threshold. Um, but I think
[00:37:13] maybe a better option at this stage
[00:37:15] would be to use a the focal loss um to
[00:37:18] handle the the the class imbalance. And
[00:37:21] you you you apply the same procedure
[00:37:24] across them all. And um then at the end
[00:37:29] the the the final loss is just the the
[00:37:33] sum of the the losses from before. And
[00:37:37] um
[00:37:38] yeah so the inputs will be you know like
[00:37:41] uh the the what I described earlier and
[00:37:43] then the outputs will be the the label
[00:37:46] for each one. It'll be a vector of like
[00:37:48] 1 1 0 or 1 0 1 0 0 1 so on so forth. Um
[00:37:53] and then probably you know you standard
[00:37:56] things like ru activation, dropout
[00:37:58] regularization um things like that. So
[00:38:01] the class imbalance um we addressed um
[00:38:05] before I forget let me write this down.
[00:38:07] Uh actually maybe I'll just bring up
[00:38:10] now. Yeah, there there is going to be
[00:38:12] some kind of label bias. Um so from what
[00:38:14] I've seen this is actually a a really
[00:38:16] hard problem. you know, if you have
[00:38:18] three different interviewers or uh not
[00:38:20] interviewers, three different people
[00:38:21] label label something, they might um
[00:38:24] well, actually, in the case of scans, I
[00:38:27] think it should probably maybe it
[00:38:29] wouldn't be in any case, maybe I'll come
[00:38:31] back to that. Um actually, yeah, like
[00:38:35] talk about that a little bit. So, um,
[00:38:39] so you're talking about label bias where
[00:38:43] there's multiple people who might,
[00:38:46] uh, label the same content differently.
[00:38:50] Is that what you're talking about?
[00:38:51] >> That's right.
[00:38:53] >> Yeah. So, uh,
[00:38:56] how do you think we can kind of
[00:38:59] handle that?
[00:39:02] >> Yeah. Um,
[00:39:03] >> that's that's a real problem. I I guess
[00:39:08] in the case of uh you know say maybe
[00:39:10] maybe here's an idea, right? So um in
[00:39:12] the case of like uh uh someone pushing
[00:39:16] some stock,
[00:39:19] wouldn't that even be a scam? It's hard
[00:39:21] to say. Like say someone's saying buy
[00:39:22] this this NFT memecoin that they're
[00:39:25] going to pump and dump, right? Like
[00:39:27] that's a scam. Um
[00:39:31] maybe that would be a um
[00:39:34] >> there's a difference between
[00:39:36] think like I think the the thing that
[00:39:39] you're describing here as as know like
[00:39:42] you yourself are having trouble trying
[00:39:44] to identify like would this be a scam or
[00:39:46] not? So um
[00:39:49] how do you identify in your model like
[00:39:53] how do you train your model so that it
[00:39:55] can differentiate between
[00:39:58] scam and scammy posts
[00:40:02] >> that they look scammy but they are not
[00:40:04] technically a scam. They might be down
[00:40:07] the line but with the information that
[00:40:10] you have right now you cannot really
[00:40:12] make a decision.
[00:40:14] Um, I'm guessing maybe the first thing
[00:40:17] that comes to my mind is the output
[00:40:19] probability. So if the model outputs
[00:40:21] like 0.5, right, then that suggests it's
[00:40:25] it's not confident one way or the other
[00:40:27] on whether or not it's a scam.
[00:40:32] >> Okay.
[00:40:35] Um, I think that's um
[00:40:38] maybe the best I can come up with right
[00:40:39] now.
[00:40:43] Is there something we can do on the
[00:40:45] labeling side that might help with it?
[00:40:50] >> Oh yeah, you could um you could assign
[00:40:52] like a confidence maybe to to the
[00:40:55] labels. So when you're actually going to
[00:40:57] do the labels, you know, if you're very
[00:41:00] confident it's a scam, you could label
[00:41:02] assign it more weight in the loss
[00:41:04] function.
[00:41:09] >> I'm guessing that's what you had in
[00:41:10] mind.
[00:41:11] something like that. Yeah. So, it's
[00:41:14] more or less uh
[00:41:18] so what I was thinking was uh
[00:41:22] having multiple people review the same
[00:41:24] content and uh pick the majority, you
[00:41:28] know, so something like that. Um so,
[00:41:32] uh we kind of like try to tune out the
[00:41:35] bias there by showing off anything to
[00:41:38] more than one person. Um
[00:41:41] that's that's one of the things uh but I
[00:41:44] think in the end that turns out to be
[00:41:46] can be like a label weight because the
[00:41:50] the higher percentage of the people that
[00:41:52] mark this as a scam the label weight
[00:41:55] goes up.
[00:41:57] >> Right. Right. Right. Yeah. Okay.
[00:42:01] Should I continue?
[00:42:02] >> Yeah. All right. So, you know, now we've
[00:42:05] got this model built. Let's think of
[00:42:07] some kind of uh offline ways to evaluate
[00:42:10] it. So since it's a binary classifier,
[00:42:12] you can use you know the classics uh uh
[00:42:16] accuracy, precision, recall, accuracy
[00:42:19] not good because um
[00:42:22] imbalance
[00:42:24] recall
[00:42:25] um precision uh those are fine in this
[00:42:29] case. Probably want to favor
[00:42:31] recall over precision.
[00:42:34] um you know, you you want to catch all
[00:42:37] of the scams, right? You don't want to
[00:42:39] you don't want to let any through. And
[00:42:41] then um
[00:42:43] the the problem with these though is
[00:42:46] that they're dependent on some kind of
[00:42:48] threshold, right? So a metric like the
[00:42:51] area under the curve of ROC is a bit
[00:42:54] better because it, you know, operates o
[00:42:58] over multiple
[00:43:00] uh thresholds. And I think even better
[00:43:02] than that is the one I'll go with is the
[00:43:04] area on the curve for precision recall.
[00:43:06] So this tends to perform
[00:43:09] better when there is um
[00:43:13] imbalance which we have a a very large
[00:43:15] imbalance.
[00:43:17] >> Mhm.
[00:43:18] >> Um and then finally I think uh the last
[00:43:21] step would be to just uh discuss the
[00:43:24] deployment and online metrics. So
[00:43:29] uh first let's I think it's best to
[00:43:32] start with you know coming up with how
[00:43:34] you want to monitor it first before you
[00:43:35] deploy it. So here um you know assuming
[00:43:40] users can like report these these these
[00:43:44] scams. Maybe something you would want to
[00:43:46] log is um you know the number of
[00:43:49] reports.
[00:43:51] Um, and you might even want to normalize
[00:43:54] this like like the by the posts per day
[00:43:57] because if you have post more posts, you
[00:43:59] might expect more more reports here. You
[00:44:02] might want to use something like um uh
[00:44:06] proactive, right? So um uh how many
[00:44:11] scams
[00:44:13] you identify before they're reported.
[00:44:16] Although since we're assuming
[00:44:19] um what was our time? 30 seconds. Okay.
[00:44:21] Yeah, that's fine. Um and then finally,
[00:44:24] you could have something like prevalence
[00:44:26] like um
[00:44:28] but this isn't so prevalence is um
[00:44:33] how many you know how many scans per you
[00:44:38] know posts are um persist on the
[00:44:41] platform. One problem with this is
[00:44:45] um it doesn't take into account, you
[00:44:47] know, how popular it uh it is, right?
[00:44:51] So, if you have a bunch of scams, but
[00:44:52] they get no views, no impressions
[00:44:55] versus, you know, one scam that gets a
[00:44:57] million impressions, that that matters a
[00:44:59] lot. Um, so here you might want to use
[00:45:02] something like kind of the the the
[00:45:04] harmful impressions idea where it's how
[00:45:08] many
[00:45:09] uh people, you know, interact
[00:45:13] with the with the scam. And then let's
[00:45:15] think, you know, now that we have these
[00:45:17] metrics in mind, let's talk briefly or
[00:45:20] talk about the uh deployment. So here
[00:45:22] there's a variety of options. You could
[00:45:24] use something like shadow deployment. So
[00:45:26] here you um deploy both models uh in
[00:45:30] parallel or not yeah you you you deploy
[00:45:33] both models but you only uh serve the
[00:45:35] old problem with this is a lot of
[00:45:38] infrastructure a lot of compute uh you
[00:45:41] could use a canary deployment
[00:45:43] um where you deploy to a certain
[00:45:46] demographic and also um with that in
[00:45:49] mind let me backtrack just a bit you
[00:45:51] know on these evaluation metrics um you
[00:45:55] know it could be the case that there's a
[00:45:56] bias present, you know, over some
[00:45:59] demographic. Um, you know, maybe this
[00:46:02] model performs better over uh or not
[00:46:05] guys. What am I thinking? Um um you
[00:46:09] know, cash app scams. Maybe it's really
[00:46:10] good at identifying cash app scams, but
[00:46:14] not you know the the bank scams or or or
[00:46:17] Telegram scams uh for for that matter,
[00:46:20] right? Um so you'd want to segment um
[00:46:24] you know the evaluation to see where
[00:46:26] it's performing uh good and bad.
[00:46:28] >> Uh so for the canary deployment you want
[00:46:30] to deploy to certain demographics or
[00:46:31] maybe certain regions. Um but there's
[00:46:34] some bias uh as I just mentioned.
[00:46:37] Finally the kind of standard way is to
[00:46:39] do some kind of AD AB testing. And in
[00:46:41] this case since we have a very you know
[00:46:44] sensitive um you know thing we're
[00:46:47] dealing with it'd be probably best to to
[00:46:49] gradually roll it out. You don't want to
[00:46:51] just deploy the model it not perform
[00:46:53] well and then expose a bunch of people
[00:46:54] to to harmful content. So you might want
[00:46:57] to start off with like a 9010
[00:47:00] 10% split and then once you gain some
[00:47:02] confidence slowly roll it out to 50/50
[00:47:07] >> and uh what metric are we using here uh
[00:47:11] to decide if we can roll out or not?
[00:47:14] >> Thank you. Um,
[00:47:17] I think of course you want to take them
[00:47:18] all into account, but um I'd probably I
[00:47:22] think harmful impressions would be um if
[00:47:25] you had to pick one, you could just
[00:47:27] weight them too. You could take some
[00:47:28] linear combination of these um as well.
[00:47:33] Um but I think harmful impression makes
[00:47:36] most sense to to use as our metric.
[00:47:39] >> Okay.
[00:47:43] And I think that um I think that's it.
[00:47:46] >> Okay, cool.
[00:47:48] Um well, I think uh overall um I can say
[00:47:55] you did a really good job. Um especially
[00:47:59] given uh you just finished school. Uh
[00:48:03] you don't have like a lot of
[00:48:06] experience. Uh generally this kind of
[00:48:09] thing I would expect from somebody who
[00:48:11] probably has at least like maybe like
[00:48:14] seven to eight years of experience. Uh
[00:48:16] also probably have experience in this
[00:48:18] field. Uh because the kind of things
[00:48:20] that you talked about uh do seem like um
[00:48:25] very specific to this type of a problem.
[00:48:27] So I I just wonder like do you work with
[00:48:29] this kind of thing or do you just happen
[00:48:33] to study about this during your time?
[00:48:36] Um, I mean, I have a background in ML
[00:48:40] and
[00:48:42] I, um, I've never had a real job in my
[00:48:44] life. I have no real formal training in
[00:48:46] ML. I I did my PhD in physics. So, um, I
[00:48:50] don't know if that answers your
[00:48:51] question.
[00:48:53] >> No, I think that's Yeah, so I I think
[00:48:55] you you did really well. So probably I
[00:48:57] think uh from all the uh things that you
[00:49:00] have read so far um uh you do have like
[00:49:04] a really good grasp of the product area
[00:49:05] as well. Um so it comes with ML uh
[00:49:09] because there's a lot there's a lot of
[00:49:10] people who have like really good ML uh
[00:49:12] but uh it's good to see a person who can
[00:49:17] relate the ML back to the product. So um
[00:49:21] like you know like that that comes to
[00:49:23] show like what kind of metrics do you
[00:49:24] pick for example like the metrics about
[00:49:29] prevalence um and harmful
[00:49:33] impression um these
[00:49:36] someone who hasn't worked with this type
[00:49:37] of content probably wouldn't
[00:49:40] have in their mind. Um, so I think
[00:49:43] that's that's that's something good um
[00:49:46] that you identified um
[00:49:51] like the biases as well. Uh that might
[00:49:54] be here especially like the label bias.
[00:49:56] Uh that's something I really haven't
[00:49:59] really heard somebody talk about before.
[00:50:02] Um apply to work. Um and um um I think
[00:50:08] you're aware way of like handling the
[00:50:10] the different type of content. Uh
[00:50:15] especially like the hyperlinks and the
[00:50:17] audio files. I think that was good. Uh
[00:50:19] people usually don't mention that. Uh
[00:50:22] they usually stick with image and text.
[00:50:24] So I I think that's a that's a big plus.
[00:50:26] Um and uh I think some of the the
[00:50:32] areas uh I think I probably also wanted
[00:50:35] to mention that um around the cost
[00:50:38] imbalance I think that the loss type
[00:50:39] that you mentioned vocal loss and I
[00:50:42] think that was uh very insightful as
[00:50:45] well. Um yeah. So um so I would say like
[00:50:50] as it comes to improvement uh I think
[00:50:53] like if I were to like say like one
[00:50:55] thing
[00:50:57] um that that you might to might want to
[00:51:00] work on uh would be asking a little bit
[00:51:02] more questions
[00:51:04] u and starting simple. So uh for example
[00:51:10] um you did talk about uh like the shadow
[00:51:13] deployment we have both models um I
[00:51:17] never mentioned we had an old model um
[00:51:20] >> you mean on the deployment aspect
[00:51:23] >> yeah so um you didn't ask do we have a
[00:51:26] model uh we don't so we uh my mind was
[00:51:30] like we don't have any model um
[00:51:32] >> got it
[00:51:33] >> uh one of the things that um I would
[00:51:36] have like um you do kind of ask would
[00:51:41] they regarding the metrics uh maybe
[00:51:45] towards the beginning as well like have
[00:51:47] been subjects right so you did you did
[00:51:50] talk about revenue here uh it's it's a
[00:51:54] little I would say probably like it's
[00:51:56] it's useful if you try to fish this
[00:51:58] information out of the person first so
[00:52:01] you might want to like start off with
[00:52:02] like so uh what kind of object is are
[00:52:06] you looking at here? So, they might have
[00:52:09] something in their mind, they might talk
[00:52:10] about it or they might just throw throw
[00:52:11] the question back at you like what do
[00:52:13] you think? Right? So, but it's always
[00:52:16] good just try it out. Just ask them.
[00:52:19] Sometimes you might get an answer. For
[00:52:21] example, in this type of a problem,
[00:52:25] uh the general highest concern is user
[00:52:31] engagement, right? So we we want to make
[00:52:35] sure that the besides the legal thing
[00:52:38] you know that's that's obviously there
[00:52:41] the trust and safety and that's that's
[00:52:43] fine but as for like some tangible thing
[00:52:46] like you want to make sure that the user
[00:52:48] engagement you know like remains high um
[00:52:51] that we don't impact that in in any way.
[00:52:54] um you know like too many false
[00:52:56] positives might discourage people to
[00:52:59] post stuff
[00:53:01] um and too many false negatives might
[00:53:03] just make the platform full of content
[00:53:07] where people don't don't enjoy coming
[00:53:08] back to it anymore. So um kind of like
[00:53:12] trying to fish this thing uh talk about
[00:53:15] both things usually uh even if you're
[00:53:18] like I think you're talking about the
[00:53:21] recommener system even in that you know
[00:53:23] like just do mention both of the things
[00:53:27] uh revenue and uh and uh user engagement
[00:53:31] and usually people will ask you a
[00:53:33] question like how do you measure user
[00:53:35] engagement uh or how would you measure
[00:53:38] like the revenue new impact. So be ready
[00:53:41] to talk about like a tangible metric
[00:53:44] that you can
[00:53:45] >> mention at that point whether yes I will
[00:53:48] measure maybe uh some post click or user
[00:53:52] post by the day or how many likes are
[00:53:55] happening. You don't have to make up the
[00:53:59] exact best metric. Just just make
[00:54:01] something up that sounds reasonable.
[00:54:04] >> Got it. Uh um um and I think um
[00:54:12] the next thing goes on is the metrics
[00:54:15] that we were talking about. Um so
[00:54:19] uh we talked about
[00:54:22] evaluation like how will we evaluate the
[00:54:25] model? Um you were talking about how do
[00:54:29] we like we would favor recall. I think
[00:54:33] that would be a question to ask
[00:54:37] uh like what are the goals here? Are we
[00:54:40] trying to reduce
[00:54:43] the volume of the scams? Um like how are
[00:54:46] false positives more expensive than
[00:54:49] false negatives? There might be a case
[00:54:52] where we might be well, you know what,
[00:54:54] if you have too many false positives, if
[00:54:57] you're focusing solely on recall, we
[00:55:00] might be taking down quite a lot of
[00:55:01] content that might cause a little bit
[00:55:03] friction between users. Uh so, you know,
[00:55:08] we we want a really high precision
[00:55:10] model.
[00:55:12] We just we want like it to be it's fine
[00:55:14] if we get less stuff, but we want it to
[00:55:16] be very very confident. So um I think
[00:55:19] this is a thing that you could have
[00:55:21] asked that that would have come out and
[00:55:24] might have uh influenced maybe the way
[00:55:27] you select the metrics. Um,
[00:55:32] and also your training weights, uh,
[00:55:35] because if you're favoring precision
[00:55:38] over recall, it changes the way that you
[00:55:40] assign weights because now you want the
[00:55:43] model to be more confident in
[00:55:46] like let's say having a really high
[00:55:49] precision for the negative class, but it
[00:55:52] kind of shifts. But you want to be
[00:55:55] making sure that it it is very confident
[00:55:57] in picking the negative class. at the
[00:56:00] cost of the positive one because we we
[00:56:03] want we want like two labels to be
[00:56:06] really true. Um so um so I think this
[00:56:10] this is one of the things um uh I would
[00:56:14] say like in terms of like simplicity
[00:56:17] uh the the moral structure that they
[00:56:20] talked about uh I think you kind of went
[00:56:22] on with like the you did mention that we
[00:56:25] might do multi-ask
[00:56:28] uh model but you were not sure if we
[00:56:30] need it but then you ended up doing it
[00:56:33] anyways in the
[00:56:35] design you kind of start to break it
[00:56:38] down. Um like we have this uh we have
[00:56:41] like a model for doing XYZ
[00:56:44] scans. Um, again that might be a good
[00:56:48] question to ask like do we need to break
[00:56:49] it down or how do you think uh
[00:56:54] in the business case like do do we have
[00:56:58] off like do we have money to be able to
[00:57:00] train all these models or are we
[00:57:03] constrained right um and and that's fine
[00:57:06] like you you might be able to say like
[00:57:09] we don't know like how do you think
[00:57:10] about it so um generally I would air on
[00:57:15] the side of simple and mention how
[00:57:19] complex it could have been
[00:57:23] >> and then go down with the simple or like
[00:57:25] we just have like a binary model which
[00:57:27] just takes in all these features into
[00:57:30] like a one NLP classifier um and we have
[00:57:34] like a binary score the benefit of that
[00:57:38] is that it is very easy to read so if
[00:57:42] you are supplying the score to maybe
[00:57:44] let's say Facebook or Instagram or
[00:57:47] WhatsApp,
[00:57:49] it's much easier for them to be like,
[00:57:51] okay, I have this content, they gave me
[00:57:53] back a score and based on that I can
[00:57:56] decide if I want to demote this content,
[00:58:00] remove this content or report this
[00:58:02] content for manual review. But if you
[00:58:05] have multiple scores or let's say
[00:58:09] 10 different type of uh scams, then that
[00:58:12] becomes a little bit of a like a
[00:58:14] problem. So I would say just like start
[00:58:17] very simple um and then mention that
[00:58:20] this could have been if we had more time
[00:58:23] if we had more resources uh but try to
[00:58:27] follow the simple path. If the time you
[00:58:29] feel like there's a lot of time then
[00:58:31] always just go back and talk about
[00:58:33] things that you mentioned that I could
[00:58:35] have added XYZ here. So that generally
[00:58:38] makes the flow a little bit more easy as
[00:58:41] well and then gives you a chance to
[00:58:43] finish the question
[00:58:46] right on time and then add stuff on top
[00:58:49] of it. So just in case let's say
[00:58:53] time ran out at least you had a basic
[00:58:56] approach ready to go. Um, so it's it's
[00:59:01] more of a I would say like a time
[00:59:03] optimization strategy uh when you're
[00:59:05] doing the interviews. Um, so um it's
[00:59:10] yeah, so I think that's that's mainly I
[00:59:13] I'll probably say like uh try to ask a
[00:59:16] little bit more questions, try to fish
[00:59:18] as much as you can from the interviewer.
[00:59:23] uh and uh try to go simple first and uh
[00:59:27] mention about the things that you could
[00:59:29] have done like you know pros and cons
[00:59:30] but just follow the simple path and then
[00:59:33] go back to it if there is time. Um but I
[00:59:36] would say overall uh this was very good.
[00:59:39] Um I I just want to know like what level
[00:59:42] are you applying for?
[00:59:46] >> Uh yeah thanks for asking. Um there it
[00:59:49] wasn't specified. Um I I have no idea
[00:59:53] what my level will be.
[00:59:56] >> So was that so? Okay. So this is a uh
[00:59:59] fresh grad, right? So you're So you
[01:00:01] finished your uh graduate school uh PhD
[01:00:05] and then this is your first job.
[01:00:07] >> That's right. I finished uh almost 3
[01:00:09] years ago about 2 and a half years ago.
[01:00:12] Um, Meta contacted me a few months ago
[01:00:15] uh for the interview and um yeah, this
[01:00:19] is um the only interview I have is this
[01:00:22] is basically the first interview I've
[01:00:24] ever done um postgraduation. I started a
[01:00:26] company of my own two and a half years
[01:00:28] ago and I've been working on that since
[01:00:30] then. Um so this will be my my first
[01:00:33] job.
[01:00:34] >> Okay. Yeah. So this is uh I would say um
[01:00:38] I I would probably think it would be
[01:00:40] maybe um like a IC4 uh since uh you have
[01:00:45] the PhD and you have some experience
[01:00:48] even if it is working for yourselves. Um
[01:00:51] and I would probably say like this would
[01:00:53] be a like a green light or ICore to go
[01:00:57] ahead um
[01:01:00] on meta. Definitely.
[01:01:03] >> Yeah, true. Uh just a few quick
[01:01:05] questions for me. Um what where do you
[01:01:08] work and where do you where where uh
[01:01:10] country are you in? Obviously you don't
[01:01:11] have to answer, but I'm just curious.
[01:01:14] >> I work.
[01:01:17] >> Oh, fair enough.
[01:01:20] >> Yeah. So I'm in the US.
[01:01:22] >> You're in the US?
[01:01:24] >> Mhm.
[01:01:25] >> Gotcha. Um and then my last question,
[01:01:28] you know, I haven't really spent a lot
[01:01:29] of time on the the job hunt right now.
[01:01:32] things don't seem quite good. I I
[01:01:34] haven't This is the only interview I
[01:01:36] have and they contacted me. I'm just
[01:01:39] curious if you have any advice on how to
[01:01:40] like get referrals or land more
[01:01:42] interviews. I spent so much time
[01:01:44] preparing for this interview that I'd
[01:01:46] really like to add some companies, you
[01:01:48] know.
[01:01:50] >> Um I think like this is um this is
[01:01:53] already I would say like a hard time to
[01:01:56] be honest. Um I've had the question come
[01:01:59] across like multiple people. uh that how
[01:02:03] do I land jobs because I'm not even
[01:02:06] getting contacted. Um and
[01:02:11] I would think that it's generally
[01:02:16] comes down to as number one is the type
[01:02:20] of the role that you have. So machine
[01:02:23] learning um is really I would say in
[01:02:27] demand right now. So widget goat. So
[01:02:30] that's your specialty. Um, and I think
[01:02:34] you probably will fare much better than
[01:02:37] any other person who doesn't have an
[01:02:40] expertise in ML. Um, and I would say
[01:02:44] besides this, the only other people I
[01:02:46] would say would be not having a problem
[01:02:48] would be some people who are specialized
[01:02:51] in very niche fields uh, ML or nonML. Um
[01:02:56] um and I think if you want to kind of
[01:02:58] increase your chances of getting more
[01:03:01] companies um approaching you um
[01:03:07] one best way is to have experience
[01:03:11] working somewhere which is uh known
[01:03:16] in the industry. There is uh I have seen
[01:03:19] a big trend where people without
[01:03:22] experience or who are just like getting
[01:03:24] out of college now are having an
[01:03:26] extremely hard time but people with
[01:03:28] experience
[01:03:30] don't have the similar kind of problems.
[01:03:35] Um it's it's because like the the the
[01:03:40] companies are trying to kind of hire
[01:03:42] more experienced people uh especially in
[01:03:44] the times when the economy is not very
[01:03:48] stable. So they want to take a risk with
[01:03:51] somebody who doesn't have a draft
[01:03:52] record.
[01:03:54] >> So it's morely like more like trying to
[01:03:56] play a little conservative u with hiring
[01:04:00] uh especially in this time. So there
[01:04:02] isn't really like too much that you are
[01:04:05] not doing or you are doing wrong. Uh
[01:04:08] it's just the time that is uh happening
[01:04:11] right now. And I would just say like
[01:04:12] apply as much as you can. Um the the
[01:04:17] other way is if you know somebody, if
[01:04:20] you have friends, um referrals
[01:04:25] do significantly boost your chances of
[01:04:27] landing an interview. Um you can meet
[01:04:31] people in maybe some type of like tech
[01:04:34] talks or something might be happening in
[01:04:36] your local area uh which are not like
[01:04:40] don't pay to go to like expensive
[01:04:43] conferences but generally better to like
[01:04:46] go to like a smaller tech talk where you
[01:04:48] know it's like a small group of people
[01:04:50] which is lends you a better chance of
[01:04:52] meeting somebody talking to them about
[01:04:55] your work and maybe getting a referral.
[01:04:58] Um, so, uh, so I think like I would I
[01:05:02] would just say probably focus more on
[01:05:04] like a small meetups that are happening
[01:05:07] in her area regarding your field that
[01:05:09] you want to work in.
[01:05:12] >> Yeah, that that seems like um solid um
[01:05:15] advice. Um I to be honest I might just
[01:05:17] wait for the market to cool off because
[01:05:18] I I really or not cool off but to come
[01:05:21] back because it's just it's you know I
[01:05:25] feel like if I could get a couple
[01:05:27] interviews I would pass at least one of
[01:05:28] them. It's just I it's very hard. I
[01:05:31] don't even know why Meta contacted me in
[01:05:33] the first place to be honest but
[01:05:36] they have a higher push. big big higher
[01:05:38] push. So, um, and I think they are
[01:05:42] probably the only large company right
[01:05:44] now that is hiring that aggressively. I
[01:05:49] don't think there's any other company
[01:05:50] hiring that much.
[01:05:52] >> Yeah, that's the impression I got as
[01:05:54] well. Like there's some people I've been
[01:05:55] studying with and um I've been seeing
[01:05:57] the offers come in at a pretty high rate
[01:06:01] among my study group. So, that that for
[01:06:04] for meta specifically. So
[01:06:07] >> yeah, I think they they have they have a
[01:06:09] very
[01:06:11] very high I would say
[01:06:15] uh hiring array going on right now.
[01:06:19] There's a lot of pressure especially on
[01:06:22] the recruiting side to get as many
[01:06:25] people as you can. teams also are
[01:06:29] growing uh significantly
[01:06:32] uh like you know like so uh that's one
[01:06:36] of the reasons why like they they are
[01:06:38] really I think it was a good time to
[01:06:41] hire because they know that not many
[01:06:43] other companies are hiring so they might
[01:06:45] they'll have a good big talent in the
[01:06:48] market so um they don't have to compete
[01:06:52] with other companies as much so
[01:06:54] financially it makes more sense for
[01:06:57] to hire right now and nobody else is.
[01:07:00] >> But yeah, that makes sense.
[01:07:02] >> Yeah, but it's not good for the person
[01:07:04] on the other side because you don't have
[01:07:06] a lot of leverage when it comes to
[01:07:08] negotiating your offer.
[01:07:10] >> That's so
[01:07:11] >> Yeah, that's what I was going to say.
[01:07:13] Like, you know, if they made me an
[01:07:15] offer, I I probably I might not
[01:07:17] negotiate at all. And even if I did, it
[01:07:19] would be very lightweight, you know. I
[01:07:21] think um with that said,
[01:07:22] >> I would I would say like just my advice
[01:07:28] uh negotiate as much as you want to. Um,
[01:07:32] I can almost guarantee you that
[01:07:37] like they will try their best to get you
[01:07:39] in if you have the offer green light
[01:07:42] because they target set on recruiters
[01:07:47] are so high um that losing even one
[01:07:50] candidate is like they lost like a lot
[01:07:52] of work. So
[01:07:55] >> I'm not even like I'm not going to joke
[01:07:57] like you and say like say yeah I want
[01:07:58] like half a million dollars. Like you
[01:08:00] can just say they might not give it to
[01:08:01] you.
[01:08:03] >> But you can say it and they will they
[01:08:05] will still come back to you with
[01:08:06] something. They're not going to be like
[01:08:08] oh this guy is not serious. I'm not
[01:08:10] going to move forward. So I'm just
[01:08:11] telling like you in that way you have
[01:08:14] leverage because there's a big need for
[01:08:17] hiring right now. A lot of targets are
[01:08:20] set.
[01:08:21] Um so with that information you know you
[01:08:26] probably have a you some chance of at
[01:08:28] least doing negotiations. Um and I would
[01:08:32] very strongly suggest please do
[01:08:34] negotiate.
[01:08:36] >> Yeah.
[01:08:36] >> And because of first offer will not will
[01:08:38] not be a very good offer.
[01:08:41] >> Oh yeah. I I appreciate that because
[01:08:43] that was what I've always been told as
[01:08:45] well. Like once you get the offer, the
[01:08:47] power dynamics shift a little bit. Like
[01:08:50] um they took a lot of work to get you
[01:08:52] there. And I the data that I've seen
[01:08:55] says that like once they make you an
[01:08:57] offer like very very rarely do they
[01:09:00] resend it based on the negotiation.
[01:09:02] >> No, they won't. Yeah. I mean
[01:09:04] >> I I just like went back on my offer. I
[01:09:08] said I'm I I negotiated really hard and
[01:09:11] then in the end they were still not
[01:09:12] there. I just said I don't want to join
[01:09:14] and then
[01:09:15] um I got a few offers afterwards. Uh I
[01:09:20] didn't like them. I think the letter
[01:09:22] offer was still the best. I went back to
[01:09:23] them after like 10 days and they were
[01:09:26] still like yeah fine we going to
[01:09:31] um that's that's why I tell you that the
[01:09:34] recruiters have like a big big pressure
[01:09:36] to hire people. So they even if you said
[01:09:38] like no I don't want to go right now
[01:09:40] come go go go back to them after 2 weeks
[01:09:42] they will still take you.
[01:09:45] >> Yeah
[01:09:45] >> and that's generally true because your
[01:09:47] your interview remains valid for I think
[01:09:50] maybe like 6 months or something like
[01:09:52] that. So um so yeah don't worry about
[01:09:55] like if you were to like red do like a
[01:09:59] really hard negotiation they might they
[01:10:01] might resend the offer or they might
[01:10:03] just not go move forward. Uh and the
[01:10:06] best thing that moves fast is uh the
[01:10:09] highest I would say gain you will get it
[01:10:12] on uh sign on bonuses
[01:10:15] and the stock
[01:10:17] uh and the base is very hard to move.
[01:10:21] you you can move and you probably they
[01:10:23] they might move but I don't expect more
[01:10:26] than like 10 15% change in the base but
[01:10:30] sign on bonus you probably won't get any
[01:10:34] and they offer you uh just look at level
[01:10:39] FI uh see what people are getting and
[01:10:42] just ask that much and they will give it
[01:10:44] to you like instantly without even like
[01:10:47] you just they just want people to ask if
[01:10:50] sometime people Don't even ask anything.
[01:10:52] So they lose
[01:10:53] like 100k just like that. Just we just
[01:10:57] just ask them once and they will give
[01:10:59] they will be like fine here
[01:11:01] 50k.
[01:11:03] Uh and do I need a do I need like
[01:11:05] another offer to to negotiate?
[01:11:07] >> If you have if you have a counter offer
[01:11:12] that can get you
[01:11:15] base salary and stock a little higher.
[01:11:19] >> Gotcha. Uh but they have a limit that is
[01:11:22] on their website for the role and that
[01:11:26] is the hard limit. The high upper limit
[01:11:28] that generally is the upper limit unless
[01:11:31] you do so good for the interview that
[01:11:33] they might consider you for the next
[01:11:35] level.
[01:11:37] >> Unless that happens they will stick with
[01:11:39] the limit that they have and that will
[01:11:41] be the like that will be the max that
[01:11:44] they will be able to offer at that
[01:11:45] level. Uh that's why I said like sign on
[01:11:48] bonus is the first thing that you should
[01:11:49] always talk about always and just ask
[01:11:52] whatever you see online the maximum
[01:11:55] value for your level just ask that
[01:11:58] exactly.
[01:12:00] >> Gotcha.
[01:12:01] >> Uh
[01:12:02] >> yeah yeah and go ahead.
[01:12:03] >> Yeah. So big and yeah f and then the
[01:12:06] next thing is probably like um like
[01:12:07] stocks um
[01:12:10] that that they would be willing to go a
[01:12:12] little bit higher on uh especially right
[01:12:16] now I don't know they might not because
[01:12:17] the stock is low so they might push you
[01:12:20] on like saying stock is low right now so
[01:12:22] you might have a very big upside but
[01:12:25] yeah I mean you you'll be able to just
[01:12:28] don't
[01:12:30] don't not negotiate
[01:12:33] Yeah, I appreciate that. You know,
[01:12:35] >> yeah,
[01:12:35] >> like a little I'm not I'm not quite
[01:12:37] desperate yet, but I'm I'm getting
[01:12:39] there. And so, it's good to know that I
[01:12:41] still have
[01:12:42] >> some room, you know, a lot of room to to
[01:12:44] negotiate. Just the market.
[01:12:46] >> Yeah. I mean, you know, you you have you
[01:12:48] definitely have people generally think
[01:12:50] that they don't, but uh even if you
[01:12:53] don't have a a counter offer, you still
[01:12:55] have a very big room to negotiate.
[01:12:58] >> Gotcha. Yeah.
[01:13:02] Um yeah. Anything else you want to add?
[01:13:05] >> Uh no, I think that's uh that's good.
[01:13:07] I'm just going to like leave like a
[01:13:10] structure uh that generally I share with
[01:13:14] the people that I do system design with.
[01:13:17] Um I think you kind of have like a good
[01:13:20] structure of your own as well. Um, but
[01:13:23] this is kind of what uh
[01:13:28] advice people
[01:13:29] >> uh to talk about like how to break down
[01:13:31] the problem. Um, so um I
[01:13:36] >> in the chat.
[01:13:37] >> Yes, I that Yeah, I see that. Thank you.
[01:13:40] >> Uh yeah, so I think that that should be
[01:13:43] it. Uh and all the best for the rest of
[01:13:45] your interviews. Um I will you offer.
[01:13:51] >> Thank you. I appreciate all the
[01:13:52] feedback. Um you were one of the better
[01:13:54] mock interviewers I've had. So um
[01:13:56] >> Oh, thank you. Thank you very much.
[01:13:58] >> Yeah, thanks for staying staying over. I
[01:14:00] know we went a bit over, but um thanks
[01:14:02] again for everything. Take care.
[01:14:03] >> Yeah. Yeah. Okay. Thank you. Bye.
[01:14:05] >> All right, that's all we have for today.
[01:14:06] Thank you for watching. And if you want
[01:14:07] to get immediate feedback from the same
[01:14:09] people we make hiring decisions at
[01:14:11] companies like Google, Meta, and OpenAI,
[01:14:13] hit the link in our show notes to book
[01:14:14] your session now.

FEEDBACK_MD:
---
section: "Interviewer feedback and praise"
start: "00:48:00"
end: "00:51:00"
start_seconds: 2880
end_seconds: 3060
---

you don't have like a lot of experience. Uh generally this kind of thing I would expect from somebody who probably has at least like maybe like seven to eight years of experience. Uh also probably have experience in this field. Uh because the kind of things that you talked about uh do seem like um very specific to this type of a problem. So I I just wonder like do you work with this kind of thing or do you just happen to study about this during your time? Um, I mean, I have a background in ML and I, um, I've never had a real job in my life. I have no real formal training in ML. I I did my PhD in physics. So, um, I don't know if that answers your question. >> No, I think that's Yeah, so I I think you you did really well. So probably I think uh from all the uh things that you have read so far um uh you do have like a really good grasp of the product area as well. Um so it comes with ML uh because there's a lot there's a lot of people who have like really good ML uh but uh it's good to see a person who can relate the ML back to the product. So um like you know like that that comes to show like what kind of metrics do you pick for example like the metrics about prevalence um and harmful impression um these someone who hasn't worked with this type of content probably wouldn't have in their mind. Um, so I think that's that's that's something good um that you identified um like the biases as well. Uh that might be here especially like the label bias. Uh that's something I really haven't really heard somebody talk about before. Um apply to work. Um and um um I think you're aware way of like handling the the different type of content. Uh especially like the hyperlinks and the audio files. I think that was good. Uh people usually don't mention that. Uh they usually stick with image and text. So I I think that's a that's a big plus. Um and uh I think some of the the areas uh I think I probably also wanted to mention that um around the cost imbalance I think that the loss type that you mentioned vocal loss and I think that was uh very insightful as well. Um yeah. So um so I would say like as it comes to improvement uh I think like if I were to like say like one thing um that that you might to might want to

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
Write JSON only to: splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.json \
    --video transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.json --out splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.qa-split.json \
    --video transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.validation-report.md

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
video.md: transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/video.md

--- CHAPTER `00:00:30` — System design prompt: ML model to detect scam content ---
window: 00:00:30 .. 00:36:00
recognition_status: multiple (4 items)

ITEM #1
  interviewer_question: time=00:51 text="This will be a machine learning system design interview. Um the way generally uh it works is that I want to know a little bit more about you. Uh what's your background? Um and if you have any interviews coming up um and what companies might they be uh so I might be able to tailor um my feedback accordingly. Um and generally the system design part lasts around 40 45 minutes. Um and I can do some feedback post uh on that. Um or if you want um some people like to get feedback as we go. So um so yeah"
  candidate_answer: time=01:38 text="um yeah I'll give you a quick background. I um I have a uh PhD in physics. I graduated about three years ago and I have my on-site with Meta next Monday. Uh so that's what things are looking like. As for the feedback,"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Communication

ITEM #2
  interviewer_question: time=03:08 text='what did you have in mind, by the way?'
  candidate_answer: time=03:11 text='had recommended system. Yeah. No, but I thought harmful system'
  reference_answer: time=None text=None
  interviewer_feedback: time=03:06 text="Okay. Yeah, that's that sounds good. Um,"
  question_topic: Communication

ITEM #3
  interviewer_question: time=05:35 text="good. So um this is kind of your job here is that uh you come in as a machine learning engineer and the first thing that uh you might want to end up doing is um you want to develop something that can pick up um let's say with some confidence that this might be a fraudulent or this might be uh a scam content uh so that uh the content can either to be taken down uh or be used um kind of for manual review um or just be like kind of not recommended to users depending on the use case uh and u the score that the classifier produces."
  candidate_answer: time=06:32 text="Yeah. Okay. So we'll start off with some clarifying questions. So first let's just talk think of scale. Um how many you know users are there and how many posts per day and like um what's the like historic history of fraudulent posts per day. Yeah. And 2% of back is is Yeah. right? Yep. Yeah. Uh yes. So we do have uh some of the people who are hired to do the reviews um and we do also get user reported content. Um so um that is also a source um which can be used generally user reported content goes for a review like a manual review. recommener system doesn't have as direct connection to to revenue but it still does have some right. So if you have a better system um that can reduce the need for human annotation. Uh so that's one way you can improve the revenue. The other is by promoting a safer environment um for advertisers, right? Like they don't want to advertise on a platform where there's a lot of you know negative content. The other is improve the you know trust and safety of the of the users. And finally, I can think of a third reason which is you know there could be some legal um you know things going on where harmful content not being suggested to um minors and things like that. Um so first I'll just give a kind of an outline of the um the system as a whole. I don't know if I can draw anywhere here like a whiteboard. Um, you can there's a power whiteboard. Uh, if if you want to just do like a rough boxes, that's fine. Yep, I see. it's going to store um the post and the associated data the metadata and uh uh content uh in our feature store. And there will also be you know uh some trained model that it sends the the the features to um the the classifier which I'll I'll talk on in a second. Okay. Yeah. So then in that case when you do you know identify the the that it's a scam or fraud we're going to notify the user for you know why that was the case. So that's kind of the highle design of what the system will look like. Let me just give a brief outline of some things I want to go over. So we're going to have the data. So you know features labels feature engineering right? Then we're going to have the um you know modeling aspect. So training it, evaluating it um and then deploying the model and monitoring the model. Feel like I'm forgetting something, but maybe I'll uh figure out as I go along. um data model. Yeah. So this is you know um this is um will look like. So let's think about what the data looks like. So we'll have um you know of course three sources. We'll have the user um and then this is this is some kind of Facebook post right for the item. And then we'll have user host interactions and we'll go through these um uh one by one. So for the user there's different kinds of um data associated with them. There's demographics, there's contextual information, there's also social information. So let's go through those. So we'll have the age, gender, location. Um what else? Date, finger, location. Yeah. Um and so for the context we'll have device, time of day, um things like that. Um social. So, so this will include things like, you know, number of reports they've received in the past, right? and you know here it's important that the image you know this can contain text itself you can extract via uh OCR so this is often the case in um you know memes uh there can be video audio I and then I'll just include one last one um so some kind of hyperlink um and then for the user post interactions Again, we could have number of of reports which um you know number of reports um um number of of comments, number of likes, the actual comments themselves and um I think that should be a good place to start. um because you know 11 p.m. is going to be closer to to 1:00 a.m. and that takes it into account. Um, number of reports. I think maybe the best way here would be um trying to think if it's going to have a skew is what's going through my mind right now. Um, maybe this might be best to just bucketize and uh, one hot code. So, you could have, you know, zero is not a lot of reports, one is a lot of reports and so on. You could also do something maybe like quantile binning here. Um let me um so number of messages sent in the last um n seconds. I think here probably just use some kind of um standardization and interactions with known offenders. Um you know maybe it's easest to just um have this as a one or a zero basically. So just one hunting code bat whether like one if they've interacted with known offender and zero zero otherwise. Okay. Um so now let's look at the the post itself. So um I guess I should have asked previously but um is this model you know global or multilingual? Yes. Give me a moment to think. H maybe that's what apply here. Um I'm I'm drawing a blank. Um maybe I'll ask you to step in actually for a moment. I changed my mind. is um is there the potential for like multiple things to interact to produce something harmful here? Uh what do you mean? So like in the case of um you know they're trying say if someone makes a Facebook post and you're trying to detect whether like um like if if you have a meme, right? So when you have a meme, the image by itself can be safe. the the text associated with the image can be safe by themselves, but when you combine them, it's bad, right? Okay. So, if you look at them in by themselves, they're fine. But when you combine them, then that becomes like a offending thing. Yep. So is there an analogous situation here? is fine. but if you are showing like people throwing cash in the air that's fine but if you're like I'm going to give you loan and then that's a picture associated with it and generally a bank wouldn't do that. Like that sounds like a scam. Yeah. Uh, great example. I I think that's pretty good. All right. So, um, I I'll continue on from there. So, okay, then in that case, um, you you wouldn't want to use late fusion then, uh, for that reason. Um, so you can't learn the joint distributions. Um, so, okay. So, um, then you have the option of early fusion. So, here, um, instead of training a model on each kind of scam, you, you know, concatenate all of the features above. uh immediately and then uh train a single model, right? Um and uh let go back to the whiteboard. So, uh start to kind of zoom in on the the model itself. So, um actually, let me just draw. So, there's a variety of different options as far as the model is concerned. So, um, you know, you could just have logistic regression. Um, there's problems with this at, uh, there's a few different problems with this. One is, um, you know, it's it's a binary classifier. So, it it can't identify the the kind of scam, which may, you know, may or may not be important. um uh when the there's you know colinearity in the features it's uh it's no it's known to struggle often it doesn't perform as strong as as other um uh models and um lastly uh it assumes the data is uh linearly separable which is often often not the case. it does have some pros. You know, it's fast, scales well, and so on. Um, you could instead consider something like a gradient boosted decision tree. Um, so some pros here include, you know, minimal feature processing. Um, you don't need to pre-process it like you do for the other ones. It's fast. It scale scales well. Um, but there are some cons. So, one con in particular is uh no online training. Uh so you have to retrain the entire model. You can't continuously train it which is a big drawback. Um another one is uh usually doesn't perform as good as something like a neural network when you have a lot of data which is is the case here. Um and then before I forget let me make a note for the cost and balance. So you want to probably use some kind of neural network approach. So it kind of alleviates a lot of the problems before. You're very free on the input layer is very flexible. You know, you can set it up to be multiclass, multilel, multitask, so on so forth. Um, you know, continuous learning. And of course, it performs well when you have a lot of data. Um, and so let's kind of briefly go over what the model might look like. So yeah, um okay. So you know, you're going to have the uh input features here. might make sense to run them through kind of a lightweight MLP um to pre-process them and then so um we talk about like a light light with MLP from the features. So these are the features that will be the embeddings that are coming out of the model that you described like slip or something like that. Oh yeah, sorry. I didn't mean for these this arrow to be em uh coming from the the feature store. But um sorry, what was your question"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #4
  interviewer_question: time=35:06 text='Um yeah. Yeah, I just wanted to know like um what what are the inputs to this'
  candidate_answer: time=35:13 text="Oh yeah, sorry. Sorry. Yeah, I guess it it could come from there. Uh the user features. Sorry, I wasn't clear about that. The post features and then the user post interaction features will be the the input to the model. Um and this will just learn some kind of embedding. And um from here I think kind of uh uh maybe the best way is to have do multitask where you have you know some kind of um you know head for each um kind of scam you know whether it's crypto scam, cash app scam, you know um whatever uh you know cash uh bank related, right? And um so you feed all these features uh feed these features to to each of these models. Um and then um so each class, let's talk about how to train it. So you're going to have some uh a sigmoid activation at the end. And then for the loss function could use something just um since this each one of these is a binary classifier detecting um you could use something like binary cross entropy or you know normalized cross entropy which is just binary cross entropy dividing by the the average. Um but there is a class imbalance. Um, so there's a few different ways we can handle it here. So for the imbalance, you can use um class weights. So like you said, 2% of the post will be will be bad. So you could use class weights, you could win the threshold. Um, but I think maybe a better option at this stage would be to use a the focal loss um to handle the the the class imbalance. And you you you apply the same procedure across them all. And um then at the end the the the final loss is just the the sum of the the losses from before. And um yeah so the inputs will be you know like uh the the what I described earlier and then the outputs will be the the label for each one. It'll be a vector of like 1 1 0 or 1 0 1 0 0 1 so on so forth. Um and then probably you know you standard things like ru activation, dropout regularization um things like that. So the class imbalance um we addressed um before I forget let me write this down. Uh actually maybe I'll just bring up now. Yeah, there there is going to be some kind of label bias. Um so from what I've seen this is actually a a really hard problem. you know, if you have three different interviewers or uh not interviewers, three different people label label something, they might um well, actually, in the case of scans, I think it should probably maybe it wouldn't be in any case, maybe I'll come back to that. Um actually, yeah, like talk about that a little bit. So, um, so you're talking about label bias where there's multiple people who might, uh, label the same content differently."
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `00:36:00` — Modeling strategy, focal loss, and label bias ---
window: 00:36:00 .. конец
recognition_status: multiple (8 items)

ITEM #5
  interviewer_question: time=38:56 text='how do you think we can kind of handle that?'
  candidate_answer: time=39:02 text="Yeah. Um, that's that's a real problem. I I guess in the case of uh you know say maybe maybe here's an idea, right? So um in the case of like uh uh someone pushing some stock, wouldn't that even be a scam? It's hard to say. Like say someone's saying buy this this NFT memecoin that they're going to pump and dump, right? Like that's a scam. Um maybe that would be a um"
  reference_answer: time=None text=None
  interviewer_feedback: time=38:51 text="That's right."
  question_topic: ML

ITEM #6
  interviewer_question: time=39:34 text="there's a difference between think like I think the the thing that you're describing here as as know like you yourself are having trouble trying to identify like would this be a scam or not? So um how do you identify in your model like how do you train your model so that it can differentiate between scam and scammy posts"
  candidate_answer: time=40:14 text="Um, I'm guessing maybe the first thing that comes to my mind is the output probability. So if the model outputs like 0.5, right, then that suggests it's it's not confident one way or the other on whether or not it's a scam."
  reference_answer: time=None text=None
  interviewer_feedback: time=40:32 text="Okay. Um, I think that's um maybe the best I can come up with right now."
  question_topic: ML

ITEM #7
  interviewer_question: time=40:43 text='Is there something we can do on the labeling side that might help with it?'
  candidate_answer: time=40:50 text="Oh yeah, you could um you could assign like a confidence maybe to to the labels. So when you're actually going to do the labels, you know, if you're very confident it's a scam, you could label assign it more weight in the loss function."
  reference_answer: time=41:11 text="something like that. Yeah. So, it's more or less uh so what I was thinking was uh having multiple people review the same content and uh pick the majority, you know, so something like that. Um so, uh we kind of like try to tune out the bias there by showing off anything to more than one person. Um that's that's one of the things uh but I think in the end that turns out to be can be like a label weight because the the higher percentage of the people that mark this as a scam the label weight goes up."
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #8
  interviewer_question: time=42:02 text="Yeah. All right. So, you know, now we've got this model built. Let's think of some kind of uh offline ways to evaluate"
  candidate_answer: time=42:10 text="it. So since it's a binary classifier, you can use you know the classics uh uh accuracy, precision, recall, accuracy not good because um imbalance recall um precision uh those are fine in this case. Probably want to favor recall over precision. um you know, you you want to catch all of the scams, right? You don't want to you don't want to let any through. And then um the the problem with these though is that they're dependent on some kind of threshold, right? So a metric like the area under the curve of ROC is a bit better because it, you know, operates o over multiple uh thresholds. And I think even better than that is the one I'll go with is the area on the curve for precision recall. So this tends to perform better when there is um imbalance which we have a a very large imbalance. Um and then finally I think uh the last step would be to just uh discuss the deployment and online metrics. So uh first let's I think it's best to start with you know coming up with how you want to monitor it first before you deploy it. So here um you know assuming users can like report these these these scams. Maybe something you would want to log is um you know the number of reports. Um, and you might even want to normalize this like like the by the posts per day because if you have post more posts, you might expect more more reports here. You might want to use something like um uh proactive, right? So um uh how many scams you identify before they're reported. Although since we're assuming um what was our time? 30 seconds. Okay. Yeah, that's fine. Um and then finally, you could have something like prevalence like um but this isn't so prevalence is um how many you know how many scans per you know posts are um persist on the platform. One problem with this is um it doesn't take into account, you know, how popular it uh it is, right? So, if you have a bunch of scams, but they get no views, no impressions versus, you know, one scam that gets a million impressions, that that matters a lot. Um, so here you might want to use something like kind of the the the harmful impressions idea where it's how many uh people, you know, interact with the with the scam. And then let's think, you know, now that we have these metrics in mind, let's talk briefly or talk about the uh deployment. So here there's a variety of options. You could use something like shadow deployment. So here you um deploy both models uh in parallel or not yeah you you you deploy both models but you only uh serve the old problem with this is a lot of infrastructure a lot of compute uh you could use a canary deployment um where you deploy to a certain demographic and also um with that in mind let me backtrack just a bit you know on these evaluation metrics um you know it could be the case that there's a bias present, you know, over some demographic. Um, you know, maybe this model performs better over uh or not guys. What am I thinking? Um um you know, cash app scams. Maybe it's really good at identifying cash app scams, but not you know the the bank scams or or or Telegram scams uh for for that matter, right? Um so you'd want to segment um you know the evaluation to see where it's performing uh good and bad. Uh so for the canary deployment you want to deploy to certain demographics or maybe certain regions. Um but there's some bias uh as I just mentioned. Finally the kind of standard way is to do some kind of AD AB testing. And in this case since we have a very you know sensitive um you know thing we're dealing with it'd be probably best to to gradually roll it out. You don't want to just deploy the model it not perform well and then expose a bunch of people to to harmful content. So you might want to start off with like a 9010 10% split and then once you gain some confidence slowly roll it out to 50/50"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #9
  interviewer_question: time=47:07 text='and uh what metric are we using here uh to decide if we can roll out or not?'
  candidate_answer: time=47:14 text="Thank you. Um, I think of course you want to take them all into account, but um I'd probably I think harmful impressions would be um if you had to pick one, you could just weight them too. You could take some linear combination of these um as well. Um but I think harmful impression makes most sense to to use as our metric."
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Product Metrics

ITEM #10
  interviewer_question: time=48:27 text='So I I just wonder like do you work with this kind of thing or do you just happen to study about this during your time?'
  candidate_answer: time=48:36 text="Um, I mean, I have a background in ML and I, um, I've never had a real job in my life. I have no real formal training in ML. I I did my PhD in physics. So, um, I don't know if that answers your"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Communication

ITEM #11
  interviewer_question: time=59:39 text='Um I I just want to know like what level are you applying for?'
  candidate_answer: time=59:46 text="Uh yeah thanks for asking. Um there it wasn't specified. Um I I have no idea what my level will be."
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Prioritization

ITEM #12
  interviewer_question: time=59:56 text="So was that so? Okay. So this is a uh fresh grad, right? So you're So you finished your uh graduate school uh PhD and then this is your first job."
  candidate_answer: time=00:07 text="That's right. I finished uh almost 3 years ago about 2 and a half years ago. Um, Meta contacted me a few months ago uh for the interview and um yeah, this is um the only interview I have is this is basically the first interview I've ever done um postgraduation. I started a company of my own two and a half years ago and I've been working on that since then. Um so this will be my my first"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Communication

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12/ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
