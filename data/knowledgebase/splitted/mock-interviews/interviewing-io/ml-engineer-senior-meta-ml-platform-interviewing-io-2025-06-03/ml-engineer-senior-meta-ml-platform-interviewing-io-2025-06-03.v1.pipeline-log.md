<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03",
  "transcript_folder": "transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03",
  "source_id": "ml_engineer_senior_meta_ml_platform_interviewing_io_2025_06_03",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:18:06 +0200",
  "updated_at": "2026-05-20 21:31:24 +0200",
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
    "json": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/timecodes.txt",
        "en",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 21:18:06 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:31:23 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 2.0,
      "notes": null,
      "finished_at": "2026-05-20 21:31:24 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03`
- **Source ID:** `ml_engineer_senior_meta_ml_platform_interviewing_io_2025_06_03`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:18:06 +0200
- **Last updated:** 2026-05-20 21:31:24 +0200

Фильтр в IDE: `*ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/timecodes.txt`<br>`en`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.pipeline-log.md` | — | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.validation-report.md` | 2.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.pipeline-log.md`

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
SOURCE_ID: ml_engineer_senior_meta_ml_platform_interviewing_io_2025_06_03
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03
INTERVIEW_LANGUAGE: en
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00:00] [Music]
[00:00:07] Sweet, great to have you here. So, first
[00:00:09] I will briefly introduce myself and I
[00:00:11] also want to just know more about your
[00:00:13] background, your expectations. After
[00:00:15] that, we can jump into the practice. So,
[00:00:19] sweet. So, yeah, my name is Max. I'm
[00:00:22] senior engineer at meta and after
[00:00:25] joining meta I've conducted more than
[00:00:27] 500 interviews ranging from coding
[00:00:29] behavior all the way to the manager
[00:00:31] industry and with that I will hand over
[00:00:33] to you would you please briefly
[00:00:35] introduce yourself yeah sure uh my name
[00:00:37] is Brian uh I'm a software engineer with
[00:00:40] uh 13 years of experience I'm currently
[00:00:43] interviewing with Meta for the E5 loop
[00:00:46] that's going to be happening this
[00:00:47] upcoming week and upcoming week yes and
[00:00:51] So, at this point, I'm pretty deep in my
[00:00:53] prep, and I'm mostly just looking at
[00:00:54] this point to get some feedback about
[00:00:57] some gap areas where it might make sense
[00:00:58] for me to do some highv value focused
[00:01:00] studying over the next day or two and uh
[00:01:04] just working also on how I actually
[00:01:07] present my ideas and making sure that I
[00:01:09] have good pacing and things like that.
[00:01:12] Got true. So, Brian, uh is this your
[00:01:14] first time to interview with the matter?
[00:01:16] Uh no, it is not. It is not. Right.
[00:01:19] Okay. So when will be the last time? The
[00:01:22] last time was a year ago. One year ago.
[00:01:24] Still the same as the same level or the
[00:01:27] uh senior or the uh last year's was
[00:01:30] actually at an E6 level. Um and I did
[00:01:32] two systems design interviews instead of
[00:01:34] one in that loop. Uh this time around
[00:01:37] the recruiter recommendation after the
[00:01:39] phone screen was to go for E5. So I
[00:01:42] thought I would try it at E5 and see if
[00:01:44] I have more success. Sweet. I wish all
[00:01:46] the best and Okay. So that being said,
[00:01:49] since you're already familiar with the
[00:01:51] whole setup and maybe let's try to uh
[00:01:55] jump into the uh the whiteboard. Yeah,
[00:01:57] sounds good. Yep, let's do that.
[00:02:02] Okay, so here's the thing. Uh yeah,
[00:02:05] since you have you know everything, but
[00:02:06] I also want to just remind you a little
[00:02:08] bit. uh no matter that the E5 or E6 row
[00:02:12] basically I think uh we have 45 minutes
[00:02:14] for each round and specifically as the
[00:02:17] interviewer we try to finish everything
[00:02:19] we try to collect the signals from you
[00:02:22] within uh maybe the 40 minutes okay so
[00:02:25] that being said I think right now we
[00:02:27] will start from around 05 and we will
[00:02:30] end around 45 because I want to I want
[00:02:33] to just uh reiterate the time management
[00:02:35] will be always the key for the senior or
[00:02:37] even the staff
[00:02:38] Okay, that was good. Brian, with that,
[00:02:42] let's uh try this
[00:02:50] question. Hey, Brian, if you were the
[00:02:52] Vincent developer, would you please try
[00:02:54] to decide the centralized machine
[00:02:55] learning management platform? With that,
[00:02:57] I'll hand over to you. Okay, cool. Uh,
[00:03:00] so I think I'm going to need to ask some
[00:03:02] clarifying questions to make sure I
[00:03:04] understand. So I have a couple things
[00:03:06] that come to mind immediately as far as
[00:03:08] what the core operations are here but
[00:03:10] maybe I could uh kind of clarify them
[00:03:12] with you. Uh so when we say management
[00:03:15] here is this including serving uh for
[00:03:18] the purposes of actually the operations
[00:03:19] of those or is it more for like model
[00:03:21] iterations training validation and the
[00:03:24] production of the models or is it kind
[00:03:25] of an endto-end platform? Great
[00:03:27] question. That should be the end to end
[00:03:29] uh that should be the end to end
[00:03:30] platform. But more than that, let me
[00:03:32] just give you some uh give you some
[00:03:34] context here. So we have so many machine
[00:03:36] learning engineer just at the matter and
[00:03:39] to develop the machine learning efforts
[00:03:41] there are typically three stages. Okay.
[00:03:43] The first is data collection. The second
[00:03:46] is model training and the third is model
[00:03:49] serving. So basically this platform we
[00:03:52] need to cover three stages.
[00:03:54] Yep. Understood. Cool. So let's just go
[00:03:56] ahead and write those down. So we have
[00:03:58] data collection,
[00:04:01] model training, and model serving.
[00:04:04] Serving. Yes. Cool. Um, so uh yeah, I
[00:04:10] think we can probably talk about each of
[00:04:12] these different things kind of as a
[00:04:14] discrete phase and uh they'll sort of
[00:04:16] lead into each other one into the next.
[00:04:18] Um so let's maybe start with data
[00:04:20] collection. Well, actually, you know, I
[00:04:22] would like to take pause for a second
[00:04:24] here and just make sure that uh I
[00:04:26] understand the constraints. So, uh are
[00:04:28] there any constraints as far as like the
[00:04:30] number of models, the uh the size of the
[00:04:35] data that we intend to be using
[00:04:37] uh the maybe the uh sort of the the
[00:04:42] request rate or transactions per second
[00:04:44] that we can expect on the inferences
[00:04:45] during the actual model serving? Uh is
[00:04:48] there anything that we can kind of dial
[00:04:49] in to make sure that we understand where
[00:04:51] the key scaling points are? Great. And
[00:04:54] so Brad, this is a great question, but I
[00:04:56] think maybe you can just do some
[00:04:58] ballpark estimations down the line, but
[00:05:00] this I can call you. I can share with
[00:05:02] you think of I'm happy to do some
[00:05:05] ballpark estimates as well if uh if we
[00:05:07] it'll move us faster here. So I mean on
[00:05:09] the data collection side, most of these
[00:05:11] models I imagine will be training over
[00:05:12] potentially years of historical data,
[00:05:14] relatively high cardality. So we're
[00:05:17] talking terabytes at least I think uh
[00:05:19] maybe even pabytes in certain
[00:05:21] circumstances. Uh so our data collection
[00:05:24] and sort of data management systems are
[00:05:25] definitely going to need to manage big
[00:05:27] data. Yes, sounds good. So like hundreds
[00:05:31] I'll call it hundreds of terabytes of uh
[00:05:34] at least there uh model training. Um
[00:05:37] again, you know, the actual training
[00:05:39] process is going to require, you know,
[00:05:41] relatively horizontally scalable systems
[00:05:44] that uh that can actually accommodate
[00:05:46] training using that large amount of
[00:05:47] data. Um so I'll just put
[00:05:51] same. And then on the serving side of
[00:05:53] things, I'm just going to, you know,
[00:05:54] make some ballpark numbers here. I
[00:05:56] imagine that there's, you know, at
[00:05:57] least, you know, thousands to tens of
[00:06:00] thousands of individual models in use.
[00:06:02] And uh
[00:06:09] and the uh actual you know request
[00:06:11] weight for for those models uh can
[00:06:13] probably vary a lot between them and I
[00:06:15] think that's something that will be
[00:06:16] important when we talk about model
[00:06:17] serving is the specific types of use
[00:06:18] cases that we run into here but I think
[00:06:20] you know on the sharp end of model
[00:06:23] serving we should be prepared to be
[00:06:25] executing these models you know many
[00:06:28] times uh a minute uh you know for userf
[00:06:33] facing workloads Um, so let's just call
[00:06:35] it I don't know uh is like a thousand
[00:06:38] TPS uh completely off base to you for
[00:06:41] like a sort of peak load for one of the
[00:06:44] um you know higher scale models or am I
[00:06:47] off by a lot from what you're looking
[00:06:49] for or is that reasonable for jumping
[00:06:51] off? This is reasonable. Yes. Okay,
[00:06:53] cool. All right, I think we can go ahead
[00:06:55] and
[00:06:57] uh get started with that then. So data
[00:07:00] collection um maybe let's uh let's kind
[00:07:02] of ask a few more clarifying questions
[00:07:04] there when it comes to data collection.
[00:07:06] So uh
[00:07:08] the when I hear collection here I think
[00:07:10] one of two things you know there's you
[00:07:12] know computation of aggregate data uh
[00:07:14] and sort of collection in forms that are
[00:07:16] readily encodable as features uh but but
[00:07:20] data that is you know basically already
[00:07:21] being written into databases and then I
[00:07:23] also think data collection in the form
[00:07:25] of like uh online telemetry and things
[00:07:27] like that about user behavior engagement
[00:07:29] numbers and things like that. Um so
[00:07:31] let's maybe just start there. Um I think
[00:07:34] for the purposes of this you know just
[00:07:36] in time I'm going to make some
[00:07:38] assumptions about the existence of the
[00:07:43] uh data collection code in our clients
[00:07:45] of our systems and uh and just assume
[00:07:48] that they're able to you know make
[00:07:49] requests. Maybe I can just write like a
[00:07:52] a brief API uh for just like uh
[00:07:58] um let's I'm just going to completely
[00:08:00] simplify for now and just call it uh
[00:08:03] metrics um and just uh for assuming that
[00:08:08] this exists in the actual clients for
[00:08:09] actually publishing telemetry about user
[00:08:11] behavior. Um. Mhm.
[00:08:17] Okay. So, uh we're going to uh for
[00:08:20] starters, um we're going to need to
[00:08:22] receive uh and actually catalog all of
[00:08:25] this information. And that is going to
[00:08:26] be relatively high cardality and
[00:08:29] relatively um high frequency. So, uh, I
[00:08:33] I just want to kind of come up here
[00:08:34] because I'm realizing that I could spend
[00:08:36] a lot of time here to to like, uh, that
[00:08:39] could be a whole system design interview
[00:08:41] in and of itself. Is it fair for me to
[00:08:43] start with the data existing in a
[00:08:45] database or would you like me to include
[00:08:47] sort of upstream of the actual uh uh
[00:08:51] writing of telemetry data? I see. Hey
[00:08:55] Brian, I think just for today's uh just
[00:08:57] for the data collection part, right? I
[00:08:59] will expect you to just write some data
[00:09:01] or maybe read some data just from the
[00:09:03] database. Yeah. Okay. So, so let's go
[00:09:06] ahead and assume that that data actually
[00:09:07] lands in some databases. And so we're
[00:09:10] probably going to have a bunch of
[00:09:11] different databases here. Um
[00:09:15] so I'll just uh give them a couple.
[00:09:18] Brian, I I do have a question here. So
[00:09:20] are you trying to just start from the
[00:09:23] high level design or I want to I want to
[00:09:25] understand what would be your
[00:09:26] presentation flow here. Yeah,
[00:09:28] absolutely. Uh that's a great question.
[00:09:30] So I yeah I think I'd like to just sort
[00:09:31] of identify key components uh at a high
[00:09:34] level and then we can sort of dive
[00:09:36] deeply into the uh actual underlying
[00:09:39] architecture in in cases. I see. But
[00:09:42] before that brand I do have a very quick
[00:09:44] suggestion here because I think uh we
[00:09:46] would I would like to start from the
[00:09:48] future part the functional requirements.
[00:09:50] So basically I think right now we have
[00:09:52] three stages. They are pretty high
[00:09:53] level. Let's try to break down a little
[00:09:55] bit for you. Okay. Yeah sure that
[00:09:57] absolutely that sounds good. So let's
[00:09:59] break that down a little further. Um so
[00:10:02] uh I'll just go ahead and move this over
[00:10:04] here as an assumption. Um so breaking
[00:10:07] that down. So on the model training side
[00:10:09] of things, I'll just start with the
[00:10:11] models themselves.
[00:10:14] Uh so what do we actually need to do for
[00:10:16] the model training? So there's going to
[00:10:18] need to be a data access layer there. Uh
[00:10:20] and we're going to need a mechanism for
[00:10:26] uh
[00:10:28] the exe. So there's the actual training
[00:10:31] execution uh in terms of like the uh the
[00:10:33] compute that we'll run this on.
[00:10:37] um are going to need
[00:10:41] uh model publishing. Uh so like when a
[00:10:44] new a new version of the methodology or
[00:10:47] some tweaks to the features that we use
[00:10:48] uh that needs to be publishable
[00:10:50] somewhere and then we're going to need
[00:10:52] to actually execute training on those.
[00:10:54] then we're probably going to need um
[00:10:57] model validation and guard rails after
[00:11:00] the actual training effort to make sure
[00:11:02] that we uh have uh you know a high
[00:11:06] quality bar for the actual predictive
[00:11:08] power of the models that we produce.
[00:11:11] Um and so I'm and then uh once we've
[00:11:16] actually hit that quality bar, we want
[00:11:18] to actually move ahead to model serving.
[00:11:20] I'll go with model deployment
[00:11:23] um as kind of like the core uh areas
[00:11:26] that I think about when I think about uh
[00:11:28] an ML management uh for the sort of the
[00:11:31] well I guess I'm sort of beginning to
[00:11:32] blend uh model training and serving.
[00:11:35] Um so it's not necessarily that this is
[00:11:38] all part of the the training uh step but
[00:11:41] rather that we're just sort of breaking
[00:11:43] it down a little further.
[00:11:45] Um, so the,
[00:11:48] uh, I think for the most part, um, and
[00:11:52] then there's going to be, uh, let me
[00:11:56] collect my thoughts for one second.
[00:12:03] Cool. Yeah. Okay. So, the uh, the
[00:12:06] mechanisms here, I think, what are what
[00:12:08] are the sort of data stoages uh, and um,
[00:12:11] that we're going to need? One thing that
[00:12:12] comes to mind for me is like what is
[00:12:14] what does it mean for the model actually
[00:12:15] to be deployed. We're going to need the
[00:12:18] uh and what the data that's getting used
[00:12:21] for training execution and also
[00:12:22] validation presumably some split like a
[00:12:25] training test split of that data. Um
[00:12:27] we're going to need a feature data store
[00:12:29] of the actual features themselves. Uh so
[00:12:32] and there so there's probably also going
[00:12:33] to be a step at the beginning uh ahead
[00:12:35] of all of this in the data collection
[00:12:37] side of things that is just sort of um
[00:12:40] you know a registry of the creating a
[00:12:43] registry of the potentially
[00:12:44] heterogeneous data tables. So like a a
[00:12:48] data registry. Um and then we might also
[00:12:52] have a feature encoding
[00:12:55] step. Um
[00:12:58] uh there might be for example you know
[00:13:00] feature sets that are in reuse by
[00:13:01] multiple different types of models. And
[00:13:03] so being able to share those things
[00:13:04] efficiently uh to prevent retraining or
[00:13:07] to prevent you know large scale
[00:13:09] processing over and over again would be
[00:13:11] really useful.
[00:13:13] And then when I say model publishing
[00:13:16] here, publishing is maybe uh you know a
[00:13:18] misnomer. What I'm really talking about
[00:13:19] is uh iterations of models by actual ML
[00:13:22] engineers and data
[00:13:25] scientists. Um so there's going to need
[00:13:28] to be an operation um for them to
[00:13:30] actually upload, you know, the latest
[00:13:32] code or maybe it would be triggered off
[00:13:34] of a merge to a a code pipeline. Um
[00:13:38] okay. And then we would sort of
[00:13:39] automatically flow into the remaining
[00:13:41] steps downstream of that. Um, so I'll
[00:13:43] come up for air there. I think that uh I
[00:13:45] I have maybe uh I have maybe enough to
[00:13:49] go off of here where we can start
[00:13:50] putting um pieces on the board so to
[00:13:52] speak to actually identify the
[00:13:55] relationships between the components and
[00:13:56] make sure uh let's before one more thing
[00:14:00] before I go ahead and start doing that
[00:14:02] let's just kind of write down what are
[00:14:03] the core operations that uh
[00:14:06] we need to support. So we need to
[00:14:08] support registering registering new
[00:14:12] data.
[00:14:14] Um for example, if there's a new data
[00:14:16] set that gets in use, uh or as we start
[00:14:19] collecting new types of data from our
[00:14:21] users, uh new pages, things like that,
[00:14:24] um we are going to want to uh publish
[00:14:30] um new model iterations.
[00:14:35] um we are going uh and then
[00:14:41] the process for the way that I'm
[00:14:44] imagining how this would work at at a
[00:14:46] high level is that in in the general
[00:14:48] case the uh training and the validation
[00:14:52] of that training is stuff that we would
[00:14:53] definitely want to automate downstream
[00:14:55] of the actual publishing of that model
[00:14:56] iteration but I can imagine that there's
[00:14:58] also going to want to be automated
[00:15:00] retraining drift detection to trigger
[00:15:02] retraining and things like that um
[00:15:04] So uh so we're probably going to want an
[00:15:06] operation for actually just running
[00:15:08] training
[00:15:12] and that will probably take a specific
[00:15:13] model. Um and then uh we'll also want to
[00:15:18] deploy um the ability to to redeploy
[00:15:21] specific models uh if that is something
[00:15:24] that we need in cases where we might
[00:15:26] need to do a roll back to reduce the
[00:15:27] blast radius of failures or things like
[00:15:29] that.
[00:15:33] Uh and
[00:15:35] um then finally uh the last step for the
[00:15:38] actual serving side of things um I think
[00:15:40] we're going to need um you know
[00:15:43] operations for actually executing the
[00:15:45] inferences uh which may vary the the
[00:15:48] nature of the inference may may vary on
[00:15:49] the model but the actual um so I'll just
[00:15:52] say
[00:15:54] serving let's call it inference for now.
[00:16:02] Cool. Um, all right. So, now we have
[00:16:05] some operations that we can kind of run
[00:16:07] through as we build this to make sure
[00:16:08] that we sort of are have covered all of
[00:16:10] the core uh use cases for how to
[00:16:14] actually make the platform usable. Um,
[00:16:17] and then I think we can uh we can go
[00:16:20] ahead and um and get started. So, let's
[00:16:24] see. So I think uh how I would choose to
[00:16:28] build this is that um in the general
[00:16:30] case I would like to you know not think
[00:16:34] too hard about something like the data
[00:16:36] register. The idea there is that
[00:16:37] basically we're going to want to make
[00:16:39] data discoverable across the
[00:16:42] organization. Probably there will be you
[00:16:44] know a couple different ways that it
[00:16:46] might be stored based on the type of
[00:16:47] data. And so we'd like there to be some
[00:16:50] kind of service that's when uploading a
[00:16:52] new data set, when creating a new data
[00:16:54] set, uh or when maybe you know calling a
[00:16:57] partition finished on data that's sort
[00:16:59] of streaming and happening in real life
[00:17:00] and and registering that in a way that
[00:17:02] it is accessible to training uh
[00:17:06] mechanisms. Uh we're going to want some
[00:17:08] kind of uh so I'm going to assume that
[00:17:11] we have potentially a bunch of different
[00:17:13] kind of uh you know types of of data
[00:17:16] here. Mhm. So I'm just going to call
[00:17:20] this and uh there's going to be some
[00:17:25] layer on top of that that is just uh a
[00:17:28] kind of a a registry. So
[00:17:34] uh and it will be the responsibility of
[00:17:36] this registry to sort of act as you
[00:17:39] would expect almost on a search engine
[00:17:40] for all of the data that you have where
[00:17:43] um the process of actually ETL processes
[00:17:46] that load data will maybe also make an
[00:17:48] API call um to uh to the registry. So,
[00:17:54] I'll just uh assume that we have, you
[00:17:56] know, it's a maybe a little out of scope
[00:17:58] for uh our purposes at this exact
[00:18:00] moment, but we can go back and talk in
[00:18:01] more detail about that. So, I'll just
[00:18:02] assume that there's some ETL
[00:18:07] um that uh will maybe write this data
[00:18:10] into, you know, blob storage or into
[00:18:13] uh sorry, how do I call five is the
[00:18:15] line? I'm I'm still getting used to
[00:18:17] this. Uh no worries. Yeah, got to get
[00:18:19] used to the hotkeys here. So some
[00:18:21] processes will publish data and it will
[00:18:23] make that data available to all of our
[00:18:25] downstreams by you know registering a
[00:18:27] new partition or indicating uh that uh
[00:18:30] some data set is now completed. Um and
[00:18:35] the actual ML platform will sort of be
[00:18:38] built on these these data building
[00:18:40] blocks. So when it comes to the actual
[00:18:45] um feature encodings I I can think off
[00:18:48] the top of my head of kind of two ways
[00:18:49] out. Some of them might be very model
[00:18:51] specific in which case that could almost
[00:18:52] you know be included in the model code
[00:18:54] itself for how we might want to do that.
[00:18:57] There are probably plenty of well-known
[00:19:00] encodings uh that are reusable and there
[00:19:04] actually may be uh we we may want to run
[00:19:07] sort of like a second layer of ETL in
[00:19:09] effect that uh is responsible for
[00:19:13] reading these sort of like raw tables,
[00:19:15] staging them, uh potentially doing some
[00:19:17] transformations on that data and
[00:19:19] otherwise generating sort of partial
[00:19:21] feature encodings uh of the actual
[00:19:25] uh you know beginning to look like the
[00:19:27] data that will actually be in use in the
[00:19:29] in the training itself. So I'm just
[00:19:31] going to
[00:19:32] uh you know for now I'll just call that
[00:19:39] feature I'll just call this generic
[00:19:42] um and in fact I think I would like this
[00:19:46] to sort of feedback directly into the
[00:19:49] data registry itself such that uh there
[00:19:52] are sort of you know feature sets that
[00:19:55] are uh registered with the data registry
[00:19:57] and uh they they we can use those as if
[00:20:01] they were the um you know the raw data
[00:20:03] and just sort of make them available to
[00:20:04] you streaming processing in the same
[00:20:06] way. Um and then when it comes to the
[00:20:09] actual model training okay so this is
[00:20:12] where we kind of get into the meat of
[00:20:13] the system a little bit more and so
[00:20:16] let's assume for now that the model
[00:20:19] training is going to be uh a you know a
[00:20:23] small platform of its own. So I imagine
[00:20:25] that for example there are probably
[00:20:26] going to be uh I'll just write draining
[00:20:29] over it for now just to uh kind of
[00:20:32] organize my own thoughts
[00:20:34] here. Um and let's maybe start with the
[00:20:37] actual rather than the the edge of the
[00:20:39] system. Let's start with the building
[00:20:40] blocks. Right? There's going to need to
[00:20:42] be uh some compute instances that are
[00:20:45] ideally you know very horizontally
[00:20:46] scalable for uh you know I'm I work with
[00:20:50] AWS a lot. So something like SageMaker
[00:20:52] compute uh or the underlying EC2
[00:20:55] instances for example. So we're going to
[00:20:57] need the actual um
[00:21:02] uh compute instances and these are going
[00:21:04] to be what get uh allocated for the
[00:21:08] purposes of running. There is a new
[00:21:09] training request coming in for a
[00:21:11] specific uh system. There will then we
[00:21:15] need kind of like a a a layer on top of
[00:21:20] this uh a supervisory layer that would
[00:21:22] be responsible for allocating specific
[00:21:25] partitions from the data registry to be
[00:21:28] uh used in training for uh kind of
[00:21:31] sharding out the individual training to
[00:21:33] individual uh instances. So I think we
[00:21:37] can go ahead and assume that there will
[00:21:39] be uh sort of like a training management
[00:21:42] layer.
[00:21:45] Uh so I'm just going to call this uh
[00:21:51] the like the training
[00:21:58] organizer.
[00:22:01] Uh sorry, let me uh grow these a little
[00:22:04] bit.
[00:22:08] Okay. So, as written right now, this is
[00:22:09] kind of like a single instance. I think
[00:22:11] that itself would probably uh be
[00:22:13] something that we could load balance
[00:22:15] across a couple different instances. Um,
[00:22:18] so maybe I'll just
[00:22:20] uh and then ultimately the actual uh
[00:22:25] sort of edge of the system would be some
[00:22:27] kind of API gateway uh that is
[00:22:29] responsible for receiving requests to
[00:22:32] train our model.
[00:22:34] um and then farming those out. Uh we
[00:22:38] would probably want to separate concerns
[00:22:39] from the actual API gateway that might
[00:22:41] do authentication or making data access
[00:22:43] uh middleware permissions requests,
[00:22:45] things like that. um to uh decouple that
[00:22:50] from the actual responsibility of okay,
[00:22:52] we have a specific model version and we
[00:22:56] know which and so the training organizer
[00:22:59] is probably going to be communicating
[00:23:01] with the data
[00:23:03] registry and uh that would sort of be
[00:23:07] birectional in order to sort of maybe
[00:23:08] get a manifest of the number of
[00:23:10] different partitions within a specific
[00:23:12] set of date ranges or something like
[00:23:13] that. And then the individual uh sort of
[00:23:17] allocation of those to compute units for
[00:23:20] the purposes of doing partitions and the
[00:23:22] training I think is something that would
[00:23:25] be happening uh sort of directly between
[00:23:28] the the compute would sort of request
[00:23:30] for directly data registry.
[00:23:33] Uh and so the uh I I spoke very briefly
[00:23:37] I kind of glossed over uh model version
[00:23:40] as part of the API gateway here. So
[00:23:42] yeah, so there's going to need to be
[00:23:43] some uh repository of the actual I'm
[00:23:47] realizing that I uh did not really uh
[00:23:51] kind of set up my space. Yeah, no
[00:23:54] worries effectively here. I'll move some
[00:23:57] stuff around if that's okay.
[00:23:59] So um I'm going to assume that we have
[00:24:02] some store of actual
[00:24:05] uh models themselves. Okay. And uh there
[00:24:10] there will be some requests that are
[00:24:12] triggered to the API gateway. Oh, that's
[00:24:15] the wrong thing. Uh that will use
[00:24:19] models. Um and so I identified a couple
[00:24:23] of these off the top of my head. So we
[00:24:24] might want to do ad hoc training, which
[00:24:25] is something where like an actual user
[00:24:28] uh would
[00:24:33] trigger. Uh and then we could also have
[00:24:36] some kind of like uh so an ad hoc
[00:24:39] request might say um you know train this
[00:24:42] model uh maybe in development purposes
[00:24:49] um and so I'll just kind of write uh
[00:25:02] uh and so the uh if we assume that
[00:25:06] there's kind of like a a submit training
[00:25:09] uh and that that might take some
[00:25:10] configuration about how you know
[00:25:12] hyperparameters or the uh you know which
[00:25:16] model to use what how far back to go for
[00:25:18] specific date ranges on on the data
[00:25:20] things like that be included there but
[00:25:22] uh ultimately the actual events there
[00:25:25] could be a couple different types of
[00:25:26] events to do this there might be one
[00:25:28] that's sort of triggered by uh you know
[00:25:30] continuous integration or continuous
[00:25:31] deployment uh as Well, whenever a new
[00:25:35] version of the model actually happens,
[00:25:38] uh uh um a new new version of model
[00:25:40] code, I should say, uh is published, uh
[00:25:44] that could be something that actually
[00:25:46] happens here where maybe there's
[00:25:48] actually an event.
[00:25:50] uh feel like I've seen a way for people
[00:25:52] to do kind of curves lines that I don't
[00:25:54] actually know how to do. But the idea
[00:25:55] being that you know there could be some
[00:25:58] uh stream of events from the publishing
[00:26:00] of new models here that's
[00:26:03] uh that
[00:26:05] itself can I oh is this what I want?
[00:26:08] Perfect. Um
[00:26:15] so maybe you know there's ad hoc maybe
[00:26:18] uh when stuff isn't was is unpublished
[00:26:20] or still in development and then sort of
[00:26:22] as a new model is finalized after it
[00:26:24] gets reviewed and and ends up getting
[00:26:26] published to the sort of repository of
[00:26:28] model methodologies maybe a stream of
[00:26:30] the publishing of those events will go
[00:26:32] to some CI/CD process which will then
[00:26:33] trigger the training and all the
[00:26:35] downstream that happens after that. Mhm.
[00:26:38] So, okay, just kind of checking in with
[00:26:39] myself here. So, uh we have covered the
[00:26:42] idea of uh data registry. So, I'm going
[00:26:45] to um just call this
[00:26:52] uh that I you know assuming that the
[00:26:55] there's some mechanism baked into our
[00:26:57] ECL processing platform or pipeline such
[00:27:00] that as we actually generate new data
[00:27:02] partitions, we register those with a
[00:27:03] data registry. Okay, so we have that
[00:27:05] here. um the actual publishing of the
[00:27:08] model iterations itself. Uh I'm not
[00:27:10] going to go too far into that. You know,
[00:27:12] a code review process probably going to
[00:27:14] be in place uh and and things like that.
[00:27:17] But so in terms of actually publishing a
[00:27:19] new version of a model that I want to
[00:27:20] get trained um is something that would
[00:27:22] just sort of be upstream of this models
[00:27:25] DB itself. So maybe I'll just have a
[00:27:27] line into
[00:27:28] that. There's some operation for publish
[00:27:32] happening.
[00:27:38] Okay. Uh let's see. Um so I feel like
[00:27:43] we've gone through most of the pretty
[00:27:44] high level building blocks here for
[00:27:46] actually getting to a place of the
[00:27:48] actual training happening. Um one thing
[00:27:50] that we haven't done is where's the
[00:27:51] output of that training actually going?
[00:27:53] Where is sort of the models themselves
[00:27:55] landing? Uh we're going to need some
[00:27:57] kind of
[00:27:59] um that's not what I wanted to say.
[00:28:02] We're going to need some kind of
[00:28:05] um finished uh model registry.
[00:28:15] Uh and the idea being here that sort of
[00:28:19] the results the training would be
[00:28:20] complete. Uh the actual data that is
[00:28:23] generated um in the form of those models
[00:28:25] might uh need to be written to sort of
[00:28:29] model storage itself. Uh
[00:28:32] so um
[00:28:38] oops I hope that's relatively clear the
[00:28:41] different shape encodings that I'm using
[00:28:43] of circles for for data
[00:28:47] storage. Uh I'm just going to instead of
[00:28:50] making this bigger I'll just write next
[00:28:52] to
[00:28:55] them.
[00:28:57] Uh and so the idea being that basically
[00:29:00] the actual compute will um and um
[00:29:03] informing the training organizer of Oh,
[00:29:07] what's okay? How do I stop this? Uh oh
[00:29:11] boy, is there a cancel button? Okay,
[00:29:14] there we go. Sorry. Uh so when the
[00:29:18] training is actually completed, there's
[00:29:20] going to be some training output that
[00:29:22] constitutes the actual model, the
[00:29:23] artifacts uh of the the sort of data
[00:29:27] that's been computed over and the
[00:29:28] weights of the model itself. Um and so
[00:29:31] those weights are going to need to get
[00:29:32] published. Maybe just to disambiguate
[00:29:35] that, we'll call this
[00:29:37] um weight storage here. And so the
[00:29:41] [Music]
[00:29:43] uh I would say that uh rather than kind
[00:29:46] of single threading all of that through
[00:29:48] the individual organizer, I think the
[00:29:49] individual training as part of the
[00:29:51] organization, we could maybe establish
[00:29:52] some space uh or some prefix maybe a
[00:29:56] model revision number uh for that
[00:29:59] training in particular. And the
[00:30:01] individual training compute units can be
[00:30:03] responsible for writing their partitions
[00:30:05] of the weights into the weight storage
[00:30:07] system. And then at the actual
[00:30:09] completion of that
[00:30:16] um so the training will actually
[00:30:19] register the model to indicate hey this
[00:30:21] uh this model is
[00:30:26] um the trained model specifically
[00:30:29] um and so here I'll
[00:30:37] Okay. Okay. So now I do feel like we
[00:30:40] have been relatively end to end on what
[00:30:42] we need to do for the actual training
[00:30:44] itself. Um, importantly we have we still
[00:30:47] have a few key elements that are missing
[00:30:49] here on the actual validation of these
[00:30:52] whether or not this it's is itself going
[00:30:54] to be um you know usable or if we need
[00:30:58] to go back and do another iteration or
[00:31:00] something like that. Uh and so how is
[00:31:02] that actually going to happen? So, um,
[00:31:05] we're going to need to add some kind of
[00:31:08] procedural validation that's going to
[00:31:10] essentially be batch inference over, um,
[00:31:13] some subset of the training data that
[00:31:15] was reserved back for the purposes of
[00:31:17] doing validation.
[00:31:19] Um, and in order to actually do that,
[00:31:24] we're going to need to trigger that sort
[00:31:25] of after the training itself has
[00:31:27] actually completed.
[00:31:29] Um, and so I need to think a little
[00:31:33] carefully about this because one thing
[00:31:35] that's coming to mind for me is like
[00:31:36] does it make sense to always be
[00:31:37] registering the train model and
[00:31:39] publishing the weights if it turns out
[00:31:40] that the model itself is not remotely
[00:31:41] predictive? Um, and I think the answer
[00:31:44] is yes because we're probably going to
[00:31:45] want to introspect the nature of that
[00:31:46] lack of prediction and look at the data,
[00:31:49] look at the weights that were actually
[00:31:50] produced and maybe use that to guide
[00:31:52] some intuition about how we might evolve
[00:31:55] the model forward. So, uh, I was
[00:31:58] thinking for a minute, does it make
[00:31:59] sense to maybe, uh, do the validation
[00:32:01] upstream of publishing to the model
[00:32:03] registry? And I think what I'd rather do
[00:32:05] instead is evolve the idea of the model
[00:32:08] registry that there's maybe different
[00:32:10] states that models can be in and we can
[00:32:12] sort of establish guardrails. Um so when
[00:32:15] it comes to serving and publishing the
[00:32:17] models from the registry into the actual
[00:32:20] edge layer of the system that would be
[00:32:22] customerf facing um it would only be
[00:32:24] doing that over models that are either
[00:32:27] under underactive experimentation or are
[00:32:30] uh you know known working and have
[00:32:33] satisfactory
[00:32:34] criteria across some kind of model
[00:32:36] evaluation criteria. So I think at this
[00:32:40] point we need to kind of make sure we
[00:32:42] get through everything. Um so let's go
[00:32:46] ahead and try to uh speed back up. Um so
[00:32:49] model validation is as we said it's
[00:32:52] going to be functionally similar to the
[00:32:53] actual training compute. So I think the
[00:32:56] underlying uh compute instances and
[00:32:58] compute engine here could be used for
[00:32:59] both training and validation. uh
[00:33:05] and because fundamentally I think uh the
[00:33:09] the workloads there are relatively
[00:33:11] similar. Um and uh so the training
[00:33:16] organizer itself could be something as a
[00:33:20] layer that is responsible for a couple
[00:33:22] different types of operations. So there
[00:33:24] could be a
[00:33:25] train operation and there could be a
[00:33:28] validate operation and depending on
[00:33:32] which of those things
[00:33:35] uh that
[00:33:36] is so sorry which operation that we're
[00:33:39] doing we'll either be reading from the
[00:33:40] raw data registry of feature encodings
[00:33:43] and of okay so actually so one thing
[00:33:46] that I missed here um sorry coming up
[00:33:49] for air I know I'm talking in a couple
[00:33:50] different directions at the same time so
[00:33:52] some of this feature encoding ET L like
[00:33:54] we said is going to be generic and we
[00:33:56] want to
[00:33:58] um but the the encodings that we
[00:34:01] generate as part of the training compute
[00:34:03] here we may optionally be interested in
[00:34:07] publishing those back to the data
[00:34:08] registry um and like a model specific
[00:34:12] namespace or or otherwise to kind of
[00:34:15] introduce some idea of checkpointing so
[00:34:17] we can sort of speed up and make the
[00:34:19] training itself a little more efficient
[00:34:20] in the future. Um, so I'm just going to
[00:34:23] make this birectional for now just
[00:34:25] because there I think I can I can
[00:34:27] conceive of circumstances where we would
[00:34:28] want encodings that are sort of defined
[00:34:31] in the uh in the model code itself to
[00:34:34] still be publishable into the data
[00:34:36] registry in some way in which case we
[00:34:38] would need to potentially write from the
[00:34:40] training compute into the
[00:34:43] uh sort of the the feature stores as
[00:34:46] well as the actual weight storage. Um.
[00:34:48] Mhm.
[00:34:50] Okay. So, uh, coming back to my original
[00:34:52] train of thought here. So, the training
[00:34:54] organizer could be responsible for both,
[00:34:57] um, you know, issuing out the training
[00:34:59] requests and also issuing out
[00:35:00] validation. Uh, validation is usually a
[00:35:03] smaller subset of the data than the
[00:35:04] training, but it could still be
[00:35:05] potentially very large if the overall
[00:35:07] data is really really big and we reserve
[00:35:09] back like 10% of it in order to do a
[00:35:11] relatively exhaustive uh, validation
[00:35:14] over it.
[00:35:15] Um so uh in in that case I think we
[00:35:19] would still want to shard it over uh
[00:35:21] multiple different horizontally scalable
[00:35:23] compute instances. Um and the in in that
[00:35:28] circumstance what would the
[00:35:31] uh what where would those outputs
[00:35:33] actually go? Um I think we would need uh
[00:35:36] some sort of reporting layer. Uh so I'm
[00:35:40] going to oops sorry wrong thing here.
[00:35:49] So some layer that's responsible for
[00:35:51] doing validation reporting that will
[00:35:52] basically take the results uh from
[00:35:56] actually running the validation
[00:35:57] operations and actually publish that
[00:36:00] somewhere. Um
[00:36:03] that is
[00:36:09] uh these validation results are things
[00:36:12] that maybe depending on the uh stage of
[00:36:15] maturity of the model could be manually
[00:36:16] reviewed if we're still in an
[00:36:18] experimentation phase. Uh this is
[00:36:20] something that could be also happening
[00:36:21] as part of a CI/CD pipeline for the
[00:36:23] purposes of establishing you know if we
[00:36:26] have automated guardrails in place
[00:36:28] already. uh then I think we would need
[00:36:32] to
[00:36:33] um sorry not need but we would be able
[00:36:36] to sort of move ahead with the actual
[00:36:38] publishing into uh or sort of setting
[00:36:42] the status.
[00:36:44] Uh so I'm going to say that there's
[00:36:47] maybe
[00:36:48] um a couple different operations on the
[00:36:51] model registry here or sort of so we we
[00:36:54] might want to register that a model is
[00:36:57] uh is trained and then we might also
[00:36:59] want to
[00:37:02] um uh publish validated and publish
[00:37:07] itself might maybe just be setting some
[00:37:08] state in the model registry on the the
[00:37:12] model itself. else that indicates
[00:37:16] uh uh you know
[00:37:19] um maybe if we have you know an enum of
[00:37:21] different states that it could be in
[00:37:30] uh like maybe we ran the validation
[00:37:33] criteria and then we had a miss or
[00:37:35] something and so we might want to
[00:37:36] preserve those artifacts in the
[00:37:38] registering and weight storage okay so
[00:37:40] uh I feel like I've gone into suffic
[00:37:42] sufficient detail to cover the basics of
[00:37:44] the actual training of the model,
[00:37:46] different versioning of them um and the
[00:37:49] execution of the training, the
[00:37:50] validation of that. Let's talk uh
[00:37:52] deployment. So um skipping over for a
[00:37:55] minute the idea of how we decide when
[00:37:57] we're going to do the deployment um
[00:38:00] which I think is important and we can
[00:38:01] discuss that, but let's just assume for
[00:38:03] a minute that we don't have to think
[00:38:04] about that. What does deployment
[00:38:05] actually entail for us here? So uh
[00:38:08] there's probably a couple different
[00:38:09] types of model use cases that I can
[00:38:11] think of. Some of them are going to be
[00:38:13] online models that are actually running
[00:38:15] as like in the client or in response to
[00:38:17] client behavior um at the edge of our
[00:38:20] system. And some of them are things that
[00:38:22] are maybe more expensive uh maybe the
[00:38:24] types of things that we might want to do
[00:38:27] offline, you know, batch generation of
[00:38:30] inferences and then bloating those batch
[00:38:31] inferences into some kind of cache or
[00:38:33] something like that. So I can think of
[00:38:36] uh I think for the purposes of talking
[00:38:38] about model deployments, I'm going to
[00:38:40] only focus on the former of those two
[00:38:42] things. The latter is really not all
[00:38:44] that different conceptually than the ETL
[00:38:46] that we're doing to actually produce
[00:38:48] data of facts versus inferences. Uh so
[00:38:51] we might want to extend our data
[00:38:52] registry a little bit in some way to
[00:38:54] make sure that we can differentiate
[00:38:55] between numbers that we know that are
[00:38:58] stemming from facts and numbers that are
[00:39:00] you know or or not necessarily numbers
[00:39:02] but data points and tables that are
[00:39:05] inferences. But batch inference I think
[00:39:08] is really fundamentally pretty similar
[00:39:09] to ETL. So I'm going to kind of gloss
[00:39:11] over that for the moment. Mhm. When it
[00:39:13] comes to uh
[00:39:15] the the former of these two options,
[00:39:18] which is sort of online models, um we're
[00:39:20] going to need those models to be
[00:39:22] publishable to some uh some sort of edge
[00:39:25] servers where the model can actually um
[00:39:29] live. And so what I mean by that is I
[00:39:31] think the actual weights themselves for
[00:39:32] most of these were probably going to
[00:39:34] need to be in memory in order to ensure
[00:39:36] a performant experience for customers.
[00:39:39] Um so when the actual publishing
[00:39:42] operation I think is going to be some
[00:39:45] mechanism by which we actually get
[00:39:47] weights
[00:39:49] uh in
[00:39:56] caches and that is something that
[00:39:58] basically from the actual weights data
[00:40:00] storage we might uh publish and so I'm
[00:40:04] writing this out as one cache you can
[00:40:06] consider this as a distributed cache
[00:40:07] where there's potentially a bunch just
[00:40:11] uh bunch of different types of models.
[00:40:13] Um maybe one per model or uh depending
[00:40:16] on the actual you know server form
[00:40:19] infrastructure it might make sense to
[00:40:21] have there be one logical cache here
[00:40:23] that has a bunch of different uh
[00:40:26] entities in it with and the keys would
[00:40:28] indicate which particular type of model
[00:40:30] we're using. And then the importantly
[00:40:33] for whatever application is actually
[00:40:35] routing user requests to use these
[00:40:38] weights and to use
[00:40:41] um there's going to need to be some kind
[00:40:43] of uh what I would call an analog to
[00:40:46] service discovery uh of in informing the
[00:40:49] application servers. So let's go ahead
[00:40:51] and like I said uh I can't really scroll
[00:40:54] here very easily. Can I? I'm going to
[00:40:55] zoom out. Okay. Um so I'm going to
[00:41:00] assume that there are application
[00:41:02] servers uh that are responsible for uh
[00:41:06] you know there's probably an API gateway
[00:41:07] and a whole architecture upstream of
[00:41:09] this but fundamentally there are you
[00:41:10] know service workers or some uh compute
[00:41:13] layer that's going to be responsible for
[00:41:15] routing requests for customers and the
[00:41:20] uh actual requests themselves
[00:41:24] uh might uh interact with the weights
[00:41:27] cache to fetch some specific weights or
[00:41:29] and then actually do an inference. Um
[00:41:40] uh and so now we have kind of like a
[00:41:43] pseudo end to end but with a a
[00:41:45] relatively glossed over middle here of
[00:41:47] what is the actual um mechanism look
[00:41:51] like for how we actually do that
[00:41:52] deployment. So I think
[00:41:55] uh probably something relatively similar
[00:41:58] to what we talked about for some of
[00:41:59] these other aspects where ideally I'd
[00:42:01] like this to be a continuously deploying
[00:42:03] system so that we can rapidly evolve our
[00:42:06] system uh and make sure that we can sort
[00:42:08] of seamlessly per uh deploy new weights.
[00:42:10] So I would imagine that sort of the
[00:42:13] validation results would sort of
[00:42:14] directly inform uh in the in the event
[00:42:17] of sort of passing. Um so let's see like
[00:42:20] uh it's kind of two outcomes here,
[00:42:22] right? is pass and fail more or less.
[00:42:27] Uh and so
[00:42:30] um in the event of uh a pass I feel like
[00:42:34] we would sort of plug back into our
[00:42:36] continuous integration um now that there
[00:42:39] is uh you know approvals have been
[00:42:41] satisfied and we can proceed to the next
[00:42:43] step that would be responsible for
[00:42:45] actually interacting with the the model
[00:42:48] registry to find where the weights are
[00:42:50] for a specific model.
[00:42:54] uh and ultimately those weights would
[00:42:58] need to be published into the weights
[00:43:00] cache and so some system would need to
[00:43:04] be responsible for writing to the cache
[00:43:07] the results from the the model registry.
[00:43:12] Um okay so let's see let's just kind of
[00:43:15] go back through my checklist over here
[00:43:16] to the left. So, we've got our data
[00:43:18] registry. We've got this idea of feature
[00:43:20] encodings, writing back into the data
[00:43:21] registry. Um, I don't think I actually
[00:43:24] published a lot in the design here about
[00:43:26] model iterations and versioning of the
[00:43:28] models themselves. That's something that
[00:43:29] I think I would probably put on the data
[00:43:31] model for how we actually manage the
[00:43:34] versions of the model in the model
[00:43:35] registry and that and the training
[00:43:37] organizer would be aware of that. So we
[00:43:39] can maybe talk a little bit about
[00:43:42] um that sort of at the end but I do feel
[00:43:45] like we have you know at least verbally
[00:43:47] discussed the ways that we could care
[00:43:49] about model iteration model versioning.
[00:43:51] Okay. So one thing I actually mentioned
[00:43:52] up at the beginning that I haven't des
[00:43:54] uh included here is online maintenance
[00:43:56] and monitoring of these models and
[00:43:58] specifically drift detection. So you
[00:44:00] know as the models after the models are
[00:44:01] deployed they you know get stale over
[00:44:04] time and user behavior uh you know is
[00:44:07] evolutionary with respect to these. So
[00:44:10] we might want to be observing the actual
[00:44:13] inferences and sort of the um the
[00:44:16] behavior of the inferences and also user
[00:44:18] behavior uh as the model itself is live.
[00:44:22] So I think in addition to actually just
[00:44:24] getting the weights and doing the
[00:44:25] inferences, we're probably going to want
[00:44:27] some sort of uh reporting system. Mhm.
[00:44:32] Uh
[00:44:33] so live model reporting I'll call it for
[00:44:37] now.
[00:44:38] Um and basically the application servers
[00:44:41] that are sort of uh fetching weights
[00:44:43] doing these inferences would be
[00:44:45] recording those inferences.
[00:44:52] uh maybe they would sort of record some
[00:44:54] information about the user or so I'm
[00:44:56] just going to put calls context actually
[00:44:57] because it's not necessarily the user
[00:44:59] but um you know we might want to if for
[00:45:02] example we're seeing that there's a
[00:45:05] massive spike in you know positive uh
[00:45:08] positive rate coming out of the
[00:45:10] inferences for one specific browser or
[00:45:12] something that might be something that'd
[00:45:13] be really interesting for us. So we want
[00:45:14] to know as much as we can about the
[00:45:16] context for both the user and the
[00:45:18] environment when we're actually looking
[00:45:20] at these kind of inferences.
[00:45:23] Um we can kind of crossorrelate that
[00:45:26] with some of the telemetry data that
[00:45:28] actually fed into the data registry
[00:45:29] itself. And ultimately we would want
[00:45:32] this live model reporting to potentially
[00:45:35] um so I'll just call this uh model
[00:45:38] telemetry.
[00:45:41] um telemetry is maybe a little bit of an
[00:45:44] abused concept here but it's it's not
[00:45:46] too dissimilar to you know cloudatch
[00:45:47] metrics or something like that
[00:45:48] publishing for the behavior of an
[00:45:50] application um the behavior of the model
[00:45:52] is just a different type of application
[00:45:55] and I think to close the loop what I
[00:45:57] would like to have happen here is that
[00:45:59] that model telemetry would be informing
[00:46:02] some process that is maybe either doing
[00:46:04] stream processing or a nightly batch
[00:46:06] that is producing some graphs or
[00:46:07] something like that updating dashboards
[00:46:10] that our operators and on calls can
[00:46:13] actually look at and potentially uh
[00:46:15] triggering alarms if manual intervention
[00:46:17] is required or even just seamlessly
[00:46:20] automatically re-triggering a training
[00:46:22] if we fall below some certain thresholds
[00:46:24] or guard rails. So, I don't really want
[00:46:26] to draw a line through the entire uh
[00:46:29] thing here, but I'm just going to draw a
[00:46:31] line off into space and just said
[00:46:35] uh triggering retraining um if
[00:46:40] performance drifts uh and so I mean
[00:46:45] again I think there are probably certain
[00:46:47] types of models that are lent well more
[00:46:49] to that uh retraining. There are some
[00:46:52] other models and inference types that uh
[00:46:55] it may require manual intervention every
[00:46:57] time uh or it may we may always want to
[00:47:00] get a human in the loop on that. So uh
[00:47:02] in addition to that it might also uh hey
[00:47:07] um hey Brian maybe after this part a
[00:47:10] little bit because we are at time but I
[00:47:12] do have a couple of the questions on my
[00:47:14] list I want to ask you. Okay. Yeah
[00:47:16] totally. Great. Thank you.
[00:47:20] Uh so yeah I I I feel like we can go
[00:47:24] ahead and uh you know put a pin in it
[00:47:26] for now and kind of go uh talk about any
[00:47:28] questions or dive into some scaling
[00:47:30] considerations. Yes. Great. So uh
[00:47:33] actually let me start from the um the
[00:47:36] the uh the weight storage part. I'm
[00:47:38] clicking on the three uh circles here.
[00:47:41] So basically I think this is very
[00:47:42] important components where we store the
[00:47:44] the model weights. My question comes to
[00:47:47] are you using the database or are you
[00:47:49] using the blob storage and how can we
[00:47:51] how should we just store the weight
[00:47:53] here? Yeah. So that's a really great
[00:47:56] question. Uh so I think um what I'm
[00:47:59] thinking about when I think about that
[00:48:01] is to sort of what is the actual access
[00:48:02] pattern uh that the weights are going to
[00:48:05] use and how are we going to be fetching
[00:48:07] them. So uh I'm a little out of my depth
[00:48:11] to be honest about the the usual size of
[00:48:13] the amount of weights. know from at a
[00:48:16] high level that uh you know there are
[00:48:19] some types of models that are very large
[00:48:20] you know for example large language
[00:48:22] models is in the name have billions huge
[00:48:24] amounts of weights those are really big
[00:48:26] uh I think storing all of those weights
[00:48:29] for something of that size in
[00:48:32] uh in sort of like uh you know a
[00:48:35] relational database for example is I
[00:48:37] think uh exceedingly unlikely to be
[00:48:39] performance or scalable at all. Um, and
[00:48:41] so I think fundamentally we're going to
[00:48:43] have to use some kind of big data
[00:48:45] appropriate storage for models past a
[00:48:47] certain size. Um, and what I'm imagining
[00:48:51] I think is that the relative cardality
[00:48:54] of the weights is something that would
[00:48:58] be pretty heterogeneous across the
[00:49:00] different types of models that we do
[00:49:02] like there. uh and in many cases the
[00:49:05] amount of model the amount of weights
[00:49:07] could be you know thousands uh tens of
[00:49:09] thousands or something that is actually
[00:49:10] a lot more tractable and could be much
[00:49:12] more performantly accessed uh in a
[00:49:16] relational database. So I think the way
[00:49:18] that I would actually approach this um
[00:49:21] would be you know the first thing I
[00:49:23] would do would be to kind of survey our
[00:49:25] requirements a little bit about how what
[00:49:27] types of models we're intending to
[00:49:28] deploy with this system and whether or
[00:49:30] not we need a one-sizefits-all
[00:49:32] uh actual backing data store for the
[00:49:34] types of weights. I think I can conceive
[00:49:37] of a world where part of the
[00:49:39] relationship between the training
[00:49:40] organizer and the model registry is some
[00:49:43] accounting of the amount of weights that
[00:49:44] were generated and that would sort of
[00:49:46] inform the decision about where and how
[00:49:48] we're actually publishing that data into
[00:49:50] storage. If you made me actually pick
[00:49:52] one specific, you know, one-sizefits-all
[00:49:55] solution, I would say probably use
[00:49:56] something like
[00:49:58] um a blob storage uh and and actually
[00:50:03] just
[00:50:04] uh writing these as kind of files into
[00:50:07] S3 or something like that. The downside
[00:50:09] there is that I think your processing
[00:50:11] load of actually getting those into a
[00:50:13] cache uh and sort of finding specific
[00:50:15] models, versions of specific weights, if
[00:50:17] you're not careful, uh I think that
[00:50:19] could potentially increase the the
[00:50:21] workload on your system there versus
[00:50:23] like very specifically targeting
[00:50:25] querying for a very specific ID. And now
[00:50:27] you can do that with a blob storage too
[00:50:29] if you like were to partition on the
[00:50:30] model identifier in some way. Um but
[00:50:35] there are some scaling limitations to
[00:50:36] the number of small files that you could
[00:50:38] produce. If some if a lot of your model
[00:50:40] models are small and you're publishing a
[00:50:42] lot of versions and iterations of them,
[00:50:43] you might end up in a circumstance when
[00:50:45] you have many thousands of really small
[00:50:47] weights files which is maybe a less uh
[00:50:50] effective fit for how we would uh want
[00:50:54] to store those. Okay, I think that
[00:50:57] sounds good. And maybe let's switch
[00:50:59] gears. Uh I want to ask you a little bit
[00:51:01] about scalability. So I think right now
[00:51:03] this is very uh comprehensive design
[00:51:05] here. We cover everything most of
[00:51:08] everything here. So what would be the
[00:51:10] bottleneck in terms of scalability and
[00:51:12] how would you want to address the
[00:51:13] bottleneck? Yeah. So let's think. So I I
[00:51:16] can see a few areas right now that are
[00:51:19] potential bottleneck. So the let's start
[00:51:21] with the very superficial ones. I think
[00:51:23] there are a couple areas here that I
[00:51:25] just kind of uh threw one instance uh in
[00:51:29] the way. for example the API gateway or
[00:51:31] the model registry or the data registry
[00:51:33] right now in the design as literally
[00:51:35] written are kind of monolithic
[00:51:37] instances. Um I think for the most part
[00:51:41] the load on the system for the
[00:51:43] registering of data partitions and the
[00:51:45] registering of models and the publishing
[00:51:48] of validation status for models is going
[00:51:50] to be several orders of magnitude lower
[00:51:52] than the actual cardality on that data
[00:51:55] themselves. And so I do think that the
[00:52:00] uh you know the API gateway for the
[00:52:01] training organization uh or you know I
[00:52:04] didn't go into it too deeply but there
[00:52:06] might be an API gateway for the actual
[00:52:07] data registry itself uh and stuff like
[00:52:09] that. I don't think those are actual
[00:52:11] bottlenecks for the system. I think the
[00:52:13] main bottlenecks for the system are
[00:52:15] going to be things like the the weights
[00:52:18] cache and actually loading uh generated
[00:52:20] weights into a form that is actually
[00:52:23] deployable really uh you know how how
[00:52:26] can we make that deployment happen
[00:52:27] really fast? How can we make sure that
[00:52:29] it happens globally to make sure that uh
[00:52:31] we're trying to keep downtime uh or
[00:52:34] sorry not downtime but uh latency low
[00:52:36] for the inferences if we're even if the
[00:52:38] model itself is really really fast if we
[00:52:40] have to go halfway across the world to
[00:52:41] do it the speed of light is going to be
[00:52:43] factor there. So I think uh if I were to
[00:52:46] go back and try to introduce some
[00:52:48] additional elements here, I would assume
[00:52:50] that this um distributed cache uh is
[00:52:53] something that we could sort of like
[00:52:54] regionalize and we actually may have
[00:52:56] different trained versions of the model
[00:52:58] for different regions because different
[00:52:59] regions have different user behavior or
[00:53:02] things like that. So you can imagine
[00:53:04] kind of a regionalized point of presence
[00:53:06] based architecture here where a lot of
[00:53:08] this actually maybe the the generation
[00:53:11] of the model code um or the data
[00:53:13] registries themselves for the offline
[00:53:15] data processing might not necessarily
[00:53:17] have to be globally distributed
[00:53:20] but everything from the actual uh
[00:53:22] postraining phase through so I'm trying
[00:53:26] to just select the whole right half of
[00:53:27] the screen here up to basically model
[00:53:28] registry uh I could imagine you know us
[00:53:31] maybe wanting that to be kind like a
[00:53:32] point of presence based architecture
[00:53:34] where this is a cell of the ML uh
[00:53:38] platform and we might want to deploy
[00:53:40] that in a number of different regions in
[00:53:42] order to uh basically get as close to
[00:53:45] the edge as possible to our users with
[00:53:47] the with the actual caches of the
[00:53:49] weights um and the actual weights cache
[00:53:51] itself. Yeah. So I kind of glossed over
[00:53:53] this a fair bit talking about it being
[00:53:56] distributed and just basically not
[00:53:58] having a limit on the size of the cache
[00:54:00] but the number of uh different models
[00:54:02] that we have and the size of the weights
[00:54:04] there I think are definitely going to be
[00:54:06] major design factors for the actual
[00:54:07] low-level design that we go through and
[00:54:10] uh you know in particular for something
[00:54:13] like large language models like I said
[00:54:15] you know just the first example that
[00:54:16] comes to mind with billions of weights
[00:54:18] um that even just actually loading all
[00:54:21] of those into memory is something that
[00:54:23] would be a relatively you know latent
[00:54:26] process. So we need to think very
[00:54:28] carefully about what our deployment
[00:54:29] mechanism there is because it might be
[00:54:31] slow to revert. Uh so we might want to
[00:54:34] do some kind of blue green deployment
[00:54:35] for example to make sure that we always
[00:54:36] have a fast roll back to a previous
[00:54:38] version of the weights in cases where we
[00:54:42] have you know immediate alarming about
[00:54:44] negative performance impact. Uh so
[00:54:46] that's something that I would think
[00:54:47] about in a lower level design for how we
[00:54:49] could efficiently actually get the
[00:54:50] weights from storage into cache. That
[00:54:52] seems like a relatively important
[00:54:54] bottleneck for us to resolve. Um
[00:54:57] other than that I think uh I mean the
[00:55:01] training compute and the validation
[00:55:03] compute I think should be pretty
[00:55:04] trivially horizontally scalable. It's
[00:55:06] kind of an embarrassingly parallel
[00:55:07] problem in the general sense. So I think
[00:55:10] uh you know horizontally scalable
[00:55:11] compute there should resolve that being
[00:55:13] a bottleneck. we would want to, you
[00:55:15] know, rightsize our allocation there to
[00:55:17] make sure that we're on a reasonable
[00:55:18] budget. So, we would probably establish
[00:55:20] some kind of um scaling factor based on
[00:55:25] memory usage and compute usage on the
[00:55:28] sort of fleet of compute instances to
[00:55:30] indicate whether or not we need to spin
[00:55:31] up new ones elastically or actually spin
[00:55:33] them down in times where there's less
[00:55:35] training happening.
[00:55:37] But again, I don't really conceive of
[00:55:39] that as something that would be like a
[00:55:40] major bottleneck because it's already
[00:55:42] horizontally scaled in the design. Okay.
[00:55:44] Um, yeah. Uh, let's pause a little bit
[00:55:47] here because I think we almost here. I
[00:55:49] just make all the all the notes on my
[00:55:51] side. Let's pause a little bit. I want
[00:55:53] to make sure we have some free
[00:55:54] discussions at the end. Okay. Yeah,
[00:55:56] sure. Absolutely. Great. Brian uh I
[00:55:58] always ask a candidate on this platform
[00:56:00] just for the past maybe 55 minutes you
[00:56:03] gave me a very good presentation but
[00:56:05] from your perspective what is the
[00:56:06] highlight what is the lowa in your
[00:56:08] presentation today let's see uh I think
[00:56:11] highlights I think the the architecture
[00:56:13] that I put together here is pretty
[00:56:15] comprehensive of like the endto-end life
[00:56:17] cycle of many different aspects of
[00:56:19] machine learning model management um I
[00:56:22] think it was so comprehensive that maybe
[00:56:25] uh maybe a low light for me is I didn't
[00:56:27] really get to actually write a lot in
[00:56:29] the design that indicates my depth of
[00:56:33] expertise on some of the actual scaling
[00:56:35] issues bottlenecks here. Um, so I sort
[00:56:38] of feel like from a high level, what
[00:56:41] signal do I feel like came across in
[00:56:42] this interview? I feel like it came
[00:56:44] across that I'm able to think broadly
[00:56:45] about the problem and keep a large
[00:56:48] number of different facets of the
[00:56:49] problem in my head and kind of think
[00:56:51] reason about complicated problems piece
[00:56:54] by piece. But uh I don't think I
[00:56:56] necessarily demonstrated a huge amount
[00:56:58] of deep technical expertise on the
[00:57:00] scaling of the system because I spent a
[00:57:02] lot of time on the actual comprehensive
[00:57:05] making sure that every aspect of this
[00:57:07] was kind of recorded here and I I guess
[00:57:09] it depends a little on what the
[00:57:11] interviewer is looking for but I can
[00:57:12] imagine a world where the interviewer
[00:57:14] might come away from this thinking this
[00:57:16] guy knows a lot about design di design
[00:57:18] documents don't know if he knows a lot
[00:57:20] about actually building scalable
[00:57:22] systems. Um I I did my best to try to
[00:57:25] cover bases there verbally. Um and some
[00:57:27] of this is I think is maybe
[00:57:28] unfamiliarity with the actual platform
[00:57:30] the Excala draw situation thing and I
[00:57:32] need to practice that a little bit. Um
[00:57:34] because I think I was that was my speed
[00:57:37] limit a few times. But yeah, I'll kind
[00:57:39] of come up here. That's sort of my
[00:57:41] initial assessment of myself.
[00:57:44] Sounds great. And uh I second most of
[00:57:48] the sement you have come up with. I
[00:57:49] think this is very good presentation.
[00:57:51] I'm so impressed by especially the right
[00:57:54] side. This is super super comprehensive
[00:57:56] because actually I think you just offer
[00:57:58] way more than I expect from you uh just
[00:58:01] for the senior role because uh this is
[00:58:04] the end to end machine learning platform
[00:58:07] and I think you cover the collections
[00:58:09] training and serving with tons of the
[00:58:11] great details. You also try to connect
[00:58:13] the dust all the dust together which I
[00:58:16] think that is terrific. So uh the TLDDR
[00:58:19] if I were the interview just for the E5
[00:58:21] uh just for the E5 uh system design
[00:58:24] interview I I would give this candidate
[00:58:26] the higher decision. Okay. But actually
[00:58:29] at this point I keep thinking when you
[00:58:31] just um show your thinking process when
[00:58:33] you just call out your solution, right?
[00:58:35] I keep thinking about okay you have such
[00:58:37] a you have tons of the great um
[00:58:39] materials just on your side and you can
[00:58:42] articulate your thinking process in a
[00:58:44] crystal way but what would be the
[00:58:46] missing point for us to just go from uh
[00:58:49] why can't we just have the strong high
[00:58:50] instead of the high basically I think
[00:58:52] high is great nowadays but I keep
[00:58:55] thinking about what might be the
[00:58:56] headrooms we can go from high all the
[00:58:58] way to the strong high so this will be
[00:59:00] my honest feedback just to the
[00:59:02] presentation here I just feel like uh
[00:59:05] you have tons of the great contents and
[00:59:07] you just compress everything uh just
[00:59:11] within the 50 minutes but at the same
[00:59:13] time I keep thinking about in so think
[00:59:15] about this is the presentation right you
[00:59:17] are in front of the real human beings
[00:59:20] and I may want you to sometimes just
[00:59:22] pause a little bit such that you can
[00:59:24] give some spaces back to the audience
[00:59:26] such that they can ask the question
[00:59:28] because actually I think you have tons
[00:59:30] of the great contents you just showing
[00:59:32] your thinking process build everything
[00:59:34] together. But actually, I do have some
[00:59:36] quick questions. I want to chime in, but
[00:59:38] I can't chime in. It's because I don't
[00:59:40] want to break your flow. But that put at
[00:59:44] some point maybe that will just put you
[00:59:46] to another dilemma where okay, you drive
[00:59:48] the conversations, but at some point you
[00:59:50] have no idea whether that will be the
[00:59:51] top what will be the that will be the
[00:59:53] most important topics just on top of the
[00:59:55] interviewer's side.
[00:59:58] Come up for air and and check in a
[01:00:00] little bit more. And Exactly. Exactly.
[01:00:02] Exactly. This is what I'm think because
[01:00:04] I when I just I also serve as the hiring
[01:00:07] committee members when I just read
[01:00:08] through the feedback from different
[01:00:10] interviewers right I just feel like most
[01:00:12] of the time if that be the strong high I
[01:00:14] think we are just past the bar but we
[01:00:16] are talking about if that will be the
[01:00:17] strong high decision I think I can see
[01:00:19] most are just from the feedbacks is that
[01:00:22] the interviewer they would just feel
[01:00:23] like this is very good discussions not
[01:00:26] simply the presentation they are just
[01:00:27] serving as the audience but this is the
[01:00:29] very good discussions between them and
[01:00:32] the inter interviewee. So that's why I
[01:00:34] think what we can do train a little bit
[01:00:37] here is to maybe at some point you pause
[01:00:38] a little bit and roll the ball back to
[01:00:40] the interview to see to collect the
[01:00:42] signals from them to see whether that
[01:00:44] will be the most important thing they
[01:00:45] want because I think a very good
[01:00:47] presentation or discussions is we fit
[01:00:50] the right content the most important
[01:00:51] content to our stakeholders within the
[01:00:54] time budget. This is my definition.
[01:00:55] Okay. And another thing here is that I
[01:00:58] also just make another note on my side.
[01:01:00] uh I think we may still miss something
[01:01:03] here is about the trade-off discussions.
[01:01:07] So I just feel like this is workable
[01:01:09] solution. This is the great uh solution.
[01:01:11] Don't get me wrong. But I keep thinking
[01:01:13] about what if the reality is very
[01:01:16] complex. What if we just decide the
[01:01:19] system but it doesn't work as we have
[01:01:21] expected? What would be the plan B? So
[01:01:24] the reason why we really want our
[01:01:26] candidate to talk about the trade-off
[01:01:27] especially for the staff role trade-off
[01:01:29] discussion is mandatory. Why? Because we
[01:01:32] want to see the breath of the breath of
[01:01:34] the knowledge on our candidate side. We
[01:01:36] want to see hey um do you have the plan
[01:01:38] B? If plan A doesn't work what would be
[01:01:40] the plan B? Do we have multiple options
[01:01:42] towards um one solutions? This is
[01:01:45] something we want to know from you. And
[01:01:47] I can see like I said if that will be
[01:01:48] the strong hire decision most of the
[01:01:50] time uh the interviewer they will
[01:01:52] mention okay the candidate can
[01:01:53] proactively talk about the tradeoff. So
[01:01:56] the question comes to you here is that
[01:01:58] what will be some places you can you
[01:02:00] think you can just talk about the
[01:02:01] trade-off when you're looking back.
[01:02:04] Yeah. So one we kind of discussed but it
[01:02:06] was actually not until you prompted me
[01:02:07] but that was about you know what are the
[01:02:09] different trade-offs for how we might
[01:02:10] choose to actually store the weights.
[01:02:11] That's exactly exactly that's a big one.
[01:02:14] Uh I think uh another trade-off I could
[01:02:18] think of is um you know the need for
[01:02:21] complexity in the architecture of
[01:02:22] something like the data registry versus
[01:02:24] just relying on the individual models
[01:02:26] themselves to kind of track the tables
[01:02:28] and and versions and data locations that
[01:02:30] they care about. I think and actually
[01:02:32] that kind of raises a question for me. I
[01:02:34] do want to get back to trade-offs, but
[01:02:36] how important do you feel like it is to
[01:02:37] kind of start with a simple architecture
[01:02:40] and then evolve towards a finalized one
[01:02:43] as you run into speed bumps versus
[01:02:45] trying to I feel like I spent more time
[01:02:49] kind of uh trying to arrive at like a
[01:02:52] finished complex architecture from the
[01:02:54] start anticipating issues and and kind
[01:02:57] of building in but I but I think I kind
[01:03:00] of lose out on an opportunity to
[01:03:02] demonstrate my awareness of those issues
[01:03:04] by illustrating why one architecture
[01:03:07] wouldn't work and then one ar then
[01:03:09] evolving the architecture would help. Do
[01:03:11] you think that's important in a case
[01:03:12] like this? Great question. But I think
[01:03:14] each interview they have their different
[01:03:16] preferences. I can't speak for uh all
[01:03:19] but most of the time uh I I when I just
[01:03:23] looking back I conduct a lot of the
[01:03:24] interview when I looking back I just
[01:03:26] feel like wait within this time budget
[01:03:28] especially the meta and the Google we
[01:03:30] only have 45 minutes compared with the
[01:03:33] they have one hour 50 minutes more so I
[01:03:36] keep thinking about maybe just in the
[01:03:37] meta or the Google interviews I would
[01:03:40] suggest let's come up with something a a
[01:03:41] brute force approach that'll be the very
[01:03:44] simple uh maybe the workable solutions
[01:03:46] and come back to optimize that and also
[01:03:48] given the time budget I don't think we
[01:03:50] can optimize everything. So that's why I
[01:03:52] would just encourage to to just talk
[01:03:54] about uh just talk with the uh
[01:03:56] interviewer to see what would be
[01:03:57] something they would like to do if you
[01:04:00] just collect the signals feed them with
[01:04:01] the right answers and conclude the
[01:04:04] interview uh within the 45 minutes. I
[01:04:06] think that should be the safe bet. Yeah.
[01:04:09] Cool. That's that's really good
[01:04:10] feedback. Anyway, to get back to your
[01:04:12] point as far as like what are some areas
[01:04:13] that I can kind of I think are
[01:04:14] candidates to talk about tradeoff. I
[01:04:16] think the weight storage and the actual
[01:04:18] storage mechanism there is definitely a
[01:04:20] big one. Even the weights cache I think
[01:04:22] is something that is a little
[01:04:23] underexamined here and and we talked a
[01:04:25] little about that at the end as far as
[01:04:26] one option for how we could improve
[01:04:28] scalability. But I think there's
[01:04:29] definitely more that I could have talked
[01:04:31] about or identified on on there. Um
[01:04:34] maybe a third thing actually is
[01:04:36] trade-offs regarding the actual model
[01:04:39] registry. like I just gave a kind of
[01:04:41] canned example of how we might have
[01:04:43] different statuses for the models that
[01:04:45] inform whether or not we're ready to go
[01:04:47] to prod with them. But um there's
[01:04:50] definitely you know any number of
[01:04:51] different designs that we could have
[01:04:53] gone with for how we actually checkpoint
[01:04:56] from training to validation to
[01:04:58] deployment. So I think that's an area
[01:04:59] that I could have talked through some
[01:05:01] trade-offs on. Those are the ones that
[01:05:03] kind of come to mind rel uh top of mind
[01:05:06] for me. Are there any that you feel like
[01:05:07] I'm missing there? No, you I think you
[01:05:09] just covered more than I expected. I
[01:05:11] think the database of the storage part
[01:05:13] is very natural and I second you I think
[01:05:17] cache is very another very obvious
[01:05:19] thing. If we are talking about Q maybe
[01:05:20] that is another thing we can just talk
[01:05:22] about the tradeoff but typically on my
[01:05:24] side I think uh
[01:05:26] database Q or maybe the cache these
[01:05:29] three things they can we can easily just
[01:05:30] talk about the trade-off. I think that
[01:05:32] should be and you know you actually
[01:05:34] mentioned cues. I didn't even get into
[01:05:35] the idea of potentially asynchronously
[01:05:37] triggering the training processes.
[01:05:39] Exactly. That's definitely another
[01:05:40] candidate area to go into. Yeah, for
[01:05:43] sure.
[01:05:45] Great, great discussions. Okay, so um
[01:05:49] Brian give like I said I think you uh
[01:05:52] you have already passed this round but I
[01:05:54] share some of the very uh neat feedback
[01:05:57] to you. Hopefully you can just get
[01:05:59] absolutely yeah a a strong higher
[01:06:02] decision and with what you mentioned you
[01:06:04] will have the real interview in the next
[01:06:05] week. With that I wish all the best.
[01:06:07] Thank you very much. I appreciate all
[01:06:08] the feedback and uh All right. Thanks.
[01:06:11] Thank you so much. Talk soon. Bye. Bye.
[01:06:17] [Music]

FEEDBACK_MD:
---
section: "Interviewer feedback"
start: "00:57:45"
end: "01:06:33"
start_seconds: 3465
end_seconds: 3993
---

the sement you have come up with. I think this is very good presentation. I'm so impressed by especially the right side. This is super super comprehensive because actually I think you just offer way more than I expect from you uh just for the senior role because uh this is the end to end machine learning platform and I think you cover the collections training and serving with tons of the great details. You also try to connect the dust all the dust together which I think that is terrific. So uh the TLDDR if I were the interview just for the E5 uh just for the E5 uh system design interview I I would give this candidate the higher decision. Okay. But actually at this point I keep thinking when you just um show your thinking process when you just call out your solution, right? I keep thinking about okay you have such a you have tons of the great um materials just on your side and you can articulate your thinking process in a crystal way but what would be the missing point for us to just go from uh why can't we just have the strong high instead of the high basically I think high is great nowadays but I keep thinking about what might be the headrooms we can go from high all the way to the strong high so this will be my honest feedback just to the presentation here I just feel like uh you have tons of the great contents and you just compress everything uh just within the 50 minutes but at the same time I keep thinking about in so think about this is the presentation right you are in front of the real human beings and I may want you to sometimes just pause a little bit such that you can give some spaces back to the audience such that they can ask the question because actually I think you have tons of the great contents you just showing your thinking process build everything together. But actually, I do have some quick questions. I want to chime in, but I can't chime in. It's because I don't want to break your flow. But that put at some point maybe that will just put you to another dilemma where okay, you drive the conversations, but at some point you have no idea whether that will be the top what will be the that will be the most important topics just on top of the interviewer's side. Come up for air and and check in a little bit more. And Exactly. Exactly. Exactly. This is what I'm think because I when I just I also serve as the hiring committee members when I just read through the feedback from different interviewers right I just feel like most of the time if that be the strong high I think we are just past the bar but we are talking about if that will be the strong high decision I think I can see most are just from the feedbacks is that the interviewer they would just feel like this is very good discussions not simply the presentation they are just serving as the audience but this is the very good discussions between them and the inter interviewee. So that's why I think what we can do train a little bit here is to maybe at some point you pause a little bit and roll the ball back to the interview to see to collect the signals from them to see whether that will be the most important thing they want because I think a very good presentation or discussions is we fit the right content the most important content to our stakeholders within the time budget. This is my definition. Okay. And another thing here is that I also just make another note on my side. uh I think we may still miss something here is about the trade-off discussions. So I just feel like this is workable solution. This is the great uh solution. Don't get me wrong. But I keep thinking about what if the reality is very complex. What if we just decide the system but it doesn't work as we have expected? What would be the plan B? So the reason why we really want our candidate to talk about the trade-off especially for the staff role trade-off discussion is mandatory. Why? Because we want to see the breath of the breath of the knowledge on our candidate side. We want to see hey um do you have the plan B? If plan A doesn't work what would be the plan B? Do we have multiple options towards um one solutions? This is something we want to know from you. And I can see like I said if that will be the strong hire decision most of the time uh the interviewer they will mention okay the candidate can proactively talk about the tradeoff. So the question comes to you here is that what will be some places you can you think you can just talk about the trade-off when you're looking back. Yeah. So one we kind of discussed but it was actually not until you prompted me but that was about you know what are the different trade-offs for how we might choose to actually store the weights. That's exactly exactly that's a big one. Uh I think uh another trade-off I could think of is um you know the need for complexity in the architecture of something like the data registry versus just relying on the individual models themselves to kind of track the tables and and versions and data locations that they care about. I think and actually that kind of raises a question for me. I do want to get back to trade-offs, but how important do you feel like it is to kind of start with a simple architecture and then evolve towards a finalized one as you run into speed bumps versus trying to I feel like I spent more time kind of uh trying to arrive at like a finished complex architecture from the start anticipating issues and and kind of building in but I but I think I kind of lose out on an opportunity to demonstrate my awareness of those issues by illustrating why one architecture wouldn't work and then one ar then evolving the architecture would help. Do you think that's important in a case like this? Great question. But I think each interview they have their different preferences. I can't speak for uh all but most of the time uh I I when I just looking back I conduct a lot of the interview when I looking back I just feel like wait within this time budget especially the meta and the Google we only have 45 minutes compared with the they have one hour 50 minutes more so I keep thinking about maybe just in the meta or the Google interviews I would suggest let's come up with something a a brute force approach that'll be the very simple uh maybe the workable solutions and come back to optimize that and also given the time budget I don't think we can optimize everything. So that's why I would just encourage to to just talk about uh just talk with the uh interviewer to see what would be something they would like to do if you just collect the signals feed them with the right answers and conclude the interview uh within the 45 minutes. I think that should be the safe bet. Yeah. Cool. That's that's really good feedback. Anyway, to get back to your point as far as like what are some areas that I can kind of I think are candidates to talk about tradeoff. I think the weight storage and the actual storage mechanism there is definitely a big one. Even the weights cache I think is something that is a little underexamined here and and we talked a little about that at the end as far as one option for how we could improve scalability. But I think there's definitely more that I could have talked about or identified on on there. Um maybe a third thing actually is trade-offs regarding the actual model registry. like I just gave a kind of canned example of how we might have different statuses for the models that inform whether or not we're ready to go to prod with them. But um there's definitely you know any number of different designs that we could have gone with for how we actually checkpoint from training to validation to deployment. So I think that's an area that I could have talked through some trade-offs on. Those are the ones that kind of come to mind rel uh top of mind for me. Are there any that you feel like I'm missing there? No, you I think you just covered more than I expected. I think the database of the storage part is very natural and I second you I think cache is very another very obvious thing. If we are talking about Q maybe that is another thing we can just talk about the tradeoff but typically on my side I think uh database Q or maybe the cache these three things they can we can easily just talk about the trade-off. I think that should be and you know you actually mentioned cues. I didn't even get into the idea of potentially asynchronously triggering the training processes. Exactly. That's definitely another candidate area to go into. Yeah, for sure. Great, great discussions. Okay, so um Brian give like I said I think you uh you have already passed this round but I share some of the very uh neat feedback to you. Hopefully you can just get absolutely yeah a a strong higher decision and with what you mentioned you will have the real interview in the next week. With that I wish all the best. Thank you very much. I appreciate all the feedback and uh All right. Thanks. Thank you so much. Talk soon. Bye. Bye. [Music]

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
Write JSON only to: splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.json \
    --video transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.json --out splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.qa-split.json \
    --video transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.validation-report.md

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
video.md: transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/video.md

--- CHAPTER `00:02:43` — Question begins ---
window: 00:02:43 .. 00:47:33
recognition_status: multiple (5 items)

ITEM #6
  interviewer_question: time=00:02:50 text="Brian, if you were the Vincent developer, would you please try to decide the centralized machine learning management platform? With that, I'll hand over to you."
  candidate_answer: time=00:03:00 text="so I think I'm going to need to ask some clarifying questions to make sure I understand. So I have a couple things that come to mind immediately as far as what the core operations are here but maybe I could uh kind of clarify them with you. Uh so when we say management here is this including serving uh for the purposes of actually the operations of those or is it more for like model iterations training validation and the production of the models or is it kind of an endto-end platform? Yep. Understood. Cool. So let's just go ahead and write those down. So we have data collection, model training, and model serving. Serving. Yes. Cool. Um, so uh yeah, I think we can probably talk about each of these different things kind of as a discrete phase and uh they'll sort of lead into each other one into the next. Um so let's maybe start with data collection. Well, actually, you know, I would like to take pause for a second here and just make sure that uh I understand the constraints. So, uh are there any constraints as far as like the number of models, the uh the size of the data that we intend to be using uh the maybe the uh sort of the the request rate or transactions per second that we can expect on the inferences during the actual model serving? Uh is there anything that we can kind of dial in to make sure that we understand where the key scaling points are? Great. And so Brad, this is a great question, but I think maybe you can just do some ballpark estimations down the line, but this I can call you. I can share with you think of I'm happy to do some ballpark estimates as well if uh if we it'll move us faster here. So I mean on the data collection side, most of these models I imagine will be training over potentially years of historical data, relatively high cardality. So we're talking terabytes at least I think uh maybe even pabytes in certain circumstances. Uh so our data collection and sort of data management systems are definitely going to need to manage big data. Yes, sounds good. So like hundreds I'll call it hundreds of terabytes of uh at least there uh model training. Um again, you know, the actual training process is going to require, you know, relatively horizontally scalable systems that uh that can actually accommodate training using that large amount of data. Um so I'll just put same. And then on the serving side of things, I'm just going to, you know, make some ballpark numbers here. I imagine that there's, you know, at least, you know, thousands to tens of thousands of individual models in use. And uh and the uh actual you know request weight for for those models uh can probably vary a lot between them and I think that's something that will be important when we talk about model serving is the specific types of use cases that we run into here but I think you know on the sharp end of model serving we should be prepared to be executing these models you know many times uh a minute uh you know for userf facing workloads Um, so let's just call it I don't know uh is like a thousand TPS uh completely off base to you for like a sort of peak load for one of the um you know higher scale models or am I off by a lot from what you're looking for or is that reasonable for jumping off? This is reasonable. Yes. Okay, cool. All right, I think we can go ahead and uh get started with that then. So data collection um maybe let's uh let's kind of ask a few more clarifying questions there when it comes to data collection. So uh the when I hear collection here I think one of two things you know there's you know computation of aggregate data uh and sort of collection in forms that are readily encodable as features uh but but data that is you know basically already being written into databases and then I also think data collection in the form of like uh online telemetry and things like that about user behavior engagement numbers and things like that. Um so let's maybe just start there. Um I think for the purposes of this you know just in time I'm going to make some assumptions about the existence of the uh data collection code in our clients of our systems and uh and just assume that they're able to you know make requests. Maybe I can just write like a a brief API uh for just like uh um let's I'm just going to completely simplify for now and just call it uh metrics um and just uh for assuming that this exists in the actual clients for actually publishing telemetry about user behavior. Um. Mhm. Okay. So, uh we're going to uh for starters, um we're going to need to receive uh and actually catalog all of this information. And that is going to be relatively high cardality and relatively um high frequency. So, uh, I I just want to kind of come up here because I'm realizing that I could spend a lot of time here to to like, uh, that could be a whole system design interview in and of itself. Is it fair for me to start with the data existing in a database or would you like me to include sort of upstream of the actual uh uh writing of telemetry data? I see. Hey"
  reference_answer: time=00:03:27 text='Great question. That should be the end to end uh that should be the end to end platform. But more than that, let me just give you some uh give you some context here. So we have so many machine learning engineer just at the matter and to develop the machine learning efforts there are typically three stages. Okay. The first is data collection. The second is model training and the third is model serving. So basically this platform we need to cover three stages.'
  interviewer_feedback: time=00:04:54 text='so Brad, this is a great question, but I think maybe you can just do some ballpark estimations down the line, but off? This is reasonable. Yes. Okay,'
  question_topic: ML

ITEM #7
  interviewer_question: time=00:08:55 text="Brian, I think just for today's uh just for the data collection part, right? I will expect you to just write some data or maybe read some data just from the database."
  candidate_answer: time=00:09:06 text="ahead and assume that that data actually lands in some databases. And so we're probably going to have a bunch of different databases here. Um so I'll just uh give them a couple."
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #8
  interviewer_question: time=00:09:18 text='Brian, I I do have a question here. So are you trying to just start from the high level design or I want to I want to understand what would be your presentation flow here.'
  candidate_answer: time=00:09:28 text="absolutely. Uh that's a great question. So I yeah I think I'd like to just sort of identify key components uh at a high level and then we can sort of dive deeply into the uh actual underlying architecture in in cases. I see. But"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #9
  interviewer_question: time=00:09:42 text="But before that brand I do have a very quick suggestion here because I think uh we would I would like to start from the future part the functional requirements. So basically I think right now we have three stages. They are pretty high level. Let's try to break down a little bit for you."
  candidate_answer: time=00:09:55 text="Yeah sure that absolutely that sounds good. So let's break that down a little further. Um so uh I'll just go ahead and move this over here as an assumption. Um so breaking that down. So on the model training side of things, I'll just start with the models themselves. Uh so what do we actually need to do for the model training? So there's going to need to be a data access layer there. Uh and we're going to need a mechanism for uh the exe. So there's the actual training execution uh in terms of like the uh the compute that we'll run this on. um are going to need uh model publishing. Uh so like when a new a new version of the methodology or some tweaks to the features that we use uh that needs to be publishable somewhere and then we're going to need to actually execute training on those. then we're probably going to need um model validation and guard rails after the actual training effort to make sure that we uh have uh you know a high quality bar for the actual predictive power of the models that we produce. Um and so I'm and then uh once we've actually hit that quality bar, we want to actually move ahead to model serving. I'll go with model deployment um as kind of like the core uh areas that I think about when I think about uh an ML management uh for the sort of the well I guess I'm sort of beginning to blend uh model training and serving. Um so it's not necessarily that this is all part of the the training uh step but rather that we're just sort of breaking it down a little further. Um, so the, uh, I think for the most part, um, and then there's going to be, uh, let me collect my thoughts for one second. Cool. Yeah. Okay. So, the uh, the mechanisms here, I think, what are what are the sort of data stoages uh, and um, that we're going to need? One thing that comes to mind for me is like what is what does it mean for the model actually to be deployed. We're going to need the uh and what the data that's getting used for training execution and also validation presumably some split like a training test split of that data. Um we're going to need a feature data store of the actual features themselves. Uh so and there so there's probably also going to be a step at the beginning uh ahead of all of this in the data collection side of things that is just sort of um you know a registry of the creating a registry of the potentially heterogeneous data tables. So like a a data registry. Um and then we might also have a feature encoding step. Um uh there might be for example you know feature sets that are in reuse by multiple different types of models. And so being able to share those things efficiently uh to prevent retraining or to prevent you know large scale processing over and over again would be really useful. And then when I say model publishing here, publishing is maybe uh you know a misnomer. What I'm really talking about is uh iterations of models by actual ML engineers and data scientists. Um so there's going to need to be an operation um for them to actually upload, you know, the latest code or maybe it would be triggered off of a merge to a a code pipeline. Um okay. And then we would sort of automatically flow into the remaining steps downstream of that. Um, so I'll come up for air there. I think that uh I I have maybe uh I have maybe enough to go off of here where we can start putting um pieces on the board so to speak to actually identify the relationships between the components and make sure uh let's before one more thing before I go ahead and start doing that let's just kind of write down what are the core operations that uh we need to support. So we need to support registering registering new data. Um for example, if there's a new data set that gets in use, uh or as we start collecting new types of data from our users, uh new pages, things like that, um we are going to want to uh publish um new model iterations. um we are going uh and then the process for the way that I'm imagining how this would work at at a high level is that in in the general case the uh training and the validation of that training is stuff that we would definitely want to automate downstream of the actual publishing of that model iteration but I can imagine that there's also going to want to be automated retraining drift detection to trigger retraining and things like that um So uh so we're probably going to want an operation for actually just running training and that will probably take a specific model. Um and then uh we'll also want to deploy um the ability to to redeploy specific models uh if that is something that we need in cases where we might need to do a roll back to reduce the blast radius of failures or things like that. Uh and um then finally uh the last step for the actual serving side of things um I think we're going to need um you know operations for actually executing the inferences uh which may vary the the nature of the inference may may vary on the model but the actual um so I'll just say serving let's call it inference for now. Cool. Um, all right. So, now we have some operations that we can kind of run through as we build this to make sure that we sort of are have covered all of the core uh use cases for how to actually make the platform usable. Um, and then I think we can uh we can go ahead and um and get started. So, let's see. So I think uh how I would choose to build this is that um in the general case I would like to you know not think too hard about something like the data register. The idea there is that basically we're going to want to make data discoverable across the organization. Probably there will be you know a couple different ways that it might be stored based on the type of data. And so we'd like there to be some kind of service that's when uploading a new data set, when creating a new data set, uh or when maybe you know calling a partition finished on data that's sort of streaming and happening in real life and and registering that in a way that it is accessible to training uh mechanisms. Uh we're going to want some kind of uh so I'm going to assume that we have potentially a bunch of different kind of uh you know types of of data here. Mhm. So I'm just going to call this and uh there's going to be some layer on top of that that is just uh a kind of a a registry. So uh and it will be the responsibility of this registry to sort of act as you would expect almost on a search engine for all of the data that you have where um the process of actually ETL processes that load data will maybe also make an API call um to uh to the registry. So, I'll just uh assume that we have, you know, it's a maybe a little out of scope for uh our purposes at this exact moment, but we can go back and talk in more detail about that. So, I'll just assume that there's some ETL um that uh will maybe write this data into, you know, blob storage or into uh sorry, how do I call five is the line? I'm I'm still getting used to this. Uh no worries. Yeah, got to get used to the hotkeys here. So some processes will publish data and it will make that data available to all of our downstreams by you know registering a new partition or indicating uh that uh some data set is now completed. Um and the actual ML platform will sort of be built on these these data building blocks. So when it comes to the actual um feature encodings I I can think off the top of my head of kind of two ways out. Some of them might be very model specific in which case that could almost you know be included in the model code itself for how we might want to do that. There are probably plenty of well-known encodings uh that are reusable and there actually may be uh we we may want to run sort of like a second layer of ETL in effect that uh is responsible for reading these sort of like raw tables, staging them, uh potentially doing some transformations on that data and otherwise generating sort of partial feature encodings uh of the actual uh you know beginning to look like the data that will actually be in use in the in the training itself. So I'm just going to uh you know for now I'll just call that feature I'll just call this generic um and in fact I think I would like this to sort of feedback directly into the data registry itself such that uh there are sort of you know feature sets that are uh registered with the data registry and uh they they we can use those as if they were the um you know the raw data and just sort of make them available to you streaming processing in the same way. Um and then when it comes to the actual model training okay so this is where we kind of get into the meat of the system a little bit more and so let's assume for now that the model training is going to be uh a you know a small platform of its own. So I imagine that for example there are probably going to be uh I'll just write draining over it for now just to uh kind of organize my own thoughts here. Um and let's maybe start with the actual rather than the the edge of the system. Let's start with the building blocks. Right? There's going to need to be uh some compute instances that are ideally you know very horizontally scalable for uh you know I'm I work with AWS a lot. So something like SageMaker compute uh or the underlying EC2 instances for example. So we're going to need the actual um uh compute instances and these are going to be what get uh allocated for the purposes of running. There is a new training request coming in for a specific uh system. There will then we need kind of like a a a layer on top of this uh a supervisory layer that would be responsible for allocating specific partitions from the data registry to be uh used in training for uh kind of sharding out the individual training to individual uh instances. So I think we can go ahead and assume that there will be uh sort of like a training management layer. Uh so I'm just going to call this uh the like the training organizer. Uh sorry, let me uh grow these a little bit. Okay. So, as written right now, this is kind of like a single instance. I think that itself would probably uh be something that we could load balance across a couple different instances. Um, so maybe I'll just uh and then ultimately the actual uh sort of edge of the system would be some kind of API gateway uh that is responsible for receiving requests to train our model. um and then farming those out. Uh we would probably want to separate concerns from the actual API gateway that might do authentication or making data access uh middleware permissions requests, things like that. um to uh decouple that from the actual responsibility of okay, we have a specific model version and we know which and so the training organizer is probably going to be communicating with the data registry and uh that would sort of be birectional in order to sort of maybe get a manifest of the number of different partitions within a specific set of date ranges or something like that. And then the individual uh sort of allocation of those to compute units for the purposes of doing partitions and the training I think is something that would be happening uh sort of directly between the the compute would sort of request for directly data registry. Uh and so the uh I I spoke very briefly I kind of glossed over uh model version as part of the API gateway here. So yeah, so there's going to need to be some uh repository of the actual I'm realizing that I uh did not really uh kind of set up my space. Yeah, no worries effectively here. I'll move some stuff around if that's okay. So um I'm going to assume that we have some store of actual uh models themselves. Okay. And uh there there will be some requests that are triggered to the API gateway. Oh, that's the wrong thing. Uh that will use models. Um and so I identified a couple of these off the top of my head. So we might want to do ad hoc training, which is something where like an actual user uh would trigger. Uh and then we could also have some kind of like uh so an ad hoc request might say um you know train this model uh maybe in development purposes um and so I'll just kind of write uh uh and so the uh if we assume that there's kind of like a a submit training uh and that that might take some configuration about how you know hyperparameters or the uh you know which model to use what how far back to go for specific date ranges on on the data things like that be included there but uh ultimately the actual events there could be a couple different types of events to do this there might be one that's sort of triggered by uh you know continuous integration or continuous deployment uh as Well, whenever a new version of the model actually happens, uh uh um a new new version of model code, I should say, uh is published, uh that could be something that actually happens here where maybe there's actually an event. uh feel like I've seen a way for people to do kind of curves lines that I don't actually know how to do. But the idea being that you know there could be some uh stream of events from the publishing of new models here that's uh that itself can I oh is this what I want? Perfect. Um so maybe you know there's ad hoc maybe uh when stuff isn't was is unpublished or still in development and then sort of as a new model is finalized after it gets reviewed and and ends up getting published to the sort of repository of model methodologies maybe a stream of the publishing of those events will go to some CI/CD process which will then trigger the training and all the downstream that happens after that. Mhm. So, okay, just kind of checking in with myself here. So, uh we have covered the idea of uh data registry. So, I'm going to um just call this uh that I you know assuming that the there's some mechanism baked into our ECL processing platform or pipeline such that as we actually generate new data partitions, we register those with a data registry. Okay, so we have that here. um the actual publishing of the model iterations itself. Uh I'm not going to go too far into that. You know, a code review process probably going to be in place uh and and things like that. But so in terms of actually publishing a new version of a model that I want to get trained um is something that would just sort of be upstream of this models DB itself. So maybe I'll just have a line into that. There's some operation for publish happening. Okay. Uh let's see. Um so I feel like we've gone through most of the pretty high level building blocks here for actually getting to a place of the actual training happening. Um one thing that we haven't done is where's the output of that training actually going? Where is sort of the models themselves landing? Uh we're going to need some kind of um that's not what I wanted to say. We're going to need some kind of um finished uh model registry. Uh and the idea being here that sort of the results the training would be complete. Uh the actual data that is generated um in the form of those models might uh need to be written to sort of model storage itself. Uh so um oops I hope that's relatively clear the different shape encodings that I'm using of circles for for data storage. Uh I'm just going to instead of making this bigger I'll just write next to them. Uh and so the idea being that basically the actual compute will um and um informing the training organizer of Oh, what's okay? How do I stop this? Uh oh boy, is there a cancel button? Okay, there we go. Sorry. Uh so when the training is actually completed, there's going to be some training output that constitutes the actual model, the artifacts uh of the the sort of data that's been computed over and the weights of the model itself. Um and so those weights are going to need to get published. Maybe just to disambiguate that, we'll call this um weight storage here. And so the [Music] uh I would say that uh rather than kind of single threading all of that through the individual organizer, I think the individual training as part of the organization, we could maybe establish some space uh or some prefix maybe a model revision number uh for that training in particular. And the individual training compute units can be responsible for writing their partitions of the weights into the weight storage system. And then at the actual completion of that um so the training will actually register the model to indicate hey this uh this model is um the trained model specifically um and so here I'll Okay. Okay. So now I do feel like we have been relatively end to end on what we need to do for the actual training itself. Um, importantly we have we still have a few key elements that are missing here on the actual validation of these whether or not this it's is itself going to be um you know usable or if we need to go back and do another iteration or something like that. Uh and so how is that actually going to happen? So, um, we're going to need to add some kind of procedural validation that's going to essentially be batch inference over, um, some subset of the training data that was reserved back for the purposes of doing validation. Um, and in order to actually do that, we're going to need to trigger that sort of after the training itself has actually completed. Um, and so I need to think a little carefully about this because one thing that's coming to mind for me is like does it make sense to always be registering the train model and publishing the weights if it turns out that the model itself is not remotely predictive? Um, and I think the answer is yes because we're probably going to want to introspect the nature of that lack of prediction and look at the data, look at the weights that were actually produced and maybe use that to guide some intuition about how we might evolve the model forward. So, uh, I was thinking for a minute, does it make sense to maybe, uh, do the validation upstream of publishing to the model registry? And I think what I'd rather do instead is evolve the idea of the model registry that there's maybe different states that models can be in and we can sort of establish guardrails. Um so when it comes to serving and publishing the models from the registry into the actual edge layer of the system that would be customerf facing um it would only be doing that over models that are either under underactive experimentation or are uh you know known working and have satisfactory criteria across some kind of model evaluation criteria. So I think at this point we need to kind of make sure we get through everything. Um so let's go ahead and try to uh speed back up. Um so model validation is as we said it's going to be functionally similar to the actual training compute. So I think the underlying uh compute instances and compute engine here could be used for both training and validation. uh and because fundamentally I think uh the the workloads there are relatively similar. Um and uh so the training organizer itself could be something as a layer that is responsible for a couple different types of operations. So there could be a train operation and there could be a validate operation and depending on which of those things uh that is so sorry which operation that we're doing we'll either be reading from the raw data registry of feature encodings and of okay so actually so one thing that I missed here um sorry coming up for air I know I'm talking in a couple different directions at the same time so some of this feature encoding ET L like we said is going to be generic and we want to um but the the encodings that we generate as part of the training compute here we may optionally be interested in publishing those back to the data registry um and like a model specific namespace or or otherwise to kind of introduce some idea of checkpointing so we can sort of speed up and make the training itself a little more efficient in the future. Um, so I'm just going to make this birectional for now just because there I think I can I can conceive of circumstances where we would want encodings that are sort of defined in the uh in the model code itself to still be publishable into the data registry in some way in which case we would need to potentially write from the training compute into the uh sort of the the feature stores as well as the actual weight storage. Um. Mhm. Okay. So, uh, coming back to my original train of thought here. So, the training organizer could be responsible for both, um, you know, issuing out the training requests and also issuing out validation. Uh, validation is usually a smaller subset of the data than the training, but it could still be potentially very large if the overall data is really really big and we reserve back like 10% of it in order to do a relatively exhaustive uh, validation over it. Um so uh in in that case I think we would still want to shard it over uh multiple different horizontally scalable compute instances. Um and the in in that circumstance what would the uh what where would those outputs actually go? Um I think we would need uh some sort of reporting layer. Uh so I'm going to oops sorry wrong thing here. So some layer that's responsible for doing validation reporting that will basically take the results uh from actually running the validation operations and actually publish that somewhere. Um that is uh these validation results are things that maybe depending on the uh stage of maturity of the model could be manually reviewed if we're still in an experimentation phase. Uh this is something that could be also happening as part of a CI/CD pipeline for the purposes of establishing you know if we have automated guardrails in place already. uh then I think we would need to um sorry not need but we would be able to sort of move ahead with the actual publishing into uh or sort of setting the status. Uh so I'm going to say that there's maybe um a couple different operations on the model registry here or sort of so we we might want to register that a model is uh is trained and then we might also want to um uh publish validated and publish itself might maybe just be setting some state in the model registry on the the model itself. else that indicates uh uh you know um maybe if we have you know an enum of different states that it could be in uh like maybe we ran the validation criteria and then we had a miss or something and so we might want to preserve those artifacts in the registering and weight storage okay so uh I feel like I've gone into suffic sufficient detail to cover the basics of the actual training of the model, different versioning of them um and the execution of the training, the validation of that. Let's talk uh deployment. So um skipping over for a minute the idea of how we decide when we're going to do the deployment um which I think is important and we can discuss that, but let's just assume for a minute that we don't have to think about that. What does deployment actually entail for us here? So uh there's probably a couple different types of model use cases that I can think of. Some of them are going to be online models that are actually running as like in the client or in response to client behavior um at the edge of our system. And some of them are things that are maybe more expensive uh maybe the types of things that we might want to do offline, you know, batch generation of inferences and then bloating those batch inferences into some kind of cache or something like that. So I can think of uh I think for the purposes of talking about model deployments, I'm going to only focus on the former of those two things. The latter is really not all that different conceptually than the ETL that we're doing to actually produce data of facts versus inferences. Uh so we might want to extend our data registry a little bit in some way to make sure that we can differentiate between numbers that we know that are stemming from facts and numbers that are you know or or not necessarily numbers but data points and tables that are inferences. But batch inference I think is really fundamentally pretty similar to ETL. So I'm going to kind of gloss over that for the moment. Mhm. When it comes to uh the the former of these two options, which is sort of online models, um we're going to need those models to be publishable to some uh some sort of edge servers where the model can actually um live. And so what I mean by that is I think the actual weights themselves for most of these were probably going to need to be in memory in order to ensure a performant experience for customers. Um so when the actual publishing operation I think is going to be some mechanism by which we actually get weights uh in caches and that is something that basically from the actual weights data storage we might uh publish and so I'm writing this out as one cache you can consider this as a distributed cache where there's potentially a bunch just uh bunch of different types of models. Um maybe one per model or uh depending on the actual you know server form infrastructure it might make sense to have there be one logical cache here that has a bunch of different uh entities in it with and the keys would indicate which particular type of model we're using. And then the importantly for whatever application is actually routing user requests to use these weights and to use um there's going to need to be some kind of uh what I would call an analog to service discovery uh of in informing the application servers. So let's go ahead and like I said uh I can't really scroll here very easily. Can I? I'm going to zoom out. Okay. Um so I'm going to assume that there are application servers uh that are responsible for uh you know there's probably an API gateway and a whole architecture upstream of this but fundamentally there are you know service workers or some uh compute layer that's going to be responsible for routing requests for customers and the uh actual requests themselves uh might uh interact with the weights cache to fetch some specific weights or and then actually do an inference. Um uh and so now we have kind of like a pseudo end to end but with a a relatively glossed over middle here of what is the actual um mechanism look like for how we actually do that deployment. So I think uh probably something relatively similar to what we talked about for some of these other aspects where ideally I'd like this to be a continuously deploying system so that we can rapidly evolve our system uh and make sure that we can sort of seamlessly per uh deploy new weights. So I would imagine that sort of the validation results would sort of directly inform uh in the in the event of sort of passing. Um so let's see like uh it's kind of two outcomes here, right? is pass and fail more or less. Uh and so um in the event of uh a pass I feel like we would sort of plug back into our continuous integration um now that there is uh you know approvals have been satisfied and we can proceed to the next step that would be responsible for actually interacting with the the model registry to find where the weights are for a specific model. uh and ultimately those weights would need to be published into the weights cache and so some system would need to be responsible for writing to the cache the results from the the model registry. Um okay so let's see let's just kind of go back through my checklist over here to the left. So, we've got our data registry. We've got this idea of feature encodings, writing back into the data registry. Um, I don't think I actually published a lot in the design here about model iterations and versioning of the models themselves. That's something that I think I would probably put on the data model for how we actually manage the versions of the model in the model registry and that and the training organizer would be aware of that. So we can maybe talk a little bit about um that sort of at the end but I do feel like we have you know at least verbally discussed the ways that we could care about model iteration model versioning. Okay. So one thing I actually mentioned up at the beginning that I haven't des uh included here is online maintenance and monitoring of these models and specifically drift detection. So you know as the models after the models are deployed they you know get stale over time and user behavior uh you know is evolutionary with respect to these. So we might want to be observing the actual inferences and sort of the um the behavior of the inferences and also user behavior uh as the model itself is live. So I think in addition to actually just getting the weights and doing the inferences, we're probably going to want some sort of uh reporting system. Mhm. Uh so live model reporting I'll call it for now. Um and basically the application servers that are sort of uh fetching weights doing these inferences would be recording those inferences. uh maybe they would sort of record some information about the user or so I'm just going to put calls context actually because it's not necessarily the user but um you know we might want to if for example we're seeing that there's a massive spike in you know positive uh positive rate coming out of the inferences for one specific browser or something that might be something that'd be really interesting for us. So we want to know as much as we can about the context for both the user and the environment when we're actually looking at these kind of inferences. Um we can kind of crossorrelate that with some of the telemetry data that actually fed into the data registry itself. And ultimately we would want this live model reporting to potentially um so I'll just call this uh model telemetry. um telemetry is maybe a little bit of an abused concept here but it's it's not too dissimilar to you know cloudatch metrics or something like that publishing for the behavior of an application um the behavior of the model is just a different type of application and I think to close the loop what I would like to have happen here is that that model telemetry would be informing some process that is maybe either doing stream processing or a nightly batch that is producing some graphs or something like that updating dashboards that our operators and on calls can actually look at and potentially uh triggering alarms if manual intervention is required or even just seamlessly automatically re-triggering a training if we fall below some certain thresholds or guard rails. So, I don't really want to draw a line through the entire uh thing here, but I'm just going to draw a line off into space and just said uh triggering retraining um if performance drifts uh and so I mean again I think there are probably certain types of models that are lent well more to that uh retraining. There are some other models and inference types that uh it may require manual intervention every time uh or it may we may always want to get a human in the loop on that. So uh in addition to that it might also uh hey"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #10
  interviewer_question: time=00:47:07 text='hey Brian maybe after this part a little bit because we are at time but I do have a couple of the questions on my list I want to ask you.'
  candidate_answer: time=00:47:16 text='totally. Great. Thank you. Uh so yeah I I I feel like we can go ahead and uh you know put a pin in it for now and kind of go uh talk about any questions or dive into some scaling considerations. Yes. Great. So uh'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `00:47:33` — Interviewer's questions on weight storage ---
window: 00:47:33 .. 00:50:57
recognition_status: single (1 items)

ITEM #11
  interviewer_question: time=00:47:47 text='are you using the database or are you using the blob storage and how can we how should we just store the weight here?'
  candidate_answer: time=00:47:56 text="question. Uh so I think um what I'm thinking about when I think about that is to sort of what is the actual access pattern uh that the weights are going to use and how are we going to be fetching them. So uh I'm a little out of my depth to be honest about the the usual size of the amount of weights. know from at a high level that uh you know there are some types of models that are very large you know for example large language models is in the name have billions huge amounts of weights those are really big uh I think storing all of those weights for something of that size in uh in sort of like uh you know a relational database for example is I think uh exceedingly unlikely to be performance or scalable at all. Um, and so I think fundamentally we're going to have to use some kind of big data appropriate storage for models past a certain size. Um, and what I'm imagining I think is that the relative cardality of the weights is something that would be pretty heterogeneous across the different types of models that we do like there. uh and in many cases the amount of model the amount of weights could be you know thousands uh tens of thousands or something that is actually a lot more tractable and could be much more performantly accessed uh in a relational database. So I think the way that I would actually approach this um would be you know the first thing I would do would be to kind of survey our requirements a little bit about how what types of models we're intending to deploy with this system and whether or not we need a one-sizefits-all uh actual backing data store for the types of weights. I think I can conceive of a world where part of the relationship between the training organizer and the model registry is some accounting of the amount of weights that were generated and that would sort of inform the decision about where and how we're actually publishing that data into storage. If you made me actually pick one specific, you know, one-sizefits-all solution, I would say probably use something like um a blob storage uh and and actually just uh writing these as kind of files into S3 or something like that. The downside there is that I think your processing load of actually getting those into a cache uh and sort of finding specific models, versions of specific weights, if you're not careful, uh I think that could potentially increase the the workload on your system there versus like very specifically targeting querying for a very specific ID. And now you can do that with a blob storage too if you like were to partition on the model identifier in some way. Um but there are some scaling limitations to the number of small files that you could produce. If some if a lot of your model models are small and you're publishing a lot of versions and iterations of them, you might end up in a circumstance when you have many thousands of really small weights files which is maybe a less uh effective fit for how we would uh want to store those. Okay, I think that"
  reference_answer: time=None text=None
  interviewer_feedback: time=00:50:57 text='Okay, I think that sounds good.'
  question_topic: ML

--- CHAPTER `00:50:57` — Interviewer's questions on scalability ---
window: 00:50:57 .. 00:55:58
recognition_status: single (1 items)

ITEM #12
  interviewer_question: time=00:50:59 text='what would be the bottleneck in terms of scalability and how would you want to address the bottleneck?'
  candidate_answer: time=00:51:16 text="can see a few areas right now that are potential bottleneck. So the let's start with the very superficial ones. I think there are a couple areas here that I just kind of uh threw one instance uh in the way. for example the API gateway or the model registry or the data registry right now in the design as literally written are kind of monolithic instances. Um I think for the most part the load on the system for the registering of data partitions and the registering of models and the publishing of validation status for models is going to be several orders of magnitude lower than the actual cardality on that data themselves. And so I do think that the uh you know the API gateway for the training organization uh or you know I didn't go into it too deeply but there might be an API gateway for the actual data registry itself uh and stuff like that. I don't think those are actual bottlenecks for the system. I think the main bottlenecks for the system are going to be things like the the weights cache and actually loading uh generated weights into a form that is actually deployable really uh you know how how can we make that deployment happen really fast? How can we make sure that it happens globally to make sure that uh we're trying to keep downtime uh or sorry not downtime but uh latency low for the inferences if we're even if the model itself is really really fast if we have to go halfway across the world to do it the speed of light is going to be factor there. So I think uh if I were to go back and try to introduce some additional elements here, I would assume that this um distributed cache uh is something that we could sort of like regionalize and we actually may have different trained versions of the model for different regions because different regions have different user behavior or things like that. So you can imagine kind of a regionalized point of presence based architecture here where a lot of this actually maybe the the generation of the model code um or the data registries themselves for the offline data processing might not necessarily have to be globally distributed but everything from the actual uh postraining phase through so I'm trying to just select the whole right half of the screen here up to basically model registry uh I could imagine you know us maybe wanting that to be kind like a point of presence based architecture where this is a cell of the ML uh platform and we might want to deploy that in a number of different regions in order to uh basically get as close to the edge as possible to our users with the with the actual caches of the weights um and the actual weights cache itself. Yeah. So I kind of glossed over this a fair bit talking about it being distributed and just basically not having a limit on the size of the cache but the number of uh different models that we have and the size of the weights there I think are definitely going to be major design factors for the actual low-level design that we go through and uh you know in particular for something like large language models like I said you know just the first example that comes to mind with billions of weights um that even just actually loading all of those into memory is something that would be a relatively you know latent process. So we need to think very carefully about what our deployment mechanism there is because it might be slow to revert. Uh so we might want to do some kind of blue green deployment for example to make sure that we always have a fast roll back to a previous version of the weights in cases where we have you know immediate alarming about negative performance impact. Uh so that's something that I would think about in a lower level design for how we could efficiently actually get the weights from storage into cache. That seems like a relatively important bottleneck for us to resolve. Um other than that I think uh I mean the training compute and the validation compute I think should be pretty trivially horizontally scalable. It's kind of an embarrassingly parallel problem in the general sense. So I think uh you know horizontally scalable compute there should resolve that being a bottleneck. we would want to, you know, rightsize our allocation there to make sure that we're on a reasonable budget. So, we would probably establish some kind of um scaling factor based on memory usage and compute usage on the sort of fleet of compute instances to indicate whether or not we need to spin up new ones elastically or actually spin them down in times where there's less training happening. But again, I don't really conceive of that as something that would be like a major bottleneck because it's already horizontally scaled in the design. Okay."
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `00:55:58` — How did the candidate feel he did ---
window: 00:55:58 .. конец
recognition_status: multiple (2 items)

ITEM #13
  interviewer_question: time=00:55:58 text='from your perspective what is the highlight what is the lowa in your presentation today'
  candidate_answer: time=00:56:11 text="highlights I think the the architecture that I put together here is pretty comprehensive of like the endto-end life cycle of many different aspects of machine learning model management um I think it was so comprehensive that maybe uh maybe a low light for me is I didn't really get to actually write a lot in the design that indicates my depth of expertise on some of the actual scaling issues bottlenecks here. Um, so I sort of feel like from a high level, what signal do I feel like came across in this interview? I feel like it came across that I'm able to think broadly about the problem and keep a large number of different facets of the problem in my head and kind of think reason about complicated problems piece by piece. But uh I don't think I necessarily demonstrated a huge amount of deep technical expertise on the scaling of the system because I spent a lot of time on the actual comprehensive making sure that every aspect of this was kind of recorded here and I I guess it depends a little on what the interviewer is looking for but I can imagine a world where the interviewer might come away from this thinking this guy knows a lot about design di design documents don't know if he knows a lot about actually building scalable systems. Um I I did my best to try to cover bases there verbally. Um and some of this is I think is maybe unfamiliarity with the actual platform the Excala draw situation thing and I need to practice that a little bit. Um because I think I was that was my speed limit a few times. But yeah, I'll kind of come up here. That's sort of my initial assessment of myself."
  reference_answer: time=None text=None
  interviewer_feedback: time=00:57:44 text="Sounds great. And uh I second most of the sement you have come up with. I think this is very good presentation. I'm so impressed by especially the right side. This is super super comprehensive because actually I think you just offer way more than I expect from you uh just for the senior role because uh this is the end to end machine learning platform and I think you cover the collections training and serving with tons of the great details. You also try to connect the dust all the dust together which I think that is terrific. So uh the TLDDR if I were the interview just for the E5 uh just for the E5 uh system design interview I I would give this candidate the higher decision. Okay. But actually at this point I keep thinking when you just um show your thinking process when you just call out your solution, right? I keep thinking about okay you have such a you have tons of the great um materials just on your side and you can articulate your thinking process in a crystal way but what would be the missing point for us to just go from uh why can't we just have the strong high instead of the high basically I think high is great nowadays but I keep thinking about what might be the headrooms we can go from high all the way to the strong high so this will be my honest feedback just to the presentation here I just feel like uh you have tons of the great contents and you just compress everything uh just within the 50 minutes but at the same time I keep thinking about in so think about this is the presentation right you are in front of the real human beings and I may want you to sometimes just pause a little bit such that you can give some spaces back to the audience such that they can ask the question because actually I think you have tons of the great contents you just showing your thinking process build everything together. But actually, I do have some quick questions. I want to chime in, but I can't chime in. It's because I don't want to break your flow. But that put at some point maybe that will just put you to another dilemma where okay, you drive the conversations, but at some point you have no idea whether that will be the top what will be the that will be the most important topics just on top of the interviewer's side. Come up for air and and check in a little bit more. And Exactly. Exactly. Exactly. This is what I'm think because I when I just I also serve as the hiring committee members when I just read through the feedback from different interviewers right I just feel like most of the time if that be the strong high I think we are just past the bar but we are talking about if that will be the strong high decision I think I can see most are just from the feedbacks is that the interviewer they would just feel like this is very good discussions not simply the presentation they are just serving as the audience but this is the very good discussions between them and the inter interviewee. So that's why I think what we can do train a little bit here is to maybe at some point you pause a little bit and roll the ball back to the interview to see to collect the signals from them to see whether that will be the most important thing they want because I think a very good presentation or discussions is we fit the right content the most important content to our stakeholders within the time budget. This is my definition. Okay. And another thing here is that I also just make another note on my side. uh I think we may still miss something here is about the trade-off discussions. So I just feel like this is workable solution. This is the great uh solution. Don't get me wrong. But I keep thinking about what if the reality is very complex. What if we just decide the system but it doesn't work as we have expected? What would be the plan B? So the reason why we really want our candidate to talk about the trade-off especially for the staff role trade-off discussion is mandatory. Why? Because we want to see the breath of the breath of the knowledge on our candidate side. We want to see hey um do you have the plan B? If plan A doesn't work what would be the plan B? Do we have multiple options towards um one solutions? This is something we want to know from you. And I can see like I said if that will be the strong hire decision most of the time uh the interviewer they will mention okay the candidate can proactively talk about the tradeoff. So the question comes to you here is that"
  question_topic: Communication

ITEM #14
  interviewer_question: time=01:01:58 text="what will be some places you can you think you can just talk about the trade-off when you're looking back."
  candidate_answer: time=01:02:04 text="Yeah. So one we kind of discussed but it was actually not until you prompted me but that was about you know what are the different trade-offs for how we might choose to actually store the weights. That's exactly exactly that's a big one. Uh I think uh another trade-off I could think of is um you know the need for complexity in the architecture of something like the data registry versus just relying on the individual models themselves to kind of track the tables and and versions and data locations that they care about. I think and actually that kind of raises a question for me. I do want to get back to trade-offs, but how important do you feel like it is to kind of start with a simple architecture and then evolve towards a finalized one as you run into speed bumps versus trying to I feel like I spent more time kind of uh trying to arrive at like a finished complex architecture from the start anticipating issues and and kind of building in but I but I think I kind of lose out on an opportunity to demonstrate my awareness of those issues by illustrating why one architecture wouldn't work and then one ar then evolving the architecture would help. Do you think that's important in a case like this? Great question. But I think each interview they have their different preferences. I can't speak for uh all but most of the time uh I I when I just looking back I conduct a lot of the interview when I looking back I just feel like wait within this time budget especially the meta and the Google we only have 45 minutes compared with the they have one hour 50 minutes more so I keep thinking about maybe just in the meta or the Google interviews I would suggest let's come up with something a a brute force approach that'll be the very simple uh maybe the workable solutions and come back to optimize that and also given the time budget I don't think we can optimize everything. So that's why I would just encourage to to just talk about uh just talk with the uh interviewer to see what would be something they would like to do if you just collect the signals feed them with the right answers and conclude the interview uh within the 45 minutes. I think that should be the safe bet. Yeah. Cool. That's that's really good feedback. Anyway, to get back to your point as far as like what are some areas that I can kind of I think are candidates to talk about tradeoff. I think the weight storage and the actual storage mechanism there is definitely a big one. Even the weights cache I think is something that is a little underexamined here and and we talked a little about that at the end as far as one option for how we could improve scalability. But I think there's definitely more that I could have talked about or identified on on there. Um maybe a third thing actually is trade-offs regarding the actual model registry. like I just gave a kind of canned example of how we might have different statuses for the models that inform whether or not we're ready to go to prod with them. But um there's definitely you know any number of different designs that we could have gone with for how we actually checkpoint from training to validation to deployment. So I think that's an area that I could have talked through some trade-offs on. Those are the ones that kind of come to mind rel uh top of mind for me. Are there any that you feel like I'm missing there? No, you I think you just covered more than I expected. I think the database of the storage part is very natural and I second you I think cache is very another very obvious thing. If we are talking about Q maybe that is another thing we can just talk about the tradeoff but typically on my side I think uh database Q or maybe the cache these three things they can we can easily just talk about the trade-off. I think that should be and you know you actually mentioned cues. I didn't even get into the idea of potentially asynchronously triggering the training processes. Exactly. That's definitely another candidate area to go into. Yeah, for sure."
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03/ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
