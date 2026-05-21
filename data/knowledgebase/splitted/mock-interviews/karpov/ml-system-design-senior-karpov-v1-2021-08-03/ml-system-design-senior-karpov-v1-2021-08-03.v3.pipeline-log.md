<!-- PIPELINE_MANIFEST
{
  "version": 3,
  "basename": "ml-system-design-senior-karpov-v1-2021-08-03",
  "transcript_folder": "transcripts/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03",
  "source_id": "ml_system_design_senior_karpov_v1_2021_08_03",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 18:21:12 +0200",
  "updated_at": "2026-05-20 18:25:01 +0200",
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
    "json": "splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/timecodes.txt",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 18:21:12 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 18:24:49 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 0.0,
      "notes": null,
      "finished_at": "2026-05-20 18:24:50 +0200"
    },
    {
      "id": 5,
      "name": "llm_validation",
      "llm": true,
      "model": "claude-sonnet-4-6",
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.pipeline-log.md#LLM_INPUT_STEP_5"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 18:25:01 +0200"
    }
  ]
}
-->

# Pipeline log v3

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03`
- **Source ID:** `ml_system_design_senior_karpov_v1_2021_08_03`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 18:21:12 +0200
- **Last updated:** 2026-05-20 18:25:01 +0200

Фильтр в IDE: `*ml-system-design-senior-karpov-v1-2021-08-03.v3*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/timecodes.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.pipeline-log.md` | — | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.validation-report.md` | 0.0s | completed |
| 5 | llm_validation | yes | claude-sonnet-4-6 | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.pipeline-log.md#LLM_INPUT_STEP_5` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.validation-report.md` | — | completed |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.pipeline-log.md`

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
SOURCE_ID: ml_system_design_senior_karpov_v1_2021_08_03
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00] всем привет сегодня мы здесь собрались с
[00:02] рядом преподавателей из харди миль чтобы
[00:05] обсудить в хорошей нетоксичной манере
[00:08] тех людей это как они прошли
[00:11] собеседование поймали дизайну который
[00:13] была записана и возможно даже
[00:15] опубликовано раньше чем это видео меня
[00:17] зовут валера бабушкин на момент записи
[00:20] видео я работаю в фейсбуке в лондоне по
[00:23] г представьтесь пожалуйста так меня
[00:25] зовут увага на момент записи в индексе
[00:28] яндекс маркете занимаясь моделирование
[00:31] бизнеса один из преподавателей курса
[00:33] хардом и что же ты подаешь блог по
[00:36] uplift моделирование игры скажи почему
[00:38] позвали сюда
[00:39] тебя меня зовут игорь какую поняли по
[00:42] упрощению валера бабушкиной я занимаюсь
[00:44] и матче нгам алиэкспрессе до этого
[00:45] занимался match.com и яндекс маркете
[00:47] кажется что об одной из задач котором
[00:49] сегодня будем обсуждать я что-то знаю а
[00:50] про что твой блог в хардом и
[00:52] тоже внезапно про matching и также право
[00:54] ранжирование отлично мы сейчас начнём
[00:56] как раз кстати с
[00:57] обсуждение собеседник про ранжирования
[00:59] но прежде чем мы начнем его ты же
[01:02] посмотрю видео разметали не буду давать
[01:04] итогов никто не станет задавать
[01:08] особенности знать какие то на них палыч
[01:10] мы прежде чем
[01:13] обсудим это собеседование я задам вопрос
[01:17] такой вы наверное читать что qml дизайн
[01:19] годами сегодня одно из ключевых
[01:21] собеседований которая определяет сеньор
[01:24] ность
[01:25] инженер это может пятый уровень и 6 7 8
[01:29] это бесконечно глубокая вещь собственно
[01:32] который очень хорошо показывает опыт
[01:35] понимание практические знания и мы когда
[01:38] записались в 3 видео там действительно
[01:40] видна разница между тем как миддлтон
[01:42] себя на этом собеседование и как сеньор
[01:44] вел себя на собеседовании
[01:45] почему один сеньор он не разбирался в
[01:48] конкретном вопросе который ему заду
[01:50] потому его
[01:51] году 2 больше избрался этом вопросе тоже
[01:53] можно видеть разницу между опытом и
[01:56] общими навыками но что вот на ваш взгляд
[02:00] самая важная в мыле дизайн но след очень
[02:05] важно понимать саму бизнес-задач а
[02:06] потому что в верхнем уровне у чуваков
[02:08] вроде сеньоров ее людей стоящих над ними
[02:10] хочется им принести кого-то бизнес
[02:12] задачу сказать что мы хотим получить те
[02:13] мы хотим заработать денег они туми
[02:15] транслировать какие-то понятные мэй
[02:17] pipeline и говорят здесь мы сделаем одно
[02:19] здесь делаем другой здесь делаем третье
[02:20] у нас есть вот вариант сделать так и
[02:22] сделать вот так здесь мы потеряем
[02:23] побольше этом придется купить больше
[02:25] оборудование но будет лучше или какой-то
[02:27] другой thread'ов возможно он знает как
[02:29] замерить эффект и он знает как посчитать
[02:32] выгоду как провести хотя бы базовое бы
[02:34] тесто легко это не очень базовый с
[02:36] разными дополнениями потому что очень
[02:39] часто мы не можем в тупую провести тест
[02:41] и часто это не работает потому что
[02:42] сиськи это без и есть как минимум
[02:45] кого-нить сезонность либо разные регионы
[02:47] и так далее так далее так далее и вот вы
[02:49] скоро лючок он должен все это понимать
[02:50] все это держать голове и уметь в
[02:52] достаточно короткие сроки перебивать
[02:54] бизнес задачу в мыльную задачу и давайте
[02:56] уже технической команде такой мы и так
[02:59] но игр значительная часть вещей которые
[03:00] хотел сказать действительно уже сказал
[03:02] вот но действительно первый тест которую
[03:05] хочу выделить это что марксистом дизайн
[03:07] конечно в каких то моментах
[03:08] от общего системы дизайна может
[03:10] отличаться но основные пункты
[03:12] действительно такие нужно уметь понимать
[03:14] какая именно задача стоит причем не
[03:17] обязательно счет к формулировке до из
[03:19] какой-то общей постановке
[03:21] выбирать разные варианты дальше уже
[03:25] уметь выстраивать эту систему так чтобы
[03:28] она именно по требование подходила так
[03:31] чтобы если допустим обстоятельства
[03:34] поменяются во времени через полгода то
[03:36] эту систему можно достроить
[03:39] перри перестроить как-то по-другому вот
[03:42] чтобы
[03:43] доработки были проще вот но если именно
[03:48] в детали какие-то сдаться то человек
[03:50] должен опять же все требования там
[03:52] объемы данных которые через эту систему
[03:54] будут идти осознать осознать какие
[03:57] сущности там есть существует четко
[03:59] выделить что там этот товар относится к
[04:01] такому-то мастеру не знает так далее вот
[04:04] продумать всю схему данных и там прочее
[04:08] прочее вот в целом дальнейшие детали мы
[04:11] например
[04:12] обсудим да то есть если подвести итог
[04:14] окажется что основная
[04:17] важная вещь в этом собеседование эта
[04:20] целостность
[04:21] нужно составить целостную картинку
[04:23] рабочего решения у нас будет дружеское
[04:27] интервью и мир дизайна
[04:29] mr design system design by several это
[04:32] три наиболее важных интервью который и
[04:34] по которым оценивается сеньор ность
[04:36] кандидата
[04:37] технологические компании будь то фейсбук
[04:38] гугл amazon и прочее
[04:41] задача имели дизайна и задача системы
[04:45] дизайна с твоей стороны рассказать мне
[04:47] историю это очень тяжело самом деле
[04:50] поможет 45 минут ты практически солирует
[04:52] в идеале и чем меньше вопросов я тебе
[04:55] задаю тем лучше я могу иногда задавать
[04:58] вопросы которые просто погружают тебя в
[05:00] кроличью нору это нормально это эти
[05:03] просто пишу signal там сейчас у нас все
[05:04] равно это такое пробная дружеская тут
[05:06] тут мы в порядке каретка сбора потом я в
[05:09] конце с тобой по разбираюсь что можно
[05:11] было сделать лучше что хорошо на что
[05:13] обратить внимание
[05:14] не так далее то есть я просто даю тему
[05:16] рассказывают почему эта тема важна а
[05:18] дальше мне рассказываешь лайма и дизайне
[05:20] как бы ты это дело с точки зрения мы то
[05:23] есть тебе не нужно ударяться
[05:24] инфраструктуру тебе не нужно говорить
[05:25] здесь нужна какая-то база данных здесь
[05:28] нужно столько скверов здесь нужно
[05:29] столько то оперативки нет все конкретно
[05:32] prime и
[05:32] а тема у меня будет следующий это не
[05:36] matching марш
[05:38] мальчик уже был знаком не придет
[05:42] кстати достаточно классическая ее
[05:44] съеденная пусть это будет ранжирование
[05:48] рекламы в фиде какой-то социальные сети
[05:51] вязать что социальная сеть у тебя
[05:54] люди просматривают ленту и там
[05:58] периодически нужно подкидывать им
[05:59] рекламу понятно почему то можно за счет
[06:02] этого социальные сети зарабатывает
[06:04] деньги возникает вопрос как нам
[06:07] правильно каждому человеку подкинуть
[06:09] конкретную рекламу так правильно я
[06:15] понимаю человек заходит социальную сеть
[06:18] представит ленту периодическим увидеть
[06:20] какие-то баннеры он может кликнуть на
[06:23] баннер может про скролить может
[06:25] пожаловаться
[06:25] да сразу такой вопрос социальная сеть
[06:31] зарабатывает с кликов это очень хороший
[06:35] вопрос о социальной сети безусловного
[06:38] зарабатывает криков но в сан-сити точно
[06:40] так же как у поискового движка
[06:42] есть понятие длинные деньги то есть
[06:44] рекламодатель то платит за то чтобы в
[06:47] итоге что-то купили то есть ты конечно
[06:50] можешь в каком-то промежутке времени
[06:53] заработать много денег максимизировать
[06:54] их но потом ты потеряешь много денег
[06:56] потому что у тебя тебя выйдут тогда
[06:58] задач понятно показывать самый дорогой
[07:00] баннер по нему кликнуть и все хорошо а
[07:02] тебе хочется еще чтобы все-таки купить
[07:07] значит можно наверно так сформулировать
[07:12] следующую эмаль задач у нас есть
[07:17] пользователь какого-то у которого есть
[07:19] кое-то профиль мы знаем про него там как
[07:23] минимум пол возраст
[07:24] какие-то минимальные интересы круг его
[07:26] друзей и так далее на кино ки
[07:28] сообществом подписан что это еще вот
[07:34] соответственно скорее всего там какой-то
[07:40] продакшен системе это будет выглядеть
[07:42] следующим образом он листает ленту и на
[07:46] там определенных позициях этой ленты у
[07:48] нас есть слот для баннера
[07:51] и соответственно нам нужно выбрать какой
[07:55] конкретно баннер мы хотим ему показать
[07:58] так чтобы он там с большой вероятностью
[08:00] него перешел и чет купил
[08:02] соответственно тут возникает как раз
[08:05] таки наша задача ранжирования то есть у
[08:07] нас есть какое какая-то база всех
[08:09] рекламных банеров предложений и
[08:15] в данный слот мы должны предоставить
[08:19] наиболее подходящий то есть если
[08:21] говорить о праймале задачу это прям вот
[08:23] ранжирование как много вообще у нас
[08:25] может быть потенциально таких банеров
[08:29] миллионы носит очень большое количество
[08:33] соответственно если мы то посмотрим на
[08:36] количество кандидатов при ранжировании
[08:39] мы поймем что наверное для начала нам
[08:43] нужно сделать какой-то первичный отбор
[08:44] то есть вообще когда решаются задачи
[08:47] связанные с ранжированием например
[08:50] задача поиска или того же матч инга
[08:52] которую мы так любим то есть несколько
[08:57] этапов отбора кандидатов то есть это вот
[09:01] можно просить как такую воронку сначала
[09:03] у нас она большая мы на входе имеем вот
[09:06] все баннеры которые есть ну практически
[09:09] и потом мы по каким-то правилам может
[09:12] быть по каким-то
[09:14] моделям машинного обучения должны это
[09:17] количество как-то сузить оставив там
[09:19] финальный н кандидатов небольшое число
[09:21] там условно 10 после этого вот эти вот
[09:25] малое количество кандидатов мы можем уже
[09:27] скормить в какую-то более серьезную
[09:30] модель машину обучения которые там
[09:32] какие-то сложные признаки чтобы она там
[09:35] хорошо определила по какому же манеру
[09:38] юзер наиболее вероятно перейдет и что-то
[09:41] купит когда саша начал рассказывать он
[09:46] ну не то чтобы сделал ошибку он начал
[09:48] рассказывать сначала про отбор
[09:49] кандидатов водорода еще потом он
[09:52] перепрыгнул к данным я причем в записке
[09:55] делать не записка
[09:56] а как данные собирать то есть
[09:59] даже написано экспрессе то есть он
[10:02] проданный рассказал но если мы берем
[10:04] какой-то логическую целостность быстрее
[10:06] наверно сначала нужны данные о строении
[10:09] кандидат наверное нам нужно начать того
[10:12] как мы собираемся
[10:13] отбирать кандидатов я не очень прям
[10:17] имею хорошее представление о том как
[10:18] работает конкретным такая рекламная сеть
[10:21] но так сделаю предположение о том что
[10:25] есть кит партнера до от которых вот эти
[10:28] баннеры проходят и соответственно
[10:30] соцсеть на их агрегирует соответственно
[10:35] изначально наши кандидаты это все
[10:38] баннеры так после
[10:42] нам нужно остановиться на какой-то
[10:46] кандидат на модели который отбирает
[10:47] адекватное количество для последующего а
[10:50] ранжирования что вообще здесь может быть
[10:52] что вам мы можем знать про баннеры вот
[10:54] эти вот рекламные картинка картинка и
[10:58] текст кто-кто-кто какая организация
[11:04] сотрудница муж не первый раз уже так
[11:06] возможно мы можем кроме того
[11:09] описать что это напиток футболка
[11:14] косметика
[11:15] услуга так у нас есть это сайт на
[11:18] который ведет достаточно много всего
[11:22] вот почему мы можем построить какие
[11:24] признаки касаемые именно банеров
[11:27] вот соответственно признаки пользователя
[11:30] у нас тоже имеются поскольку это у нас
[11:33] социальная сеть признаки взаимодействия
[11:37] пользователей с баннером
[11:39] ну наверно там стоит посмотреть
[11:42] показывали ли мы ему до этого такой же
[11:44] баннер
[11:45] может быть какие то похожие вот здесь то
[11:49] же есть достаточно большое пространство
[11:50] по тому как мы можем вот эти признаки
[11:54] генри тут он спрашивает какие фичи у нас
[11:56] есть и биде то есть я я когда ему говорю
[12:00] он спросил одессе нас картинка искал да
[12:02] у нас есть картинка у нас есть вебсайт
[12:05] некоторые видео у нас есть возможные
[12:07] интересы на которых идет не просто начал
[12:10] случайно набор слов говорить александр
[12:12] что периодически самое случается и
[12:14] просто выкрикивать слова воздух но это
[12:18] вот это нормально просто мы задались
[12:20] что-то здесь можно было улучшить
[12:21] личную прослушку я просто наш вопрос был
[12:24] след от и не мог прослушать потому что
[12:26] это не было озвучено
[12:28] картинка что мужчины при бондарь
[12:33] картинка но это очень хороший вопрос для
[12:36] начала диалога чтобы вообще понимать с
[12:37] чем мы работаем наверное передадим стал
[12:40] еще более углубиться в то как у цели мы
[12:42] преследуем и что мы хотим оценивать
[12:44] потому что насколько помню видео вы
[12:45] только в конце перешли к ожиданию
[12:47] выигрыша от клика на баннер то так но
[12:50] вообще самая
[12:52] за что я зацепился то что он сам сначала
[12:55] не предположил что мы про баннер можем
[12:57] знать вот что в целом тоже было бы круто
[13:01] если бы кандидат как бы сказал ну
[13:02] кажется что вот про баннер мы можем
[13:05] знать та-та-та-та-та-та и уточнить уже о
[13:07] интервьюера а действительно ли эта
[13:09] информация доступна верует то есть я
[13:11] соглашения причем скажем вас соглашусь
[13:13] на будет наверное он не должен меня
[13:16] спрашиваете ждать это не ответ он должен
[13:18] искать я считаю что у баннера но в
[13:21] принципе даже если не специалист в
[13:23] рекламе
[13:23] ты же все равно видеорекламу она может
[13:26] прикинуть что там есть но сказать пусть
[13:27] у нас имеется это это это это тогда мы
[13:30] делаем то то это
[13:32] а тут он у меня спросил о самом начале
[13:34] интервью сказал что чем больше это меня
[13:36] говорю им хуже чем одна из сложностей
[13:39] дизайнов как int или в том что этот патч
[13:42] практически 5 минутного выступления
[13:44] но еще зачастую на иностранном языке как
[13:47] кстати энергично отлично ты должен был
[13:50] сказать нет нет нет про все хантер и вот
[13:56] здесь он он он задал правильный вопрос
[13:58] но если я был бы на реальном интервью я
[14:01] бы сразу это у меня был начертан что это
[14:03] нет где 6
[14:05] что это нагиб что он не говорит мне
[14:08] утверждает своего опыта
[14:10] спрашивает уточнение то есть это не
[14:13] ошибка но это опять же вопрос то есть
[14:15] кажется что хотя бы было бы круто
[14:17] задавать вопросы в тот моя когда это уже
[14:19] очень специфично домена знания которые
[14:22] кандидат на в принципе могут знать и он
[14:25] спрашивать и пока настоящего эксперта
[14:27] глубокого где либо еще нужно прилагать
[14:29] вариант я не знаю может быть так может
[14:31] быть так может быть так вот это вот это
[14:33] вот а после этого же уточнить а такое
[14:35] вам кажется ну в крайнем здание то есть
[14:38] river city art сказал показывали мы ему
[14:42] и что-то он делал да наверное в этом
[14:46] моменте я хочу чуть остановиться и
[14:49] обсудить про то как мы будем измерять
[14:51] потому что мы вроде как определили
[14:54] задача машинного обучения мы вроде как
[14:56] поняли что у нас является так
[15:00] кандидатами для ранжирования что у нас
[15:03] является запросам то есть это вот сам
[15:05] пользователь
[15:06] его профиль и там момент времени в
[15:08] которой мы ему показываем вот этот
[15:11] баннер
[15:12] соответственно надо так закрепить вот
[15:17] тот момент что как мы будем измерять
[15:19] нашу модель как могла умереть его плане
[15:22] как мы будем не умереть в онлайн
[15:25] наверно стоит начать с онлайн а то есть
[15:30] тут скорее всего
[15:33] других вариантов я не вижу это а.б. у
[15:35] нас есть там модель старая модель новая
[15:38] мы проводим эксперимент
[15:41] все параметры
[15:44] отрегулировав чтобы точно сказать что
[15:47] там вот в таким-то уровнем значимости мы
[15:51] получаем вот такой вот прирост по какой
[15:54] метрики
[15:54] вот это хорош смотри что мы можем вообще
[16:00] оптимизировать в качестве бизнес метрики
[16:04] можно оптимизировать
[16:06] сетях можно оптимизировать
[16:10] покупки то есть если мы предлагаем
[16:13] человеку купить что-то мы наверное
[16:16] сможем дальше отследить чел
[16:18] куда он идет и что покупает нам партнеры
[16:20] должны говорить я думаю что вот стоит
[16:25] остановиться на чем-то одном из двух с
[16:29] покупками на дно может быть чуть сложнее
[16:31] потому что это более долгая история чем
[16:34] просто клик и как мне подсказывает
[16:40] интуиция не всегда наверное человек
[16:41] покупает вот данный товар с первого раза
[16:44] это правда ну знаешь какая система
[16:46] учится как раз на клики индекс цен
[16:51] ты читал я xd да понимаю я мать приводит
[16:54] к что учиться наклейки но можем учиться
[16:57] на клип здесь я начала начал улыбаться
[16:59] человек работающий в яндексе он читал
[17:03] яндексе я не верю что все мы тарикат
[17:06] ручные клики могут быть плохими ли он
[17:08] пришел не казаться
[17:09] если ты учти наклейки у тебя одна из
[17:12] информация это тайтл то это называется
[17:13] клик будет как ни странно говорить весь
[17:19] вопрос был достаточно простой вот он ска
[17:22] мы будем на что-то учиться опять же
[17:25] когда ты говоришь на что ты будешь
[17:27] учиться
[17:27] ниже плюс есть минус у меня бы например
[17:30] сварского можно учиться наклейки почему
[17:32] кликов немного гораздо больше чем
[17:35] покупок у кликов есть такие минусы
[17:38] упаковок есть такие плюсы но такие
[17:40] минусы в идеале сделать какой-то таргет
[17:43] композитный логично для это логично .
[17:47] врачи предположений еще знаешь что есть
[17:49] распространена практика обучения на
[17:50] время пребывания на странице после клика
[17:52] но не у всех компаний могут быть такая
[17:54] информация безусловно но
[17:55] допустим то что из крикета что есть
[17:57] покупка меня бы устроил сон стал вот
[17:59] есть такие плюсы и минусы возьмем как бы
[18:01] и зла и опять же если мы говорим про
[18:05] целостность решения есть несколько
[18:06] вокруг как я первый подход это просто
[18:08] постройки вызван solution при этом в ком
[18:10] на каждом пункте сказать что вот здесь
[18:12] может быть такая здесь такая здесь такая
[18:14] потом вернуться в принципе меня не
[18:16] смутило бы если бы он сразу оговорился
[18:19] что давайте мы вопрос выбора таргета
[18:22] даже отложим хотя это ну не очень круто
[18:24] но тем не менее и про это поговорим
[18:25] подробно отдельно сейчас меня будут вам
[18:30] сказал бы что я вернусь к 2 рации доход
[18:32] у меня базовый таргет я посмотрю вопрос
[18:35] про b
[18:35] представь что ты сравнивать что я не
[18:39] очень это тематике представь что у тебя
[18:43] в этой команде оранжевой реклама
[18:46] работает больше одного инженера так
[18:48] может такое быть и ты сравнить ни с
[18:51] одной моделью а с десятью а потому что
[18:55] каждый из них запилил какое-то и мега
[18:56] модель стандартный из транса то есть
[19:00] обычно в таком случае что-то меняется
[19:02] или все тоже самое когда каждый
[19:03] человеком ты вперёд своих речей потом
[19:05] это складывают в общую корзину
[19:09] ну типа вопрос в том насколько у нас
[19:14] большое поле для экспериментов если мы
[19:18] можем построить эксперимент так что это
[19:21] не обед с то например a b c или там еще
[19:23] дальше то в целом мы можем двигаться по
[19:25] такой стати мне что-то меняется меняется
[19:28] то что как мы будем результаты вот
[19:31] исследователей этих инженеров соединять
[19:34] ну то есть там может быть такое что мы
[19:37] добавили там одну фичу и добавили другую
[19:40] фичу параллельный аппарат это протестили
[19:43] там каждый свечей добавленных дает
[19:45] какой-то прирост который мы иногда
[19:48] замерили а потом когда и мы это
[19:49] соединяем вместе у нас черт вот идет не
[19:52] так а почему такое может быть
[19:54] это может могут быть по-разному
[19:59] составленные признаки то есть некоторые
[20:04] фичи могут ломать модели
[20:06] а может что-то в дизайне бы теста быть
[20:10] само по себе что делает его менее
[20:12] надежно в таком случае ну мы получается
[20:15] просто тестируем тогда нити не совсем те
[20:17] вещи которые мы хотим то есть у нас есть
[20:19] там параллельная разработка два инженера
[20:21] пилит свои печи
[20:22] каждый из инженеров после того как
[20:26] запилил фичи конкретно свои проверил
[20:28] запускает какой-то б там через неделю
[20:31] приходит мою этого круто у нас там
[20:32] метрика выросла к темно все и 2 инженер
[20:36] делать тоже самое и потом когда они
[20:38] говорят котят на все они как бы
[20:39] соединяются результаты и вот в этот
[20:41] момент мы получили уже третью модель
[20:43] который мы на самом деле не как не
[20:44] оценивали
[20:45] смотрите что он показал ну во первых
[20:49] какая метрика это даже не то же самое на
[20:52] какой-то орбиты ты будешь какая метрика
[20:56] но не обсудили вот эту себя то онлайн
[21:02] там в принципе можно понять что деньги
[21:06] но а ты смотрел для что ты помнишь тот
[21:10] момент был вопрос был следующим
[21:14] попробуем смерти отца юго б.а.
[21:21] представь что есть destin жене raw
[21:23] которые улучшают мы далеко как у нас в
[21:25] яндекс то есть ситуация абсолютно
[21:28] реально ну прям уж много инженеров они
[21:30] работают моделью и психологическом пойми
[21:32] так и происходит
[21:33] нет но как только есть инженеров
[21:35] работают 10 моделями
[21:37] то что происходит вы готовите много
[21:40] моделей
[21:41] готовится много модель его б они
[21:42] получается сравнивается не просто модель
[21:44] с контролем а еще много раз это сравнить
[21:46] а что произойдет если мы вот я спросил
[21:49] дальше саша что если тысячи инженеров
[21:50] работы у нас много будет ошибок на
[21:52] второго рода первых героев этих пытались
[21:55] все если мы выкатим просто тысячи
[21:57] моделей я спросил тысяч одинаковых
[21:58] моделей бака что одинаков понятно что
[22:01] они не одинаковые кредиты выдают то у
[22:03] нас даже страсти к куниц равнозначности
[22:05] 05 произойдет 50 ложных срабатываний
[22:10] а он не значил говорить тоже очень
[22:12] грамотно вещь то есть мы видим одну
[22:13] модель которая победила вторую модель
[22:15] которая победила
[22:16] забьем эти фичи в одну получите модели
[22:18] она может не победить проблема может
[22:20] быть в том даже не фичах а в том что в
[22:22] принципе не пятна никто и не победили
[22:24] вот я сел здесь записал себе ответить и
[22:28] а.б.
[22:29] sick решил то есть это реальная проблема
[22:32] которая возникает всегда как только вы
[22:34] начинаете каком-то множестве работать а
[22:36] если еще момент past papers of 10
[22:40] инженеров а представь их не 10000 и
[22:42] представь каждый из них выкатил модель
[22:45] который реально ничем не отличается от
[22:47] как от контрольной группы
[22:50] что покажет как бы в таком случае у нас
[22:56] есть 1000 моделей который ничем не
[22:57] отличаются от базового ну а нас к скажем
[23:01] так они могут быть обычно каких других
[23:03] вещах но реально они не отличаются с там
[23:06] только также вы тоже качестве они не
[23:09] дают тебе одинаковый результат на одном
[23:10] и том же единичном сэмпле но в среднем
[23:12] они не отличаются ну может показать и
[23:15] прирост на самом деле и покажет если
[23:19] висение
[23:20] не сломаны и почему покажет ну потому
[23:24] что каждый этом смысле почему пока ну
[23:29] вот почему ты скоро может показать
[23:30] прирост хотим и знаешь там реально нет
[23:32] прирост
[23:32] ну нету прироста у каждой там печей
[23:35] отдельности но 1000 инженеров запустили
[23:38] тысячи моделей
[23:39] ну это чуть другая история чем действий
[23:41] обезьяна 10 тысяч печатных машинок и
[23:43] 10000 лет пишут что то но тысячи
[23:45] инженера запустил тащи модель реально
[23:47] все из этих каждой из этих тысячи
[23:48] моделей она ни лучше ни хуже чем
[23:51] контрольную модель бред но вот
[23:54] реальность если у нас божественной
[23:55] истины а что покажет абэ что по каждой
[23:59] модели ну вот у нас и получается пройдет
[24:02] еще в тест вправду что что у нас
[24:04] получится что мы можем ожидать я здесь
[24:06] тогда что причесал приложи чтобы точно
[24:08] догадаться не сделал опять же наша
[24:12] задача посмотреть насколько глубоко он
[24:16] знает какую то тему хорошо допустим
[24:18] сразу не сказал ok
[24:21] это не то чтобы проблему нельзя знать
[24:23] все темы очень глубоко
[24:25] но нужно сказать что а б не за 10
[24:29] pricing это ганы или что-то еще это то
[24:33] что возникает
[24:34] теперь вас очень нужно оценивать
[24:35] насколько лучше стала твоя модель
[24:37] насколько оно ужасно прежде чем лезть в
[24:42] проблемы с моделью посмотри как дизайна
[24:44] бы у тебя сделан кто тебя больше одного
[24:46] инженера был просчет дизайн сделан так
[24:54] но хорошо мы модель значит выкинули ты
[24:57] сказал мы посмотрели попробуйте на
[25:00] прокси метрику быструю на клики как мы
[25:03] делаем в некоторых магических компаниях
[25:05] россии что теперь с онлайн метриками
[25:10] определились соответственно мы должны
[25:16] понять на что мы будем обучать модель
[25:19] pav они и как мы будем
[25:23] собирать для обучения данные вот значит
[25:27] смотрите на какой на 15 минуте мы стали
[25:30] говорить как мы будем собирать для
[25:31] обучения данные не то чтобы ну то есть
[25:35] это правильно и это даже не ну в
[25:40] принципе тут не так чтобы однозначно
[25:42] всегда мне кажется нужно вскакивать
[25:44] сразу так мы соберем данные иногда ты
[25:46] хотя бы чуть-чуть причесываюсь структуру
[25:48] немножечко решение или что тебе нужно
[25:50] потом такой ну да наверно нам нужна
[25:53] информация о том то том-то и ты
[25:54] начинаешь обсуждать данные но может
[25:57] действительно поздновато уже на согласен
[25:58] что тогда вот сам начале сказать что я
[26:01] сначала набрали вот это от этого будет
[26:03] зависеть каким-нибудь вреда и об этом
[26:05] скажу то есть ты всегда на росте я
[26:08] согласен что большую часть данных топор
[26:09] и уже чуть ли не сам начале можно
[26:11] обсуждать то что какие есть только ты и
[26:13] потенциально понадобится вот потом по
[26:15] ходу решения уже только вспоминать что
[26:17] еще можно докинуть и
[26:19] как это причесать схему поэтому очень
[26:21] хорошо пользоваться доской вот если вы
[26:22] смотрюсь интриги там ни один человек не
[26:24] пользовался насколько следом выходит
[26:26] приготовить пирог кстати я очень
[26:28] удивился что ну да потому что ты вышел
[26:31] народов написал какие вообще есть
[26:33] большие условно данные x y значит сразу
[26:38] какие фичи какие-то объекты как собирать
[26:40] дальше модель в ней лосс оффлайн уммой
[26:44] метрики дальше соответственно как только
[26:47] он про онлайн диплом оба тест но и
[26:51] дальше начал от этого танцы латина все
[26:52] структура есть да хорош и структуру
[26:56] можете не потому что декоративное доска
[26:58] мнение записать мне кто-то безмерно
[26:59] медисин хоть и нам стоящие маркера то
[27:02] есть если мы предполагаем нас есть кайта
[27:04] bass line который уже работает и уже
[27:06] что-то там дает то мы потом конкретному
[27:12] пользователю конкретному баннеру можем
[27:16] сказать типа если он кликнул то это один
[27:20] если не кликнул то это 0 от крикнул ни
[27:23] кликнул 10 задал он кстати хороший
[27:26] момент как даже негатива гораздо больше
[27:28] нужны ли нам какие-то специфичные
[27:30] негативы 0 и они все были очень хорошие
[27:33] кони что он отметить про скрытия или
[27:35] когда кто-то жалуется на рекламу этой
[27:37] мочка вы негатива но обычно их очень
[27:39] мало даже по сравненью с обычными
[27:40] кликами не так на блюде жалуется на
[27:42] рекламу необычные вы просто пропускаю на
[27:44] самом деле не особо согласен с тезисом
[27:45] что люди просто могут расковыривать к
[27:47] рекламу а скорее просто команда таран
[27:49] человек не знаю доли секунды тратит если
[27:50] он ничего интересно не заметила на
[27:52] пролистнул так что я бы их не отбрасывал
[27:53] как плохие негативы этот прям хорошие
[27:56] обычно негатива ну и согласно пью да не
[27:58] зацепило человека и он сразу же пошел
[28:00] дальше проводить баланс классов ну можно
[28:02] купить хитро функцию поддерживать и хоть
[28:05] даже нормализованные
[28:06] нормализованы курс энтропию она в этих
[28:08] задачах достаточно часто используется
[28:10] этот аналог фо колосса в картинка когда
[28:12] я очень много негативов заранее известно
[28:14] нормализованная образован трофей если я
[28:17] правильно помню потом покажу в коде она
[28:19] на дисбалансе классов на работают но
[28:22] хотя что имеется ввиду не работает потом
[28:24] обсудим одну к другой вопрос и в рекламе
[28:26] работу что ты скажешь так ну смотри я
[28:31] вопрос-то в начале вам не расслышал
[28:34] вопросам началась разве он собирал горди
[28:35] ты дал 0 и единицей
[28:37] жениться нас мы берем все единицы
[28:39] секретом раз как брать нули и он
[28:41] скважину не бывает разные например
[28:42] пожаловался на объявление это 10 просто
[28:45] быстро про скоро лил эту другую ну а
[28:47] увидел мол задержался на не кликал это
[28:49] третье
[28:49] нет вообще это все прекрасно что
[28:52] рассказал
[28:53] было бы вообще замечательно если бы но
[28:55] это уже в плюс прям было бы если бы он
[28:57] выкинул про парные торги ты в духе если
[29:00] он сказал что мы запоминаем
[29:03] именно пару что было допустим 2 баннера
[29:05] но он кликнул на тот они на этот вот и
[29:07] вот и это парни лосс в свою функцию
[29:12] добавить для ранжировать
[29:15] вот например но опять же там в
[29:17] постановке я просто не помню здесь
[29:21] просто общая задача стояла что что от
[29:23] одно место под баннер и нужно как бы
[29:25] травмирует выбрать или социальной сети у
[29:27] тебя есть feed.ly там вот как раз про
[29:31] постановку задачи может быть вы в начале
[29:33] недостатка медленно он спросил сколько
[29:36] баннеров а все этому поэтому он был
[29:39] вопрос про про scroll если бы было
[29:40] только одно место не было бы но все если
[29:43] там ситуация так что несколько баннеров
[29:45] то действительно вот парные штуки гриба
[29:48] очень посмотрим что до колена и
[29:50] соответственно для каждого баннера мы
[29:52] будем предсказывать вот такой вот скоро
[29:55] то есть 10 напрашивается какая-то
[29:58] бинарная классификации самый такой
[30:01] простой мы знаем что мы там для каждого
[30:04] баннера предсказывает город нуля до
[30:05] единицы
[30:06] типа 0 совсем плохо один кликаем вот как
[30:11] мы будем мерить насколько хорошо мы вот
[30:13] это вот классифицируем если говорить про
[30:15] метрики для ранжирования
[30:18] то наверное здесь можно использовать
[30:22] энди сиджи можно
[30:26] на то чтобы используйте 10g у тебя
[30:29] бинарные классификации тебе нужно вот
[30:32] вот я про это и говорю надо подумать ну
[30:39] если мы переходим бинарной классификации
[30:43] сейчас посмотрим для начала на данные
[30:46] то есть наверное у нас показа кликов
[30:49] сильно сильно меньше чем не кликов
[30:51] предположим что мы будем измерять f1
[30:57] ламинарные классификации что нам это
[31:01] даст нам даст искал на задача
[31:04] ранжирования правильно ну мы можем ее
[31:07] свести к классификации можем свести к а
[31:09] можем ли мы в классификация оценить
[31:13] метрика и ранжирование какое-то но в
[31:15] теории да но нам нужно нам нужно понять
[31:20] то есть метрики ранжирования ниже
[31:24] оценивают по конкретным запросам они все
[31:29] скопом
[31:30] как у нас есть метрики бинарная
[31:32] классификации хироси при хижины кулак
[31:36] один котировок ауке так рока ew.com
[31:39] кстати можно показывает количество верно
[31:47] но не от ранжированных от 01 пар который
[31:51] верно ну даже ранжиру на и парня я забыл
[31:55] слова то есть целом наверное мы можем
[32:00] выбрать и такую метрику так да то есть
[32:08] для нас цель такая чтобы
[32:10] скоро единички был выше чем скоро 0
[32:13] тогда мы все единички будем принимать
[32:17] вверх тянули опускать вниз и
[32:19] соответственно нам наверное не настолько
[32:21] важно по какому из банеров кликнет
[32:24] пользователь если он кликнет
[32:26] ну что есть на вот данному виду этапе
[32:28] понятно что потом нам будет от опасным
[32:31] потому что
[32:33] там он может кликнуть и купить iphone а
[32:35] может кликнуть и купить какую-нибудь
[32:38] безделушку и соответственно тут покупки
[32:40] немножко неравновесные но кажется что
[32:43] вот для бассейна можно выбрать такую
[32:45] штуку украшенный отговорки сделал
[32:49] сегодня тоже меня устроило поговорим еще
[32:53] раз про данные
[32:54] что мы обучаем клики против не кликов
[32:58] кликов у нас сильно меньше
[33:00] соответственно нам нужно придумать
[33:03] вообще то есть крики понятно как
[33:07] доставать понятно что это такое а что
[33:09] такое не клики мы могли пользователю
[33:13] показывает какое то объявление какой-то
[33:15] баннер и он мог его про скролить он мог
[33:21] его про скролить типа потому что он
[33:23] просто скрою
[33:24] или он мог построить потому что этому не
[33:26] интересно он мог на него пожаловаться
[33:28] вот то что человек жалуется на баннер и
[33:31] это нужно прям как какие-то hard
[33:33] негатива выносить что вот вот это ему
[33:35] показывать не надо ну пожаловаться
[33:39] скрыть там какие-то еще
[33:41] активности связанные прямо с неприятием
[33:44] рекламы вот соответственно если мы на
[33:47] майне на май нейм примерно одинаковое
[33:49] количество
[33:50] того что юзер кликал на баннер и юзер на
[33:54] баня жаловался
[33:55] или скрывал его на как раз получим
[33:59] какую-то более менее разметку который
[34:03] наверное сможем обучить бриз лайн так
[34:07] метрики есть данные накопали
[34:11] а финально как у тебя модель будет
[34:14] работать расскажу вот сейчас я хотела к
[34:18] этому перейти то есть к конкретному
[34:22] pipeline у все мы будем делать понятно
[34:26] что мы не будем спорить всех кандидатов
[34:28] все бояре там весь миллион миллиард
[34:30] сколько их там который у нас есть для
[34:34] начала нам нужно придумать какие-то
[34:36] более простые модели заметил что это
[34:38] было и вот здесь мы обсуждали кандидатов
[34:41] но потом понял что это сейчас еще не
[34:43] имеет смысл пока нет больших
[34:46] подробностей не тоже не имеет смысл что
[34:48] он пропустил какой-то важный кусочек мы
[34:50] обстреле сити даже кусочек он вернулся
[34:52] снова кандидат брянцев это оперативно
[34:55] интервью котором ты можешь возвращаться
[34:58] вот обычно говорю как это можно сделать
[35:00] ну во первых элементарно наверно не
[35:03] нужно ему показывать второй раз то что
[35:04] мы уже показывали это первое второе если
[35:13] мы сможем то есть у нас есть какие-то
[35:15] признаки пользователя здесь какие-то
[35:19] признаки баннера
[35:24] если мы вот
[35:26] сможем перевести пользователей банеров
[35:29] такие в такое векторное пространство что
[35:31] там вектор пользователь будет близок к
[35:36] вектору баннера если пользователь у него
[35:37] кликал соответственно взяв там к
[35:40] ближайших мы уже уже отберем какой-то
[35:45] пул кандидатов первичной которые мы
[35:47] можем давать модель дальше по моему
[35:50] единственное что он вообще за все видео
[35:51] говорит правого фичи и кажется что этого
[35:53] явно недостаточно нужно было бы добавить
[35:55] незнакомец контекст вроде того что мы
[35:57] берем несколько соседних постов в этой
[35:59] ленте куда мы хотим что-то вклеить можно
[36:01] там не знаю если у тя есть пост паркует
[36:02] событий можно вклеить рекламу этого
[36:03] события если у тебя расположен такой
[36:05] баннер
[36:05] можно добавить больше про признаки
[36:08] пользователь например что он хранил в
[36:09] историю недавно посещённый сайт и конь
[36:11] идентификатор . город или кластера ну
[36:14] казалось бы за него лишнюю минуту но это
[36:17] очень важно проговорить ну да ими так
[36:19] просто когда он говорит что мы состоим
[36:21] какой-то вектор пользу
[36:22] или мне совершенно непонятно нас на
[36:24] какую информацию этот вектор
[36:25] пользователь будет составляться вот то
[36:27] есть
[36:27] учтено летом контекст что пользователь
[36:30] посещал там последний там пару дней
[36:32] последний там 10 визитов да там каких-то
[36:35] страниц и так далее или это просто
[36:36] какое-то базовое очень тяжело
[36:38] обновляемый вектор вон то есть насколько
[36:40] он реагирует им на контекст поэтому до
[36:43] информации именно про факторы которые
[36:45] туда влетают в построении этих векторов
[36:48] правят не через к чуть более подробно
[36:51] раскрыть что такое фичи то есть конечно
[36:52] виктор пользователи вектор баннер а
[36:56] действительно нужны но из чего они
[36:57] состоят а дальше можно
[36:59] интеракция между ними может быть все жду
[37:01] ну вообще типа
[37:02] если мы проектируем какой-то большой
[37:04] поисковый движок то там бывает несколько
[37:08] разнородных кандидатах моделей то есть
[37:11] например если это прям вот поиск то там
[37:14] там как такой самый baila en можно
[37:18] использовать pn25 то есть по текстам
[37:20] вопрос документов 1 документ скажи
[37:23] слушателям чтобы им 25 и тех и дев очень
[37:25] схожие вещи да и все работали в
[37:29] поисковых кампаниях ну в общем-то да б м
[37:32] 25 от такой типа
[37:33] апгрейда то и т.д. то есть мы просто
[37:35] смотрим на
[37:38] ходимость тех же самых токенов запрос
[37:41] документ есть на самом деле и другие
[37:44] способы отбора кандидатов то есть
[37:46] по-хорошему они должны быть достаточно
[37:48] диверсифицированы мы например можем
[37:50] отбирать там если у нас вопросе есть
[37:52] картинки можем отбирать по картинкам
[37:55] если мы говорим про кита
[37:58] рекомендательных систем кстати говоря в
[38:00] том числе и про баню крутилки то
[38:03] наверное мы можем придумывать какие-то
[38:05] способы связанные с коллаборативный
[38:06] фильтрации то есть мы можем показывать
[38:09] человеку те баннеры которые мы
[38:11] показывали его друзьям
[38:14] соответственно вот тут у нас уже
[38:15] напрашивается там как минимум два
[38:18] способа отбора кандидатов и после этого
[38:23] мы должны там как 3 кандидатов нежить
[38:26] чтобы подать в дальнейшую модель вопрос
[38:29] ты построил эту модель ты падаешь им
[38:32] кандидату все работает хорошо
[38:34] возникает ли у тебя здесь какой-то петли
[38:37] обратной связи что ты
[38:38] людям выдаешь только то что моделям
[38:40] говорит и давайте модель им говорит
[38:42] вдвое только то на чем она была
[38:44] натренирована до этого ну как правило
[38:47] она ну покрайней мере как мы решаем
[38:50] подобную задачу мать инге то есть мы так
[38:55] у такое было и причем модель может
[38:57] переобучить именно надобно документы
[38:59] когда модель типа специально поднимает
[39:03] выдачи те документы которые она уже
[39:04] видела еще я уже запуталась том что
[39:08] понятно значит чем суть я пытался сашу
[39:12] навести на вопрос про фильмы клуб даже
[39:14] изначально если вы увидели некоторые
[39:16] несогласованность между окончанием
[39:18] который
[39:19] петли обратной связи как-то это не
[39:21] гнется просто которой фильмы клуб имел
[39:22] видов где я простая если я учу
[39:25] моделью давать рекламу потом я воочию на
[39:28] рекламе как эта модель является обратная
[39:31] я а будет ли я пыталась не все страшно
[39:34] просто что с этим сделать вот ты помнишь
[39:38] что он сказал дан отвечал очень хорошо
[39:40] про то что можно использовать либо
[39:41] эпсилон критики бы сэмплинг а после чего
[39:44] он сказал проведен сам сказал
[39:45] множество спуска следовали пас каких
[39:47] наводящих вопросов множество попробуем
[39:49] на этого перемотать чуть не понял до пфр
[39:52] так кстати говоря это достаточно сложно
[39:55] за детектив вот как вариант можно вообще
[39:59] поделить типа все множество документов
[40:00] на котором мы обучаемся и на которых мы
[40:03] применяем ся так чтобы они не
[40:05] пересекались
[40:06] мы скорее всего будем обучаться на
[40:08] каких-то данных из прошлого вот но здесь
[40:10] есть другой нюанс в том что наверное нам
[40:15] нужно еще показывать какие-то более
[40:18] свежий баннеры какие-то может быть
[40:21] сезонный что-то типа скажем если сейчас
[40:24] новый год и я хочу там купить елку то
[40:28] она мне будет нужна там через месяц уже
[40:30] то есть тут наверно может напроситься
[40:33] щелкать 1 кредит от на модель которая
[40:34] будет вот в эту общую ранжиру ющий
[40:38] выдачу
[40:39] давать какие-то сезонные штуки он
[40:41] сначала сказал так мы на одной обучаемся
[40:43] на другой применяем модель это было его
[40:45] первое предложение о том как избавиться
[40:48] от я буду иметь другой но вот этот
[40:51] вопрос а как для 2 на 2 будет переходить
[40:56] раз ты сказал что мы будем на одной
[40:59] выборки божественное применяться ну
[41:02] хорошо допустим не возникнет когда клуб
[41:04] а ты про обучать уборку я не не запомнил
[41:09] как мы будем ее разделять на то на чем
[41:11] учиться на чем проверять то есть я я
[41:13] решила хорошо я уйду обратно к что
[41:16] скачать уборка мы четыре года на это как
[41:19] мы до проверяем вот посмотрите это какая
[41:22] минут и 25 минут из 37 то есть и я вы
[41:26] меня зовут я думаю здесь
[41:28] если мы взяли ампул документов которые
[41:31] мы используем для обучения да а как мы
[41:34] его взяли на маниле что у нас было какие
[41:37] клики какие баннеры какие пользователи
[41:39] вот это все заморозили такой snapshot
[41:42] получили нашей социальной сети с
[41:45] рекламными
[41:46] штуками а проверились на чем дожди в
[41:57] оффлайне в оффлайне мы можем проверяться
[42:00] на том был 1 часть этого snapshot а то
[42:03] есть мы поди побили там на train ted как
[42:09] вопрос хороший здесь нужна стратегия
[42:11] такая чтобы
[42:13] наверное разные пользователи разные
[42:16] баннеры они разошлись по 30 тесту то
[42:18] есть не было такого что один
[42:22] пользователь он кликнул на два баннера и
[42:27] там один попал в трендовых тест
[42:29] кажется что самым надежным способом
[42:32] будет бить именно по пользователям то
[42:35] есть у нас есть пол пользователей на
[42:37] которых мы обучались по у пользователей
[42:38] на которых мы будем оценивать модель так
[42:41] как будешь применить в плане
[42:43] ты обучил модель так ты и вышли к тем
[42:46] пользователям которые были в обучающей
[42:48] выборке ну да я будешь в том числе они
[42:52] же то есть то есть ты сейчас механизм
[42:55] разбиение обучающие эволюционной выборки
[42:57] отделяет от того как то реальности
[42:59] будешь применять модель корректный
[43:01] вопрос
[43:02] некорректно ну кажется что он корректно
[43:04] и помощью без всем что говорил в gopro
[43:06] будущее да все так но если он даже пошел
[43:10] по такой дорожке в которой
[43:12] там именно бьет по людям то там нужно
[43:14] прям плотно засесть объяснить почему вот
[43:17] конкретном кейсе тебе кажется что именно
[43:19] по людям там полезно там например потому
[43:21] что у нас слишком нестационарные
[43:24] пространство да и мы шансов хорошо вы
[43:28] лидировать на будущем у нас нету а так
[43:30] мы хотя бы локально в моменте того что
[43:32] то можем прогрессировать вот потом
[43:34] предложил как делать и не помню все
[43:37] людям его времени мне кажется что в
[43:41] данном в данном контексте это имеет
[43:43] смысл потому что ну вот бывают такие
[43:48] хитрые штуки когда мы перри обучаемся на
[43:50] какие-то документы на какие-то отдельные
[43:52] запросы кажется что типа модель не
[43:59] должна работать сильно хуже на тех
[44:01] запросах и документах которые она там
[44:03] увидела во время обучения но мы не
[44:05] должны увидеть просадки качества на
[44:07] новых поэтому вот я считаю что вот
[44:11] именно такое разбиение на имеет смысл то
[44:14] есть мы берем так что у нас straight с
[44:17] между собой пользователями не
[44:18] пересекаются
[44:19] а получается ли следует ли из этого что
[44:23] у нас может так быть что в трене у нас
[44:26] пользователь из июля а в тесте из июня
[44:31] быть такой может можем ну типа
[44:35] можно развивать и по времени
[44:40] со временем но это звучит даже более
[44:46] логично но типа нет смысла предсказывать
[44:54] прошлое взяли конечно мы можем побить
[44:59] типа пользователем и по времени ну и еще
[45:05] нужно смотреть на сезонность то есть
[45:08] если например у нас в тесте было лет в 3
[45:11] не было лето в тесте новый год то
[45:15] наверное это не очень хорошее разбиение
[45:20] потому что новый год обычно покупают
[45:23] совсем другие вещи что я не хочу
[45:26] разбивать
[45:27] именно по времени потому что мы на
[45:30] другой сезон попадем возможно как ты ты
[45:33] можешь учесть учесть то что мы не
[45:37] попадем у другой сезон то взять типа
[45:39] июнь и июль как-то сезонные признаки
[45:41] учитесь это хорошая идея мы можем так
[45:46] учитывать но у нас сами
[45:49] документы уже будут сильно разделяться
[45:52] на типа летние и зимние
[45:54] ты же это выехать я бы хотел чтобы наша
[46:00] модель обучалась на то есть она она
[46:03] видела и те и те и те кто тебе мешает
[46:06] как сделать то есть нам нужно v-train
[46:11] насыпать такие данные чтобы они
[46:14] представляли там более-менее равномерно
[46:16] все там сезонные какие-то штуки которые
[46:18] нас интересуют и таким же образом
[46:22] насыпать их данные в тесте вы в идеале
[46:24] там есть у нас год тренингу тест
[46:27] например тогда по идее
[46:28] ну мы там до нее не ловим какие-то супер
[46:31] модные тренды которые там появились
[46:33] только сейчас хотя мы можно еще
[46:38] переобучаться
[46:39] во времени а вот этот год год train a
[46:42] god тесты ты бьешь просто по времени или
[46:44] по времени пользователю осознание
[46:47] а не продавать но тоже как мы обсудили
[46:49] что ты за начали предложил разбить по
[46:50] пользователям что в тесте одни в тренер
[46:52] в идеале конечно да а если год год взяли
[46:56] если мы сможем на собирать такие данные
[46:58] по времени и по пользователям чтобы у
[47:00] нас вообще было максимально типа
[47:02] отделенные друг от друга trainee тесты
[47:04] мы на тесте могли прям вот замирятся не
[47:07] боясь что мы там перри обучаемся под
[47:10] конкретного человека чтобы у вас был
[47:17] совсем другой путь
[47:19] так в итоге у нас мы знаем какие
[47:22] признаки брать мы можем чуть поподробнее
[47:25] обсудить особенно все признаки которые
[47:28] из разряда кликал покупал и прочее
[47:30] мы знаем как нам делить на тренд с сплит
[47:34] в принципе знаем как от оценивать онлайн
[47:38] но все-таки от мебели до конца понять
[47:40] вопрос ответ на про фидбэк лоб то есть я
[47:43] вернусь вы думаете я забыл и
[47:44] а я не забыл ты свою модель же
[47:47] применяешь ко всем баннером как какашка
[47:52] ты cardo scala разделим на множество на
[47:54] чем обучается и множество к чему
[47:55] применяется и как только у тебя есть
[47:57] модели которые ранжирует реклама на тебя
[47:59] ранжирует рекламу и потом все остальные
[48:01] данные которые ты собираешь паттерн
[48:02] жирной рекламе уже она там жирно было
[48:05] этой моделью тут тогда возникает вот
[48:09] этот вот еще один вопрос а можем ли мы
[48:12] там сделать не об этой оставь какой-то
[48:17] дополнительную штуку вот видите тут он
[48:20] задумался что-то схема то получается не
[48:21] подходит чтобы выдавать данные
[48:25] показывают банер а не для того чтобы
[48:27] человек по ним кликал а для того чтобы
[48:29] собрать и выборку и как это
[48:31] инкорпорировать в модель расскажи в саму
[48:34] модель да вот поговорим в тебе есть
[48:36] модель который выдает вероятность клика
[48:38] покупки клика мы же яндекс
[48:41] наклейки как ты применяешь и как в итоге
[48:45] ранжиру
[48:46] скажу то есть тебе вероятность клика
[48:48] нужно для чего для того чтобы выбрать
[48:53] наибольшую и показать пользователю то
[48:55] есть арк макс много по вероятность да а
[48:58] увеличит и что хочешь
[48:59] деньги хотя при этом вот он он просто не
[49:02] дата дни до ушел вглубь нашем же ставка
[49:05] iphone и какая-то дарит всем помочь
[49:07] финского на msi не все клики важны
[49:08] был уже при до должен один говоришь
[49:11] вроде как пальма
[49:12] тут чуть-чуть не дотянул хотя вот по
[49:15] абсолютно до этого дошел
[49:17] то есть вероятность клика на там смог
[49:20] века матожидания да хорошо то есть мы
[49:23] роджером по матожидания как добавить
[49:26] сюда стохастик насти чтобы увеличить
[49:28] exploration но в целом гляди какой
[49:32] нибудь стратегию до или
[49:34] или еще что ип сангрию тираны липазы
[49:37] закончите своим или взойдет ли описан
[49:41] гривен так смотря ну прям просто совсем
[49:46] случайно исчез из всех и всех банков
[49:48] которые у нас есть но мне кажется это
[49:51] просто транжирить трофи
[49:52] вот очень прожить потому что там есть
[49:55] куча очень мертвых баннеров вот который
[49:57] там ужасное совсем вот мы учились так ли
[50:14] чем во всем делились на показаны может
[50:17] быть минус если брать по классической
[50:19] говорит epson где там джексон постепенно
[50:21] уменьшается ну не выдержали не
[50:23] обязательно может просто витязь он к
[50:25] стопам оставить как быть функция
[50:27] возвращает одна константа предложил это
[50:28] не этом солнцем прямо довольно но это
[50:31] был хороший год хороший ответ при этом
[50:33] он в чем тебе не уже какой дух штуку
[50:35] диод интерполирует этот модель даже все
[50:37] же есть пазы кандидатов с которой ты
[50:38] выбираешь просто менее вероятно еще
[50:39] какой-то мент он сказал минут назад
[50:41] proart макс зачем подразумевал что
[50:43] вообще-то баннер 1 этаже может видимо в
[50:45] разных позициях меняться и видимо все
[50:46] таки есть это контекстной фичи он
[50:48] вначале все таки говорил по моему что мы
[50:49] потом будем смотреть показывается елене
[50:51] 20 я не стал на этом разбирать не манит
[50:53] нас осталось мало времени уже ну и опять
[50:55] же идея была в следующем как на
[50:57] что-то типа матожидания денег чаще всего
[51:00] смотрится да возникает вопрос у человека
[51:03] может меняться интерес конечно тает и ты
[51:08] когда сказал что мы кандидатов каких-то
[51:10] отбираем но ты сказал что мы стараемся
[51:12] это максимально syfy целовать чтобы
[51:14] среди них отбирать но в принципе
[51:16] кандидатов мы можем в том числе отбирать
[51:18] я так понял и по каким-то кластерам
[51:21] интересности но как только мы говорим
[51:22] про ленина ближайшие соседи мы можем до
[51:25] если у нас есть какое-то пространство
[51:28] интересов человека искать его вектор то
[51:32] мы можем там типа условно он там
[51:36] интересуется спорт политика музыка вот
[51:40] там из каждого кластера нас м прим здесь
[51:44] может быть очень много стратегий как мы
[51:45] убираем кандидатов но если ты истцов дом
[51:48] сен сэмплинг поставил ты уже внес
[51:50] какой-то exploration лида хорошим то
[51:56] есть ну все ты нкр привел это в модели
[51:58] она поставить я несколько представлял
[52:02] что это уже наверное не относится
[52:04] относится больше не к модели ок там
[52:06] сбору данных на будущее и тебе нужно
[52:09] как-то учитывать что мобилизует вино
[52:11] голуб
[52:11] то есть либо тебе модель не ко всем
[52:13] применяя тогда что применять к тем где у
[52:16] тебя
[52:16] ну да понятно как бы вовсе не знаю стоит
[52:19] ли нам говорит другом обидно будет мне
[52:20] кажется он хорошо проходим не знаю
[52:22] выделяет ими мнению вас электронов будет
[52:25] on buy стаценко для прошел значительного
[52:26] его очень неплохо он сказал несколько
[52:28] хороших вещей которыми основным
[52:29] непонимание почему он нарушил структуру
[52:31] своей уже почему несколько раз
[52:32] возвращался к хорошим вещам и снова из
[52:34] них уходил и так им не удавалось 1 идет
[52:37] конце развить но в целом все остальное
[52:38] очень плохо ну может быть я очень сноп
[52:41] ски подхожу но вообще очень интервьюеру
[52:46] понравится если выдержанная структура 2
[52:50] ответа
[52:51] это во первых во вторых чтобы ты но по
[52:56] требование действительно все все четко
[52:58] уточнил и сразу после требований вот на
[53:02] что
[53:02] громко бы сказал якобы обращаем внимание
[53:05] до что
[53:06] человек сразу говорит какая какие у него
[53:09] метрики целевые вот когда подступаться к
[53:13] моделям чуть не сразу говорит какой у
[53:15] него торги тылов что как бы далеко не
[53:18] сразу всплывало интервью согласно про
[53:22] структурную целостность она она а в него
[53:24] все эти пункты были но не были гурманам
[53:26] порядке да и во вторых может быть из за
[53:30] того что мы здесь просто обзор делать да
[53:32] и так богус очкам смотрели у меня вот не
[53:35] сложилось итоговая картинку вот что как
[53:37] это действительно выглядит вас важно в
[53:39] том числе вот если вы нарисовали на
[53:41] доске в да и согласья для себя три
[53:44] пункта подчеркну прямо которые для меня
[53:47] были бы красным
[53:48] относительно красным сигналом и the
[53:50] train тест сплит два момента не
[53:53] проговорил сам проект авто а раз уж я бы
[53:57] вынужден был про говорить про эту то мы
[53:59] начали плавать на второй момент это а.б.
[54:03] то есть тоже важная тем более проблема
[54:06] реально существует виртуальная не третья
[54:10] вещь видно клуб ну на мой взгляд один
[54:15] два раза отработать и вполне может шаг
[54:17] пройти на l5 google или facebook
[54:22] они так если подумать там даже ними три
[54:25] книги назвал у него есть отбор
[54:26] кандидатов я ни разу за видео не услышал
[54:27] про то что сильная метрика на например
[54:29] recall того что мы в кандидаты вообще
[54:31] что-то здраво выдаем
[54:32] да то есть ее по моему за сикретов ни
[54:34] разу не посещал этих вот у нас есть
[54:35] система сначала вот это потом вот это
[54:37] работаем если были слить нарисовалась то
[54:39] было бы очень легко например вместе
[54:40] кружочек этот сегмент а сказать здесь мы
[54:42] ценим
[54:42] у нас прокси метрика по которым и самим
[54:44] следим своим за своими моделями такая
[54:46] здесь там мы смотрим на эту метрику но
[54:48] финале бизнесу мы все равно показан вот
[54:50] на денежную метрику и на это внимание
[54:52] это собственно оффлайн онлайн метрики
[54:54] бизнеса волос и вот как только есть дура
[54:57] ты там расписал в руки и пункты найти и
[54:59] т.к. не приходит ты что думаешь про этот
[55:04] мой предыдущий комментарий было
[55:05] прозрачно zip from в целом в целом в
[55:08] целом ну посмотрев как было интервью
[55:12] кандидата
[55:13] но я допустим сразу чувствую что именно
[55:16] вот в этом домене и в этой сфере
[55:18] он скорее не работал вот потому что но
[55:21] это на мой взгляд они проблем ну как бы
[55:24] не работало не будем ждать пока
[55:26] конкретном в домино специфичный область
[55:29] вот но с другой стороны если как бы в
[55:31] других местах
[55:32] закрывал хиты задачу от и dota и опять
[55:35] просто повторюсь до ожидаешь там четкой
[55:37] структуры что если и за новую область
[55:40] возьмется то он тоже там все разложат
[55:42] разберется по полочкам мне очень
[55:43] понравилось на чем тебе ты ты ты
[55:45] рассказал в принципе общественный момент
[55:47] ты сказал сбор данных немножко прошелся
[55:49] профи чем то есть это зависит от
[55:51] интерьера я например мог пойти с тобой
[55:52] фичи начать прошла city or а если товар
[55:55] новый а сеть archos сглаживает наверное
[55:57] нужно учиться на что это может быть
[56:00] такое
[56:01] по pipeline у все отлично метрики apts
[56:07] ты теперь на что тебе обратить внимание
[56:09] train тест сплит естественный вопрос то
[56:11] есть видишь мы примем иначе я начал тебя
[56:13] докапывать корнева
[56:14] я вот в этом этом моменте да немножко
[56:18] проскочил то есть у меня была такая
[56:19] мысль что нужно подумать как мы встретим
[56:21] а в принципе вот это может был огромен
[56:23] сбора донская теперь как он потому что
[56:25] иначе мы метро какую такой тренд и
[56:27] сплита
[56:28] мы вот с тобой обсудим 3 на 3 in this
[56:30] pride мы вышли только кто-то сказал
[56:32] профи вколите спросил профит da club
[56:34] соответственно фильме клуб тоже вот это
[56:37] в итоге ты сам пришел к мысли сказал что
[56:39] мне хочется как-то
[56:41] исследовать и про б тест в чем суть чем
[56:46] севернее оппозиция тем больше вот этому
[56:48] нужно мой вопрос был наводящий
[56:54] представил
[56:54] apts иметь некоторую вероятность того
[56:57] что он выдаст ложноположительный
[56:58] результат и обвес от работы 95 процентов
[57:01] зрительными интервале даже если у тебя
[57:03] нет никакого результата пять раз состав
[57:05] среднем про краситься теперь когда я
[57:08] сказал про тысячу инженеров представь
[57:09] что из тысячи инженеров который крутит
[57:11] еще б тестов и разных и нету тебя по
[57:13] умолчанию 95 процентам интервале 50
[57:15] прокрасить и ты начнешь а почему же
[57:17] когда я бил их результаты у меня нет
[57:19] результат это потому что его и не было
[57:21] то есть вот это имел долго достойно
[57:24] достойно мне понравилось
[57:27] на эти вещи ну ты сам я думаю вами
[57:30] беседы понял на стране то есть но я
[57:34] думаю что еще одно два это можешь пол не
[57:36] проходить оси вам что тебе спасибо что
[57:39] пришел спасибо что посмотрели и до новых
[57:44] встреч всего доброго пока

FEEDBACK_MD:
---
section: "Фидбек от всех"
start: "52:18"
end: "55:43"
start_seconds: 3138
end_seconds: 3343
---

ли нам говорит другом обидно будет мне кажется он хорошо проходим не знаю выделяет ими мнению вас электронов будет on buy стаценко для прошел значительного его очень неплохо он сказал несколько хороших вещей которыми основным непонимание почему он нарушил структуру своей уже почему несколько раз возвращался к хорошим вещам и снова из них уходил и так им не удавалось 1 идет конце развить но в целом все остальное очень плохо ну может быть я очень сноп ски подхожу но вообще очень интервьюеру понравится если выдержанная структура 2 ответа это во первых во вторых чтобы ты но по требование действительно все все четко уточнил и сразу после требований вот на что громко бы сказал якобы обращаем внимание до что человек сразу говорит какая какие у него метрики целевые вот когда подступаться к моделям чуть не сразу говорит какой у него торги тылов что как бы далеко не сразу всплывало интервью согласно про структурную целостность она она а в него все эти пункты были но не были гурманам порядке да и во вторых может быть из за того что мы здесь просто обзор делать да и так богус очкам смотрели у меня вот не сложилось итоговая картинку вот что как это действительно выглядит вас важно в том числе вот если вы нарисовали на доске в да и согласья для себя три пункта подчеркну прямо которые для меня были бы красным относительно красным сигналом и the train тест сплит два момента не проговорил сам проект авто а раз уж я бы вынужден был про говорить про эту то мы начали плавать на второй момент это а.б. то есть тоже важная тем более проблема реально существует виртуальная не третья вещь видно клуб ну на мой взгляд один два раза отработать и вполне может шаг пройти на l5 google или facebook они так если подумать там даже ними три книги назвал у него есть отбор кандидатов я ни разу за видео не услышал про то что сильная метрика на например recall того что мы в кандидаты вообще что-то здраво выдаем да то есть ее по моему за сикретов ни разу не посещал этих вот у нас есть система сначала вот это потом вот это работаем если были слить нарисовалась то было бы очень легко например вместе кружочек этот сегмент а сказать здесь мы ценим у нас прокси метрика по которым и самим следим своим за своими моделями такая здесь там мы смотрим на эту метрику но финале бизнесу мы все равно показан вот на денежную метрику и на это внимание это собственно оффлайн онлайн метрики бизнеса волос и вот как только есть дура ты там расписал в руки и пункты найти и т.к. не приходит ты что думаешь про этот мой предыдущий комментарий было прозрачно zip from в целом в целом в целом ну посмотрев как было интервью кандидата но я допустим сразу чувствую что именно вот в этом домене и в этой сфере он скорее не работал вот потому что но это на мой взгляд они проблем ну как бы не работало не будем ждать пока конкретном в домино специфичный область вот но с другой стороны если как бы в других местах закрывал хиты задачу от и dota и опять просто повторюсь до ожидаешь там четкой структуры что если и за новую область возьмется то он тоже там все разложат разберется по полочкам мне очень

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
Target version for this run: v3 only.
Write JSON only to: splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. ml-system-design-senior-karpov-v1-2021-08-03.v1.qa-split.json, v2, ... except the target path above).
- Reuse items[] or field text from older splitter runs because validation passed before.

REQUIRED on step 2:
- Extract Q&A solely from PRIMARY_TRANSCRIPT in this LLM_INPUT_STEP_2 block.
- Do NOT read video.md or YouTube chapter titles (validation-only; absent in real interviews).
- Full fresh extraction; overwrite the target JSON completely.
- interviewer_feedback: interviewer speech only; candidate continuation -> candidate_answer or null feedback.
- Truncated interviewer ASR: merge adjacent interviewer lines in the transcript; do not paraphrase from external outlines.


======================================================================
OUTPUT PATHS (post-processing)
======================================================================
Save JSON to: splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.qa-split.json \
    --video transcripts/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.qa-split.json --out splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.qa-split.json \
    --video transcripts/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.validation-report.md

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
video.md: /Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/video.md

--- CHAPTER `01:59` — Самое важное в ML Design ---
window: 01:59 .. 05:52
recognition_status: multiple (2 items)

ITEM #1
  interviewer_question: time=00:01:59 text="самая важная в мыле дизайн но след очень важно понимать саму бизнес-задач а потому что в верхнем уровне у чуваков вроде сеньоров ее людей стоящих над ними хочется им принести кого-то бизнес задачу сказать что мы хотим получить те мы хотим заработать денег они туми транслировать какие-то понятные мэй pipeline и говорят здесь мы сделаем одно здесь делаем другой здесь делаем третье у нас есть вот вариант сделать так и сделать вот так здесь мы потеряем побольше этом придется купить больше оборудование но будет лучше или какой-то другой thread'ов возможно он знает как замерить эффект и он знает как посчитать выгоду как провести хотя бы базовое бы тесто легко это не очень базовый с разными дополнениями потому что очень часто мы не можем в тупую провести тест и часто это не работает потому что сиськи это без и есть как минимум кого-нить сезонность либо разные регионы и так далее так далее так далее и вот вы скоро лючок он должен все это понимать все это держать голове и уметь в достаточно короткие сроки перебивать бизнес задачу в мыльную задачу и давайте уже технической команде такой мы и так но игр значительная часть вещей которые"
  candidate_answer: time=00:03:00 text='хотел сказать действительно уже сказал вот но действительно первый тест которую хочу выделить это что марксистом дизайн конечно в каких то моментах от общего системы дизайна может отличаться но основные пункты действительно такие нужно уметь понимать какая именно задача стоит причем не обязательно счет к формулировке до из какой-то общей постановке выбирать разные варианты дальше уже уметь выстраивать эту систему так чтобы она именно по требование подходила так чтобы если допустим обстоятельства поменяются во времени через полгода то эту систему можно достроить перри перестроить как-то по-другому вот чтобы доработки были проще вот но если именно в детали какие-то сдаться то человек должен опять же все требования там объемы данных которые через эту систему будут идти осознать осознать какие сущности там есть существует четко выделить что там этот товар относится к такому-то мастеру не знает так далее вот продумать всю схему данных и там прочее прочее вот в целом дальнейшие детали мы например обсудим да то есть если подвести итог окажется что основная важная вещь в этом собеседование эта целостность нужно составить целостную картинку рабочего решения у нас будет дружеское интервью и мир дизайна mr design system design by several это три наиболее важных интервью который и по которым оценивается сеньор ность кандидата технологические компании будь то фейсбук гугл amazon и прочее задача имели дизайна и задача системы дизайна с твоей стороны рассказать мне историю это очень тяжело самом деле поможет 45 минут ты практически солирует в идеале и чем меньше вопросов я тебе задаю тем лучше я могу иногда задавать вопросы которые просто погружают тебя в кроличью нору это нормально это эти просто пишу signal там сейчас у нас все равно это такое пробная дружеская тут тут мы в порядке каретка сбора потом я в конце с тобой по разбираюсь что можно было сделать лучше что хорошо на что обратить внимание не так далее то есть я просто даю тему рассказывают почему эта тема важна а дальше мне рассказываешь лайма и дизайне как бы ты это дело с точки зрения мы то есть тебе не нужно ударяться инфраструктуру тебе не нужно говорить здесь нужна какая-то база данных здесь нужно столько скверов здесь нужно столько то оперативки нет все конкретно'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Communication

ITEM #2
  interviewer_question: time=00:05:14 text='не так далее то есть я просто даю тему рассказывают почему эта тема важна а дальше мне рассказываешь лайма и дизайне как бы ты это дело с точки зрения мы то есть тебе не нужно ударяться инфраструктуру тебе не нужно говорить здесь нужна какая-то база данных здесь нужно столько скверов здесь нужно столько то оперативки нет все конкретно prime и а тема у меня будет следующий это не matching марш мальчик уже был знаком не придет кстати достаточно классическая ее съеденная пусть это будет ранжирование рекламы в фиде какой-то социальные сети вязать что социальная сеть у тебя люди просматривают ленту и там периодически нужно подкидывать им рекламу понятно почему то можно за счет этого социальные сети зарабатывает деньги возникает вопрос как нам правильно каждому человеку подкинуть конкретную рекламу так правильно я'
  candidate_answer: time=00:06:15 text='понимаю человек заходит социальную сеть представит ленту периодическим увидеть какие-то баннеры он может кликнуть на баннер может про скролить может'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:06:25 text='пожаловаться да сразу такой вопрос социальная сеть зарабатывает с кликов это очень хороший вопрос о социальной сети безусловного зарабатывает криков но в сан-сити точно так же как у поискового движка есть понятие длинные деньги то есть рекламодатель то платит за то чтобы в итоге что-то купили то есть ты конечно можешь в каком-то промежутке времени заработать много денег максимизировать их но потом ты потеряешь много денег потому что у тебя тебя выйдут тогда задач понятно показывать самый дорогой баннер по нему кликнуть и все хорошо а тебе хочется еще чтобы все-таки купить значит можно наверно так сформулировать следующую эмаль задач у нас есть пользователь какого-то у которого есть'
  question_topic: ML

--- CHAPTER `06:28` — Социальная сеть как источник заработка ---
window: 06:28 .. 07:14
recognition_status: single (1 items)

ITEM #3
  interviewer_question: time=00:06:28 text='зарабатывает с кликов это очень хороший вопрос о социальной сети безусловного зарабатывает криков но в сан-сити точно так же как у поискового движка есть понятие длинные деньги то есть рекламодатель то платит за то чтобы в итоге что-то купили то есть ты конечно можешь в каком-то промежутке времени'
  candidate_answer: time=00:06:53 text='заработать много денег максимизировать их но потом ты потеряешь много денег потому что у тебя тебя выйдут тогда задач понятно показывать самый дорогой баннер по нему кликнуть и все хорошо а тебе хочется еще чтобы все-таки купить значит можно наверно так сформулировать'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:07:12 text='следующую эмаль задач у нас есть пользователь какого-то у которого есть кое-то профиль мы знаем про него там как минимум пол возраст какие-то минимальные интересы круг его друзей и так далее на кино ки сообществом подписан что это еще вот'
  question_topic: ML

--- CHAPTER `10:10` — Отбор баннеров ---
window: 10:10 .. 10:51
recognition_status: single (1 items)

ITEM #4
  interviewer_question: time=00:10:10 text='как мы собираемся отбирать кандидатов я не очень прям имею хорошее представление о том как работает конкретным такая рекламная сеть но так сделаю предположение о том что есть кит партнера до от которых вот эти баннеры проходят и соответственно соцсеть на их агрегирует соответственно изначально наши кандидаты это все баннеры так после нам нужно остановиться на какой-то кандидат на модели который отбирает адекватное количество для последующего а ранжирования что вообще здесь может быть'
  candidate_answer: time=00:10:52 text='что вам мы можем знать про баннеры вот эти вот рекламные картинка картинка и текст кто-кто-кто какая организация сотрудница муж не первый раз уже так возможно мы можем кроме того описать что это напиток футболка косметика услуга так у нас есть это сайт на который ведет достаточно много всего вот почему мы можем построить какие признаки касаемые именно банеров вот соответственно признаки пользователя у нас тоже имеются поскольку это у нас социальная сеть признаки взаимодействия пользователей с баннером ну наверно там стоит посмотреть показывали ли мы ему до этого такой же баннер'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `10:51` — Параметры баннеров ---
window: 10:51 .. 11:45
recognition_status: single (1 items)

ITEM #5
  interviewer_question: time=00:10:51 text='что вообще здесь может быть что вам мы можем знать про баннеры вот эти вот рекламные картинка картинка и текст кто-кто-кто какая организация'
  candidate_answer: time=00:11:04 text='сотрудница муж не первый раз уже так возможно мы можем кроме того описать что это напиток футболка косметика услуга так у нас есть это сайт на который ведет достаточно много всего вот почему мы можем построить какие признаки касаемые именно банеров вот соответственно признаки пользователя у нас тоже имеются поскольку это у нас социальная сеть признаки взаимодействия пользователей с баннером ну наверно там стоит посмотреть показывали ли мы ему до этого такой же баннер'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `15:15` — Как измерять модель ---
window: 15:15 .. 15:54
recognition_status: single (1 items)

ITEM #6
  interviewer_question: time=00:15:15 text='обсудить про то как мы будем измерять потому что мы вроде как определили задача машинного обучения мы вроде как поняли что у нас является так кандидатами для ранжирования что у нас является запросам то есть это вот сам пользователь его профиль и там момент времени в которой мы ему показываем вот этот баннер соответственно надо так закрепить вот тот момент что как мы будем измерять нашу модель как могла умереть его плане как мы будем не умереть в онлайн наверно стоит начать с онлайн а то есть тут скорее всего других вариантов я не вижу это а.б. у нас есть там модель старая модель новая мы проводим эксперимент все параметры отрегулировав чтобы точно сказать что там вот в таким-то уровнем значимости мы получаем вот такой вот прирост по какой'
  candidate_answer: time=00:15:25 text='наверно стоит начать с онлайн а то есть тут скорее всего других вариантов я не вижу это а.б. у нас есть там модель старая модель новая мы проводим эксперимент все параметры отрегулировав чтобы точно сказать что там вот в таким-то уровнем значимости мы получаем вот такой вот прирост по какой'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Experimentation

--- CHAPTER `15:54` — Выбор метрики ---
window: 15:54 .. 16:58
recognition_status: single (1 items)

ITEM #7
  interviewer_question: time=00:15:54 text='вот это хорош смотри что мы можем вообще оптимизировать в качестве бизнес метрики можно оптимизировать сетях можно оптимизировать'
  candidate_answer: time=00:16:25 text='остановиться на чем-то одном из двух с покупками на дно может быть чуть сложнее потому что это более долгая история чем просто клик и как мне подсказывает интуиция не всегда наверное человек покупает вот данный товар с первого раза это правда ну знаешь какая система'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:16:46 text='учится как раз на клики индекс цен ты читал я xd да понимаю я мать приводит к что учиться наклейки но можем учиться на клип здесь я начала начал улыбаться человек работающий в яндексе он читал'
  question_topic: Product Metrics

--- CHAPTER `18:35` — Вопрос про A/B-тестирование ---
window: 18:35 .. 20:45
recognition_status: single (1 items)

ITEM #8
  interviewer_question: time=00:18:35 text='про b представь что ты сравнивать что я не очень это тематике представь что у тебя в этой команде оранжевой реклама работает больше одного инженера так может такое быть и ты сравнить ни с одной моделью а с десятью а потому что каждый из них запилил какое-то и мега модель стандартный из транса то есть обычно в таком случае что-то меняется или все тоже самое когда каждый человеком ты вперёд своих речей потом это складывают в общую корзину'
  candidate_answer: time=00:19:09 text='ну типа вопрос в том насколько у нас большое поле для экспериментов если мы можем построить эксперимент так что это не обед с то например a b c или там еще дальше то в целом мы можем двигаться по такой стати мне что-то меняется меняется то что как мы будем результаты вот исследователей этих инженеров соединять ну то есть там может быть такое что мы добавили там одну фичу и добавили другую фичу параллельный аппарат это протестили там каждый свечей добавленных дает какой-то прирост который мы иногда замерили а потом когда и мы это соединяем вместе у нас черт вот идет не так а почему такое может быть это может могут быть по-разному составленные признаки то есть некоторые фичи могут ломать модели а может что-то в дизайне бы теста быть само по себе что делает его менее надежно в таком случае ну мы получается просто тестируем тогда нити не совсем те вещи которые мы хотим то есть у нас есть там параллельная разработка два инженера пилит свои печи каждый из инженеров после того как запилил фичи конкретно свои проверил запускает какой-то б там через неделю приходит мою этого круто у нас там метрика выросла к темно все и 2 инженер делать тоже самое и потом когда они говорят котят на все они как бы соединяются результаты и вот в этот момент мы получили уже третью модель который мы на самом деле не как не оценивали'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Experimentation

--- CHAPTER `22:37` — Увеличиваем число моделей и инженеров ---
window: 22:37 .. 24:05
recognition_status: single (1 items)

ITEM #9
  interviewer_question: time=00:22:37 text='а если еще момент past papers of 10 инженеров а представь их не 10000 и представь каждый из них выкатил модель который реально ничем не отличается от как от контрольной группы что покажет как бы в таком случае у нас'
  candidate_answer: time=00:23:15 text='прирост на самом деле и покажет если висение не сломаны и почему покажет ну потому что каждый этом смысле почему пока ну вот почему ты скоро может показать прирост хотим и знаешь там реально нет прирост ну нету прироста у каждой там печей отдельности но 1000 инженеров запустили тысячи моделей ну это чуть другая история чем действий обезьяна 10 тысяч печатных машинок и 10000 лет пишут что то но тысячи инженера запустил тащи модель реально все из этих каждой из этих тысячи моделей она ни лучше ни хуже чем контрольную модель бред но вот реальность если у нас божественной истины а что покажет абэ что по каждой модели ну вот у нас и получается пройдет еще в тест вправду что что у нас получится что мы можем ожидать я здесь'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Experimentation

--- CHAPTER `25:17` — Офлайн обучение ---
window: 25:17 .. 25:26
recognition_status: single (1 items)

ITEM #10
  interviewer_question: time=00:25:17 text='сказал мы посмотрели попробуйте на прокси метрику быструю на клики как мы делаем в некоторых магических компаниях россии что теперь с онлайн метриками определились соответственно мы должны понять на что мы будем обучать модель pav они и как мы будем'
  candidate_answer: time=00:25:23 text='собирать для обучения данные вот значит смотрите на какой на 15 минуте мы стали говорить как мы будем собирать для обучения данные не то чтобы ну то есть это правильно и это даже не ну в принципе тут не так чтобы однозначно всегда мне кажется нужно вскакивать сразу так мы соберем данные иногда ты хотя бы чуть-чуть причесываюсь структуру немножечко решение или что тебе нужно потом такой ну да наверно нам нужна информация о том то том-то и ты начинаешь обсуждать данные но может действительно поздновато уже на согласен что тогда вот сам начале сказать что я сначала набрали вот это от этого будет зависеть каким-нибудь вреда и об этом скажу то есть ты всегда на росте я согласен что большую часть данных топор и уже чуть ли не сам начале можно обсуждать то что какие есть только ты и потенциально понадобится вот потом по ходу решения уже только вспоминать что еще можно докинуть и как это причесать схему поэтому очень хорошо пользоваться доской вот если вы смотрюсь интриги там ни один человек не пользовался насколько следом выходит приготовить пирог кстати я очень удивился что ну да потому что ты вышел народов написал какие вообще есть большие условно данные x y значит сразу какие фичи какие-то объекты как собирать дальше модель в ней лосс оффлайн уммой метрики дальше соответственно как только он про онлайн диплом оба тест но и дальше начал от этого танцы латина все структура есть да хорош и структуру можете не потому что декоративное доска мнение записать мне кто-то безмерно медисин хоть и нам стоящие маркера то есть если мы предполагаем нас есть кайта bass line который уже работает и уже что-то там дает то мы потом конкретному пользователю конкретному баннеру можем'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `27:23` — Взаимодействие с баннером ---
window: 27:23 .. 30:15
recognition_status: single (1 items)

ITEM #11
  interviewer_question: time=00:27:23 text='сказать типа если он кликнул то это один если не кликнул то это 0 от крикнул ни кликнул 10 задал он кстати хороший момент как даже негатива гораздо больше'
  candidate_answer: time=00:27:28 text='нужны ли нам какие-то специфичные негативы 0 и они все были очень хорошие кони что он отметить про скрытия или когда кто-то жалуется на рекламу этой мочка вы негатива но обычно их очень мало даже по сравненью с обычными кликами не так на блюде жалуется на рекламу необычные вы просто пропускаю на самом деле не особо согласен с тезисом что люди просто могут расковыривать к рекламу а скорее просто команда таран человек не знаю доли секунды тратит если он ничего интересно не заметила на пролистнул так что я бы их не отбрасывал как плохие негативы этот прям хорошие обычно негатива ну и согласно пью да не зацепило человека и он сразу же пошел дальше проводить баланс классов ну можно купить хитро функцию поддерживать и хоть даже нормализованные нормализованы курс энтропию она в этих задачах достаточно часто используется этот аналог фо колосса в картинка когда я очень много негативов заранее известно нормализованная образован трофей если я правильно помню потом покажу в коде она на дисбалансе классов на работают но хотя что имеется ввиду не работает потом обсудим одну к другой вопрос и в рекламе работу что ты скажешь так ну смотри я вопрос-то в начале вам не расслышал вопросам началась разве он собирал горди ты дал 0 и единицей жениться нас мы берем все единицы'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `30:15` — Метрики ранжирования ---
window: 30:15 .. 33:09
recognition_status: single (1 items)

ITEM #12
  interviewer_question: time=00:30:15 text='мы будем мерить насколько хорошо мы вот это вот классифицируем если говорить про'
  candidate_answer: time=00:30:15 text='метрики для ранжирования то наверное здесь можно использовать энди сиджи можно на то чтобы используйте 10g у тебя бинарные классификации тебе нужно вот вот я про это и говорю надо подумать ну если мы переходим бинарной классификации сейчас посмотрим для начала на данные то есть наверное у нас показа кликов сильно сильно меньше чем не кликов предположим что мы будем измерять f1 ламинарные классификации что нам это даст нам даст искал на задача ранжирования правильно ну мы можем ее свести к классификации можем свести к а можем ли мы в классификация оценить метрика и ранжирование какое-то но в теории да но нам нужно нам нужно понять то есть метрики ранжирования ниже оценивают по конкретным запросам они все скопом как у нас есть метрики бинарная классификации хироси при хижины кулак один котировок ауке так рока ew.com кстати можно показывает количество верно но не от ранжированных от 01 пар который верно ну даже ранжиру на и парня я забыл слова то есть целом наверное мы можем выбрать и такую метрику так да то есть для нас цель такая чтобы скоро единички был выше чем скоро 0 тогда мы все единички будем принимать вверх тянули опускать вниз и соответственно нам наверное не настолько важно по какому из банеров кликнет пользователь если он кликнет ну что есть на вот данному виду этапе понятно что потом нам будет от опасным потому что там он может кликнуть и купить iphone а может кликнуть и купить какую-нибудь безделушку и соответственно тут покупки немножко неравновесные но кажется что вот для бассейна можно выбрать такую штуку украшенный отговорки сделал сегодня тоже меня устроило поговорим еще'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:32:53 text='раз про данные'
  question_topic: ML

--- CHAPTER `33:09` — Виды «не кликов» ---
window: 33:09 .. 34:12
recognition_status: single (1 items)

ITEM #13
  interviewer_question: time=00:33:09 text='такое не клики мы могли пользователю показывает какое то объявление какой-то'
  candidate_answer: time=00:33:15 text='баннер и он мог его про скролить он мог его про скролить типа потому что он просто скрою или он мог построить потому что этому не интересно он мог на него пожаловаться вот то что человек жалуется на баннер и это нужно прям как какие-то hard негатива выносить что вот вот это ему показывать не надо ну пожаловаться скрыть там какие-то еще активности связанные прямо с неприятием рекламы вот соответственно если мы на майне на май нейм примерно одинаковое количество того что юзер кликал на баннер и юзер на баня жаловался или скрывал его на как раз получим какую-то более менее разметку который наверное сможем обучить бриз лайн так метрики есть данные накопали'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `38:30` — Вопрос переобучения ---
window: 38:30 .. 41:06
recognition_status: single (1 items)

ITEM #15
  interviewer_question: time=00:38:30 text='кандидату все работает хорошо возникает ли у тебя здесь какой-то петли обратной связи что ты людям выдаешь только то что моделям говорит и давайте модель им говорит вдвое только то на чем она была натренирована до этого ну как правило'
  candidate_answer: time=00:38:47 text='она ну покрайней мере как мы решаем подобную задачу мать инге то есть мы так у такое было и причем модель может переобучить именно надобно документы когда модель типа специально поднимает выдачи те документы которые она уже видела еще я уже запуталась том что понятно значит чем суть я пытался сашу навести на вопрос про фильмы клуб даже изначально если вы увидели некоторые несогласованность между окончанием который петли обратной связи как-то это не гнется просто которой фильмы клуб имел видов где я простая если я учу моделью давать рекламу потом я воочию на рекламе как эта модель является обратная я а будет ли я пыталась не все страшно просто что с этим сделать вот ты помнишь что он сказал дан отвечал очень хорошо про то что можно использовать либо эпсилон критики бы сэмплинг а после чего он сказал проведен сам сказал множество спуска следовали пас каких наводящих вопросов множество попробуем на этого перемотать чуть не понял до пфр так кстати говоря это достаточно сложно за детектив вот как вариант можно вообще поделить типа все множество документов на котором мы обучаемся и на которых мы применяем ся так чтобы они не пересекались мы скорее всего будем обучаться на каких-то данных из прошлого вот но здесь есть другой нюанс в том что наверное нам нужно еще показывать какие-то более свежий баннеры какие-то может быть сезонный что-то типа скажем если сейчас новый год и я хочу там купить елку то она мне будет нужна там через месяц уже то есть тут наверно может напроситься щелкать 1 кредит от на модель которая будет вот в эту общую ранжиру ющий выдачу давать какие-то сезонные штуки он сначала сказал так мы на одной обучаемся на другой применяем модель это было его первое предложение о том как избавиться от я буду иметь другой но вот этот вопрос а как для 2 на 2 будет переходить раз ты сказал что мы будем на одной выборки божественное применяться ну хорошо допустим не возникнет когда клуб а ты про обучать уборку я не не запомнил'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `41:06` — Деление обучающей выборки ---
window: 41:06 .. 47:38
recognition_status: single (1 items)

ITEM #16
  interviewer_question: time=00:41:06 text='как мы будем ее разделять на то на чем учиться на чем проверять то есть я я'
  candidate_answer: time=00:41:13 text='решила хорошо я уйду обратно к что скачать уборка мы четыре года на это как мы до проверяем вот посмотрите это какая минут и 25 минут из 37 то есть и я вы меня зовут я думаю здесь если мы взяли ампул документов которые мы используем для обучения да а как мы его взяли на маниле что у нас было какие клики какие баннеры какие пользователи вот это все заморозили такой snapshot получили нашей социальной сети с рекламными штуками а проверились на чем дожди в оффлайне в оффлайне мы можем проверяться на том был 1 часть этого snapshot а то есть мы поди побили там на train ted как вопрос хороший здесь нужна стратегия такая чтобы наверное разные пользователи разные баннеры они разошлись по 30 тесту то есть не было такого что один пользователь он кликнул на два баннера и там один попал в трендовых тест кажется что самым надежным способом будет бить именно по пользователям то есть у нас есть пол пользователей на которых мы обучались по у пользователей на которых мы будем оценивать модель так как будешь применить в плане ты обучил модель так ты и вышли к тем пользователям которые были в обучающей выборке ну да я будешь в том числе они же то есть то есть ты сейчас механизм разбиение обучающие эволюционной выборки отделяет от того как то реальности будешь применять модель корректный вопрос некорректно ну кажется что он корректно и помощью без всем что говорил в gopro будущее да все так но если он даже пошел по такой дорожке в которой там именно бьет по людям то там нужно прям плотно засесть объяснить почему вот конкретном кейсе тебе кажется что именно по людям там полезно там например потому что у нас слишком нестационарные пространство да и мы шансов хорошо вы лидировать на будущем у нас нету а так мы хотя бы локально в моменте того что то можем прогрессировать вот потом предложил как делать и не помню все людям его времени мне кажется что в данном в данном контексте это имеет смысл потому что ну вот бывают такие хитрые штуки когда мы перри обучаемся на какие-то документы на какие-то отдельные запросы кажется что типа модель не должна работать сильно хуже на тех запросах и документах которые она там увидела во время обучения но мы не должны увидеть просадки качества на новых поэтому вот я считаю что вот именно такое разбиение на имеет смысл то есть мы берем так что у нас straight с между собой пользователями не пересекаются а получается ли следует ли из этого что у нас может так быть что в трене у нас пользователь из июля а в тесте из июня быть такой может можем ну типа можно развивать и по времени со временем но это звучит даже более логично но типа нет смысла предсказывать прошлое взяли конечно мы можем побить типа пользователем и по времени ну и еще нужно смотреть на сезонность то есть если например у нас в тесте было лет в 3 не было лето в тесте новый год то наверное это не очень хорошее разбиение потому что новый год обычно покупают совсем другие вещи что я не хочу разбивать именно по времени потому что мы на другой сезон попадем возможно как ты ты можешь учесть учесть то что мы не попадем у другой сезон то взять типа июнь и июль как-то сезонные признаки учитесь это хорошая идея мы можем так учитывать но у нас сами документы уже будут сильно разделяться на типа летние и зимние ты же это выехать я бы хотел чтобы наша модель обучалась на то есть она она видела и те и те и те кто тебе мешает как сделать то есть нам нужно v-train насыпать такие данные чтобы они представляли там более-менее равномерно все там сезонные какие-то штуки которые нас интересуют и таким же образом насыпать их данные в тесте вы в идеале там есть у нас год тренингу тест например тогда по идее ну мы там до нее не ловим какие-то супер модные тренды которые там появились только сейчас хотя мы можно еще переобучаться во времени а вот этот год год train a god тесты ты бьешь просто по времени или по времени пользователю осознание а не продавать но тоже как мы обсудили что ты за начали предложил разбить по пользователям что в тесте одни в тренер в идеале конечно да а если год год взяли если мы сможем на собирать такие данные по времени и по пользователям чтобы у нас вообще было максимально типа отделенные друг от друга trainee тесты мы на тесте могли прям вот замирятся не боясь что мы там перри обучаемся под конкретного человека чтобы у вас был совсем другой путь так в итоге у нас мы знаем какие признаки брать мы можем чуть поподробнее обсудить особенно все признаки которые из разряда кликал покупал и прочее мы знаем как нам делить на тренд с сплит в принципе знаем как от оценивать онлайн'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

SAVE JSON: вставьте ответ в конец файла /Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/ml-system-design-senior-karpov-v1-2021-08-03/ml-system-design-senior-karpov-v1-2021-08-03.v3.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
