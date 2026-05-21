<!-- PIPELINE_MANIFEST
{
  "version": 14,
  "basename": "data-scientist-junior-karpov-2022-03-30",
  "transcript_folder": "data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30",
  "source_id": "data_scientist_junior_karpov_2022_03_30",
  "splitter_mode": "split_and_validate",
  "started_at": "2026-05-21 17:17:29 +0200",
  "updated_at": "2026-05-21 17:25:32 +0200",
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
    "json": "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json",
    "xlsx": "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.xlsx",
    "validation_report_md": "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.validation-report.md",
    "pipeline_log_md": "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.pipeline-log.md"
  },
  "llm_inputs": [
    {
      "step": 2,
      "name": "qa_extraction",
      "model": "claude-sonnet-4-6",
      "prompt_location": "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.pipeline-log.md#LLM_INPUT_STEP_2"
    },
    {
      "step": 5,
      "name": "semantic_validation",
      "model": "claude-sonnet-4-6",
      "prompt_location": "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.pipeline-log.md#LLM_INPUT_STEP_5"
    }
  ],
  "steps": [
    {
      "id": 1,
      "name": "prepare",
      "llm": false,
      "model": null,
      "inputs": [
        "data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/timecodes.txt",
        "ru",
        ".claude/skills/splitter/step1-prepare/splitter_system_prompt.txt",
        ".claude/skills/splitter/step1-prepare/splitter_output_schema.json"
      ],
      "outputs": [
        "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.pipeline-log.md"
      ],
      "status": "completed",
      "duration_sec": null,
      "notes": null,
      "finished_at": "2026-05-21 17:17:29 +0200"
    },
    {
      "id": 2,
      "name": "qa_extraction",
      "llm": false,
      "model": null,
      "inputs": [
        "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json"
      ],
      "outputs": [
        "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json"
      ],
      "status": "completed",
      "duration_sec": 600.0,
      "notes": null,
      "finished_at": "2026-05-21 17:25:32 +0200"
    },
    {
      "id": 3,
      "name": "excel",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.xlsx"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-21 17:25:26 +0200"
    },
    {
      "id": 4,
      "name": "validate_chapters",
      "llm": false,
      "model": null,
      "inputs": [
        "/Users/mm/projects/ds-final-project/data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json",
        "/Users/mm/projects/ds-final-project/data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/video.md"
      ],
      "outputs": [
        "/Users/mm/projects/ds-final-project/data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 1.0,
      "notes": null,
      "finished_at": "2026-05-21 17:25:26 +0200"
    },
    {
      "id": 5,
      "name": "llm_validation",
      "llm": false,
      "model": null,
      "inputs": [
        "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.pipeline-log.md"
      ],
      "outputs": [
        "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.validation-report.md"
      ],
      "status": "completed",
      "duration_sec": 120.0,
      "notes": null,
      "finished_at": "2026-05-21 17:25:32 +0200"
    }
  ],
  "forbidden_prior_artifacts": [
    "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v2.qa-split.json",
    "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v3.qa-split.json",
    "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v4.qa-split.json",
    "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v5.qa-split.json",
    "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v6.qa-split.json",
    "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v7.qa-split.json",
    "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v8.qa-split.json",
    "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v9.qa-split.json",
    "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v10.qa-split.json",
    "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v11.qa-split.json",
    "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v12.qa-split.json",
    "data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v13.qa-split.json"
  ],
  "step2_anti_leak_check": "python3 .claude/skills/splitter/step1-prepare/splitter_check_prior_leak.py data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json"
}
-->

# Pipeline log v14

Журнал одного прогона splitter: шаги, модели, артефакты. **Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже (шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).

- **Interview folder:** `data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30`
- **Source ID:** `data_scientist_junior_karpov_2022_03_30`
- **Splitter mode:** `split_and_validate`
- **Started:** 2026-05-21 17:17:29 +0200
- **Last updated:** 2026-05-21 17:25:32 +0200

Фильтр в IDE: `*data-scientist-junior-karpov-2022-03-30.v14*`

## Models (from run_config.json)

- **step2_qa_extraction:** `claude-sonnet-4-6` (temperature 0)
- **step5_llm_validation:** `claude-sonnet-4-6` (temperature 0)

## Steps

| # | Step | LLM | Model | In | Out | Duration | Status |
|---|------|-----|-------|----|-----|----------|--------|
| 1 | prepare | no | — | `data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/timecodes.txt`<br>`ru`<br>`.claude/skills/splitter/step1-prepare/splitter_system_prompt.txt`<br>`.claude/skills/splitter/step1-prepare/splitter_output_schema.json` | `data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.pipeline-log.md` | — | completed |
| 2 | qa_extraction | no | — | `data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json` | `data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json` | 600.0s | completed |
| 3 | excel | no | — | `/Users/mm/projects/ds-final-project/data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json` | `/Users/mm/projects/ds-final-project/data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.xlsx` | 1.0s | completed |
| 4 | validate_chapters | no | — | `/Users/mm/projects/ds-final-project/data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json`<br>`/Users/mm/projects/ds-final-project/data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/video.md` | `/Users/mm/projects/ds-final-project/data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.validation-report.md` | 1.0s | completed |
| 5 | llm_validation | no | — | `data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.pipeline-log.md` | `data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.validation-report.md` | 120.0s | completed |

## Artifacts (this version)

- **json:** `data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json`
- **xlsx:** `data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.xlsx`
- **validation_report_md:** `data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.validation-report.md`
- **pipeline_log_md:** `data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.pipeline-log.md`

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
0) **No prior versions (hard):** You MUST NOT read, open, or copy from any older `*.v*.qa-split.json` in the interview folder (v1, v2, … v(N-1)). The only allowed JSON output path is the target `vN` from the user message. Every `items[]` entry MUST come from PRIMARY_TRANSCRIPT in this run. Copying a prior run — even if it passed validation — makes the extraction **invalid**.
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

§ technical_coding — pair programming / interleaved dialogue (hard)
- One coding task often spans **many minutes** (Colab, screen share). Still **one primary item** (`interview_stage`: `technical_coding`) unless the interviewer starts a **new** unrelated task.
- **Rule #1 (overrides everything below):** transcripts have **no speaker labels** and lines **alternate every few seconds**. Each LinkedText field = **one speaker only** (§11). **Never** paste interviewer coaching into `candidate_answer` to “keep the full dialogue in one field”.
- **`interviewer_question.text`:** initial task statement only (may merge adjacent interviewer fragments at the start).
- **`candidate_answer.text`:** concatenate **candidate-only** verbatim spans from first substantive reply after the task until the next interview topic. Include all candidate attempts (loop idea, pandas, confusion, debug) — but **exclude** interviewer lines.
  * Candidate signals: «я бы», «в цикле я бы», «не понимаю», «для меня», «я знаю как», «не пользовался», «кажется не сработало», describing own code aloud.
  * **Mid-line split mandatory** when one `[HH:MM:SS]` line mixes speakers, e.g. `[00:49:39] ну я бы видел это как цикл супер напиши` → candidate part ends before «супер напиши»; interviewer part → `interviewer_feedback`.
- **`interviewer_feedback.text`:** concatenate **interviewer-only** spans in the same task window (can be **long** — many minutes of hints). Not optional “only if short”.
  * Interviewer signals: «тебе нужно», «давай напиши/напишем», «проговори», «ты видишь», «не слушай ты усложняешь», «супер», «нам нужно сделать», «ты должен», «перезагрузи страничку», explaining pandas/groupby while directing «ты».
  * `interviewer_feedback.time` = timestamp of the **first** interviewer coaching line after the task (not the final hint).
- **`reference_answer.text`:** interviewer's **canonical final solution** only (often one block near the end, e.g. `dt.get()` pattern), **not** every hint while coding.
- **Forbidden:** one blob in `candidate_answer` with both «ну я бы видел…» and «типа ты видишь… давай напишем цикл» — that is **invalid** even if validation time-alignment passes.
- **Forbidden:** dropping candidate performance: `candidate_answer` one line while `reference_answer` is +15 min later with no candidate spans collected.
- **Sanity check:** if `candidate_answer` contains «ты видишь», «не слушай ты», «давай напишем» (interviewer voice) → re-cut; move those spans to `interviewer_feedback`.

Few-shot (technical_coding, Karpov-style group-by):
- BAD A: «ну я бы видел цикл… типа ты видишь это как цикл… давай напишем pandas… хорошо давай напишем цикл… я понимаю что ты всё рассказал» (interviewer + candidate merged).
- GOOD A: «ну я бы видел это как цикл… длину листа… if i в b… не понимаю где поделать… import pandas… zip не пользовался…» (candidate only).
- GOOD feedback: «супер напиши… проговори логику… не слушай ты усложняешь… давай сделаем dict… давай напишем dt… убери плюс равно…» (interviewer only, may be long).
- GOOD reference_answer: final `for i, g in zip(a, b): dt[g] = dt.get(g, 0) + i` at [01:02:58] only.

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
SOURCE_ID: data_scientist_junior_karpov_2022_03_30
SPLITTER_MODE: split_and_validate
INTERVIEW_FOLDER: data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30
INTERVIEW_LANGUAGE: ru
PRIMARY_TRANSCRIPT (TIMECODES_TXT):
[00:00:00] [музыка]
[00:00:04] значит что у нас будет сегодня у нас
[00:00:08] сегодня будет с тобой могут разъем на
[00:00:11] позицию день ртс то ли один из числа
[00:00:14] людей которые откликнуться на наш зов
[00:00:17] карп в курсах и
[00:00:20] которые хотя бы провести мог интервью
[00:00:22] что значит мог интервью по сути своей
[00:00:24] это полноценный интервью с человеком
[00:00:28] который пытается пройти позицию однако в
[00:00:32] отличии от полноценным интервью я тебе
[00:00:34] сразу дома процесс в реальной жизни мы
[00:00:37] берем там какое то время но только
[00:00:38] подумайте посмотреть других кандидатов а
[00:00:41] помимо этого
[00:00:42] дом посылаю тебя не будет . будет только
[00:00:46] просто практика прохождения интервью
[00:00:48] поводу не спасётся а вообще мог интервью
[00:00:51] и вообще интервью у куда-то sens но по
[00:00:54] крайней мере у меня она состоит из 4
[00:00:56] секций
[00:00:57] иногда эти секции разбиваются в течение
[00:01:00] времени иногда эти секции идут прям
[00:01:04] подряд друг за друга и на них уходит два
[00:01:07] часа иногда чуть больше иногда чуть
[00:01:10] меньше и так далее значит 4 секции
[00:01:13] зачастую состоят из следующих вещей у
[00:01:16] нас есть питон у нас есть вопрос связан
[00:01:21] из
[00:01:22] машин лёнинг алгоритмы меня я конкретно
[00:01:25] какие-то базовые алгоритмы говорим я
[00:01:28] пытаюсь тебя расспросить на тему чего ты
[00:01:30] знаешь что не знаешь и как ты будешь
[00:01:33] отвечать на тот или иной вопрос третья
[00:01:35] тема это работа за нами в рамках работы
[00:01:39] с данными мы тоже там спрашиваем
[00:01:42] различные вещи четвёртая тема она по
[00:01:44] разному звучит 4 секция прозвучит иногда
[00:01:49] для там специалистов junior ими до
[00:01:52] уровня это просто дизайн эксперимента и
[00:01:54] дизайна б теста для человека там медовый
[00:01:58] плюс и синий это обязательно и мой
[00:02:01] ассистент дизайн враг которого тоже
[00:02:04] обсуждаем то как создавать приложения с
[00:02:09] использованием алгоритмов мы нам очень
[00:02:12] значит у тебя будет велика ли
[00:02:16] возможность выбрать с чего ты хочешь
[00:02:20] начать
[00:02:21] вот потому что затем
[00:02:23] всего будет подходить нам один к одному
[00:02:26] и
[00:02:27] будем смотреть как ты будешь отвечать на
[00:02:30] эти вопросы вот чего бы ты хотел начать
[00:02:32] из этих четырех все они все как одна
[00:02:35] страшные поэтому срубается хорошо давай
[00:02:38] тогда но раз я уже колаб открыт
[00:02:41] давай начнем с питона я тебе буду сейчас
[00:02:46] забывать несколько вопросов бизнеса
[00:02:49] общей теории познали бетона а
[00:02:51] параллельно я напишу несколько задачек
[00:02:54] которые тебе нужно будет решить в нашем
[00:02:57] call or by давай начнем с вопроса крова
[00:03:00] изменяемые и неизменяемые типе данных
[00:03:02] кто не что это вообще такое какие типы
[00:03:06] данных каким типом данных
[00:03:08] освоения из не изменяют наверно мне
[00:03:12] известны словари который мы единожды
[00:03:15] прописываем и долине меня остальные
[00:03:18] ведьмами дня мы типа данных я правильно
[00:03:20] понимаешь кричите про
[00:03:21] сирии dataframe и списке
[00:03:26] да ну давай начнем с того что у нас есть
[00:03:30] там основные
[00:03:32] типы это в виде ну intel до флот и есть
[00:03:37] string
[00:03:38] есть с этой теплые dig-t ну есть всякие
[00:03:43] kollection это
[00:03:46] очереди
[00:03:48] там тоже есть работа с червями настрою
[00:03:52] очередь например на youtube там и так
[00:03:55] далее мы сейчас не будем досматривать
[00:03:57] давайте рассмотрим конкретно intel флот
[00:04:00] и
[00:04:01] стринги листы сеты теплые эдикты вот что
[00:04:06] из этих семи получается изменяемые что
[00:04:09] они теплые лифты не меня же мы остальные
[00:04:12] меняем и диксы это словарь это там где
[00:04:15] она соответствует какое-то значение
[00:04:17] какому-то значению более научным языком
[00:04:19] на но я не смогу сказать теплые это не
[00:04:23] меняем эй наборы значений насколько я
[00:04:24] помню все остальное наверное мы можем
[00:04:26] менять dig-t и еще раз никто мы можем
[00:04:29] менять и нет нет не может хорошо а
[00:04:34] теплые можем насколько я помню тоже нет
[00:04:36] так хорошо и
[00:04:39] с этой бабой можем или вот это сложно
[00:04:42] это было я читал но
[00:04:44] не пользовался и наверное ничего не
[00:04:47] скажу процент и хорошо entry вот но int
[00:04:50] и целые флоты подробно и до стринги они
[00:04:54] все от меня и мы не меняем мы говорим о
[00:04:57] том что если я какой-то переменной
[00:04:59] присвоил мне как эта переменная типа int
[00:05:02] и могу ли я разные значения в нее власти
[00:05:05] в процессе
[00:05:06] по сути своей да но не совсем так смотри
[00:05:11] изменяемые что что это значит представим
[00:05:14] себе что у нас есть лист в этот лист мы
[00:05:18] добавляем какое-то значение вопрос
[00:05:21] изменился ли илистых нет и изменилось ли
[00:05:24] ссылка на личику памяти в этом месте
[00:05:27] вопрос на самом деле чуть более сложный
[00:05:30] сразу тебе скажу что ты не прав своих
[00:05:33] представлениях что вадик ты не изменяем
[00:05:35] тип данных об этом собственно будет наша
[00:05:39] задача самое первое вот и чуть чуть
[00:05:43] поговорим про он давай вот чтобы у тебя
[00:05:46] в голове был правильный ответ то ты флот
[00:05:49] и другие неизменяемые теплыми изменяемые
[00:05:52] что это значит что в случае если ты
[00:05:54] что-то делаешь с этими данными
[00:05:58] этим четырьмя с это тоже не то ты по
[00:06:03] сути своей перри создаешь объект
[00:06:05] бетонные который будет ссылаться надо
[00:06:07] будет память однако есть нюанс о котором
[00:06:11] мы поговорим в летах но важно понять что
[00:06:14] дикари это изменяет тип данных и об этом
[00:06:18] мы убедимся вот это задачки смотри задач
[00:06:22] канаде нас есть некоторые функции она
[00:06:25] вот у тебя в следующих строчкой да есть
[00:06:29] три ячейки что в этой функции происходит
[00:06:33] она на вход принимает dict и на выходе
[00:06:36] выдает значит без разницы какой
[00:06:40] dictionary он получил на вход у нас
[00:06:44] идет такое объявление нового ключа и
[00:06:47] значение для этого а z равно 99 у нас
[00:06:52] есть вот такая функция foo у нас есть
[00:06:57] dictionary виде один a2b 34 d у нас есть
[00:07:03] объект б как функция от нашего диктор и
[00:07:09] затем встает вопрос равны ли а и b вот
[00:07:13] это этот самый последний часть
[00:07:16] дмитрий могу я тебя попросить сделать
[00:07:18] вот нажать в контру плюс чтобы чуть-чуть
[00:07:21] приблизить чтобы мы могли получше ну и
[00:07:25] человек который будет смотреть это
[00:07:28] transform мог получше видеть что
[00:07:31] происходит control + или shift + как-то
[00:07:34] приблизить как-то нам нужно увеличить
[00:07:37] масштаб он мог супер супер вообще
[00:07:41] идеально давая вопрос собственно он и в
[00:07:44] самом низу равно ли а и б по сути своей
[00:07:47] это булент проверка и нам нужно ответить
[00:07:51] либо true либо фолз вот какой ответ как
[00:07:54] ты думаешь у нас функции формы принимает
[00:07:58] а
[00:07:59] потому что она выдаст ru
[00:08:03] давай запустим все вот эти ячейки
[00:08:07] начиная со второй
[00:08:09] [музыка]
[00:08:16] да действительно труп но встает вопрос
[00:08:19] как выглядят они как выглядит как там но
[00:08:24] мне кажется что а мы увидим содержимое а
[00:08:28] то что мы видим сейчас 12 бы так далее и
[00:08:31] z99 и
[00:08:33] [музыка]
[00:08:34] а это будет одно и то же что это значит
[00:08:38] что dict который пришел на вход он типы
[00:08:41] измениться и
[00:08:42] мы на самом деле в этом у нас есть
[00:08:45] некоторая проблема давай даже знаешь как
[00:08:48] мы
[00:08:49] несколько усложним эту задачку я хочу
[00:08:53] чтобы ты убедился что
[00:08:57] диктата изменяемая это изменяем тип
[00:08:59] данных в питоне нам и я хочу чтобы ты
[00:09:04] знаешь как вот в ячейке где ну идет
[00:09:09] объявление одни объявления б после того
[00:09:12] как объявил а я хочу чтобы ты написал
[00:09:16] aldea придадим нет прости прям вот в
[00:09:21] ячейки под номером 2 которые у тебя вот
[00:09:24] здесь
[00:09:24] после а после объявления а самый конец
[00:09:28] самый или линиям самый конец до отожгли
[00:09:32] you enter здесь напишем print
[00:09:37] в скобочках айди
[00:09:42] в скобочках
[00:09:45] да и вот эту же самую функцию print
[00:09:49] видео добавив после b равно фуа
[00:09:54] здесь то же самое
[00:09:59] [музыка]
[00:10:00] да и запустим
[00:10:07] что делает функция 1 функция де
[00:10:10] по сути своей указывает на ячейку памяти
[00:10:13] и мы можем увидеть что увеличить память
[00:10:16] изменилась по сути своей на самом деле
[00:10:18] это старт
[00:10:20] начинаем с этой ячейке у нас находится
[00:10:22] лоб объект
[00:10:25] который видели выглядят виде некоторого
[00:10:29] диктант соответственно did изменяя в
[00:10:32] него можно что-то писать
[00:10:34] что-то с ним как-то сделать значит смысл
[00:10:37] в чем вторая задача до который выходит
[00:10:40] отсюда как мне сделать так чтобы а у
[00:10:45] меня осталось к 1 a2b 34 д а б было как
[00:10:51] один a2b 34
[00:10:55] tz-9030 изменить функции может ли ты
[00:10:58] изменить эту функцию или можешь ли ты
[00:11:00] изменить как-то создании объекта бы
[00:11:03] чтобы по сути расщепить эти два dicota
[00:11:07] могу ли я функции добавить еще одну
[00:11:09] переменную вернуть ее конечно ты можешь
[00:11:11] делать все что угодно главное чтобы эти
[00:11:13] она вы хоть вот ты можешь изменить как
[00:11:15] угодно функцию но я хочу чтобы на выходе
[00:11:18] у меня а выглядел как один а два бо3 c4d
[00:11:22] а.б. как один a2b 34 д 11 вот эту ячейку
[00:11:27] ты можешь переписывать какую я хочу
[00:11:30] делать чтобы функция вернула мне два
[00:11:31] значения родное от него положили мне не
[00:11:35] лень из sub-sub она должна все также
[00:11:37] возвращать один тип а
[00:11:40] [музыка]
[00:11:43] еще да что мы хотим сделать а вот смотри
[00:11:47] тебе нужно переписать функцию
[00:11:50] таким образом чтобы
[00:11:53] запускали вот ячейку номер четыре
[00:11:55] следующую ячейку ты получил а равное 1
[00:12:00] a2b
[00:12:01] 34 д а б равное 1 a2b 34
[00:12:08] z99 то есть чтобы они изменилось а.б.
[00:12:11] хочу объяснить немного мотивацию к чему
[00:12:14] этот вопрос учить сдается потому что в
[00:12:18] это поведение в питоне она на самом деле
[00:12:20] несколько непредсказуем по но говорить о
[00:12:23] том что в случае если мы каким-то
[00:12:25] образом но вот касательно dato sand и
[00:12:27] касательно работ создание что если мы
[00:12:30] каким-то образом изменяем наш исходный
[00:12:31] dataframe внутри допустим какой-то
[00:12:34] функции то вы должны понимать что скорее
[00:12:37] всего изменение будет и place
[00:12:39] соответственно нам нужно очень аккуратно
[00:12:41] следить за тем хотим ли мы получить уже
[00:12:44] измененный data frame лишь мы хотим
[00:12:47] получить один дтп который был на входе
[00:12:50] отдельно и
[00:12:51] какой-то dataframe который прошел
[00:12:53] трансформацию через функцию отдельно
[00:13:02] [музыка]
[00:13:11] давай подумает что произойдет
[00:13:13] приравниваем значению б.а.
[00:13:15] видимо описать его нужно сначала
[00:13:18] потом в бой добавится за 99 возвращаем б
[00:13:22] а у нас останется не тронут и на выходе
[00:13:25] у нас будет
[00:13:28] хорошо
[00:13:30] давай запустим
[00:13:33] посмотрим что получилось запустить
[00:13:35] следующую ячейку точно также и давай я
[00:13:38] выведем а и b как или теперь выглядит
[00:13:47] до
[00:13:49] кажется не сработало
[00:13:52] вопрос почему что происходит когда мы
[00:13:55] пишем ровно при своему значению бы
[00:13:58] хорошо а давай вот в ячейке который
[00:14:03] предыдущий ряда 1 на 6 у тебя
[00:14:06] напишем print айди б после объявления б
[00:14:11] здесь
[00:14:15] далее давай запустим
[00:14:20] как дома что мы здесь видим ту же самую
[00:14:23] щеку памяти что и или на кажется что то
[00:14:26] идет не так и работает не так как мы
[00:14:28] думаем соответственно задача остается та
[00:14:31] же как мы можем расширить
[00:14:33] эти значения и
[00:14:36] не знаешь
[00:14:39] хорошо есть как минимум несколько
[00:14:42] вариантов как мы можем это сделать по
[00:14:44] сути своей нам все равно придется
[00:14:47] действовать следующим образом нам нужно
[00:14:49] будет но там с точки зрения как по
[00:14:52] памяти до занять новый дедсек по мы
[00:14:56] можем сделать несколькими вариантами
[00:14:59] самый простой будет года где-то и b
[00:15:02] равно а до написан магичить номер 5 да я
[00:15:07] понимаю вот здесь написать b равно а .
[00:15:11] копит
[00:15:15] запустить и запустить следующую
[00:15:21] значит можем увидеть что мы с точки
[00:15:24] зрения памяти теперь обращаемся в две
[00:15:26] различные лечить памяти и
[00:15:30] дальше если ты посмотришь на pride aeb
[00:15:35] то можно увидеть что мы по сути своей
[00:15:38] сделали два различных dicota
[00:15:41] помимо папе и есть там понять эдип копия
[00:15:45] копии или можно был вот прям функции foo
[00:15:48] сделать новый словарь холке and views
[00:15:52] from
[00:15:53] сделать просто новый дик ну то есть по
[00:15:57] сути своей сделать deep копи
[00:16:01] все это нужно нам для того чтобы
[00:16:03] понимать вообще как работает память
[00:16:05] отсюда и следующий вопрос который могут
[00:16:08] задать на собеседовании по бетону как
[00:16:10] работает память в питоне а именно каким
[00:16:13] образом она очищается и каким образом
[00:16:17] оно выделяется вопрос достаточно большой
[00:16:20] но хотелось бы чтобы отвечающих он
[00:16:23] дискутируем это наверное ничего сказать
[00:16:26] очень
[00:16:29] короткий ответ будет звучать следующим
[00:16:33] образом очистка памяти и дело с помощью
[00:16:36] к данной школе
[00:16:37] очень часто
[00:16:40] старых скриптах питона можно увидеть
[00:16:43] такой и проси и delphi . коллег который
[00:16:47] принудительно заставляет галочками
[00:16:49] пройти и собрать условно очищенную
[00:16:52] ячейку память значит в чем идея в том
[00:16:57] что garbage collector идет погоду
[00:17:00] смотрит на ссылки на 10 памяти если
[00:17:02] ссылок на ячейку памяти активно
[00:17:05] дальнейшем метод а она забираю этот
[00:17:08] парень и таким образом очищать значит
[00:17:12] есть всякие нюансы связаны с тем как у
[00:17:15] нас работает карточка лектору о функциях
[00:17:19] про то как работает гарбич коллектора в
[00:17:22] классах когда мы создаем какие-то вещи
[00:17:25] внутри класса каким-то образом нишевым и
[00:17:28] так далее вот с точки зрения выделения
[00:17:31] памяти наверное очень интересно смотреть
[00:17:35] про то как идет выделение памяти в в
[00:17:38] питоне во время работы с листами
[00:17:40] особенно когда мы добавляем что то есть
[00:17:43] если у нас функция art and для ресторана
[00:17:47] позволяет добавить какой то есть причем
[00:17:50] сам князь и
[00:17:52] наверное интересно посмотреть на то как
[00:17:54] выделяется память в момент когда мы
[00:17:57] добавляем добавляем добавляем добавляем
[00:17:59] а вылез новые все новые и новые ленты на
[00:18:04] самом деле резервации там идет
[00:18:06] резервации памяти и
[00:18:08] можно читать друг почитать как и меня
[00:18:11] это происходит но общая идея
[00:18:13] общая логика
[00:18:15] [музыка]
[00:18:16] состоит в том что смотрится на
[00:18:19] заполнение листа то есть резервируется
[00:18:22] какая память идет наполнение этой памяти
[00:18:26] в момент какой-то когда переходит
[00:18:29] какой-то порог резервируется больше
[00:18:31] количество памяти и дальше типа ведет
[00:18:35] заполнен заполнен исполнении потом
[00:18:37] резервируется и еще и еще и еще и на
[00:18:40] самом деле листая достаточно прожег бы
[00:18:42] случай в питоне то что она может
[00:18:45] занимать памяти побольше чем клей нужно
[00:18:48] на самом деле за счет того что здесь
[00:18:49] выгоду резервирование все больше мог бы
[00:18:52] больше приступать но это там нюансы
[00:18:55] нужно смотреть опять документации в
[00:18:58] питании может играть как станете
[00:19:00] разобрались с типами данных типе данных
[00:19:03] по вере очень часто еще спрашивает про
[00:19:05] генераторы операторы декоратор питоне
[00:19:08] что это такое чем например оператора от
[00:19:12] генератора отличать и вообще что такое
[00:19:15] декоратор питон я читала все это знакомо
[00:19:18] но
[00:19:20] хорошо на практике может быть что-то
[00:19:24] использовалась при виде пожалуйста
[00:19:26] примеры оператора декоратора но давай
[00:19:28] декоратор примеры использования пример
[00:19:31] используем давайте я приведу только один
[00:19:33] пример и декораторами и пример
[00:19:35] использования это когда мы перед функции
[00:19:37] перед функции пишем такую собачку и
[00:19:40] название декоратор да я понял нет не
[00:19:43] пользовался
[00:19:44] окей хорошо ну я тогда с твоего
[00:19:47] позволения не буду распространяться
[00:19:49] здесь просто действительно напитки очень
[00:19:52] много что можно рассказать про то как
[00:19:55] или встроенные
[00:19:56] опять-таки в этом с точки зрения
[00:19:58] бетонного часто спрашивают про всякие
[00:20:01] static метод close метод декораторы вещи
[00:20:04] которые используются в
[00:20:06] объектно-ориентированном
[00:20:07] программировании в питоне есть
[00:20:09] [музыка]
[00:20:10] множеством нюансов про то как именно
[00:20:12] используется как работают это сейчас все
[00:20:17] опущу давай тогда переходите к следующей
[00:20:20] теме то есть следующей секции потому что
[00:20:23] секция по бетонного к сожалению она
[00:20:25] вообще не пройдена мы даже не будем
[00:20:28] брать какую-то задачку на простые
[00:20:31] алгоритмы мы перейдем сразу к следующей
[00:20:34] секции как думаешь какая секция тебе
[00:20:38] было бы интересно следующий
[00:20:41] apts у в тяжелый и конечно ну достаточно
[00:20:45] тяжелый вариант взял что мы можем
[00:20:48] рассказать про быть с так ну я честно не
[00:20:52] знаю как спрашивает в других местах я же
[00:20:56] всегда пытаюсь расспросить у человека
[00:21:00] как бы он проводил
[00:21:03] принципе дмитрий сейчас ты можешь и
[00:21:05] будущий шильдик экрана потому что мы
[00:21:08] ничего не будем писать
[00:21:10] однако ты можешь все на листочке
[00:21:13] записывать какие-то
[00:21:15] вещи которые вам позволят тебе ответит
[00:21:18] такой кейс вопрос давай дам тебе простой
[00:21:22] вариант проведения pt100 зависимость
[00:21:25] опять-таки в зависимости от уровня в
[00:21:27] зависимости от того работал ли уже
[00:21:29] человека нет задаются различные вопросы
[00:21:32] я задам простой вопрос представь себе
[00:21:35] представьте что у тебя есть некоторая
[00:21:38] рекомендательном адель или
[00:21:39] рекомендательных систем ваш некоторые
[00:21:42] рекомендательные системы для их сайт
[00:21:45] рамках этого сайта уже какое то время
[00:21:47] назад был блог
[00:21:50] который спалит заполнялся каким-то
[00:21:53] рекомендуешь ну какой то
[00:21:55] рекомендательный модель значит так к
[00:21:58] тебе приходит product этих рекомендаций
[00:22:01] говорит дмитрий мы запускали новую
[00:22:05] модель угаре календарь и хотим оценить
[00:22:08] эффективность новой модели и хотим чтобы
[00:22:12] ты сделал так называемый дизайн
[00:22:14] эксперимент что это значит в рамках
[00:22:18] дизайн эксперимент это должен ответить
[00:22:20] на несколько основных вопросов первый
[00:22:22] вопрос на какие метрики мы будем
[00:22:24] смотреть как мы будем оценивать
[00:22:26] эффективность работы рекомендательных
[00:22:28] модель предположить если не знаешь ну я
[00:22:31] тебе помогу подскажу это 1 2 темы тебе
[00:22:36] нужно предложить разбиение
[00:22:39] людей на основе какого-то понимания
[00:22:42] вообще того как работают от теста и
[00:22:45] 3 тебе нужно провести то есть
[00:22:48] представьте себе что эксперимент прошел
[00:22:50] то есть ты сделал выбрал метрики сказал
[00:22:54] как будем делить пользователей села
[00:22:56] команда пошла начала делать эксперимент
[00:22:59] действительно каким-то образом делит
[00:23:01] людей на группы
[00:23:04] тебе нужно сделать оценку
[00:23:06] результатов qstring чем подробней ты
[00:23:09] расскажешь тем будет лучше у тебя где-то
[00:23:11] 20 20 минут на то чтобы 1 из 1 все так
[00:23:17] octopus
[00:23:19] отвечать не как сделать первые ты мы
[00:23:23] определяемся с метриками если говорить
[00:23:24] про рекомендательных систем у
[00:23:27] меня нет большого опыта но видимо мы что
[00:23:30] то рекомендуем люди либо как либо
[00:23:31] кликают либо покупают это
[00:23:35] нота желаемой что мы хотим наблюдать
[00:23:37] соответственно это будут наши метрики
[00:23:40] допустим пусть это будут клейкие пусть
[00:23:42] это будут
[00:23:43] блики и покупки мы можем видеть
[00:23:47] это будет критерием там
[00:23:49] заинтересованности и качеству работы
[00:23:52] новой рекомендаций системы мы
[00:23:54] определились с двумя метриками они нам
[00:23:55] интересны мы хотим выбрать группы на
[00:23:59] которых будем проводить эксперимент
[00:24:01] соответственно одной группе будет
[00:24:02] показана
[00:24:03] одной группе будет даваться старая
[00:24:06] рекомендации система другую руку будет
[00:24:08] даваться ногу рекомендуется система
[00:24:10] группы
[00:24:12] соответственно мы хотим чтобы они были
[00:24:15] как это называется
[00:24:18] они были однородными чтобы в
[00:24:21] и не различались между собой по
[00:24:24] по составу по составу людей по качеству
[00:24:26] здесь так можно сказать да чтобы грубо
[00:24:28] говоря нас не получилось так что в одной
[00:24:30] группе терку мальчики другой только
[00:24:31] девочки мы хотим что в каждой группе
[00:24:33] были равные количества мальчиков равное
[00:24:36] количество девочек
[00:24:37] пропорционально равная 1 группы из 2 ну
[00:24:40] и соответственно по остальные признаком
[00:24:42] которые у нас есть допустим возраст
[00:24:45] допустим география
[00:24:47] если мы только в центральном регионе
[00:24:49] проводим соответственно особе группы
[00:24:52] при прочих равных условиях центрального
[00:24:54] региона понять что эти группы
[00:24:57] одинаковые
[00:24:59] что они подходят для этого эксперимента
[00:25:01] мы можем оао тестом мы берем эти две
[00:25:06] группы снимаем с них
[00:25:08] показания интересующих нас метрик и
[00:25:10] проводим артист соответственно а а тест
[00:25:15] на покажет есть ли статистически
[00:25:16] значимые различия между этими двумя
[00:25:18] группами если представить что мы хорошо
[00:25:21] отобрали себе группы и они на подходят
[00:25:23] что они абсолютно
[00:25:26] абсолютно что они достаточно разные
[00:25:28] одинаковые там и первой группе
[00:25:31] продолжаем оказывает старые рекомендации
[00:25:33] разрубим показываем новые рекомендации
[00:25:35] кроме того перед тем как приступить мы
[00:25:37] определяемся с нам нужно понять какое
[00:25:41] количество наблюдений мы хотим потому
[00:25:43] чтобы наши выводы имели вес имели
[00:25:45] какое-то значение если представить что
[00:25:47] мы
[00:25:48] во второй группе у нас оказалась здесь
[00:25:50] человеком первой группе еще 2 10 человек
[00:25:53] то можно говорить о том что это
[00:25:55] предполагает что это не достаточное
[00:25:57] количество есть калькулятор она в том
[00:25:59] числе вот на на курсах карпова мы
[00:26:01] считали руками
[00:26:03] необходимый объем выборки необходимый
[00:26:05] объем группы который нам нужен для того
[00:26:07] что провести эксперимент
[00:26:09] я наверное не вспомню конкретные
[00:26:12] уравнение формула но там опять же если
[00:26:14] мы калькулятор откроем то там нам
[00:26:15] предложат ввести различие которые мы
[00:26:17] хотим наблюдать мощность критерия порог
[00:26:21] на которую мы хотим
[00:26:23] некий порог
[00:26:25] некий
[00:26:27] различий который мы хотим заметить
[00:26:30] по моему все и мы таким образом получаем
[00:26:33] необходимо необходимо число наблюдений
[00:26:35] которая нам нужна для того чтобы сделать
[00:26:38] какие-то выводы допустим тем мы провели
[00:26:40] эксперимент у нас есть для гроба
[00:26:43] значений по каждой метрики далее мы их
[00:26:46] сравниваем сравниваем с помощью
[00:26:48] статистических тестов мы хотим оценить
[00:26:51] распределение первой выборке то которые
[00:26:54] у нас было на
[00:26:55] старой рекомендательной системе
[00:26:58] принципиально будет ли она носить
[00:27:01] нормальный характер ты какой-то другой
[00:27:03] характер
[00:27:05] от этого зависит этот тест который мы
[00:27:08] выберем либо параметрически либо
[00:27:09] непараметрический если она носит
[00:27:12] распределение выборки если растление
[00:27:14] выбор клип носит не нормальный характер
[00:27:16] то из того что мы делали мы пытались
[00:27:20] привести ее к
[00:27:22] нормальному через логарифмирование еще
[00:27:25] какой-то способ не помню если
[00:27:29] прости пожалуйста пока ты не ушел далеко
[00:27:32] в сторону вспомни метрики case метрики
[00:27:35] ты выбран за конверсию криком версия
[00:27:37] покупка вопрос откуда там распределения
[00:27:40] конверсия конверсия в покупку это просто
[00:27:42] цирк хотелось бы чуть больше про по
[00:27:45] тестам
[00:27:46] потому что кажется что это важно по сути
[00:27:49] у нас на выходе будет по первой группе
[00:27:51] по одной метрики две цифры тех кто
[00:27:53] кликнул и те кто не кликнул по 2 метрики
[00:27:57] но считаю что то же самое те кто купил и
[00:27:58] те кто не купил я вспоминаю
[00:28:00] статистический критерий для доля да там
[00:28:03] действительно выборки нет там немножко
[00:28:04] по другому дану соответственно применяем
[00:28:07] эстетический критерий для сравнения двух
[00:28:09] долей
[00:28:10] не вспомнил я могу даже могу наверное
[00:28:13] написать формулу потому что я решал
[00:28:15] задачи и она у меня осталась
[00:28:17] без
[00:28:21] t-статистика на корень квадратный из
[00:28:24] доля купивших допустим then умножить на
[00:28:27] единице минус доля не купивших разделить
[00:28:29] на вообще количество наблюдений хорошо
[00:28:32] дмитрий давай так про дизайн
[00:28:34] эксперимента в целом все говоришь про
[00:28:36] меня все говоришь про ну то есть ты
[00:28:39] говоришь о том что мы берем смотрим на
[00:28:43] метрики то есть выбираем 2 метрики как
[00:28:45] тир и конверсия клип конверсии в покупку
[00:28:48] супер супер что ты предложил в минимум 2
[00:28:51] по факту нужно предлагать чуть больше
[00:28:53] нового для это уже клёво ты клёво очень
[00:28:56] сказал про а тест про то что должны быть
[00:28:59] люди которые похожи друг на друга мы их
[00:29:01] там равные единственно что не сказал это
[00:29:05] в каких долях мы делим типа 50 на 50 или
[00:29:08] мы делим как вдруг у но есть еще и
[00:29:11] усложнения которые тоже бывают и она
[00:29:14] очень часто бывает и хороший аналитик
[00:29:17] должен задать вопрос а какой нос трафик
[00:29:20] как много событий у нас прилетает потому
[00:29:23] что если собрать очень много прилипает
[00:29:26] то есть смысл взять только часть людей
[00:29:29] допустим 10 процентов людей которые
[00:29:32] заходят и на 10 процентов проводить
[00:29:34] очень весь экспериментов 10 процентов а
[00:29:37] затем поделить допустим 50 на 50 1 дать
[00:29:40] одну рекомендательным огарев другой дать
[00:29:42] другой
[00:29:43] или просто сделать 91
[00:29:46] 1090 со вторым отбеливать 10 снова
[00:29:49] будильником условно
[00:29:51] но вопрос про количество событий которые
[00:29:54] генерируются он на самом деле важен
[00:29:57] затем ты все правильно сказала что есть
[00:29:59] вопрос связан с тем чтобы рассчитать
[00:30:02] сколько событий
[00:30:03] данном месте так называемый консул или
[00:30:06] порог который попытался вспомнить есть
[00:30:08] int age- и вынимаем детектирует эффект
[00:30:11] что еще ну там можно всякий вода есть
[00:30:14] еще может супер счет сказал супер
[00:30:16] наверное не буду бальзамом на душу бы уж
[00:30:19] тут и протез сказал про историю про то
[00:30:22] что мы проверяем затем смотреть когда
[00:30:26] пошла оценка пошел росси chrome да
[00:30:30] немного в различные стороны начал
[00:30:32] смотреть немного ушел прямо начал
[00:30:35] выходить не туда я понимаю что ты
[00:30:37] говоришь про пироман перечисление про
[00:30:39] металлическими варианты но
[00:30:42] вопрос откуда либо возьмите если у нас
[00:30:45] распределение нет у нас проснись цифры
[00:30:47] цикл правильный ответ что были две нити
[00:30:50] распределения на генерирует можно ну
[00:30:53] типа вообще крик меня вопросы на
[00:30:54] генерировать эти распределения отсюда
[00:30:57] вопрос как мы можем сгенерировать
[00:30:59] распределение исходя из наших вот
[00:31:03] выборок представь что ты взял к дереву
[00:31:05] людей 5050 взятом допустим 10 людей
[00:31:09] поделилась 5050 как мужу из них получить
[00:31:14] распределяем конверсия конверсия
[00:31:17] конверсия а мне кроме быстро приходят
[00:31:21] так вот он и есть он есть
[00:31:25] смысл чём смысл в том что если мы просто
[00:31:29] циферки сравниваем до конверсия в
[00:31:32] конверсию покупку то мы используем так
[00:31:34] называемый хи-квадрат это вот то что то
[00:31:37] пытался вспомнить надаль агс достаточно
[00:31:40] долях идеально работает так далее но там
[00:31:44] 10 вариант когда ну не использовать
[00:31:46] хи-квадрат а вот берем
[00:31:48] быстро-быстро пируем мы быстро пируем
[00:31:51] доли для всех книг и конверсию покупку и
[00:31:54] смотрим на вот эти распределения они по
[00:31:58] дефолту будут
[00:32:00] нормальные
[00:32:02] соответственно для будет скопирован их
[00:32:05] конверсий вклейкой конверсии покупку
[00:32:08] какой-то с мы будем применять
[00:32:11] тест это супер супер
[00:32:15] какие ограничения половинки test is now
[00:32:18] желаемое количество наблюдений приходит
[00:32:20] в голову будет предполагаем что она
[00:32:22] будет каким-то большим нормальность
[00:32:24] распределения вот этот момент он на
[00:32:28] самом деле этот вопрос встает
[00:32:31] нормальности распределения самом деле
[00:32:33] это . спора я специально задал этот
[00:32:36] вопрос специально задолго просто
[00:32:38] ограничение почему потому что
[00:32:41] здесь можно много дискутировать на тему
[00:32:44] обязательно людей должны быть нормальное
[00:32:47] распределение дтп
[00:32:48] или они должны быть симметричны потому
[00:32:51] что есть нюанс в том как мы смотрим на
[00:32:55] значит мышцы пресса можно ли мы его
[00:32:58] использовать и можем ли мы его
[00:33:00] использовать для ненормальных
[00:33:01] распределений в скобочках можем но там
[00:33:07] есть определенные нюансы почему можно
[00:33:09] использовать и без на даже не на не
[00:33:11] нормальное распределение при условиях
[00:33:15] есть нюанс реально можно почитать лучше
[00:33:18] читать зарубежную литературу или очень
[00:33:21] хорошо вот мне нравится там ребята языке
[00:33:23] x tf которые прикольно об этом
[00:33:25] рассказывают и у них можно почитать
[00:33:27] статьи нормальность распределения это
[00:33:30] некоторые упражнения на самом деле
[00:33:31] который очень часто преподается но
[00:33:34] которое не является истинным последней
[00:33:36] станции и этот момент он право дискуссий
[00:33:39] то есть мы должны пообсуждать почему
[00:33:41] обязательно нормальное распределение или
[00:33:43] ненормальная и и можем ли мы
[00:33:45] использовать по ним больных теперь какие
[00:33:48] у нас есть проверки на нормальность что
[00:33:49] приходит голову
[00:33:52] есть несколько тестов
[00:33:54] shopper и мелко по-моему
[00:33:57] в источниках описывается несколько они
[00:34:00] все приравниваются примерно говорят что
[00:34:03] они равна равнозначны дает похожий
[00:34:06] результат и тем не менее у разных а у
[00:34:08] разных авторов из разные предпочтения из
[00:34:11] того что я делал sape.ru вилка тест
[00:34:14] наверно все
[00:34:15] хорошо супер супер но лучше всего иметь
[00:34:19] как минимум там 2 ответа пей спеша
[00:34:22] первые уже хорошо и
[00:34:24] если у нас опять таки ненормальное
[00:34:28] деление как мы можем сравним два
[00:34:30] ненормально проследить есть
[00:34:33] непараметрические тесты один из помнишь
[00:34:36] parametric это стьюдента не parametric а
[00:34:39] это монолит не супер почему-то в
[00:34:42] источниках он единственно их на самом
[00:34:43] деле там много в теории вот во всяком
[00:34:47] случае в жизни применяют либо тит если
[00:34:49] бы волна with a наверное из-за того что
[00:34:52] мама ведь достаточно ну популярен в
[00:34:55] принципе я его достаточно просто
[00:34:57] реализовывать прощать просто теле хорошо
[00:35:01] супер супер
[00:35:03] дальнейшие вопросы которые могли бы быть
[00:35:05] это как работает с как именно работает и
[00:35:09] гитарист этого он же мало ведь нет и
[00:35:11] наверное последний вопрос который я бы
[00:35:14] задал
[00:35:15] такой абэ слэш статистике это почему же
[00:35:20] у нас требует стракера ваней при быстро
[00:35:22] первыми доме будут виде некоторого
[00:35:25] нормального растут давай я и даже не
[00:35:28] дали упростить или вопрос чем средний
[00:35:31] при быстро перова нее будут виде
[00:35:34] нормально
[00:35:35] волшебная центральная предельная теорема
[00:35:38] супер
[00:35:39] этого достаточно то что я сказал сейчас
[00:35:42] в доказательство в какие-то более
[00:35:45] подробные вещи там такая математика
[00:35:46] безумно короткий ответ что да вот
[00:35:50] из
[00:35:52] данного
[00:35:53] клёвый если ты можешь вспомнить очень
[00:35:57] описание пятеро не какой-то
[00:35:58] доказательство это будет звучать
[00:36:00] офигенно но в целом в целом достаточно
[00:36:03] значит она на будущее просто сразу скажу
[00:36:06] что там для людей которые уже имели опыт
[00:36:11] создание там и проведение apts дизайн
[00:36:15] экспериментов тогда она фанерный есть
[00:36:18] несколько проблем в
[00:36:20] тех же рекомендации что у нас есть
[00:36:25] допустим там store пользователи по
[00:36:27] которым ты можешь сделать а тест а для
[00:36:29] новых пользователей как что мы будем
[00:36:31] делать на новых пользователей и т.п. на
[00:36:34] самом деле здесь все вариант ответа мы
[00:36:36] будем пробовать сделать честный рандом
[00:36:39] то есть честно делить вне зависимости от
[00:36:42] того какие люди на две равнозначные
[00:36:46] группы
[00:36:47] честный рандом можно сделать через
[00:36:50] подсчет сша на человека и остаток а тени
[00:36:56] на что то это будет там при ранец если
[00:36:59] bug1 либо к другой группе я считаю что
[00:37:00] таким образом независимо от пола
[00:37:03] возраста географии национальности мы вот
[00:37:06] через этих и шик мы сделал выборку прямо
[00:37:10] на у нас будет вот идеально рандомно и
[00:37:11] она будет похоже на то что ну типа тесли
[00:37:16] у нас очень большой трафик сайт the
[00:37:18] random честный рандом он действительно
[00:37:21] разделит людей на две группы они будут
[00:37:23] похожи друг на друга реально это так
[00:37:26] однако если у нас трафик помочь большой
[00:37:29] у нас есть частицы фика какая-то по
[00:37:31] работе нашего сервисы которые
[00:37:35] рекомендации показывай то да есть нюанс
[00:37:38] что может быть такое что в одной группе
[00:37:40] одни люди в такой группе другие но
[00:37:42] честный рандом там по факту
[00:37:45] предполагается что он действительно по
[00:37:46] дереву купола
[00:37:48] прошу это
[00:37:50] одна часть которой я хотел сказать и
[00:37:53] теперь про задач и вообще какие задачи
[00:37:55] бывают ну вот этот вариант c
[00:37:57] рекомендовать наверно самый простой прям
[00:37:59] самый простой вариант которые спрашивают
[00:38:01] по обед с виду который я спрашивать
[00:38:04] честно сложно судить но который я
[00:38:07] спрашиваю которому мне иногда она но вот
[00:38:11] я на собеседование тоже хожу и меня
[00:38:12] иногда спрашивают про дизайн супер
[00:38:15] сложный вариант это рекомендуешь к
[00:38:18] только-только запускается раньше не было
[00:38:20] рекомендательного блока и нам нужно за
[00:38:22] дизайну текст рин лтд тест типа как это
[00:38:25] сделать почему потому что у нас как бы
[00:38:28] нету
[00:38:29] старой модели рекомендации нам нужно
[00:38:31] предложить что-то взамен старые модели
[00:38:33] рекомендации вообще предложить вариант
[00:38:36] дизайна эксперимент
[00:38:39] этого усложнения задачи про рекомендации
[00:38:41] затем а ты говорил про некоторые факторы
[00:38:44] например один округе а это и говорил про
[00:38:48] центральную часть чтобы если мы будем
[00:38:50] тестировать центральной части это очень
[00:38:52] хороший момент почему потому что есть
[00:38:54] так называемый биотест
[00:38:56] это
[00:38:58] следующем усложнение что мы хотим
[00:39:01] провести его в каком-то регионе
[00:39:03] привести такую 3 can проверку
[00:39:06] рекомендательных моделей я помню у меня
[00:39:08] тогда еще это фейсбук ты вот в компании
[00:39:12] фейсбук спрашивали про то как бы я
[00:39:15] приводил дизайн эксперимент too b
[00:39:20] для
[00:39:21] реакции на сообщение там очень важно
[00:39:24] говорить о том что для определенного
[00:39:28] гео-локации мы запускаем одни реакции
[00:39:30] для другой гео-локации другие реакции и
[00:39:32] мы
[00:39:33] должны подобрать как бы контроль
[00:39:37] относительно деву
[00:39:39] этот момент он очень тяжелый очень
[00:39:43] непростой нужно смотреть на него
[00:39:46] отдельно . gearbest и вообще лучше
[00:39:50] погрузиться в это посмотреть как это
[00:39:52] работает ну и там важным прям отдельный
[00:39:56] плюсик был за то что я предложил вариант
[00:39:58] теста
[00:39:59] когда мы на одном регионе одни реакции
[00:40:03] на другом другие а затем меняемся
[00:40:06] вот варианты switchback тестов это тоже
[00:40:10] очень хороший вариант как мы можем
[00:40:12] рассказать про наши тесты
[00:40:15] вот ну и самые сложен сам четвертый
[00:40:19] вариант который редко обсуждается но
[00:40:21] этот тест и без контрольной группы как
[00:40:25] как оценить тест без контроля
[00:40:29] про подбор контроля ну тут есть
[00:40:32] несколько вариантов как это проходит это
[00:40:35] достаточно тяжелая вещь не простая но
[00:40:38] в целом в интернете тоже можно найти про
[00:40:41] эксперименты про то как это все делается
[00:40:44] про вариант проведения теста без как рук
[00:40:47] ну и оценки эффективности
[00:40:49] да с точки зрения оценки эффективности я
[00:40:52] всегда говорим про вещи связаны со ну и
[00:40:55] типа у нас там нулевая гипотеза
[00:40:56] подтверждаем или опровергая миру у нас
[00:40:59] есть старт с то а затем 2 вопроса
[00:41:02] насколько одна модель лучше другой ну
[00:41:05] здесь не bootstrap на самом деле он
[00:41:07] может помочь ответить и на вопрос
[00:41:09] насколько одна модель dodge другой и ну
[00:41:13] ответь на вопрос
[00:41:14] отличается дней 2 рекомендаций модель и
[00:41:17] от касательно вот конкретных задач boost
[00:41:20] ратного покажутся средний которые яркие
[00:41:23] зрение которые выглядят 1 по 2 не совсем
[00:41:26] среднем не пока ждали конверсии покупок
[00:41:28] и конверсий птиц это не среднем все таки
[00:41:30] это не тони но они будут нормально мы
[00:41:34] можем во-первых сравнить эти два
[00:41:36] нормальных распределения понять что они
[00:41:38] различны а затем сказать насколько не
[00:41:40] различное
[00:41:42] значение ну то есть мы считаем
[00:41:44] медиальную долю плюс какой-то на
[00:41:47] стандартного кабеля с минус тип матрасик
[00:41:51] мы попали в зависимости от того как мы
[00:41:52] хотим посмотреть хорошо про оба теста
[00:41:56] закончили на давай переходите дальше что
[00:41:59] выбираешь работа с данными и
[00:42:04] работаем правильное решение
[00:42:07] наверное нам
[00:42:09] в какой-то момент придется вернуться в
[00:42:12] holland но давай сейчас просто несколько
[00:42:16] вопросов of
[00:42:17] summer на первый вопрос есть у нас
[00:42:20] гудбай функция в сквере смотри работа за
[00:42:24] нами она в основном про без курить и я
[00:42:27] буду спрашивать про тока там типа писать
[00:42:29] в том числе и вскоре запрос но если у
[00:42:33] тебя там не было опыта работы с куриным
[00:42:36] я спрашиваю про pandas если
[00:42:39] был опыт работы с по я спрашиваю послан
[00:42:43] работа с нами это общие вопросы связано
[00:42:46] с тем как он выдаст ими данные фехтовать
[00:42:50] и тогда вопрос он был ли у тебя опыт
[00:42:52] работы сына исходит
[00:42:56] с каким базам данных на работу house и
[00:42:59] пусть греет а называется скулы супер
[00:43:03] супер пушку гонг и так первый вопрос
[00:43:07] если нас грубой
[00:43:09] [музыка]
[00:43:11] силе что-то
[00:43:14] oh-группой и тогда
[00:43:16] вопрос есть хелен и есть в оба варианта
[00:43:23] накладывают каким-то образом условия
[00:43:25] вопрос как работает и как работает и чем
[00:43:29] они отличаются друг от друга но
[00:43:31] синтаксически вы всегда будет перед
[00:43:34] грубо если будет грубой не помню может
[00:43:37] быть они даже не дружит но
[00:43:39] heaven накладывается на то что
[00:43:41] сортировка грубое тело
[00:43:45] грубая потом heavy но может быть в
[00:43:48] разных диалектах я уже сталкивался с
[00:43:50] этим что в теории как будто бы они они
[00:43:53] не должны дружить хэви и грубая хэви и в
[00:43:56] они могут оказаться в этих запросов до
[00:43:59] могут быть но у меня одновременно это
[00:44:02] работал из опыта
[00:44:04] но камень привязан грубая когда мы
[00:44:08] отсортировали соответственно понимает
[00:44:10] уже ну грубо
[00:44:13] группой из очень транспортировку утра
[00:44:16] агрегат
[00:44:18] хорошо супер супер а теперь можно
[00:44:22] женских вспомнить опять таки я тебе
[00:44:24] задаю вопросы для реджину поэтому они
[00:44:27] будут максимально простыми можешь
[00:44:29] пожалуйста вспомнить все варианты join
[00:44:31] или ружжо и jo in love джо играли join и
[00:44:36] есть еще outer join на самом деле больше
[00:44:41] но истец которых сталкиваться 4 который
[00:44:44] не романа край применял я щас напишу в
[00:44:46] коробе значит а я представь себе что нас
[00:44:49] есть таблица а таблицы до в таблице 100
[00:44:52] записей в таблице б 50 записей
[00:44:55] пересечение а теперь это 25 записей
[00:44:58] вопрос
[00:44:59] лев join a и b и какое количество строк
[00:45:04] будет сторону училась будут надо
[00:45:06] насколько я понимаю да конечно будет
[00:45:10] стоить она теперь
[00:45:14] 150 супер an inner join 25 хорошо outer
[00:45:20] join
[00:45:21] окружен не сталкивался ну вот поскольку
[00:45:23] я помню два шарика они перекрываются у
[00:45:26] нас и серединке не будет не будет 25 125
[00:45:31] хорошо
[00:45:33] теперь full джон по 150 супер и теперь
[00:45:39] вопрос есть еще cross join о нём редко
[00:45:42] помнят о нем даже не знаю никто не
[00:45:45] сталкивался это декард во произведений
[00:45:48] дикарка и произведения то есть каждый
[00:45:51] скажем она будет 100 на 50 вот ну
[00:45:55] соответственно хорошо
[00:45:57] тебе какую задачу дать ты про
[00:46:02] всякие оконные функции знаешь наверное
[00:46:06] нет что мы называем
[00:46:09] которая исполняется в окне как можно
[00:46:12] догадаться по хорошо хорошо
[00:46:16] точнее плохо
[00:46:18] оконные функции это наверное одно из
[00:46:20] самых частых что спрашивается оконной
[00:46:23] функции высчитаем вот тебе ним который в
[00:46:26] том числе у меня может быть до
[00:46:28] как ни странно оконной функции сейчас
[00:46:31] это в том числе минимум который нужен
[00:46:34] для junior дат аналитика
[00:46:38] ну я искренне считаю что действительно
[00:46:40] они должны быть потому что есть вопросы
[00:46:44] связанные с
[00:46:46] почетом скользящего среднего там очень
[00:46:51] часто их спрашивать или
[00:46:53] можно смотреть давай наверное вопрос
[00:46:55] будет на то как работает группа и
[00:46:58] функции но это вопрос такой с полок
[00:47:02] почему потому что
[00:47:04] тебе грубой функцию можно будет
[00:47:07] реализовать том числе на бетон я написал
[00:47:09] два листа вклада в задача передавать
[00:47:12] группы сам функцию который на вход
[00:47:16] принимает а и b
[00:47:18] листы а на выходе должна получить
[00:47:23] диктует а
[00:47:26] значение плюс
[00:47:28] [музыка]
[00:47:37] так
[00:47:39] сохраняю попробую посмотреть на кого-то
[00:47:42] и
[00:47:43] попробуй пожаром он пожалуйста еще разок
[00:47:46] расшарить экран значит смысл в чем вот
[00:47:50] этого занятия
[00:47:52] реализации группой сам смысл в том что к
[00:47:54] сожалению я не знаю на сколько прошло
[00:47:58] понимаешь как работы групп функция но на
[00:48:00] самом деле оно там в питоне
[00:48:02] в панасе работает определенным образом
[00:48:05] тебе же нужно реализовать самую простую
[00:48:08] функцию которая на вход принимает list a
[00:48:11] и b они должны быть сервер брось бы они
[00:48:14] 1 одного размера и на выходе я должен
[00:48:18] включить dict у нас есть a b c вот эти
[00:48:23] ключи и для каждого из ключей посчитать
[00:48:26] сумму значения которые а где а в листе а
[00:48:30] ключи это значение которое есть нас т.п.
[00:48:34] а сумма это значение которые есть
[00:48:37] система не так сложно дала еще раз у нас
[00:48:39] есть a b c плести б разбросанные
[00:48:42] каким-то образом есть
[00:48:44] a123 49 досмотри представь себе таблицу
[00:48:49] в голове и представь себе таблицу у тебя
[00:48:52] есть таблица ключица значение а единица
[00:48:57] затем ключ и значение ключа 2 ключ
[00:49:03] 3c
[00:49:06] a5
[00:49:08] a6
[00:49:09] c7
[00:49:12] a8 b делится 9 вот это вот таблица и
[00:49:17] теперь нужно сделать
[00:49:19] грубой б получается грубой б а
[00:49:24] . сам родов в памяти этап это
[00:49:29] все что тебе нужно это типа взять
[00:49:32] уникальное значение из б это цербер и
[00:49:34] для них посчитать сумму всех значений
[00:49:37] которые вот и есть в
[00:49:39] ну я бы видел это как цикл супер напиши
[00:49:44] ну а это весь цикл но типа ты видишь это
[00:49:48] как цикл добавится кого напишу мы сейчас
[00:49:51] не у пару и вся с точки зрения как это
[00:49:54] лучше написать и так далее нам просто
[00:49:56] нужно сделать сделали проговорил давай
[00:50:00] проговори логику цикл длину
[00:50:04] длину вот этого листа в цикле я бы
[00:50:08] обозначил 3 переменная b c идя по циклу
[00:50:12] обращаясь к самой простой 3 условие if i
[00:50:17] в б такое избитый равно цвету c + а это
[00:50:22] и так далее да не слушай ты усложняешь
[00:50:26] честно говоря потому что ты здесь
[00:50:27] пытаешься pointer какие тут сквозь его
[00:50:29] цена этого не нужно тебе нужно просто
[00:50:33] пройти по
[00:50:34] вот этой связке а.п. давай сделаем
[00:50:37] первый шаг это получить dict у которого
[00:50:40] есть ключ виде какого-то значением
[00:50:44] уникального значения п а в значениях
[00:50:47] будет лезть из всех тех значений которые
[00:50:49] мы соберем сначала где нет смысле не
[00:50:53] хочет принимали нет не понимаю где
[00:50:55] поделать менять для меня потерь давай
[00:50:57] еще раз задачу нужно посчитать сумму ну
[00:51:01] агрегацию агрегацию покличу в
[00:51:05] посчитать сумму
[00:51:07] нам нужно сделать если вы вот в pandas
[00:51:10] если в память давай давай а даже
[00:51:13] сделаем напишем fantasy как я это вижу
[00:51:18] делаем импорт пандус спд
[00:51:23] делаем
[00:51:25] без видим
[00:51:31] здесь
[00:51:34] будет у нас dict виде
[00:51:39] большого и
[00:51:41] значение
[00:51:47] большого значения и
[00:51:58] e-bike б . а
[00:52:02] . сам и
[00:52:07] на мне закрыть тег вот и сохраню можешь
[00:52:13] пожалуйста
[00:52:14] перезагрузить страничку она тогда
[00:52:18] быстрее обновится и в самый низ и
[00:52:21] верх
[00:52:24] согрей
[00:52:27] то выглядеть нас есть pons.eu видя а и б
[00:52:30] у нас есть функции группой и мы считаем
[00:52:34] сумму по а то что нужно было сделать нет
[00:52:38] но новых у тебя выход выход выход должен
[00:52:42] быть в виде без грубой грубой и написать
[00:52:47] группа и сам добиться без поноса без
[00:52:50] группа я только у тебя выход должен быть
[00:52:53] в виде диктор у тебя а 15 b18 c20 вот
[00:52:58] такой выход из твои функции должен быть
[00:53:01] смотрели ты должен понимать группами она
[00:53:03] каким-то образом работа я хочу
[00:53:06] понял как работает грубой функция самом
[00:53:09] деле то что я тебе говорю что это dict
[00:53:11] это огромная подсказка вообще это прям
[00:53:14] огромное подскажет что тебе денег нужно
[00:53:16] кучу создаем словах об отце разделили
[00:53:21] нужно тебе не нужно вначале создавать
[00:53:24] словарь is a b c честно тебе
[00:53:26] нужно идти чтобы и создавать этот
[00:53:30] словарь если у тебя depth будет видеть c
[00:53:34] и b ничего страшного в этом нет ни об
[00:53:37] отце ну вообще ничего страшнее я понимаю
[00:53:41] типа
[00:53:44] значение присвоить как сумма туда
[00:53:48] затолкать хорошо давай напишем цикл
[00:53:51] начнем с того что мы будем идти по
[00:53:54] мы конечно уходим вообще в другую
[00:53:56] сторону мне лень и куда-то пошёл да вот
[00:53:59] здесь давай напишем
[00:54:02] давай б
[00:54:04] не незачем прям сразу и большое от
[00:54:10] выдачи и нам что нужно сделать давай я
[00:54:13] сверху перед циклом for
[00:54:16] создадим они кредит давай назовем его dt
[00:54:20] вот супер как пустой дик супер и теперь
[00:54:25] в dts делаем вообще что и dt от и
[00:54:29] квадратные скобки
[00:54:32] равно
[00:54:34] 2 и равно нулю просто-напросто
[00:54:38] все равно нулю и давай вернем в этот
[00:54:42] бета-ритм после цикла for
[00:54:46] вот запустить
[00:54:49] запустить запустить
[00:54:52] и группой и
[00:54:55] теперь давай напишем что
[00:54:58] следующей ячейке уже новую ячейку станем
[00:55:01] вот слева сверху написано + код
[00:55:05] вот и вот здесь вот напишем
[00:55:10] print
[00:55:14] грубой
[00:55:16] сам
[00:55:22] он так тот или туда а и b переданы
[00:55:30] все запускаем
[00:55:34] супер у нас получилось
[00:55:37] c00 b0 вроде бы понятно то есть мы
[00:55:41] прошлись по б мы создали вот эти вот
[00:55:44] вещь теперь смотри нам нужно
[00:55:48] одновременно и тигипко b и по а давай
[00:55:52] сделаем следующий цикл for одинакого
[00:55:55] размера да мы считаем что они одинаково
[00:55:57] размеры да они одинаково размеры по
[00:56:00] дефолту они обязательно одинаковый
[00:56:02] размер
[00:56:03] то а давай сделаем вот в нашем цикле
[00:56:08] пройдемся по виду знаешь ли функцию zip
[00:56:13] но я тебя сейчас просто расскажу как
[00:56:15] написать потому что тяжело нашли три их
[00:56:18] функцию 7 не пользовался
[00:56:21] ok но нее не осталось
[00:56:24] окей хорошо а давай напишем просто фон и
[00:56:29] , g вот здесь и
[00:56:35] мы zip а.б.
[00:56:40] [музыка]
[00:56:45] да теперь смотреть нам нужно dt сделать
[00:56:50] g
[00:56:50] потому что у нас уникальные ключи будут
[00:56:54] в.б. и
[00:56:57] вот
[00:56:58] здесь нам нужно что то придумать мне
[00:57:02] просится а
[00:57:03] неправильное
[00:57:05] нет конечно вот смотри и и это будут
[00:57:09] значение провести а
[00:57:13] вот соответственно нужно что то
[00:57:15] придумать ты знаешь что что есть и есть
[00:57:18] g вы проходите вместе по obd вот вы
[00:57:22] такой пары ведете
[00:57:25] окей окей окей окей знаешь я зря на тебя
[00:57:29] до blue давай сделаем следующим образом
[00:57:32] следующим образом вот у нас были нули да
[00:57:35] вот мы видим в 14 и строчки нулей были
[00:57:38] давай мы если напишем здесь dt от g до
[00:57:44] только не равно а + равно напишем плюс
[00:57:47] равно и
[00:57:49] единичку поставить не плюс равно 1
[00:57:54] вот и запустим и
[00:57:59] запустим теперь при
[00:58:02] так он говорит нам
[00:58:05] error ниже опусти пожалуйста давай
[00:58:09] посмотрим на error
[00:58:13] керрор цен
[00:58:21] слушай когда резик
[00:58:23] gresit а вот этот
[00:58:29] убери и вообще
[00:58:31] а как таковое вот все чтобы его
[00:58:34] да вот здесь вот вот это убери ее здесь
[00:58:39] оставим только for g вот и
[00:58:43] вот запустить и
[00:58:48] запустим а
[00:58:50] он говорит о том что ниже опусти он
[00:58:54] говорит о том что
[00:58:55] ррц потому что плюс равно единице ok
[00:59:00] плюс равно нельзя описать или на нам
[00:59:02] потому что нужно будет сделать то есть
[00:59:05] нам по сути своей нужно создать будет
[00:59:07] этот dict так не хотел делать тогда
[00:59:13] давай плюс равно берем вообще сделаем
[00:59:16] следующую схему давали контр за
[00:59:19] отрабатывает от каких назад
[00:59:24] черта не линии и вот здесь вот как ты
[00:59:30] мне тебя так натолкнуть чтоб ты понимал
[00:59:32] что я хочу но я знаю как написать
[00:59:36] [музыка]
[00:59:39] рассказ оцениваешь блин ну просто нужно
[00:59:44] знаешь как нужно чтоб ты понимал как
[00:59:46] работает грубой но я не знаю вот ты
[00:59:49] понимаешь что происходит когда у нас
[00:59:51] была c0 b0 она не только вот что
[00:59:54] произошло мы присвоили всем вот этим а
[00:59:57] по центру ли вот в этой строке а это и
[01:00:00] что нам мешает присвоить ну потому что
[01:00:02] это это это вот в данном случае это это
[01:00:06] значение это не указатель это не яндекс
[01:00:09] и в данном случае это значение это не не
[01:00:13] индекс плюс равно вамбери пожалуйста
[01:00:16] потому что мы здесь неправильно написали
[01:00:20] давай напиши равно равно и
[01:00:26] вот так
[01:00:30] запускаем
[01:00:32] не запускать здесь
[01:00:35] что как думаешь что он тебе сейчас как
[01:00:39] вы так циклов for отработал zip это
[01:00:42] объединение двух вот этих
[01:00:44] да просто простой объединение
[01:00:47] объединение
[01:00:49] вот смотри а барды да ну вот смотри вот
[01:00:53] а и b это два листа до 2 листа он взял
[01:00:58] их объединим два листа блин я знаю как
[01:01:01] тебе написать добавили напишем перед dt
[01:01:05] g&g равно и вот здесь вот обе enter
[01:01:09] снимки print и и
[01:01:15] запусти вот я уверен ты теперь поймешь
[01:01:19] как работает
[01:01:22] вот смотри чем делает 1-цы
[01:01:26] 23 п то есть он идет по вот этим списком
[01:01:31] теперь в самом конце самом конце он тебя
[01:01:35] оставил c9 а 829 это самое последнее
[01:01:39] значение которые принимали эти ключи
[01:01:41] остается написать сумму то есть мы вовсе
[01:01:44] не вложением идем я понимаю что ты все
[01:01:46] мне рассказал
[01:01:47] но я даже я видишь как я тебе даже на
[01:01:51] самом деле сказал про плюс равно потому
[01:01:53] что плюс равно хоть и не работает и не
[01:01:56] работает понятно почему на самом деле
[01:01:58] потому что нету включается а вон она его
[01:02:02] ссылается когда мы делаем плюс равно
[01:02:04] соответственно здесь нужно что то
[01:02:07] придумать
[01:02:16] созданную у тебя во первых д нет такого
[01:02:20] по определению и
[01:02:24] вот теперь ты кстати можешь посмотреть и
[01:02:27] понять в чем здесь ошибка да включая и
[01:02:32] включая и здесь
[01:02:36] терон ровно тот же что и у нас была он
[01:02:40] говорит о том что он не знает что такое
[01:02:42] и птицы и типа
[01:02:45] он вот второе значение dt а джинн он его
[01:02:50] ты его еще не создал ты его только
[01:02:53] создаешь но тут же на него ссылаешься
[01:02:55] соответственно нужно на самом деле здесь
[01:02:58] написать такую функцию get то есть д .
[01:03:02] get а вот ддт g равно
[01:03:07] dt вот здесь да да да
[01:03:10] два раза направо
[01:03:15] пиши . get
[01:03:20] круглые скобки
[01:03:22] здесь нужно написать и g ну вот и
[01:03:27] квадратную стоком скобка удалить
[01:03:29] написать , 0 круглую скобку закрыть
[01:03:34] elixir флюс и
[01:03:36] да и теперь давай попробуем запустить и
[01:03:42] как у нас получится
[01:03:45] делает get
[01:03:47] функция get она возвращает тебе
[01:03:51] значения в и льюс в ключе
[01:03:54] но если она этого ключа не найдет она
[01:03:58] вернет тебе нам мы этот man заменили на
[01:04:01] ноль по дефолту то есть вот это вот там
[01:04:04] функция get
[01:04:05] значение ключа , но это возврат значение
[01:04:10] party фото то есть если бы было ключ он
[01:04:13] бы его вернул значение если его нету он
[01:04:17] по дефолту возвращать 0 вот как работает
[01:04:20] группа issue честно говоря это чуть-чуть
[01:04:22] на питон чуть-чуть на знание того как
[01:04:24] вообще агрегационную функции работают ты
[01:04:27] должен понимать что здесь вот мы
[01:04:29] реализовали очень простую функцию
[01:04:31] суммирования до агрегация full на одну
[01:04:33] бросаю корреляционная функция в виде
[01:04:35] суммирования но на самом деле ничего
[01:04:37] тебе не решает сделать например
[01:04:39] умножение каждого ну так что
[01:04:41] кумулятивные умножение друг друга да ты
[01:04:43] можешь просто убрать плюсик поставить
[01:04:47] звездочку и ты будешь умножать каждом
[01:04:49] значении докажи это прикольно прикольно
[01:04:51] потому что типа она немного другая здесь
[01:04:55] по сути своей на самом деле по сути
[01:04:58] своей мы написали не просто грубой sum
[01:05:00] sum на кумулятивные суммы если еще
[01:05:03] упороться можем задать каким окно мы
[01:05:06] будем суммировать но это такой знаешь
[01:05:08] это хорошая практика на то чтобы
[01:05:12] понимать как работает оконные функции
[01:05:14] хорошо понимается как работает в еще
[01:05:16] питон как мы делаем в этот проход
[01:05:19] написать все это и и это честно говоря
[01:05:22] дает очень хороший куст в понимании того
[01:05:25] как мы работаем с данными как мы
[01:05:27] понимаем что лучше работает что хуже но
[01:05:30] есть нюанс нюансы всегда есть нюансы
[01:05:34] заключается в том что проход tiguan по
[01:05:36] всем значениям нашего значит который мы
[01:05:40] это такое себе условии если у нас очень
[01:05:43] длинные-длинные вот эти колонки есть
[01:05:45] понятие векторных сложений векторных
[01:05:47] предложений и всякие работы с векторами
[01:05:50] это существенно ускоряет работу
[01:05:55] и например ну работа лампой и рей и
[01:05:59] суммы мамой рейв она как раз на
[01:06:02] вектор на сложение как вот так далее то
[01:06:05] есть там есть тоже свои нюансы того как
[01:06:07] это работает в цену в целом вопрос
[01:06:10] связаны по работе с данными они
[01:06:12] закончились давай перейдем к тому что ты
[01:06:15] так откладывал кабелем можем прекратить
[01:06:19] шарик дальше идут чисто теоретические
[01:06:22] вопросы
[01:06:23] так как мы не рядом с друг с другом то я
[01:06:26] тебе просто позовем задали несколько
[01:06:28] вопросиков самых простых самых вот
[01:06:31] базовых по email посмотрим как ты на них
[01:06:34] будешь отвечать есть стандартная так вот
[01:06:37] алгоритма эмали отрезанную две задачи
[01:06:41] задачи классификации задач и тыкать где
[01:06:44] мне нужно
[01:06:47] есть задач классификации задач или песен
[01:06:50] давай поговорим про задачу регрессе но
[01:06:53] поговорим по суле есть такие вот модели
[01:06:58] линейной регрессии а нож какой-нибудь
[01:07:00] вспомнить простая линейная rising когда
[01:07:03] на вход подаем какие-то резисторы на
[01:07:06] выходе получаем числовое значение
[01:07:08] непрерывная
[01:07:10] хорошо давай вспомним просто там формулу
[01:07:15] линии или модели дамы какой-то простой
[01:07:17] крем из математики y равно 0 плюс bx
[01:07:20] супер а 0 плюс bx какие коэффициенты с
[01:07:26] помощью нашего на обучении мы подбираем
[01:07:29] просто вопрос
[01:07:33] их подбираем соответственно блоков
[01:07:36] центре коэффициент привет при каждом
[01:07:38] резисторе но принцу в данном случае реке
[01:07:40] x 2 типа она либо
[01:07:44] вопрос крупных . а мы придумываем себе
[01:07:47] функцию ошибки мы говорим про конкретно
[01:07:49] про это вот про машины обучения или про
[01:07:52] про линиями модель давай вот машин
[01:07:55] обучение линейная модель функций ошибки
[01:07:57] супер уже супер расскажи поподробней
[01:08:00] функция ошибки есть среди квадратичное
[01:08:04] есть есть у нас есть мои
[01:08:06] мысли это разница
[01:08:09] мы представляем что у нас есть какие-то
[01:08:12] истинных значений то что наша модель как
[01:08:14] сказала мы находим разницу между тем что
[01:08:17] на самом деле и тем что модель
[01:08:19] предсказала и это будет наша ошибка эта
[01:08:21] ошибка может в двух видах как сумма
[01:08:24] сумма квадратов разниц и сумма
[01:08:27] модулей разниц сумма модулей разниц
[01:08:31] самом себе показательно но с ней тяжелее
[01:08:34] работать с квадратами проще работать
[01:08:37] проще искать проще искать минимум а
[01:08:40] почему мы считаем что квадрат дает нам
[01:08:44] параболу из параболы можно работать она
[01:08:46] непрерывный они и но в каком-то общем
[01:08:48] простом случае мы считаем что нее есть
[01:08:50] один минимум так мы можем подобрать
[01:08:52] параметры таким образом чтобы наша
[01:08:54] ошибка оказалось тупо внизу парабола
[01:08:57] есть вот с математической точки зрения с
[01:09:00] квадратом работать много проще потому
[01:09:02] что как мы ищем
[01:09:05] да потому что может найти попроще
[01:09:08] дифференцировать type 1 двоечку в snes и
[01:09:11] погнал
[01:09:12] так супер супер а
[01:09:15] что он происходит в мае придеться вот
[01:09:19] когда мы берем у нас константа остается
[01:09:21] мыслить и сделать не сможем
[01:09:23] типа она в нули это
[01:09:26] плохо не дифференцирует ну типо вот
[01:09:30] когда вы теперь она даже
[01:09:32] supersu так есть от всяких аки про то
[01:09:37] как обходит вот это вот как там своем
[01:09:39] работают всякие слаженные мои как они
[01:09:42] суть мы сейчас не думает говорить или
[01:09:46] вот смотри я слышу но мне кто-то говорил
[01:09:49] про то что есть такая вещь как
[01:09:51] градиентный спуск и что она мне как-то
[01:09:55] позволяет сделать подборка в цель а вот
[01:09:59] что это за фигня такая границ курск что
[01:10:01] такое градиент что такое предельный
[01:10:03] спуск как она работает это сложная фигня
[01:10:07] градиент это производная
[01:10:10] виктор градиента показывает нам мини
[01:10:13] изменения функции и
[01:10:15] прежде не спеши
[01:10:17] upgrading to что это производные или
[01:10:21] вектор честный производство так и если
[01:10:23] подумаем я конечно до капли масла прости
[01:10:27] пожалуйста
[01:10:31] это гектор частных
[01:10:34] частные производные
[01:10:36] часть ответа вектор это часть их в целом
[01:10:40] эта вещь перчатках прыжок куда указывает
[01:10:43] людей направлении возрастания функции
[01:10:45] супер соответственно для того чтобы
[01:10:48] найти минимум надо взять
[01:10:51] integrity супер супер но все равно не
[01:10:55] поля как же я с помощью градиента в этот
[01:10:58] брезент спуска ищу коэффициенты а 0 и b
[01:11:02] вас уйти своими вопрос как идиот
[01:11:05] обучение у
[01:11:08] нас есть какая-то модель мы получили по
[01:11:11] ней ошибки мы взяли нашу amos е1 у нас
[01:11:17] какая-то функция мы в какой-то точке
[01:11:20] считаем квадратная функция
[01:11:22] соответственно в какой-то точке мы
[01:11:23] находим вектор градиента и мы стремимся
[01:11:27] его свести к нулю грузит вам дает
[01:11:31] вектор клиенты пытаются 70 камеру как то
[01:11:35] нет тогда наверное мне тогда и то есть
[01:11:39] он просто он не структурирована голове у
[01:11:42] тебя учителя есть она тебя есть сто
[01:11:45] процентов просто последовательно нужна
[01:11:48] последовательность вот что что
[01:11:52] 124 имея какое-то
[01:11:55] если рисовать параболу то мы стремимся
[01:11:58] по ней спуститься вниз эту точку .
[01:12:00] градиента спустить вниз таким образом на
[01:12:03] те минимум ошибки вот
[01:12:07] смотри типа на у
[01:12:10] тебя есть что у тебя есть предсказание
[01:12:13] модели и реально предсказать правильно у
[01:12:17] тебя есть ошибка у тебя есть сумма
[01:12:21] квадратов ошибок мы хотим сумму
[01:12:24] квадратов ошибок свести к нулю не к нулю
[01:12:27] как минимум прально говорит мне
[01:12:28] соответственно мы это можем сделать с
[01:12:30] помощью как раз среде в роспуск где там
[01:12:33] подвох подвох заключается в том что нам
[01:12:35] просто нужно грамотно расписать что на
[01:12:38] самом деле там наше предсказание от x
[01:12:43] она выглядит как некоторые там значения
[01:12:46] коэффициента а 0 песни которые значение
[01:12:49] коэффициента b ну давай мы возьмем там
[01:12:52] какой-то президентом б а 0 плюс b 0 плюс
[01:12:57] b 1 то допустим
[01:12:59] и у нас будет y равно как а 0 плюс b 0 и
[01:13:04] x плюс b 1 x квадратура
[01:13:10] теперь вот это предсказание нашего
[01:13:14] алгоритма есть какие-то значения а песок
[01:13:17] и теперь можешь посчитать разницу можешь
[01:13:21] посчитать
[01:13:23] значение м с и пытаться его
[01:13:25] минимизировать за счет глядим спуск но в
[01:13:28] целом в целом ну типа это так я понимаю
[01:13:31] вот и последует последовательность она
[01:13:34] такая что сделал предсказание на
[01:13:36] каких-то
[01:13:37] ну на каких-то писать код у нас есть
[01:13:39] какие-то веса до сделал предсказание
[01:13:42] посчитал ошибки посчитал
[01:13:44] сумму квадратов ошибок читал градиент
[01:13:48] обновил леса и заново по циклу так вот
[01:13:51] идём идём идём идём идём пока в какой-то
[01:13:54] момент у нас ошибка она не лениться и
[01:13:56] типа вот у нас ошибка не меняется значит
[01:13:58] мы достигли вот это вот выходе из-за
[01:14:02] цикла все все в принципе в принципе
[01:14:04] ничего больше не знать именно но есть
[01:14:08] такая хрень
[01:14:09] грей называется переобучение и
[01:14:13] есть варианты работать переобучения
[01:14:16] опять таки я слышу я вообще в этом не
[01:14:18] разбираюсь но я слышу что есть понятие
[01:14:22] переобучения модели что это такое и как
[01:14:25] бороться с переобучить переобучение
[01:14:27] история когда у нас модель на на
[01:14:30] трендовых данных показывать какие то
[01:14:32] есть хорошие результаты тестовых данных
[01:14:34] она может она показывает недостаточно
[01:14:37] хороший это история когда модель
[01:14:39] подстраивается под под под нашу
[01:14:42] обучающую выборку она прекрасно
[01:14:44] отрабатывает и и она повторяет может
[01:14:46] быть в каждую точку но это не имеет
[01:14:49] отношение к жизни и на тестовых данных
[01:14:51] она покажет себя гораздо хуже хорошо
[01:14:54] назови мне как минимум три banyan борьбы
[01:14:57] с переобучение применительно к линейной
[01:15:01] регрессии регуляризации мы применяем а
[01:15:03] почему то линейной регрессии
[01:15:06] просто взял оскорбил много других
[01:15:10] алгоритмов
[01:15:11] regular за
[01:15:13] у у разных алгоритмов она разная не то
[01:15:17] чтобы у разных но в том числе если не на
[01:15:18] регрессе
[01:15:20] регуляризация как действует
[01:15:21] регуляризации мы добавляем по ошибке
[01:15:24] страхующий и член который тоже бывает
[01:15:26] разный функционал ошибки и он
[01:15:29] соответственно если говорить о линейной
[01:15:31] регрессии то он он будет штрафовать
[01:15:35] случае разные регуляризации он может
[01:15:37] либо обнулить там какие то какие то
[01:15:40] предикторы либо сделать их близкими к
[01:15:42] нулю но в целом он приводит тому что он
[01:15:44] избавляет от больших весов предиктор
[01:15:48] там хорошо простите сказал занулить либо
[01:15:52] при визите к нулю это сделать очень мало
[01:15:55] очень мало ли
[01:15:57] там либо занулить либо сделать очень
[01:16:00] мало
[01:16:01] думаешь так мы говорим про веса при
[01:16:04] иксах да если мы добавляем регуляризации
[01:16:07] у линейную регрессию то
[01:16:12] просто в этот момент очень мало ни много
[01:16:15] ни математически звучать дальше и суть
[01:16:18] не суть так хорошо прилягу реализацию ты
[01:16:21] сказал еще два варианта как можно
[01:16:23] бороться с нашим переобучить тут буду
[01:16:26] импровизировать наверное но линейной
[01:16:29] регрессии в частности чувствительна к
[01:16:31] multiply near настей можно до того как
[01:16:33] мы пустим признаки в регрессию можно
[01:16:36] посмотреть оценить их насколько они
[01:16:38] коррелируют между собой если есть те
[01:16:40] которые коррелируют а от них можно но
[01:16:43] если это если это возможно будет от них
[01:16:45] можно избавиться не остановило все
[01:16:48] рассказал про шо слышал ли ты
[01:16:51] когда-нибудь про всякие в лиге ционные
[01:16:54] техники когда мы делаем отдельно с и
[01:16:59] вызывая на тестовые трейдеры набора не
[01:17:02] менее когда у нас есть тестовый набор
[01:17:05] который мы не больше никогда не ти есть
[01:17:07] странный набор а есть еще в
[01:17:09] иммиграционный datasette как часть
[01:17:11] рейном умного и там через понятие
[01:17:14] консолидации но я об этом не знаю но
[01:17:16] слышал про к соблюдаются страте five
[01:17:20] card type сирия скро сваливается цель
[01:17:24] таком слышу кросс выдался да когда мы у
[01:17:28] нас есть
[01:17:30] datasette на которую мы учимся и и
[01:17:33] тестируемся и мы берем
[01:17:38] не просто часть вот говорим что вот это
[01:17:41] у нас будет train а этот тест мы меняем
[01:17:46] их берем разные наборы на разных наборов
[01:17:48] учимся на разных наборах тестируемся но
[01:17:50] все в рамках
[01:17:52] рамках 1 1 2 это хорошо но и то есть
[01:17:56] способ борьбы с переобучение что мы
[01:17:59] начинаем проверять просто вот шафрин
[01:18:01] каким-то образом смотрим а вот такой это
[01:18:05] вариант ой очень плохой очень плохое
[01:18:10] предсказание потом опять же очень плохой
[01:18:12] предсказать ну кажется что мы период
[01:18:13] учились когда вот давай сейчас стали что
[01:18:16] зажав ли каким-то образом посмотрим на
[01:18:19] на кросс валидации назначения наши
[01:18:22] венеции бой-то
[01:18:24] метрики на которую мы будем смотреть и
[01:18:27] понимать у нас обучилась моделью меня
[01:18:29] получится хорошо на какой-то показатель
[01:18:32] качества шел есть различные способы
[01:18:35] валидации вот кросс валидации про строки
[01:18:37] fight к фолд слышал
[01:18:39] стратификация модификация стран тогда
[01:18:42] слышал ничего не скажу мне почему то
[01:18:45] кажется что мы хотим сделать так чтобы
[01:18:47] она встроена в этом наборе были
[01:18:49] одинаково присутствовали какие-то
[01:18:52] подгруппы у нас года да и то есть это
[01:18:56] есть супер то есть в каждой были
[01:18:58] рационом сети нас должно быть
[01:19:01] определенный набор групп и нута на
[01:19:04] основе каких-то вот стран это может быть
[01:19:07] значение как кода ну это особенно
[01:19:10] актуально для мытья класс классификации
[01:19:13] чтобы нас в каждом анимационном сети
[01:19:15] было определенное количество
[01:19:18] вот этих классов которые нас должны быть
[01:19:21] задача как задачах репрессии мы можем
[01:19:25] взять какую-то категорию переменную и
[01:19:27] просить чтобы в каждом выдвигаться на
[01:19:30] сайте было определенное количество вот
[01:19:32] этих вот
[01:19:33] категориальных речей
[01:19:35] от очень представители вот
[01:19:38] принадлежащих определенных категорий то
[01:19:41] есть объекта мне кажется внешне по
[01:19:43] умолчанию такие вещи которые вот без
[01:19:46] да но эта строчка вот так хорошо а про
[01:19:53] основного времени могу говорить про
[01:19:56] временные ряды до временные ряды и про
[01:20:00] кросс валидации временных рядах но это
[01:20:03] на самом деле используется не только в
[01:20:05] так называемых конкретных временных
[01:20:08] рядах и людей всегда он изменяется в
[01:20:11] течение времени так далее это просто вот
[01:20:12] у нас есть какая-то зависимость от
[01:20:16] времени и мы хотим это запчасти от
[01:20:17] времени тоже учит что ты даже
[01:20:19] представишься не могу мы уже считаем что
[01:20:21] у
[01:20:22] нас текущее значение
[01:20:24] какой-то переменной предсказывается по
[01:20:26] неким ближайшем условно ближайшем или по
[01:20:31] оси зоны был цикличным каким-то назад
[01:20:34] как здесь можно от вы лидера ваться нет
[01:20:37] не слышал оно стало любопытно опять-таки
[01:20:40] войска ерни можно посмотреть в общем
[01:20:43] видит выделить следующим образом у нас
[01:20:44] есть вот период времени на году вот есть
[01:20:47] полный период вот есть период временно
[01:20:50] которым мы обучаемся вот здесь мы
[01:20:52] лидируем ну вот да предсказанным смотрим
[01:20:54] на ошибку затем этот период берем
[01:20:58] здесь обучаемся на следующий предсказан
[01:21:01] и так далее кумулятивно типа увеличиваем
[01:21:04] увеличен смотрим на результат самый при
[01:21:07] помощи то есть вот вариант когда мы коли
[01:21:10] по кумулятивным увеличивались вариант
[01:21:12] когда у нас вот это вот окно а нам
[01:21:14] просто переползает дальше и типа ты
[01:21:17] переползаешь делаешь прогноз
[01:21:19] переползаешь делаешь прогноз приглашаешь
[01:21:21] делаешь просто есть какое-то хорошо
[01:21:25] про кроссовере доця подарили еще один
[01:21:28] способ борьбы с требующий о нем всегда
[01:21:30] забываю вот я могу сказать всегда
[01:21:33] забывают про вот этот способ борьбы с
[01:21:35] передачей но этот самый
[01:21:39] параметров моделью
[01:21:42] добавить данным а где же увеличить
[01:21:45] увеличить количество данных но как как
[01:21:49] тебе сказать мы же говорим про способы
[01:21:51] борьбы с приобретением правильный ответ
[01:21:53] ну так давайте ограничивать исайя
[01:21:55] допустим или использовать регуляризации
[01:21:58] хорошо давайте использовать другие
[01:22:00] варианты играли до суда супер но самое
[01:22:04] лучшее брендовое тебя новые данные типа
[01:22:08] просто новые данные добычи или
[01:22:11] посмотрели дальше по схеме типа это
[01:22:13] самый простой и самый течение не самый
[01:22:16] простой зачисляется на просто но самый
[01:22:18] эффективный способ борьбы с передачи
[01:22:19] прошел давай поговорим про деревья как
[01:22:24] строится дерево 1 делим задачку в
[01:22:27] деревьях есть узлы предикаты в которых
[01:22:30] выставляются какие-то условия по этому
[01:22:33] условию
[01:22:34] набор данных разбивается как правило на
[01:22:37] на 2 и дальше опять предикаты условиях и
[01:22:41] так дальше и так дальше заканчивается
[01:22:42] все листиками у ритика как будто бы есть
[01:22:45] ответы вот из того что могу рассказать
[01:22:49] главный вопрос
[01:22:51] для
[01:22:53] как разбивать данные у нас есть набор
[01:22:57] признаков мы берем тот признак который
[01:23:02] максимальная информативен короче
[01:23:04] дисперсия мир неопределённости данных
[01:23:08] когда все это повторяешь это мгла из и
[01:23:11] по данным по конкретному признаку мы
[01:23:14] находим меру неопределенности и выбираем
[01:23:17] тот признак по которому у нас самой
[01:23:21] маленькой неопределенность это признак
[01:23:22] мы будем считать самым интересным по
[01:23:26] этому признаку в это признаки у нас есть
[01:23:28] набор нам нужно определить в какую
[01:23:31] сторону упадем в какой момент мы пойдем
[01:23:33] направо пойдем налево при каком значении
[01:23:35] признака соответственно мы
[01:23:38] последовательно идем по каждому значению
[01:23:40] этого признака
[01:23:42] определяем а я что сказал тропе и должно
[01:23:45] быть но ты на и сторона это фильтр
[01:23:50] опечатку лишь ты почему-то дисперсии
[01:23:52] сказал дисперсии трапе и конечно
[01:23:54] энтропии энтропия но я далеко
[01:23:57] мы определяем энтропию разбиение таким
[01:24:02] образом чтобы и терапия в этих разбитых
[01:24:04] группах было мера неопределенностью этой
[01:24:07] тропе и было меньше чем чем вот в
[01:24:10] исходной группе и соответственно вот эта
[01:24:12] точка будет я понятно говорю я тебя
[01:24:15] попрошу давайте точка будет точкой
[01:24:18] разбиение мы говорим что вот мы
[01:24:20] допустить ее нашли вот в этом значении у
[01:24:22] нас энтропия развивается так что сумму
[01:24:25] вот этих энтропий меньше чем сумма общей
[01:24:29] терапии в этой точке мы разбиваемся
[01:24:31] говорим что если у нас
[01:24:32] значение этого признака там меньше
[01:24:35] меньше пяти то мы уходим в эту ветку
[01:24:38] если больше 5 уходим в эту ветку и в
[01:24:42] последующих ветках происходит тоже самое
[01:24:43] мы разбиваемся так до тех пор пока не
[01:24:47] доходит до критерий останова
[01:24:50] останавливаемся и в листиках у нас
[01:24:52] остается если мы говорим про про
[01:24:54] классификацию в листиках у нас остается
[01:24:57] набор каких-то объект набор объектов да
[01:25:01] и
[01:25:03] соответственно листик принимает решение
[01:25:05] листик объявляет такое движение дерево
[01:25:08] по принципу каких объектов больше
[01:25:11] какой будет
[01:25:16] сейчас небольшую пометку
[01:25:19] будущем людям которые будут смотреть
[01:25:22] возможно разбора я не знаю че с мировые
[01:25:24] детали нет давай надеюсь скажем что что
[01:25:28] сейчас сейчас на самом деле по 10
[01:25:33] долл гости
[01:25:35] естественно , физики значит оба по сути
[01:25:39] словей
[01:25:40] есть вот такая критерием пропилена он
[01:25:44] используется для того чтобы определить
[01:25:45] не только признак по которому будем
[01:25:47] делить но и точку разбиения ты все
[01:25:49] правильно вы лишь то что там суммы
[01:25:51] энтропии должна быть это все правильно
[01:25:54] единственное что но наверное так
[01:25:57] скомкано было но я могу судить что это
[01:26:01] хорошо одно дерево поняли почему
[01:26:05] работает случайный лес объяснение почему
[01:26:08] случайно не сработает хорошо здесь ответ
[01:26:11] на это вопрос да и самая важная почему
[01:26:14] мы случайно вес считается что он не
[01:26:16] перри обучается почему мы идем к
[01:26:17] случайному лесу потому что огромные
[01:26:20] вычисления если вот пока если
[01:26:22] представить что огромное количество
[01:26:23] признаков и объектов то большие
[01:26:25] вычисления мы идем переходим к
[01:26:27] случайному лесу я очень хорошо помню что
[01:26:29] на курсы и сказали так кричали
[01:26:31] пожарского типа парадокс на случайный
[01:26:33] вествуд работы
[01:26:35] удивительно да вот это это неправда
[01:26:38] вообще это неправда потому что городок
[01:26:41] сможет вы слова продукт не говорили ну
[01:26:42] как то так сказали что удивительно вот
[01:26:44] работает нет на самом деле есть жесткая
[01:26:47] давали твоя отвечу на вопросы про
[01:26:50] закончил есть очень важный постулат
[01:26:53] который стоит за случайным лесом почему
[01:26:56] случайно не сработает чего вообще там
[01:27:00] ансамбли из нескольких деревянных
[01:27:02] моделей работал потому что у нас но
[01:27:05] точнее он работает тогда когда нас
[01:27:08] вероятность предсказанием раненого
[01:27:10] класса на больше 0 5 больше случайность
[01:27:12] вот он работает случайно лишь тогда
[01:27:15] когда каждый классификатор каждая модель
[01:27:18] каждое дерево который будет построена
[01:27:21] она будет работать выше чем случайно
[01:27:24] вот в данном случае там есть математика
[01:27:27] за эти который доказывает что типа если
[01:27:30] мы лучше случайного там и в среднем
[01:27:32] будем всегда лучше случайно
[01:27:34] соответственны лучше чем просто один
[01:27:38] одесситки помимо этого есть еще подход
[01:27:42] что мы используем там беден а это значит
[01:27:45] то что наберем случайно подмножество
[01:27:48] фичей то есть наших вот регрессор
[01:27:52] декоров и случайное количество объектов
[01:27:54] и сам интересное что у нас еще может
[01:27:59] быть такое что вот в вот в этот набор
[01:28:01] свечей и объектах может попадать один и
[01:28:03] тот же объект несколько раз чисто
[01:28:05] теоретически только возможно супер то
[01:28:08] есть там нас
[01:28:09] забор с возвращения это работает хорошо
[01:28:12] работает отлично но есть следующий
[01:28:16] вопрос со звездочкой и на этом мы
[01:28:18] заканчиваем
[01:28:19] вопроса звездочка в каких случаях
[01:28:23] логистическая регрессия на задачи
[01:28:26] классификации
[01:28:27] будет работать лучше
[01:28:29] чем случайные вес даже немного вводных у
[01:28:34] нас сто пятьсот параметр и несколько
[01:28:37] миллионов
[01:28:38] объект то есть данная дофига при этом
[01:28:42] логистическая регрессия работает в разы
[01:28:44] лучше чем случайно ли мы почему про
[01:28:48] качеству говорю да про качество с точки
[01:28:51] зрения точности полноты их меры рока у к
[01:28:55] и так далее вот прям существенно лучше
[01:28:57] работать почему такое может быть я могу
[01:29:01] только рассуждать или регрессии остается
[01:29:03] регрессией а при огромном количестве ну
[01:29:06] производства и мощность нужна какая-то
[01:29:08] безумная если мы говорим про но если мы
[01:29:10] считаем что у нас предложено мощность
[01:29:12] есть как бы это не не аргумент нет
[01:29:14] недостатков деревьев только сложность
[01:29:16] озвучивается митяй смотри
[01:29:19] я только что рассказывал про важным
[01:29:22] условием почему скучали без работы
[01:29:24] поверхность должна быть больше на 5 и на
[01:29:27] бошке чайного да а
[01:29:30] если случайно мест не работает значит
[01:29:33] что естественно каждый предиктор уже
[01:29:36] случайно или или на уровне случайно
[01:29:39] edition да ну а как такое может быть вот
[01:29:43] когда такое может быть но когда вся и
[01:29:45] терапия примерно одинаково да ну то есть
[01:29:48] шум ты просто работать шумом
[01:29:52] но но как будто были грехи и правится
[01:29:54] при этом регрессе как-то справляется
[01:29:57] почему это очень хороший вопрос на
[01:30:00] подумать вот просто вот прям цепочка
[01:30:02] цепочка с пол-очка цепочка и дальше вот
[01:30:04] она привлечься не привязывается к 0 5
[01:30:07] потом пойдем от деревьев вот смотри
[01:30:09] задач дано
[01:30:13] чайный лес работает плохо есть
[01:30:15] логистической регрессии линейная ноготь
[01:30:17] который работает хорошо все это дону
[01:30:20] знаем каждое дерево случайного леса
[01:30:22] должно работать лучше чем 05 этого не
[01:30:26] происходит значит что то не то что то не
[01:30:30] так из-за того что есть шум в данных но
[01:30:33] мы знаем что случайный лес работать на
[01:30:35] подмножества данных и под множестве
[01:30:38] объект
[01:30:40] все значит следующий шаг какой не просто
[01:30:44] шум в данных но для него они все
[01:30:46] одинаковые не так ну типо вот смотри она
[01:30:49] же много деревьев соответственно много
[01:30:52] шумов дан очень много шумов данных при
[01:30:56] этом знаем что линейная модель каким-то
[01:30:59] образом среди всех данных что-то нашла
[01:31:02] что позволяет ей решить задачку весь в
[01:31:05] косы хорошо а случайный весь не может
[01:31:07] потому что он берет подмножество там шум
[01:31:10] не получилось берет подмножество тут шум
[01:31:14] не получилось берет опять по наш шум 05
[01:31:17] не получилось потом берет о что-то
[01:31:20] нащупал больше чем 5 но этих деревьев
[01:31:22] мало таких хороших деревьев мало
[01:31:25] относительно общего количества потому
[01:31:27] что там много шума
[01:31:29] соответственно соответственно таком
[01:31:31] случае я специально бурю сто пятьсот
[01:31:34] параметров миллионы
[01:31:36] объектов очень много данных случайно
[01:31:40] леса шум шух шух шух шух шух шух шух шух
[01:31:44] политической регрессе вот этот весь шум
[01:31:46] отодвинула а вот на один или там два
[01:31:49] признака ориентируется который мне
[01:31:51] зашумленным и таким образом может
[01:31:54] поделить группу на 2 это специально
[01:31:58] вопроса звездочки но это очень частый
[01:32:02] вопрос очень часто задаются джоном чтобы
[01:32:05] понять как человек думает знает ли он на
[01:32:07] тематику принимает лимонный каком бы но
[01:32:11] всегда есть красивые задач и она вот
[01:32:15] идет вот прям есть ответ слушай дмитрий
[01:32:18] на этом все давай я тебе расскажу ей дам
[01:32:21] немножко обратная связь покойного как
[01:32:24] это было значит во первых хочу
[01:32:26] поблагодарить тебя это реально очень
[01:32:29] здорово что ты готов выходить на мог
[01:32:34] интервью ты готов общаться ты готов
[01:32:36] получать какой-то там это очень здорово
[01:32:40] теперь по а секция 1 секция капитона
[01:32:44] честно очень сильно
[01:32:46] не хватает питона соответственно я бы
[01:32:49] наверное в первую очередь упор делал
[01:32:51] именно на питон на то чтобы узнать
[01:32:53] детали чуть побольше
[01:32:55] посмотреть какие-то лекции есть очень
[01:32:58] хорошие открытой лекции хотя папе туману
[01:33:01] но они такие они больше про алгоритмы но
[01:33:05] они очень хорошо дают вот базу а уже
[01:33:07] поверх базы работаем с тем что нам нужно
[01:33:11] в мыле да честно я иногда спрашиваю
[01:33:15] junior of middle of которые говорят что
[01:33:19] они не дури а на самом деле ну там прям
[01:33:22] большие группы в знаниях я иногда даю вы
[01:33:26] знаешь задачу реализуем меня пожалуйста
[01:33:28] градиентный спуск
[01:33:30] в питоне вот прям 75 или пишет возьми
[01:33:33] алгоритм построение дерева сам взять и
[01:33:37] напиши
[01:33:38] возле
[01:33:40] стохастический людей ный спуск сам сядь
[01:33:43] и выпиши напиши будет стробирования
[01:33:46] bootstrap взять напиши ты это все равно
[01:33:50] будешь использовать в аналитике ты все
[01:33:53] равно это будешь использовать в работе
[01:33:55] но тебе нужно да да работе мы не пишем
[01:33:59] кредит газ куска но это очень хорошо
[01:34:03] дает понимание того как нам нужно
[01:34:05] действовать алгоритм как он работает и
[01:34:08] так далее тот же группой sum
[01:34:11] sum sum но типа он же ничего сложного
[01:34:15] нету дам тебе нужно просто пройти по
[01:34:17] листу и
[01:34:20] все а в питонами когда ты знаешь вот
[01:34:25] базу когда ты знаешь как работает
[01:34:27] какие-то конкретные вещи все остальное
[01:34:30] много проще положить незнания пройди
[01:34:33] миллю незнание по работе с данными и
[01:34:37] статистику я б тест то есть но я тебе
[01:34:40] говорю как бывший разработчик то есть я
[01:34:44] как раз от разработчика шоу меня было
[01:34:47] хорошее математическое знаем но
[01:34:48] математическая база физическая база
[01:34:51] хорошая и я еще и программировать у меня
[01:34:53] потрясная вот тихоньку скатывался dvd с
[01:34:57] именно через программированию теперь
[01:35:02] что касается
[01:35:04] оба тестов а пытаясь то были прикольно я
[01:35:07] достаточно развернуто тебе дал про то
[01:35:10] какие еще кейс интервью вот бывают
[01:35:13] побыть с пожалуйста просто снять
[01:35:16] прочитаю несколько статей это
[01:35:18] существенно улучшить ну и нужно набить
[01:35:21] руку нужно набить руку просто взять
[01:35:25] какие-то данные посчитаю статистиками
[01:35:26] посчитай а как статистиков бы цепи
[01:35:28] выглядит почему так и так далее то есть
[01:35:32] просто реализовать посмотреть набить
[01:35:36] руку просто набить руку что касается
[01:35:39] работа с данными очень большой момент и
[01:35:43] вот мне не понравилось что ты не знаешь
[01:35:46] оконной функции хотя на самом деле есть
[01:35:50] множество
[01:35:52] открытых тренажеров который позволяет
[01:35:56] позволяет наработать
[01:35:58] руку со своими запросами в том числе с
[01:36:03] оконными функциям у нас синтаксиса как
[01:36:06] он их функцию он плюс-минус выглядит
[01:36:07] следующим образом есть какая-то
[01:36:09] гравитационная функция допустим сам или
[01:36:12] каунт или еще что-то и дальше идет такое
[01:36:16] о в
[01:36:17] окно в окне партий шамбал ордер по и
[01:36:23] еще иногда там есть такое роуз between и
[01:36:28] вот в роуз between есть еще вот антипов
[01:36:32] between the dates по датам
[01:36:34] то есть все вот эти вот возможные
[01:36:37] агрегации возможно и окна нужно ли
[01:36:41] делать опять таки есть тренажеры можно
[01:36:44] найти есть обман и можно найти есть
[01:36:47] очень хороший инструмент который в
[01:36:51] ближайшем времени тоже выйдет это
[01:36:54] инструмент там тренажер для менеджера
[01:36:57] моего сделать но по сути своей он такое
[01:37:00] он в том числе для новичков там есть и
[01:37:03] базовые знания танкович делай троен и и
[01:37:06] посчитать различные агрегационную
[01:37:08] функции это вот прям очень нужна а затем
[01:37:12] оконные функции посчитать и так далее
[01:37:16] что ты очень часто задача вот например
[01:37:19] там в предсказании спроса
[01:37:22] ценообразование
[01:37:24] реальных задачах очень часто задачи
[01:37:27] звучит следующим образом посчитай сложна
[01:37:29] и средние за какой-то период каким-то
[01:37:31] окном
[01:37:33] и пошел просто
[01:37:38] так теперь что касается в мыле конечно
[01:37:43] нужно устаканить
[01:37:46] какие-то вещи какие вещи еще спрашивают
[01:37:49] очень часто то есть честно кросс в
[01:37:52] редакционной вещи вот это нужно знать
[01:37:55] очень спрашивают про то как мы
[01:37:57] оптимизируем тут и ту или иную модель
[01:38:00] честно одно из самых просто офигенных
[01:38:03] выступлениях по вещам связан с
[01:38:07] деревьями с random forest is глядим
[01:38:11] пустить приз есть выступление игоря
[01:38:14] косякова просто лучше просто лучшее
[01:38:17] выступление я честно него недавно мы
[01:38:20] тоже ходил на интервью я его пересмотри
[01:38:22] почему потому что там очень много
[01:38:24] частности и рассказы и в том числе как
[01:38:27] активизировать гипер параметры в таких
[01:38:30] моделях как лагерем их жуков skittles и
[01:38:33] так далее эта вещь она ну и и очень
[01:38:36] часто спрашивают даже для junior
[01:38:38] специалистов как мы оптимизируем каким
[01:38:41] гипер параметры вести как активизировать
[01:38:43] какая формула как оптимизируем что в
[01:38:46] этой формуле есть на что обратить
[01:38:47] внимание это очень хорошо что ты уже
[01:38:50] что-то знаешь лучше если ты знал еще
[01:38:53] чуть больше я например ну вот сегодня
[01:38:55] они говорили об этом но я очень любил
[01:38:57] вопрос связан с метриками качества и на
[01:39:00] схемой а ты сегодня говорим этого мало
[01:39:03] справедливости ради да если мы говорим
[01:39:06] про на задаче
[01:39:07] регрессия r-квадрат как считается rms е
[01:39:10] почему rm если я лучше чем из нас есть
[01:39:13] точки зрения бизнес
[01:39:14] интерпретации как россия отличается как
[01:39:17] у нас я отличается она какая модель
[01:39:20] лучше
[01:39:21] почему лучше как смотреть вообще на эти
[01:39:24] метрики качества есть всякие квантиль
[01:39:27] нее
[01:39:28] loss как они работают типа вот мы м с
[01:39:32] кем они определили да а как лосса
[01:39:35] работает в виде фонтан как и не работает
[01:39:39] есть еще rms егэ очень интересная
[01:39:43] гладкая который там дифференцируема она
[01:39:47] очень прикольная она штрафует за не до
[01:39:50] прогноз и сильно программе сильно
[01:39:52] штрафуют за не это прогноз ней чуть
[01:39:55] меньше штрафуют за перри прогноз в каких
[01:39:58] случаях какую метрику качестве нужно
[01:40:00] выбрать это вот прям как важный момент и
[01:40:02] он очень сильно влияет вот так как мы
[01:40:06] работаем с метрика качественно то как мы
[01:40:08] работаем с loss как оптимизируем на эту
[01:40:10] метрику непосредственно очень сильно
[01:40:13] говорит об уровне знания и об уровне
[01:40:17] опыта специалистов до принципе все там
[01:40:21] по бетону очень много вопросов очень
[01:40:23] много вопросов по
[01:40:25] анализу по работе с данными там много
[01:40:29] вопрос может быть но думаю все это можно
[01:40:32] там осилить течение какого-то день тесно
[01:40:36] было клёво я очень рад есть куда расти
[01:40:39] есть что поднимать и тебе остается
[01:40:42] только сесть и и работы спасибо большое
[01:40:46] саша забыл круто спасибо тебе огромное я
[01:40:48] получил удовольствие да спасибо да я
[01:40:52] надеюсь что что у нас будет там серия
[01:40:54] вот таких вот мог интервью она будет
[01:40:56] общий доступ а возможно при себя тоже
[01:40:59] увидишь
[01:41:01] надеюсь что что в будущем когда ты
[01:41:03] будешь смотреть себя тут же много
[01:41:06] ответов надежду на те вопрос который
[01:41:08] считал его не были за все спасибо
[01:41:11] большое

FEEDBACK_MD:
---
section: "Конец, обратная связь"
start: "01:32:18"
end: "01:41:13"
start_seconds: 5538
end_seconds: 6073
---

на этом все давай я тебе расскажу ей дам немножко обратная связь покойного как это было значит во первых хочу поблагодарить тебя это реально очень здорово что ты готов выходить на мог интервью ты готов общаться ты готов получать какой-то там это очень здорово теперь по а секция 1 секция капитона честно очень сильно не хватает питона соответственно я бы наверное в первую очередь упор делал именно на питон на то чтобы узнать детали чуть побольше посмотреть какие-то лекции есть очень хорошие открытой лекции хотя папе туману но они такие они больше про алгоритмы но они очень хорошо дают вот базу а уже поверх базы работаем с тем что нам нужно в мыле да честно я иногда спрашиваю junior of middle of которые говорят что они не дури а на самом деле ну там прям большие группы в знаниях я иногда даю вы знаешь задачу реализуем меня пожалуйста градиентный спуск в питоне вот прям 75 или пишет возьми алгоритм построение дерева сам взять и напиши возле стохастический людей ный спуск сам сядь и выпиши напиши будет стробирования bootstrap взять напиши ты это все равно будешь использовать в аналитике ты все равно это будешь использовать в работе но тебе нужно да да работе мы не пишем кредит газ куска но это очень хорошо дает понимание того как нам нужно действовать алгоритм как он работает и так далее тот же группой sum sum sum но типа он же ничего сложного нету дам тебе нужно просто пройти по листу и все а в питонами когда ты знаешь вот базу когда ты знаешь как работает какие-то конкретные вещи все остальное много проще положить незнания пройди миллю незнание по работе с данными и статистику я б тест то есть но я тебе говорю как бывший разработчик то есть я как раз от разработчика шоу меня было хорошее математическое знаем но математическая база физическая база хорошая и я еще и программировать у меня потрясная вот тихоньку скатывался dvd с именно через программированию теперь что касается оба тестов а пытаясь то были прикольно я достаточно развернуто тебе дал про то какие еще кейс интервью вот бывают побыть с пожалуйста просто снять прочитаю несколько статей это существенно улучшить ну и нужно набить руку нужно набить руку просто взять какие-то данные посчитаю статистиками посчитай а как статистиков бы цепи выглядит почему так и так далее то есть просто реализовать посмотреть набить руку просто набить руку что касается работа с данными очень большой момент и вот мне не понравилось что ты не знаешь оконной функции хотя на самом деле есть множество открытых тренажеров который позволяет позволяет наработать руку со своими запросами в том числе с оконными функциям у нас синтаксиса как он их функцию он плюс-минус выглядит следующим образом есть какая-то гравитационная функция допустим сам или каунт или еще что-то и дальше идет такое о в окно в окне партий шамбал ордер по и еще иногда там есть такое роуз between и вот в роуз between есть еще вот антипов between the dates по датам то есть все вот эти вот возможные агрегации возможно и окна нужно ли делать опять таки есть тренажеры можно найти есть обман и можно найти есть очень хороший инструмент который в ближайшем времени тоже выйдет это инструмент там тренажер для менеджера моего сделать но по сути своей он такое он в том числе для новичков там есть и базовые знания танкович делай троен и и посчитать различные агрегационную функции это вот прям очень нужна а затем оконные функции посчитать и так далее что ты очень часто задача вот например там в предсказании спроса ценообразование реальных задачах очень часто задачи звучит следующим образом посчитай сложна и средние за какой-то период каким-то окном и пошел просто так теперь что касается в мыле конечно нужно устаканить какие-то вещи какие вещи еще спрашивают очень часто то есть честно кросс в редакционной вещи вот это нужно знать очень спрашивают про то как мы оптимизируем тут и ту или иную модель честно одно из самых просто офигенных выступлениях по вещам связан с деревьями с random forest is глядим пустить приз есть выступление игоря косякова просто лучше просто лучшее выступление я честно него недавно мы тоже ходил на интервью я его пересмотри почему потому что там очень много частности и рассказы и в том числе как активизировать гипер параметры в таких моделях как лагерем их жуков skittles и так далее эта вещь она ну и и очень часто спрашивают даже для junior специалистов как мы оптимизируем каким гипер параметры вести как активизировать какая формула как оптимизируем что в этой формуле есть на что обратить внимание это очень хорошо что ты уже что-то знаешь лучше если ты знал еще чуть больше я например ну вот сегодня они говорили об этом но я очень любил вопрос связан с метриками качества и на схемой а ты сегодня говорим этого мало справедливости ради да если мы говорим про на задаче регрессия r-квадрат как считается rms е почему rm если я лучше чем из нас есть точки зрения бизнес интерпретации как россия отличается как у нас я отличается она какая модель лучше почему лучше как смотреть вообще на эти метрики качества есть всякие квантиль нее loss как они работают типа вот мы м с кем они определили да а как лосса работает в виде фонтан как и не работает есть еще rms егэ очень интересная гладкая который там дифференцируема она очень прикольная она штрафует за не до прогноз и сильно программе сильно штрафуют за не это прогноз ней чуть меньше штрафуют за перри прогноз в каких случаях какую метрику качестве нужно выбрать это вот прям как важный момент и он очень сильно влияет вот так как мы работаем с метрика качественно то как мы работаем с loss как оптимизируем на эту метрику непосредственно очень сильно говорит об уровне знания и об уровне опыта специалистов до принципе все там по бетону очень много вопросов очень много вопросов по анализу по работе с данными там много вопрос может быть но думаю все это можно там осилить течение какого-то день тесно было клёво я очень рад есть куда расти есть что поднимать и тебе остается только сесть и и работы спасибо большое саша забыл круто спасибо тебе огромное я получил удовольствие да спасибо да я надеюсь что что у нас будет там серия вот таких вот мог интервью она будет общий доступ а возможно при себя тоже увидишь надеюсь что что в будущем когда ты будешь смотреть себя тут же много ответов надежду на те вопрос который считал его не были за все спасибо большое

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
Target version for this run: v14 only.
Write JSON only to: data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json
(Step 1 created an empty stub `items: []` at this path — you MUST replace it entirely.)

FORBIDDEN on step 2 (hard — run invalid if violated):
- Open, read, copy, merge, or patch ANY prior qa-split JSON in this interview folder.
- Use IDE search across `*.v*.qa-split.json` except the target file above.
- Reuse items[] or field text from older runs because validation passed before.

Forbidden prior artifacts (do NOT read):
  - data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v2.qa-split.json
  - data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v3.qa-split.json
  - data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v4.qa-split.json
  - data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v5.qa-split.json
  - data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v6.qa-split.json
  - data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v7.qa-split.json
  - data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v8.qa-split.json
  - data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v9.qa-split.json
  - data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v10.qa-split.json
  - data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v11.qa-split.json
  - data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v12.qa-split.json
  - data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v13.qa-split.json

After saving JSON, agent MUST run:
  python3 .claude/skills/splitter/step1-prepare/splitter_check_prior_leak.py data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json
(exit 0 required; exit 1 = identical to an older version — re-extract from transcript)

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
Save JSON to: data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json

Then (preferred — no LLM):
  .claude/skills/splitter/step3-excel/splitter_post.sh data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json \
    --video data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/video.md

Or manually:
  python3 .claude/skills/splitter/step3-excel/splitter_json_to_excel.py data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json --out data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.xlsx

Validation (video.md offline only — never paste into the model):
  python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
    --splitter data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.qa-split.json \
    --video data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/video.md \
    --tolerance 120 \
    --out data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.validation-report.md

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
   - for `technical_coding` / pair programming: flag false if candidate_answer contains interviewer coaching ("ты видишь", "не слушай ты усложняешь", "давай напишем", "проговори", "тебе нужно", "супер напиши") — those belong in interviewer_feedback; candidate_answer = candidate-only spans concatenated
   - interviewer_question is a complete intelligible question (flag false if truncated ASR: ends mid-clause like "...еще не Что", "...должен быть", or duplicates the opening of candidate_answer)
   - interviewer_question and candidate_answer do NOT share a long verbatim prefix (flag false if the first 6+ words are identical — echo / mis-attributed span)
   - interviewer_feedback contains only the interviewer's speech (flag false if candidate biography/case continuation appears there: "я пошёл", "у нас Kanban", "мы причесали", "я считаю что лучший код", etc. — that belongs in candidate_answer)
   - for `technical_coding` / live Colab tasks: flag false if `candidate_answer` is one short line but `reference_answer.time` is many minutes later and the chapter window shows a long pair-programming dialogue — collect candidate-only attempts in `candidate_answer` and interviewer coaching in `interviewer_feedback` (both may be long; do not merge speakers into one field)
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
video.md: /Users/mm/projects/ds-final-project/data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/video.md

--- CHAPTER `00:02:30` — Вопрос на изменяемые и неизменяемые типы данных ---
window: 00:02:30 .. 00:06:21
recognition_status: multiple (2 items)

ITEM #1
  interviewer_question: time=00:03:00 text='изменяемые и неизменяемые типе данных кто не что это вообще такое какие типы данных каким типом данных'
  candidate_answer: time=00:03:08 text='освоения из не изменяют наверно мне известны словари который мы единожды прописываем и долине меня остальные ведьмами дня мы типа данных я правильно понимаешь кричите про сирии dataframe и списке'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: Python

ITEM #2
  interviewer_question: time=00:03:57 text='давайте рассмотрим конкретно intel флот и стринги листы сеты теплые эдикты вот что'
  candidate_answer: time=00:04:06 text='из этих семи получается изменяемые что они теплые лифты не меня же мы остальные меняем и диксы это словарь это там где она соответствует какое-то значение какому-то значению более научным языком на но я не смогу сказать теплые это не меняем эй наборы значений насколько я помню все остальное наверное мы можем менять dig-t и еще раз никто мы можем менять и нет нет не может хорошо а теплые можем насколько я помню тоже нет так хорошо и с этой бабой можем или вот это сложно это было я читал но не пользовался и наверное ничего не скажу процент и хорошо entry вот но int'
  reference_answer: time=00:04:50 text='и целые флоты подробно и до стринги они все от меня и мы не меняем мы говорим о том что если я какой-то переменной присвоил мне как эта переменная типа int и могу ли я разные значения в нее власти в процессе по сути своей да но не совсем так смотри изменяемые что что это значит представим себе что у нас есть лист в этот лист мы добавляем какое-то значение вопрос изменился ли илистых нет и изменилось ли ссылка на личику памяти в этом месте вопрос на самом деле чуть более сложный сразу тебе скажу что ты не прав своих представлениях что вадик ты не изменяем тип данных об этом собственно будет наша'
  interviewer_feedback: time=00:05:30 text='сразу тебе скажу что ты не прав своих представлениях что вадик ты не изменяем тип данных об этом собственно будет наша задача самое первое вот и чуть чуть поговорим про он давай вот чтобы у тебя в голове был правильный ответ то ты флот и другие неизменяемые теплыми изменяемые что это значит что в случае если ты что-то делаешь с этими данными этим четырьмя с это тоже не то ты по сути своей перри создаешь объект бетонные который будет ссылаться надо будет память однако есть нюанс о котором мы поговорим в летах но важно понять что дикари это изменяет тип данных и об этом'
  question_topic: Python

--- CHAPTER `00:06:21` — Задача на dict и ответ Дмитрия ---
window: 00:06:21 .. 00:08:15
recognition_status: single (1 items)

ITEM #3
  interviewer_question: time=00:06:22 text='канаде нас есть некоторые функции она вот у тебя в следующих строчкой да есть три ячейки что в этой функции происходит она на вход принимает dict и на выходе выдает значит без разницы какой dictionary он получил на вход у нас идет такое объявление нового ключа и значение для этого а z равно 99 у нас есть вот такая функция foo у нас есть dictionary виде один a2b 34 d у нас есть объект б как функция от нашего диктор и затем встает вопрос равны ли а и b вот это этот самый последний часть дмитрий могу я тебя попросить сделать вот нажать в контру плюс чтобы чуть-чуть приблизить чтобы мы могли получше ну и человек который будет смотреть это transform мог получше видеть что происходит control + или shift + как-то приблизить как-то нам нужно увеличить масштаб он мог супер супер вообще идеально давая вопрос собственно он и в самом низу равно ли а и б по сути своей это булент проверка и нам нужно ответить либо true либо фолз вот какой ответ как ты думаешь у нас функции формы принимает'
  candidate_answer: time=00:07:58 text='а потому что она выдаст ru'
  reference_answer: time=00:08:16 text='да действительно труп но встает вопрос как выглядят они как выглядит как там но мне кажется что а мы увидим содержимое а то что мы видим сейчас 12 бы так далее и z99 и [музыка] а это будет одно и то же что это значит что dict который пришел на вход он типы измениться и мы на самом деле в этом у нас есть'
  interviewer_feedback: time=00:08:16 text='да действительно труп но встает вопрос'
  question_topic: Python

--- CHAPTER `00:10:38` — Задача, цель которой — сделать, чтобы дикты были разные, ответ Дмитрия ---
window: 00:10:38 .. 00:13:51
recognition_status: single (1 items)

ITEM #4
  interviewer_question: time=00:10:40 text='отсюда как мне сделать так чтобы а у меня осталось к 1 a2b 34 д а б было как один a2b 34 tz-9030 изменить функции может ли ты изменить эту функцию или можешь ли ты изменить как-то создании объекта бы чтобы по сути расщепить эти два dicota'
  candidate_answer: time=00:13:11 text='давай подумает что произойдет приравниваем значению б.а. видимо описать его нужно сначала потом в бой добавится за 99 возвращаем б а у нас останется не тронут и на выходе у нас будет хорошо давай запустим посмотрим что получилось запустить следующую ячейку точно также и давай я выведем а и b как или теперь выглядит до кажется не сработало'
  reference_answer: time=00:14:39 text='хорошо есть как минимум несколько вариантов как мы можем это сделать по сути своей нам все равно придется действовать следующим образом нам нужно будет но там с точки зрения как по памяти до занять новый дедсек по мы можем сделать несколькими вариантами самый простой будет года где-то и b равно а до написан магичить номер 5 да я понимаю вот здесь написать b равно а . копит запустить и запустить следующую значит можем увидеть что мы с точки зрения памяти теперь обращаемся в две различные лечить памяти и дальше если ты посмотришь на pride aeb то можно увидеть что мы по сути своей сделали два различных dicota помимо папе и есть там понять эдип копия копии или можно был вот прям функции foo сделать новый словарь холке and views from сделать просто новый дик ну то есть по сути своей сделать deep копи'
  interviewer_feedback: time=00:13:49 text='кажется не сработало'
  question_topic: Python

--- CHAPTER `00:16:10` — Вопрос о выделении и очистке памяти в Python, ответ Дмитрия ---
window: 00:16:10 .. 00:16:26
recognition_status: not_recognized (0 items)

(no items extracted)
--- CHAPTER `00:19:00` — Вопрос о генераторах, декораторах и итераторах ---
window: 00:19:00 .. 00:20:35
recognition_status: single (1 items)

ITEM #6
  interviewer_question: time=00:19:03 text='по вере очень часто еще спрашивает про генераторы операторы декоратор питоне что это такое чем например оператора от генератора отличать и вообще что такое декоратор питон я читала все это знакомо но хорошо на практике может быть что-то использовалась при виде пожалуйста'
  candidate_answer: time=00:19:15 text='декоратор питон я читала все это знакомо но хорошо на практике может быть что-то использовалась при виде пожалуйста примеры оператора декоратора но давай декоратор примеры использования пример используем давайте я приведу только один пример и декораторами и пример использования это когда мы перед функции перед функции пишем такую собачку и название декоратор да я понял нет не'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:19:26 text='примеры оператора декоратора но давай декоратор примеры использования пример используем давайте я приведу только один пример и декораторами и пример использования это когда мы перед функции перед функции пишем такую собачку и название декоратор да я понял нет не пользовался окей хорошо ну я тогда с твоего'
  question_topic: Python

--- CHAPTER `00:20:35` — Вопрос о моделировании A/B теста ---
window: 00:20:35 .. 00:30:57
recognition_status: multiple (2 items)

ITEM #7
  interviewer_question: time=00:21:25 text='опять-таки в зависимости от уровня в зависимости от того работал ли уже человека нет задаются различные вопросы я задам простой вопрос представь себе представьте что у тебя есть некоторая рекомендательном адель или рекомендательных систем ваш некоторые рекомендательные системы для их сайт рамках этого сайта уже какое то время назад был блог который спалит заполнялся каким-то рекомендуешь ну какой то рекомендательный модель значит так к тебе приходит product этих рекомендаций говорит дмитрий мы запускали новую модель угаре календарь и хотим оценить эффективность новой модели и хотим чтобы ты сделал так называемый дизайн эксперимент что это значит в рамках дизайн эксперимент это должен ответить на несколько основных вопросов первый вопрос на какие метрики мы будем смотреть как мы будем оценивать эффективность работы рекомендательных модель предположить если не знаешь ну я тебе помогу подскажу это 1 2 темы тебе нужно предложить разбиение людей на основе какого-то понимания вообще того как работают от теста и 3 тебе нужно провести то есть представьте себе что эксперимент прошел то есть ты сделал выбрал метрики сказал как будем делить пользователей села команда пошла начала делать эксперимент действительно каким-то образом делит людей на группы тебе нужно сделать оценку результатов qstring чем подробней ты расскажешь тем будет лучше у тебя где-то 20 20 минут на то чтобы 1 из 1 все так'
  candidate_answer: time=00:23:19 text='отвечать не как сделать первые ты мы определяемся с метриками если говорить про рекомендательных систем у меня нет большого опыта но видимо мы что то рекомендуем люди либо как либо кликают либо покупают это нота желаемой что мы хотим наблюдать соответственно это будут наши метрики допустим пусть это будут клейкие пусть это будут блики и покупки мы можем видеть это будет критерием там заинтересованности и качеству работы новой рекомендаций системы мы определились с двумя метриками они нам интересны мы хотим выбрать группы на которых будем проводить эксперимент соответственно одной группе будет показана одной группе будет даваться старая рекомендации система другую руку будет даваться ногу рекомендуется система группы соответственно мы хотим чтобы они были как это называется они были однородными чтобы в и не различались между собой по по составу по составу людей по качеству здесь так можно сказать да чтобы грубо говоря нас не получилось так что в одной группе терку мальчики другой только девочки мы хотим что в каждой группе были равные количества мальчиков равное количество девочек пропорционально равная 1 группы из 2 ну и соответственно по остальные признаком которые у нас есть допустим возраст допустим география если мы только в центральном регионе проводим соответственно особе группы при прочих равных условиях центрального региона понять что эти группы одинаковые что они подходят для этого эксперимента мы можем оао тестом мы берем эти две группы снимаем с них показания интересующих нас метрик и проводим артист соответственно а а тест на покажет есть ли статистически значимые различия между этими двумя группами если представить что мы хорошо отобрали себе группы и они на подходят что они абсолютно абсолютно что они достаточно разные одинаковые там и первой группе продолжаем оказывает старые рекомендации разрубим показываем новые рекомендации кроме того перед тем как приступить мы определяемся с нам нужно понять какое количество наблюдений мы хотим потому чтобы наши выводы имели вес имели какое-то значение если представить что мы во второй группе у нас оказалась здесь человеком первой группе еще 2 10 человек то можно говорить о том что это предполагает что это не достаточное количество есть калькулятор она в том числе вот на на курсах карпова мы считали руками необходимый объем выборки необходимый объем группы который нам нужен для того что провести эксперимент я наверное не вспомню конкретные уравнение формула но там опять же если мы калькулятор откроем то там нам предложат ввести различие которые мы хотим наблюдать мощность критерия порог на которую мы хотим некий порог некий различий который мы хотим заметить по моему все и мы таким образом получаем необходимо необходимо число наблюдений которая нам нужна для того чтобы сделать какие-то выводы допустим тем мы провели эксперимент у нас есть для гроба значений по каждой метрики далее мы их сравниваем сравниваем с помощью статистических тестов мы хотим оценить распределение первой выборке то которые у нас было на старой рекомендательной системе принципиально будет ли она носить нормальный характер ты какой-то другой характер от этого зависит этот тест который мы выберем либо параметрически либо непараметрический если она носит распределение выборки если растление выбор клип носит не нормальный характер то из того что мы делали мы пытались привести ее к нормальному через логарифмирование еще какой-то способ не помню если прости пожалуйста пока ты не ушел далеко'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:28:32 text='дмитрий давай так про дизайн эксперимента в целом все говоришь про меня все говоришь про ну то есть ты говоришь о том что мы берем смотрим на метрики то есть выбираем 2 метрики как тир и конверсия клип конверсии в покупку супер супер что ты предложил в минимум 2 по факту нужно предлагать чуть больше нового для это уже клёво ты клёво очень сказал про а тест про то что должны быть люди которые похожи друг на друга мы их там равные единственно что не сказал это в каких долях мы делим типа 50 на 50 или мы делим как вдруг у но есть еще и усложнения которые тоже бывают и она очень часто бывает и хороший аналитик должен задать вопрос а какой нос трафик как много событий у нас прилетает потому что если собрать очень много прилипает то есть смысл взять только часть людей допустим 10 процентов людей которые заходят и на 10 процентов проводить очень весь экспериментов 10 процентов а затем поделить допустим 50 на 50 1 дать одну рекомендательным огарев другой дать другой или просто сделать 91 1090 со вторым отбеливать 10 снова будильником условно но вопрос про количество событий которые генерируются он на самом деле важен затем ты все правильно сказала что есть вопрос связан с тем чтобы рассчитать сколько событий данном месте так называемый консул или порог который попытался вспомнить есть int age- и вынимаем детектирует эффект что еще ну там можно всякий вода есть еще может супер счет сказал супер'
  question_topic: Experimentation

ITEM #8
  interviewer_question: time=00:27:29 text='прости пожалуйста пока ты не ушел далеко в сторону вспомни метрики case метрики ты выбран за конверсию криком версия покупка вопрос откуда там распределения конверсия конверсия в покупку это просто цирк хотелось бы чуть больше про по тестам потому что кажется что это важно по сути у нас на выходе будет по первой группе по одной метрики две цифры тех кто кликнул и те кто не кликнул по 2 метрики но считаю что то же самое те кто купил и те кто не купил я вспоминаю статистический критерий для доля да там действительно выборки нет там немножко по другому дану соответственно применяем эстетический критерий для сравнения двух долей'
  candidate_answer: time=00:28:00 text='статистический критерий для доля да там действительно выборки нет там немножко по другому дану соответственно применяем эстетический критерий для сравнения двух долей не вспомнил я могу даже могу наверное написать формулу потому что я решал задачи и она у меня осталась'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:28:32 text='дмитрий давай так про дизайн эксперимента в целом все говоришь про меня все говоришь про ну то есть ты говоришь о том что мы берем смотрим на метрики то есть выбираем 2 метрики как тир и конверсия клип конверсии в покупку супер супер что ты предложил в минимум 2 по факту нужно предлагать чуть больше нового для это уже клёво ты клёво очень сказал про а тест про то что должны быть люди которые похожи друг на друга мы их там равные единственно что не сказал это в каких долях мы делим типа 50 на 50 или мы делим как вдруг у но есть еще и усложнения которые тоже бывают и она очень часто бывает и хороший аналитик должен задать вопрос а какой нос трафик как много событий у нас прилетает потому что если собрать очень много прилипает то есть смысл взять только часть людей допустим 10 процентов людей которые заходят и на 10 процентов проводить очень весь экспериментов 10 процентов а затем поделить допустим 50 на 50 1 дать одну рекомендательным огарев другой дать другой или просто сделать 91 1090 со вторым отбеливать 10 снова будильником условно но вопрос про количество событий которые генерируются он на самом деле важен затем ты все правильно сказала что есть вопрос связан с тем чтобы рассчитать сколько событий данном месте так называемый консул или порог который попытался вспомнить есть int age- и вынимаем детектирует эффект что еще ну там можно всякий вода есть еще может супер счет сказал супер наверное не буду бальзамом на душу бы уж тут и протез сказал про историю про то что мы проверяем затем смотреть когда пошла оценка пошел росси chrome да немного в различные стороны начал смотреть немного ушел прямо начал выходить не туда я понимаю что ты говоришь про пироман перечисление про металлическими варианты но вопрос откуда либо возьмите если у нас распределение нет у нас проснись цифры цикл правильный ответ что были две нити распределения на генерирует можно ну типа вообще крик меня вопросы на'
  question_topic: Experimentation

--- CHAPTER `00:30:57` — Вопрос о генерации распределений ---
window: 00:30:57 .. 00:31:22
recognition_status: single (1 items)

ITEM #9
  interviewer_question: time=00:30:57 text='вопрос как мы можем сгенерировать распределение исходя из наших вот выборок представь что ты взял к дереву людей 5050 взятом допустим 10 людей поделилась 5050 как мужу из них получить'
  candidate_answer: time=00:31:14 text='распределяем конверсия конверсия конверсия а мне кроме быстро приходят так вот он и есть он есть'
  reference_answer: time=00:31:25 text='смысл чём смысл в том что если мы просто циферки сравниваем до конверсия в конверсию покупку то мы используем так называемый хи-квадрат это вот то что то пытался вспомнить надаль агс достаточно долях идеально работает так далее но там 10 вариант когда ну не использовать хи-квадрат а вот берем быстро-быстро пируем мы быстро пируем доли для всех книг и конверсию покупку и смотрим на вот эти распределения они по дефолту будут нормальные соответственно для будет скопирован их конверсий вклейкой конверсии покупку какой-то с мы будем применять'
  interviewer_feedback: time=None text=None
  question_topic: Statistics

--- CHAPTER `00:31:22` — Подводка к критерию стьюдента и вопрос про ограничения его применения ---
window: 00:31:22 .. 00:32:26
recognition_status: single (1 items)

ITEM #10
  interviewer_question: time=00:32:15 text='какие ограничения половинки test is now желаемое количество наблюдений приходит в голову будет предполагаем что она будет каким-то большим нормальность'
  candidate_answer: time=00:32:20 text='в голову будет предполагаем что она будет каким-то большим нормальность распределения вот этот момент он на'
  reference_answer: time=00:32:31 text='нормальности распределения самом деле это . спора я специально задал этот вопрос специально задолго просто ограничение почему потому что здесь можно много дискутировать на тему обязательно людей должны быть нормальное распределение дтп или они должны быть симметричны потому что есть нюанс в том как мы смотрим на значит мышцы пресса можно ли мы его использовать и можем ли мы его использовать для ненормальных распределений в скобочках можем но там есть определенные нюансы почему можно использовать и без на даже не на не нормальное распределение при условиях есть нюанс реально можно почитать лучше читать зарубежную литературу или очень хорошо вот мне нравится там ребята языке x tf которые прикольно об этом рассказывают и у них можно почитать статьи нормальность распределения это некоторые упражнения на самом деле который очень часто преподается но которое не является истинным последней станции и этот момент он право дискуссий то есть мы должны пообсуждать почему обязательно нормальное распределение или ненормальная и и можем ли мы'
  interviewer_feedback: time=None text=None
  question_topic: Statistics

--- CHAPTER `00:32:26` — О необходимости нормальности распределения ---
window: 00:32:26 .. 00:33:46
recognition_status: not_recognized (0 items)

(no items extracted)
--- CHAPTER `00:33:46` — Тесты для проверки на нормальность ---
window: 00:33:46 .. 00:34:24
recognition_status: single (1 items)

ITEM #11
  interviewer_question: time=00:33:48 text='у нас есть проверки на нормальность что приходит голову'
  candidate_answer: time=00:33:52 text='есть несколько тестов shopper и мелко по-моему в источниках описывается несколько они все приравниваются примерно говорят что они равна равнозначны дает похожий результат и тем не менее у разных а у разных авторов из разные предпочтения из того что я делал sape.ru вилка тест'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:34:15 text='хорошо супер супер но лучше всего иметь как минимум там 2 ответа пей спеша'
  question_topic: Statistics

--- CHAPTER `00:34:24` — Как сравнить ненормальные распределения ---
window: 00:34:24 .. 00:35:02
recognition_status: single (1 items)

ITEM #12
  interviewer_question: time=00:34:24 text='если у нас опять таки ненормальное деление как мы можем сравним два'
  candidate_answer: time=00:34:30 text='ненормально проследить есть непараметрические тесты один из помнишь parametric это стьюдента не parametric а'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:34:39 text='это монолит не супер почему-то в источниках он единственно их на самом деле там много в теории вот во всяком случае в жизни применяют либо тит если бы волна with a наверное из-за того что мама ведь достаточно ну популярен в принципе я его достаточно просто реализовывать прощать просто теле хорошо'
  question_topic: Statistics

--- CHAPTER `00:35:02` — Подводка к вопросу о нормальности распределения средних при бутстрапе ---
window: 00:35:02 .. 00:36:04
recognition_status: multiple (2 items)

ITEM #13
  interviewer_question: time=00:35:03 text='дальнейшие вопросы которые могли бы быть это как работает с как именно работает и гитарист этого он же мало ведь нет и наверное последний вопрос который я бы задал такой абэ слэш статистике это почему же у нас требует стракера ваней при быстро первыми доме будут виде некоторого нормального растут давай я и даже не дали упростить или вопрос чем средний при быстро перова нее будут виде нормально'
  candidate_answer: time=00:35:35 text='волшебная центральная предельная теорема'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:35:39 text='этого достаточно то что я сказал сейчас в доказательство в какие-то более подробные вещи там такая математика безумно короткий ответ что да вот из данного клёвый если ты можешь вспомнить очень описание пятеро не какой-то доказательство это будет звучать офигенно но в целом в целом достаточно'
  question_topic: Statistics

ITEM #14
  interviewer_question: time=00:36:03 text='значит она на будущее просто сразу скажу что там для людей которые уже имели опыт создание там и проведение apts дизайн экспериментов тогда она фанерный есть несколько проблем в тех же рекомендации что у нас есть допустим там store пользователи по которым ты можешь сделать а тест а для новых пользователей как что мы будем делать на новых пользователей и т.п. на'
  candidate_answer: time=None text=None
  reference_answer: time=00:36:36 text='будем пробовать сделать честный рандом то есть честно делить вне зависимости от того какие люди на две равнозначные группы честный рандом можно сделать через подсчет сша на человека и остаток а тени на что то это будет там при ранец если bug1 либо к другой группе я считаю что таким образом независимо от пола возраста географии национальности мы вот через этих и шик мы сделал выборку прямо на у нас будет вот идеально рандомно и она будет похоже на то что ну типа тесли у нас очень большой трафик сайт the random честный рандом он действительно разделит людей на две группы они будут похожи друг на друга реально это так однако если у нас трафик помочь большой у нас есть частицы фика какая-то по работе нашего сервисы которые рекомендации показывай то да есть нюанс что может быть такое что в одной группе одни люди в такой группе другие но честный рандом там по факту предполагается что он действительно по дереву купола'
  interviewer_feedback: time=None text=None
  question_topic: Experimentation

--- CHAPTER `00:36:04` — Как быть, если нет старых пользователей, и нужно провести тест только на новых ---
window: 00:36:04 .. 00:37:53
recognition_status: not_recognized (0 items)

(no items extracted)
--- CHAPTER `00:42:04` — Вопрос про разницу Where и Having ---
window: 00:42:04 .. 00:44:20
recognition_status: multiple (2 items)

ITEM #15
  interviewer_question: time=00:42:52 text='работы сына исходит'
  candidate_answer: time=00:42:56 text='с каким базам данных на работу house и пусть греет а называется скулы супер'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: SQL

ITEM #16
  interviewer_question: time=00:43:11 text='силе что-то oh-группой и тогда вопрос есть хелен и есть в оба варианта накладывают каким-то образом условия'
  candidate_answer: time=00:43:25 text='вопрос как работает и как работает и чем они отличаются друг от друга но синтаксически вы всегда будет перед грубо если будет грубой не помню может быть они даже не дружит но heaven накладывается на то что сортировка грубое тело грубая потом heavy но может быть в разных диалектах я уже сталкивался с этим что в теории как будто бы они они не должны дружить хэви и грубая хэви и в они могут оказаться в этих запросов до могут быть но у меня одновременно это работал из опыта но камень привязан грубая когда мы отсортировали соответственно понимает уже ну грубо группой из очень транспортировку утра'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:44:18 text='хорошо супер супер а теперь можно'
  question_topic: SQL

--- CHAPTER `00:44:20` — вопрос про виды join и задания на join ---
window: 00:44:20 .. 00:45:57
recognition_status: multiple (3 items)

ITEM #17
  interviewer_question: time=00:44:22 text='женских вспомнить опять таки я тебе задаю вопросы для реджину поэтому они'
  candidate_answer: time=00:44:27 text='будут максимально простыми можешь пожалуйста вспомнить все варианты join или ружжо и jo in love джо играли join и есть еще outer join на самом деле больше но истец которых сталкиваться 4 который не романа край применял я щас напишу в'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: SQL

ITEM #18
  interviewer_question: time=00:44:46 text='коробе значит а я представь себе что нас есть таблица а таблицы до в таблице 100 записей в таблице б 50 записей'
  candidate_answer: time=00:44:55 text='пересечение а теперь это 25 записей вопрос лев join a и b и какое количество строк будет сторону училась будут надо насколько я понимаю да конечно будет стоить она теперь 150 супер an inner join 25 хорошо outer join окружен не сталкивался ну вот поскольку я помню два шарика они перекрываются у нас и серединке не будет не будет 25 125'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:45:14 text='150 супер an inner join 25 хорошо outer join окружен не сталкивался ну вот поскольку я помню два шарика они перекрываются у нас и серединке не будет не будет 25 125 хорошо теперь full джон по 150 супер и теперь'
  question_topic: SQL

ITEM #19
  interviewer_question: time=00:45:39 text='вопрос есть еще cross join о нём редко помнят о нем даже не знаю никто не'
  candidate_answer: time=00:45:45 text='сталкивался это декард во произведений дикарка и произведения то есть каждый скажем она будет 100 на 50 вот ну'
  reference_answer: time=None text=None
  interviewer_feedback: time=00:45:55 text='соответственно хорошо'
  question_topic: SQL

--- CHAPTER `00:45:57` — подводка к задаче про group by в Python ---
window: 00:45:57 .. 00:47:49
recognition_status: not_recognized (0 items)

(no items extracted)
--- CHAPTER `00:47:49` — Задача на group by в Python ---
window: 00:47:49 .. 01:06:22
recognition_status: single (1 items)

ITEM #20
  interviewer_question: time=00:48:05 text='тебе же нужно реализовать самую простую функцию которая на вход принимает list a и b они должны быть сервер брось бы они 1 одного размера и на выходе я должен включить dict у нас есть a b c вот эти ключи и для каждого из ключей посчитать сумму значения которые а где а в листе а ключи это значение которое есть нас т.п. а сумма это значение которые есть система не так сложно дала еще раз у нас есть a b c плести б разбросанные каким-то образом есть a123 49 досмотри представь себе таблицу в голове и представь себе таблицу у тебя есть таблица ключица значение а единица затем ключ и значение ключа 2 ключ 3c a5 a6 c7 a8 b делится 9 вот это вот таблица и теперь нужно сделать грубой б получается грубой б а . сам родов в памяти этап это все что тебе нужно это типа взять уникальное значение из б это цербер и для них посчитать сумму всех значений которые вот и есть в'
  candidate_answer: time=00:49:39 text='ну я бы видел это как цикл ну а это весь цикл длину вот этого листа в цикле я бы обозначил 3 переменная b c идя по циклу обращаясь к самой простой 3 условие if i в б такое избитый равно цвету c + а это и так далее нет не понимаю где поделать менять для меня потерь понял как работает грубой функция функцию 7 не пользовался просится а но я знаю как написать что как думаешь что он тебе сейчас как вы так циклов for отработал zip это объединение двух вот этих да просто простой объединение объединение'
  reference_answer: time=01:02:58 text='создаём пустой dict dt; затем for i, g in zip(a, b): dt[g] = dt.get(g, 0) + i. Функция get возвращает значение по ключу; если ключа нет — 0 по умолчанию.'
  interviewer_feedback: time=00:49:44 text='супер напиши но типа ты видишь это как цикл добавится кого напишу мы сейчас не у пару и вся с точки зрения как это лучше написать и так далее нам просто нужно сделать сделали проговорил давай как цикл добавится кого напишу мы сейчас не у пару и вся с точки зрения как это лучше написать и так далее нам просто нужно сделать сделали проговорил давай проговори логику цикл длину обозначил 3 переменная b c идя по циклу обращаясь к самой простой 3 условие if i в б такое избитый равно цвету c + а это и так далее да не слушай ты усложняешь честно говоря потому что ты здесь пытаешься pointer какие тут сквозь его цена этого не нужно тебе нужно просто пройти по вот этой связке а.п. давай сделаем первый шаг это получить dict у которого есть ключ виде какого-то значением уникального значения п а в значениях будет лезть из всех тех значений которые давай хочет принимали нет не понимаю где еще раз задачу нужно посчитать сумму ну агрегацию агрегацию покличу в посчитать сумму еще раз задачу нужно посчитать сумму ну агрегацию агрегацию покличу в посчитать сумму нам нужно сделать если вы вот в pandas если в память давай давай а даже сделаем напишем fantasy как я это вижу делаем импорт пандус спд делаем без видим здесь будет у нас dict виде большого и значение большого значения и e-bike б . а . сам и на мне закрыть тег вот и сохраню можешь пожалуйста перезагрузить страничку она тогда быстрее обновится и в самый низ и верх согрей то выглядеть нас есть pons.eu видя а и б у нас есть функции группой и мы считаем сумму по а то что нужно было сделать нет но новых у тебя выход выход выход должен быть в виде без грубой грубой и написать группа и сам добиться без поноса без группа я только у тебя выход должен быть в виде диктор у тебя а 15 b18 c20 вот такой выход из твои функции должен быть смотрели ты должен понимать группами она каким-то образом работа я хочу деле то что я тебе говорю что это dict это огромная подсказка вообще это прям огромное подскажет что тебе денег нужно кучу создаем словах об отце разделили нужно тебе не нужно вначале создавать словарь is a b c честно тебе нужно идти чтобы и создавать этот словарь если у тебя depth будет видеть c и b ничего страшного в этом нет ни об отце ну вообще ничего страшнее я понимаю типа значение присвоить как сумма туда затолкать хорошо давай напишем цикл начнем с того что мы будем идти по мы конечно уходим вообще в другую сторону мне лень и куда-то пошёл да вот здесь давай напишем давай б не незачем прям сразу и большое от выдачи и нам что нужно сделать давай я сверху перед циклом for создадим они кредит давай назовем его dt вот супер как пустой дик супер и теперь в dts делаем вообще что и dt от и квадратные скобки равно 2 и равно нулю просто-напросто все равно нулю и давай вернем в этот бета-ритм после цикла for вот запустить запустить запустить и группой и теперь давай напишем что следующей ячейке уже новую ячейку станем вот слева сверху написано + код вот и вот здесь вот напишем print грубой сам он так тот или туда а и b переданы все запускаем супер у нас получилось c00 b0 вроде бы понятно то есть мы прошлись по б мы создали вот эти вот вещь теперь смотри нам нужно одновременно и тигипко b и по а давай сделаем следующий цикл for одинакого размера да мы считаем что они одинаково размеры да они одинаково размеры по дефолту они обязательно одинаковый размер то а давай сделаем вот в нашем цикле пройдемся по виду знаешь ли функцию zip но я тебя сейчас просто расскажу как написать потому что тяжело нашли три их ok но нее не осталось окей хорошо а давай напишем просто фон и , g вот здесь и , g вот здесь и мы zip а.б. [музыка] да теперь смотреть нам нужно dt сделать g потому что у нас уникальные ключи будут в.б. и вот здесь нам нужно что то придумать мне неправильное нет конечно вот смотри и и это будут значение провести а вот соответственно нужно что то придумать ты знаешь что что есть и есть g вы проходите вместе по obd вот вы такой пары ведете окей окей окей окей знаешь я зря на тебя до blue давай сделаем следующим образом до blue давай сделаем следующим образом следующим образом вот у нас были нули да вот мы видим в 14 и строчки нулей были давай мы если напишем здесь dt от g до только не равно а + равно напишем плюс равно и единичку поставить не плюс равно 1 вот и запустим и запустим теперь при так он говорит нам error ниже опусти пожалуйста давай посмотрим на error керрор цен слушай когда резик gresit а вот этот убери и вообще а как таковое вот все чтобы его да вот здесь вот вот это убери ее здесь оставим только for g вот и вот запустить и запустим а он говорит о том что ниже опусти он говорит о том что ррц потому что плюс равно единице ok плюс равно нельзя описать или на нам потому что нужно будет сделать то есть нам по сути своей нужно создать будет этот dict так не хотел делать тогда давай плюс равно берем вообще сделаем следующую схему давали контр за отрабатывает от каких назад черта не линии и вот здесь вот как ты мне тебя так натолкнуть чтоб ты понимал [музыка] рассказ оцениваешь блин ну просто нужно знаешь как нужно чтоб ты понимал как работает грубой но я не знаю вот ты понимаешь что происходит когда у нас была c0 b0 она не только вот что произошло мы присвоили всем вот этим а по центру ли вот в этой строке а это и что нам мешает присвоить ну потому что это это это вот в данном случае это это значение это не указатель это не яндекс и в данном случае это значение это не не индекс плюс равно вамбери пожалуйста потому что мы здесь неправильно написали давай напиши равно равно и вот так запускаем не запускать здесь вы так циклов for отработал zip это объединение двух вот этих объединение вот смотри а барды да ну вот смотри вот а и b это два листа до 2 листа он взял блин я знаю как тебе написать добавили напишем перед dt g&g равно тебе написать добавили напишем перед dt g&g равно и вот здесь вот обе enter снимки print и и запусти вот я уверен ты теперь поймешь как работает вот смотри чем делает 1-цы 23 п то есть он идет по вот этим списком теперь в самом конце самом конце он тебя оставил c9 а 829 это самое последнее значение которые принимали эти ключи остается написать сумму то есть мы вовсе не вложением идем я понимаю что ты все мне рассказал но я даже я видишь как я тебе даже на самом деле сказал про плюс равно потому что плюс равно хоть и не работает и не работает понятно почему на самом деле потому что нету включается а вон она его ссылается когда мы делаем плюс равно соответственно здесь нужно что то придумать созданную у тебя во первых д нет такого по определению и вот теперь ты кстати можешь посмотреть и понять в чем здесь ошибка да включая и включая и здесь терон ровно тот же что и у нас была он говорит о том что он не знает что такое и птицы и типа он вот второе значение dt а джинн он его ты его еще не создал ты его только создаешь но тут же на него ссылаешься соответственно нужно на самом деле здесь написать такую функцию get то есть д . get а вот ддт g равно dt вот здесь да да да два раза направо пиши . get круглые скобки здесь нужно написать и g ну вот и квадратную стоком скобка удалить написать , 0 круглую скобку закрыть elixir флюс и да и теперь давай попробуем запустить и как у нас получится делает get функция get она возвращает тебе значения в и льюс в ключе но если она этого ключа не найдет она вернет тебе нам мы этот man заменили на ноль по дефолту то есть вот это вот там функция get значение ключа , но это возврат значение party фото то есть если бы было ключ он бы его вернул значение если его нету он по дефолту возвращать 0 вот как работает группа issue честно говоря это чуть-чуть на питон чуть-чуть на знание того как вообще агрегационную функции работают ты должен понимать что здесь вот мы реализовали очень простую функцию суммирования до агрегация full на одну бросаю корреляционная функция в виде суммирования но на самом деле ничего тебе не решает сделать например умножение каждого ну так что кумулятивные умножение друг друга да ты можешь просто убрать плюсик поставить звездочку и ты будешь умножать каждом значении докажи это прикольно прикольно потому что типа она немного другая здесь по сути своей на самом деле по сути своей мы написали не просто грубой sum sum на кумулятивные суммы если еще упороться можем задать каким окно мы будем суммировать но это такой знаешь это хорошая практика на то чтобы понимать как работает оконные функции хорошо понимается как работает в еще питон как мы делаем в этот проход написать все это и и это честно говоря дает очень хороший куст в понимании того как мы работаем с данными как мы понимаем что лучше работает что хуже но есть нюанс нюансы всегда есть нюансы заключается в том что проход tiguan по всем значениям нашего значит который мы это такое себе условии если у нас очень длинные-длинные вот эти колонки есть понятие векторных сложений векторных предложений и всякие работы с векторами это существенно ускоряет работу и например ну работа лампой и рей и суммы мамой рейв она как раз на вектор на сложение как вот так далее то есть там есть тоже свои нюансы того как это работает в цену в целом вопрос связаны по работе с данными они'
  question_topic: Python

--- CHAPTER `01:06:22` — Задача о линейных регрессиях ---
window: 01:06:22 .. 01:09:47
recognition_status: multiple (6 items)

ITEM #21
  interviewer_question: time=01:06:53 text='поговорим по суле есть такие вот модели линейной регрессии а нож какой-нибудь'
  candidate_answer: time=01:07:00 text='вспомнить простая линейная rising когда на вход подаем какие-то резисторы на выходе получаем числовое значение непрерывная'
  reference_answer: time=None text=None
  interviewer_feedback: time=01:07:10 text='хорошо давай вспомним просто там формулу'
  question_topic: ML

ITEM #22
  interviewer_question: time=01:07:10 text='хорошо давай вспомним просто там формулу линии или модели дамы какой-то простой'
  candidate_answer: time=01:07:17 text='крем из математики y равно 0 плюс bx'
  reference_answer: time=None text=None
  interviewer_feedback: time=01:07:20 text='супер а 0 плюс bx какие коэффициенты с'
  question_topic: ML

ITEM #23
  interviewer_question: time=01:07:20 text='супер а 0 плюс bx какие коэффициенты с помощью нашего на обучении мы подбираем'
  candidate_answer: time=01:07:29 text='просто вопрос их подбираем соответственно блоков центре коэффициент привет при каждом резисторе но принцу в данном случае реке x 2 типа она либо вопрос крупных . а мы придумываем себе функцию ошибки мы говорим про конкретно про это вот про машины обучения или про про линиями модель давай вот машин обучение линейная модель функций ошибки супер уже супер расскажи поподробней функция ошибки есть среди квадратичное есть есть у нас есть мои мысли это разница мы представляем что у нас есть какие-то истинных значений то что наша модель как сказала мы находим разницу между тем что на самом деле и тем что модель предсказала и это будет наша ошибка эта ошибка может в двух видах как сумма сумма квадратов разниц и сумма модулей разниц сумма модулей разниц'
  reference_answer: time=None text=None
  interviewer_feedback: time=01:07:57 text='супер уже супер расскажи поподробней'
  question_topic: ML

ITEM #24
  interviewer_question: time=01:08:40 text='почему мы считаем что квадрат дает нам'
  candidate_answer: time=01:08:44 text='параболу из параболы можно работать она непрерывный они и но в каком-то общем простом случае мы считаем что нее есть один минимум так мы можем подобрать параметры таким образом чтобы наша ошибка оказалось тупо внизу парабола есть вот с математической точки зрения с квадратом работать много проще потому что как мы ищем да потому что может найти попроще дифференцировать type 1 двоечку в snes и'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #25
  interviewer_question: time=01:09:15 text='что он происходит в мае придеться вот'
  candidate_answer: time=01:09:19 text='когда мы берем у нас константа остается мыслить и сделать не сможем типа она в нули это плохо не дифференцирует ну типо вот когда вы теперь она даже'
  reference_answer: time=None text=None
  interviewer_feedback: time=01:09:32 text='supersu так есть от всяких аки про то как обходит вот это вот как там своем работают всякие слаженные мои как они суть мы сейчас не думает говорить или'
  question_topic: ML

ITEM #26
  interviewer_question: time=01:09:46 text='вот смотри я слышу но мне кто-то говорил про то что есть такая вещь как градиентный спуск и что она мне как-то позволяет сделать подборка в цель а вот что это за фигня такая границ курск что такое градиент что такое предельный спуск как она работает это сложная фигня'
  candidate_answer: time=01:10:07 text='градиент это производная виктор градиента показывает нам мини изменения функции и прежде не спеши'
  reference_answer: time=01:10:21 text='вектор честный производство так и если подумаем я конечно до капли масла прости пожалуйста это гектор частных частные производные часть ответа вектор это часть их в целом эта вещь перчатках прыжок куда указывает людей направлении возрастания функции супер соответственно для того чтобы найти минимум надо взять integrity супер супер но все равно не'
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `01:09:47` — Вопрос о градиентном спуске ---
window: 01:09:47 .. 01:14:06
recognition_status: single (1 items)

ITEM #27
  interviewer_question: time=01:10:55 text='поля как же я с помощью градиента в этот брезент спуска ищу коэффициенты а 0 и b вас уйти своими вопрос как идиот'
  candidate_answer: time=01:11:05 text='обучение у нас есть какая-то модель мы получили по ней ошибки мы взяли нашу amos е1 у нас какая-то функция мы в какой-то точке считаем квадратная функция соответственно в какой-то точке мы находим вектор градиента и мы стремимся его свести к нулю грузит вам дает вектор клиенты пытаются 70 камеру как то нет тогда наверное мне тогда и то есть он просто он не структурирована голове у тебя учителя есть она тебя есть сто процентов просто последовательно нужна последовательность вот что что 124 имея какое-то если рисовать параболу то мы стремимся по ней спуститься вниз эту точку . градиента спустить вниз таким образом на те минимум ошибки вот'
  reference_answer: time=01:12:07 text='смотри типа на у тебя есть что у тебя есть предсказание модели и реально предсказать правильно у тебя есть ошибка у тебя есть сумма квадратов ошибок мы хотим сумму квадратов ошибок свести к нулю не к нулю как минимум прально говорит мне соответственно мы это можем сделать с помощью как раз среде в роспуск где там подвох подвох заключается в том что нам просто нужно грамотно расписать что на самом деле там наше предсказание от x она выглядит как некоторые там значения коэффициента а 0 песни которые значение коэффициента b ну давай мы возьмем там какой-то президентом б а 0 плюс b 0 плюс b 1 то допустим и у нас будет y равно как а 0 плюс b 0 и x плюс b 1 x квадратура теперь вот это предсказание нашего алгоритма есть какие-то значения а песок и теперь можешь посчитать разницу можешь посчитать значение м с и пытаться его минимизировать за счет глядим спуск но в целом в целом ну типа это так я понимаю вот и последует последовательность она такая что сделал предсказание на каких-то ну на каких-то писать код у нас есть какие-то веса до сделал предсказание посчитал ошибки посчитал сумму квадратов ошибок читал градиент обновил леса и заново по циклу так вот идём идём идём идём идём пока в какой-то момент у нас ошибка она не лениться и типа вот у нас ошибка не меняется значит мы достигли вот это вот выходе из-за'
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `01:14:06` — Вопрос о переобучении ---
window: 01:14:06 .. 01:22:20
recognition_status: multiple (6 items)

ITEM #28
  interviewer_question: time=01:14:09 text='грей называется переобучение и есть варианты работать переобучения опять таки я слышу я вообще в этом не разбираюсь но я слышу что есть понятие переобучения модели что это такое и как'
  candidate_answer: time=01:14:25 text='бороться с переобучить переобучение история когда у нас модель на на трендовых данных показывать какие то есть хорошие результаты тестовых данных она может она показывает недостаточно хороший это история когда модель подстраивается под под под нашу обучающую выборку она прекрасно отрабатывает и и она повторяет может быть в каждую точку но это не имеет отношение к жизни и на тестовых данных'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #29
  interviewer_question: time=01:14:54 text='назови мне как минимум три banyan борьбы с переобучение применительно к линейной'
  candidate_answer: time=01:15:01 text='регрессии регуляризации мы применяем а почему то линейной регрессии просто взял оскорбил много других алгоритмов regular за у у разных алгоритмов она разная не то чтобы у разных но в том числе если не на регрессе регуляризация как действует регуляризации мы добавляем по ошибке страхующий и член который тоже бывает разный функционал ошибки и он соответственно если говорить о линейной регрессии то он он будет штрафовать случае разные регуляризации он может либо обнулить там какие то какие то предикторы либо сделать их близкими к нулю но в целом он приводит тому что он избавляет от больших весов предиктор там хорошо простите сказал занулить либо при визите к нулю это сделать очень мало очень мало ли там либо занулить либо сделать очень мало думаешь так мы говорим про веса при иксах да если мы добавляем регуляризации у линейную регрессию то просто в этот момент очень мало ни много ни математически звучать дальше и суть не суть так хорошо прилягу реализацию ты сказал еще два варианта как можно бороться с нашим переобучить тут буду импровизировать наверное но линейной регрессии в частности чувствительна к multiply near настей можно до того как мы пустим признаки в регрессию можно посмотреть оценить их насколько они коррелируют между собой если есть те которые коррелируют а от них можно но если это если это возможно будет от них можно избавиться не остановило все'
  reference_answer: time=None text=None
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #30
  interviewer_question: time=01:16:51 text='когда-нибудь про всякие в лиге ционные техники когда мы делаем отдельно с и вызывая на тестовые трейдеры набора не менее когда у нас есть тестовый набор который мы не больше никогда не ти есть странный набор а есть еще в иммиграционный datasette как часть рейном умного и там через понятие консолидации но я об этом не знаю но слышал про к соблюдаются страте five'
  candidate_answer: time=01:17:16 text='слышал про к соблюдаются страте five card type сирия скро сваливается цель таком слышу кросс выдался да когда мы у нас есть datasette на которую мы учимся и и тестируемся и мы берем не просто часть вот говорим что вот это у нас будет train а этот тест мы меняем их берем разные наборы на разных наборов учимся на разных наборах тестируемся но все в рамках рамках 1 1 2 это хорошо но и то есть способ борьбы с переобучение что мы начинаем проверять просто вот шафрин каким-то образом смотрим а вот такой это вариант ой очень плохой очень плохое предсказание потом опять же очень плохой предсказать ну кажется что мы период учились когда вот давай сейчас стали что зажав ли каким-то образом посмотрим на на кросс валидации назначения наши венеции бой-то метрики на которую мы будем смотреть и понимать у нас обучилась моделью меня получится хорошо на какой-то показатель качества шел есть различные способы валидации вот кросс валидации про строки'
  reference_answer: time=None text=None
  interviewer_feedback: time=01:18:05 text='вариант ой очень плохой очень плохое предсказание потом опять же очень плохой предсказать ну кажется что мы период учились когда вот давай сейчас стали что зажав ли каким-то образом посмотрим на на кросс валидации назначения наши венеции бой-то метрики на которую мы будем смотреть и понимать у нас обучилась моделью меня получится хорошо на какой-то показатель качества шел есть различные способы валидации вот кросс валидации про строки fight к фолд слышал стратификация модификация стран тогда'
  question_topic: ML

ITEM #31
  interviewer_question: time=01:18:39 text='стратификация модификация стран тогда'
  candidate_answer: time=01:18:42 text='слышал ничего не скажу мне почему то кажется что мы хотим сделать так чтобы она встроена в этом наборе были одинаково присутствовали какие-то подгруппы у нас года да и то есть это есть супер то есть в каждой были рационом сети нас должно быть определенный набор групп и нута на основе каких-то вот стран это может быть значение как кода ну это особенно актуально для мытья класс классификации чтобы нас в каждом анимационном сети было определенное количество вот этих классов которые нас должны быть задача как задачах репрессии мы можем взять какую-то категорию переменную и просить чтобы в каждом выдвигаться на сайте было определенное количество вот этих вот'
  reference_answer: time=None text=None
  interviewer_feedback: time=01:18:56 text='есть супер то есть в каждой были рационом сети нас должно быть определенный набор групп и нута на основе каких-то вот стран это может быть значение как кода ну это особенно актуально для мытья класс классификации чтобы нас в каждом анимационном сети было определенное количество вот этих классов которые нас должны быть задача как задачах репрессии мы можем взять какую-то категорию переменную и просить чтобы в каждом выдвигаться на сайте было определенное количество вот этих вот категориальных речей от очень представители вот принадлежащих определенных категорий то есть объекта мне кажется внешне по умолчанию такие вещи которые вот без'
  question_topic: ML

ITEM #32
  interviewer_question: time=01:19:56 text='временные ряды до временные ряды и про кросс валидации временных рядах но это на самом деле используется не только в так называемых конкретных временных рядах и людей всегда он изменяется в течение времени так далее это просто вот у нас есть какая-то зависимость от времени и мы хотим это запчасти от времени тоже учит что ты даже представишься не могу мы уже считаем что у нас текущее значение какой-то переменной предсказывается по неким ближайшем условно ближайшем или по оси зоны был цикличным каким-то назад как здесь можно от вы лидера ваться нет'
  candidate_answer: time=01:20:37 text='не слышал оно стало любопытно опять-таки'
  reference_answer: time=01:20:43 text='видит выделить следующим образом у нас есть вот период времени на году вот есть полный период вот есть период временно которым мы обучаемся вот здесь мы лидируем ну вот да предсказанным смотрим на ошибку затем этот период берем здесь обучаемся на следующий предсказан и так далее кумулятивно типа увеличиваем увеличен смотрим на результат самый при помощи то есть вот вариант когда мы коли по кумулятивным увеличивались вариант когда у нас вот это вот окно а нам просто переползает дальше и типа ты переползаешь делаешь прогноз переползаешь делаешь прогноз приглашаешь'
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #33
  interviewer_question: time=01:21:25 text='про кроссовере доця подарили еще один способ борьбы с требующий о нем всегда забываю вот я могу сказать всегда забывают про вот этот способ борьбы с передачей но этот самый'
  candidate_answer: time=01:21:39 text='параметров моделью добавить данным а где же увеличить увеличить количество данных но как как'
  reference_answer: time=01:21:53 text='ну так давайте ограничивать исайя допустим или использовать регуляризации хорошо давайте использовать другие варианты играли до суда супер но самое лучшее брендовое тебя новые данные типа'
  interviewer_feedback: time=01:22:04 text='лучшее брендовое тебя новые данные типа просто новые данные добычи или посмотрели дальше по схеме типа это самый простой и самый течение не самый простой зачисляется на просто но самый эффективный способ борьбы с передачи'
  question_topic: ML

--- CHAPTER `01:22:20` — Вопрос о деревьях и их построении ---
window: 01:22:20 .. 01:26:04
recognition_status: multiple (2 items)

ITEM #34
  interviewer_question: time=01:22:24 text='строится дерево 1 делим задачку в деревьях есть узлы предикаты в которых выставляются какие-то условия по этому условию набор данных разбивается как правило на на 2 и дальше опять предикаты условиях и так дальше и так дальше заканчивается все листиками у ритика как будто бы есть ответы вот из того что могу рассказать главный вопрос для'
  candidate_answer: time=01:22:53 text='как разбивать данные у нас есть набор признаков мы берем тот признак который максимальная информативен короче дисперсия мир неопределённости данных когда все это повторяешь это мгла из и по данным по конкретному признаку мы находим меру неопределенности и выбираем тот признак по которому у нас самой маленькой неопределенность это признак мы будем считать самым интересным по этому признаку в это признаки у нас есть набор нам нужно определить в какую сторону упадем в какой момент мы пойдем направо пойдем налево при каком значении признака соответственно мы последовательно идем по каждому значению этого признака определяем а я что сказал тропе и должно быть но ты на и сторона это фильтр опечатку лишь ты почему-то дисперсии сказал дисперсии трапе и конечно энтропии энтропия но я далеко мы определяем энтропию разбиение таким образом чтобы и терапия в этих разбитых группах было мера неопределенностью этой тропе и было меньше чем чем вот в исходной группе и соответственно вот эта точка будет я понятно говорю я тебя попрошу давайте точка будет точкой разбиение мы говорим что вот мы допустить ее нашли вот в этом значении у нас энтропия развивается так что сумму вот этих энтропий меньше чем сумма общей терапии в этой точке мы разбиваемся говорим что если у нас значение этого признака там меньше меньше пяти то мы уходим в эту ветку если больше 5 уходим в эту ветку и в последующих ветках происходит тоже самое мы разбиваемся так до тех пор пока не'
  reference_answer: time=01:25:39 text='словей есть вот такая критерием пропилена он используется для того чтобы определить не только признак по которому будем делить но и точку разбиения ты все правильно вы лишь то что там суммы энтропии должна быть это все правильно единственное что но наверное так скомкано было но я могу судить что это'
  interviewer_feedback: time=None text=None
  question_topic: ML

ITEM #35
  interviewer_question: time=01:26:01 text='хорошо одно дерево поняли почему работает случайный лес объяснение почему случайно не сработает хорошо здесь ответ'
  candidate_answer: time=01:26:11 text='на это вопрос да и самая важная почему мы случайно вес считается что он не перри обучается почему мы идем к случайному лесу потому что огромные вычисления если вот пока если представить что огромное количество признаков и объектов то большие вычисления мы идем переходим к случайному лесу я очень хорошо помню что на курсы и сказали так кричали пожарского типа парадокс на случайный вествуд работы'
  reference_answer: time=01:26:38 text='вообще это неправда потому что городок сможет вы слова продукт не говорили ну как то так сказали что удивительно вот работает нет на самом деле есть жесткая давали твоя отвечу на вопросы про закончил есть очень важный постулат который стоит за случайным лесом почему случайно не сработает чего вообще там ансамбли из нескольких деревянных моделей работал потому что у нас но точнее он работает тогда когда нас вероятность предсказанием раненого класса на больше 0 5 больше случайность вот он работает случайно лишь тогда когда каждый классификатор каждая модель каждое дерево который будет построена она будет работать выше чем случайно вот в данном случае там есть математика за эти который доказывает что типа если мы лучше случайного там и в среднем будем всегда лучше случайно соответственны лучше чем просто один одесситки помимо этого есть еще подход что мы используем там беден а это значит то что наберем случайно подмножество фичей то есть наших вот регрессор декоров и случайное количество объектов и сам интересное что у нас еще может быть такое что вот в вот в этот набор свечей и объектах может попадать один и тот же объект несколько раз чисто теоретически только возможно супер то есть там нас забор с возвращения это работает хорошо работает отлично но есть следующий'
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `01:26:04` — Вопрос: почему случайный лес работает хорошо и не переобучается? ---
window: 01:26:04 .. 01:28:20
recognition_status: single (1 items)

ITEM #36
  interviewer_question: time=01:28:12 text='работает отлично но есть следующий вопрос со звездочкой и на этом мы заканчиваем вопроса звездочка в каких случаях логистическая регрессия на задачи классификации будет работать лучше чем случайные вес даже немного вводных у нас сто пятьсот параметр и несколько миллионов объект то есть данная дофига при этом логистическая регрессия работает в разы лучше чем случайно ли мы почему про качеству говорю да про качество с точки зрения точности полноты их меры рока у к'
  candidate_answer: time=01:29:01 text='только рассуждать или регрессии остается регрессией а при огромном количестве ну производства и мощность нужна какая-то безумная если мы говорим про но если мы считаем что у нас предложено мощность есть как бы это не не аргумент нет недостатков деревьев только сложность озвучивается митяй смотри я только что рассказывал про важным условием почему скучали без работы поверхность должна быть больше на 5 и на бошке чайного да а если случайно мест не работает значит что естественно каждый предиктор уже случайно или или на уровне случайно edition да ну а как такое может быть вот когда такое может быть но когда вся и терапия примерно одинаково да ну то есть шум ты просто работать шумом но но как будто были грехи и правится при этом регрессе как-то справляется почему это очень хороший вопрос на подумать вот просто вот прям цепочка цепочка с пол-очка цепочка и дальше вот она привлечься не привязывается к 0 5 потом пойдем от деревьев вот смотри задач дано чайный лес работает плохо есть логистической регрессии линейная ноготь который работает хорошо все это дону знаем каждое дерево случайного леса должно работать лучше чем 05 этого не происходит значит что то не то что то не так из-за того что есть шум в данных но мы знаем что случайный лес работать на подмножества данных и под множестве объект все значит следующий шаг какой не просто шум в данных но для него они все одинаковые не так ну типо вот смотри она же много деревьев соответственно много шумов дан очень много шумов данных при этом знаем что линейная модель каким-то образом среди всех данных что-то нашла что позволяет ей решить задачку весь в косы хорошо а случайный весь не может потому что он берет подмножество там шум не получилось берет подмножество тут шум не получилось берет опять по наш шум 05 не получилось потом берет о что-то нащупал больше чем 5 но этих деревьев мало таких хороших деревьев мало относительно общего количества потому'
  reference_answer: time=01:29:57 text='почему это очень хороший вопрос на подумать вот просто вот прям цепочка цепочка с пол-очка цепочка и дальше вот она привлечься не привязывается к 0 5 потом пойдем от деревьев вот смотри задач дано чайный лес работает плохо есть логистической регрессии линейная ноготь который работает хорошо все это дону знаем каждое дерево случайного леса должно работать лучше чем 05 этого не происходит значит что то не то что то не так из-за того что есть шум в данных но мы знаем что случайный лес работать на подмножества данных и под множестве объект все значит следующий шаг какой не просто шум в данных но для него они все одинаковые не так ну типо вот смотри она же много деревьев соответственно много шумов дан очень много шумов данных при этом знаем что линейная модель каким-то образом среди всех данных что-то нашла что позволяет ей решить задачку весь в косы хорошо а случайный весь не может потому что он берет подмножество там шум не получилось берет подмножество тут шум не получилось берет опять по наш шум 05 не получилось потом берет о что-то нащупал больше чем 5 но этих деревьев мало таких хороших деревьев мало относительно общего количества потому что там много шума соответственно соответственно таком случае я специально бурю сто пятьсот параметров миллионы объектов очень много данных случайно леса шум шух шух шух шух шух шух шух шух политической регрессе вот этот весь шум отодвинула а вот на один или там два признака ориентируется который мне зашумленным и таким образом может поделить группу на 2 это специально'
  interviewer_feedback: time=None text=None
  question_topic: ML

--- CHAPTER `01:28:20` — Последний вопрос со звездочкой: в каких случаях логистическая регрессия на задачах классификации будет работать лучше, чем случайный лес ---
window: 01:28:20 .. 01:32:18
recognition_status: not_recognized (0 items)

(no items extracted)
SAVE JSON: вставьте ответ в конец файла /Users/mm/projects/ds-final-project/data/knowledgebase/splitted/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/data-scientist-junior-karpov-2022-03-30.v14.validation-report.md в секцию «Semantic validation (step 5)» (между <!-- SEMANTIC_VALIDATION --> и <!-- /SEMANTIC_VALIDATION -->, блок ```json).

======================================================================
RUNTIME_HINTS (from step1-prepare/run_config.json)
======================================================================
Required model for step 5 — do not substitute another model without user approval.
Required model: claude-sonnet-4-6
Required temperature: 0
```

<!-- /LLM_INPUT_STEP_5 -->
