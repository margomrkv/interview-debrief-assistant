<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19",
  "transcript_folder": "transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19",
  "source_id": "ml_engineer_senior_meta_harmful_content_interviewing_io_2023_08_19",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:18:06 +0200",
  "updated_at": "2026-05-20 21:31:17 +0200",
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
    "json": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/timecodes.txt",
        "en",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.pipeline-log.md"
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
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:31:17 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:31:17 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19`
- **Source ID:** `ml_engineer_senior_meta_harmful_content_interviewing_io_2023_08_19`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:18:06 +0200
- **Last updated:** 2026-05-20 21:31:17 +0200

Фильтр в IDE: `*ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/timecodes.txt`<br>`en`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.pipeline-log.md` | — | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.validation-report.md` | 1.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.pipeline-log.md`

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
SOURCE_ID: ml_engineer_senior_meta_harmful_content_interviewing_io_2023_08_19
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19
INTERVIEW_LANGUAGE: en
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00:00] foreign
[00:00:05] [Music]
[00:00:09] yes can you hear me loud and clear Okay
[00:00:13] cool so just to get started maybe uh
[00:00:16] give me a quick run through of what
[00:00:17] you're prepping for as well as what
[00:00:19] you're looking to get out of this that
[00:00:20] way I can make sure like we target that
[00:00:22] exactly and get the most money for you
[00:00:24] out of this yep
[00:00:27] um so I'm interviewing for some like
[00:00:30] senior machine learning ml Ops positions
[00:00:33] and
[00:00:34] um I will be editing uh some of the
[00:00:37] machine Learning System design questions
[00:00:39] along the way
[00:00:41] um and so that's kind of the the angle I
[00:00:45] think now I'm not sure the the company
[00:00:47] I'm actually interviewing for does like
[00:00:48] a lot of payments stuff
[00:00:51] um I'm not sure if they'll give me one
[00:00:53] that's like focused on that or it'll
[00:00:55] just give me like a random machine
[00:00:57] learning Ops uh question so I'm not sure
[00:01:01] I see okay so lots of infrastructure
[00:01:03] monitoring and uh you know something
[00:01:05] along the lines and given that it's a
[00:01:07] payment probably along the lines of uh
[00:01:10] anomaly detection in this case right
[00:01:13] could be I don't know
[00:01:15] all right I'm just say yeah like it's a
[00:01:18] it's like a Best Bet kind of situation
[00:01:20] because what I usually uh try to do is
[00:01:23] given the company or the target company
[00:01:25] a try and think of problems that have a
[00:01:28] high probability of showing up who knows
[00:01:30] you know if you practice with that and
[00:01:32] it shows up that's a good thing right
[00:01:33] yeah so the company absorbed uh they do
[00:01:37] Lending
[00:01:39] um I don't know if it's as much anomaly
[00:01:41] I mean it could be anomaly detection
[00:01:44] um uh but
[00:01:47] um
[00:01:48] yeah I'm not sure
[00:01:50] I hear you okay make sense I mean at the
[00:01:53] end of the day fortunately you know the
[00:01:55] infrastructure roughly stays the same
[00:01:57] because it's usually if you have a model
[00:01:59] handy then it's more or less about
[00:02:00] scaling up and making it available so
[00:02:02] the process stays roughly the same
[00:02:04] regardless of the application or the you
[00:02:06] know contextually it can be different
[00:02:08] especially when thinking about
[00:02:10] requirements and you know and I noticed
[00:02:13] that this is a mentorship session so
[00:02:15] have you done any such interview before
[00:02:17] and if so what's your comfort level with
[00:02:20] the machine learning interviews overall
[00:02:23] so I've done plenty of like normal sweet
[00:02:26] interviews uh I am not as experienced in
[00:02:29] system design stuff
[00:02:31] um in general
[00:02:34] um and so so technically the way this
[00:02:37] like it's kind of weird the package the
[00:02:39] way it worked was basically like I
[00:02:41] wanted uh uh
[00:02:43] a staff engineer who did machine
[00:02:45] learning and we couldn't find a map so
[00:02:47] they said uh people throw in a free
[00:02:50] machine learning uh infra like infra
[00:02:53] interview for you so I was like okay
[00:02:54] cool
[00:02:56] um so kind of how this is like marked as
[00:02:57] a mentorship session
[00:02:59] um I see
[00:03:01] yeah
[00:03:02] okay that makes sense cool and final
[00:03:06] question at least before we jump in here
[00:03:08] and have have you done any prep along
[00:03:10] the lines
[00:03:13] a little bit of prep with Alex Alex
[00:03:17] Zoo's book
[00:03:19] um
[00:03:20] yeah I've read like the first four
[00:03:24] chapters
[00:03:26] um or so
[00:03:28] perfect yeah if you've done that at the
[00:03:30] very least then you know you're in a
[00:03:31] good place and uh tldr just to like you
[00:03:34] know set expectations the process is
[00:03:37] roughly the same as traditional system
[00:03:39] design the only difference will be maybe
[00:03:42] less of the estimates a bit of extra
[00:03:45] time on the apis and at the end of the
[00:03:48] day in terms of monitoring it's not the
[00:03:50] traditional stocks like P90 and whatever
[00:03:52] it is it will focus on ML specifics
[00:03:56] ml specific metrics depending on the
[00:03:58] model if you so it's a it's fairly
[00:04:00] straightforward process so okay what
[00:04:03] yeah I have a proposal at least for this
[00:04:05] uh interview in order to help make sure
[00:04:07] that you get that practice so I can give
[00:04:10] it I'll give a question to you a prompt
[00:04:11] to you although it's a normal question
[00:04:13] and you'll go through it and now unlike
[00:04:15] traditional moves where I'll Reserve
[00:04:17] feedback for the end if there are any
[00:04:20] glaring weaknesses I can kinda you know
[00:04:23] stop in the moment suggest a way we can
[00:04:25] improve and then try again and then if
[00:04:28] there's anything that's good enough I
[00:04:30] can resolve feedback towards the end
[00:04:32] like you know so minor things Reserve
[00:04:34] feedback for the end major things kind
[00:04:37] of stop we iterate and then think of
[00:04:39] better ways to do that way we target the
[00:04:41] big weaknesses weaknesses if any and
[00:04:44] then for the minor ones just give
[00:04:46] resources or like a stock you can
[00:04:47] practice or anything what do you think
[00:04:50] yeah yeah that sounds good to me
[00:04:52] perfect okay and so you know building on
[00:04:55] the same problem so what you're gonna
[00:04:57] try and do here is essentially something
[00:04:59] more traditional we're gonna again
[00:05:00] Target then
[00:05:02] okay what is happening with this thing
[00:05:03] are you able to see what's going on on
[00:05:05] the screen
[00:05:06] uh yeah
[00:05:09] yeah okay I'll reload so that the bug
[00:05:11] goes off I don't know what's going on
[00:05:13] with
[00:05:14] oh
[00:05:19] oh okay you're able to see my screen
[00:05:22] right oh well you see me type
[00:05:26] sorry yeah it was some weird infinite
[00:05:29] Loop thing okay
[00:05:34] it's okay okay
[00:05:37] we're gonna focus on a normally
[00:05:39] detection problem and in this regard
[00:05:41] we're going to focus on
[00:05:43] actually let me even pick it up a bit so
[00:05:46] let me generalize even instead of
[00:05:47] anomaly detection let's think of harmful
[00:05:50] content
[00:05:52] uh removal so it's somewhat anomaly
[00:05:55] detection but I think it gives us a
[00:05:57] better more General light framework and
[00:05:59] you know we're not going to Target the
[00:06:00] payments company yet so think in terms
[00:06:03] of Reddit and in the beauty of it is it
[00:06:05] gives us multiple media types so it'll
[00:06:08] give you an initialization here imagine
[00:06:10] we have relics so we have the subred
[00:06:12] Reddit we have the reactions and a
[00:06:14] couple of things to get you started we
[00:06:16] have the ability to report
[00:06:18] posts we have the ability to
[00:06:21] let's say react
[00:06:24] posts
[00:06:25] and so we also support the following
[00:06:28] types of posts so images
[00:06:31] uh you know short
[00:06:33] videos but mostly text
[00:06:38] okay
[00:06:40] so this is like you know our water down
[00:06:42] version of Reddit so given that what I
[00:06:45] would like you to do is think of how you
[00:06:47] will build out a system to essentially
[00:06:50] handle harmful content removal and by
[00:06:53] harmful content and feel free to add to
[00:06:55] this this is what you mean
[00:06:58] content related to abuse
[00:07:01] content related to nudity
[00:07:04] content related to what else uh violence
[00:07:10] oops misinformation
[00:07:13] this one is especially tricky since it's
[00:07:15] hard to know but you know yeah we can
[00:07:18] think of it as an extended goal we can
[00:07:20] discuss it once we have the rest done so
[00:07:22] that's kind of the synopsis of this feel
[00:07:25] free to take over just run me through
[00:07:26] how it's here to build this system
[00:07:28] assuming this watered down version of
[00:07:31] Reddit exists how you go by that
[00:07:33] um so I have a couple like questions in
[00:07:36] terms of uh
[00:07:38] uh the overall I guess like requirements
[00:07:41] Gathering
[00:07:43] um uh so I guess the first question is
[00:07:45] is like
[00:07:47] um
[00:07:49] how soon do we need to moderate content
[00:07:53] right like so somebody posts a picture
[00:07:56] um I guess like well I guess I guess
[00:07:59] even before this like is this a like
[00:08:01] reactionary system or is this a
[00:08:04] proactive system
[00:08:06] um that's some question so I would say
[00:08:09] maybe let's try get a hybrid where for
[00:08:12] some contents or specially categories of
[00:08:14] contents that are extremely harmful we
[00:08:16] basically react
[00:08:19] and for some other contents we can maybe
[00:08:21] take a day
[00:08:23] right so we we are open to different or
[00:08:26] variation in timing in this case
[00:08:27] depending on the type of home
[00:08:30] well certainly like with nudity violence
[00:08:33] I think another one is called like or
[00:08:35] something like that
[00:08:37] um uh those are all things that we'd
[00:08:40] want to like take down immediately or
[00:08:41] sorry this would be proactive
[00:08:44] and then other pieces of content like
[00:08:48] uh I mean abuse is is going here as well
[00:08:53] um but like we would say for the
[00:08:55] reactive case perhaps like
[00:08:58] misinformation there's just a different
[00:09:01] thing here okay
[00:09:03] um and this is just posts and reactions
[00:09:07] to posts there's no comments or anything
[00:09:09] like that
[00:09:12] um and then uh I'm assuming there's like
[00:09:15] other
[00:09:16] pipelines that like when you you post
[00:09:19] something it's not like in terms of
[00:09:21] Reddit like the uh I guess like SLO for
[00:09:27] like uh post to feed time
[00:09:32] um is probably not on the order of like
[00:09:34] milliseconds it's probably on the order
[00:09:36] of seconds
[00:09:40] assumption here like are there other
[00:09:42] like background like data processing
[00:09:45] jobs that are actually going on in the
[00:09:46] system or will at least be the first of
[00:09:49] these
[00:09:51] excellent question so you can assume you
[00:09:53] have some background jobs let's say
[00:09:55] they'll also give you the freedom to
[00:09:57] Define what job you think will be
[00:09:59] convenient and if you think uh exposing
[00:10:03] the data that they're processing either
[00:10:04] in state or after
[00:10:08] okay
[00:10:11] okay
[00:10:13] um first async system okay cool
[00:10:17] ah let's see
[00:10:19] um let's get a sense of like like what
[00:10:21] are the number of like the volume of uh
[00:10:25] posts and reactions per day
[00:10:30] um so this is like Reddit right reddit's
[00:10:33] supposed to have like 50 million uh
[00:10:37] daily active users I don't know if
[00:10:40] they're uh
[00:10:42] posting 50 million videos a day
[00:10:46] um it's probably well like then we can
[00:10:49] just do sort of like a range estimate of
[00:10:51] like in the one to hundreds of Millions
[00:10:57] of uh posts and then just a
[00:10:59] clarification a post does that include
[00:11:02] comments
[00:11:05] so we don't care about comments
[00:11:08] um it probably revise this to be down a
[00:11:10] little bit maybe like to 50 million
[00:11:13] posts per day
[00:11:15] um including the all of the content
[00:11:18] that's in it
[00:11:20] um
[00:11:22] uh uh let's see do we have a question on
[00:11:27] that so when you say 50 million posts do
[00:11:29] you have a distribution in mind because
[00:11:31] uh you know given what you have on line
[00:11:33] six it will be good to think about how
[00:11:36] this is distributed right
[00:11:38] oh I see
[00:11:40] um yeah so given like
[00:11:43] so if there's 50 million posts
[00:11:46] then like if we're saying most of the
[00:11:49] texts are posts or sorry most of the
[00:11:52] posts are text only
[00:11:55] um if we add like like most meaning
[00:11:59] maybe 80 percent
[00:12:02] um if we say 80 or whoa okay 80 are
[00:12:06] texts only
[00:12:08] um this will leave us uh
[00:12:12] uh what would that actually be
[00:12:15] um
[00:12:16] I am not good at math right now 40
[00:12:19] million to
[00:12:21] uh
[00:12:23] uh um
[00:12:24] million text posts
[00:12:28] per day with like a mix of image and
[00:12:32] video so like up to 10 million
[00:12:36] uh images and videos per day
[00:12:42] um
[00:12:42] yeah do you in terms of videos in this
[00:12:45] regard are there any assumptions you're
[00:12:48] making with respect to what the size of
[00:12:52] the video is gonna be as well as what
[00:12:54] the input format is going to be so are
[00:12:56] you thinking somebody will upload an
[00:12:58] actual video or will they link a YouTube
[00:13:00] video a video video that's gonna be
[00:13:03] let's say rendered with an iframe in
[00:13:05] Reddit
[00:13:07] uh yeah so
[00:13:09] um
[00:13:10] good question my assumption is
[00:13:13] um uh
[00:13:18] that's true so so text can have links
[00:13:22] um
[00:13:23] uh
[00:13:26] so that'll be something to consider
[00:13:28] we'll need like a link detection
[00:13:30] uh deal here service
[00:13:35] um if the if there's a video I'm
[00:13:36] assuming the videos are direct uploads
[00:13:38] so we'll be able to like analyze them
[00:13:41] within our system
[00:13:43] um these are like directly attached
[00:13:49] um yeah because otherwise it's really
[00:13:51] hard to moderate if somebody's adding
[00:13:53] like a YouTube embed I mean one we
[00:13:55] assume that YouTube is doing their own
[00:13:57] moderation they're doing a good job and
[00:13:58] two like if there's a sketchy link then
[00:14:01] what we may want to do is actually like
[00:14:04] um uh cue this stuff up so I guess the
[00:14:07] next
[00:14:09] um question is like do we have some data
[00:14:12] sets around of existing content that is
[00:14:15] like labeled
[00:14:18] um
[00:14:18] or is there like
[00:14:21] um or like do we need a
[00:14:25] um labeling slash like uh manual
[00:14:30] review system
[00:14:33] excellent question so online 31 I'll
[00:14:35] make reference to line four so feel free
[00:14:37] to make assumptions about having a human
[00:14:39] in the loop so we will actually have a
[00:14:41] continuous stream of uh some of the
[00:14:44] posts that will be labeled depending on
[00:14:46] the category so we do have humans in the
[00:14:48] loop and we actually do have a mechanism
[00:14:50] available for reports okay cool yeah so
[00:14:54] so that mechanism uh from what I'm
[00:14:56] familiar with uh is basically like the
[00:14:59] way the mechanism is structured is
[00:15:02] uh they monitor the number of uh reports
[00:15:10] um if reports
[00:15:13] exceed some threshold
[00:15:17] a cue
[00:15:20] or
[00:15:23] manual review
[00:15:26] and then we get the labels there
[00:15:28] um so in terms of data set size and
[00:15:33] distribution can we assume that the
[00:15:36] training data that we have is
[00:15:40] um
[00:15:41] mirrors the uh like mirrors the
[00:15:45] population data set distribution
[00:15:48] um like like an assumption is maybe like
[00:15:50] images are more frequently moderated
[00:15:52] than text only and so like it could be
[00:15:56] the case that the data set has like 50
[00:15:58] 50 images 50 text whereas we're getting
[00:16:03] 80 tax from our like prod distribution
[00:16:09] I see so I'll yeah I think it's fair to
[00:16:12] assume that the rate of report should
[00:16:13] the size of the data set in this case
[00:16:16] especially since uh you know from my uh
[00:16:18] point of view any abuse is always going
[00:16:21] to be abuse so once it's in the database
[00:16:23] we can always reuse it in the future so
[00:16:25] to a degree it's kind of hard to argue
[00:16:28] that the distribution of data we have
[00:16:30] currently will be the distribution all
[00:16:32] the time but for now I think for
[00:16:34] Simplicity purposes I think that's a
[00:16:36] fair assumption to make at least for
[00:16:37] design purposes okay right yes
[00:16:42] in addition to that I was actually going
[00:16:45] to suggest might it might be worth
[00:16:46] thinking of dated risk ahead of time in
[00:16:49] this case because you know one year ago
[00:16:51] or two years ago even five years ago we
[00:16:53] remember
[00:16:54] images of the thing like you know it was
[00:16:56] a bigger deal but now with the age of
[00:16:58] tick tock now that's a bigger deal right
[00:17:00] people are looking at videos more often
[00:17:02] and this is why like I'm saying it might
[00:17:04] be hard to argue that the distribution
[00:17:05] will stay static but at the end of the
[00:17:08] day the data is always going to be the
[00:17:10] same it's always going to be abuse right
[00:17:12] yeah yeah
[00:17:13] and then and then uh another question is
[00:17:17] like what percentage
[00:17:19] um of posts are
[00:17:21] uh marked harmful
[00:17:25] so I'm assuming it's in like a one to
[00:17:28] two percent range kind of thing here
[00:17:32] um
[00:17:34] right
[00:17:35] yeah and Reddit is crazy so yep that's a
[00:17:37] fair function
[00:17:39] maybe right it's like five percent I
[00:17:41] don't know
[00:17:42] yeah with that platform yeah three days
[00:17:45] a lot but yeah I agree yeah or like
[00:17:48] Twitter
[00:17:49] um yeah so uh uh I guess
[00:17:53] um
[00:17:54] the last thing I think
[00:17:56] uh I wanted to cover here well I think I
[00:18:00] have enough in terms of like
[00:18:02] requirements
[00:18:04] um to kind of move forward here the like
[00:18:08] I know it's
[00:18:10] um in terms of like machine learning
[00:18:12] today like multi-modal is starting to
[00:18:14] really take over where you can just sort
[00:18:16] of give
[00:18:17] a machine learning model like I think
[00:18:19] Salesforce came out with instruct blip
[00:18:21] like two uh pretty recently and you can
[00:18:24] just like feed it
[00:18:27] um feed the model like kind of anything
[00:18:29] and it'll all figure out like
[00:18:32] um whether the model is uh or sorry
[00:18:36] it'll figure out like whether the the
[00:18:38] actual like content is uh something like
[00:18:42] abusive or violent or might be
[00:18:45] misinformation or something like that
[00:18:47] um the more like traditional way of
[00:18:49] setting it up is just having uh like
[00:18:51] kind of one model per
[00:18:54] um uh modality
[00:18:57] um and so like like that's the system
[00:19:00] I'm more familiar with but I like today
[00:19:03] if I were setting this up from scratch
[00:19:05] or even just like joining a company I'd
[00:19:08] really look at multimodal uh first to
[00:19:11] see if there are like wins there and
[00:19:14] then
[00:19:14] um but the system I'm proposing for the
[00:19:16] interviews and what I'm more familiar
[00:19:18] with which is just uh
[00:19:21] um
[00:19:22] unimodal right
[00:19:26] um
[00:19:27] yeah so let's let's hear let's do this
[00:19:29] let's make the assumption that either we
[00:19:32] have an ensemble that essentially gives
[00:19:34] us
[00:19:35] a multi-modality functionality so you
[00:19:39] know it kind of marries the two ideas
[00:19:40] where you have one model that can do it
[00:19:42] all with all data types alternatively
[00:19:44] you know you can set spin out separate
[00:19:47] models in fact I would actually argue it
[00:19:49] might be worth going with your intuition
[00:19:50] here let's go with the traditional
[00:19:52] approach reason being we already made
[00:19:55] the assumption that there might be more
[00:19:57] images that are harmful so if we have
[00:19:59] one model yet most of our content is
[00:20:01] going to expect let's say images we
[00:20:03] might want to scale that up without
[00:20:05] reading we might want to scale the
[00:20:07] processor folder uh what do you call it
[00:20:10] other image images in this case while
[00:20:13] leaving the text on to stay content but
[00:20:15] that said before you know with all the
[00:20:17] model assumptions made I would like you
[00:20:19] to talk about pre-processing like given
[00:20:22] this data that we have is there any
[00:20:24] pre-processing steps you might want to
[00:20:26] make in order to make this data
[00:20:27] available because my assumption is
[00:20:29] regardless of the type of model we have
[00:20:31] we still have to process the different
[00:20:33] data types to make it ready for the
[00:20:35] model with the target standard input
[00:20:37] type right
[00:20:38] yeah so
[00:20:41] um uh there's a few pieces here in terms
[00:20:44] of pre-processing we can kind of split
[00:20:46] it up so for text
[00:20:49] cycling talks there's uh tokenization
[00:20:52] that you need to do uh I can't spell t-o
[00:20:56] tokenization
[00:20:59] um and so like uh basically it's the
[00:21:02] process of
[00:21:04] um what like an NLP used to do where you
[00:21:06] do uh like stemming removing stop words
[00:21:11] um and uh
[00:21:13] um trying to like clean up
[00:21:14] capitalizations fix misspellings and
[00:21:17] things like that like
[00:21:19] um it was like traditionally thing you
[00:21:21] do nowadays there's libraries that
[00:21:24] basically break words up into
[00:21:27] um well tokens and then uh creates kind
[00:21:31] of like a a sort of um
[00:21:35] I want to say it's it's
[00:21:37] yeah it just assigns like an ID to each
[00:21:39] of the the tokens and then that's sort
[00:21:42] of like the sequence of
[00:21:44] um uh like features that are fed into a
[00:21:48] NLP model
[00:21:50] I think like a popular one was a tick
[00:21:53] token uh by like
[00:21:58] uh that'll actually do the the
[00:22:01] tokenization of the text
[00:22:04] um
[00:22:04] and then for uh like images and video
[00:22:09] um some of the things that are really
[00:22:11] important uh for like
[00:22:15] pre-processing I think the first one is
[00:22:17] like making sure that the dimensions of
[00:22:19] the images are like correctly sized
[00:22:22] um because if there's uh images that are
[00:22:25] like bigger or smaller trying to
[00:22:28] um uh fit all those things into the
[00:22:32] model definitely will like cause some
[00:22:34] issues and so you want to like uh scale
[00:22:38] the image uh
[00:22:39] so I haven't worked with video much but
[00:22:43] I can say like for images you definitely
[00:22:45] want to like
[00:22:46] scale it
[00:22:47] um and then also like if we are working
[00:22:50] with a very low percent of harmful
[00:22:52] content sometimes it can help to up
[00:22:55] sample uh these these images by like
[00:22:58] doing things like adding a rotation
[00:23:02] um
[00:23:03] uh uh what's it called where you you
[00:23:07] change the um like Hue saturation
[00:23:10] brightness
[00:23:12] um
[00:23:13] there's a special I don't
[00:23:17] changing like hsl values so like
[00:23:20] brightening an image darkening an image
[00:23:24] um doing all that or like changing the
[00:23:27] contrast of the image
[00:23:29] um in terms of like pre-processing to
[00:23:32] kind of get more uh sample in there
[00:23:35] make sense
[00:23:36] um
[00:23:38] yeah but my question actually yeah I
[00:23:41] have two questions particularly here so
[00:23:43] and you know totally okay if you're not
[00:23:45] familiar with any of this but this is
[00:23:47] actually a very interesting point
[00:23:48] especially in the context of valid so
[00:23:51] when it comes to tokenization here there
[00:23:53] are multiple strategies we can use you
[00:23:55] know you don't have to cite any specific
[00:23:57] tokenization strategies but in terms of
[00:24:00] token size
[00:24:01] how long do you think each token should
[00:24:04] be and for reference engram is usually
[00:24:07] like you know intro World it can be two
[00:24:10] or three syllables yet you can also have
[00:24:12] bug Words which in that regard it looks
[00:24:14] like it looks at entire words in this
[00:24:17] case or you can even have multi-word
[00:24:20] tokenization strategies so it looks at
[00:24:22] samples of phrases or something like
[00:24:24] that and you know maybe looks at overlap
[00:24:26] so in terms of tokenization which
[00:24:28] strategy do you think will make most
[00:24:30] sense in our case and why
[00:24:34] huh
[00:24:35] um good question I think uh
[00:24:41] so
[00:24:43] like single
[00:24:46] I mean like a kind of like single word
[00:24:48] tokenization sort of seems to make I
[00:24:51] mean you can't like tokenize broccoli a
[00:24:53] word
[00:24:54] um I believe like
[00:24:56] there's something like you pick like
[00:24:57] eight characters and that should be
[00:24:59] enough to sort of Encompass most words
[00:25:02] and then some words get chunked into two
[00:25:04] uh tokens I think
[00:25:08] um uh
[00:25:10] that's that's at least like what I'm
[00:25:12] kind of familiar with in the space
[00:25:15] um
[00:25:15] uh I guess like what are the the
[00:25:18] trade-offs there uh I think there's a
[00:25:20] well there's definitely a trade-off
[00:25:22] between like the
[00:25:24] um
[00:25:25] uh the more unique tokens you uh
[00:25:30] sorry there's a plane
[00:25:32] [Music]
[00:25:34] I live next to the boring hitchq so
[00:25:36] trust me I hear that a lot
[00:25:39] yeah yeah
[00:25:41] um
[00:25:42] so I think I think there's a trade-off
[00:25:44] with the uh number of like token values
[00:25:47] that your
[00:25:49] um like vocabulary has so you have to be
[00:25:53] careful like if you only do one
[00:25:54] character you end up with like
[00:25:56] you know if you use ASCII like 256
[00:25:59] values but I don't think the models are
[00:26:01] as good at being able to like pull out
[00:26:04] context on a like per character basis
[00:26:08] um now if you do like a bigger token
[00:26:11] size then then you'll have a lot more
[00:26:15] um unique values
[00:26:17] um so models will I mean think up to a
[00:26:21] certain extent models will do like
[00:26:23] pretty well
[00:26:24] um on attention it's just that now
[00:26:26] you're feeding in like a like larger
[00:26:30] um uh
[00:26:32] I guess like you kind of blow up the
[00:26:34] size of your embedding table uh a little
[00:26:37] bit so you have to kind of watch out the
[00:26:39] mem watch out for your memory of your
[00:26:41] system
[00:26:42] excellent that's exactly what I'll start
[00:26:44] getting right there and it's really
[00:26:45] really good that you brought in context
[00:26:47] because abuse is in context you know uh
[00:26:50] that is always have the same characters
[00:26:52] as praise so in that regard I think
[00:26:55] you're right I think I would also lean
[00:26:57] towards a single one probably towards
[00:27:00] multiple words token Aviation especially
[00:27:02] since you know nowadays a lot of abuse
[00:27:05] will lean towards three four words like
[00:27:07] people will combine multiple ones a
[00:27:09] single one that is you know sometimes
[00:27:11] abusive might not necessarily be abusive
[00:27:13] if I let's say I'm describing the word
[00:27:15] stupid
[00:27:15] in itself it might not be abusive but
[00:27:18] yeah you're calling a person abuse are
[00:27:20] stupid then that is actually instant
[00:27:22] insult so I think multi-word
[00:27:24] tokenization you can also justify a
[00:27:26] single one tokenization in that regard
[00:27:28] and then this yeah that was something
[00:27:30] you mentioned that made me think a bit
[00:27:32] so you mentioned that we need to be
[00:27:34] mindful of performance but that's why
[00:27:36] maybe I might question it a bit because
[00:27:38] if we have let's say single word or
[00:27:39] multi-word tokenization then to a degree
[00:27:41] we are reducing the total cardinality of
[00:27:45] the total number of tokens DNA returned
[00:27:47] from any particular text input which
[00:27:49] could actually end up helping the
[00:27:51] performance compared to let's say doing
[00:27:52] an engram tokenization where we're
[00:27:54] looking at individual characters so do
[00:27:57] you think let's say this approach would
[00:27:59] actually end up meaning something in
[00:28:01] terms of path like I would say intuition
[00:28:02] on that
[00:28:05] um somebody okay so so basically just to
[00:28:08] to
[00:28:09] re-reiterate what you just said the idea
[00:28:12] is like as you
[00:28:14] choose like a larger like a multi-wad
[00:28:17] like token that that should result in an
[00:28:20] increase in the number of
[00:28:23] um uh what do you call it it's like a
[00:28:27] decrease in the sequence length but also
[00:28:30] an increase in the kind of like
[00:28:32] embedding table size right
[00:28:36] um
[00:28:37] uh so I guess like in terms of
[00:28:40] performance
[00:28:43] um
[00:28:44] I'm not actually
[00:28:47] 100 sure on one what would actually end
[00:28:51] up uh causing the most issues I think
[00:28:53] like
[00:28:54] my feeling is that at training time
[00:28:58] um having like a larger embedding table
[00:29:00] can uh be more memory intensive but at
[00:29:03] inference time your uh context like the
[00:29:07] sequence link that you actually need
[00:29:10] um should be like shorter and so the
[00:29:13] inference should be
[00:29:16] um quicker because you're just doing
[00:29:18] less like matrix multiplication at
[00:29:21] inference time
[00:29:23] um that's that's my intuition on it I
[00:29:25] think
[00:29:26] that's a that kind of confuses me though
[00:29:29] because technically with the reduced
[00:29:31] number of token sizes or at least the
[00:29:33] radius number of tokens we should
[00:29:35] technically also have a reduced
[00:29:37] embedding table size because each of the
[00:29:40] yeah right because the size of the
[00:29:41] embeddings themselves yeah the number of
[00:29:44] embedding should stay roughly the same
[00:29:46] the size of the embeddings is what will
[00:29:47] vary right right yeah yeah yeah
[00:29:51] um and
[00:29:52] just a tools
[00:29:54] a bit further in terms of capacity do
[00:29:57] you think there are any implications
[00:29:59] with let's say a multi-word tokenization
[00:30:01] compared to let's say uh engram
[00:30:03] tokenization
[00:30:07] um in terms of sparsity uh yeah like
[00:30:14] uh I mean
[00:30:18] so I
[00:30:26] I guess like with with
[00:30:30] this is just a guess because I I don't
[00:30:33] actually uh know but I'm guessing like
[00:30:35] there's a
[00:30:37] um uh
[00:30:42] I'm guessing with like engrams there's
[00:30:44] probably a higher
[00:30:46] sparsity of tokenization
[00:30:49] um
[00:30:52] hello
[00:30:54] Lucia
[00:31:03] hello
[00:31:06] foreign
[00:31:30] hello
[00:31:38] [Music]
[00:31:40] I hear something
[00:31:43] oh can you hear me now
[00:31:45] oh I don't know what happened there yeah
[00:31:47] sorry I was saying you are right your
[00:31:49] intuition is very correct on that
[00:31:50] because objectively if we have engrams
[00:31:53] we have a huge embedding table because
[00:31:55] there are too many unique bodies and so
[00:31:57] for it to make sense you have to have
[00:31:59] huge embeddings in this case probably
[00:32:01] more than 10 30
[00:32:04] 36. so in that regard most of the values
[00:32:07] of the zeros and so we lined up with too
[00:32:10] many zeros and two little information
[00:32:12] but with multi-word tokenization small
[00:32:15] embeddings which will mostly have values
[00:32:18] because in this case essentially with
[00:32:21] all n is the same size of input we have
[00:32:22] fewer boxes to eat and so not only will
[00:32:25] they be more useful because they
[00:32:27] encapsulate context too and so it also
[00:32:30] ends up helping the performance in that
[00:32:31] regard but anyway sorry we spent a bit
[00:32:33] too much time on that so I think we can
[00:32:35] move on in this regard let's maybe talk
[00:32:37] about the API so given what we have here
[00:32:39] talk to me about some apis we might want
[00:32:41] to design in order to solve this data
[00:32:45] uh yeah so
[00:32:48] um
[00:32:49] uh let's see
[00:32:52] um so I could see like a few different
[00:32:54] uh systems here I mean so the idea is
[00:32:57] that
[00:32:58] we kind of said we're going to do
[00:33:01] um uh single modal
[00:33:04] um uh inference and
[00:33:07] um inference
[00:33:09] in this case it could be done uh as like
[00:33:13] a a batch inference or online
[00:33:16] um to me they kind of like both uh
[00:33:21] work
[00:33:22] um because talking with an async process
[00:33:26] um but also like the this data is kind
[00:33:28] of coming in as a stream so like uh to
[00:33:32] me I think it's just
[00:33:33] um
[00:33:34] like easier to kind of uh
[00:33:38] model it as an online uh inference
[00:33:42] system in just sort of like a little
[00:33:44] more future proof if you do need it to
[00:33:46] be more real-time it will still be there
[00:33:48] you don't have to migrate from batch to
[00:33:49] real time
[00:33:53] um so like there's basically going to be
[00:33:55] three services uh one for image one for
[00:34:01] text and one for video
[00:34:09] um so maybe it's like moderate
[00:34:13] um seek and say service dot moderate and
[00:34:15] then uh the
[00:34:18] request
[00:34:19] um
[00:34:20] should be like post requests and if
[00:34:23] we're thinking about like what kind of
[00:34:24] data we want for the body
[00:34:27] um uh so we should have like features
[00:34:29] and then we'll uh pass in a list of
[00:34:34] features
[00:34:36] [Music]
[00:34:36] um
[00:34:37] the I guess like should the I mean the
[00:34:41] services should be doing the same
[00:34:43] pre-processing that we're doing to uh
[00:34:46] generate the data and and train the
[00:34:49] model with it
[00:34:51] um so uh I think like these features
[00:34:56] I mean in in reality the way this would
[00:34:59] kind of work is that you use like
[00:35:00] feature IDs and then sort of work
[00:35:02] through some kind of a feature store
[00:35:06] um so this is actually something I
[00:35:08] didn't cover but I feel like we we
[00:35:11] should talk about is
[00:35:12] um uh it's not just um image text and
[00:35:16] video but also like user profiles might
[00:35:18] also be something that we want to like
[00:35:21] consider
[00:35:22] at least in the the future so it's not
[00:35:24] just like show me an image it's like
[00:35:26] show me
[00:35:28] um an image by a like particular user
[00:35:31] and then maybe that helps with
[00:35:33] identifying
[00:35:35] um things like misinformation like if a
[00:35:37] if there's a post and that user has been
[00:35:40] reported a number of times maybe that
[00:35:42] actually like positively impact
[00:35:45] um but maybe that's like a I'm like
[00:35:48] sorry I'm kind of thinking out loud here
[00:35:49] I'm a little disorganized I think
[00:35:52] um
[00:35:54] I think having
[00:35:56] the three services here and then another
[00:36:00] service a fourth one for just uh text
[00:36:03] misinformation
[00:36:07] that makes sense
[00:36:09] these are a lot easier to
[00:36:12] um moderate and then uh with
[00:36:15] misinformation it's a little more
[00:36:17] subjective and uh the model may end up
[00:36:21] having features in it that the text
[00:36:23] model uh
[00:36:25] uh doesn't need to include so that's why
[00:36:28] I'm kind of like uh
[00:36:30] building this out as a separate service
[00:36:33] here
[00:36:35] um so for uh this API
[00:36:40] um you'll pass in a a list of features
[00:36:44] maybe it's as simple as just saying like
[00:36:45] a dictionary and then we can say the
[00:36:49] text
[00:36:50] for text right
[00:36:54] um One Two Three or or
[00:36:57] um
[00:36:58] uh
[00:36:59] same with images it'd just be the blob
[00:37:02] or video
[00:37:03] um
[00:37:08] uh so the blob and the bite
[00:37:12] and then the same thing with the video
[00:37:13] right so that's just the the kind of the
[00:37:16] Epi there
[00:37:17] uh and then the response is going to be
[00:37:20] a list of
[00:37:22] um
[00:37:23] uh labels and uh confidences so
[00:37:28] uh you'd say like results
[00:37:33] and then so we'll have like a label
[00:37:36] and then so we may want to say like this
[00:37:40] is
[00:37:41] like the abuse label
[00:37:43] and then we can give a like a confidence
[00:37:49] uh and then this will be a float between
[00:37:52] zero and one so this could be like
[00:37:56] um
[00:37:57] and then like we can have other labels
[00:38:00] here as well so we'd have like labels
[00:38:02] for nudity violence
[00:38:07] um
[00:38:12] and then um yeah please
[00:38:17] yeah
[00:38:19] these would be like the labels yeah
[00:38:23] um so that's basically the uh the apis
[00:38:26] of the service
[00:38:28] um
[00:38:29] in terms of like uh there's a few
[00:38:33] important things here
[00:38:35] um uh which is like as a system as a
[00:38:39] whole there are uh
[00:38:41] well the thing I want to touch on is
[00:38:43] like there's training metrics and then
[00:38:45] there's online metrics and like how are
[00:38:47] we doing
[00:38:49] um
[00:38:49] uh so for things like online metrics uh
[00:38:53] like actual production metrics we want
[00:38:55] to cover things like the number of
[00:38:58] um
[00:38:59] we call it harmful uh
[00:39:04] uh oops
[00:39:06] we'll call it harmful impressions
[00:39:09] um and so that's just the number of
[00:39:11] people that have seen these things uh
[00:39:14] and then like number of reports
[00:39:18] nice nice
[00:39:20] and uh uh maybe even
[00:39:25] um
[00:39:26] uh
[00:39:28] so there's
[00:39:31] um Impressions and then also maybe like
[00:39:33] a time-based one so like uh average time
[00:39:38] um
[00:39:39] to take down
[00:39:41] so when we when something is like posted
[00:39:45] reactively and we need to take it down
[00:39:47] we want to be able to take it down
[00:39:48] quicker and hopefully models will
[00:39:50] facilitate that that take down time
[00:39:54] um in terms of actual like
[00:39:57] uh training metrics
[00:40:00] uh some of the things that
[00:40:03] um we want to like consider here so
[00:40:07] when we're training on image text or
[00:40:09] video we're doing a
[00:40:12] um
[00:40:13] a
[00:40:14] multi-class classification
[00:40:18] um which means that we'll be doing a
[00:40:23] uh
[00:40:25] orals that are mixed up all the time
[00:40:27] it's um
[00:40:32] oh sorry
[00:40:34] um
[00:40:36] yeah yeah so uh we care about uh
[00:40:44] uh and recall
[00:40:46] um
[00:40:47] and so Precision is basically the uh
[00:40:52] number of uh true positives divided by
[00:40:57] um the two positives plus the false
[00:41:01] positives and the recall is two positive
[00:41:04] is divided by
[00:41:07] negatives
[00:41:12] in terms of like
[00:41:15] uh how we want to actually like present
[00:41:18] this I think just presenting in terms of
[00:41:20] precision and recall
[00:41:21] like you don't have to do an F1 score or
[00:41:24] like a
[00:41:27] receiver or operator curve
[00:41:31] just leaving his Precision recall works
[00:41:36] and uh
[00:41:38] yeah I mean in these questions
[00:41:42] nope no question on that maybe just a
[00:41:44] quick suggestion because I was literally
[00:41:46] typing feedback on this bit because I
[00:41:48] totally relate to you on one bit I
[00:41:50] absolutely hate these two terms because
[00:41:52] I really remember what it was
[00:41:55] and so my fallback is literally saying
[00:41:58] I'm just gonna generate a confusion
[00:41:59] Matrix because it's gonna allow me to
[00:42:02] interpret the same metric the same way
[00:42:04] like I'm I'm better with the intuition
[00:42:06] rather than the terminologies but I
[00:42:09] totally agree on this yeah
[00:42:11] yeah that makes sense
[00:42:13] um okay so uh
[00:42:16] that's that for uh
[00:42:18] uh for training metrics uh actually
[00:42:20] sorry quick question objectively
[00:42:22] speaking because uh given this metrics
[00:42:25] these training metrics are there can you
[00:42:27] define to me the objective of the model
[00:42:29] and
[00:42:31] yeah
[00:42:34] um so that there's you're talking about
[00:42:36] like the loss function
[00:42:38] and not necessarily the most function we
[00:42:40] can speak on that later given we have a
[00:42:41] multi-classification problem here but
[00:42:43] I'm interested in what is the goal like
[00:42:45] do you want to minimize Precision while
[00:42:47] maximizing recoil or do you want to
[00:42:49] maximize both like what's the goals
[00:42:50] particularly
[00:42:52] yeah so I think
[00:42:54] um uh
[00:42:56] so this is actually interesting because
[00:42:58] like it depends on the business
[00:43:00] um objectives and time so I've actually
[00:43:02] seen that at my company where
[00:43:06] um we basically said like for a while we
[00:43:09] were okay with businesses
[00:43:11] um we were okay with uh
[00:43:14] um being very strict in terms of
[00:43:18] of I want to say like false negatives
[00:43:20] and then economic downturn kind of
[00:43:24] happened and then we kind of said like
[00:43:25] hey we don't we don't want to be
[00:43:29] um uh
[00:43:31] we want less false positives because we
[00:43:33] want people to actually spend on our
[00:43:38] um platform
[00:43:39] and so we were actually willing to trade
[00:43:42] off like recall I think back for
[00:43:44] precision
[00:43:45] um or by any other way but like business
[00:43:49] metrics but if you're if you're trying
[00:43:51] to
[00:43:53] um juice engagement
[00:43:55] then uh you want to be careful with
[00:43:59] um
[00:44:00] uh I think it's
[00:44:02] okay so false negative in this case
[00:44:04] would be
[00:44:06] um
[00:44:07] classifying something as harmful when
[00:44:09] it's not
[00:44:11] and so
[00:44:13] um uh
[00:44:15] if you're trying to like juice
[00:44:16] engagement metrics having a very
[00:44:20] um uh
[00:44:22] High precision and low recall is good
[00:44:30] um because if you have high Precision
[00:44:33] low recall what we're basically saying
[00:44:36] is we're trying to
[00:44:39] um
[00:44:39] we're okay with like harmful content
[00:44:45] making it half the model
[00:44:49] uh because we don't
[00:44:53] want to block like good content
[00:44:59] so in this case essentially what you're
[00:45:01] saying is we are okay
[00:45:05] rather than being less sensitive and as
[00:45:08] missing on actual abuse contents like
[00:45:10] it's okay if they report something and
[00:45:12] they find out it's not harmful and
[00:45:14] restore it rather than the opposite way
[00:45:15] they failed reports or we fail to plug
[00:45:18] and excellent so we're basically making
[00:45:20] our thresholds very low forward abuse
[00:45:22] or or a flag for abuse
[00:45:26] but tell me of course we have the human
[00:45:27] in the loop so we'll always have a
[00:45:29] restoration process but those who did
[00:45:31] that yeah I think that's an excellent
[00:45:32] approach and I was actually very happy
[00:45:34] with that because I was gonna Grill you
[00:45:36] after that on that point like would you
[00:45:39] want it to be you know the opposite and
[00:45:42] why but I think you immediately went to
[00:45:44] it which was accident yeah and then yeah
[00:45:46] final content system
[00:45:48] uh-huh sorry I was gonna sort of make a
[00:45:50] joke which is this is until uh you have
[00:45:53] to advertise on the platform and Brandon
[00:45:59] um yeah actually if you think about it
[00:46:01] though that strategy can actually help
[00:46:04] because if we are worried about
[00:46:06] advertisement then
[00:46:08] unless we are worried about the rate of
[00:46:10] reporting on advert because we know it
[00:46:12] is always annoy people and then they'll
[00:46:14] report it but I think advertisers will
[00:46:16] probably be happy with a platform that's
[00:46:18] a bit more strict because you know we
[00:46:21] look at let's say Twitter right Twitter
[00:46:22] is not strict at all right non-abuse and
[00:46:25] they pulled up because they don't want
[00:46:27] the possibility of being 16 with right
[00:46:30] so to a degree that strategy will
[00:46:32] actually help with ads do you think
[00:46:35] um
[00:46:36] the the
[00:46:38] opposite strategy right because what
[00:46:41] we're saying is we'll let harmful
[00:46:43] content through and because we don't
[00:46:45] want to block good content accidentally
[00:46:47] and then if you want to be brand safe
[00:46:49] we'll actually start blocking more
[00:46:51] harmful content at the expense of
[00:46:53] blocking some good ones every once in a
[00:46:55] while so we're more brand safe
[00:46:57] exactly yeah yeah
[00:47:00] yeah we're in line on that okay and then
[00:47:03] let's see I had a final question with
[00:47:05] respect to metrics and then you know the
[00:47:06] next section I wanted you to focus on
[00:47:08] before it is to get a feedback is
[00:47:10] killing so just pure architecture talks
[00:47:12] I was thinking how are you going to
[00:47:14] scale it up but before we do that
[00:47:16] now that we have our objective function
[00:47:18] uh our objective in this case can you
[00:47:21] talk to me about the loss function like
[00:47:22] if you're going to choose a loss
[00:47:24] function here for your model like this
[00:47:25] is the most technical I'll get to the
[00:47:27] model but uh what loss function do you
[00:47:29] think would make most
[00:47:30] yeah so
[00:47:32] um
[00:47:33] the loss function is uh
[00:47:38] uh oh I'm blinking so it's a multi-class
[00:47:41] classification
[00:47:42] uh and I know that you apply well you're
[00:47:50] supposed to apply a soft Max
[00:47:52] at the the very end and then what you do
[00:47:54] is you compute well you compute the loss
[00:47:56] the loss is
[00:47:58] um
[00:47:59] uh in this case my
[00:48:05] um
[00:48:09] the only one I'm
[00:48:11] thinking of is well there's there's two
[00:48:16] um
[00:48:17] like mean squared error or like maximum
[00:48:21] likelihood
[00:48:23] um
[00:48:24] uh I mean I think like
[00:48:27] maximum likelihood
[00:48:31] sounds like it'd be the right
[00:48:35] right loss function
[00:48:38] um but I'm gonna have a hard time with
[00:48:39] this section because I uh
[00:48:43] uh definitely need to study up on my
[00:48:45] loss functions
[00:48:48] all right are you familiar with cross
[00:48:50] entropy
[00:48:51] oh
[00:48:53] um
[00:48:54] familiar with cross entropy I think uh
[00:48:58] it's oh
[00:49:00] I mean I know the word I don't know what
[00:49:02] it represents at the moment
[00:49:04] yeah so the reason I brought up I
[00:49:06] brought that up is because at least from
[00:49:08] my understanding it's been a while since
[00:49:10] I had to
[00:49:11] but I remember it as a way of estimating
[00:49:15] my my parameters for my model
[00:49:19] sorry
[00:49:24] tuning the parameters
[00:49:26] but the loss functions we tend to be
[00:49:30] things like cross entropy it could be
[00:49:32] you know there's binary cross entropy
[00:49:34] when you have two labels or multi-level
[00:49:36] cross entropy when you have multiple
[00:49:38] levels uh the things like hinge loss
[00:49:41] maybe focal loss and a couple of other
[00:49:42] examples I cannot think of all of them
[00:49:44] off of the top of my head but honestly
[00:49:47] and this is the you know a quick tip
[00:49:50] cross entropy will almost always be a
[00:49:52] good answer when you asked about the
[00:49:54] loss function the only difference might
[00:49:56] be you need to showcase the intuition on
[00:49:59] the variant so things like multi-level
[00:50:01] or binary as well as understanding how
[00:50:03] it penalizes false predictions now the
[00:50:06] downside to it though is it's excellent
[00:50:08] for supervised problems where we have
[00:50:10] labeled input in our case that would
[00:50:12] work well but for unsupervised problems
[00:50:16] that becomes a bit of a problem and this
[00:50:18] is where I think of let's say
[00:50:19] pre-clustering in order to get a sense
[00:50:21] of uh let's say some sense of labels
[00:50:24] that might actually be helpful
[00:50:26] okay yeah yeah all right yeah and then
[00:50:30] final bit of uh probing in this case so
[00:50:32] talk to me about deployment so say we've
[00:50:34] set this up uh how are you thinking of
[00:50:37] let's say scaling the system up uh it
[00:50:39] may be and like are you gonna have like
[00:50:41] a multi-service architecture or like a
[00:50:44] monolith like water intuition
[00:50:47] um yeah so uh there's a few things here
[00:50:51] the the first like point is
[00:50:55] um you know uh my my initial launch I'd
[00:51:00] want the models to be small enough to
[00:51:03] fit on a single like GPU for inference
[00:51:06] because if I had to do like a
[00:51:08] distributed GPU thing uh that just adds
[00:51:11] uh more complexity to the system
[00:51:15] um uh so like single GPU inference
[00:51:19] that'd be nice
[00:51:21] um and uh
[00:51:23] um you know we basically put a load
[00:51:26] balancer in front of a number of these
[00:51:28] uh instances I think each of the major
[00:51:31] Frameworks has like their own serving
[00:51:33] framework so like a pytorch and
[00:51:35] tensorflow have their own like serving
[00:51:38] infrastructure so I would just run it on
[00:51:41] uh top of that
[00:51:43] um and uh
[00:51:46] um
[00:51:47] yeah I mean like in terms of like doing
[00:51:50] uh a couple things that are important
[00:51:52] I'd want to make sure that
[00:51:54] um I'm logging all of the features at
[00:51:57] request time
[00:51:59] um one thing I want to do to make sure I
[00:52:01] minimize the amount of potential data
[00:52:05] leakage that's happening
[00:52:07] um in terms of like rolling that data
[00:52:08] out into the new data set and then also
[00:52:10] uh we want some like uh
[00:52:14] um
[00:52:14] metrics and monitoring uh to watch for
[00:52:18] data set distribution shifts so things
[00:52:20] like anomal infections to figure out
[00:52:22] like hey are we getting a bunch of nulls
[00:52:24] or a particular
[00:52:27] um uh feature like in this case it's
[00:52:30] text images and videos but if we're
[00:52:32] doing
[00:52:33] um something with like uh
[00:52:36] misinformation where we care about the
[00:52:38] user profile like you do care about that
[00:52:40] kind of like data distribution shift
[00:52:43] um and also like you want to look for
[00:52:44] your label shifts too like there could
[00:52:46] just be like all of a sudden one day
[00:52:48] everyone's posting a bunch of crypto
[00:52:50] nonsense and like you're predicting a
[00:52:53] lot more uh
[00:52:56] um like abuse on the platform that day
[00:52:58] so you do need to be able to alert say
[00:53:00] like hey our models
[00:53:02] um are kind of going off the rails here
[00:53:05] um the system that I would actually set
[00:53:07] up okay so there's there's scaling
[00:53:09] scaling I would just do a load balancer
[00:53:11] with a cluster of machines as CPU or GPU
[00:53:15] I guess utilization uh reaches a
[00:53:18] threshold add more
[00:53:21] um clusters to the machine and auto
[00:53:22] scale the the thing I would I would want
[00:53:25] to do though is on any new model rollout
[00:53:28] to do an AP study
[00:53:30] um just to see how the models performing
[00:53:33] online versus the existing Baseline uh
[00:53:36] before just blindly deploying it out to
[00:53:39] production
[00:53:42] doesn't really make sense and you know
[00:53:43] just a quick point on in addition to
[00:53:45] what you've just mentioned there are
[00:53:47] also other benefits to think about given
[00:53:49] that our service you know and maybe you
[00:53:51] should have clarified this initially
[00:53:53] ought to be global abuse in the US might
[00:53:56] not necessarily be abused in some other
[00:53:58] place and in similar regard we have
[00:54:01] inputs that might be different that
[00:54:03] might completely distort the model like
[00:54:05] you know we want to stratify the models
[00:54:07] by geographic features like language
[00:54:10] like you know what might happen in China
[00:54:12] versus what might happen in Russia the
[00:54:14] languages are completely different the
[00:54:15] input
[00:54:16] you probably want different
[00:54:19] play or your approach here where we have
[00:54:21] many models or microservices essentially
[00:54:23] and distributing them depending on the
[00:54:25] data service that will end up being a
[00:54:27] very useful
[00:54:29] useful of these Papas too right
[00:54:31] yeah
[00:54:32] yeah having like original yeah
[00:54:37] okay we have about five minutes left I
[00:54:40] will add a couple more to make sure we
[00:54:42] are going
[00:54:44] but for context I never give feedback
[00:54:46] straight up I usually want to first get
[00:54:48] your intuition so looking back at the
[00:54:50] interview what do you think you did well
[00:54:52] and what do you think you could improve
[00:54:54] I think
[00:54:55] um I did all right with the initial part
[00:55:01] um the sort of like requirements
[00:55:02] Gathering uh I definitely need to go
[00:55:05] deeper well I got like stuck on the
[00:55:07] tokenization uh piece
[00:55:11] um so like I think there's just a little
[00:55:14] bit more focus on some of the machine
[00:55:15] learning aspects of things like you know
[00:55:17] what are some of the more like common
[00:55:20] like pre-processing Steps tokenization
[00:55:23] looking at like the different scalings
[00:55:27] and things like that like doing log
[00:55:28] Transformations when your data
[00:55:30] distribution isn't exactly uh gaussian
[00:55:33] things like that I need to just like
[00:55:35] Refresh on
[00:55:37] um
[00:55:37] uh
[00:55:39] I thought like the API endpoint part was
[00:55:42] fine
[00:55:44] um
[00:55:45] yeah like I don't know if there's
[00:55:47] anything like really glaring there
[00:55:49] um uh I mean ultimately I feel like you
[00:55:54] know
[00:55:56] I'm not sure I mean I called it out in
[00:55:58] the beginning which was like we really
[00:56:00] should be doing a multimodal system
[00:56:01] that's just like more intelligent I I
[00:56:04] have a feeling that that would actually
[00:56:06] perform better
[00:56:08] um
[00:56:08] but like
[00:56:11] um so I'm glad I called that out and
[00:56:13] then went with the system that I'm a
[00:56:15] little bit more familiar with it's like
[00:56:18] it actually likes each of these things
[00:56:20] um I'm not actually sure if it's like
[00:56:23] better to do it that way uh in a real
[00:56:27] interview
[00:56:28] or if it's like by going this way I'm
[00:56:30] giving the interviewer an opportunity to
[00:56:32] dig on like like let's talk about image
[00:56:35] related models let's talk about like
[00:56:38] text related models
[00:56:40] um versus like potentially
[00:56:43] um
[00:56:44] like if I'm saying let's build some like
[00:56:45] multimodal system and the interviewer
[00:56:48] doesn't know how to or isn't familiar
[00:56:50] with multimodal systems than like
[00:56:52] I'm not sure if they're getting signal
[00:56:54] so I'm not sure if that's like the right
[00:56:56] path to to take there
[00:56:58] um I did just like I need to just do
[00:57:00] better on my loss function stuff
[00:57:03] um and uh uh just kind of yeah didn't
[00:57:07] get that piece
[00:57:10] um
[00:57:11] and then
[00:57:13] uh I mean other than that like I think
[00:57:15] everything kind of
[00:57:18] um did all right
[00:57:21] so that's sort of how I I feel like
[00:57:23] there's some ups and downs um definitely
[00:57:25] not like the perfect interview
[00:57:28] um
[00:57:30] here's the thing I rarely find a person
[00:57:33] who finds out for mentorship but then at
[00:57:35] the end I'm telling them I will probably
[00:57:37] give you a pass so you actually be
[00:57:40] pretty damn well
[00:57:42] so I still took it still took a ton of
[00:57:44] notes as I said uh so you know to start
[00:57:48] with keeping it short I frankly think
[00:57:50] you're almost there like uh it was to
[00:57:52] give you like feedback in case you want
[00:57:54] to sign up for more sessions you
[00:57:56] probably need at most five if not three
[00:57:58] three just to kind of refine the process
[00:58:01] because in terms of content you probably
[00:58:03] are one of the few people been able to
[00:58:05] keep up with the line of questioning
[00:58:07] I've asked which was excellent so you
[00:58:09] know just to go through the feedback and
[00:58:11] mind you'll paste all of this in in
[00:58:13] addition to some extra resources you can
[00:58:15] look at at the end for the most part I
[00:58:17] agree with you but you know objectively
[00:58:19] communication excellent like you're
[00:58:21] really easy to communicate with easy to
[00:58:23] follow even throwing jokes on occasion
[00:58:25] in the interview which keeps it
[00:58:26] light-hearted so really really did well
[00:58:28] with that
[00:58:29] and then the line of questioning with
[00:58:31] respect to background processes I really
[00:58:34] really like that because most people
[00:58:35] fail to think about that they think they
[00:58:37] have to design Reddit in fact one of the
[00:58:39] biggest problem I've had with candidates
[00:58:40] is you ask them to detect how to design
[00:58:43] a harmful content protection process but
[00:58:45] they don't think about the background
[00:58:47] processes that exist so you started with
[00:58:49] that make it a point in any interview
[00:58:51] like nobody is asking to design the
[00:58:53] actual system they are designing a new
[00:58:55] system in exist in addition to the
[00:58:58] platform that's already there so feel
[00:59:00] free to denote exactly what you think
[00:59:03] already exists and maybe this is where
[00:59:05] one bit of improvement you can have here
[00:59:07] is actually detailing those bits so if
[00:59:11] we expect that let's say ready to give
[00:59:12] us apis that can extract text or
[00:59:15] alternatively if we expect that you have
[00:59:17] a push model where if a post is made a
[00:59:21] model automatically consumes that post
[00:59:23] or you know has that post uh pushed into
[00:59:26] let's say some message queue where we
[00:59:28] can consume it and process it it will be
[00:59:30] good to talk about it from that stage
[00:59:32] and in fact for most my most machine
[00:59:34] learning interviews I think that's
[00:59:36] probably the best Stage to start it just
[00:59:38] thinking about what's my input like
[00:59:40] what's the current platform giving me in
[00:59:43] terms of input of course yes it's not
[00:59:45] like a you know platform based system it
[00:59:48] could be different but typically data
[00:59:50] source is always the first stage but it
[00:59:52] was really really good to hear you
[00:59:53] actually talk about that because it
[00:59:55] shows that you had the intuition to
[00:59:56] think about that bit and then
[00:59:59] uh on line 85 I mentioned the
[01:00:01] pre-processing bit I felt as though you
[01:00:03] were not thinking about it until I
[01:00:05] pushed you in that direction and so
[01:00:08] okay right like you know I had to
[01:00:10] actually ask you okay how are you going
[01:00:12] to standardize this how are you going to
[01:00:13] pre-process it but once I asked you you
[01:00:15] went in depth on tokenization
[01:00:18] pre-processing removal of stopwatch it
[01:00:21] is key to think about that because part
[01:00:22] of the ml system design but sometimes
[01:00:24] you may find that that's the state that
[01:00:26] requires the most ml system design work
[01:00:29] because these are heavy processes like
[01:00:31] you can imagine uh you know when you
[01:00:33] have a bunch of images or even let's say
[01:00:35] videos where you have to do frame
[01:00:37] sampling then that's computationally
[01:00:39] intensive and it's usually what we're
[01:00:41] thinking about how that setup is going
[01:00:43] to look like what those features you
[01:00:45] know once you've extracted the features
[01:00:47] because this is basically the feature
[01:00:48] engineering part once you've extracted
[01:00:50] them where you're gonna store them
[01:00:52] because you know you don't want to
[01:00:53] process all of that and then all that
[01:00:55] data is basically output into some log
[01:00:58] file you want to actually think about
[01:00:59] the data output in that case talk about
[01:01:01] let's say readys or whatever you know
[01:01:04] data ta and storage solution you have
[01:01:06] where the model can consume from there
[01:01:08] in a quick manner so it might be what I
[01:01:11] was talking about API endpoints there
[01:01:13] maybe talk about them being marked by
[01:01:16] let's say
[01:01:18] I don't know ready for some other
[01:01:19] systems so that's stage one of the
[01:01:21] system design and then you know I give
[01:01:23] you a breakdown you can clearly see
[01:01:24] online 82 on how I typically do it it's
[01:01:27] kind of worked well for me maybe it can
[01:01:30] inspire you to curate a process for you
[01:01:32] so typically it's usually requirements
[01:01:34] pre-processing and then Define my apis
[01:01:37] both the input and output before I even
[01:01:39] jump into the model stuff and then I
[01:01:42] think we delve deep here yeah I actually
[01:01:44] made the point on that you went deep
[01:01:46] into it so I didn't really have any line
[01:01:47] of questioning on that so that was good
[01:01:49] so for the tokenization bit I think we
[01:01:52] kind of covered much of that
[01:01:53] conversation in the interview but
[01:01:55] Refresh on that that way at least you
[01:01:57] have a stronger sense of the intuition
[01:02:00] between of the implication or
[01:02:02] performance between shorter than the
[01:02:04] Lord so clearly that's probably the
[01:02:07] weakest point of the interview because I
[01:02:09] felt like we were going through like you
[01:02:11] know kind of like throw something at the
[01:02:13] wallet see if it sticks but for the most
[01:02:15] part it was good that you even knew of
[01:02:17] the different education strategies even
[01:02:19] went to a level of giving me examples
[01:02:20] which I could identify so I really
[01:02:22] appreciate that and then yeah like let's
[01:02:26] see I think this is the same point I've
[01:02:27] made there where pre-processing is
[01:02:29] always step one so it was good that we
[01:02:31] talked about that and then in terms of
[01:02:33] output I felt like you really you know
[01:02:36] once you were done with like the core
[01:02:38] apis the rest of the stages are perfect
[01:02:41] like it was like you talked about the
[01:02:44] output you expect in fact uh the funny
[01:02:46] thing when you said the API was okay to
[01:02:48] me it was like this is probably closer
[01:02:51] to what I would want to see in an
[01:02:52] interview where somebody actually gives
[01:02:54] me example payloads I always ask for
[01:02:56] example payloads most people won't give
[01:02:58] that so this was actually really really
[01:03:00] good so the only maybe you know there's
[01:03:03] a myths I would say maybe include the
[01:03:06] expected protocol for the for machine
[01:03:09] Learning System design I don't think
[01:03:10] I'll push anybody down to that uh you
[01:03:12] know up to that level but the reason why
[01:03:15] I might want to converse about that is
[01:03:17] sometimes it's worth thinking about
[01:03:18] let's say the concurrency or the number
[01:03:20] of requests I expect so if the API it is
[01:03:24] gonna it's gonna expect a lot of let's
[01:03:26] say get requests get requests tend to be
[01:03:28] more performance and let's say post
[01:03:30] requests so when you're talking about
[01:03:32] that especially in this case you know
[01:03:34] there will be a lot of text request
[01:03:36] coming in like as soon as the post is
[01:03:38] made that request is made so there
[01:03:40] should be a ton of them especially since
[01:03:42] the share volume is going to be a lot
[01:03:43] but most of the payloads will be tiny so
[01:03:46] in that case we probably want to have
[01:03:48] lightweight post requests in this case
[01:03:51] you know those maybe the downside might
[01:03:53] be since most uh most uh of the requests
[01:03:57] will correspond to a unique thread then
[01:04:00] maybe post my touch is that actually
[01:04:02] good is it supposed to put like in terms
[01:04:05] of method because I want to create a
[01:04:08] post is kind of a
[01:04:10] well like there's there's two ways to
[01:04:12] think about it's like rest and then
[01:04:14] there's just like
[01:04:15] Json or PC
[01:04:18] um so if you're thinking about it in
[01:04:19] terms of like rest a post request is
[01:04:21] more intend to create something and a
[01:04:24] put is like a update on the full entity
[01:04:28] people who like grpc is all post
[01:04:31] requests even if you want to get
[01:04:33] something
[01:04:35] um I see which one is the one that has
[01:04:37] bad impotency I think it's a post uh
[01:04:44] like in terms of like a session Aid and
[01:04:46] potential
[01:04:47] I can't remember which
[01:04:48] uh uh
[01:04:50] I mean
[01:04:52] I would assume like
[01:04:55] poets or
[01:04:57] I mean they're both supposed to be item
[01:05:00] potent I think uh it's it's uh
[01:05:04] um uh
[01:05:06] yeah I don't think it should matter like
[01:05:07] like for instance if you're doing a
[01:05:09] endpoint you want to post to like create
[01:05:12] the payment
[01:05:13] um but that's the item potent like if
[01:05:15] you try and call it twice
[01:05:18] um it needs to
[01:05:20] like have the same result today yeah
[01:05:25] actually I do believe put is actually
[01:05:27] item uh put his either important well
[01:05:29] post is not so and this is actually the
[01:05:31] key bit right there so if we made a put
[01:05:33] request especially since we know most
[01:05:35] requests will not be updating they'll be
[01:05:37] sending this one request to the process
[01:05:39] we're done and that's where maybe you
[01:05:41] can justify both because we you know I
[01:05:43] don't think we worry too much about
[01:05:45] reprocessing the same thread but the
[01:05:48] downside might be if somebody decides to
[01:05:50] spam our system then once they start
[01:05:53] sending threads and you know maybe they
[01:05:55] know we are pre-processing them for this
[01:05:56] or whatever so they just send like 20 30
[01:05:58] threads if you are processing them using
[01:06:01] post each and every thread will be
[01:06:03] processed but if you're using a put type
[01:06:06] of request then once they've done it
[01:06:09] then we kind of Might monitor the
[01:06:11] session although if it's let's say along
[01:06:12] the same request line then yeah you
[01:06:15] might yeah so you know we could have a
[01:06:17] conversation on that much you know you
[01:06:18] kind of see why depending on user
[01:06:20] Behavior the method might be worth
[01:06:22] talking about but other than that most
[01:06:24] of the content was perfect in fact I
[01:06:26] really really appreciated that you
[01:06:27] thought of the multi-level approach
[01:06:29] without prompting I've honestly not had
[01:06:31] anybody immediately think of that so
[01:06:34] you've done a good job with that like a
[01:06:36] photo value you're going to prevent them
[01:06:38] in terms of multiple labels and then
[01:06:41] yeah I think I break this down for you
[01:06:43] in order to like give a sense of the
[01:06:44] sequence of steps yeah for the most part
[01:06:47] you know oh I think we already touched
[01:06:49] on the precision versus trickle bit
[01:06:51] honestly I'm not going to agree on that
[01:06:53] because I know I struggled with that too
[01:06:55] so without a suggestion ahead you just
[01:06:57] use a computation Matrix that way you
[01:06:59] avoid having to talk of the terms
[01:07:00] themselves but that said it always looks
[01:07:03] good if you immediately talk about it
[01:07:06] without even defining it because it kind
[01:07:08] of gives that interview the illusion
[01:07:09] that I work with this Matrix regularly I
[01:07:12] know what they mean so I don't need to
[01:07:13] think too heavily about what they mean
[01:07:15] so you know just essentially just review
[01:07:18] the review the resources to kind of have
[01:07:20] a sense of what high Precision low
[01:07:23] Precision means and then maybe I forgot
[01:07:26] to mention this but this objective the
[01:07:28] objective function or the objective of
[01:07:30] the
[01:07:31] of the modeling all together it might be
[01:07:34] something we want to highlight in the
[01:07:36] initial stages but you know it's totally
[01:07:39] understandable to talk about it even at
[01:07:41] the end I felt like you know it gave the
[01:07:43] interview a more natural flow but at the
[01:07:45] end you know you want that optimization
[01:07:47] in terms of process so maybe try and
[01:07:50] touch on it right at the get-go that way
[01:07:52] you know it's not something that you
[01:07:54] might miss out on let's say the
[01:07:56] interview is kind of hard and like
[01:07:58] you're stuck with some steps you want to
[01:07:59] just knock it out of the way because
[01:08:00] it's easy to do and then keep going
[01:08:03] yeah yeah
[01:08:05] for sure but other than that as I said
[01:08:07] like
[01:08:08] I will give you a pass like I think you
[01:08:10] actually really really did a good job I
[01:08:12] could clearly pick up on the knowledge
[01:08:14] so if you have interviews tomorrow I
[01:08:16] honestly will become uh confidential do
[01:08:19] well it's more or less about refining
[01:08:20] the process so still putting a bit more
[01:08:23] work and like try and get the processes
[01:08:25] refined and uh final bit maybe spend a
[01:08:28] bit less time on the requirements but I
[01:08:30] was okay with this because I felt like
[01:08:32] you were talking about design as you
[01:08:34] went through it and that's why I think
[01:08:35] that was Timeless and but yeah in case
[01:08:38] the internet is proving to be a bit more
[01:08:39] technical just or a bit more
[01:08:42] crazy because you'll find some
[01:08:43] interviewers who are generally hard to
[01:08:44] work with just try and uh maybe 10 boxes
[01:08:48] out there to at most seven minutes or so
[01:08:50] okay all right cool you gotta make sure
[01:08:53] awesome
[01:08:54] all right any other questions anything
[01:08:56] else I can clarify
[01:08:58] uh nothing else today thank you so much
[01:09:01] absolutely I enjoyed this I hope you did
[01:09:03] too and it was nice talking to you yeah
[01:09:05] this was really great really uh
[01:09:07] appreciate taking your time today
[01:09:09] absolutely all right thank you all right
[01:09:12] thank you
[01:09:26] thank you

FEEDBACK_MD:
---
section: "Feedback from the interviewer"
start: "00:58:09"
end: "01:09:32"
start_seconds: 3489
end_seconds: 4172
---

know just to go through the feedback and mind you'll paste all of this in in addition to some extra resources you can look at at the end for the most part I agree with you but you know objectively communication excellent like you're really easy to communicate with easy to follow even throwing jokes on occasion in the interview which keeps it light-hearted so really really did well with that and then the line of questioning with respect to background processes I really really like that because most people fail to think about that they think they have to design Reddit in fact one of the biggest problem I've had with candidates is you ask them to detect how to design a harmful content protection process but they don't think about the background processes that exist so you started with that make it a point in any interview like nobody is asking to design the actual system they are designing a new system in exist in addition to the platform that's already there so feel free to denote exactly what you think already exists and maybe this is where one bit of improvement you can have here is actually detailing those bits so if we expect that let's say ready to give us apis that can extract text or alternatively if we expect that you have a push model where if a post is made a model automatically consumes that post or you know has that post uh pushed into let's say some message queue where we can consume it and process it it will be good to talk about it from that stage and in fact for most my most machine learning interviews I think that's probably the best Stage to start it just thinking about what's my input like what's the current platform giving me in terms of input of course yes it's not like a you know platform based system it could be different but typically data source is always the first stage but it was really really good to hear you actually talk about that because it shows that you had the intuition to think about that bit and then uh on line 85 I mentioned the pre-processing bit I felt as though you were not thinking about it until I pushed you in that direction and so okay right like you know I had to actually ask you okay how are you going to standardize this how are you going to pre-process it but once I asked you you went in depth on tokenization pre-processing removal of stopwatch it is key to think about that because part of the ml system design but sometimes you may find that that's the state that requires the most ml system design work because these are heavy processes like you can imagine uh you know when you have a bunch of images or even let's say videos where you have to do frame sampling then that's computationally intensive and it's usually what we're thinking about how that setup is going to look like what those features you know once you've extracted the features because this is basically the feature engineering part once you've extracted them where you're gonna store them because you know you don't want to process all of that and then all that data is basically output into some log file you want to actually think about the data output in that case talk about let's say readys or whatever you know data ta and storage solution you have where the model can consume from there in a quick manner so it might be what I was talking about API endpoints there maybe talk about them being marked by let's say I don't know ready for some other systems so that's stage one of the system design and then you know I give you a breakdown you can clearly see online 82 on how I typically do it it's kind of worked well for me maybe it can inspire you to curate a process for you so typically it's usually requirements pre-processing and then Define my apis both the input and output before I even jump into the model stuff and then I think we delve deep here yeah I actually made the point on that you went deep into it so I didn't really have any line of questioning on that so that was good so for the tokenization bit I think we kind of covered much of that conversation in the interview but Refresh on that that way at least you have a stronger sense of the intuition between of the implication or performance between shorter than the Lord so clearly that's probably the weakest point of the interview because I felt like we were going through like you know kind of like throw something at the wallet see if it sticks but for the most part it was good that you even knew of the different education strategies even went to a level of giving me examples which I could identify so I really appreciate that and then yeah like let's see I think this is the same point I've made there where pre-processing is always step one so it was good that we talked about that and then in terms of output I felt like you really you know once you were done with like the core apis the rest of the stages are perfect like it was like you talked about the output you expect in fact uh the funny thing when you said the API was okay to me it was like this is probably closer to what I would want to see in an interview where somebody actually gives me example payloads I always ask for example payloads most people won't give that so this was actually really really good so the only maybe you know there's a myths I would say maybe include the expected protocol for the for machine Learning System design I don't think I'll push anybody down to that uh you know up to that level but the reason why I might want to converse about that is sometimes it's worth thinking about let's say the concurrency or the number of requests I expect so if the API it is gonna it's gonna expect a lot of let's say get requests get requests tend to be more performance and let's say post requests so when you're talking about that especially in this case you know there will be a lot of text request coming in like as soon as the post is made that request is made so there should be a ton of them especially since the share volume is going to be a lot but most of the payloads will be tiny so in that case we probably want to have lightweight post requests in this case you know those maybe the downside might be since most uh most uh of the requests will correspond to a unique thread then maybe post my touch is that actually good is it supposed to put like in terms of method because I want to create a post is kind of a well like there's there's two ways to think about it's like rest and then there's just like Json or PC um so if you're thinking about it in terms of like rest a post request is more intend to create something and a put is like a update on the full entity people who like grpc is all post requests even if you want to get something um I see which one is the one that has bad impotency I think it's a post uh like in terms of like a session Aid and potential I can't remember which uh uh I mean I would assume like poets or I mean they're both supposed to be item potent I think uh it's it's uh um uh yeah I don't think it should matter like like for instance if you're doing a endpoint you want to post to like create the payment um but that's the item potent like if you try and call it twice um it needs to like have the same result today yeah actually I do believe put is actually item uh put his either important well post is not so and this is actually the key bit right there so if we made a put request especially since we know most requests will not be updating they'll be sending this one request to the process we're done and that's where maybe you can justify both because we you know I don't think we worry too much about reprocessing the same thread but the downside might be if somebody decides to spam our system then once they start sending threads and you know maybe they know we are pre-processing them for this or whatever so they just send like 20 30 threads if you are processing them using post each and every thread will be processed but if you're using a put type of request then once they've done it then we kind of Might monitor the session although if it's let's say along the same request line then yeah you might yeah so you know we could have a conversation on that much you know you kind of see why depending on user Behavior the method might be worth talking about but other than that most of the content was perfect in fact I really really appreciated that you thought of the multi-level approach without prompting I've honestly not had anybody immediately think of that so you've done a good job with that like a photo value you're going to prevent them in terms of multiple labels and then yeah I think I break this down for you in order to like give a sense of the sequence of steps yeah for the most part you know oh I think we already touched on the precision versus trickle bit honestly I'm not going to agree on that because I know I struggled with that too so without a suggestion ahead you just use a computation Matrix that way you avoid having to talk of the terms themselves but that said it always looks good if you immediately talk about it without even defining it because it kind of gives that interview the illusion that I work with this Matrix regularly I know what they mean so I don't need to think too heavily about what they mean so you know just essentially just review the review the resources to kind of have a sense of what high Precision low Precision means and then maybe I forgot to mention this but this objective the objective function or the objective of the of the modeling all together it might be something we want to highlight in the initial stages but you know it's totally understandable to talk about it even at the end I felt like you know it gave the interview a more natural flow but at the end you know you want that optimization in terms of process so maybe try and touch on it right at the get-go that way you know it's not something that you might miss out on let's say the interview is kind of hard and like you're stuck with some steps you want to just knock it out of the way because it's easy to do and then keep going yeah yeah for sure but other than that as I said like I will give you a pass like I think you actually really really did a good job I could clearly pick up on the knowledge so if you have interviews tomorrow I honestly will become uh confidential do well it's more or less about refining the process so still putting a bit more work and like try and get the processes refined and uh final bit maybe spend a bit less time on the requirements but I was okay with this because I felt like you were talking about design as you went through it and that's why I think that was Timeless and but yeah in case the internet is proving to be a bit more technical just or a bit more crazy because you'll find some interviewers who are generally hard to work with just try and uh maybe 10 boxes out there to at most seven minutes or so okay all right cool you gotta make sure awesome all right any other questions anything else I can clarify uh nothing else today thank you so much absolutely I enjoyed this I hope you did too and it was nice talking to you yeah this was really great really uh appreciate taking your time today absolutely all right thank you all right thank you thank you

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
Write JSON only to: splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.json \
    --video transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.json --out splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.qa-split.json \
    --video transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.validation-report.md

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
video.md: transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/video.md

--- CHAPTER `00:05:38` — Question Starts ---
window: 00:05:38 .. 00:07:35
recognition_status: single (1 items)

ITEM #6
  interviewer_question: time=00:06:45 text="would like you to do is think of how you will build out a system to essentially handle harmful content removal and by harmful content and feel free to add to this this is what you mean content related to abuse content related to nudity content related to what else uh violence oops misinformation this one is especially tricky since it's hard to know but you know yeah we can think of it as an extended goal we can discuss it once we have the rest done so that's kind of the synopsis of this feel free to take over just run me through how it's here to build this system assuming this watered down version of Reddit exists how you go by that"
  candidate_answer: time=00:07:33 text="um so I have a couple like questions in terms of uh uh the overall I guess like requirements Gathering um uh so I guess the first question is is like um how soon do we need to moderate content right like so somebody posts a picture um I guess like well I guess I guess even before this like is this a like reactionary system or is this a proactive system depending on the type of home well certainly like with nudity violence I think another one is called like or something like that um uh those are all things that we'd want to like take down immediately or sorry this would be proactive and then other pieces of content like uh I mean abuse is is going here as well um but like we would say for the reactive case perhaps like misinformation there's just a different thing here okay um and this is just posts and reactions to posts there's no comments or anything like that um and then uh I'm assuming there's like other pipelines that like when you you post something it's not like in terms of Reddit like the uh I guess like SLO for like uh post to feed time um is probably not on the order of like milliseconds it's probably on the order of seconds assumption here like are there other like background like data processing jobs that are actually going on in the system or will at least be the first of these"
  reference_answer: time=00:08:06 text="um that's some question so I would say maybe let's try get a hybrid where for some contents or specially categories of contents that are extremely harmful we basically react and for some other contents we can maybe take a day right so we we are open to different or variation in timing in this case excellent question so you can assume you have some background jobs let's say they'll also give you the freedom to Define what job you think will be convenient and if you think uh exposing the data that they're processing either in state or after okay okay um first async system okay cool ah let's see um let's get a sense of like like what are the number of like the volume of uh posts and reactions per day um so this is like Reddit right reddit's supposed to have like 50 million uh daily active users I don't know if they're uh posting 50 million videos a day um it's probably well like then we can just do sort of like a range estimate of like in the one to hundreds of Millions of uh posts and then just a clarification a post does that include comments so we don't care about comments um it probably revise this to be down a little bit maybe like to 50 million posts per day um including the all of the content that's in it um uh uh let's see do we have a question on"
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `00:07:35` — Requirements ---
window: 00:07:35 .. 00:10:19
recognition_status: not_recognized (0 items)

(no items extracted)
--- CHAPTER `00:10:19` — Volume estimates ---
window: 00:10:19 .. 00:14:07
recognition_status: multiple (2 items)

ITEM #7
  interviewer_question: time=00:11:27 text='that so when you say 50 million posts do you have a distribution in mind because uh you know given what you have on line six it will be good to think about how this is distributed right'
  candidate_answer: time=00:11:38 text="oh I see um yeah so given like so if there's 50 million posts then like if we're saying most of the texts are posts or sorry most of the posts are text only um if we add like like most meaning maybe 80 percent um if we say 80 or whoa okay 80 are texts only um this will leave us uh uh what would that actually be um I am not good at math right now 40 million to uh uh um million text posts per day with like a mix of image and video so like up to 10 million uh images and videos per day um"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #8
  interviewer_question: time=00:12:42 text="yeah do you in terms of videos in this regard are there any assumptions you're making with respect to what the size of the video is gonna be as well as what the input format is going to be so are you thinking somebody will upload an actual video or will they link a YouTube video a video video that's gonna be let's say rendered with an iframe in Reddit"
  candidate_answer: time=00:13:07 text="uh yeah so um good question my assumption is um uh that's true so so text can have links um uh so that'll be something to consider we'll need like a link detection uh deal here service um if the if there's a video I'm assuming the videos are direct uploads so we'll be able to like analyze them within our system um these are like directly attached um yeah because otherwise it's really hard to moderate if somebody's adding like a YouTube embed I mean one we assume that YouTube is doing their own moderation they're doing a good job and two like if there's a sketchy link then what we may want to do is actually like um uh cue this stuff up so I guess the next um question is like do we have some data sets around of existing content that is like labeled um or is there like um or like do we need a um labeling slash like uh manual review system so that mechanism uh from what I'm familiar with uh is basically like the way the mechanism is structured is uh they monitor the number of uh reports um if reports exceed some threshold a cue or manual review and then we get the labels there um so in terms of data set size and distribution can we assume that the training data that we have is um mirrors the uh like mirrors the population data set distribution um like like an assumption is maybe like images are more frequently moderated than text only and so like it could be the case that the data set has like 50 50 images 50 text whereas we're getting 80 tax from our like prod distribution I see so I'll yeah I think it's fair to assume that the rate of report should the size of the data set in this case especially since uh you know from my uh point of view any abuse is always going to be abuse so once it's in the database we can always reuse it in the future so to a degree it's kind of hard to argue that the distribution of data we have currently will be the distribution all the time but for now I think for Simplicity purposes I think that's a fair assumption to make at least for design purposes okay right yes in addition to that I was actually going to suggest might it might be worth thinking of dated risk ahead of time in this case because you know one year ago or two years ago even five years ago we remember images of the thing like you know it was a bigger deal but now with the age of tick tock now that's a bigger deal right people are looking at videos more often and this is why like I'm saying it might be hard to argue that the distribution will stay static but at the end of the day the data is always going to be the same it's always going to be abuse right yeah yeah and then and then uh another question is like what percentage um of posts are uh marked harmful so I'm assuming it's in like a one to two percent range kind of thing here um right um the last thing I think uh I wanted to cover here well I think I have enough in terms of like requirements um to kind of move forward here the like I know it's um in terms of like machine learning today like multi-modal is starting to really take over where you can just sort of give a machine learning model like I think Salesforce came out with instruct blip like two uh pretty recently and you can just like feed it um feed the model like kind of anything and it'll all figure out like um whether the model is uh or sorry it'll figure out like whether the the actual like content is uh something like abusive or violent or might be misinformation or something like that um the more like traditional way of setting it up is just having uh like kind of one model per um uh modality um and so like like that's the system I'm more familiar with but I like today if I were setting this up from scratch or even just like joining a company I'd really look at multimodal uh first to see if there are like wins there and then um but the system I'm proposing for the interviews and what I'm more familiar with which is just uh um unimodal right um"
  reference_answer: time=00:14:33 text="excellent question so online 31 I'll make reference to line four so feel free to make assumptions about having a human in the loop so we will actually have a continuous stream of uh some of the posts that will be labeled depending on the category so we do have humans in the loop and we actually do have a mechanism available for reports okay cool yeah so I see so I'll yeah I think it's fair to assume that the rate of report should the size of the data set in this case especially since uh you know from my uh point of view any abuse is always going to be abuse so once it's in the database we can always reuse it in the future so to a degree it's kind of hard to argue that the distribution of data we have currently will be the distribution all the time but for now I think for Simplicity purposes I think that's a fair assumption to make at least for design purposes okay right yes in addition to that I was actually going to suggest might it might be worth thinking of dated risk ahead of time in this case because you know one year ago or two years ago even five years ago we remember images of the thing like you know it was a bigger deal but now with the age of tick tock now that's a bigger deal right people are looking at videos more often and this is why like I'm saying it might be hard to argue that the distribution will stay static but at the end of the day the data is always going to be the same it's always going to be abuse right yeah yeah yeah and Reddit is crazy so yep that's a fair function maybe right it's like five percent I don't know yeah with that platform yeah three days a lot but yeah I agree yeah or like Twitter um yeah so uh uh I guess"
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `00:14:07` — Datasets ---
window: 00:14:07 .. 00:33:53
recognition_status: multiple (5 items)

ITEM #9
  interviewer_question: time=00:19:27 text="yeah so let's let's hear let's do this let's make the assumption that either we have an ensemble that essentially gives us a multi-modality functionality so you know it kind of marries the two ideas where you have one model that can do it all with all data types alternatively you know you can set spin out separate models in fact I would actually argue it might be worth going with your intuition here let's go with the traditional approach reason being we already made the assumption that there might be more images that are harmful so if we have one model yet most of our content is going to expect let's say images we might want to scale that up without reading we might want to scale the processor folder uh what do you call it other image images in this case while leaving the text on to stay content but that said before you know with all the model assumptions made I would like you to talk about pre-processing like given this data that we have is there any pre-processing steps you might want to make in order to make this data available because my assumption is regardless of the type of model we have we still have to process the different data types to make it ready for the model with the target standard input type right"
  candidate_answer: time=00:20:38 text="yeah so um uh there's a few pieces here in terms of pre-processing we can kind of split it up so for text cycling talks there's uh tokenization that you need to do uh I can't spell t-o tokenization um and so like uh basically it's the process of um what like an NLP used to do where you do uh like stemming removing stop words um and uh um trying to like clean up capitalizations fix misspellings and things like that like um it was like traditionally thing you do nowadays there's libraries that basically break words up into um well tokens and then uh creates kind of like a a sort of um I want to say it's it's yeah it just assigns like an ID to each of the the tokens and then that's sort of like the sequence of um uh like features that are fed into a NLP model I think like a popular one was a tick token uh by like uh that'll actually do the the tokenization of the text um and then for uh like images and video um some of the things that are really important uh for like pre-processing I think the first one is like making sure that the dimensions of the images are like correctly sized um because if there's uh images that are like bigger or smaller trying to um uh fit all those things into the model definitely will like cause some issues and so you want to like uh scale the image uh so I haven't worked with video much but I can say like for images you definitely want to like scale it um and then also like if we are working with a very low percent of harmful content sometimes it can help to up sample uh these these images by like doing things like adding a rotation um uh uh what's it called where you you change the um like Hue saturation brightness um there's a special I don't changing like hsl values so like brightening an image darkening an image um doing all that or like changing the contrast of the image um in terms of like pre-processing to kind of get more uh sample in there make sense"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #10
  interviewer_question: time=00:23:41 text="have two questions particularly here so and you know totally okay if you're not familiar with any of this but this is actually a very interesting point especially in the context of valid so when it comes to tokenization here there are multiple strategies we can use you know you don't have to cite any specific tokenization strategies but in terms of token size how long do you think each token should be and for reference engram is usually like you know intro World it can be two or three syllables yet you can also have bug Words which in that regard it looks like it looks at entire words in this case or you can even have multi-word tokenization strategies so it looks at samples of phrases or something like that and you know maybe looks at overlap so in terms of tokenization which strategy do you think will make most sense in our case and why"
  candidate_answer: time=00:24:34 text="huh um good question I think uh so like single I mean like a kind of like single word tokenization sort of seems to make I mean you can't like tokenize broccoli a word um I believe like there's something like you pick like eight characters and that should be enough to sort of Encompass most words and then some words get chunked into two uh tokens I think um uh that's that's at least like what I'm kind of familiar with in the space um uh I guess like what are the the trade-offs there uh I think there's a well there's definitely a trade-off between like the um uh the more unique tokens you uh sorry there's a plane [Music] I live next to the boring hitchq so trust me I hear that a lot yeah yeah um so I think I think there's a trade-off with the uh number of like token values that your um like vocabulary has so you have to be careful like if you only do one character you end up with like you know if you use ASCII like 256 values but I don't think the models are as good at being able to like pull out context on a like per character basis um now if you do like a bigger token size then then you'll have a lot more um unique values um so models will I mean think up to a certain extent models will do like pretty well um on attention it's just that now you're feeding in like a like larger um uh I guess like you kind of blow up the size of your embedding table uh a little bit so you have to kind of watch out the mem watch out for your memory of your system"
  reference_answer: time=None text=None
  interviewer_feedback: time=00:26:42 text="excellent that's exactly what I'll start getting right there and it's really really good that you brought in context because abuse is in context you know uh that is always have the same characters as praise so in that regard I think you're right I think I would also lean towards a single one probably towards multiple words token Aviation especially since you know nowadays a lot of abuse will lean towards three four words like people will combine multiple ones a single one that is you know sometimes abusive might not necessarily be abusive if I let's say I'm describing the word stupid in itself it might not be abusive but yeah you're calling a person abuse are stupid then that is actually instant insult so I think multi-word tokenization you can also justify a single one tokenization in that regard and then this yeah that was something"
  question_topic: Statistics

ITEM #11
  interviewer_question: time=00:27:36 text="maybe I might question it a bit because if we have let's say single word or multi-word tokenization then to a degree we are reducing the total cardinality of the total number of tokens DNA returned from any particular text input which could actually end up helping the performance compared to let's say doing an engram tokenization where we're looking at individual characters so do you think let's say this approach would actually end up meaning something in terms of path like I would say intuition on that"
  candidate_answer: time=00:28:05 text="um somebody okay so so basically just to to re-reiterate what you just said the idea is like as you choose like a larger like a multi-wad like token that that should result in an increase in the number of um uh what do you call it it's like a decrease in the sequence length but also an increase in the kind of like embedding table size right um uh so I guess like in terms of performance um I'm not actually 100 sure on one what would actually end up uh causing the most issues I think like my feeling is that at training time um having like a larger embedding table can uh be more memory intensive but at inference time your uh context like the sequence link that you actually need um should be like shorter and so the inference should be um quicker because you're just doing less like matrix multiplication at inference time um that's that's my intuition on it I think"
  reference_answer: time=None text=None
  interviewer_feedback: time=00:29:26 text="that's a that kind of confuses me though because technically with the reduced number of token sizes or at least the radius number of tokens we should technically also have a reduced embedding table size because each of the yeah right because the size of the embeddings themselves yeah the number of embedding should stay roughly the same the size of the embeddings is what will vary right right yeah yeah yeah"
  question_topic: ML

ITEM #12
  interviewer_question: time=00:29:54 text="a bit further in terms of capacity do you think there are any implications with let's say a multi-word tokenization compared to let's say uh engram tokenization"
  candidate_answer: time=00:30:07 text="um in terms of sparsity uh yeah like uh I mean so I I guess like with with this is just a guess because I I don't actually uh know but I'm guessing like there's a um uh I'm guessing with like engrams there's probably a higher sparsity of tokenization um hello Lucia hello foreign hello [Music]"
  reference_answer: time=00:31:45 text="oh I don't know what happened there yeah sorry I was saying you are right your intuition is very correct on that because objectively if we have engrams we have a huge embedding table because there are too many unique bodies and so for it to make sense you have to have huge embeddings in this case probably more than 10 30 36. so in that regard most of the values of the zeros and so we lined up with too many zeros and two little information but with multi-word tokenization small embeddings which will mostly have values because in this case essentially with all n is the same size of input we have fewer boxes to eat and so not only will they be more useful because they encapsulate context too and so it also ends up helping the performance in that regard but anyway sorry we spent a bit too much time on that so I think we can move on in this regard let's maybe talk"
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #13
  interviewer_question: time=00:32:37 text='about the API so given what we have here talk to me about some apis we might want to design in order to solve this data uh yeah so'
  candidate_answer: time=00:32:48 text="um uh let's see um so I could see like a few different uh systems here I mean so the idea is that we kind of said we're going to do um uh single modal um uh inference and um inference in this case it could be done uh as like a a batch inference or online um to me they kind of like both uh work um because talking with an async process um but also like the this data is kind of coming in as a stream so like uh to me I think it's just um like easier to kind of uh model it as an online uh inference system in just sort of like a little more future proof if you do need it to be more real-time it will still be there you don't have to migrate from batch to real time um so like there's basically going to be three services uh one for image one for text and one for video um so maybe it's like moderate um seek and say service dot moderate and then uh the request um should be like post requests and if we're thinking about like what kind of data we want for the body um uh so we should have like features and then we'll uh pass in a list of features [Music] um the I guess like should the I mean the services should be doing the same pre-processing that we're doing to uh generate the data and and train the model with it um so uh I think like these features I mean in in reality the way this would kind of work is that you use like feature IDs and then sort of work through some kind of a feature store um so this is actually something I didn't cover but I feel like we we should talk about is um uh it's not just um image text and video but also like user profiles might also be something that we want to like consider at least in the the future so it's not just like show me an image it's like show me um an image by a like particular user and then maybe that helps with identifying um things like misinformation like if a if there's a post and that user has been reported a number of times maybe that actually like positively impact um but maybe that's like a I'm like sorry I'm kind of thinking out loud here I'm a little disorganized I think um I think having the three services here and then another service a fourth one for just uh text misinformation that makes sense these are a lot easier to um moderate and then uh with misinformation it's a little more subjective and uh the model may end up having features in it that the text model uh uh doesn't need to include so that's why I'm kind of like uh building this out as a separate service here um so for uh this API um you'll pass in a a list of features maybe it's as simple as just saying like a dictionary and then we can say the text for text right um One Two Three or or um uh same with images it'd just be the blob or video um uh so the blob and the bite and then the same thing with the video right so that's just the the kind of the Epi there uh and then the response is going to be a list of um uh labels and uh confidences so uh you'd say like results and then so we'll have like a label and then so we may want to say like this is like the abuse label and then we can give a like a confidence uh and then this will be a float between zero and one so this could be like um and then like we can have other labels here as well so we'd have like labels for nudity violence um and then um yeah please these would be like the labels yeah um so that's basically the uh the apis of the service um in terms of like uh there's a few important things here um uh which is like as a system as a whole there are uh well the thing I want to touch on is like there's training metrics and then there's online metrics and like how are we doing um uh so for things like online metrics uh like actual production metrics we want to cover things like the number of um we call it harmful uh uh oops we'll call it harmful impressions um and so that's just the number of people that have seen these things uh and then like number of reports nice nice and uh uh maybe even um uh so there's um Impressions and then also maybe like a time-based one so like uh average time um to take down so when we when something is like posted reactively and we need to take it down we want to be able to take it down quicker and hopefully models will facilitate that that take down time um in terms of actual like uh training metrics uh some of the things that um we want to like consider here so when we're training on image text or video we're doing a um a multi-class classification um which means that we'll be doing a uh orals that are mixed up all the time it's um oh sorry um yeah yeah so uh we care about uh uh and recall um and so Precision is basically the uh number of uh true positives divided by um the two positives plus the false positives and the recall is two positive is divided by negatives in terms of like uh how we want to actually like present this I think just presenting in terms of precision and recall like you don't have to do an F1 score or like a receiver or operator curve just leaving his Precision recall works"
  reference_answer: time=None text=None
  interviewer_feedback: time=00:38:17 text='yeah'
  question_topic: ML

--- CHAPTER `00:33:53` — Services ---
window: 00:33:53 .. 00:42:20
recognition_status: not_recognized (0 items)

(no items extracted)
--- CHAPTER `00:42:20` — Objective of the model ---
window: 00:42:20 .. 00:54:48
recognition_status: multiple (5 items)

ITEM #14
  interviewer_question: time=00:42:20 text="sorry quick question objectively speaking because uh given this metrics these training metrics are there can you define to me the objective of the model and yeah um so that there's you're talking about like the loss function and not necessarily the most function we can speak on that later given we have a multi-classification problem here but I'm interested in what is the goal like do you want to minimize Precision while maximizing recoil or do you want to maximize both like what's the goals particularly"
  candidate_answer: time=00:42:52 text="yeah so I think um uh so this is actually interesting because like it depends on the business um objectives and time so I've actually seen that at my company where um we basically said like for a while we were okay with businesses um we were okay with uh um being very strict in terms of of I want to say like false negatives and then economic downturn kind of happened and then we kind of said like hey we don't we don't want to be um uh we want less false positives because we want people to actually spend on our um platform and so we were actually willing to trade off like recall I think back for precision um or by any other way but like business metrics but if you're if you're trying to um juice engagement then uh you want to be careful with um uh I think it's okay so false negative in this case would be um classifying something as harmful when it's not and so um uh if you're trying to like juice engagement metrics having a very um uh High precision and low recall is good um because if you have high Precision low recall what we're basically saying is we're trying to um we're okay with like harmful content making it half the model uh because we don't want to block like good content so in this case essentially what you're saying is we are okay rather than being less sensitive and as missing on actual abuse contents like it's okay if they report something and they find out it's not harmful and restore it rather than the opposite way they failed reports or we fail to plug and excellent so we're basically making our thresholds very low forward abuse or or a flag for abuse"
  reference_answer: time=None text=None
  interviewer_feedback: time=00:45:01 text="saying is we are okay rather than being less sensitive and as missing on actual abuse contents like it's okay if they report something and they find out it's not harmful and restore it rather than the opposite way they failed reports or we fail to plug and excellent so we're basically making our thresholds very low forward abuse or or a flag for abuse but tell me of course we have the human in the loop so we'll always have a restoration process but those who did that yeah I think that's an excellent approach and I was actually very happy with that because I was gonna Grill you after that on that point like would you want it to be you know the opposite and why but I think you immediately went to it which was accident yeah and then yeah"
  question_topic: Statistics

ITEM #15
  interviewer_question: time=00:47:16 text="now that we have our objective function uh our objective in this case can you talk to me about the loss function like if you're going to choose a loss function here for your model like this is the most technical I'll get to the model but uh what loss function do you think would make most yeah so um"
  candidate_answer: time=00:47:33 text="the loss function is uh uh oh I'm blinking so it's a multi-class classification uh and I know that you apply well you're supposed to apply a soft Max at the the very end and then what you do is you compute well you compute the loss the loss is um uh in this case my um the only one I'm thinking of is well there's there's two um like mean squared error or like maximum likelihood um uh I mean I think like maximum likelihood sounds like it'd be the right right loss function um but I'm gonna have a hard time with this section because I uh uh definitely need to study up on my loss functions"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #16
  interviewer_question: time=00:48:48 text='all right are you familiar with cross entropy oh um'
  candidate_answer: time=00:48:54 text="familiar with cross entropy I think uh it's oh I mean I know the word I don't know what it represents at the moment"
  reference_answer: time=00:49:04 text="yeah so the reason I brought up I brought that up is because at least from my understanding it's been a while since I had to but I remember it as a way of estimating my my parameters for my model sorry tuning the parameters but the loss functions we tend to be things like cross entropy it could be you know there's binary cross entropy when you have two labels or multi-level cross entropy when you have multiple levels uh the things like hinge loss maybe focal loss and a couple of other examples I cannot think of all of them off of the top of my head but honestly and this is the you know a quick tip cross entropy will almost always be a good answer when you asked about the loss function the only difference might be you need to showcase the intuition on the variant so things like multi-level or binary as well as understanding how it penalizes false predictions now the downside to it though is it's excellent for supervised problems where we have labeled input in our case that would work well but for unsupervised problems that becomes a bit of a problem and this is where I think of let's say pre-clustering in order to get a sense of uh let's say some sense of labels that might actually be helpful"
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #17
  interviewer_question: time=00:50:32 text="talk to me about deployment so say we've set this up uh how are you thinking of let's say scaling the system up uh it may be and like are you gonna have like a multi-service architecture or like a monolith like water intuition"
  candidate_answer: time=00:50:47 text="um yeah so uh there's a few things here the the first like point is um you know uh my my initial launch I'd want the models to be small enough to fit on a single like GPU for inference because if I had to do like a distributed GPU thing uh that just adds uh more complexity to the system um uh so like single GPU inference that'd be nice um and uh um you know we basically put a load balancer in front of a number of these uh instances I think each of the major Frameworks has like their own serving framework so like a pytorch and tensorflow have their own like serving infrastructure so I would just run it on uh top of that um and uh um yeah I mean like in terms of like doing uh a couple things that are important I'd want to make sure that um I'm logging all of the features at request time um one thing I want to do to make sure I minimize the amount of potential data leakage that's happening um in terms of like rolling that data out into the new data set and then also uh we want some like uh um metrics and monitoring uh to watch for data set distribution shifts so things like anomal infections to figure out like hey are we getting a bunch of nulls or a particular um uh feature like in this case it's text images and videos but if we're doing um something with like uh misinformation where we care about the user profile like you do care about that kind of like data distribution shift um and also like you want to look for your label shifts too like there could just be like all of a sudden one day everyone's posting a bunch of crypto nonsense and like you're predicting a lot more uh um like abuse on the platform that day so you do need to be able to alert say like hey our models um are kind of going off the rails here um the system that I would actually set up okay so there's there's scaling scaling I would just do a load balancer with a cluster of machines as CPU or GPU I guess utilization uh reaches a threshold add more um clusters to the machine and auto scale the the thing I would I would want to do though is on any new model rollout to do an AP study um just to see how the models performing online versus the existing Baseline uh before just blindly deploying it out to production doesn't really make sense and you know just a quick point on in addition to what you've just mentioned there are also other benefits to think about given that our service you know and maybe you should have clarified this initially ought to be global abuse in the US might not necessarily be abused in some other place and in similar regard we have inputs that might be different that might completely distort the model like you know we want to stratify the models by geographic features like language like you know what might happen in China versus what might happen in Russia the languages are completely different the input you probably want different play or your approach here where we have many models or microservices essentially and distributing them depending on the data service that will end up being a very useful useful of these Papas too right yeah"
  reference_answer: time=None text=None
  interviewer_feedback: time=00:53:42 text="doesn't really make sense and you know just a quick point on in addition to what you've just mentioned there are also other benefits to think about given that our service you know and maybe you should have clarified this initially ought to be global abuse in the US might not necessarily be abused in some other place and in similar regard we have inputs that might be different that might completely distort the model like you know we want to stratify the models by geographic features like language like you know what might happen in China versus what might happen in Russia the languages are completely different the input you probably want different play or your approach here where we have many models or microservices essentially and distributing them depending on the data service that will end up being a very useful useful of these Papas too right yeah yeah having like original yeah"
  question_topic: ML

ITEM #18
  interviewer_question: time=00:54:44 text='but for context I never give feedback straight up I usually want to first get your intuition so looking back at the interview what do you think you did well and what do you think you could improve I think'
  candidate_answer: time=00:54:55 text="um I did all right with the initial part um the sort of like requirements Gathering uh I definitely need to go deeper well I got like stuck on the tokenization uh piece um so like I think there's just a little bit more focus on some of the machine learning aspects of things like you know what are some of the more like common like pre-processing Steps tokenization looking at like the different scalings and things like that like doing log Transformations when your data distribution isn't exactly uh gaussian things like that I need to just like Refresh on um uh I thought like the API endpoint part was fine um yeah like I don't know if there's anything like really glaring there um uh I mean ultimately I feel like you know I'm not sure I mean I called it out in the beginning which was like we really should be doing a multimodal system that's just like more intelligent I I have a feeling that that would actually perform better um but like um so I'm glad I called that out and then went with the system that I'm a little bit more familiar with it's like it actually likes each of these things um I'm not actually sure if it's like better to do it that way uh in a real interview or if it's like by going this way I'm giving the interviewer an opportunity to dig on like like let's talk about image related models let's talk about like text related models um versus like potentially um like if I'm saying let's build some like multimodal system and the interviewer doesn't know how to or isn't familiar with multimodal systems than like I'm not sure if they're getting signal so I'm not sure if that's like the right path to to take there um I did just like I need to just do better on my loss function stuff um and uh uh just kind of yeah didn't get that piece um and then uh I mean other than that like I think everything kind of um did all right so that's sort of how I I feel like there's some ups and downs um definitely not like the perfect interview"
  reference_answer: time=None text=None
  interviewer_feedback: time=00:57:30 text="here's the thing I rarely find a person who finds out for mentorship but then at the end I'm telling them I will probably give you a pass so you actually be pretty damn well so I still took it still took a ton of notes as I said uh so you know to start with keeping it short I frankly think you're almost there like uh it was to give you like feedback in case you want to sign up for more sessions you probably need at most five if not three three just to kind of refine the process because in terms of content you probably are one of the few people been able to keep up with the line of questioning I've asked which was excellent so you know just to go through the feedback and mind you'll paste all of this in in addition to some extra resources you can look at at the end for the most part I agree with you but you know objectively communication excellent like you're really easy to communicate with easy to follow even throwing jokes on occasion in the interview which keeps it light-hearted so really really did well with that and then the line of questioning with respect to background processes I really really like that because most people fail to think about that they think they have to design Reddit in fact one of the biggest problem I've had with candidates is you ask them to detect how to design a harmful content protection process but they don't think about the background processes that exist so you started with that make it a point in any interview like nobody is asking to design the actual system they are designing a new system in exist in addition to the platform that's already there so feel free to denote exactly what you think already exists and maybe this is where one bit of improvement you can have here is actually detailing those bits so if we expect that let's say ready to give us apis that can extract text or alternatively if we expect that you have a push model where if a post is made a model automatically consumes that post or you know has that post uh pushed into let's say some message queue where we can consume it and process it it will be good to talk about it from that stage and in fact for most my most machine learning interviews I think that's probably the best Stage to start it just thinking about what's my input like what's the current platform giving me in terms of input of course yes it's not like a you know platform based system it could be different but typically data source is always the first stage but it was really really good to hear you actually talk about that because it shows that you had the intuition to think about that bit and then uh on line 85 I mentioned the pre-processing bit I felt as though you were not thinking about it until I pushed you in that direction and so okay right like you know I had to actually ask you okay how are you going to standardize this how are you going to pre-process it but once I asked you you went in depth on tokenization pre-processing removal of stopwatch it is key to think about that because part of the ml system design but sometimes you may find that that's the state that requires the most ml system design work because these are heavy processes like you can imagine uh you know when you have a bunch of images or even let's say videos where you have to do frame sampling then that's computationally intensive and it's usually what we're thinking about how that setup is going to look like what those features you know once you've extracted the features because this is basically the feature engineering part once you've extracted them where you're gonna store them because you know you don't want to process all of that and then all that data is basically output into some log file you want to actually think about the data output in that case talk about let's say readys or whatever you know data ta and storage solution you have where the model can consume from there in a quick manner so it might be what I was talking about API endpoints there maybe talk about them being marked by let's say I don't know ready for some other systems so that's stage one of the system design and then you know I give you a breakdown you can clearly see online 82 on how I typically do it it's kind of worked well for me maybe it can inspire you to curate a process for you so typically it's usually requirements pre-processing and then Define my apis both the input and output before I even jump into the model stuff and then I think we delve deep here yeah I actually made the point on that you went deep into it so I didn't really have any line of questioning on that so that was good so for the tokenization bit I think we kind of covered much of that conversation in the interview but Refresh on that that way at least you have a stronger sense of the intuition between of the implication or performance between shorter than the Lord so clearly that's probably the weakest point of the interview because I felt like we were going through like you know kind of like throw something at the wallet see if it sticks but for the most part it was good that you even knew of the different education strategies even went to a level of giving me examples which I could identify so I really appreciate that and then yeah like let's see I think this is the same point I've made there where pre-processing is always step one so it was good that we talked about that and then in terms of output I felt like you really you know once you were done with like the core apis the rest of the stages are perfect like it was like you talked about the output you expect in fact uh the funny thing when you said the API was okay to me it was like this is probably closer to what I would want to see in an interview where somebody actually gives me example payloads I always ask for example payloads most people won't give that so this was actually really really good so the only maybe you know there's a myths I would say maybe include the expected protocol for the for machine Learning System design I don't think I'll push anybody down to that uh you know up to that level but the reason why I might want to converse about that is sometimes it's worth thinking about let's say the concurrency or the number of requests I expect so if the API it is gonna it's gonna expect a lot of let's say get requests get requests tend to be more performance and let's say post requests so when you're talking about that especially in this case you know there will be a lot of text request coming in like as soon as the post is made that request is made so there should be a ton of them especially since the share volume is going to be a lot but most of the payloads will be tiny so in that case we probably want to have lightweight post requests in this case you know those maybe the downside might be since most uh most uh of the requests will correspond to a unique thread then maybe post my touch is that actually good is it supposed to put like in terms of method because I want to create a post is kind of a well like there's there's two ways to think about it's like rest and then there's just like Json or PC um so if you're thinking about it in terms of like rest a post request is more intend to create something and a put is like a update on the full entity people who like grpc is all post requests even if you want to get something um I see which one is the one that has bad impotency I think it's a post uh like in terms of like a session Aid and potential I can't remember which uh uh I mean I would assume like poets or I mean they're both supposed to be item potent I think uh it's it's uh um uh yeah I don't think it should matter like like for instance if you're doing a endpoint you want to post to like create the payment um but that's the item potent like if you try and call it twice um it needs to like have the same result today yeah actually I do believe put is actually item uh put his either important well post is not so and this is actually the key bit right there so if we made a put request especially since we know most requests will not be updating they'll be sending this one request to the process we're done and that's where maybe you can justify both because we you know I don't think we worry too much about reprocessing the same thread but the downside might be if somebody decides to spam our system then once they start sending threads and you know maybe they know we are pre-processing them for this or whatever so they just send like 20 30 threads if you are processing them using post each and every thread will be processed but if you're using a put type of request then once they've done it then we kind of Might monitor the session although if it's let's say along the same request line then yeah you might yeah so you know we could have a conversation on that much you know you kind of see why depending on user Behavior the method might be worth talking about but other than that most of the content was perfect in fact I really really appreciated that you thought of the multi-level approach without prompting I've honestly not had anybody immediately think of that so you've done a good job with that like a photo value you're going to prevent them in terms of multiple labels and then yeah I think I break this down for you in order to like give a sense of the sequence of steps yeah for the most part you know oh I think we already touched on the precision versus trickle bit honestly I'm not going to agree on that because I know I struggled with that too so without a suggestion ahead you just use a computation Matrix that way you avoid having to talk of the terms themselves but that said it always looks good if you immediately talk about it without even defining it because it kind of gives that interview the illusion that I work with this Matrix regularly I know what they mean so I don't need to think too heavily about what they mean so you know just essentially just review the review the resources to kind of have a sense of what high Precision low Precision means and then maybe I forgot to mention this but this objective the objective function or the objective of the of the modeling all together it might be something we want to highlight in the initial stages but you know it's totally understandable to talk about it even at the end I felt like you know it gave the interview a more natural flow but at the end you know you want that optimization in terms of process so maybe try and touch on it right at the get-go that way you know it's not something that you might miss out on let's say the interview is kind of hard and like you're stuck with some steps you want to just knock it out of the way because it's easy to do and then keep going yeah yeah for sure but other than that as I said"
  question_topic: Communication

--- CHAPTER `00:54:48` — How did the interviewee feel about their performance ---
window: 00:54:48 .. конец
recognition_status: single (1 items)

ITEM #19
  interviewer_question: time=01:08:54 text='all right any other questions anything else I can clarify'
  candidate_answer: time=01:08:58 text='uh nothing else today thank you so much'
  reference_answer: time=None text=None
  interviewer_feedback: time=01:09:01 text='absolutely I enjoyed this I hope you did too and it was nice talking to you yeah this was really great really uh appreciate taking your time today absolutely all right thank you all right'
  question_topic: Communication

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19/ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
