"""Interview language detection and localized validation-report strings."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Literal

InterviewLang = Literal["ru", "en"]

_CYR_RE = re.compile(r"[а-яА-ЯёЁ]")
_LAT_RE = re.compile(r"[a-zA-Z]")
_VIDEO_LANG_RE = re.compile(r"^language:\s*(\w+)", re.MULTILINE | re.IGNORECASE)


def detect_interview_language(
    transcript_text: str,
    video_md_path: Path | None = None,
) -> InterviewLang:
    """
    ru — кириллица доминирует в транскрипте (или video.md language: ru).
    en — иначе (в т.ч. language: en в frontmatter video.md).
    """
    if video_md_path and video_md_path.exists():
        m = _VIDEO_LANG_RE.search(video_md_path.read_text(encoding="utf-8"))
        if m:
            code = m.group(1).lower()[:2]
            if code in ("ru", "uk", "be"):
                return "ru"
            if code in ("en",):
                return "en"

    sample = transcript_text[:120_000]
    cyr = len(_CYR_RE.findall(sample))
    lat = len(_LAT_RE.findall(sample))
    if cyr >= 80 and cyr >= lat * 0.25:
        return "ru"
    return "en"


class _LocaleStore:
    lang: InterviewLang = "ru"

    def set(self, lang: InterviewLang) -> None:
        self.lang = lang

    def t(self, key: str, **fmt: object) -> str:
        table = _STRINGS.get(self.lang, _STRINGS["ru"])
        text = table.get(key, _STRINGS["ru"].get(key, key))
        return text.format(**fmt) if fmt else text


locale = _LocaleStore()


def activate_locale(lang: InterviewLang) -> None:
    locale.set(lang)


def load_transcript_from_folder(folder: Path) -> str:
    tc = folder / "timecodes.txt"
    tr = folder / "transcript.txt"
    if tc.exists():
        return tc.read_text(encoding="utf-8")
    if tr.exists():
        return tr.read_text(encoding="utf-8")
    return ""


def detect_language_for_folder(folder: Path) -> InterviewLang:
    return detect_interview_language(
        load_transcript_from_folder(folder),
        folder / "video.md" if (folder / "video.md").exists() else None,
    )


def step2_locale_rules(lang: InterviewLang) -> list[str]:
    if lang == "ru":
        return [
            "INTERVIEW_LANGUAGE: ru (обязательно для этого прогона)",
            "- Все поля text в JSON — дословные фрагменты из PRIMARY_TRANSCRIPT на русском. Без перевода на английский.",
            "- Запрещены пересказы («кандидат рассказал о…», «The candidate…»).",
            "- Метки question_type / question_topic / interview_stage — enum на английском (схема), тексты Q&A — только русский ASR.",
        ]
    return [
        "INTERVIEW_LANGUAGE: en (mandatory for this run)",
        "- All text fields in JSON must be verbatim contiguous spans from PRIMARY_TRANSCRIPT in English. No Russian translation.",
        "- Forbidden: summaries («The candidate explained…», «кандидат сказал…»).",
        "- Labels question_type / question_topic / interview_stage stay English enums (schema); Q/A wording stays English ASR only.",
    ]


def step5_notes_language_line(lang: InterviewLang) -> str:
    if lang == "ru":
        return "Language for notes: Russian. Keep notes short and actionable. Leave notes as \"\" when both flags are true."
    return 'Language for notes: English. Keep notes short and actionable. Leave notes as "" when both flags are true.'


# Keys used across validate_chapters / validate_video
_STRINGS: dict[InterviewLang, dict[str, str]] = {
    "ru": {
        "report_title": "# Отчёт валидации сплиттера",
        "artifacts_heading": "### Артефакты этого прогона",
        "artifact_json": "- **Разбивка Q&A (JSON):** `{path}`",
        "artifact_xlsx": "- **Разбивка Q&A (Excel):** `{path}`",
        "artifact_video": (
            "- **Эталон для проверки:** `{path}` — описание YouTube с тайм-кодами "
            "и рубриками; сплиттер при извлечении Q&A этот файл **не видел**"
        ),
        "tolerance_line": (
            "- **Порог расхождения тайм-кодов:** ±{tol} с — максимальная разница "
            "между тайм-кодом вопроса на YouTube и временем `interviewer_question.time` в JSON, "
            "при которой пара Q&A всё ещё считается относящейся к этой главе"
        ),
        "how_check_title": "## Как устроена проверка",
        "verdict_heading": "### Вердикт:",
        "pipeline_steps_note": (
            "Пайплайн — **5 шагов**. В этом файле — **проверки 1–3** (шаги 2, 4, 5). "
            "Шаги 1 и 3 только готовят данные."
        ),
        "verdict_pass": "✅ ПРОЙДЕНО",
        "verdict_fail": "❌ НЕ ПРОЙДЕНО",
        "verdict_partial": "⚠️ ЧАСТИЧНО",
        "verdict_partial_chapters": "⚠️ ЧАСТИЧНО — {n} {word} без Q&A у маркера",
        "chapter_word_1": "глава",
        "chapter_word_n": "глав",
        "check1_title": "## Проверка 1. Структура JSON (шаг 2 — выход сплиттера)",
        "check1_intro": (
            "Детерминированная проверка файла после извлечения Q&A: парсинг и JSON Schema "
            "`splitter_output_schema.json`."
        ),
        "check2_title": "## Проверка 2. Сверка с тайм-кодами YouTube (шаг 4)",
        "check3_title": "## Проверка 3. Смысл и тайм-коды полей внутри глав (шаг 5, LLM)",
        "check3_intro": (
            "Модель в Cursor (как на шаге 2) проверяет **уже извлечённые** Q&A: правдоподобны ли "
            "тайм-коды полей в окне главы и совпадают ли тексты с заголовком главы и метками "
            "(`question_topic`, `question_type`). На общий вердикт не влияет."
        ),
        "yt_table_title": "### Все главы YouTube",
        "yt_table_intro": (
            "Каждый тайм-код из `video.md`: вопросные — статус и Q&A; служебные — куда ушли в JSON. "
            "Развёрнутые тексты — ниже по вопросным главам."
        ),
        "chapter_details_title": "### Детали по вопросным главам",
        "chapter_details_intro": (
            "Развёрнутые тексты Q&A. Служебные главы — только в таблице «Все главы YouTube» выше."
        ),
        "qa_at_marker": "**Q&A у маркера главы** (±tolerance; каждый item только в одной главе)",
        "field_question": "Вопрос",
        "field_answer": "Ответ кандидата",
        "field_reference": "Эталон интервьюера",
        "field_feedback": "Комментарий интервьюера",
        "field_labels": "Метки",
        "reference_empty": "—",
        "speaker_mix_title": "## Проверка границ реплик (эвристика)",
        "speaker_mix_intro": (
            "Автоматическая проверка ролей (без diarization): дубли Q/A, обрывки вопроса, "
            "фразы кандидата в поле вопроса, реплики интервьюера внутри ответа."
        ),
        "gaps_title": "## Фрагменты транскрипта без Q&A в JSON",
        "gaps_intro": (
            "Интервалы `timecodes.txt`, не попавшие в span ни одного item сплиттера. "
            "Проверьте, не пропущен ли вопрос или это служебная речь."
        ),
        "gaps_none": "_Крупных непокрытых фрагментов не найдено (порог: ≥25 с, ≥4 строк с тайм-кодом)._",
        "semantic_heading": "## Semantic validation (step 5)",
        "semantic_machine": "Машинный ответ LLM (шаг 5). Валидатор читает этот блок при повторном прогоне.",
        "step5_pipeline_title": "## Шаг 5 — семантическая валидация (LLM)",
        "status_recognized_one": "распознан (1 Q&A)",
        "status_recognized_many": "распознано ({n} Q&A)",
        "status_nearby": "рядом",
        "status_missing": "не распознан",
        "col_question_start": "Начало вопроса",
        "table_item": "Item",
        "json_schema_ok": "JSON Schema OK",
        "json_schema_fail": "ошибки структуры / схемы",
        "items_count": "{n} items",
        "llm_step_pending": "шаг 5 не выполнен",
        "llm_all_ok": "все {n} глав без замечаний",
        "interview_language_line": "**Язык интервью:** `{lang}` — отчёт и заметки шага 5 на этом языке; тексты Q/A в JSON — дословно из транскрипта.",
    },
    "en": {
        "report_title": "# Splitter validation report",
        "artifacts_heading": "### Run artifacts",
        "artifact_json": "- **Q&A split (JSON):** `{path}`",
        "artifact_xlsx": "- **Q&A split (Excel):** `{path}`",
        "artifact_video": (
            "- **Validation reference:** `{path}` — YouTube chapters and sections; "
            "the splitter did **not** see this file during Q&A extraction"
        ),
        "tolerance_line": (
            "- **Timestamp tolerance:** ±{tol}s — max drift between a YouTube chapter marker "
            "and `interviewer_question.time` in JSON while still attributing the Q&A pair to that chapter"
        ),
        "how_check_title": "## How validation works",
        "verdict_heading": "### Verdict:",
        "pipeline_steps_note": (
            "Pipeline has **5 steps**. This file covers **checks 1–3** (steps 2, 4, 5). "
            "Steps 1 and 3 only prepare data."
        ),
        "verdict_pass": "✅ PASSED",
        "verdict_fail": "❌ FAILED",
        "verdict_partial": "⚠️ PARTIAL",
        "verdict_partial_chapters": "⚠️ PARTIAL — {n} chapter(s) without Q&A at marker",
        # word unused in en template
        "chapter_word_1": "chapter",
        "chapter_word_n": "chapters",
        "check1_title": "## Check 1. JSON structure (step 2 — splitter output)",
        "check1_intro": (
            "Deterministic check after Q&A extraction: parse + JSON Schema "
            "`splitter_output_schema.json`."
        ),
        "check2_title": "## Check 2. YouTube chapter alignment (step 4)",
        "check3_title": "## Check 3. Semantic field alignment per chapter (step 5, LLM)",
        "check3_intro": (
            "The Cursor agent (same as step 2) reviews **extracted** Q&A: field timestamps vs chapter "
            "windows and whether texts match chapter titles and labels (`question_topic`, `question_type`). "
            "Does not change the overall verdict."
        ),
        "yt_table_title": "### All YouTube chapters",
        "yt_table_intro": (
            "Every timestamp from `video.md`: question chapters — status and Q&A; "
            "service chapters — where speech landed in JSON. Full texts below per question chapter."
        ),
        "chapter_details_title": "### Question chapter details",
        "chapter_details_intro": (
            "Full Q&A texts. Service chapters appear only in the table above."
        ),
        "qa_at_marker": "**Q&A at chapter marker** (±tolerance; each item in one chapter only)",
        "field_question": "Question",
        "field_answer": "Candidate answer",
        "field_reference": "Reference answer",
        "field_feedback": "Interviewer feedback",
        "field_labels": "Labels",
        "reference_empty": "—",
        "speaker_mix_title": "## Speaker boundary check (heuristic)",
        "speaker_mix_intro": (
            "Automatic role check (no diarization): Q/A duplicates, truncated questions, "
            "candidate speech in question field, interviewer lines inside answer."
        ),
        "gaps_title": "## Transcript spans without Q&A in JSON",
        "gaps_intro": (
            "Intervals in `timecodes.txt` not covered by any item span. "
            "Check for a missed question or service speech."
        ),
        "gaps_none": "_No large uncovered spans (threshold: ≥25s, ≥4 timecoded lines)._",
        "semantic_heading": "## Semantic validation (step 5)",
        "semantic_machine": "LLM machine response (step 5). The validator reads this block on re-run.",
        "step5_pipeline_title": "## Step 5 — semantic chapter validation (LLM)",
        "status_recognized_one": "recognized (1 Q&A)",
        "status_recognized_many": "recognized ({n} Q&A)",
        "status_nearby": "nearby",
        "status_missing": "not recognized",
        "col_question_start": "Question start",
        "table_item": "Item",
        "json_schema_ok": "JSON Schema OK",
        "json_schema_fail": "schema / structure errors",
        "items_count": "{n} items",
        "llm_step_pending": "step 5 not run",
        "llm_all_ok": "all {n} chapters OK",
        "interview_language_line": "**Interview language:** `{lang}` — report and step-5 notes in this language; Q/A JSON text verbatim from transcript.",
    },
}
