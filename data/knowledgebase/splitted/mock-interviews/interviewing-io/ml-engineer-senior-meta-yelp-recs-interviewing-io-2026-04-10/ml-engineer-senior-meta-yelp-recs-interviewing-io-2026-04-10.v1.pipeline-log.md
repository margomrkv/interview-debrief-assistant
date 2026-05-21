<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10",
  "transcript_folder": "transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10",
  "source_id": "ml_engineer_senior_meta_yelp_recs_interviewing_io_2026_04_10",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:18:06 +0200",
  "updated_at": "2026-05-20 21:31:28 +0200",
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
    "json": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/timecodes.txt",
        "en",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.pipeline-log.md"
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
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 2.0,
      "notes": null,
      "finished_at": "2026-05-20 21:31:28 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:31:28 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10`
- **Source ID:** `ml_engineer_senior_meta_yelp_recs_interviewing_io_2026_04_10`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:18:06 +0200
- **Last updated:** 2026-05-20 21:31:28 +0200

Фильтр в IDE: `*ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/timecodes.txt`<br>`en`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.pipeline-log.md` | — | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.xlsx` | 2.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.validation-report.md` | 1.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.pipeline-log.md`

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
SOURCE_ID: ml_engineer_senior_meta_yelp_recs_interviewing_io_2026_04_10
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10
INTERVIEW_LANGUAGE: en
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:08] Hello.
[00:09] Hello, can you hear me?
[00:11] Yes, I can.
[00:12] Okay, awesome.
[00:14] So, let me quickly introduce myself. And
[00:18] then I will follow up with some
[00:19] questions I have about yourself.
[00:22] So, my name is
[00:23] I'm currently working as a staff ML
[00:25] engineer at Meta. I have been with Meta
[00:27] for almost 3 years now. And before that,
[00:29] I used to work for Amazon, Microsoft,
[00:32] and also for Samsung. So, I have in
[00:34] total 12 years worth of experience.
[00:37] So, be And so far in my career, I have
[00:40] conducted like north to 400 interviews,
[00:44] like a mix of system design, ML system
[00:46] design, coding, and behavioral.
[00:49] So, before we get started, may I know
[00:51] like
[00:54] why you're actually doing that
[00:56] this ML system design? Do you have like
[00:58] an upcoming interview? And also, what is
[01:00] a little bit of your background? How
[01:02] many years worth of experience do you
[01:03] have?
[01:04] Sure. Yeah, I have a upcoming ML system
[01:07] design on Wednesday.
[01:09] Um might be something related to Reels
[01:13] ranking or something.
[01:14] Um and
[01:18] I working on like Reels ranking.
[01:20] Something like that.
[01:22] Yeah, so.
[01:23] Okay,
[01:25] and then I've worked so I started
[01:27] working
[01:28] um on like ML engineering
[01:31] uh about 4 years ago, but I was mostly
[01:34] focusing on feature engineering and also
[01:38] creating like the feature store at a
[01:40] startup.
[01:41] And then I worked in industry
[01:44] um on forecast training infrastructure
[01:49] for a year and a half, and then um ads
[01:53] uh like relevance models like for a
[01:56] search term and an item is the item
[01:57] relevant to the search term
[01:59] out of a catalog of items.
[02:01] And building out some of like the
[02:02] simulation infrastructure. So, focusing
[02:04] more on like the like the kind of the
[02:06] back end side rather than like the
[02:08] modeling directly, although I you know,
[02:10] do have some experience with doing
[02:12] modeling from school.
[02:14] Um and I've gotten like involved in it
[02:16] in some of my jobs. And then
[02:18] I I took a break to do some
[02:20] interpretability research for
[02:23] a few months last year um to kind of get
[02:25] my feet wet on a more like cutting edge
[02:28] problem, although it wasn't quite so
[02:30] applied to like industry setting. So,
[02:32] that's why now I'm looking to move more
[02:35] back into like a
[02:37] Rexis uh industry applied modeling role.
[02:42] >> [snorts]
[02:42] >> Okay, I see. So, you're looking for
[02:44] switching back in a
[02:46] MLE type of role, let's say.
[02:49] Yes.
[02:50] Okay, I see. And you have like an
[02:52] upcoming interview with
[02:54] For what is the position that you're
[02:56] actually targeting?
[02:58] Um it's like software engineer {comma}
[03:00] machine learning.
[03:02] Yeah, but what level?
[03:08] So, for a senior position. How many
[03:09] years worth of experience do you have in
[03:10] total?
[03:11] Well, I started working in 2017.
[03:15] Um
[03:16] >> 2017.
[03:17] Yeah, but I took like a year off in the
[03:19] middle of it in total. So, like
[03:23] 5 minus 7, so like I'd let's say 7 years
[03:26] of experience.
[03:28] Yeah, the reason why I'm asking if you
[03:29] have close like to 8 years, then you are
[03:32] a little bit to be considered for a
[03:33] staff level position.
[03:35] That's why I was asking you that
[03:36] question. Okay, let me give you an
[03:39] overview of the loop.
[03:41] What you should expect on the upcoming
[03:43] loop with then we can switch over like
[03:45] to the mock ML system design.
[03:47] So, with the interview with you should
[03:49] expect to get like to have like two
[03:52] coding round. Usually, like you should
[03:54] expect like two medium lead code type of
[03:56] question on each round.
[03:57] And then you should have like an ML
[03:59] system design plus one behavioral.
[04:01] Now,
[04:02] the ML system design um it is actually
[04:06] the most important from a technical
[04:07] point of view because it's actually
[04:09] being used to determine your level.
[04:12] And then on the other side is the
[04:14] behavioral, it also determine your level
[04:16] from a behavioral point of view.
[04:18] So,
[04:19] those are kind of a let's say
[04:22] an overview of what you should expect on
[04:24] the loop.
[04:25] Now, switching from there, um let's fo-
[04:30] So,
[04:30] what's my key point there? Like the
[04:32] coding round that usually pass or fail,
[04:34] so they're not being considered for
[04:36] determining your level.
[04:38] But the the ML system design and the
[04:40] behavioral are the most important from a
[04:42] a leveling point of view.
[04:43] So, do prepare yourself also the
[04:45] behavioral as well because I have seen a
[04:47] lot of people recently get down level
[04:49] because of the behavior.
[04:50] Now,
[04:52] having said that, do you have any other
[04:54] question for me? Otherwise, we can start
[04:56] like with the mock ML system design.
[04:59] Um no, I I've read the the prep guide
[05:02] from them. So, I think I understand
[05:04] what's coming up. I'm ready to go.
[05:07] Okay, perfect. So, what we going to do,
[05:10] we're going to switch over like to the
[05:12] to the whiteboard. And then what I'm
[05:14] expecting from you is to lead the whole
[05:17] design because this for a senior
[05:18] position, you might ask some clarifying
[05:20] question, but I will leave the time and
[05:22] space for you to lead the whole design.
[05:25] And then I will interrupt you at around
[05:26] like uh 43 mark
[05:29] and in order like to switch over like to
[05:32] feedback. So, also keep an eye on the
[05:33] time. And I might just sit back and I
[05:38] will only jump in and interrupt you if I
[05:40] want to ask like a a question. But the
[05:42] expectation is for you to lead the whole
[05:44] design.
[05:46] Okay.
[05:48] Perfect. The reason being is that during
[05:50] like the interview, you're also being
[05:52] evaluated on how you handle ambiguity,
[05:55] how you make a reasonable assumption,
[05:56] and you move on, and you unblock
[05:58] yourself.
[05:59] So, what we're actually designing today
[06:01] is we're designing like the Yelp system,
[06:03] the recommendation algorithm behind the
[06:05] Yelp
[06:06] um
[06:08] system.
[06:11] Yelp recommendation system.
[06:14] Exactly.
[06:15] Yeah, okay.
[06:17] Um so, this is like on the homepage,
[06:21] like you open up Yelp for the first time
[06:24] it today, and then you see a list of
[06:27] recommended venues, like they could be
[06:29] restaurants or
[06:32] bars or like any like place on the map,
[06:35] basically.
[06:37] Exactly, that's correct.
[06:40] Got it.
[06:41] Um okay. And this is Is this just on the
[06:45] homepage? Are we thinking about the
[06:47] search system as well?
[06:50] Yeah, let's focus on the on the landing
[06:52] page.
[06:53] Just on the landing page. Okay, so a
[06:57] user will come onto the page
[06:59] and given everything we know about them,
[07:03] um what's in their immediate vicinity,
[07:07] um what's open, we think they're going
[07:09] to we will show them the
[07:11] uh places that we think they're most
[07:14] going to want to
[07:15] visit. So, what Yeah, so what would we
[07:17] consider
[07:19] um
[07:20] to be like the thing that we're trying
[07:21] to optimize here? I guess it would be
[07:24] whether somebody actually visits the
[07:27] place.
[07:29] Um like how does Yelp make money?
[07:33] Yeah, through bookings, let's say.
[07:37] Bookings?
[07:39] Yes.
[07:40] Okay. Okay, so so Yelp has a list of
[07:43] venues that have some either like a
[07:46] restaurant with a meal or like a laser
[07:48] tag place where you could sign up for an
[07:51] hour, but there's something
[07:53] uh where a user can convert for that
[07:55] venue.
[07:56] Uh and we want to
[07:59] like make sure like make that as like
[08:01] likely as possible that the user will
[08:03] convert whatever conversion means for
[08:06] the venue.
[08:08] Um
[08:09] I guess like do we get paid based on
[08:12] like if like you make a reservation
[08:14] for like I don't know,
[08:16] uh like $80 at a laser tag, like we get
[08:19] paid proportional to how big the the
[08:22] payment was for the reservation.
[08:25] Yeah.
[08:26] Yeah, okay. I'm just thinking like if,
[08:28] you know, we want them to click on
[08:30] anything at all and and convert or we
[08:32] want to like optimize for I guess we
[08:35] maybe going to let people
[08:37] um
[08:38] or like I should say that the venues uh
[08:41] list their own prices.
[08:43] Um but yeah, we probably would want
[08:46] people to It's probably like a balance
[08:47] here between we want people to click on
[08:50] expensive reservations that we get a
[08:53] higher um commission for. But then we
[08:56] also don't want to like only show
[08:57] expensive things and then the user
[08:59] doesn't click on anything. Um and we
[09:01] should have shown them something a
[09:02] little cheaper. So, there's like a bit
[09:03] of a balance there.
[09:04] Um okay.
[09:08] what else should I think about? Um
[09:11] um
[09:14] Okay, so yeah, like we assume that the
[09:16] all the places that they're going to see
[09:17] are open and you can make a a
[09:19] reservation that night or I guess like
[09:21] sometime in the next week
[09:23] for for the venue, right? Like it
[09:25] doesn't really matter when the
[09:26] reservation happens as long as it
[09:28] happens during the session. Like they
[09:29] make the reservation during the session,
[09:31] right?
[09:33] Yes.
[09:34] Yeah, okay.
[09:36] Um
[09:37] What Okay, let me think about So, okay,
[09:40] so
[09:41] um
[09:43] Let me think about what we're trying to
[09:45] Okay, I think I have a sense of what
[09:46] we're trying to do.
[09:47] Um
[09:49] and
[09:51] we we Yeah, we want to
[09:54] uh increase I guess the the the online
[09:57] metric that we care about. I'll start
[09:59] writing things down. Um
[10:01] online
[10:04] online metric is
[10:07] Well, yeah, so like we get Do we get
[10:10] like a Is it a fixed commission? Sorry,
[10:12] I may may should be clear. Is it a fixed
[10:13] commission per click? Or do we get paid
[10:16] You said we get paid proportionally. So,
[10:18] so I guess like um total like the
[10:23] uh
[10:25] I hear a a being Oh, did you disconnect?
[10:29] Hello?
[10:30] No, I can still hear you.
[10:32] Okay, cool. Cool, sorry. Um
[10:35] So, I guess what we're going to try to
[10:38] optimize for is
[10:41] um the like total revenue
[10:45] generated
[10:48] um across
[10:50] all
[10:51] sessions
[10:53] uh through conversion. Like that's
[10:56] that's really what we're trying to
[10:58] optimize for.
[11:00] Um
[11:01] And then I'll think about what what
[11:03] we're going to be tracking in training
[11:07] uh towards that goal. So,
[11:10] Okay, so the general I'll maybe I'll
[11:12] talk about first um like what the
[11:14] end-to-end flow is going to look like.
[11:16] Um first from like when the user opens
[11:18] up the app and sees something and then
[11:21] um we can we can dive into different
[11:23] parts and and explore how how those work
[11:26] and like leading up to the inference.
[11:27] So, uh inference time
[11:31] um
[11:32] user goes to their app and then they
[11:37] make a
[11:38] request for So, at a certain time, they
[11:42] they open up Yelp and they want to see
[11:43] like given where I'm at um
[11:47] and what time it is uh what are all the
[11:50] places that I might want to look at
[11:52] right now. Um and maybe other day make a
[11:55] reservation for for tonight or for for
[11:57] somewhere down the line. Doesn't really
[11:59] matter as long as the session ends with
[12:01] a conversion uh where
[12:03] we're successful.
[12:05] Um So, then when when Yelp gets that um
[12:11] user request for for the homepage then
[12:15] we go into some sort of index of I guess
[12:19] like all the um So, this is like the
[12:24] Yelp server.
[12:25] And then we have an index which contains
[12:29] every
[12:30] um Yeah, these are just primarily
[12:33] venues, not like the events themselves,
[12:35] right?
[12:41] Hello?
[12:42] Yeah.
[12:43] Yeah, okay, sorry.
[12:45] Um Right, so we have some sort of
[12:48] reverse index where we we know like
[12:52] where the location is, whether it's open
[12:55] um some basic things like that. I'll get
[12:57] into more things we know about the
[12:58] venues later. Um
[13:01] And then we
[13:04] we we get some sort of candidate set of
[13:07] of all the the potential venues that
[13:10] that are at least like within driving
[13:12] distance or or
[13:14] uh I guess I guess it doesn't have to be
[13:16] open right now, right? Because if we can
[13:18] make a reservation for like 5 days from
[13:21] now, then we don't have to really care
[13:24] if it's open at the moment that the user
[13:26] um goes to it. So, I think it's more
[13:27] important that we just see where the
[13:29] user is and find nearby places.
[13:33] Um and then
[13:35] the the index returns some candidates
[13:38] which we would then rank uh by some
[13:42] means. Uh and maybe just like something
[13:46] like a combination of
[13:49] like just clicking um clicking or
[13:51] converting. I'll think about that, how
[13:53] to balance between the two. Um And then
[13:57] we'll we'll serve up to the user
[13:58] whatever has the highest score. Maybe um
[14:03] if if we're optimizing for
[14:05] conversions, we could we could rank by
[14:07] that. Um but I guess given that that
[14:12] most people like that that the number of
[14:15] like the number of
[14:17] clicks across all views
[14:20] um
[14:21] is, you know, not that many. Like maybe
[14:23] like I don't know what the conversion
[14:24] may be like
[14:25] Well, if you're on the app, you're
[14:26] probably going to be looking at a few
[14:27] places.
[14:28] Um but like for all the items, maybe
[14:31] there's like a 10% chance that a given
[14:33] item gets clicked in a in a session. And
[14:36] then of those um that you convert is is
[14:40] like an even lower funnel. Um So, I
[14:43] would imagine that there'd be
[14:45] um like generally more like there'd be
[14:48] more positive labels in the click um
[14:53] like in the click data set and is it
[14:55] converted.
[14:56] So, maybe that would be make more sense
[14:58] as as like a primary filter. Maybe it
[15:00] could be like two stages depending on
[15:02] how large the um
[15:04] the candidate sets are.
[15:06] Of like first you could you could rank
[15:08] by is it going to get clicked?
[15:11] Um and then within those you could
[15:12] re-rank by like you once you once you
[15:15] cut to a cut-off of like the top I don't
[15:17] know, 50 most likely items to get
[15:18] clicked on, you could re-rank by the
[15:20] most like the the the likelihood that
[15:22] those would get a conversion. Um and
[15:25] then show the user from those uh 50
[15:29] re-ranked.
[15:31] So, okay, anyway, sorry. I'm I should
[15:33] finish the end-to-end first. So, yes,
[15:36] the reverse index um would then I don't
[15:39] know how to represent a model. Uh
[15:42] Let's let's just call it like
[15:44] um some sort of let's say
[15:49] PCTR
[15:50] model. Oops, sorry.
[15:53] Um
[15:56] Right, which which then
[15:59] um
[16:01] Well, let's let's say for now, even
[16:03] though ultimately we care about revenue,
[16:05] we we we start by just predicting
[16:08] clicks.
[16:09] Um So, yeah, that's that's the overall
[16:11] flow at
[16:12] inference time. Um
[16:15] of how that would work.
[16:17] And
[16:20] So, yeah, let's talk about what kind of
[16:24] uh data we have available um before we
[16:27] talk about yeah, what kind of model we
[16:29] would make based on that data.
[16:31] Yeah?
[16:33] Mhm.
[16:34] Okay.
[16:35] So,
[16:37] we have venues
[16:40] um and
[16:43] users
[16:45] and
[16:47] um
[16:50] I guess yeah, the way that
[16:52] a user's interact. So, so Yelp has
[16:56] Right, and then venues have different
[16:58] types of events. So, like a user
[17:02] who's going to bars is going to
[17:05] Yeah, I guess that's like a category of
[17:07] a a venue.
[17:10] Um All right, let me think of a few. So,
[17:11] there's there's like the
[17:14] free form text that describes
[17:16] it's or it's sorry, it's um
[17:19] it's name.
[17:20] Excuse me. Uh
[17:22] it's address.
[17:24] Um the owner's
[17:27] description.
[17:29] It has associated
[17:31] reviews across all things that people do
[17:34] in it. Um which are left by users,
[17:39] obviously. And
[17:41] uh we know the price of the uh
[17:48] whatever the the reservation.
[17:51] Um
[17:55] And then
[17:57] I'll just I'll just hop around a bit and
[17:58] I'll I'll jump back in if if I think of
[17:59] something else.
[18:01] So, a user and then like user
[18:05] um in a session.
[18:08] Just to make that clear that like this
[18:10] is what we know at inference time. Um
[18:12] So, we know
[18:14] what
[18:16] time it is that the user is browsing.
[18:19] The location that they're at. Um we know
[18:21] the history of past reservations.
[18:26] Um
[18:27] We know
[18:29] I guess like reviews
[18:32] that they've left.
[18:35] And
[18:37] Can you like
[18:39] Are you friends with other people on
[18:40] Yelp? Is there like I I guess that's not
[18:41] really a major feature of it, right? Is
[18:43] like the network of like where did your
[18:45] friends go out to, right?
[18:54] The social aspect I don't believe that
[18:56] it is part of Yelp.
[18:58] Yeah, I don't think so. Um okay.
[19:02] Um
[19:04] So, yeah, and then like we need some
[19:07] sort of I mean, I was
[19:09] Yeah, maybe like just a easier like
[19:12] predefined
[19:14] category instead of like just relying on
[19:16] this free form description. We give them
[19:18] certain categories that um like a
[19:21] taxonomy that they can fall into. We can
[19:23] maintain this taxonomy ourselves. The
[19:25] taxonomy could itself be like
[19:27] like some
[19:29] taxonomic classification. So, you could
[19:31] have like, you know, at a high level,
[19:33] nightlife. And then below that
[19:36] um
[19:37] uh like a bar versus a club versus a
[19:40] jazz venue. And those are like nested.
[19:43] And and then like yeah, you got a venue
[19:45] could have um multiple like levels of
[19:49] granularity of of classification there.
[19:52] Um
[19:54] Okay, so I think
[19:56] I think that's a that's enough to get
[19:59] started with.
[20:01] Uh or Okay, we also have our
[20:04] sessions.
[20:06] Um
[20:07] So, like historically, what is a what
[20:10] has happened on the app with regards to
[20:12] like what when a user
[20:14] um
[20:16] like saw a particular venue
[20:21] um and it was at this or
[20:25] Yeah, so a a a user so a So, a session
[20:28] is
[20:29] composed of
[20:31] a user
[20:33] looking at multiple venues at a certain
[20:36] like
[20:37] um position in
[20:39] the like like uh the results
[20:43] and then
[20:44] was
[20:47] clicked
[20:48] like did
[20:50] convert by the end of that session.
[20:53] Um which we should we should know that.
[20:57] Uh of like start time.
[21:01] Okay, so these are Oh,
[21:05] sorry.
[21:06] Um
[21:08] Right, so so that's that's what we know
[21:10] about what's what's happening. That's
[21:11] what we're trying to predict at at
[21:13] inference time.
[21:14] Um
[21:16] So,
[21:19] let me think more about
[21:22] um
[21:23] yeah, what what is the
[21:26] the the training objective that we're
[21:28] trying to optimize for. I guess
[21:30] um
[21:33] it might be like a combination
[21:36] of
[21:38] like
[21:39] did It's either we we could separately
[21:41] consider our success in predicting
[21:45] clicks and conversions or we could come
[21:48] up with like
[21:50] one overall
[21:52] uh metric that combines both of them.
[21:55] Um
[21:57] Hmm.
[21:58] >> [clears throat]
[22:00] >> Yeah, I guess I guess to keep it simple
[22:03] for now, I would
[22:06] rather just focus on predicting
[22:09] clicks
[22:10] and then
[22:12] I could think about how I would expand
[22:13] it to incorporate uh conversions as well
[22:17] later.
[22:19] Um
[22:21] Okay, so let me let me think about how
[22:25] to
[22:26] build like a um a training pipeline
[22:30] uh to to determine
[22:33] if someone's going to click on on a
[22:35] given results
[22:37] and then I'll Yeah, I'll think about
[22:39] um
[22:42] Yeah, we we don't really have to focus
[22:43] or maybe should I
[22:46] I
[22:48] Okay, I was thinking if I I need to
[22:49] worry about like building up the index
[22:51] properly um
[22:53] because
[22:55] like you know, like given given like uh
[22:57] a definition of the index that's going
[22:59] to determine what's even in or
[23:04] Sorry, am I am I like going to cold
[23:06] start this like from scratch or should I
[23:08] assume that a system already exists and
[23:11] I'm iterating on it?
[23:13] Cold start.
[23:14] Cold start. Okay.
[23:16] Got it.
[23:18] Um okay, so initially
[23:21] we're not going to have any sessions.
[23:23] We're not going to Right, all we're
[23:24] going to have is venues and users.
[23:26] So, initially we have to bootstrap this
[23:28] somehow um with with some heuristic
[23:31] metrics.
[23:32] So, I think before we get into like
[23:35] modeling anything
[23:37] um
[23:38] I would want to suggest that people
[23:42] visit popular
[23:43] uh venues in their area. So,
[23:47] um All right, so initially what kind of
[23:50] data So, okay, so so
[23:53] So, this is bootstrap So, this is like
[23:54] Yelp doesn't exist or Yelp is just a
[23:57] pure like database like you just search
[24:00] for things, but we don't like show
[24:02] anything on the homepage by default.
[24:09] We have a system that actually pilot is
[24:11] not an ML system though.
[24:14] We have a pilot system.
[24:16] Yeah, we have a simple rule-based
[24:18] system. We can ask Okay.
[24:20] We already have a simple rule-based
[24:21] system which is giving us some sessions
[24:24] where So, we we are giving
[24:26] uh people
[24:28] like things to possibly click on or
[24:30] convert to
[24:31] and we know whether they did or not. Um
[24:34] but yeah, those heuristics might be
[24:36] Yeah, things like
[24:38] uh I'm assuming
[24:40] um is it is it a popular venue in the
[24:42] area? Um does it have like a deal going
[24:46] on right now or good discount? I guess
[24:48] what I'm trying to say is there might be
[24:50] um like newer up-and-coming venues that
[24:54] aren't going like I don't know if if our
[24:56] old system has the ability to like
[25:00] balance exploring new venues versus
[25:02] exploiting ones and we have to come up
[25:04] with a way ourselves of of like randomly
[25:08] introducing like newer low PCTR
[25:13] uh items into people's feed just to get
[25:15] them out there and get information on
[25:17] whether people like them or not. Yeah?
[25:20] Hmm.
[25:21] Hmm.
[25:22] Make any reasonable assumption like you
[25:24] are designing the whole system so you
[25:26] have full power over any direction of
[25:29] the system.
[25:30] Okay.
[25:31] Right. So, yeah, so if I was Yeah, if I
[25:33] had the original system, then I would
[25:35] have
[25:37] some sort of basic uh yeah, like
[25:40] popularity metric and and I guess I
[25:43] don't know if we have like an ad system.
[25:45] Um or like based on like number of like
[25:49] good reviews, we do have that, right? Um
[25:53] which is a list
[25:54] of
[25:56] list of reviews and a review itself has
[25:58] like a
[25:59] numerical rating I guess out of five and
[26:03] and possibly
[26:06] photos and um
[26:09] and a text description of of the
[26:12] whatever, maybe like the event itself.
[26:15] Um text
[26:17] star rating out of five
[26:21] photo optional.
[26:23] Um
[26:26] and
[26:29] Okay.
[26:32] So,
[26:33] so yeah, let me let me think about how
[26:35] how I build a model which would um
[26:40] which would predict
[26:43] click given that Oh, the Yeah, as I said
[26:45] you
[26:46] even with the with the bootstrap model,
[26:47] it's going to be the case that most
[26:49] people like for the most part people
[26:50] aren't going to even click on a lot of
[26:53] the results. Um they're going to scroll
[26:55] through and then click on only a couple.
[26:57] So, there's going to be class imbalance
[26:59] that I'm going to have to address at
[27:01] some point.
[27:02] Um
[27:04] Maybe Yeah, and Yeah, given that I care
[27:07] a lot about um
[27:10] more about false
[27:13] Hmm, okay, so a false positive would be
[27:15] I show somebody something I think
[27:17] they're going to click on and they don't
[27:18] click on it.
[27:20] Okay.
[27:21] I mean, maybe they would think that I'm
[27:22] not really good at knowing what they
[27:23] like, but not a not a huge deal. If it's
[27:26] a false negative where there is
[27:27] something in my catalog that they could
[27:30] have clicked on, but I didn't show it to
[27:31] them, then that's potentially missed
[27:34] revenue. So, I guess I would
[27:36] And Yeah, and like given that clicking
[27:37] is a rarer thing, I would want to
[27:40] um maybe have a
[27:42] uh like a larger penalty for for missing
[27:47] uh like if the model predicts that they
[27:49] weren't going to click on it, but they
[27:51] actually would have, then that would
[27:52] that would incur a larger penalty than
[27:54] than the reverse.
[27:56] Um Okay, so
[27:59] Yeah, like
[28:00] for for setting up the training
[28:03] um
[28:04] system, I need to I need to create like
[28:05] a unified view of a user at a given
[28:08] point in time. Um I think it maybe
[28:11] should be
[28:12] Yeah, like pairwise. So, for for a user
[28:16] for a venue
[28:18] um predicts likely here that the user
[28:20] would have clicked on the venue
[28:22] um at the point of of browsing it in
[28:25] their search results. And then
[28:27] I guess
[28:28] Yeah, maybe some sort of offline metric
[28:30] that I would want to track would be if
[28:32] I'm just predicting like this this
[28:34] binary um label
[28:37] uh but it's it's showing up in a ranked
[28:39] list, then I'd want to use something
[28:41] like um discounted cumulative gain to
[28:45] uh assess like how well the the ranked
[28:49] results was um given that I like ran a
[28:53] simulation um and tried predicting the
[28:57] uh Yeah, the the likelihood of click for
[28:59] each item in the ranked list. All right,
[29:02] so
[29:03] I'll just add that offline
[29:06] metric
[29:08] and DCG for some n
[29:11] um posts at the top that that we care
[29:14] about
[29:15] uh for clicks, I guess.
[29:19] Um Okay, so
[29:22] so I think I'm going to Yeah, I'm going
[29:23] to build a
[29:24] a
[29:26] like Let me think. I guess I could start
[29:27] off by building a
[29:29] uh a vector that describes both the user
[29:33] and the
[29:34] um and the venue.
[29:38] And initially, to keep it very simple, I
[29:42] I could use some sort of linear model
[29:45] uh that that predicts,
[29:48] um,
[29:49] yeah, that that it
[29:51] produces a value between zero and one,
[29:54] uh, by feeding that through a sigmoid
[29:56] like a logistic regression, um, which
[29:58] predicts likelihood of click for a pair.
[30:01] And then we can think about making that
[30:03] more complicated, uh, if if we want to
[30:06] capture, uh, cross feature
[30:08] relationships. Um, but just to get
[30:10] something off the ground, I think I
[30:12] think logistic regression is is a fine
[30:14] start.
[30:15] Um, so yeah, let me think about what
[30:18] that would look like.
[30:20] Um,
[30:21] I think I'll just build up each each in
[30:24] uh, part of of this this vector at once
[30:28] or on on each side. So for a user,
[30:31] >> [snorts]
[30:31] >> um,
[30:33] yeah, I guess like given the time that
[30:36] they're browsing, if they're like
[30:37] looking for something to do right there
[30:39] and then, which I'm guessing is a lot of
[30:41] the time when you go on Yelp, it's not
[30:42] like just like plan out
[30:45] the the rest of your week, it's like I'm
[30:47] currently out somewhere and I want to
[30:48] find a place to go. That's probably the
[30:51] majority, I would imagine the majority
[30:53] use case. So, um,
[30:57] I want to have a sense of their,
[31:02] um,
[31:04] their city.
[31:05] So maybe like,
[31:06] yeah, so just the well, the city is
[31:09] already being used to do the filtering
[31:12] from the from the index like to to
[31:15] retrieve things that are close. Um,
[31:19] so maybe so I have user features,
[31:23] uh, venue features and user venue.
[31:27] Um,
[31:29] so I guess what I was trying to say is
[31:32] that
[31:33] um, like the the distance
[31:37] from a user to the venue could be
[31:40] something I'd want to use, but then
[31:42] that's very different in like Austin
[31:45] versus New York, right? Um,
[31:49] the like I you can drive in Austin, but
[31:52] you don't drive in New York. So then you
[31:53] could tend to go to you're willing to go
[31:54] further, relatively speaking, in Austin.
[31:57] Um,
[31:59] so I I guess maybe I I I'm just going to
[32:03] like throw something out here.
[32:05] Um, maybe like distance to venue
[32:10] divided by like something like city
[32:15] diameter. It's it's like a really rough,
[32:19] uh, ratio like like distance
[32:22] ratio.
[32:24] Um, just something to like normalize it,
[32:26] but I'd probably think about like
[32:28] whether it's like public transit or
[32:30] something.
[32:31] Um,
[32:33] and then
[32:35] uh,
[32:37] for the venue like is open
[32:41] as a bool, which mean yeah, again, we
[32:42] could we could still show venues that
[32:45] are closed. And obviously they're like
[32:47] when they're sending a
[32:50] Yeah, I'm not sure like there's like the
[32:52] balance between do I put this into the
[32:54] model or do I just like rely on the user
[32:58] doing the filtering themselves? Um, so
[33:01] they wouldn't even like see, let's say,
[33:05] um, venues that are closed if they're
[33:07] looking for something right this moment.
[33:09] Um, so I'll [clears throat] I'll think
[33:11] about whether doing cool like yeah, I
[33:13] think I'll just include everything by
[33:14] default. Um, but like I'll think about
[33:17] to do
[33:19] um, how to balance Maybe I shouldn't put
[33:22] it here, but uh,
[33:26] how to balance between
[33:28] uh, users doing filtering versus using
[33:33] uh, venue attributes in the model.
[33:39] Um, okay.
[33:41] And then
[33:43] So we have the address and then we have
[33:45] maybe like,
[33:47] um, average
[33:51] rating
[33:53] um,
[33:54] past
[33:56] month.
[33:58] Uh, sorry, did you disconnect for a sec?
[34:02] No, I'm still here. I'm still here.
[34:04] >> I I saw I see something on the on the
[34:07] Excalidraw that's like you reconnected.
[34:08] Anyway, so I'm thinking about, um, yes,
[34:12] I want to know if it's a good venue,
[34:16] but then this is going to potentially
[34:18] penalize
[34:20] new venues who don't have many ratings
[34:22] yet. Um, so maybe there's some way of
[34:26] like normalizing this by
[34:28] like the the the the ratings that the
[34:31] venues received based and then like the
[34:34] number of ratings.
[34:36] Um,
[34:38] yeah, I'm not sure how to formulate that
[34:40] right now, but I'll think about that.
[34:43] Um, how to consider low rate Maybe like
[34:47] you have some sort of like, um, for the
[34:50] city you have like, uh,
[34:54] prior under like a prior probability of
[34:56] like what the average rating is for
[34:59] different venues of different categories
[35:02] at at diff like at different points in
[35:03] the life cycle and then you like use
[35:06] that as like the baseline that you're
[35:08] normalizing it by.
[35:10] I don't know.
[35:11] Um,
[35:12] and then the
[35:16] um, yeah, we could have like embedding
[35:20] repre from the text of the, um, of the
[35:25] name plus
[35:27] the description, which I could describe,
[35:29] um, later if if we have time, how to
[35:32] generate that, but we could use
[35:34] something like various like take an
[35:36] off-the-shelf just concatenate them
[35:37] together and then, uh, put it through an
[35:41] off-the-shelf BERT type model. Um, and
[35:44] that would give us an embedding to
[35:45] compare venues.
[35:47] And
[35:49] and yeah, again, we like even if it's in
[35:50] logistic regression, it doesn't matter.
[35:52] Like you can just, um, have each of
[35:54] these embedding dimensions as a separate
[35:57] coefficient.
[35:58] And you could have the
[36:01] taxonomy,
[36:03] um, as a categorical,
[36:06] um,
[36:08] one hot.
[36:10] Maybe like keep the category simple if
[36:12] the taxonomy simple and just use like
[36:13] the top level taxonomy.
[36:15] And then
[36:17] for a user,
[36:20] um, you could do something like
[36:25] >> [snorts]
[36:25] >> number
[36:26] of times
[36:29] uh, click We so we also know
[36:32] like well well, we know conversions.
[36:35] Like we know when people actually made
[36:36] reservations. So you could have like
[36:39] number of times clicked um, on
[36:45] yeah, let's say let's say venues of
[36:49] different So assuming that tax like for
[36:51] the top level taxonomy, um, we don't
[36:54] have that many categories. We have maybe
[36:56] like,
[36:58] I don't know, 15 or something. Like
[37:01] then it wouldn't be too bad to have a
[37:05] like one hot, um, features that were
[37:08] defined along
[37:10] like within that, um, set of values.
[37:12] Like number of times clicked on like
[37:17] taxonomy category
[37:20] one
[37:21] uh, last month. And then you can or like
[37:25] actually like basically I'm saying
[37:28] we you can have this like aggregated,
[37:31] um, feature which which describes like
[37:34] how often did they go to a bar or do
[37:36] they go to a restaurant that those of
[37:39] selling tacos or whatever, um, we choose
[37:43] for our top level taxonomies. And that
[37:45] should give us a good sense of what
[37:46] they're going to do next.
[37:48] Um,
[37:50] and then yeah, like maybe,
[37:52] um,
[37:53] some sort of uh, to like hour
[37:57] bucket. So like, you know, from zero to
[38:01] like 23 again as as like, um,
[38:05] as a one hot vector. Excuse me. Um, so
[38:08] to determine like when they're browsing
[38:10] that could affect what they want to
[38:11] click on.
[38:13] Um,
[38:14] okay. I I think I'll go a little deeper,
[38:16] but I I think
[38:18] this is
[38:19] pretty much the the basics of what I I
[38:23] would want to incorporate here. Um,
[38:25] given that we have we don't have much
[38:27] Well, so we also want to consider like
[38:30] people who
[38:31] tend to go to like So like a venue
[38:35] would have a certain type of person who
[38:38] goes to that venue, right? Like a jazz
[38:40] lover. So maybe I could think about like
[38:45] on the user-to-user side like like users
[38:49] who went to venues users who go to
[38:53] venues like the ones you go to,
[38:55] um,
[38:57] also go to venues like this one you
[39:00] haven't been to yet.
[39:01] Um, but that that's like a maybe like a
[39:03] later stage, um,
[39:07] interaction feature that, uh, is is
[39:09] worth incorporating, but just for the
[39:11] MVP for this initial iteration, we won't
[39:14] worry about it. But like,
[39:16] um,
[39:17] places that are like the ones that
[39:22] people similar to you go to.
[39:26] Um,
[39:28] and then yeah, maybe
[39:30] um,
[39:32] I guess this I'm not sure I'm not sure
[39:34] this is like a a model feature or this
[39:36] is like part of the
[39:38] index.
[39:39] Um,
[39:41] yeah, but you get it going the other way
[39:42] basically of of thinking about like of
[39:44] the places that the user has gone
[39:48] in the last month, what are
[39:54] venues that are similar to those places?
[39:59] Yeah, but I don't want to get too
[40:00] complicated right now before I've gotten
[40:02] the end-to-end system working for
[40:04] this set of features. So,
[40:08] I would build up a
[40:11] training set
[40:13] of examples of
[40:16] like from historical sessions
[40:19] hydrating the user and the venue
[40:23] with with these pieces of information
[40:28] then predicting
[40:32] or it would have the like did was
[40:37] clicked
[40:39] yeah as a bool
[40:41] and
[40:43] so how would I and I have to think about
[40:45] how I would
[40:47] split up this this data set into train
[40:49] validation and test.
[40:53] I think
[40:55] that I'd want to
[40:58] probably make sure that
[41:00] I don't leak user level data. So, I
[41:03] wouldn't want to have like data
[41:07] I would want to make sure that any users
[41:09] in the test set are not in the train or
[41:11] validation set. So, keep things separate
[41:13] like that.
[41:16] And then
[41:18] I probably would also want to consider
[41:21] that like
[41:23] what someone's done in the past is going
[41:26] to help me predict the future. So, I
[41:28] wouldn't want to have time leakage
[41:30] either
[41:33] with it within a user. So, I would
[41:34] probably
[41:38] want to consider
[41:42] like doing splits where like for some
[41:45] users I only consider
[41:49] like I I train on
[41:52] what like what their history was like
[41:54] what sessions from like 5 years ago and
[41:56] then I try to predict what they did
[42:00] well not sorry. I yeah I I only
[42:05] well
[42:07] sorry. I'm I'm I'm I'm not speaking very
[42:08] coherently.
[42:13] Okay, so I guess I guess within within
[42:15] this user stratified data set
[42:22] yeah I would I would want to
[42:26] let me let me let me
[42:29] stop you here in order to switch over to
[42:31] the feedback, but first I would like to
[42:33] hear from you. How did you find this
[42:35] question and what is your
[42:36] self-evaluation?
[42:40] All right, so I found well this is a
[42:42] good question.
[42:45] I found it
[42:46] a little
[42:48] difficult to know how to pace things
[42:51] out. I think I got bogged down with the
[42:53] features which is
[42:54] like a common thing that people get
[42:56] tripped up on
[42:59] and I maybe wasn't
[43:02] I should have like gone further into
[43:05] like quickly getting to
[43:07] having a model that predicts the basic
[43:09] thing and then getting it deployed and
[43:11] then describing how I would evaluate it
[43:14] online.
[43:16] I think I should have
[43:18] gone to that a little more quickly
[43:19] rather than
[43:21] going like listing out all the possible
[43:24] additional
[43:26] nuance features that I might want to
[43:28] have.
[43:31] So, my self-evaluation is
[43:34] maybe mid-level but probably not yet
[43:37] senior.
[43:40] Yeah, I will
[43:43] tend to agree on that
[43:45] and I want to share with you. I'm just
[43:47] going to share with you a link. You
[43:49] covered stuff like the stuff that you
[43:52] covered it was actually okay,
[43:55] but it needed a more holistic view of
[43:58] the whole system.
[44:00] That was the missing point here.
[44:03] Let me actually share a link. If you
[44:05] toggle back to the
[44:07] to the main
[44:08] file, I'm going to share a link
[44:11] to a Google Drive just to have together
[44:14] like a look
[44:15] into let's say a staff level solution
[44:18] this problem. Can you actually access
[44:20] that?
[44:21] Just let me know once you can actually
[44:23] access.
[44:25] Yes. Yes.
[44:28] Okay, once you landed there
[44:30] you are seeing like the whole system.
[44:32] So, the first thing which I kind of
[44:35] provide to you is like to clarify like
[44:37] are we speaking about like new user are
[44:39] we speaking about like existing user
[44:42] and then you need to state out like what
[44:44] is the business metrics that we're
[44:45] actually going to track for this system.
[44:47] For example, on this one we just
[44:49] maximize for user engagement. We want to
[44:52] keep our user to retain our user and
[44:54] also maximize the booking.
[44:56] So, at the end of the day you have like
[44:57] two metrics that you always need to look
[44:59] at them in pair like the click-through
[45:02] rate and the bounce rate.
[45:04] So, we want to avoid like recommending
[45:06] like clickbait
[45:08] recommendations to customers.
[45:11] At the same time what we would like to
[45:13] maximize to maximize the long-term
[45:15] satisfaction of user plus business plus
[45:18] also ad.
[45:20] So, the user want from user point of
[45:23] view want to minimize the bounce rate
[45:25] while maximizing the productive time
[45:27] that they spend on the platform. So,
[45:29] ideally at the end it should follow up
[45:31] like we should end up like with some
[45:33] conversion
[45:35] type of
[45:36] of metric.
[45:37] So, the user they actually need to book
[45:40] or actually click on something so to
[45:41] have some success. Otherwise that they
[45:43] signal that is actually scrolling
[45:45] through the app and they are not able to
[45:47] find what they are looking.
[45:48] Now, from a business point of view we
[45:51] can look on send rate the growth rate of
[45:53] business sign up. From an ad
[45:55] click-through rate, dwell time, ad
[45:57] revenue.
[45:58] Now, as bonus you can look on
[46:00] explainability like the sub values,
[46:03] bias, cold start,
[46:05] what is the fallback signal there and
[46:08] also the dilemma between exploration
[46:10] versus exploitation.
[46:12] Now, in terms of the design we have
[46:14] input as a user and output like a list
[46:16] of recommendations.
[46:18] Now, in terms of scale we have different
[46:20] kind of generator in order to fetch
[46:21] place that they are close and they are
[46:23] also open.
[46:25] And then we're also looking to we're
[46:27] going to follow from machine learning
[46:29] point of view we're going to treat it as
[46:30] a point wise learning to rank
[46:32] and create a binary classification.
[46:35] And then we can have like multitask like
[46:37] we can let's say output like different
[46:39] probabilities like
[46:43] what is the probability of actually
[46:44] booking of actually
[46:46] clicking on a listing
[46:48] and then what is the final engagement
[46:50] score. We're going to take the weighted
[46:51] average of those different
[46:53] probabilities.
[46:55] Then now in terms of the labels in terms
[46:57] of the labels we can use like soft
[46:59] labels. We can also have some hard
[47:00] positive negative examples. Those can be
[47:03] case that the user actually book.
[47:05] They leave a a recommendation or they
[47:08] are actually hide this listing.
[47:10] Now, in terms of negative example we
[47:12] need to be very specific that negatives
[47:14] are case that they were actually shown
[47:16] to the user but within x hour or x time
[47:19] the user didn't interact with.
[47:21] Now, for
[47:23] we need to stratify our data set and the
[47:25] reason for that is to understand like
[47:27] the popular places.
[47:29] Otherwise they are going to dominate our
[47:31] data set and we're only going to
[47:32] showcase like the popular place.
[47:35] And also in terms of the negative page
[47:37] you can even take like some random
[47:39] negative user item there.
[47:42] Now, in terms of the feature we're
[47:43] looking for offline and online feature
[47:45] store.
[47:47] We're looking also for data governance,
[47:49] how you're going to encrypt and privacy
[47:51] as well.
[47:52] Now, personalization we're looking on a
[47:54] user
[47:55] level on a an economic what is the
[47:59] LTV lifetime value of the user. Do they
[48:03] like expensive or cheap places, the
[48:05] relation and how they engage with the
[48:07] platform. What are usually the reaction
[48:09] of the user they perform and also do
[48:11] they have like a bad or good user
[48:13] experience so far.
[48:14] Now, other important feature are the
[48:16] average of the last 10 item embeddings.
[48:20] It is like the time of the day. Are we
[48:22] recommending like dinner place or lunch
[48:24] places.
[48:26] The
[48:27] another behavioral can be like the like
[48:29] rate for a particular category of
[48:31] restaurant.
[48:32] And then for cold start like how we're
[48:34] going to treat it. We're going to
[48:35] cluster like similar user together or
[48:37] similar listing together.
[48:40] Now, in terms of modeling you can
[48:42] mention like two model like logistic
[48:44] regression two tower network. You can
[48:46] mention that the two tower is the model
[48:48] of choice because we're actually able to
[48:51] capture like the non-linear
[48:52] relationship.
[48:53] We're going to have a tower for a user
[48:55] and we're going to have another tower
[48:57] for the item. Then we're going to fuse
[48:59] them together and we're going to have
[49:00] separate head per probability.
[49:03] Like
[49:04] click versus conversion you mean?
[49:06] Yes, exactly.
[49:08] And then we're going to have because
[49:10] we're following like the multitask
[49:12] type of approach like the shared layers
[49:14] they are going to update less frequent
[49:16] rather than the specialized layer.
[49:18] Now, in terms of the loss we're going to
[49:20] have like the loss per click, the loss
[49:22] also per queue. And also in terms of
[49:24] evaluation it's important to mention
[49:26] like the different metrics. For offline
[49:28] we can have precision at K, we can have
[49:30] recall at K, we can have like mean
[49:31] average precision.
[49:33] Online click-through rate, bounce rate,
[49:35] churn rate, revenue lift reaction rate.
[49:38] Then from a production point of view,
[49:40] like ML ops,
[49:41] how we're going to do like an offline
[49:43] evaluation followed by a shadow log-only
[49:45] deployment, followed by AB testing, like
[49:47] we're going to look on the success in
[49:49] the guardrail metrics. Uh even better,
[49:52] like use interleaving AB testing. Like
[49:54] what exactly is that? It is out of the
[49:57] top 10, like five of them they are from
[50:00] model one and the other five they are
[50:02] from model two. So, within the same,
[50:04] let's say list of recommendations, you
[50:06] just blend them together. So, they all
[50:08] are model one,
[50:10] even they're from model two. Multi-armed
[50:12] bandit, what is the rollback there in
[50:14] case something goes out, how we monitor
[50:16] the alerts. And in terms of system
[50:18] metrics, we monitor like the latency,
[50:20] the throughput, queries per second.
[50:22] In terms of retraining, how do we
[50:24] actually keep an eye on the data drift?
[50:27] Then how we actually follow a hybrid
[50:29] approach, like online, uh how we
[50:33] incrementally train the model during the
[50:35] online, and also how we actually retrain
[50:37] like the full model uh model every once
[50:40] per week.
[50:41] And then in terms of bias, like
[50:42] positional bias, layout, like
[50:45] popularity, so positional bias, how you
[50:47] understand like the popular places.
[50:49] At the same time, you can also use
[50:51] position as a feature. So, during
[50:53] conference, you just apply the same
[50:55] position for all of the features just to
[50:56] cancel this out. And you take into
[50:58] consideration that feature as part of
[51:00] the training.
[51:01] And then for popularity, you don't
[51:02] weight those
[51:04] those popular places. Important to
[51:06] mention the exploration versus
[51:07] exploitation. If you are only casing
[51:09] like the
[51:11] uh follow the exploitation, actually
[51:13] what the system is actually
[51:14] recommending, you're going to have a
[51:15] self-reinforcing loop. So, you need a
[51:18] sample to also
[51:20] recommend some random place or some new
[51:21] place.
[51:22] So, the system overall looks like that.
[51:24] You have the candidate generator, you
[51:26] optimize them for a call, and then maybe
[51:28] you have a distilled version of your
[51:30] bigger model that looks on a particular
[51:32] set of feature, actually take the 10K
[51:35] business, limit them to 100, and then
[51:37] you have your heavyweight ranker in
[51:39] order to reprioritize those ones. And
[51:41] then you follow with a post-processing.
[51:43] There is just if you want to do some
[51:45] apply some business rule, maybe for
[51:47] example, you do not want to showcase the
[51:49] same cuisine more than five times at the
[51:52] end
[51:53] in the recommendation.
[51:56] And that is all in terms of the system.
[51:58] Like for example, like think we're not
[52:00] going to recommend, let's say, Italian
[52:02] places
[52:03] only Italian places like have like more
[52:06] than five positions
[52:08] at the final list. And the way to
[52:10] actually limit that is through the
[52:12] post-processing. We have some business
[52:15] rule there that they actually adapt.
[52:17] And that is all in terms of the system.
[52:21] Okay.
[52:22] Huh.
[52:23] Wow. So, you think it's good to like
[52:28] copy this like skeleton of design,
[52:31] labels, features, modeling, and then
[52:34] like try to run through that really
[52:36] quick,
[52:37] and like just get it working end to end,
[52:39] even if I like haven't really fleshed
[52:41] out the features, you know, while I
[52:43] touch upon it, and then later go back
[52:46] and I guess on my own
[52:49] decide where it's most lacking, and then
[52:52] or I should I like ask the interviewer
[52:54] like, "Where do you want to
[52:56] dive into as far as bottlenecks?"
[53:00] Yeah, I would say follow this framework
[53:02] because it actually helps structure
[53:03] your, let's say, your thought. And then
[53:06] always leave at least 5 minutes at the
[53:08] end just for question, and also places
[53:11] that you can go back and actually do it
[53:14] like a deep dive.
[53:16] Yeah.
[53:18] Okay. Yeah, cuz there's so much, you're
[53:19] only going to be able to dive into like
[53:21] one thing. Um so, you got to make sure
[53:24] that like you've at least mentioned it
[53:26] so that you could dive into it if they
[53:27] want you to.
[53:29] Exactly. Okay. That's it.
[53:32] Sounds good.
[53:35] Thank you.
[53:37] Yeah, no worries. So, the thing that I
[53:39] was actually mentioning, it is like just
[53:41] try to follow like a structured approach
[53:43] here.
[53:44] Yeah.
[53:44] >> And then take it from there.
[53:47] Okay.
[53:48] Okay. I'll try redoing it with this
[53:50] structure. Thank you.
[53:52] Yeah.
[53:54] Perfect.
[53:56] Well, all right. So, you'll send me like
[53:57] a kind of like a write-up of things you
[54:00] thought about during this interview?
[54:03] Yeah, like for me, like you were missing
[54:06] a little bit the structure, like the
[54:07] areas that you touch point, it was
[54:09] actually to the point,
[54:11] but I would explain like more of a
[54:13] holistic picture. Like remember that
[54:15] this role is an ML engineer role. So,
[54:18] they're looking from end to end. They're
[54:20] not looking for a data scientist to
[54:22] actually train a model. They're actually
[54:23] looking for a person that will hit the
[54:26] ground, and they would actually able
[54:27] like to deliver, let's say, model from,
[54:31] let's say, from start to end.
[54:33] Mhm.
[54:35] Right.
[54:35] >> Yeah.
[54:37] Okay.
[54:39] Okay.
[54:41] Awesome. Follow on this structure,
[54:43] follow on this system, and yeah, and
[54:46] best of luck with your interview.
[54:48] Appreciate it.
[54:50] Thanks so much.
[54:52] Have a good night.
[54:53] You too.
[54:54] Bye.
[54:59] >> [music]
[55:07] [music]

FEEDBACK_MD:
---
section: "Self-evaluation and feedback"
start: "42:19"
end: "44:22"
start_seconds: 2539
end_seconds: 2662
---

yeah I would I would want to let me let me let me stop you here in order to switch over to the feedback, but first I would like to hear from you. How did you find this question and what is your self-evaluation? All right, so I found well this is a good question. I found it a little difficult to know how to pace things out. I think I got bogged down with the features which is like a common thing that people get tripped up on and I maybe wasn't I should have like gone further into like quickly getting to having a model that predicts the basic thing and then getting it deployed and then describing how I would evaluate it online. I think I should have gone to that a little more quickly rather than going like listing out all the possible additional nuance features that I might want to have. So, my self-evaluation is maybe mid-level but probably not yet senior. Yeah, I will tend to agree on that and I want to share with you. I'm just going to share with you a link. You covered stuff like the stuff that you covered it was actually okay, but it needed a more holistic view of the whole system. That was the missing point here. Let me actually share a link. If you toggle back to the to the main file, I'm going to share a link to a Google Drive just to have together like a look into let's say a staff level solution this problem. Can you actually access that? Just let me know once you can actually

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
Write JSON only to: splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.json \
    --video transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.json --out splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.qa-split.json \
    --video transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.validation-report.md

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
video.md: transcripts/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/video.md

--- CHAPTER `04:54` — Problem clarification and business metrics ---
window: 04:54 .. 42:19
recognition_status: single (1 items)

ITEM #6
  interviewer_question: time=05:59 text="So, what we're actually designing today is we're designing like the Yelp system, the recommendation algorithm behind the Yelp um system. Yelp recommendation system. Um so, this is like on the homepage, like you open up Yelp for the first time it today, and then you see a list of recommended venues, like they could be restaurants or bars or like any like place on the map, basically."
  candidate_answer: time=06:40 text="Got it. Um okay. And this is Is this just on the homepage? Are we thinking about the search system as well? Okay, so a user will come onto the page and given everything we know about them, um what's in their immediate vicinity, um what's open, we think they're going to we will show them the uh places that we think they're most going to want to visit. So, what Yeah, so what would we consider um to be like the thing that we're trying to optimize here? I guess it would be whether somebody actually visits the place. Um like how does Yelp make money? Okay. Okay, so so Yelp has a list of venues that have some either like a restaurant with a meal or like a laser tag place where you could sign up for an hour, but there's something uh where a user can convert for that venue. Uh and we want to like make sure like make that as like likely as possible that the user will convert whatever conversion means for the venue. Um I guess like do we get paid based on like if like you make a reservation for like I don't know, uh like $80 at a laser tag, like we get paid proportional to how big the the payment was for the reservation. you know, we want them to click on anything at all and and convert or we want to like optimize for I guess we maybe going to let people um or like I should say that the venues uh list their own prices. Um but yeah, we probably would want people to It's probably like a balance here between we want people to click on expensive reservations that we get a higher um commission for. But then we also don't want to like only show expensive things and then the user doesn't click on anything. Um and we should have shown them something a little cheaper. So, there's like a bit of a balance there. Um okay. what else should I think about? Um um Okay, so yeah, like we assume that the all the places that they're going to see are open and you can make a a reservation that night or I guess like sometime in the next week for for the venue, right? Like it doesn't really matter when the reservation happens as long as it happens during the session. Like they make the reservation during the session, right? Um What Okay, let me think about So, okay, so um Let me think about what we're trying to Okay, I think I have a sense of what we're trying to do. Um and we we Yeah, we want to uh increase I guess the the the online metric that we care about. I'll start writing things down. Um online online metric is Well, yeah, so like we get Do we get like a Is it a fixed commission? Sorry, I may may should be clear. Is it a fixed commission per click? Or do we get paid You said we get paid proportionally. So, so I guess like um total like the uh I hear a a being Oh, did you disconnect? No, I can still hear you. Okay, cool. Cool, sorry. Um So, I guess what we're going to try to optimize for is um the like total revenue generated um across all sessions uh through conversion. Like that's that's really what we're trying to optimize for. Um And then I'll think about what what we're going to be tracking in training uh towards that goal. So, Okay, so the general I'll maybe I'll talk about first um like what the end-to-end flow is going to look like. Um first from like when the user opens up the app and sees something and then um we can we can dive into different parts and and explore how how those work and like leading up to the inference. So, uh inference time um user goes to their app and then they make a request for So, at a certain time, they they open up Yelp and they want to see like given where I'm at um and what time it is uh what are all the places that I might want to look at right now. Um and maybe other day make a reservation for for tonight or for for somewhere down the line. Doesn't really matter as long as the session ends with a conversion uh where we're successful. Um So, then when when Yelp gets that um user request for for the homepage then we go into some sort of index of I guess like all the um So, this is like the Yelp server. And then we have an index which contains every um Yeah, these are just primarily venues, not like the events themselves, right? Um Right, so we have some sort of reverse index where we we know like where the location is, whether it's open um some basic things like that. I'll get into more things we know about the venues later. Um And then we we we get some sort of candidate set of of all the the potential venues that that are at least like within driving distance or or uh I guess I guess it doesn't have to be open right now, right? Because if we can make a reservation for like 5 days from now, then we don't have to really care if it's open at the moment that the user um goes to it. So, I think it's more important that we just see where the user is and find nearby places. Um and then the the index returns some candidates which we would then rank uh by some means. Uh and maybe just like something like a combination of like just clicking um clicking or converting. I'll think about that, how to balance between the two. Um And then we'll we'll serve up to the user whatever has the highest score. Maybe um if if we're optimizing for conversions, we could we could rank by that. Um but I guess given that that most people like that that the number of like the number of clicks across all views um is, you know, not that many. Like maybe like I don't know what the conversion may be like Well, if you're on the app, you're probably going to be looking at a few places. Um but like for all the items, maybe there's like a 10% chance that a given item gets clicked in a in a session. And then of those um that you convert is is like an even lower funnel. Um So, I would imagine that there'd be um like generally more like there'd be more positive labels in the click um like in the click data set and is it converted. So, maybe that would be make more sense as as like a primary filter. Maybe it could be like two stages depending on how large the um the candidate sets are. Of like first you could you could rank by is it going to get clicked? Um and then within those you could re-rank by like you once you once you cut to a cut-off of like the top I don't know, 50 most likely items to get clicked on, you could re-rank by the most like the the the likelihood that those would get a conversion. Um and then show the user from those uh 50 re-ranked. So, okay, anyway, sorry. I'm I should finish the end-to-end first. So, yes, the reverse index um would then I don't know how to represent a model. Uh Let's let's just call it like um some sort of let's say PCTR model. Oops, sorry. Um Right, which which then um Well, let's let's say for now, even though ultimately we care about revenue, we we we start by just predicting clicks. Um So, yeah, that's that's the overall flow at inference time. Um of how that would work. And So, yeah, let's talk about what kind of uh data we have available um before we talk about yeah, what kind of model we would make based on that data. Yeah? So, we have venues um and users and um I guess yeah, the way that a user's interact. So, so Yelp has Right, and then venues have different types of events. So, like a user who's going to bars is going to Yeah, I guess that's like a category of a a venue. Um All right, let me think of a few. So, there's there's like the free form text that describes it's or it's sorry, it's um it's name. Excuse me. Uh it's address. Um the owner's description. It has associated reviews across all things that people do in it. Um which are left by users, obviously. And uh we know the price of the uh whatever the the reservation. Um And then I'll just I'll just hop around a bit and I'll I'll jump back in if if I think of something else. So, a user and then like user um in a session. Just to make that clear that like this is what we know at inference time. Um So, we know what time it is that the user is browsing. The location that they're at. Um we know the history of past reservations. Um We know I guess like reviews that they've left. And Can you like Are you friends with other people on Yelp? Is there like I I guess that's not really a major feature of it, right? Is like the network of like where did your friends go out to, right? So, yeah, and then like we need some sort of I mean, I was Yeah, maybe like just a easier like predefined category instead of like just relying on this free form description. We give them certain categories that um like a taxonomy that they can fall into. We can maintain this taxonomy ourselves. The taxonomy could itself be like like some taxonomic classification. So, you could have like, you know, at a high level, nightlife. And then below that um uh like a bar versus a club versus a jazz venue. And those are like nested. And and then like yeah, you got a venue could have um multiple like levels of granularity of of classification there. Um Okay, so I think I think that's a that's enough to get started with. Uh or Okay, we also have our sessions. Um So, like historically, what is a what has happened on the app with regards to like what when a user um like saw a particular venue um and it was at this or Yeah, so a a a user so a So, a session is composed of a user looking at multiple venues at a certain like um position in the like like uh the results and then was clicked like did convert by the end of that session. Um which we should we should know that. Uh of like start time. Okay, so these are Oh, sorry. Um Right, so so that's that's what we know about what's what's happening. That's what we're trying to predict at at inference time. Um So, let me think more about um yeah, what what is the the the training objective that we're trying to optimize for. I guess um it might be like a combination of like did It's either we we could separately consider our success in predicting clicks and conversions or we could come up with like one overall uh metric that combines both of them. Um  Yeah, I guess I guess to keep it simple for now, I would rather just focus on predicting clicks and then I could think about how I would expand it to incorporate uh conversions as well later. Um Okay, so let me let me think about how to build like a um a training pipeline uh to to determine if someone's going to click on on a given results and then I'll Yeah, I'll think about um Yeah, we we don't really have to focus or maybe should I I Okay, I was thinking if I I need to worry about like building up the index properly um because like you know, like given given like uh a definition of the index that's going to determine what's even in or Sorry, am I am I like going to cold start this like from scratch or should I assume that a system already exists and I'm iterating on it? Um okay, so initially we're not going to have any sessions. We're not going to Right, all we're going to have is venues and users. So, initially we have to bootstrap this somehow um with with some heuristic metrics. So, I think before we get into like modeling anything um I would want to suggest that people visit popular uh venues in their area. So, um All right, so initially what kind of data So, okay, so so So, this is bootstrap So, this is like Yelp doesn't exist or Yelp is just a pure like database like you just search for things, but we don't like show anything on the homepage by default. where So, we we are giving uh people like things to possibly click on or convert to and we know whether they did or not. Um but yeah, those heuristics might be Yeah, things like uh I'm assuming um is it is it a popular venue in the area? Um does it have like a deal going on right now or good discount? I guess what I'm trying to say is there might be um like newer up-and-coming venues that aren't going like I don't know if if our old system has the ability to like balance exploring new venues versus exploiting ones and we have to come up with a way ourselves of of like randomly introducing like newer low PCTR uh items into people's feed just to get them out there and get information on whether people like them or not. Yeah? Right. So, yeah, so if I was Yeah, if I had the original system, then I would have some sort of basic uh yeah, like popularity metric and and I guess I don't know if we have like an ad system. Um or like based on like number of like good reviews, we do have that, right? Um which is a list of list of reviews and a review itself has like a numerical rating I guess out of five and and possibly photos and um and a text description of of the whatever, maybe like the event itself. Um text star rating out of five photo optional. Um and So, so yeah, let me let me think about how how I build a model which would um which would predict click given that Oh, the Yeah, as I said you even with the with the bootstrap model, it's going to be the case that most people like for the most part people aren't going to even click on a lot of the results. Um they're going to scroll through and then click on only a couple. So, there's going to be class imbalance that I'm going to have to address at some point. Um Maybe Yeah, and Yeah, given that I care a lot about um more about false Hmm, okay, so a false positive would be I show somebody something I think they're going to click on and they don't click on it. I mean, maybe they would think that I'm not really good at knowing what they like, but not a not a huge deal. If it's a false negative where there is something in my catalog that they could have clicked on, but I didn't show it to them, then that's potentially missed revenue. So, I guess I would And Yeah, and like given that clicking is a rarer thing, I would want to um maybe have a uh like a larger penalty for for missing uh like if the model predicts that they weren't going to click on it, but they actually would have, then that would that would incur a larger penalty than than the reverse. Um Okay, so Yeah, like for for setting up the training um system, I need to I need to create like a unified view of a user at a given point in time. Um I think it maybe should be Yeah, like pairwise. So, for for a user for a venue um predicts likely here that the user would have clicked on the venue um at the point of of browsing it in their search results. And then I guess Yeah, maybe some sort of offline metric that I would want to track would be if I'm just predicting like this this binary um label uh but it's it's showing up in a ranked list, then I'd want to use something like um discounted cumulative gain to uh assess like how well the the ranked results was um given that I like ran a simulation um and tried predicting the uh Yeah, the the likelihood of click for each item in the ranked list. All right, so I'll just add that offline metric and DCG for some n um posts at the top that that we care about uh for clicks, I guess. Um Okay, so so I think I'm going to Yeah, I'm going to build a a like Let me think. I guess I could start off by building a uh a vector that describes both the user and the um and the venue. And initially, to keep it very simple, I I could use some sort of linear model uh that that predicts, um, yeah, that that it produces a value between zero and one, uh, by feeding that through a sigmoid like a logistic regression, um, which predicts likelihood of click for a pair. And then we can think about making that more complicated, uh, if if we want to capture, uh, cross feature relationships. Um, but just to get something off the ground, I think I think logistic regression is is a fine start. Um, so yeah, let me think about what that would look like. Um, I think I'll just build up each each in uh, part of of this this vector at once or on on each side. So for a user,  um, yeah, I guess like given the time that they're browsing, if they're like looking for something to do right there and then, which I'm guessing is a lot of the time when you go on Yelp, it's not like just like plan out the the rest of your week, it's like I'm currently out somewhere and I want to find a place to go. That's probably the majority, I would imagine the majority use case. So, um, I want to have a sense of their, um, their city. So maybe like, yeah, so just the well, the city is already being used to do the filtering from the from the index like to to retrieve things that are close. Um, so maybe so I have user features, uh, venue features and user venue. Um, so I guess what I was trying to say is that um, like the the distance from a user to the venue could be something I'd want to use, but then that's very different in like Austin versus New York, right? Um, the like I you can drive in Austin, but you don't drive in New York. So then you could tend to go to you're willing to go further, relatively speaking, in Austin. Um, so I I guess maybe I I I'm just going to like throw something out here. Um, maybe like distance to venue divided by like something like city diameter. It's it's like a really rough, uh, ratio like like distance ratio. Um, just something to like normalize it, but I'd probably think about like whether it's like public transit or something. Um, and then uh, for the venue like is open as a bool, which mean yeah, again, we could we could still show venues that are closed. And obviously they're like when they're sending a Yeah, I'm not sure like there's like the balance between do I put this into the model or do I just like rely on the user doing the filtering themselves? Um, so they wouldn't even like see, let's say, um, venues that are closed if they're looking for something right this moment. Um, so I'll [clears throat] I'll think about whether doing cool like yeah, I think I'll just include everything by default. Um, but like I'll think about to do um, how to balance Maybe I shouldn't put it here, but uh, how to balance between uh, users doing filtering versus using uh, venue attributes in the model. Um, okay. And then So we have the address and then we have maybe like, um, average rating um, past month. Uh, sorry, did you disconnect for a sec? Excalidraw that's like you reconnected. Anyway, so I'm thinking about, um, yes, I want to know if it's a good venue, but then this is going to potentially penalize new venues who don't have many ratings yet. Um, so maybe there's some way of like normalizing this by like the the the the ratings that the venues received based and then like the number of ratings. Um, yeah, I'm not sure how to formulate that right now, but I'll think about that. Um, how to consider low rate Maybe like you have some sort of like, um, for the city you have like, uh, prior under like a prior probability of like what the average rating is for different venues of different categories at at diff like at different points in the life cycle and then you like use that as like the baseline that you're normalizing it by. I don't know. Um, and then the um, yeah, we could have like embedding repre from the text of the, um, of the name plus the description, which I could describe, um, later if if we have time, how to generate that, but we could use something like various like take an off-the-shelf just concatenate them together and then, uh, put it through an off-the-shelf BERT type model. Um, and that would give us an embedding to compare venues. And and yeah, again, we like even if it's in logistic regression, it doesn't matter. Like you can just, um, have each of these embedding dimensions as a separate coefficient. And you could have the taxonomy, um, as a categorical, um, one hot. Maybe like keep the category simple if the taxonomy simple and just use like the top level taxonomy. And then for a user, um, you could do something like  number of times uh, click We so we also know like well well, we know conversions. Like we know when people actually made reservations. So you could have like number of times clicked um, on yeah, let's say let's say venues of different So assuming that tax like for the top level taxonomy, um, we don't have that many categories. We have maybe like, I don't know, 15 or something. Like then it wouldn't be too bad to have a like one hot, um, features that were defined along like within that, um, set of values. Like number of times clicked on like taxonomy category one uh, last month. And then you can or like actually like basically I'm saying we you can have this like aggregated, um, feature which which describes like how often did they go to a bar or do they go to a restaurant that those of selling tacos or whatever, um, we choose for our top level taxonomies. And that should give us a good sense of what they're going to do next. Um, and then yeah, like maybe, um, some sort of uh, to like hour bucket. So like, you know, from zero to like 23 again as as like, um, as a one hot vector. Excuse me. Um, so to determine like when they're browsing that could affect what they want to click on. Um, okay. I I think I'll go a little deeper, but I I think this is pretty much the the basics of what I I would want to incorporate here. Um, given that we have we don't have much Well, so we also want to consider like people who tend to go to like So like a venue would have a certain type of person who goes to that venue, right? Like a jazz lover. So maybe I could think about like on the user-to-user side like like users who went to venues users who go to venues like the ones you go to, um, also go to venues like this one you haven't been to yet. Um, but that that's like a maybe like a later stage, um, interaction feature that, uh, is is worth incorporating, but just for the MVP for this initial iteration, we won't worry about it. But like, um, places that are like the ones that people similar to you go to. Um, and then yeah, maybe um, I guess this I'm not sure I'm not sure this is like a a model feature or this is like part of the index. Um, yeah, but you get it going the other way basically of of thinking about like of the places that the user has gone in the last month, what are venues that are similar to those places? Yeah, but I don't want to get too complicated right now before I've gotten the end-to-end system working for this set of features. So, I would build up a training set of examples of like from historical sessions hydrating the user and the venue with with these pieces of information then predicting or it would have the like did was clicked yeah as a bool and so how would I and I have to think about how I would split up this this data set into train validation and test. I think that I'd want to probably make sure that I don't leak user level data. So, I wouldn't want to have like data I would want to make sure that any users in the test set are not in the train or validation set. So, keep things separate like that. And then I probably would also want to consider that like what someone's done in the past is going to help me predict the future. So, I wouldn't want to have time leakage either with it within a user. So, I would probably want to consider like doing splits where like for some users I only consider like I I train on what like what their history was like what sessions from like 5 years ago and then I try to predict what they did well not sorry. I yeah I I only well sorry. I'm I'm I'm I'm not speaking very coherently. Okay, so I guess I guess within within this user stratified data set yeah I would I would want to let me let me let me"
  reference_answer: time=None text=None
  interviewer_feedback: time=06:50 text="Yeah, let's focus on the on the landing page. Yeah, through bookings, let's say. Yes. Yeah. Yes. Yeah. Yeah, okay, sorry. Mhm. The social aspect I don't believe that it is part of Yelp. Cold start. Yeah, we have a simple rule-based system. We can ask Okay. We already have a simple rule-based system which is giving us some sessions Make any reasonable assumption like you are designing the whole system so you have full power over any direction of the system."
  question_topic: ML

--- CHAPTER `42:19` — Self-evaluation and feedback ---
window: 42:19 .. конец
recognition_status: single (1 items)

ITEM #7
  interviewer_question: time=42:29 text='stop you here in order to switch over to the feedback, but first I would like to hear from you. How did you find this question and what is your self-evaluation?'
  candidate_answer: time=42:40 text="All right, so I found well this is a good question. I found it a little difficult to know how to pace things out. I think I got bogged down with the features which is like a common thing that people get tripped up on and I maybe wasn't I should have like gone further into like quickly getting to having a model that predicts the basic thing and then getting it deployed and then describing how I would evaluate it online. I think I should have gone to that a little more quickly rather than going like listing out all the possible additional nuance features that I might want to have. So, my self-evaluation is maybe mid-level but probably not yet senior."
  reference_answer: time=None text=None
  interviewer_feedback: time=43:43 text="tend to agree on that and I want to share with you. I'm just going to share with you a link. You covered stuff like the stuff that you covered it was actually okay, but it needed a more holistic view of the whole system. That was the missing point here."
  question_topic: Communication

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/interviewing-io/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10/ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
