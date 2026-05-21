<!-- PIPELINE_MANIFEST
{
  "version": 2,
  "basename": "data-analyst-junior-karpov-vyacheslav-2021-06-24",
  "transcript_folder": "transcripts/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24",
  "source_id": "data_analyst_junior_karpov_vyacheslav_2021_06_24",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-20 16:01:51 +0200",
  "updated_at": "2026-05-20 16:37:42 +0200",
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
    "json": "splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.qa-split.json",
    "xlsx": "splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.qa-split.xlsx",
    "validation_report_md": "splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.validation-report.md",
    "pipeline_log_md": "splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "transcripts/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/timecodes.txt",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-20 16:01:51 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-20 16:33:55 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.qa-split.json",
        "/Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 0.0,
      "notes": null,
      "finished_at": "2026-05-20 16:33:56 +0200"
    },
    {
      "id": 5,
      "name": "semantic_validation",
      "llm": true,
      "model": "claude-sonnet-4-6",
      "inputs": [],
      "outputs": [],
      "status": "ok",
      "duration_sec": 0.0,
      "notes": null,
      "finished_at": "2026-05-20 16:37:42 +0200"
    }
  ]
}
-->

# Pipeline log v2

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `transcripts/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24`
- **Source ID:** `data_analyst_junior_karpov_vyacheslav_2021_06_24`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-20 16:01:51 +0200
- **Last updated:** 2026-05-20 16:37:42 +0200

Фильтр в IDE: `*data-analyst-junior-karpov-vyacheslav-2021-06-24.v2*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `transcripts/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/timecodes.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.pipeline-log.md` | — | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.qa-split.json` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.qa-split.json`<br>`/Users/mm/projects/ds-final-project/transcripts/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/video.md` | `/Users/mm/projects/ds-final-project/splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.validation-report.md` | 0.0s | completed |
| 5 | semantic_validation | yes | claude-sonnet-4-6 | — | — | 0.0s | ok |

## Artifacts (this version)

- **json:** `splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.qa-split.json`
- **xlsx:** `splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.qa-split.xlsx`
- **validation_report_md:** `splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.validation-report.md`
- **pipeline_log_md:** `splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.pipeline-log.md`

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
7) Sidecars in the user message (e.g. TIMECODES_TXT, FEEDBACK_MD) are hints for boundaries and timestamps only. Never invent facts that are not supported by the primary transcript text.
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
SOURCE_ID: data_analyst_junior_karpov_vyacheslav_2021_06_24
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: transcripts/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00:01] тем, как перейти к каким-то техническим
[00:00:03] историям, можешь просто немного
[00:00:04] рассказать вообще, как ты как ты
[00:00:06] оказался в мире в мире анализа данных?
[00:00:08] Почему почему?
[00:00:09] Оказалось очень просто. Сейчас я учусь
[00:00:11] на третьем курсе в Этмольте
[00:00:13] информационных технологий и
[00:00:14] программирования. Вот, соответственно,
[00:00:16] на третьем курсе, в пятом семестре у
[00:00:18] меня был курс по машинному обучению. Вот
[00:00:20] до этого я вообще не знал о мире
[00:00:22] машинного обучения. Вот. Но курс мне
[00:00:24] показался настолько интересным, что я
[00:00:25] решил найти работу. Вот. успешно прошёл
[00:00:29] собеседование. Вот. И сейчас работаю
[00:00:31] начинающим датасаинтистом.
[00:00:32] [откашливается]
[00:00:33] Угу.
[00:00:33] Вот этого сном увлекался
[00:00:35] программированию, разработкой, но после
[00:00:37] курса по машинам обучения понял, что,
[00:00:39] наверное, нашёл свою область.
[00:00:41] Понятно. Понятно. А, соответственно,
[00:00:44] можешь рассказать немного вот чем вообще
[00:00:47] интересно заниматься? То есть что бы
[00:00:48] хотелось сделать?
[00:00:50] В основном мне интересно заниматься
[00:00:51] машинным обучением, вот, но в том числе
[00:00:54] статистикой, аналитикой в каком-то
[00:00:56] плане, исследовать закономерности в
[00:00:58] данных, какие-то инсайты доставать, вот,
[00:01:01] и так далее.
[00:01:02] Угу. Понятно, понятно. Ну, то есть такая
[00:01:04] аналитика
[00:01:06] by машинное обучение,
[00:01:07] можно так сказать. Угу.
[00:01:09] О'кей. Хорошо, хорошо. Слушай, ну давай
[00:01:11] тогда, раз такое дело, со статистики
[00:01:12] начнём, как вообще у тебя с мастатом?
[00:01:15] Ну, с мастатом нормально. У меня был
[00:01:16] курс базовый по массо статистике на
[00:01:18] втором курсе.
[00:01:19] Угу. Угу.
[00:01:20] Вот. Но не то, чтобы был слишком
[00:01:22] профильный. Вот скорее у меня уклонны
[00:01:24] машины обучения. Вот.
[00:01:26] Понятно, понятно. Хорошо. Ну давай с
[00:01:28] базовых вещей. Вот можешь рассказать,
[00:01:30] что такое Pvue и зачем оно нужно? А Pvue
[00:01:33] - это уровень значимости.
[00:01:36] Вот говоря, а приведу просто пример, так
[00:01:39] будет проще объяснить. Вот, допустим, у
[00:01:41] нас есть некоторые утверждения, вот, и
[00:01:44] есть некоторые гипотеза, которую мы
[00:01:45] хотим проверить. Угу.
[00:01:47] И, соответственно, мы выдвигаем нулевую
[00:01:49] гипотезу, которая нам говорит о том,
[00:01:52] что,
[00:01:54] точнее, мы хотим найти найти или
[00:01:55] показать различие в том, что являлися
[00:01:58] является ли наша гипотеза правдой. И
[00:02:01] если она является правдой, то насколько
[00:02:03] сильно она отклоняется от истинного
[00:02:05] утверждения. Вот, соответственно, давай
[00:02:07] какой-то саж какой-нибудь, чтобы совсе
[00:02:09] заземлить какой-нибудь пример более
[00:02:10] такой реалистичный, то есть условно там
[00:02:12] проводим а тест какой-нибудь.
[00:02:15] Мм. Мм, мне больше нравится пример с
[00:02:17] монеткой приводить.
[00:02:18] Давай.
[00:02:18] Вот у нас есть частная монетка. Угу.
[00:02:21] Вот мы подкидываем её там условно, не
[00:02:23] знаю, допустим, 20 раз.
[00:02:25] Вот. И, допустим, все 20 раз выпадает
[00:02:27] орёл. Ну, понятное дело, потому что это
[00:02:29] маловероятно, но для простой пример это
[00:02:31] будет,
[00:02:31] а, нагляднее. Вот. И, соответственно,
[00:02:36] а, подбросив монетку 20 раз и видев, что
[00:02:38] это орёл, а, можно сделать такую
[00:02:41] гипотезу о том, что наша монетка
[00:02:43] является какая-то какой-то специальной.
[00:02:45] Вот. И,
[00:02:48] ну, в каком-то плане, [откашливается]
[00:02:54] ну, грубо говоря, не совсем честный.
[00:02:56] Ну, понятно, да? То есть давай давай
[00:02:58] теперь всё-таки сформулируем это вот две
[00:02:59] гипотезы. Ты уже упомянул. Есть нулевая
[00:03:00] гипотеза, есть альтернативная. Примере,
[00:03:03] как будет звучать первая, как вторая
[00:03:04] гипотеза будет звучать?
[00:03:06] Нулевая гипотезачит
[00:03:08] так, то, что наша монетка является
[00:03:10] честной и ничего в ней такого особенного
[00:03:12] нет.
[00:03:12] Угу. Соответственно, первая гипо, ну,
[00:03:14] альтернативная гипотеза звучит так, то
[00:03:16] что наша монетка специальная, и,
[00:03:21] ну, я думаю, так проще будет сказать.
[00:03:22] Вот.
[00:03:23] Ну вот если всё-таки можно было бы вот
[00:03:25] как-то это более так ещё обернуть, что
[00:03:27] нулевая гипотеза звучит, что выпадение
[00:03:29] орла и решки равновероятное, в то время
[00:03:32] как альтернативная говорит, что
[00:03:34] вероятности не равны.
[00:03:35] Да, неравны. Да,
[00:03:36] ну да. О'кей, хорошо. И где же тут
[00:03:39] возникает пивели? И что это за что это
[00:03:40] такое? Почему вообще это по сути
[00:03:43] вероятность ээ данного события при том,
[00:03:46] что нулевая гипотеза будет верной.
[00:03:48] Угу.
[00:03:49] В нашем случае можем посчитать Pvue
[00:03:52] очень просто. То есть мы знаем то, что
[00:03:54] вероятность для частной монетки падения
[00:03:56] орла равна 1/2.
[00:03:59] Вот откидываем монетку 20 раз
[00:04:01] и 20 раздает орёл. Понятное дело то, что
[00:04:03] вероятность будет равна 1 / 2 степени.
[00:04:07] Ну дада.
[00:04:08] Приблизительно получается одна
[00:04:09] миллионная.
[00:04:11] Вот. И по сути это и будет значение P
[00:04:14] value. Вот. И далее на основании нашего
[00:04:16] значения Pvue мы можем посчитать,
[00:04:19] является ли наша гипотеза, ну, точнее,
[00:04:22] наш результат статистически значимым или
[00:04:24] нет. Обычно берут пятипроцентное
[00:04:27] значение уровня значимости, вот, и
[00:04:29] сравнивают его со значением Pvue. Если
[00:04:31] Pvue получается меньше, чем э,
[00:04:35] ну, 5%, то, соответственно, мы наклоняем
[00:04:38] нулевую гипотезу и принимаем
[00:04:40] альтернативную. Вот в противном случае
[00:04:41] мы принимаем нулевую гипотезу. Ну, в
[00:04:43] нашем случае будет верна альтернативная.
[00:04:46] Ты сказал, что вот PV - это по сути
[00:04:47] вероятность получить такие результаты,
[00:04:49] если нулевая гипотеза верна. А если мы,
[00:04:51] допустим, перейдём в формат уже не
[00:04:54] монетки, а более такой реалистичной
[00:04:56] истории, вот мы сравнили две группы. У
[00:04:58] нас есть две группы пользователей. У
[00:05:00] одних пользователей, допустим, там
[00:05:01] старый дизайн приложения, у других
[00:05:03] пользователей новый дизайн приложения. И
[00:05:04] мы замеряем среднее значения,
[00:05:06] соответственно, не знаю, там среднее
[00:05:08] значение в каждой группе, сколько
[00:05:10] пользователей провели время на сайте.
[00:05:13] Вот, соответственно, если твоим
[00:05:14] определением пользоваться, правда ли
[00:05:17] утверждение, что Pvue - это вероятность
[00:05:20] получить именно такое различие в средних
[00:05:22] значениях, как мы наблюдаем в наших
[00:05:23] группах, при условии верности нулевой
[00:05:25] гипотезы?
[00:05:28] М, сейчас. [откашливается]
[00:05:33] А что мы сейчас считаем за нулевую
[00:05:34] гипотезу?
[00:05:35] Что средние одинаковые.
[00:05:38] Мы, соответственно, получили, что в
[00:05:40] одной группе среднее равняется 100, а в
[00:05:41] другой 150. Правда ли сказать, что Pvue
[00:05:44] - это вероятность получить такие
[00:05:46] различия в средних при верности нулевой
[00:05:49] гипотезы?
[00:05:50] Ну да, просто верно.
[00:05:51] Угу. Давайте попробуем понять, почему
[00:05:53] это на самом деле неправильный ответ. А
[00:05:55] вот если ты вспомнишь, как обычно пили в
[00:05:57] учебниках рисуются,
[00:06:01] вот рисуется такое распределение, и там
[00:06:03] есть есть ещё односторонняя,
[00:06:04] двусторонняя гипотеза. Видел когда-нибуд
[00:06:06] такое графическое представление?
[00:06:09] Вот что там важно. Там вот как как это
[00:06:12] вообще график выглядит? Вот у нас есть
[00:06:13] вот распределение и с двух сторон у нас
[00:06:15] заштрихована какая-то зона под прямой,
[00:06:17] да?
[00:06:18] Угу.
[00:06:19] Какой мы из этого можем сделать вывод?
[00:06:21] Что PVL - это вероятность получить не
[00:06:23] такие различия, именно такие различия
[00:06:26] при нулевой гипотезе. А какие различия?
[00:06:31] М,
[00:06:33] ну вот чисто визуально смотри. условно
[00:06:35] там отрезает какой-то кусочек и дальше
[00:06:38] всё правее него. Что это означает на
[00:06:40] практике?
[00:06:42] Мм, так это означает, что
[00:06:45] сейчас
[00:06:50] это означает, что мы, когда сравниваем,
[00:06:52] допустим, средний или монетку, мы
[00:06:54] говорим, что P value - это вероятность
[00:06:55] получить такие или ещё более сильно
[00:06:57] выраженные различия, да,
[00:06:59] если верна нулевая гипотеза. Опять же,
[00:07:02] это не то, чтобы сверхкритичная вот
[00:07:05] разница, но всё-таки довольно
[00:07:07] существенная, потому что при
[00:07:08] интерпретации пивео часто действительно
[00:07:10] существует некоторая путаница. А и вот
[00:07:14] действительно сказать, что пиве - это
[00:07:15] именно прямо вот такая точечная оценка
[00:07:18] вероятности именно такого события, это,
[00:07:20] конечно, не совсем верно. То есть это
[00:07:22] такого или ещё более сильно выраженного.
[00:07:25] А, кстати, вот есть ещё двусторонние,
[00:07:26] односторонние гипотезы, они чем
[00:07:27] отличаются друг от друга?
[00:07:30] А в том, что
[00:07:33] двусторонне мы, грубо говоря, не знаем,
[00:07:35] а в какую сторону будет отклонение. Угу.
[00:07:37] Угу. И, кстати, возвращаясь к нашему
[00:07:39] предыдущему вопросу, это означает, что
[00:07:41] если мы проверяем двустороннюю гипотезу
[00:07:43] Pвео и считаем вот 05, это означает, что
[00:07:46] это вероятность получить как сильно
[00:07:48] выраженные различия в правую, в большую
[00:07:50] сторону, в одной из групп, так и на
[00:07:52] самом деле в меньшую. Вот как-то так.
[00:07:54] О'кей, хорошо. Хорошо. А ты говорил, что
[00:07:57] ты любишь пошиное обучение, аналитику.
[00:07:59] Давай прямо кейсик разберём. Вот у нас
[00:08:02] есть пользователи. Пользователь в
[00:08:04] социальной сети, я думаю, ты сам
[00:08:05] социальными сетями пользуешься, там
[00:08:07] Facebook, Контакт. А, как ты знаешь, в
[00:08:09] аналитике есть прямо вот такая, знаешь,
[00:08:12] метрика, на которую все любят молиться,
[00:08:14] вот и радоваться. Это вот удержание
[00:08:15] наших клиентов. Это некоторые чёрный
[00:08:18] retтенtion. И поэтому очень часто мы
[00:08:21] прогнозируем, мы прогнозируем, что наш
[00:08:23] пользователь, он собирается покинуть,
[00:08:26] например, нашу социальную сеть и больше
[00:08:27] никогда не пользоваться. Понимаешь
[00:08:29] задачу, да? То есть мы хотимть, что
[00:08:32] человек перестанет пользоваться, ну,
[00:08:34] допустим, Фейсбуком. Мы работаем вот
[00:08:36] аналитиками в фейсбуке, у нас есть там
[00:08:38] миллиарды пользователей, и мы хотим в
[00:08:40] каком-то мере их как-то кластеризовать.
[00:08:42] говорим, что вот эти ребята - это наши
[00:08:44] ядровые аудитории, они точно будут
[00:08:46] продолжать пользоваться нашим продуктом,
[00:08:48] а вот эти ребятки, они собираются
[00:08:50] дропнуться. Вот перед тем, как мы
[00:08:52] перейдём к какой-то там архитектуре
[00:08:54] модели и так далее, вот сначала
[00:08:56] бизнес-логика, как ты думаешь, вообще,
[00:08:57] зачем это нужно делать? Вот зачем нам в
[00:08:59] целом нужно предсказывать, что
[00:09:00] пользователь куда-то дропнутся? Но мне
[00:09:02] кажется, что если мы знаем, что какая-то
[00:09:04] определённая группа пользователей
[00:09:06] дропнутся, то, допустим, не знаю,
[00:09:07] провести какую-то маркетинговую
[00:09:08] рассылку, а с цель повысить их интерес к
[00:09:11] нашей к нашему приложению, к нашей
[00:09:13] социальной сети. Вот. И в этом плане оно
[00:09:15] может, ну, повлиять в какой-то мере, и,
[00:09:17] соответственно, уход пользователя он
[00:09:19] будет в меньшей мере, вот, чем был до
[00:09:22] этого. Ну, конечно, да, если так
[00:09:24] всё-таки ещё более явно сказать, то есть
[00:09:27] мы всё-таки живём в мире капитала, и
[00:09:30] надо понимать, что когда пользователь
[00:09:31] пользуется социальной сетью, на самом
[00:09:33] деле мы в каком-то смысле зарабатываем
[00:09:35] деньги на этом факте, да, там, например,
[00:09:37] мы показываем пользователю рекламу или
[00:09:38] он покупает там платные стикеры у нас,
[00:09:41] да, и если пользователь перестанет
[00:09:43] пользоваться нашим продуктом, ну, [смех]
[00:09:45] мы как бы просто теряем деньги, вот
[00:09:47] условно. Хорошо. можешь тогда вот
[00:09:50] рассказать, как бы ты к такой задачке
[00:09:52] подошёл. Давай вот попробуем сейчас
[00:09:54] как-то вот накидать высокоуровнево.
[00:09:59] Вот какие бы ты признаки собрал, какие
[00:10:01] бы фичи собрал, как бы ты вот вот вот
[00:10:05] end to end можешь такими крупными
[00:10:06] мазками нарисовать твой подход к решению
[00:10:09] задачи. Мы говорим: "У нас все логи
[00:10:11] есть. Допустим, мы живём в идеальном
[00:10:12] мире, где у нас там инфраструктура, всё
[00:10:14] настроено, даты, инженеры всё собрали".
[00:10:17] Соответственно, у нас есть там вот все
[00:10:18] данные. про пользователя. Хотим понять,
[00:10:22] кто дропнется, [фыркает] кто нет.
[00:10:24] М. Так, сейчас надо подумать.
[00:10:28] Сейчас признанки у нас уже о
[00:10:29] пользователях есть готовые, которы
[00:10:33] ну как бы мы предполагаем, что у нас
[00:10:35] есть максимальная свобода действия. То
[00:10:37] есть если ты скажешь собрать, сколько
[00:10:39] пользователей лайкл посты за последний
[00:10:41] год, мы как бы всё соберём. Вот. То есть
[00:10:43] вопрос технически не стоит. Вопрос, что
[00:10:45] собирать?
[00:10:49] Ну, я думаю, да, вот как разтаки такую
[00:10:51] информацию вот, допустим, о лайках либо,
[00:10:53] допустим, о времени провождения на сайте
[00:10:56] тоже могло быть полезно.
[00:10:57] Угу. Ну, если вот попробовать всё-таки
[00:11:01] теперь перевести это на язык, знаешь,
[00:11:02] такой более, э, исполнительный, если ты
[00:11:06] придёшь условно к команде датаинженеров
[00:11:08] и скажешь: "Хочу, чтобы мне выгрузили
[00:11:10] время проведения на сайте". Ну, тебя не
[00:11:12] поймут. Вот можешь прямо там сделать,
[00:11:15] например, там топ-пять фичей, которые ты
[00:11:17] хотел бы взять, топ- пять признаков
[00:11:19] максимально операционализированных,
[00:11:22] максимально понятных. То есть условно,
[00:11:23] чтобы человек тебя послушал и мог запрос
[00:11:25] в базу написать, там select сумма лайков
[00:11:29] from table, group by user ID условно.
[00:11:32] Ладно, так, пожалуй, так. А время
[00:11:35] провождения на сайте в секундах
[00:11:37] зако времени. Угу.
[00:11:41] Мм.
[00:11:42] количество лайков, совершённых
[00:11:44] пользователем.
[00:11:49] Так что ещё можно
[00:11:52] количество друзей, знакомых
[00:11:59] можно использовать какие-то
[00:12:00] географические признаки, возможно, в
[00:12:03] разных регионах лишного смысла. Да. Да.
[00:12:06] Популярность. Наша сеть имеет разную
[00:12:08] популярность. Дада. Да. Это очень,
[00:12:10] кстати, хорошая мысль, потому что,
[00:12:12] условно, если человек находится в
[00:12:14] некотором таком в ядре от этого
[00:12:16] социального графа, где все пользуются
[00:12:17] Фейсбуком, это скорее всего, да, может
[00:12:20] как-то быть связано с географией. О'кей,
[00:12:22] хорошо. Давай пока на нашем примере
[00:12:24] остановимся. Ты сказал: "Время
[00:12:26] проведения в миллисекундах". Лайки, а
[00:12:29] география и что ещё?
[00:12:31] Мм, так.
[00:12:32] А, и друзей. И друзей. Угу.
[00:12:35] Погнали. А как ты думаешь, почему просто
[00:12:39] суммарное количество лайков, условно,
[00:12:42] это на самом деле довольно плохая
[00:12:44] метрика? В чём подвох вообще суммарных
[00:12:46] метрик? Вот у нас есть пользователь, у
[00:12:48] одного 100 лайков, у другого 1.000.
[00:12:50] Почему на самом деле тут не хватает ещё
[00:12:54] очень важного уточнения?
[00:12:56] Сейчас 1.000 лайков, которые он сам
[00:12:57] ставит или которые ему ставит?
[00:12:58] Не, пока мы только те лайки, которые он
[00:13:00] сам ставит, суммируем.
[00:13:02] М. Так.
[00:13:05] Ну, смотри, ведь мы же зачем лайки
[00:13:07] собираем? Мы хотим как бы сделать вывод,
[00:13:10] что якобы первый пользователь, у
[00:13:12] которого 1000 лайков, он более вовлечён,
[00:13:13] да, в соцсет, чем второй, у которого
[00:13:15] 100. Почему на самом деле это может быть
[00:13:18] не совсем так? Что мы не учитываем, если
[00:13:21] учитываем только суммарной лайки?
[00:13:28] Подскажу, на чтобы нам нужно нормировать
[00:13:30] эти лайки, чтобы получить более
[00:13:32] интересную метрику.
[00:13:34] на количество друзей, к примеру.
[00:13:37] А если, ну, не совсем, если всё-таки
[00:13:40] даже взять, вот смотри, как бы даже если
[00:13:42] просто взять условно
[00:13:45] прямой сценарий, откуда лайк возникает?
[00:13:47] Вот человек скролит ленту, ставит лайки.
[00:13:49] То есть на что бы нам на что бы нам
[00:13:51] нормировать можно было бы?
[00:13:53] А, от количество просмотреных постов.
[00:13:54] Ну, конечно, конечно, потому что, ну,
[00:13:56] смотри, как бы просто суммарное
[00:13:58] количество лайков, на самом деле мало
[00:14:01] что говорит. Условно, если человек
[00:14:03] просмотрел миллиард постов и поставил
[00:14:06] 1.000 лайков, это не то же самое, что
[00:14:08] человек просмотрел 100 постов и поставил
[00:14:11] 100 лайков. То есть как бы получается,
[00:14:14] что у второго человека, которого лайков
[00:14:16] меньше, но условный как бы CTR,
[00:14:18] некоторая конверсия в лайк у него
[00:14:20] гораздо больше. означает, что его
[00:14:21] вовлечённость в процесс, это опять же
[00:14:24] гипотеза, но теперь у нас хотя бы есть
[00:14:26] какой-то к ней подход. О'кей? А, да, и
[00:14:30] здесь как бы важно понимать, что вот эти
[00:14:32] вот такие суммарные метрики, которые
[00:14:34] просто делают какую-то общую информацию,
[00:14:37] они вот коварны. То же самое общее время
[00:14:40] проведения на сайте. Вот если теперь
[00:14:43] просто просто мы представим, что у нас
[00:14:45] есть вот таблица с пользователями. Вот
[00:14:47] как бы ты эту метрику посчитал, ты
[00:14:49] просто взял бы, не знаю, все секунды,
[00:14:51] которые человек провёл на сайте за всю
[00:14:52] свою историю регистрации или как?
[00:14:56] Мм,
[00:14:59] не, наверное, это не очень хороший
[00:15:00] подход, потому что, допустим,
[00:15:01] пользователь может просто там, не знаю,
[00:15:02] открыть нашу социальную сеть в фоновом
[00:15:04] режиме и время будет текать. Вот,
[00:15:07] конечно, но даже сейчас, смотри, это
[00:15:09] даже меньше изол, потому что это уже
[00:15:11] совсем тяжело трекать, знаешь, там как
[00:15:13] бы вот в целом время проведения на сайте
[00:15:16] - это хорошая метрика. Давай только тоже
[00:15:18] вернёмся к предыдущей идее. Вот если
[00:15:21] лайки нам нужно было как-то нормировать
[00:15:22] и считать не просто сумму, то с временем
[00:15:24] приведения на сайте тоже как-то вот надо
[00:15:26] посчитать её немножко иначе. Вот давай
[00:15:28] просто, ну, здесь как бы, ну, вот как мы
[00:15:31] её, как мы её будем считать? Вот первый
[00:15:33] вариант, просто взять сумму
[00:15:35] время на сайте за всё время. В принципе,
[00:15:38] хорошая метрика, но опять же, если
[00:15:40] кто-то провёл 2 дня, а кто-то провёл 10
[00:15:43] лет, ну, как минимум у нас может быть
[00:15:45] человек, который просто вчера
[00:15:46] зарегистрировался
[00:15:49] и выясняется, что его время проведения
[00:15:51] на сайте очень маленькое, но просто
[00:15:52] потому, что он ещё и только вчера попал
[00:15:55] туда. Как бы нам вот это обойти
[00:15:57] препятствие? Как бы нам получить
[00:15:59] какое-то такое опять же либо
[00:16:00] нормированное, либо усреднённое какое-то
[00:16:01] значение? получить среднее значение в
[00:16:03] секундах в год, к примеру, либо в день.
[00:16:06] Ну, конечно, в день, да. Ну год - это,
[00:16:08] [смех] ну, год - это перебор. Ну, то,
[00:16:11] что человек делал год назад, условно,
[00:16:13] как бы, скорее всего уже, может быть, не
[00:16:15] так актуально. Абсолютно верно. И
[00:16:17] среднее проведение в день, опять же, уже
[00:16:21] может быть гораздо более понятнее. А
[00:16:24] один человек в среднем проводит на сайте
[00:16:26] 5 минут, а другой 15 часов. Ну,
[00:16:30] интуитивно кажется, да, что у второго
[00:16:32] человека вовлечённость она как бы
[00:16:34] получше. [фыркает] О'кей, хорошо. Ээ, я
[00:16:37] думаю, идея ясна, да? Как бы в обеих
[00:16:39] метриках мы поняли, что их надо
[00:16:40] необходимо ещё как-то как-то
[00:16:42] донормировать. Вот. Идём дальше.
[00:16:44] Количество друзей. Вот с количество
[00:16:46] друзей тоже как бы давай тоже добьём и
[00:16:49] попробуем какие-нибудь ввести всё-таки
[00:16:50] пограничные случаи. Ну, на что бы здесь
[00:16:53] тоже можно было бы как-то обратить
[00:16:55] внимание, а не просто взять условно там
[00:16:58] суммарное количество друзей.
[00:17:02] Но опять же, смотри, суммарное
[00:17:03] количество друзей чем плохо? Если
[00:17:05] человек давно ВКонтакте, у него 100
[00:17:07] друзей. Если он вчера ВКонтакте, у него
[00:17:09] ноль друзей. Получается, что как бы
[00:17:12] просто время проведения очень сильно
[00:17:13] влияет. Может быть, какую-нибудь
[00:17:15] метрику, тоже связанную с друзьями, но
[00:17:18] которая скорее показывает вовлечение в
[00:17:20] общение. Можно было, скорее,
[00:17:22] допустим, сколько новых друзей у этого
[00:17:24] человека за какой-то промежуток времени.
[00:17:26] Абсолютно верно. Абсолютно верно.
[00:17:28] Абсолютно верно. То есть суммарное
[00:17:29] количество друзей даже не так важно. Нам
[00:17:31] скорее важно понять, продолжается ли
[00:17:34] пополнение друзей у человека. И вот эта
[00:17:37] фича, поверь мне, как бы точно будет
[00:17:39] куда более предиктабл вот по своей силе,
[00:17:42] чем обычно. Супер. Смотри, три фичи
[00:17:45] собрали. Что дальше? Теперь у нас есть
[00:17:48] такая важная история. Мы хотим понять,
[00:17:50] дропнулся человек или нет. Вот как
[00:17:53] вообще понять? Это дропнулся, если он
[00:17:55] неделю не заходил или месяц или год? У
[00:17:58] нас же или Ну, самое простое - это
[00:18:00] аккаунт удалил. Но очень многие
[00:18:02] пользователи аккаунт не удаляют, они
[00:18:03] просто перестают заходить. Как нам
[00:18:05] понять, сколько времени должно пройти с
[00:18:08] последнего захода, чтобы считать, что
[00:18:10] этот человек уже, скорее всего, к нам не
[00:18:12] вернётся?
[00:18:15] А мы берём в расчёт только время.
[00:18:16] [откашливается]
[00:18:17] Что
[00:18:18] мы берём в расчёт только время, которое
[00:18:20] не заходил на сайт?
[00:18:22] Это я накидываю идеи. Вот у нас просто
[00:18:23] есть понятие. Пользователь покинул,
[00:18:26] ушёл, ну как бы вот дропнулся. Вот как
[00:18:28] мы опять же это операционализируем?
[00:18:31] Что мы вкладываем в это понятие? Я
[00:18:32] говорю, есть несколько вариантов. Вот
[00:18:35] первый можно сказать, просто удалил
[00:18:36] анкету свою, но сразу же я как бы сам
[00:18:39] себе отвечаю, это плохой вариант, потому
[00:18:41] что он, ну, много пользователей просто
[00:18:43] перестают заходить. И давай вот эту
[00:18:45] мысль разовьём. Сколько времени человек
[00:18:48] должен перестать заходить, чтобы мы
[00:18:50] считали, что он уже всё, как бы не
[00:18:51] вернётся к нам?
[00:18:56] Ну, допустим, условно 2 недели.
[00:18:58] 2 недели. А если попробовать как-нибудь
[00:19:00] сюда прикрутить какую-нибудь
[00:19:02] статистическую историю? Ну, а почему
[00:19:04] две, а почему не три? Вот,
[00:19:08] наверное, лучше рассматривать ещё
[00:19:09] предыдущую историю увлечённости.
[00:19:12] Возможно, раньше он был более активным,
[00:19:13] и сейчас его активность она спала.
[00:19:16] Вот.
[00:19:17] И учитывать эту разницу.
[00:19:19] Поясни, пожалуйста.
[00:19:23] Ну, допустим, если мы рассматриваем
[00:19:26] активность пользователя за последний
[00:19:27] год,
[00:19:28] Угу.
[00:19:28] Вот. И, к примеру, мы видим то, что он
[00:19:30] там условно проводил по 30 минут. в
[00:19:33] день.
[00:19:34] Угу.
[00:19:35] Сети. Вот. А сейчас примеры проводит по
[00:19:37] 3-5 минут.
[00:19:39] Угу. Случае его активность, ну, как
[00:19:43] минимум спала вниз.
[00:19:45] Это да. Это да. Не, ну это ты уже как бы
[00:19:47] стараешься некоторый прогноз делать. Ну
[00:19:49] смотри, ведь мы же когда хотим какую-то
[00:19:51] модельку условную там обучить, допустим,
[00:19:52] да, там какую-нибудь регрессию или
[00:19:53] какую-нибудь там нейроную сеть, неважно,
[00:19:55] что, нам бы сначала лучше подготовить
[00:19:57] какую-то выборку, а условно, где есть
[00:19:59] два класса. вот пользователи, которые
[00:20:01] дропнулись, а вот пользователи, которые
[00:20:03] не дропнулись. И, соответственно, потом
[00:20:05] мы действительно уже сможем заранее
[00:20:07] предсказывать. Вот так вот. Если я
[00:20:08] просто хочу тебя попросить, вот я тебе
[00:20:10] прихожу и говорю и ставлю тебе такое ТЗ,
[00:20:12] возьми, пожалуйста, всех пользователей,
[00:20:14] которые перестали пользоваться нашим
[00:20:16] сайтом, и посмотри, сколько они там в
[00:20:19] среднем ставили лайки за последний
[00:20:21] месяц. Вот. Да. Вот вопрос-то в том, как
[00:20:24] понять, каких пользователей нужно взять?
[00:20:27] Вот я уже говорю, возьми уже тех
[00:20:29] пользователей, которые уже отвалились.
[00:20:30] Вот как понять пользователей, которые
[00:20:31] уже отвалились? Вот ты говоришь, те, кто
[00:20:33] 2 недели не заходил, я тебя вот
[00:20:36] спрашиваю, а почему две, почему не три?
[00:20:39] Можно ли здесь как-то попробовать
[00:20:40] статистически подобраться и подумать,
[00:20:42] что можно как-то обосновать это решение?
[00:20:48] Может привести какой-нибудь аботест?
[00:20:50] Ну, совсем сложно, кстати, тоже, знаешь,
[00:20:53] в аналитике часто бывает, что без
[00:20:55] а-тестов тоже хорошо можно жить, когда
[00:20:57] особенно какие-тохоки мы выполняем. Ну,
[00:20:59] смотри, попробую тоже навести на мысль.
[00:21:01] Вот если я скажу, будем считать, что
[00:21:03] человек дропнулся, если он не заходил
[00:21:06] день вКонтакт,
[00:21:08] почему это неправильное утверждение
[00:21:10] интуитивно?
[00:21:15] Ну, потому что, допустим, у него не
[00:21:16] могло могло быть не могло быть интернета
[00:21:17] в это потому что кажется, что если
[00:21:20] человек день не заходил, это не значит,
[00:21:22] что он теперь никогда не зайдёт.
[00:21:23] Кажется, что день - это какой-то
[00:21:24] маленький промежуток, после которого,
[00:21:26] скорее всего, последует заход. А если
[00:21:29] человек год не заходил, опять же
[00:21:32] интуитивно кажется, что засчитано. Вот,
[00:21:35] скорее всего, и не зайдёт. А вот как
[00:21:38] найти золотую серединку, как найти тот
[00:21:40] промежуток, как бы, который между
[00:21:43] заходами, который действительно, скорее
[00:21:46] всего, уже является с определённой, там,
[00:21:48] скажем, девяносто пятипроцентной
[00:21:49] вероятностью
[00:21:51] последним заходом пользователя.
[00:21:54] подскажу, что у нас есть вся история
[00:21:56] предыдущих захо Ну, у нас есть
[00:21:58] Так вот, да, краски мом взять инфу о
[00:22:00] предыдущих пользователях, а тех, которые
[00:22:02] дропнулись и о тех, которые не
[00:22:03] дропнулись,
[00:22:04] и проаносировать, сколько времени они не
[00:22:07] заходили на сайт
[00:22:09] и уже отливаться от этого.
[00:22:11] Да. Да. И просто когда мы для всех
[00:22:13] пользователей посмотрели статистику их
[00:22:15] как бы
[00:22:18] разрывов в их активности сессий, можно
[00:22:20] действительно просто распределеница
[00:22:22] построить и сказать, что если
[00:22:23] пользователь не заходит на сайт 2
[00:22:25] недели, то только у 5% пользователей, у
[00:22:30] которых превышает разрыв 2 недели, есть
[00:22:32] последующие сессии. Ну это я сейчас
[00:22:34] утрирую, фантазирую, но как бы или или у
[00:22:37] 10%. И тогда нам нужно наоборот как-то
[00:22:39] подвинуть этот порог. Ну вот, да, то
[00:22:41] есть видишь, мы тоже выяснили, что,
[00:22:43] чтобы данные подготовить, сколько тут
[00:22:45] подводных камней скрывается. Ну и
[00:22:48] финальная история. Вот мы собрали наши
[00:22:50] три фичи. Вот мы, соответственно, а там,
[00:22:54] я не знаю, разметили нашу выборку на
[00:22:57] тех, кто там, а,
[00:23:00] как сказать, дропнулся, не дропнулся.
[00:23:02] Допустим, обучили какой-то
[00:23:04] классификатор. Какой классификатор ты бы
[00:23:06] хотел, кстати, здесь обучить?
[00:23:08] У нас выборка пользователя большая. Ой,
[00:23:10] у нас очень большая, да?
[00:23:13] М на трёх фичах.
[00:23:15] Не, ну это я утрирую. Ну, допустим, мы
[00:23:17] там уже сделали там больше фичей, то
[00:23:19] есть, ну, в целом, какой метод ты бы
[00:23:20] здесь применил?
[00:23:21] Не знаю, к примеру, градиентный бустинг.
[00:23:24] Ну, why not, да? Применили градиентный
[00:23:26] бустинг, обучили, провалидировали, всё
[00:23:29] работает. Ну, предсказываем уход в
[00:23:31] пользователя. Теперь аналитический
[00:23:34] вопрос: а что делать-то? Ну вот,
[00:23:37] допустим, мы предсказали, что
[00:23:38] пользователь Анатолий Карпов через
[00:23:40] неделю собирается окончательно
[00:23:43] прекратить пользоваться нашим сервисом.
[00:23:45] Вот что бы теперь с ним сделать?
[00:23:48] Можем, к примеру, отправить ему какое-то
[00:23:49] сообщение или уведомление о том, чтобы
[00:23:51] напомнить ему, что у нас есть сервис,
[00:23:53] которым может пользоваться либо как-то
[00:23:55] заинтриговать его внимание.
[00:23:58] Угу.
[00:23:59] Ну, а можешь прямо вот представь, что мы
[00:24:01] сидим на таком брейнсторме с
[00:24:03] маркетологами. Вот они говорят: "Так, а
[00:24:05] что именно? Что именно? Вот что
[00:24:06] отправляем?" Вот тут можешь прямо
[00:24:08] какое-нибудь такое финальное решение
[00:24:09] сказать? Вот что мы этому человеку
[00:24:11] отправим?
[00:24:13] Опять же, это может быть какая-то
[00:24:14] персонализированная история, что одним
[00:24:15] то, другим это. Опять же на основе их
[00:24:17] какого-то поведения. Ну вот каких-нибудь
[00:24:19] два таких самых явных сценария можешь
[00:24:21] предложить?
[00:24:34] Ну, я бы предложил чисто с головы взял,
[00:24:37] э, просто напомнить ему зайти на сайт.
[00:24:40] Вот, потому что он уже, допустим, не
[00:24:41] заходил долгие перерё у него могли быть
[00:24:43] новые сообщения потенциальные.
[00:24:45] Ну вот опять же обрати внимание, да,
[00:24:48] давай теперь эту мысль завьём. Ему можно
[00:24:49] кинуть пуш, что у тебя есть пять
[00:24:50] непрочитанных сообщений. Э, обрати
[00:24:53] внимание, насколько это приятнее с точки
[00:24:57] зрения какого-то баланса. Если ты просто
[00:25:00] отправишь пользователю пуш, зайди на
[00:25:02] сайт, ну, какая скорее всего у него
[00:25:04] будет реакция? Ну, типа очень, да,
[00:25:07] здорово. Если ты отправишь ему пуш о
[00:25:09] том, что, допустим, у него сообщения
[00:25:10] непрочитанные есть, это будет выглядеть,
[00:25:13] знаешь, такое модное слово нативно. Вот.
[00:25:16] То есть это не то, что мы просто
[00:25:17] стараемся человека явно ему запихнуть
[00:25:21] вот уведомление в телефон, а ещё потому
[00:25:24] что мы хотим сделать нативненько. В чём
[00:25:26] проблема вообще пушей? Я думаю, не
[00:25:27] секрет, что пользователи не особо любят,
[00:25:29] когда им шлют пуши,
[00:25:30] потому что они могут наоборот оттолкнуть
[00:25:32] пользователя, хотя он конечно, конечно.
[00:25:34] Да. Поэтому пуши - это на самом деле это
[00:25:36] уже тяжёлая артиллерия. Их надо
[00:25:38] использовать уже в такой в какой-то
[00:25:40] смысле в последний момент. Вот. А потому
[00:25:45] что, ну, как бы пользователи не любят
[00:25:48] пуши. Очень большое количество
[00:25:50] пользователей в приложениях вообще
[00:25:51] отключаются пуши. Вот. И как бы таких
[00:25:55] пользователей со включёнными пушами
[00:25:56] нужно беречь, да. И поэтому вот смотри,
[00:25:59] первый вариант очень мне понравился, да,
[00:26:01] что есть непрочитанные сообщения - это
[00:26:02] крутой пуш. ещё какой-нибудь пуш,
[00:26:05] который можно было бы отправить
[00:26:06] пользователю, который тоже как бы вроде
[00:26:09] бы намекает ему просто вернись в
[00:26:10] приложение, но при этом не говорит это
[00:26:12] прямым языком.
[00:26:15] Допустим, не знаю, он подписан на
[00:26:16] какие-то группы, и мы можем послать ему
[00:26:18] информацию о том, что, ну, с каким-то
[00:26:21] интересным предложением, допустим, он,
[00:26:23] не знаю, покупает а какие-то товары
[00:26:25] определённые. Вот можем на основе
[00:26:28] информации о его группах и о постах,
[00:26:30] которые постятся в этой группе,
[00:26:32] допустим, написать, что появился
[00:26:33] такой-то крутой товар. Вот. И тоже
[00:26:34] послать ему.
[00:26:35] Ну да. Да. Причём как бы идея
[00:26:37] правильная. Я думаю, там уже в какие-то
[00:26:39] конкретные товары заужаться, это уже
[00:26:41] совсем как бы такая тонкая штука. Но в
[00:26:44] целом, да, например, прислать ему пуш,
[00:26:46] чтобы появился какой-то новый контент,
[00:26:47] на который он подписан, это тоже очень
[00:26:51] нативненько, так скажем. Вот. О'кей.
[00:26:54] О'кей. Да. Вот это довольно хорошая
[00:26:55] история. Но обрати внимание, что мы как
[00:26:57] бы видишь проделали такой весь путь от
[00:26:59] сборки сырых логов до какой-то уже
[00:27:01] бизнес-логики, которая за машины
[00:27:03] обучением стоит. И это, кстати, тоже
[00:27:05] очень важно понимать, что когда мы
[00:27:06] машинрг в какой-то аналитике применяем,
[00:27:09] на самом деле-то финальным результатом
[00:27:11] этого машин-лернинга является не сама
[00:27:13] модель, которая предсказывает, а что мы
[00:27:15] с этой моделью делаем. Вот, например,
[00:27:17] шлём какие-нибуд хитрые пуши. И обрати
[00:27:19] внимание, что даже если у нас моделька
[00:27:21] работает просто супер круто,
[00:27:23] предсказывает идеально, но мы берём и
[00:27:25] шлём пользователям пуши из разряда:
[00:27:28] "Просто зайди в приложение". Мы как бы
[00:27:31] ээ всю всю работу на самом деле на
[00:27:33] смарт, да. Поэтому здесь, видишь, везде
[00:27:35] на каждом этапе требуется довольно такая
[00:27:37] тонкая история. Спасибо. Спасибо.
[00:27:40] Слушай, наверное, у меня вопросов нет,
[00:27:42] э, поэтому было интересно. Спасибо.
[00:27:47] Опять же после публичной части можем с
[00:27:50] тобой ещё будем обсудить вот приватно
[00:27:53] какие-то вопросы, которые остались.
[00:27:54] Хорошо.
[00:27:55] Да, хорошо, понял. Мне тоже было
[00:27:56] интересно.
[00:27:57] Спасибо. Спасибо тебе.

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required for step 2 (Q&A extraction). splitter_prepare_prompt.py does not call any LLM API.
Do NOT substitute another model (e.g. GPT) unless the user explicitly overrides.
Required model: claude-sonnet-4-6
Suggested temperature: 0


======================================================================
OUTPUT PATHS (post-processing)
======================================================================
Save JSON to: splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.qa-split.json

Then (preferred — no LLM):
  scripts/splitter_post.sh splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.qa-split.json \
    --video transcripts/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.qa-split.json --out splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.qa-split.json \
    --video transcripts/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/video.md \
    --tolerance 120 \
    --out splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.validation-report.md

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
   - self-answered interviewer turns correctly use candidate_answer.text = null and reference_answer for the explanation

When a chapter shows 0 extracted items (recognition_status: not_recognized):
- Look at the previous chapter's last item(s). If one has a timestamp within 60 seconds BEFORE this chapter's marker AND its content matches this chapter's title → set BOTH flags true, leave notes as empty string "". This is normal drift within tolerance.
- Set both flags false ONLY when the topic is genuinely not covered anywhere nearby: truly missed question, or a discussion/explanation segment with no interviewer question.

Return ONLY valid JSON matching the schema. No markdown fences.
Language for notes: Russian. Keep notes short and actionable. Leave notes as "" when both flags are true.

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
video.md: transcripts/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/video.md

--- CHAPTER `00:31:05` — Рассказ кандидата о себе ---
window: 00:31:05 .. 00:35:45
recognition_status: multiple (4 items)

ITEM #1
  interviewer_question: time=00:00:01 text='тем, как перейти к каким-то техническим историям, можешь просто немного рассказать вообще, как ты как ты оказался в мире в мире анализа данных? Почему почему?'
  candidate_answer: time=00:00:09 text='Оказалось очень просто. Сейчас я учусь на третьем курсе в Этмольте информационных технологий и программирования. Вот, соответственно, на третьем курсе, в пятом семестре у меня был курс по машинному обучению. Вот до этого я вообще не знал о мире машинного обучения. Вот. Но курс мне показался настолько интересным, что я решил найти работу. Вот. успешно прошёл собеседование. Вот. И сейчас работаю начинающим датасаинтистом. Вот этого сном увлекался программированию, разработкой, но после курса по машинам обучения понял, что, наверное, нашёл свою область.'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Adaptability

ITEM #2
  interviewer_question: time=00:00:41 text='А, соответственно, можешь рассказать немного вот чем вообще интересно заниматься? То есть что бы хотелось сделать?'
  candidate_answer: time=00:00:50 text='В основном мне интересно заниматься машинным обучением, вот, но в том числе статистикой, аналитикой в каком-то плане, исследовать закономерности в данных, какие-то инсайты доставать, вот, и так далее.'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Adaptability

ITEM #3
  interviewer_question: time=00:01:09 text='Слушай, ну давай тогда, раз такое дело, со статистики начнём, как вообще у тебя с мастатом?'
  candidate_answer: time=00:01:15 text='Ну, с мастатом нормально. У меня был курс базовый по массо статистике на втором курсе. Вот. Но не то, чтобы был слишком профильный. Вот скорее у меня уклонны машины обучения. Вот.'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Statistics

ITEM #4
  interviewer_question: time=00:01:26 text='Ну давай с базовых вещей. Вот можешь рассказать, что такое P-value и зачем оно нужно?'
  candidate_answer: time=00:01:33 text='P-value - это уровень значимости. Вот говоря, а приведу просто пример, так будет проще объяснить. Вот, допустим, у нас есть некоторые утверждения, вот, и есть некоторые гипотеза, которую мы хотим проверить. И, соответственно, мы выдвигаем нулевую гипотезу, которая нам говорит о том, что, точнее, мы хотим найти найти или показать различие в том, что является ли наша гипотеза правдой. Мм. Мне больше нравится пример с монеткой приводить. Вот у нас есть частная монетка. Вот мы подкидываем её там условно, не знаю, допустим, 20 раз. Вот. И, допустим, все 20 раз выпадает орёл. Нулевая гипотеза звучит так, то, что наша монетка является честной и ничего в ней такого особенного нет. А альтернативная гипотеза звучит так, то что наша монетка специальная. P-value - это по сути это вероятность данного события при том, что нулевая гипотеза будет верной. В нашем случае можем посчитать P-value очень просто. То есть мы знаем то, что вероятность для частной монетки падения орла равна 1/2. Вот откидываем монетку 20 раз и 20 раздает орёл. Понятное дело то, что вероятность будет равна 1 / 2 степени. Приблизительно получается одна миллионная. И по сути это и будет значение P-value. И далее на основании нашего значения P-value мы можем посчитать, является ли наша гипотеза, ну, точнее, наш результат статистически значимым или нет. Обычно берут пятипроцентное значение уровня значимости, вот, и сравнивают его со значением P-value. Если P-value получается меньше, чем, ну, 5%, то, соответственно, мы наклоняем нулевую гипотезу и принимаем альтернативную. В нашем случае будет верна альтернативная.'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Statistics

--- CHAPTER `00:35:45` — Настройка системы оповещений ---
window: 00:35:45 .. 00:43:53
recognition_status: multiple (5 items)

ITEM #5
  interviewer_question: time=00:04:46 text='Ты сказал, что вот P-value - это по сути вероятность получить такие результаты, если нулевая гипотеза верна. А если мы, допустим, перейдём в формат уже не монетки, а более такой реалистичной истории, вот мы сравнили две группы. У нас есть две группы пользователей. У одних пользователей, допустим, там старый дизайн приложения, у других пользователей новый дизайн приложения. И мы замеряем среднее значения, соответственно, там среднее значение в каждой группе, сколько пользователей провели время на сайте. Мы, соответственно, получили, что в одной группе среднее равняется 100, а в другой 150. Правда ли сказать, что P-value - это вероятность получить такие различия в средних при верности нулевой гипотезы?'
  candidate_answer: time=00:05:50 text='Ну да, просто верно.'
  reference_answer: time=00:05:51 text='Давайте попробуем понять, почему это на самом деле неправильный ответ. А вот если ты вспомнишь, как обычно P-value в учебниках рисуются, вот рисуется такое распределение, и там есть есть ещё односторонняя, двусторонняя гипотеза. Вот у нас есть вот распределение и с двух сторон у нас заштрихована какая-то зона под прямой. P-value - это вероятность получить такие или ещё более сильно выраженные различия, да, если верна нулевая гипотеза. Это не то, чтобы сверхкритичная вот разница, но всё-таки довольно существенная, потому что при интерпретации P-value часто действительно существует некоторая путаница. И вот действительно сказать, что P-value - это именно прямо вот такая точечная оценка вероятности именно такого события, это, конечно, не совсем верно. То есть это такого или ещё более сильно выраженного.'
  interviewer_feedback: time=None text=None
  question_topic: Statistics

ITEM #6
  interviewer_question: time=00:07:25 text='А, кстати, вот есть ещё двусторонние, односторонние гипотезы, они чем отличаются друг от друга?'
  candidate_answer: time=00:07:30 text='А в том, что двусторонне мы, грубо говоря, не знаем, а в какую сторону будет отклонение.'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:07:37 text='Угу. Угу. И, кстати, возвращаясь к нашему предыдущему вопросу, это означает, что если мы проверяем двустороннюю гипотезу P-value и считаем вот 0.05, это означает, что это вероятность получить как сильно выраженные различия в правую, в большую сторону, в одной из групп, так и на самом деле в меньшую. Вот как-то так.'
  question_topic: Statistics

ITEM #7
  interviewer_question: time=00:08:52 text='перед тем, как мы перейдём к какой-то там архитектуре модели и так далее, вот сначала бизнес-логика, как ты думаешь, вообще, зачем это нужно делать? Вот зачем нам в целом нужно предсказывать, что пользователь куда-то дропнутся? Мы говорим: «У нас все логи есть. Допустим, мы живём в идеальном мире, где у нас там инфраструктура, всё настроено, даты, инженеры всё собрали». Мы работаем аналитиками в фейсбуке, у нас есть там миллиарды пользователей, и мы хотим в каком-то мере их как-то кластеризовать. Вот говорим, что вот эти ребята - это наши ядровые аудитории, а вот эти ребятки, они собираются дропнуться. Вот зачем нам в целом нужно предсказывать, что пользователь куда-то дропнутся?'
  candidate_answer: time=00:09:02 text='Но мне кажется, что если мы знаем, что какая-то определённая группа пользователей дропнутся, то, допустим, не знаю, провести какую-то маркетинговую рассылку, а с цель повысить их интерес к нашему приложению, к нашей социальной сети. Вот. И в этом плане оно может, ну, повлиять в какой-то мере, и, соответственно, уход пользователя он будет в меньшей мере, вот, чем был до этого.'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:09:24 text='Ну, конечно, да, если так всё-таки ещё более явно сказать, то есть мы всё-таки живём в мире капитала, и надо понимать, что когда пользователь пользуется социальной сетью, на самом деле мы в каком-то смысле зарабатываем деньги на этом факте, там, например, мы показываем пользователю рекламу или он покупает там платные стикеры у нас, и если пользователь перестанет пользоваться нашим продуктом, ну, мы как бы просто теряем деньги, вот условно.'
  question_topic: Product Metrics

ITEM #8
  interviewer_question: time=00:09:50 text='Хорошо. можешь тогда вот рассказать, как бы ты к такой задачке подошёл. Давай вот попробуем сейчас как-то вот накидать высокоуровнево. Вот какие бы ты признаки собрал, какие бы фичи собрал, как бы ты вот вот вот end to end можешь такими крупными мазками нарисовать твой подход к решению задачи. можешь прямо там сделать, например, там топ-пять фичей, которые ты хотел бы взять, топ-пять признаков максимально операционализированных, максимально понятных. То есть условно, чтобы человек тебя послушал и мог запрос в базу написать, там select сумма лайков from table, group by user ID условно.'
  candidate_answer: time=00:10:49 text='Ну, я думаю, да, вот как раз таки такую информацию вот, допустим, о лайках либо, допустим, о времени провождения на сайте тоже могло быть полезно. Ладно, так, пожалуй, так. А время провождения на сайте в секундах. Мм. количество лайков, совершённых пользователем. количество друзей, знакомых. можно использовать какие-то географические признаки, возможно, в разных регионах лишного смысла. Да. Да. Популярность. Наша сеть имеет разную популярность.'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:12:10 text='Это очень, кстати, хорошая мысль, потому что, условно, если человек находится в некотором таком в ядре от этого социального графа, где все пользуются Фейсбуком, это скорее всего, да, может как-то быть связано с географией.'
  question_topic: Product Metrics

ITEM #9
  interviewer_question: time=00:12:35 text='А как ты думаешь, почему просто суммарное количество лайков, условно, это на самом деле довольно плохая метрика? В чём подвох вообще суммарных метрик? Вот у нас есть пользователь, у одного 100 лайков, у другого 1.000. Почему на самом деле тут не хватает ещё очень важного уточнения?'
  candidate_answer: time=00:13:53 text='А, от количество просмотреных постов.'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:13:54 text='Ну, конечно, конечно, потому что, ну, смотри, как бы просто суммарное количество лайков, на самом деле мало что говорит. Условно, если человек просмотрел миллиард постов и поставил 1.000 лайков, это не то же самое, что человек просмотрел 100 постов и поставил 100 лайков. То есть как бы получается, что у второго человека, которого лайков меньше, но условный как бы CTR, некоторая конверсия в лайк у него гораздо больше. означает, что его вовлечённость в процесс, это опять же гипотеза, но теперь у нас хотя бы есть какой-то к ней подход.'
  question_topic: Product Metrics

--- CHAPTER `00:43:53` — Вопрос про best practices ---
window: 00:43:53 .. 00:44:33
recognition_status: not_recognized (0 items)

(no items extracted)
--- CHAPTER `00:44:33` — Как понять, что различия значимы ---
window: 00:44:33 .. 00:49:52
recognition_status: multiple (3 items)

ITEM #10
  interviewer_question: time=00:14:43 text='Вот если теперь просто просто мы представим, что у нас есть вот таблица с пользователями. Вот как бы ты эту метрику посчитал, ты просто взял бы, не знаю, все секунды, которые человек провёл на сайте за всю свою историю регистрации или как? Давай только тоже вернёмся к предыдущей идее. Вот если лайки нам нужно было как-то нормировать и считать не просто сумму, то с временем приведения на сайте тоже как-то вот надо посчитать её немножко иначе. Вот как мы её будем считать?'
  candidate_answer: time=00:14:56 text='не, наверное, это не очень хороший подход, потому что, допустим, пользователь может просто там, не знаю, открыть нашу социальную сеть в фоновом режиме и время будет текать. получить среднее значение в секундах в год, к примеру, либо в день.'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:16:06 text='Ну, конечно, в день, да. Ну год - это, ну, год - это перебор. Ну, то, что человек делал год назад, условно, как бы, скорее всего уже, может быть, не так актуально. Абсолютно верно. И среднее проведение в день, опять же, уже может быть гораздо более понятнее.'
  question_topic: Product Metrics

ITEM #11
  interviewer_question: time=00:16:44 text='Количество друзей. Вот с количество друзей тоже как бы давай тоже добьём и попробуем какие-нибудь ввести всё-таки пограничные случаи. Ну, на что бы здесь тоже можно было бы как-то обратить внимание, а не просто взять условно там суммарное количество друзей.'
  candidate_answer: time=00:17:22 text='Можно было, скорее, допустим, сколько новых друзей у этого человека за какой-то промежуток времени.'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:17:26 text='Абсолютно верно. Абсолютно верно. Абсолютно верно. То есть суммарное количество друзей даже не так важно. Нам скорее важно понять, продолжается ли пополнение друзей у человека. И вот эта фича, поверь мне, как бы точно будет куда более предиктабл вот по своей силе, чем обычно.'
  question_topic: Product Metrics

ITEM #12
  interviewer_question: time=00:17:50 text='Мы хотим понять, дропнулся человек или нет. Вот как вообще понять? Это дропнулся, если он неделю не заходил или месяц или год? Как нам понять, сколько времени должно пройти с последнего захода, чтобы считать, что этот человек уже, скорее всего, к нам не вернётся? Можно ли здесь как-то попробовать статистически подобраться и подумать, что можно как-то обосновать это решение?'
  candidate_answer: time=00:18:56 text='Ну, допустим, условно 2 недели. наверное, лучше рассматривать ещё предыдущую историю увлечённости. Возможно, раньше он был более активным, и сейчас его активность она спала. И учитывать эту разницу. Так вот, да, можно взять инфу о предыдущих пользователях, а тех, которые дропнулись и о тех, которые не дропнулись, и проаносировать, сколько времени они не заходили на сайт и уже отливаться от этого.'
  reference_answer: time=00:22:11 text='Да. Да. И просто когда мы для всех пользователей посмотрели статистику их как бы разрывов в их активности сессий, можно действительно просто распределеница построить и сказать, что если пользователь не заходит на сайт 2 недели, то только у 5% пользователей, у которых превышает разрыв 2 недели, есть последующие сессии. Ну это я сейчас утрирую, фантазирую, но как бы или или у 10%. И тогда нам нужно наоборот как-то подвинуть этот порог. Ну вот, да, то есть видишь, мы тоже выяснили, что, чтобы данные подготовить, сколько тут подводных камней скрывается.'
  interviewer_feedback: time=None text=None
  question_topic: Product Metrics

--- CHAPTER `00:49:52` — Доверительные интервалы ---
window: 00:49:52 .. 00:52:58
recognition_status: not_recognized (0 items)

(no items extracted)
--- CHAPTER `00:52:58` — Количество слов в английском языке ---
window: 00:52:58 .. 00:55:27
recognition_status: multiple (2 items)

ITEM #13
  interviewer_question: time=00:23:04 text='Допустим, обучили какой-то классификатор. Какой классификатор ты бы хотел, кстати, здесь обучить? ну, в целом, какой метод ты бы здесь применил?'
  candidate_answer: time=00:23:21 text='Не знаю, к примеру, градиентный бустинг.'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:23:24 text='Ну, why not, да? Применили градиентный бустинг, обучили, провалидировали, всё работает.'
  question_topic: ML

ITEM #14
  interviewer_question: time=00:23:34 text='Ну, предсказываем уход в пользователя. Теперь аналитический вопрос: а что делать-то? Ну вот, допустим, мы предсказали, что пользователь Анатолий Карпов через неделю собирается окончательно прекратить пользоваться нашим сервисом. Вот что бы теперь с ним сделать? а можешь прямо вот представь, что мы сидим на таком брейнсторме с маркетологами. Вот они говорят: «Так, а что именно? Что именно? Вот что отправляем?» Вот тут можешь прямо какое-нибудь такое финальное решение сказать? Вот что мы этому человеку отправим?'
  candidate_answer: time=00:23:48 text='Можем, к примеру, отправить ему какое-то сообщение или уведомление о том, чтобы напомнить ему, что у нас есть сервис, которым может пользоваться либо как-то заинтриговать его внимание. Ну, я бы предложил чисто с головы взял, э, просто напомнить ему зайти на сайт. Вот, потому что он уже, допустим, не заходил долгие перерё у него могли быть новые сообщения потенциальные.'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:24:48 text='Давайте теперь эту мысль завьём. Ему можно кинуть пуш, что у тебя есть пять непрочитанных сообщений. Обрати внимание, насколько это приятнее с точки зрения какого-то баланса. Если ты просто отправишь пользователю пуш «зайди на сайт», ну, какая скорее всего у него будет реакция? Если ты отправишь ему пуш о том, что, допустим, у него сообщения непрочитанные есть, это будет выглядеть нативно. То есть это не то, что мы просто стараемся человека явно запихнуть уведомление в телефон. В чём проблема вообще пушей? Пользователи не особо любят, когда им шлют пуши, потому что они могут наоборот оттолкнуть пользователя. Поэтому пуши - это на самом деле это уже тяжёлая артиллерия. Их надо использовать уже в такой в какой-то смысле в последний момент.'
  question_topic: Product Metrics

--- CHAPTER `00:55:27` — Количество активных пользователей в месяц в «Одноклассниках» ---
window: 00:55:27 .. 01:02:08
recognition_status: single (1 items)

ITEM #15
  interviewer_question: time=00:26:04 text='ещё какой-нибудь пуш, который можно было бы отправить пользователю, который тоже как бы вроде бы намекает ему просто вернись в приложение, но при этом не говорит это прямым языком.'
  candidate_answer: time=00:26:15 text='Допустим, не знаю, он подписан на какие-то группы, и мы можем послать ему информацию о том, что, ну, с каким-то интересным предложением, допустим, он, не знаю, покупает а какие-то товары определённые. Вот можем на основе информации о его группах и о постах, которые постятся в этой группе, допустим, написать, что появился такой-то крутой товар. Вот. И тоже послать ему.'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:26:35 text='Ну да. Да. Причём как бы идея правильная. Я думаю, там уже в какие-то конкретные товары заужаться, это уже совсем как бы такая тонкая штука. Но в целом, да, например, прислать ему пуш, что появился какой-то новый контент, на который он подписан, это тоже очень нативненько, так скажем.'
  question_topic: Product Metrics

SAVE JSON: вставьте ответ в конец файла splitter_output/mock-interviews/karpov/data-analyst-junior-karpov-vyacheslav-2021-06-24/data-analyst-junior-karpov-vyacheslav-2021-06-24.v2.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
