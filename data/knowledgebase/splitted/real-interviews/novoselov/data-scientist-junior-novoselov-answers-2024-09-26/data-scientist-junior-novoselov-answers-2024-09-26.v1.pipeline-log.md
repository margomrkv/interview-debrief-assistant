<!-- PIPELINE_MANIFEST
{
  "version": 1,
  "basename": "data-scientist-junior-novoselov-answers-2024-09-26",
  "transcript_folder": "transcripts/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26",
  "source_id": "data_scientist_junior_novoselov_answers_2024_09_26",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 21:27:57 +0200",
  "updated_at": "2026-05-20 21:34:51 +0200",
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
    "json": "splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.json",
    "xlsx": "splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.xlsx",
    "validation_report_md": "splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.validation-report.md",
    "pipeline_log_md": "splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/timecodes.txt",
        "ru",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 21:27:57 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 2.0,
      "notes": null,
      "finished_at": "2026-05-20 21:34:51 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 21:34:51 +0200"
    }
  ]
}
-->

# Pipeline log v1

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26`
- **Source ID:** `data_scientist_junior_novoselov_answers_2024_09_26`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 21:27:57 +0200
- **Last updated:** 2026-05-20 21:34:51 +0200

Фильтр в IDE: `*data-scientist-junior-novoselov-answers-2024-09-26.v1*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/timecodes.txt`<br>`ru`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.pipeline-log.md` | — | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.xlsx` | 2.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.validation-report.md` | 1.0s | completed |

## Artifacts (this version)

- **json:** `splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.json`
- **xlsx:** `splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.xlsx`
- **validation_report_md:** `splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.validation-report.md`
- **pipeline_log_md:** `splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.pipeline-log.md`

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
SOURCE_ID: data_scientist_junior_novoselov_answers_2024_09_26
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26
INTERVIEW_LANGUAGE: ru
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00] сейчас я буду разбирать реальное
[00:01] собеседование на позицию Data scientist
[00:03] уровня midle мы посмотрим все вопросы
[00:05] которые задавали на этом собеседовании и
[00:07] то как правильно на них отвечать погнали
[00:10] получается в целом сегментом звука речи
[00:12] ты не работал А да я не работал я в
[00:16] принципе да и сказал об этом как мы
[00:18] видим у этого человека справа открыто
[00:20] собеседование а слева у него открыта
[00:22] Легенда которую он читает соответственно
[00:24] когда его спрашивают про его опыт Я
[00:25] советую делать так же но только в случае
[00:28] если вы накручивает опыт А это
[00:32] плохо и начать собеседование они решили
[00:35] с вопросов по питону как правило на
[00:36] позицию дата саста по питону спрашивают
[00:39] совсем уж базовые вещи и самое сложное
[00:41] что я видел это спросили про
[00:42] асинхронность Но в данном случае
[00:44] спрашивают декораторы декораторы это
[00:46] такие обёртки над функциями которые
[00:48] позволяют выполнять какой-либо код до
[00:50] или после вызова этой функции но вопро а
[00:53] Кая
[00:58] биоте похвастаться опять же пока пока не
[01:01] могу вот только начал вообще есть всего
[01:03] три библиотеки для написания
[01:07] нейронокс чаще всего используются пайтор
[01:10] Если вы хотите работать в компании где
[01:12] занимаются Нерон то лучше его выучить А
[01:15] вот Tor Flow и caros используются очень
[01:18] редко поэтому их в принципе можно не
[01:20] учить и конечно есть огромное количество
[01:23] вспомогательных библиотек Но их так
[01:25] много что в этом видео мы не будем их
[01:27] разбирать Вы не брали никакие модели там
[01:30] я не знаю из общего доступа скажем там с
[01:32] гин фейса и условно не пробовали как-то
[01:34] до обучать например ну тут понятно к
[01:37] чему он клонит Скорее всего в компании
[01:39] занимаются нейронка И им нужен человек
[01:41] который будет их писать но к сожалению у
[01:44] ученика пока что таких знаний нет
[01:46] поэтому они перешли обратно к вопросам
[01:48] по питону заче чи достав вже думаю почти
[01:51] все кто смотрит это видео наизусть
[01:52] выучили этот вопрос они отличаются тем
[01:54] что лист - Это изменяемый тип данных а
[01:57] tuple - это неизменяемый тип данных и в
[02:00] лист можно добавлять элементы удалять
[02:02] элементы а ВЛ просто его нельзя не
[02:06] добавлять не удалять В общем Ну зато тюл
[02:08] быстрее смотри если Ты создаёшь лист
[02:13] называем его А и он состоит из трх
[02:15] элементов о 2 и 3 и затем
[02:22] присваивает в B изменяешь последний
[02:25] элемент то что ты получишь при выводе А
[02:27] И на самом делене все реализованы через
[02:30] ссылки и если мы сделаем одну переменную
[02:33] которая указывает на изменяемый тип
[02:35] данных и присвоил это значение другой
[02:37] переменной и изменим этот объект Через
[02:39] Первую переменную то во второй
[02:41] переменной будет уже изменённый объект
[02:44] потому что мы двумя переменными
[02:45] указывали на один и тот же объект А вот
[02:47] если мы сделаем копию этого объекта и
[02:49] присвоил Его второй переменной то уже
[02:51] ничего меняться не будет потому что мы
[02:53] сделали как бы отдельный объект и это
[02:56] уже две разные переменные короче на
[02:58] самом деле это несложно и кто это не
[03:00] понимает то записывайтесь Кстати куда
[03:02] дорогие друзья если вы устали от курсов
[03:04] И хотите устроиться на работу как можно
[03:06] скорее то я вам предлагаю нашу программу
[03:09] офер под ключ и важно понимать что эта
[03:11] программа отличается от всех курсов
[03:14] которые вы проходили Дело в том что
[03:15] проходя эту программу мы не будем вас
[03:17] обучать вы будете обучаться сами но при
[03:20] этом у вас будет личный наставник
[03:23] который будет выдавать вам все задания
[03:25] будет проверять ваш Прогресс который
[03:27] будет помогать вам с резюме с легендой и
[03:29] с Совсем Совсем Совсем до того момента
[03:32] пока вы не устроитесь на работу и не
[03:34] пройдёте испытательный срок это важно мы
[03:36] будем работать с вами пока вы не
[03:38] устроитесь на работу в среднем наши
[03:40] ученики устраиваются на работу за 2-3
[03:42] месяца и сразу на уровень midle если вам
[03:45] Интересно как это возможно то более
[03:47] подробно я рассказываю Вот где-то вот в
[03:49] этом вот видео записывайтесь ссылка
[03:51] будет в описании В чём ча Панда Если вы
[03:55] проходите собеседование на дата
[03:56] сайентиста то Будьте уверены что вас
[03:58] попросят написать что-нибудь на пансе
[04:00] либо нам пае Дело в том что знания этих
[04:03] библиотек даже важнее чем умение строить
[04:05] ML модельки потому что это напрямую как
[04:08] бы работа с данными и с данными вам
[04:10] придётся работать гораздо больше чем
[04:12] строить какие-либо модели Например у
[04:14] датафрейма в пансе есть такой метод Log
[04:17] Он позволяет находить элемент по индексу
[04:19] и по названию столбца есть также его
[04:22] альтернатива - это метод ilog он также
[04:24] может находить элементы но уже не по
[04:26] названию индекса и названию столбца А по
[04:29] их номеру собственно в этом вся и
[04:31] разница Кстати на любом собеседовани на
[04:33] дата сайентиста Будьте готовы к тому что
[04:35] вас просят написать что-нибудь на пансе
[04:38] либо на нампа дело в том что это две
[04:40] основные библиотеки используемые для
[04:42] работы с данными А работать с данными
[04:44] вам придётся гораздо больше чем строить
[04:46] какие-либо ML модельки Какие в целом ты
[04:48] ещ знаешь метрики для зада класификации
[04:51] Тори
[04:54] Моть Ох это прям жирный вопрос поэтому
[04:57] Давайте ребят наливайте чай и
[04:59] Возвращайтесь а самая базовая простая А
[05:03] давайте начнём с метрик по классификации
[05:04] и конечно самая простая из них - это
[05:06] акураси Это просто доля совпадений по
[05:08] всем классам но эта Метрика она
[05:11] неустойчива к дисбалансу классов то есть
[05:13] если в вашем наборе данных одного класса
[05:15] значительно больше чем другого то эта
[05:17] Метрика будет показывать такой не очень
[05:19] результат точнее она будет неоправданно
[05:22] большая это в принципе Даля всех верно
[05:25] положительных результатов всех в целом
[05:27] Метрика неплохая но очень редко
[05:29] используемое потому что в случае
[05:31] дисбаланса
[05:33] классов плохо не отображает качество
[05:35] действительно поэтому сразу стоит
[05:37] перейти к лу следующая Метрика - это
[05:40] prision и она обозначает долю Угадай
[05:43] ответов положительного класса из всех
[05:45] положительных и в пару с ней обычно идёт
[05:47] Метрика recol то есть они используются
[05:49] как бы вдвоём и она обозначает долю
[05:51] объектов положительного класса из всех
[05:54] что мы предсказали положительными и
[05:56] имейте в виду что это две разные метрики
[05:58] и постарайтесь их когда не путать и одна
[06:01] Метрика используется в одном случае а
[06:02] другая в другом Давайте разберём на
[06:04] реальных каких-то примерах Например если
[06:06] Наша задача предсказать является человек
[06:08] террористом или нет то логичнее
[06:10] использовать prision Потому что так хоть
[06:12] мы и поймаем большее количество людей но
[06:14] зато мы поймаем всех террористов А если
[06:17] Наша задача состоит в том чтобы казнить
[06:19] всех террористов из тех что мы поймали
[06:21] то логичнее использовать рекол чтобы
[06:23] случайно не казнить какого-то
[06:25] невиновного
[06:27] человека всех истинных из результатов
[06:30] правильных среди всех положительных
[06:32] результатов То есть это истинно
[06:34] правильных только среди истинно
[06:37] правильных и
[06:39] отрицательно да да ложно негативных
[06:41] следующая важная Метрика - это F1 мера и
[06:44] это средне гармоническая между ном и
[06:46] рело используется она тогда когда нам
[06:48] нужно максимизировать и prision и рекол
[06:51] А если случилось так что в вашей задаче
[06:53] важен и prision и recol но recol как бы
[06:56] важнее то тогда мы сможем использовать F
[06:59] бета меру она так называется потому что
[07:01] туда входит коэффициент бета который и
[07:04] регулирует важность
[07:10] пренадлежности от того важнее нам
[07:12] precision или важнее нам recol и как вы
[07:15] можете видеть при бета равно единице F
[07:17] бета мера превращается в F1 меру Кстати
[07:20] на собеседованиях часто спрашивают
[07:22] Почему используется именно средне
[07:23] гармоническая а не например средне
[07:25] арифметическая либо средне
[07:27] геометрическая В общем ответ таков а
[07:29] например в случае среднего
[07:31] арифметического при стиже неи равном
[07:33] единице а реко равным нулю а значение
[07:36] получается ну средние 0,5 И на самом
[07:39] деле эта ситуация нас не устраивает
[07:41] Потому что при Жени равном единице а
[07:44] реко равном нулю классификация
[07:46] получается вырожденная то же самое
[07:48] получится если предсказать все объекты
[07:50] одним классом то prion получится один а
[07:53] recol ноль И наоборот если мы предскажет
[07:55] хотя бы один элемент но правильно тогда
[07:57] рекол будет единица А prision будет
[07:59] равен нулю и средняя получится 0,5 И на
[08:02] самом деле нас это не устраивает Мы
[08:04] хотим чтобы а Метрика обращалась в ноль
[08:07] в случае если либо prision либо recol
[08:10] равен нулю а в единицу только в том
[08:12] случае если обе метрики равны единице
[08:15] собственно поэтому и используется
[08:16] средняя гармоническая - это это Метрика
[08:20] которая в целом отражает способность
[08:22] модели различать положительно тение
[08:24] класса строится в орке PR PR
[08:29] такое наконец Пятая самая часто
[08:32] используемая Метрика для классификации -
[08:34] это Ro и она на самом деле очень важная
[08:37] и очень уникально Дело в том что многие
[08:40] модели классификации они выдают не сразу
[08:43] класс не сразу там метку класса ноль
[08:45] либо один Да они выдают вероятность и
[08:47] эту вероятность уже Мы потом Превращаем
[08:49] в класс выбирая какой-либо порог
[08:52] отсечения вероятности Например если
[08:54] поставить этот порог равным 0,5 тогда
[08:56] все объекты которые а имеют вероятность
[08:59] больше чем 0,5 они обращаются в первый
[09:02] класс А те что меньше они в нулевой
[09:04] класс идут это называется порог
[09:06] вероятности и не всегда этот порог равен
[09:08] 0,5 может так получиться что вы
[09:11] построите такую модель при которой
[09:13] оптимальная классификация получается при
[09:15] пороге равном 0,9 например либо 01 Это
[09:19] зависит от модели от задачи от ваших
[09:21] данных Короче от многих факторов Поэтому
[09:24] чтобы получить хорошую классификацию нам
[09:26] Кроме того что нужно построить модель
[09:27] так ещё и нужно подобрать минимальный
[09:29] порог вероятности и потом уже считать
[09:31] все метрики Все метрики кроме рока аука
[09:34] потому что рока аук можно считать сразу
[09:36] на вероятностях которая выдаёт модель и
[09:39] это очень круто Rock даёт агрегированный
[09:42] оценку по всем порогам как бы которые
[09:44] только есть и это его особенность И
[09:46] именно поэтому его используют потому что
[09:48] после того как вы использовали
[09:49] классификацию можно сразу оценить модель
[09:51] рока уком а не подбирать порог и считать
[09:54] Там prision recol и так далее Это быстро
[09:56] это удобно и как правило модели которые
[09:59] имеют больший ро аук они имеют больши и
[10:02] другие метрики типа accur и precision и
[10:04] recol ещё часто спрашивают как считается
[10:06] Ro аук но про это я сейчас рассказывать
[10:09] не буду потому что там целая теория и
[10:11] более подробно Вы можете посмотреть это
[10:12] на каком-нибудь другом канале например
[10:14] Stat Quest Мне очень нравится этот канал
[10:16] потому что там очень коротко и понятно
[10:18] всё объясняется и очень простым языком
[10:20] но к сожалению на английском с
[10:22] классификацией Мы закончили Давайте
[10:23] теперь коротко разберём основные метрики
[10:25] для регрессии Первая - это Метрика mse
[10:28] Она считает средне квадратичное
[10:30] отклонение ваших предсказаний на самом
[10:31] деле это крутая Метрика потому что она
[10:33] может использоваться как Лос функция то
[10:36] есть мы можем сразу оптимизировать
[10:37] метрику которую мы считаем Это очень
[10:40] круто это всё равно что в классификации
[10:43] Мы бы могли напрямую оптимизировать рок
[10:45] аук но это невозможно кстати Напишите
[10:48] Почему также есть Метрика мае Она
[10:50] считает уже не среднее квадратичное
[10:52] отклонение а абсолютная и к сожалению её
[10:55] мы уже не можем использовать как Лос
[10:58] функцию но если честно конечно может
[11:01] если использовать методы приближённого
[11:02] вычисления градиента как например в
[11:04] пайта арче но как бы чисто математически
[11:07] нельзя третья популярная Метрика - это
[11:09] коэффициент детерминации R к она равна
[11:12] единице Когда наши предсказания 100%
[11:14] совпадают с ожидаемыми и она равна нулю
[11:18] Когда наши предсказание констант И чем
[11:20] ближе это значение к единице тем больше
[11:23] корреляция между нашими ответами и
[11:25] реальными значениями переменных также
[11:28] иногда говорят что это э Метрика
[11:29] обозначает какая доля дисперсии таргета
[11:32] объяснима моделью и если вам это понятно
[11:34] То я вас поздравляю недостатком R
[11:36] квадрата является то что её значение
[11:38] увеличивается Точнее не уменьшается при
[11:41] добавлении в модель новых фичей даже
[11:43] если эти фичи полностью бесполезные
[11:45] Поэтому при помощи этой метрики нельзя
[11:47] сравнивать две модели у которых разное
[11:49] количество фичей конечно в регрессии
[11:51] есть и другие популярные метрики Но на
[11:53] них мы не будем останавливаться Итак
[11:56] дисбаланс классов у вас была проблема
[11:58] недостатка данных или была проблема
[12:00] наоборот слишком переизбытка данных Я не
[12:02] знаю сталкивались Вы в целом на рабочем
[12:04] Ну в рабочем моменте дисбаланс классов -
[12:06] это явление когда в обучающей выборке
[12:08] одного класса сильно больше чем другого
[12:10] и соответственно модель больше видит
[12:12] примеров одного класса и обучается лучше
[12:14] на нём чем На классах другого класса и
[12:17] типа это проблема но вопрос в том как с
[12:20] ней бороться ответ может Вас удивить
[12:23] никак Дело в том что разные методы
[12:25] сокращения выборки Либо наоборот симпли
[12:28] выборки делают ваши данные менее
[12:30] похожими на те что будут встречаться в
[12:32] реальной жизни поэтому модели обученные
[12:35] на Таких данных будут на самом деле хуже
[12:37] хоть могут и показывать какое-то более
[12:39] высокое качество на тесте Конечно если у
[12:42] Вас например есть 1.000 примеров
[12:43] нулевого класса и всего 10 примеров
[12:45] первого класса то логично выкинуть
[12:47] какую-то часть примеров нулевого класса
[12:50] чтобы ваша какая-нибудь Лог регрессия
[12:52] вообще обучила но будьте внимательны
[12:54] Потому что при этом вы теряете важную
[12:55] информацию которая хранилась в выкину
[12:58] объектах также часто говорят про веса
[13:00] классов Но во-первых это есть не во всех
[13:02] моделях А во-вторых это полная шляпа
[13:05] потому что изменение весов классов
[13:07] равносильно изменению порога отсечения
[13:09] вероятности про который мы с вами
[13:11] говорили ранее и вы можете проверить это
[13:13] самостоятельно то есть никакого
[13:14] физического реально прикладного смысла в
[13:16] том чтобы менять веса классов просто не
[13:17] существует вместо этого вы можете просто
[13:20] поменять порог вероятности у а ваших
[13:22] результатов которые уже выдаст модель
[13:25] короче лучший выход этой ситуации - это
[13:27] собрать ещё данных чтобы классов было
[13:29] примерно поровну Ну или если не
[13:30] получается выбрать модель которая
[13:32] нормально обучится на на данных с
[13:34] дисбалансом класса что есть переобучение
[13:38] переобучение - это когда модель слишком
[13:40] сильно настраивается на обучающую
[13:42] выборку учится слишком хорошо её
[13:44] предсказывать А на тестовой показывает
[13:46] результаты всё хуже и хуже и хуже С
[13:48] какими типами нейронных сетей Ты знаком
[13:51] Ну вот наконец-то пошли вопросы по
[13:53] нейронка в этом видео мы не будем
[13:55] подробно разбирать все архитектуры но
[13:57] основные Мы конечно же разберём кра и
[13:59] первый важный вид нейронокс вязаные сети
[14:02] то есть куча разных линейных слоёв с
[14:05] функцией активации на конце и тут Важно
[14:07] зачем нужна функция активации Потому что
[14:10] если её убрать то не имеет никакого
[14:12] значения у вас 100 линейных слоёв либо
[14:15] Один потому что кто изучал математику в
[14:17] школе знает что Линейная функция от
[14:19] линейных функций равна линейной функции
[14:22] функция активации это некая нелинейность
[14:24] которая добавляется к выходу каждого
[14:25] слоя и это просто очень-очень важно
[14:28] потому что ЕС если бы этой активации не
[14:30] было тогда не было бы никакого смысла
[14:32] добавлять новые слои Потому что если Вы
[14:34] хорошо изучали алгебру в школе то
[14:35] узнаете что Линейная комбинация от
[14:37] линейных комбинаций равна линейной
[14:39] комбинации то есть линейной функции
[14:41] поэтому нет никакой разницы у вас один
[14:43] линейный слой либо их тысяча если нет
[14:45] функции активации то нейронка обучится
[14:47] совершенно одинаково второй тип
[14:49] нейронных сетей - это свёрточные сети
[14:51] используются они в основном для работе с
[14:54] изображениями но с текстами также иногда
[14:56] используются и называются они так потому
[14:58] что там есть специальные свёрточные слои
[15:00] и важная особенность этих нейронокс в
[15:03] том что они работают достаточно быстро и
[15:05] хорошо параллелям на процессоре либо на
[15:08] видеокарте а недостаток свёрточные
[15:10] нейронных сетей в том то что функция
[15:12] свёртки а теряет много Важной информации
[15:15] третий важный вид - это рекуррентные
[15:17] нейронные сети или рнн вот они чаще
[15:20] всего используются именно с текстами и
[15:22] их особенность заключается в том то что
[15:24] вот эти блоки рекуррентных сетей у них
[15:26] вход и выходы абсолютно одинаковые и
[15:29] соответственно Градиент прогоняет через
[15:31] один и тот же блок много раз собственно
[15:34] поэтому они называются рекуррентными в
[15:36] частности можно взять очень популярную
[15:37] архитектуру lstm это long short term
[15:41] Memory вроде она переводится и её прикол
[15:44] в том то что вот когда мы обучаем на
[15:46] тексте мы как бы слово за словом да
[15:48] скармливать Этой нейронки и хотим там
[15:50] предсказать следующее слово и вот прикол
[15:53] этой сети в том то что она не просто
[15:54] смотрит на каждое слово по отдельности
[15:56] она ещё запоминает контекст и в этом её
[15:59] особенность то есть получив на вход
[16:01] последнее слово она всё ещё помнит
[16:03] что-то о том что там было в самом начале
[16:06] предложения из недостатков рекуррентные
[16:08] сети работают Достаточно долго и их
[16:10] нельзя распараллелить на процессоре Ну и
[16:12] самый важный в настоящее время тип
[16:15] нейронокс нае на трансформерах они
[16:18] используются и в видео и в текстах и в
[16:20] картинках в общем везде и на них именно
[16:23] на них построены чат gpt berd Там и
[16:26] прочие модели которые сейчас просто
[16:28] хайпят особенность архитектуры
[16:29] Трансформеров в том что там используется
[16:31] механизм Attention то есть Он позволяет
[16:33] А Мало того что учитывать контекст так
[16:36] ещё и он хорошо как бы параллели на
[16:38] процессорах и работает очень быстро
[16:40] поэтому Трансформеры сейчас на таком
[16:43] пике подъёме В общем работает очень
[16:44] хорошо Но вообще есть много разных
[16:46] других архитектур типа диффузионные сети
[16:48] Ганы а там байесовские нейронные сети и
[16:52] когда вот эти все типы изучают идут
[16:54] прямо голопоп и соответственно изучают
[16:56] плохо поэтому нейронки - это такая
[16:58] отдель отдель прямо вот если вы хотите
[17:00] заниматься нейронка то вы должны именно
[17:03] их учить и только ими заниматься и
[17:05] забить на классический ме практически
[17:07] полностью есть задача то биш перевода
[17:12] речи в текст Ну грубо говоря ты берёшь
[17:15] возьмём тот же самый у телеграма есть
[17:18] возможность записи аудиосообщений у тебя
[17:20] будет автоматическое транскрибирование
[17:21] этого текста Каким образом ты бы
[17:23] подготовил аудиоданные для того чтобы
[17:26] начать проводить обучение интересная
[17:29] задача на тему нейронокс водится к тому
[17:31] чтобы правильно очистить текстовые
[17:33] данные и голосовые данные Давайте начнём
[17:35] с текстовых в текстовых данных очевидно
[17:37] нужно исправить все орфографические
[17:39] ошибки расставить все знаки припинания
[17:41] убрать разные лишние символы Да которые
[17:44] там могут встречаться в общем убрать все
[17:45] аномалии это называется очистить эти
[17:47] данные короче провести полную очистку
[17:49] данных это можно сделать как и вручную
[17:51] так и при помощи других
[17:54] нейронокс нужно тоже обработать то есть
[17:57] удалить шумы нормализовать звуковую
[17:59] дорожку то есть чтобы не было громких и
[18:02] тихих звуков главное учитывать что с
[18:04] входными данными то есть звуком Вы
[18:06] можете делать только те изменения
[18:07] которые же будете делать на проде и вот
[18:10] в данной конкретной задаче с телеграмом
[18:12] применять какую-то Нерон для очистки
[18:14] звука просто нецелесообразно потому что
[18:16] ну прикиньте Вот вы записываете
[18:18] голосовое жмёт потом его а чтобы
[18:20] транскрибировать и вы ждёте пока там на
[18:23] сервере у телеграма прогони какая-то
[18:25] нейронка для того чтобы прогнать потом
[18:28] ещё Чере вашу Нейрон Да перевода и уже
[18:30] выдать результат Короче если это
[18:32] работает долго то это будет просто
[18:34] неэффективно и всегда учитывайте что
[18:36] изменения входных данных Вы можете
[18:38] делать только те что и будете делать на
[18:40] проде В каких-то задачах это Окей в
[18:42] каких-то Не окей а И кстати я ещё забыл
[18:44] есть такая штука Как частота
[18:45] дискретизации или дискретизации в общем
[18:48] я не занимаюсь музыкой Но если что её
[18:51] тоже нужно вроде как бы выровнить знаешь
[18:53] что такое
[18:55] дискретизации затрудняюсь ответь блин
[18:58] Чувак ну зачем у него это спрашивает Ну
[19:00] видно же что он не шарит Ты знаком с
[19:03] понятием
[19:05] гам А я знаю что такое Гра Да ладно я
[19:08] реально знаю Гра - это наборы слов То
[19:11] есть Двойки тройки Там и так далее слов
[19:13] а которые нужны для обучения нейронокс
[19:17] это могут быть как и просто буквы так и
[19:20] наборы букв в общем неважно Это
[19:23] называется игра а языковые модели в
[19:26] каком-то в какой-то мере может быть знае
[19:29] что-нибудь про ни Ну тоже Видимо да да
[19:32] да Ну и дальше он пошл спрашивать
[19:34] вопросы про Нерон которые наш герой к
[19:36] сожалению не выучил С Трансформерами
[19:39] тоже пря совсем мимо Да с Трансформерами
[19:44] архитектуры алгоритм внимания тоже не
[19:46] знаешь да
[19:49] Нам короче вот такое вот собеседование
[19:51] если вам интересно полная версия то
[19:53] ссылочка будет в описании и как
[19:55] результат к сожалению наш герой его не
[19:57] прол из того что он плохо выучил ни
[20:00] ронки но зато на следующем собеседовании
[20:02] он получил офер на 300.000 руб в месяц и
[20:06] хорошо что он это собеседование не
[20:07] прошёл потому что здесь была вилка
[20:08] меньше такие вот дела друзья так что
[20:10] записывайтесь на программу офер подключ
[20:12] и мы обязательно вас обучим и выбьем вам
[20:14] офер который будет в два или в полтора
[20:17] раза больше чем тот который вы можете
[20:19] получить сами а также обязательно
[20:21] подпишитесь на все Мои соцсети чтобы не
[20:23] пропускать новости и анонсы и первым
[20:25] узнавать о выходе новых собеседований
[20:27] Желаю всем жирных офферов Друзья всем
[20:29] пока
[20:32] [музыка]

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
Write JSON only to: splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.json

FORBIDDEN on step 2:
- Read, copy, merge, or patch any prior qa-split JSON in this interview folder
  (e.g. data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.json, v2, ... except the target path above).
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
Save JSON to: splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.json \
    --video transcripts/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.json --out splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.qa-split.json \
    --video transcripts/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/video.md \
    --tolerance 120 \
    --out splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.validation-report.md

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
video.md: transcripts/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/video.md

--- CHAPTER `00:31` — Что такое декоратор? ---
window: 00:31 .. 00:51
recognition_status: multiple (2 items)

ITEM #1
  interviewer_question: time=00:44 text='что такое декораторы'
  candidate_answer: time=None text=None
  reference_answer: time=00:46 text='декораторы это такие обёртки над функциями которые позволяют выполнять какой-либо код до или после вызова этой функции'
  interviewer_feedback: time=None text=None
  question_topic: Python

ITEM #2
  interviewer_question: time=00:50 text='но вопро а Кая'
  candidate_answer: time=00:58 text='биоте похвастаться опять же пока пока не могу вот только начал'
  reference_answer: time=01:03 text='вообще есть всего три библиотеки для написания нейронокс чаще всего используются пайтор Если вы хотите работать в компании где занимаются Нерон то лучше его выучить А вот Tor Flow и caros используются очень редко поэтому их в принципе можно не учить'
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `00:51` — Какие есть фреймворки для написания нейронок? ---
window: 00:51 .. 01:28
recognition_status: single (1 items)

ITEM #3
  interviewer_question: time=01:27 text='Вы не брали никакие модели там я не знаю из общего доступа скажем там с гин фейса и условно не пробовали как-то до обучать например'
  candidate_answer: time=None text=None
  reference_answer: time=None text=None
  interviewer_feedback: time=01:34 text='ну тут понятно к чему он клонит Скорее всего в компании занимаются нейронка И им нужен человек который будет их писать но к сожалению у ученика пока что таких знаний нет поэтому они перешли обратно к вопросам по питону'
  question_topic: ML

--- CHAPTER `01:28` — Опыт с HuggingFace ---
window: 01:28 .. 01:48
recognition_status: not_recognized (0 items)

(no items extracted)
--- CHAPTER `01:48` — В чём отличие list от tuple? ---
window: 01:48 .. 02:08
recognition_status: single (1 items)

ITEM #4
  interviewer_question: time=01:48 text='заче чи достав вже'
  candidate_answer: time=None text=None
  reference_answer: time=01:54 text='они отличаются тем что лист - Это изменяемый тип данных а tuple - это неизменяемый тип данных и в лист можно добавлять элементы удалять элементы а ВЛ просто его нельзя не добавлять не удалять В общем Ну зато тюл быстрее'
  interviewer_feedback: time=None text=None
  question_topic: Python

--- CHAPTER `02:08` — Как работают ссылки в питоне ---
window: 02:08 .. 02:58
recognition_status: single (1 items)

ITEM #5
  interviewer_question: time=02:08 text='смотри если Ты создаёшь лист называем его А и он состоит из трх элементов о 2 и 3 и затем присваивает в B изменяешь последний элемент то что ты получишь при выводе А'
  candidate_answer: time=None text=None
  reference_answer: time=02:27 text='на самом делене все реализованы через ссылки и если мы сделаем одну переменную которая указывает на изменяемый тип данных и присвоил это значение другой переменной и изменим этот объект Через Первую переменную то во второй переменной будет уже изменённый объект потому что мы двумя переменными указывали на один и тот же объект А вот если мы сделаем копию этого объекта и присвоил Его второй переменной то уже ничего меняться не будет потому что мы сделали как бы отдельный объект и это уже две разные переменные'
  interviewer_feedback: time=None text=None
  question_topic: Python

--- CHAPTER `03:52` — Библиотеки для работы с данными ---
window: 03:52 .. 04:47
recognition_status: not_recognized (0 items)

(no items extracted)
--- CHAPTER `04:47` — Какие есть метрики для задачи классификации? ---
window: 04:47 .. 05:04
recognition_status: single (1 items)

ITEM #7
  interviewer_question: time=04:48 text='Какие в целом ты ещ знаешь метрики для зада класификации'
  candidate_answer: time=04:54 text='Тори Моть'
  reference_answer: time=05:03 text='самая простая из них - это акураси Это просто доля совпадений по всем классам но эта Метрика она неустойчива к дисбалансу классов то есть если в вашем наборе данных одного класса значительно больше чем другого то эта Метрика будет показывать такой не очень результат следующая Метрика - это prision и она обозначает долю угаданных ответов положительного класса из всех положительных и в пару с ней обычно идёт Метрика recol то есть они используются как бы вдвоём и она обозначает долю объектов положительного класса из всех что мы предсказали положительными следующая важная Метрика - это F1 мера и это средне гармоническая между nom и rело используется она тогда когда нам нужно максимизировать и prision и рекол это Метрика которая в целом отражает способность модели различать положительно тение класса строится в орке PR пятая самая часто используемая Метрика для классификации - это Ro и она работает потому что многие модели классификации они выдают вероятность и эту вероятность уже Мы потом Превращаем в класс выбирая какой-либо порог отсечения вероятности Rock даёт агрегированный оценку по всем порогам как бы которые только есть и это его особенность'
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `10:21` — Основные метрики для регрессии (MSE, MAE, Коэфф. детерминации) ---
window: 10:21 .. 11:54
recognition_status: single (1 items)

ITEM #8
  interviewer_question: time=10:23 text='Давайте теперь коротко разберём основные метрики для регрессии'
  candidate_answer: time=None text=None
  reference_answer: time=10:28 text='Первая - это Метрика mse Она считает средне квадратичное отклонение ваших предсказаний на самом деле это крутая Метрика потому что она может использоваться как Лос функция то есть мы можем сразу оптимизировать метрику которую мы считаем также есть Метрика мае Она считает уже не среднее квадратичное отклонение а абсолютная третья популярная Метрика - это коэффициент детерминации R к она равна единице Когда наши предсказания 100% совпадают с ожидаемыми и она равна нулю Когда наши предсказание констант недостатком R квадрата является то что её значение увеличивается Точнее не уменьшается при добавлении в модель новых фичей даже если эти фичи полностью бесполезные'
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `11:54` — Что такое дисбаланс классов? ---
window: 11:54 .. 13:35
recognition_status: multiple (2 items)

ITEM #9
  interviewer_question: time=11:56 text='у вас была проблема недостатка данных или была проблема наоборот слишком переизбытка данных Я не знаю сталкивались Вы в целом на рабочем'
  candidate_answer: time=None text=None
  reference_answer: time=12:23 text='ответ может Вас удивить никак Дело в том что разные методы сокращения выборки Либо наоборот симпли выборки делают ваши данные менее похожими на те что будут встречаться в реальной жизни поэтому модели обученные на Таких данных будут на самом деле хуже хоть могут и показывать какое-то более высокое качество на тесте короче лучший выход этой ситуации - это собрать ещё данных чтобы классов было примерно поровну'
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #10
  interviewer_question: time=13:34 text='что есть переобучение'
  candidate_answer: time=None text=None
  reference_answer: time=13:38 text='переобучение - это когда модель слишком сильно настраивается на обучающую выборку учится слишком хорошо её предсказывать А на тестовой показывает результаты всё хуже и хуже и хуже'
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `13:35` — Что такое переобучение модели? ---
window: 13:35 .. 13:48
recognition_status: not_recognized (0 items)

(no items extracted)
--- CHAPTER `13:48` — Основные типы нейронных сетей ---
window: 13:48 .. 17:07
recognition_status: single (1 items)

ITEM #11
  interviewer_question: time=13:48 text='С какими типами нейронных сетей Ты знаком'
  candidate_answer: time=None text=None
  reference_answer: time=13:51 text='первый важный вид нейронокс вязаные сети то есть куча разных линейных слоёв с функцией активации на конце и тут Важно зачем нужна функция активации Потому что если её убрать то не имеет никакого значения у вас 100 линейных слоёв либо Один второй тип нейронных сетей - это свёрточные сети используются они в основном для работе с изображениями их особенность в том что они работают достаточно быстро и хорошо параллелям на процессоре либо на видеокарте третий важный вид - это рекуррентные нейронные сети или рнн вот они чаще всего используются именно с текстами и их особенность заключается в том то что вот эти блоки рекуррентных сетей у них вход и выходы абсолютно одинаковые в частности можно взять очень популярную архитектуру lstm это long short term Memory и её прикол в том то что она не просто смотрит на каждое слово по отдельности она ещё запоминает контекст и самый важный в настоящее время тип нейронокс нае на трансформерах они используются и в видео и в текстах и в картинках особенность архитектуры Трансформеров в том что там используется механизм Attention то есть Он позволяет учитывать контекст так ещё и он хорошо как бы параллели на процессорах и работает очень быстро'
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `17:07` — Как бы ты подготовил аудиоданные для обучения модели? ---
window: 17:07 .. 18:52
recognition_status: single (1 items)

ITEM #12
  interviewer_question: time=17:07 text='есть задача то биш перевода речи в текст Ну грубо говоря ты берёшь возьмём тот же самый у телеграма есть возможность записи аудиосообщений у тебя будет автоматическое транскрибирование этого текста Каким образом ты бы подготовил аудиоданные для того чтобы начать проводить обучение'
  candidate_answer: time=None text=None
  reference_answer: time=17:29 text='интересная задача на тему нейронокс водится к тому чтобы правильно очистить текстовые данные и голосовые данные в текстовых данных очевидно нужно исправить все орфографические ошибки расставить все знаки припинания убрать разные лишние символы нужно тоже обработать то есть удалить шумы нормализовать звуковую дорожку то есть чтобы не было громких и тихих звуков главное учитывать что с входными данными то есть звуком Вы можете делать только те изменения которые же будете делать на проде'
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `18:52` — Что такое частота дискретизации? (what??) ---
window: 18:52 .. 19:03
recognition_status: single (1 items)

ITEM #13
  interviewer_question: time=18:52 text='Ты знаешь что такое дискретизации'
  candidate_answer: time=18:55 text='затрудняюсь ответь'
  reference_answer: time=None text=None
  interviewer_feedback: time=18:58 text='Чувак ну зачем у него это спрашивает Ну видно же что он не шарит'
  question_topic: ML

--- CHAPTER `19:03` — Что такое N-gram? ---
window: 19:03 .. 19:23
recognition_status: single (1 items)

ITEM #14
  interviewer_question: time=19:03 text='Ты знаком с понятием гам'
  candidate_answer: time=19:07 text='А я знаю что такое Гра Да ладно я реально знаю Гра - это наборы слов То есть Двойки тройки Там и так далее слов а которые нужны для обучения нейронокс это могут быть как и просто буквы так и наборы букв в общем неважно'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `19:23` — Ещё вопросы про нейронки ---
window: 19:23 .. 19:50
recognition_status: single (1 items)

ITEM #15
  interviewer_question: time=19:23 text='языковые модели в каком-то в какой-то мере может быть знаешь что-нибудь про них'
  candidate_answer: time=19:29 text='Ну тоже Видимо да да да'
  reference_answer: time=None text=None
  interviewer_feedback: time=19:39 text='С Трансформерами тоже пря совсем мимо Да с Трансформерами архитектуры алгоритм внимания тоже не знаешь да'
  question_topic: ML

SAVE JSON: вставьте ответ в конец файла splitter_output/real-interviews/novoselov/data-scientist-junior-novoselov-answers-2024-09-26/data-scientist-junior-novoselov-answers-2024-09-26.v1.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
