<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "data-engineer-middle-amazon-tips-interview-query-2020-05-21",
  "transcript_folder": "transcripts/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21",
  "source_id": "data_engineer_middle_amazon_tips_interview_query_2020_05_21",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:18:02 +0200",
  "updated_at": "2026-05-20 21:32:21 +0200",
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
    "json": "splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/timecodes.txt",
        "en",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 21:18:02 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 2.0,
      "notes": null,
      "finished_at": "2026-05-20 21:32:20 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:32:21 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21`
- **Source ID:** `data_engineer_middle_amazon_tips_interview_query_2020_05_21`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:18:02 +0200
- **Last updated:** 2026-05-20 21:32:21 +0200

Фильтр в IDE: `*data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/timecodes.txt`<br>`en`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.pipeline-log.md` | — | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.xlsx` | 2.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.validation-report.md` | 1.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.pipeline-log.md`

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
SOURCE_ID: data_engineer_middle_amazon_tips_interview_query_2020_05_21
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21
INTERVIEW_LANGUAGE: en
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00] [Music]
[00:08] hi everyone this is Jay from a view
[00:11] query today I am doing a mock interview
[00:13] with Scott Scott is a machine learning
[00:17] engineer and data engineer at next door
[00:20] welcome to the mock interview Scott hey
[00:23] oh I thought this is a real interview
[00:25] [Laughter]
[00:35] so before we start I'd love for you to
[00:38] talk a little bit about yourself and how
[00:39] you got into tech engineering data all
[00:43] that yeah so let's see here I mean I got
[00:49] into tech because I was obsessed with
[00:52] computers when I was in high school when
[00:55] I thought I would credit them
[00:56] I really wasn't but I kept being
[00:59] interested in it in it so I needed up
[01:03] taking computer science for my
[01:05] undergraduate it was until like my first
[01:10] internship where I realized that this
[01:13] is really boring
[01:14] I started reading or like leads to stuff
[01:18] that I was doing was really boring I
[01:20] started reading a lot more software
[01:22] engineering literature and actually got
[01:24] a lot deeper into I guess the trade then
[01:34] I had initially thought I was going to
[01:36] be and I did I think that's kind of like
[01:39] why I'm here okay as I I still think
[01:43] it's a very interesting way to build out
[01:47] things that are useful for people yeah
[01:51] how I ended up in data is I've always
[01:53] been kind of a database nerd I guess or
[01:58] how how I store data efficiently I think
[02:03] there's been a lot of interesting
[02:08] problems surrounding that and I don't
[02:13] know I just kept digging into those kind
[02:16] of rules
[02:17] my first role out of my undergraduate
[02:21] degree was working on AWS in storage
[02:24] mm-hmm
[02:26] when I was working at a start-up I liked
[02:30] the projects where I got to build out
[02:33] our own data warehouse and then when I
[02:36] applied to next door I found most of my
[02:39] interests being around how to
[02:43] efficiently transform data it's it being
[02:47] something that could be searched and
[02:51] transformed very efficiently so I think
[02:55] that's like largely the journey that
[02:59] I've been through so far awesome
[03:01] yeah and I think that is good because
[03:04] I've asked a lot of people this question
[03:06] and they all have different answers
[03:08] based on how they feel about having
[03:11] eventually got to their current moment
[03:13] right and their current experience level
[03:15] and it's definitely super interesting I
[03:17] think yours is no different cool so
[03:21] let's start out with the first question
[03:23] and this is like more of a data
[03:25] engineering question coming Amazon but
[03:27] let's say that you have a table with a
[03:30] billion rows right and let's say that we
[03:33] want to add a column to this table but
[03:37] we want to do so without any sort of
[03:38] downtime can you lay out like the
[03:42] scenario and how you'd actually perform
[03:44] that well or yeah I mean before we dive
[03:51] into the question I guess I have a few
[03:54] questions for you what kind of database
[03:59] let's say it's a Postgres database
[04:05] database yeah okay so with if we don't
[04:15] want to incur any downtime I guess my
[04:19] question to you is what impact with
[04:23] downtime have good questions so downtime
[04:28] would be bad because let's say the
[04:30] is Amazon like e-commerce site right and
[04:34] so if we're down for like 10 seconds
[04:37] that's probably like a million dollars
[04:40] in sales or something okay so our best
[04:43] interest to keep up time because up time
[04:50] is worth the million dollars so exactly
[04:53] being able to backfill with time just
[05:03] isn't really I would I would actually do
[05:09] this in two phases
[05:10] okay and it also depends on like it can
[05:14] we have like a default value attached to
[05:18] so Postgres allows you to have default
[05:21] values without actually writing the
[05:25] actual call value into the record okay
[05:29] so we can use that as leverage then we
[05:35] don't even have to really backfill we
[05:36] just have to apply our table when our
[05:43] table definition change and then we're
[05:47] good to go
[05:48] all right so let's see it's not Postgres
[05:52] and then it's like my sequel or
[05:54] something so if we don't have that at
[05:56] all yeah we don't know you just want to
[05:58] say we don't have we don't have the
[06:00] default value so I would do this in
[06:04] phases I think it makes sense to lock
[06:13] out chunks of Records and update those
[06:18] values but let's initially just have
[06:20] them how many records get added to the
[06:38] table
[06:41] per second per second so let's say if
[06:48] there's a billion rows then let's say
[06:52] that there gets like a million rows
[06:57] added per day and then let's say like if
[07:01] we extrapolate from that like probably
[07:03] like like a couple like a thousand
[07:09] records per second that's probably not
[07:11] right but let's just say a thousand
[07:13] records per second okay yeah so one way
[07:19] to kind of do this is to create a table
[07:23] that is identical to the other table but
[07:26] with an extra record and have all new
[07:29] records write to that new table and then
[07:33] we'll slowly start copying data from
[07:36] that old table to the new table with
[07:42] whatever default value that we want to
[07:44] give at that table and when we're
[07:50] reading from that table we have to read
[07:52] from both tables for the short for the
[07:54] short term okay eventually after all of
[07:59] the old records are copied over to the
[08:05] new table we can drop the old table and
[08:08] move on with our lives and then we have
[08:13] we effectively have our new column with
[08:16] no downtime all right cool
[08:20] I want to ask you retro so what did you
[08:23] think about the questions that were
[08:25] asked what did you think about the
[08:27] interview um I think the questions that
[08:35] were asked were intentionally left vague
[08:37] no I definitely have to probe and get a
[08:42] better understanding of like where our
[08:45] constraints lives yep so that I could
[08:48] give a good ish answer
[08:55] I mean lemme answer so kind of hand wavy
[08:57] if I were being quite honest but I think
[09:02] like I think high level I hit them okay
[09:15] do you think in terms of like difficulty
[09:20] level unlike how much you have to pro is
[09:22] it more on so I guess on my side I think
[09:27] like a lot of the time I think it's like
[09:29] on the candidate for a lot of interviews
[09:32] because they're faced with a lot of
[09:37] variability in their interviewers
[09:39] because many can be more leading all
[09:42] some will be like less so right and so
[09:45] if you stop asking questions then
[09:48] potentially they may you know just move
[09:53] on to the next one and assume the worst
[09:55] which is that you didn't know anything
[09:59] even though you probably did know it and
[10:01] so do you think that there's like what
[10:06] do you think about like the amount that
[10:08] you have to like basically dig in versus
[10:10] like almost answer and like kind of have
[10:13] a conversational back and forth right
[10:16] I thought that one's hard to answer
[10:18] actually um I tend to play it by ear
[10:22] so I think if you ask too many questions
[10:25] then you're not doing any thinking or
[10:29] any Discovery on your own yeah which
[10:32] doesn't but
[10:33] well in debrief so it's good to have
[10:38] some ideas talk aloud on those kind of
[10:44] ideas and even just ask for feedback on
[10:48] what the interviewers thinks of like
[10:51] your idea
[10:53] yep um and I think that's good I think I
[10:56] think if you listen you also need to
[10:59] listen to the interviewer and pick up on
[11:01] any sort of hints that they may give you
[11:03] so when you said do things letter by
[11:08] letter immediately clicked in my head
[11:10] that was a hint yeah
[11:12] and if I pick up on the hand then the
[11:17] interviewer knows that I picked up on
[11:19] the hand and can probably think or I
[11:23] think the interview will think like okay
[11:26] this person probably knows yeah it
[11:28] what's going on here and what I was
[11:31] thinking in terms of structure I think
[11:35] it makes a lot of sense

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
Write JSON only to: splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.json \
    --video transcripts/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.json --out splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.qa-split.json \
    --video transcripts/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.validation-report.md

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
video.md: transcripts/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/video.md

--- CHAPTER `00:00` — Amazon Data Engineer mock interview ---
window: 00:00 .. конец
recognition_status: multiple (4 items)

ITEM #1
  interviewer_question: time=00:35 text="so before we start I'd love for you to talk a little bit about yourself and how you got into tech engineering data all that"
  candidate_answer: time=00:43 text="yeah so let's see here I mean I got into tech because I was obsessed with computers when I was in high school when I thought I would credit them I really wasn't but I kept being interested in it in it so I needed up taking computer science for my undergraduate it was until like my first internship where I realized that this is really boring I started reading or like leads to stuff that I was doing was really boring I started reading a lot more software engineering literature and actually got a lot deeper into I guess the trade then I had initially thought I was going to be and I did I think that's kind of like why I'm here okay as I I still think it's a very interesting way to build out things that are useful for people yeah how I ended up in data is I've always been kind of a database nerd I guess or how how I store data efficiently I think there's been a lot of interesting problems surrounding that and I don't know I just kept digging into those kind of rules my first role out of my undergraduate degree was working on AWS in storage when I was working at a start-up I liked the projects where I got to build out our own data warehouse and then when I applied to next door I found most of my interests being around how to efficiently transform data it's it being something that could be searched and transformed very efficiently so I think that's like largely the journey that I've been through so far"
  reference_answer: time=None text=None
  interviewer_feedback: time=03:01 text="awesome yeah and I think that is good because I've asked a lot of people this question and they all have different answers based on how they feel about having eventually got to their current moment right and their current experience level and it's definitely super interesting I think yours is no different cool so"
  question_topic: Communication

ITEM #2
  interviewer_question: time=03:21 text="let's start out with the first question and this is like more of a data engineering question coming Amazon but let's say that you have a table with a billion rows right and let's say that we want to add a column to this table but we want to do so without any sort of downtime can you lay out like the scenario and how you'd actually perform that well or"
  candidate_answer: time=03:44 text="yeah I mean before we dive into the question I guess I have a few questions for you what kind of database database yeah okay so with if we don't want to incur any downtime I guess my question to you is what impact with downtime have being able to backfill with time just isn't really I would I would actually do this in two phases okay and it also depends on like it can we have like a default value attached to so Postgres allows you to have default values without actually writing the actual call value into the record okay so we can use that as leverage then we don't even have to really backfill we just have to apply our table when our table definition change and then we're good to go something so if we don't have that at all yeah we don't know you just want to say we don't have we don't have the default value so I would do this in phases I think it makes sense to lock out chunks of Records and update those values but let's initially just have them how many records get added to the table yeah so one way to kind of do this is to create a table that is identical to the other table but with an extra record and have all new records write to that new table and then we'll slowly start copying data from that old table to the new table with whatever default value that we want to give at that table and when we're reading from that table we have to read from both tables for the short for the short term okay eventually after all of the old records are copied over to the new table we can drop the old table and move on with our lives and then we have we effectively have our new column with no downtime"
  reference_answer: time=None text=None
  interviewer_feedback: time=03:59 text="let's say it's a Postgres database good questions so downtime would be bad because let's say the is Amazon like e-commerce site right and so if we're down for like 10 seconds that's probably like a million dollars in sales or something okay so our best interest to keep up time because up time is worth the million dollars so exactly all right so let's see it's not Postgres and then it's like my sequel or something so if we don't have that at all yeah we don't know you just want to say we don't have we don't have the default value so per second per second so let's say if there's a billion rows then let's say that there gets like a million rows added per day and then let's say like if we extrapolate from that like probably like like a couple like a thousand records per second that's probably not right but let's just say a thousand records per second okay all right cool"
  question_topic: Data Modeling

ITEM #3
  interviewer_question: time=08:20 text='I want to ask you retro so what did you think about the questions that were asked what did you think about the interview'
  candidate_answer: time=08:27 text='um I think the questions that were asked were intentionally left vague no I definitely have to probe and get a better understanding of like where our constraints lives yep so that I could give a good ish answer I mean lemme answer so kind of hand wavy if I were being quite honest but I think like I think high level I hit them okay'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Communication

ITEM #4
  interviewer_question: time=09:15 text="do you think in terms of like difficulty level unlike how much you have to pro is it more on so I guess on my side I think like a lot of the time I think it's like on the candidate for a lot of interviews because they're faced with a lot of variability in their interviewers because many can be more leading all some will be like less so right and so if you stop asking questions then potentially they may you know just move on to the next one and assume the worst which is that you didn't know anything even though you probably did know it and so do you think that there's like what do you think about like the amount that you have to like basically dig in versus like almost answer and like kind of have a conversational back and forth right"
  candidate_answer: time=10:16 text="I thought that one's hard to answer actually um I tend to play it by ear so I think if you ask too many questions then you're not doing any thinking or any Discovery on your own yeah which doesn't but well in debrief so it's good to have some ideas talk aloud on those kind of ideas and even just ask for feedback on what the interviewers thinks of like your idea yep um and I think that's good I think I think if you listen you also need to listen to the interviewer and pick up on any sort of hints that they may give you so when you said do things letter by letter immediately clicked in my head that was a hint yeah and if I pick up on the hand then the interviewer knows that I picked up on the hand and can probably think or I think the interview will think like okay this person probably knows yeah it what's going on here and what I was thinking in terms of structure I think it makes a lot of sense"
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Communication

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/interview-query/data-engineer-middle-amazon-tips-interview-query-2020-05-21/data-engineer-middle-amazon-tips-interview-query-2020-05-21.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
