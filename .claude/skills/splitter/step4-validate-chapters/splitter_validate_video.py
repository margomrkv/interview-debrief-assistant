"""
splitter_validate_video.py

Cross-validates a splitter JSON output against the YouTube video.md file
(chapters list). video.md is used ONLY for validation — it must not be
present in the splitter run context.

Usage:
    python3 .claude/skills/splitter/step4-validate-chapters/splitter_validate_video.py \
        --splitter data/knowledgebase/splitted/.../basename.vN.qa-split.json \
        --video data/knowledgebase/raw/.../video.md \
        [--section-config .claude/skills/splitter/step4-validate-chapters/section_topic_map.example.json] \
        [--out data/knowledgebase/splitted/.../basename.vN.validation-report.md] \
        [--prepare-llm]

--section-config (optional) JSON file with keys:
  {
    "section_timecodes": {"Section Name": "HH:MM:SS", ...},
    "topic_map": {"Section Name": ["Topic1", "Topic2"], ...}
  }
If omitted, section assignment and topic-consistency check are skipped;
only coverage (did the splitter find every question chapter?) is reported.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

SKILL_DIR = Path(__file__).resolve().parent.parent
STEP1_DIR = SKILL_DIR / "step1-prepare"

if str(STEP1_DIR) not in sys.path:
    sys.path.insert(0, str(STEP1_DIR))
from interview_locale import (  # noqa: E402
    activate_locale,
    detect_language_for_folder,
    locale as loc,
)


# ─── Section → accepted question_topic values ────────────────────────────────
# Loaded from --section-config at runtime; defaults to empty (topic check skipped).
# Optional --section-config JSON: see step4-validate-chapters/section_topic_map.example.json.

_DEFAULT_SECTION_TOPIC_MAP: dict[str, list[str]] = {}
_DEFAULT_SECTION_TIMECODES: dict[str, str] = {}

# Prefixes/keywords that mark an explanation or transition chapter, not a question
EXPLANATION_PREFIXES = (
    # ── Russian: generic ───────────────────────────────────────────────────────
    "Введение",
    "О структуре",
    "Объяснение",
    "Разбор",
    # «Подводка к» — не здесь: это отдельный тип главы (🔗), см. LEAD_IN_PREFIXES в splitter_validate_chapters.py
    "Интерпретация",
    "Конец",
    "Конец,",
    "Какие еще",
    "Общие рассуждения",
    # ── Russian: interview framing ─────────────────────────────────────────────
    "Начало",
    "Приветствие",
    "Представление",
    "Завершение",
    "Комментирование",
    "Зачем задаем",
    "Фидбек",
    "Обратная связь",
    "Вопросы к",            # "Вопросы к Валерию Бабушкину" — блок вопросов от кандидата
                "Подводим",         # "Подводим итоги и делаем выводы" — резюмирование, не вопрос
                "Итоги",            # "Итоги собеседования"
                "Интро",            # "Интро" — русский вариант видео-интро
    "Вступление",       # "Вступление и знакомство"
    "Как обычно проходят",  # "Как обычно проходят собеседования" — мета-объяснение формата
    "Problem Specifics:",   # "Problem Specifics: Beginning of the Answer" — начало ответа, не вопрос
    "Returning to",         # "Returning to the general structure" — переход к следующей теме
    "Подход к вопросу",     # "Подход к вопросу от Валерия" — разбор интервьюера, не вопрос
    "Возврат к",            # "Возврат к отбору баннеров" / "Возврат к вопросу переобучения" — продолжение
    "Возвращаемся к",       # "Возвращаемся к вопросу, какую модель оставить" — продолжение обсуждения
    "Ответ",                # "Ответ" — кандидат начинает отвечать, не новый вопрос
    "Постановка",           # "Постановка задачи" — постановка, не вопрос
    "Резюме",               # "Резюме первой итерации" — промежуточное резюме, не вопрос
    "Что такое ML Design",  # мета-объяснение формата, не вопрос
    "Первый комментарий",   # "N-й комментарий" = панельные комментарии, не вопросы
    "Второй комментарий",
    "Третий комментарий",
    "Четвертый комментарий",
    "Четвёртый комментарий",
    "Пятый комментарий",
    "Шестой комментарий",
    "Седьмой комментарий",
    "Фидбек от",            # "Фидбек от всех" — разбор панели
    "Тема интервью",        # "Тема интервью" — постановка задачи, не вопрос
    "Формат собеседования", # "Формат собеседования" — мета-объяснение, не вопрос
    "Воспоминания",         # "Воспоминания" — биографический рассказ, не вопрос
    "Обобщение ответа",     # "Обобщение ответа" — кандидат резюмирует, не новый вопрос
    "Обоснования выбора",   # "Обоснования выбора и описание модели" — продолжение ответа
    "Определение",          # "Определение LTV, уточнение условий задачи" — уточнение задачи, не вопрос
    "Знакомство",           # "Знакомство с кандидатом" — интро-секция, не вопрос
    "ОС от",                # "ОС от Валерия" — обратная связь интервьюера, не вопрос
    "Возможность \u201c",  # "Возможность "завалить"..." — финальная мета-секция, не вопрос
    "Структура собеседования",  # "Структура собеседования" — объяснение формата
    "О структуре собеседования",
    "Не прощаемся",  # rzv_de финал / обратная связь на Boosty
    "Формат, бусти",  # rzv_de интро
    "Про новый формат",  # rzv_de S2 интро
    "Что нового будет",  # rzv_de S2 интро
    "Что нужно знать",  # "Что нужно знать для дата аналитика" — мета-секция, не вопрос
    "ОФФЕР",            # "ОФФЕР ПОД КЛЮЧ" — реклама, не вопрос
    "Легенда для",      # "Легенда для собеса" — контекст интервью, не вопрос
    "Это БАЗА",         # "Это БАЗА" — мета-оценка, не вопрос
    "Accuracy",         # sub-метрика классификации (разбор), не отдельный вопрос
    "Precision и Recall", # sub-метрика классификации (разбор)
    "F1 Score",         # sub-метрика классификации (разбор)
    "ROC-AUC",          # sub-метрика классификации (разбор)
    "Полезный канал",   # "Полезный канал по мат. статистике" — реклама/анонс
    "Итог собеседования", # "Итог собеседования" — вывод, не вопрос
    "Как можно быстрее", # "Как можно быстрее получить оффер" — реклама курса
    "Так ли хорош",     # "Так ли хорош Data Science?" — мета-комментарий автора, не вопрос
    "Финал",            # "Финал" — завершение видео, не вопрос
    "Заключение",       # "Заключение" — outro/ending, не вопрос
    "UNICODE",          # "UNICODE" — анонс сообщества «UniCode» Новосёлова, не вопрос
    "ЧЗХ",              # "ЧЗХ???" — мата-комментарий Новосёлова, не вопрос
    "КОНЕЦ",            # "КОНЕЦ" — завершение видео (верхний регистр)
    "Задачи на теорвер", # "Задачи на теорвер" — пропущены Новосёловым в записи
    "Функция Лагранжа", # "Функция Лагранжа" — вопрос показан на экране, не проговорён вслух
    "Решение ",         # "Решение второй задачи" — разбор решения, не отдельный вопрос
    "Советы",           # "Советы" — советы зрителям после интервью, не вопрос
    "Опыт и проекты",   # "Опыт и проекты Димы" — вступительная биография кандидата, пропускается
    "Шаг ",             # "Шаг 1: Постановка задачи" и т.д. — структурные метки system design, не вопросы
    "Мои Соц.",         # "Мои Соц. Сети" — реклама соцсетей Новосёлова, не вопрос
    "Как мы будем",     # "Как мы будем действовать" — переход/продолжение, не отдельный вопрос
    # ── samokat-ml-2026-02-25 ───────────────────────────────────────────────────
    "Формат интервью",  # "Формат интервью и как проходит технический этап" — мета-интро
    "Реальные продовые",  # "Реальные продовые задачи NLP-команды" — контекст, не вопрос
    "Контент, модерация",  # "Контент, модерация, SEO и генерация" — контекст команды
    "Главные боли",     # "Главные боли продакшена" — контекст, не вопрос
    "Кого ищут",        # "Кого ищут в Самокат?" — контекст, не вопрос
    "Какой у меня",     # "Какой у меня опыт?" — самопрезентация автора, не вопрос
    "Гайд по трудоустройству",  # реклама курса/гайда, не вопрос
    "Как получить оффер",  # "Как получить оффер от 200к" — реклама, не вопрос
    "Как выйти",        # "Как выйти на O(n)" — редакционная подсказка, не вопрос
    "Правильная идея",  # "Правильная идея через два прохода" — редакционный комментарий
    "Проверка решения", # "Проверка решения и тесты" — разбор, не отдельный вопрос
    "Ключевая идея",    # "Ключевая идея через словарь соседей" — редакционный комментарий
    "Как найти крайние",  # "Как найти крайние элементы" — редакционная подсказка
    "Понимание задачи как", # "Понимание задачи как графа" — редакционный комментарий
    "Финальная логика", # "Финальная логика обхода" — редакционный комментарий
    "Почему O(",        # "Почему O(n log n) — это уровень сильного кандидата" — комментарий
    "Логи, ClickHouse,",  # "Логи, ClickHouse, Elastic — как устроена аналитика" — описание стека Станислава, не вопрос к кандидату
    "ML-мониторинг:",   # "ML-мониторинг: drift, Evidently, распределения" — монолог Станислава о планах, не вопрос к кандидату
    "Технические шоколадки",  # rzv_de — обсуждение без отдельного Q&A у маркера
    "Вступление эфира",  # dataengineers-pro / Tinkoff Connect
    "Вопросы интервьюеру",  # финальный блок вопросов кандидата, не Q&A у маркера
    # ── Russian: case/scenario setup (not a question itself) ───────────────────
    "Кейс ",      # "Кейс про соцсети" etc.
    "Кейс:",
    "Постановка",
    "Условие задачи",
    "Перерыв",
    "Подведение итогов",
    "Переход",          # "Переход ко второй части интервью"
    # ── English: stream/interview framing ─────────────────────────────────────
    "Intro",
    "Introduction",
    "<Untitled",  # YouTube placeholder chapter titles
    "Product-sense solution",  # DataInterview debrief segment, not a new question
    "SQL solution",
    "Solution + Feedback",
    "Assessment",  # post-interview assessment / debrief
    "Explanation",  # Jay Feng / IQ debrief segments
    "Interview Feedback",
    "Jeff's Explanation",
    "Clarifying Questions",
    "Ved whiteboarding",
    "Interviewer feedback",
    "Advice on",
    "Interview strategy",
    "Final takeaways",
    "Did they pass",
    "Staff-level solution",
    "Meta-specific offer",
    "Why this would not pass",
    "What the candidate did well",
    "Break",          # "Break Before the Second Candidate"
    "Summary",        # "Summary" / "Summary and feedback"
    "Wrap",           # "Wrap-up"
    "How interviews", # "How interviews typically work"
    "How the interview",
    "About the interview",
    "Feedback",
    # ── English: case/scenario setup (preamble, not a standalone question) ─────
    "A case study",   # "A case study on social media"
    "Case study",
    "Setting up",     # "Setting up the problem..."
    "Background:",
    "Context:",
)


# ─── Data structures ──────────────────────────────────────────────────────────

@dataclass
class Chapter:
    time_sec: int
    time_str: str
    title: str
    section: Optional[str] = None
    is_question: bool = False


@dataclass
class SplitterItem:
    index: int          # 1-based
    q_time_str: Optional[str]
    q_time_sec: Optional[int]
    question_topic: Optional[str]
    question_type: Optional[str]
    interview_stage: Optional[str]
    q_text_preview: str
    a_text_preview: str
    short_answer: bool = False


@dataclass
class MatchResult:
    chapter: Chapter
    item: Optional[SplitterItem] = None
    drift_sec: Optional[int] = None
    topic_ok: Optional[bool] = None
    topic_allowed: Optional[list] = None   # list of accepted topic values for this section
    topic_actual: Optional[str] = None


# ─── Parsers ──────────────────────────────────────────────────────────────────

def _ts_to_sec(ts: str) -> int:
    """Convert HH:MM:SS or MM:SS to total seconds."""
    parts = ts.strip().split(":")
    parts = [int(p) for p in parts]
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    return int(parts[0])


def _sec_to_ts(sec: int) -> str:
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def _normalize_ts_hms(ts: str) -> str:
    """Normalize MM:SS or H:MM:SS to HH:MM:SS for section boundaries."""
    ts = ts.strip().strip("[]")
    parts = [int(p) for p in ts.split(":")]
    if len(parts) == 2:
        return f"00:{parts[0]:02d}:{parts[1]:02d}"
    if len(parts) == 3:
        return f"{parts[0]:02d}:{parts[1]:02d}:{parts[2]:02d}"
    raise ValueError(f"bad timestamp: {ts}")


# topic_map for Karpov mock section names (when auto-parsed from video.md Description)
KARPOV_MOCK_TOPIC_MAP: dict[str, list[str]] = {
    "Python": ["Python"],
    "A/B-тесты": ["Experimentation", "Statistics"],
    "Работа с данными": ["SQL", "Python"],
    "ML алгоритмы": ["ML"],
}


def parse_section_timecodes_from_description(text: str) -> dict[str, str]:
    """Parse `Секция «Name»` blocks under ## Description; first timestamp in block = section start."""
    desc_match = re.search(r"## Description\n(.*)", text, re.DOTALL | re.IGNORECASE)
    if not desc_match:
        return {}
    desc = desc_match.group(1)
    sections: dict[str, str] = {}
    for m in re.finditer(r"Секция\s*[«\"]([^»\"]+)[»\"]", desc, re.IGNORECASE):
        sec_name = m.group(1).strip()
        chunk = desc[m.end() :]
        next_m = re.search(r"Секция\s*[«\"]", chunk, re.IGNORECASE)
        if next_m:
            chunk = chunk[: next_m.start()]
        ts_m = re.search(
            r"(?:\[)?(\d{1,2}:\d{2}(?::\d{2})?)(?:\])?",
            chunk,
        )
        if ts_m:
            sections[sec_name] = _normalize_ts_hms(ts_m.group(1))
    return sections


def _preview(text: str, limit: int = 100) -> str:
    t = (text or "").replace("\n", " ").strip()
    if len(t) <= limit:
        return t
    return t[: limit - 1] + "…"


def read_time_offset_seconds(video_md_text: str) -> int:
    """Read <!-- time_offset_seconds: N --> from video.md comments. Returns 0 if absent."""
    m = re.search(r"<!--\s*time_offset_seconds:\s*(\d+)", video_md_text)
    return int(m.group(1)) if m else 0


def parse_video_md(
    path: Path,
    section_timecodes: dict[str, str] | None = None,
) -> list[Chapter]:
    """Parse chapters from video.md, assign sections, classify questions.

    section_timecodes: mapping of section name → "HH:MM:SS" string.
    If None or empty, section assignment is skipped (all chapters get section=None).
    """
    text = path.read_text(encoding="utf-8")

    # Extract the ## Chapters block (stop at ## Description or end)
    chapters_block_match = re.search(r"## Chapters\n(.*?)(?:\n## |\Z)", text, re.DOTALL)
    if not chapters_block_match:
        raise ValueError(f"No '## Chapters' section found in {path}")

    chapters_block = chapters_block_match.group(1)

    # Build sorted section boundaries (sec_name → start_seconds)
    resolved_timecodes: dict[str, int] = {}
    for sec_name, ts_str in (section_timecodes or {}).items():
        resolved_timecodes[sec_name] = _ts_to_sec(ts_str)
    sorted_sections = sorted(resolved_timecodes.items(), key=lambda x: x[1])

    chapters: list[Chapter] = []
    pattern = re.compile(r"-\s+\[(\d{1,2}:\d{2}(?::\d{2})?)\]\s+(.+)")
    for line in chapters_block.splitlines():
        m = pattern.match(line.strip())
        if not m:
            continue
        ts, title = m.group(1), m.group(2).strip()
        sec = _ts_to_sec(ts)

        # Assign section
        section = None
        for sec_name, sec_start in reversed(sorted_sections):
            if sec >= sec_start:
                section = sec_name
                break

        # Classify as question vs. explanation
        is_question = not any(title.startswith(p) for p in EXPLANATION_PREFIXES)

        chapters.append(Chapter(
            time_sec=sec,
            time_str=ts,
            title=title,
            section=section,
            is_question=is_question,
        ))

    return chapters


def parse_splitter_json(path: Path) -> tuple[list[SplitterItem], list[dict]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    items: list[SplitterItem] = []
    raw_items: list[dict] = []
    for i, it in enumerate(data.get("items", []), start=1):
        raw_items.append(it)
        q = it.get("interviewer_question") or {}
        a = it.get("candidate_answer") or {}
        q_time = q.get("time")
        q_raw = q.get("text") or ""
        a_raw = a.get("text") or ""
        a_words = len(a_raw.split()) if a_raw else 0
        items.append(SplitterItem(
            index=i,
            q_time_str=q_time,
            q_time_sec=_ts_to_sec(q_time) if q_time else None,
            question_topic=it.get("question_topic"),
            question_type=it.get("question_type"),
            interview_stage=it.get("interview_stage"),
            q_text_preview=_preview(q_raw, 100),
            a_text_preview=_preview(a_raw, 80),
            short_answer=bool(a_raw) and a_words > 0 and a_words <= 4,
        ))
    return items, raw_items


# ─── Matching ─────────────────────────────────────────────────────────────────

def match_chapters_to_items(
    chapters: list[Chapter],
    items: list[SplitterItem],
    tolerance_sec: int,
    section_topic_map: dict[str, list[str]] | None = None,
) -> list[MatchResult]:
    """
    For each question chapter, find the closest splitter item within tolerance.
    Each item can be matched to at most one chapter.

    Uses a global drift-sorted greedy strategy: consider all (chapter, item) pairs
    within tolerance, sort by drift ascending, then assign closest pairs first.
    This avoids the sequential greedy problem where an earlier chapter "steals" an
    item that would be a perfect match for a later chapter.

    section_topic_map: mapping of section name → allowed question_topic values.
    If None or empty, topic consistency check is skipped for all items.
    """
    topic_map = section_topic_map or {}
    question_chapters = [c for c in chapters if c.is_question]

    # Build all candidate pairs within tolerance, sorted by drift ascending
    candidates: list[tuple[int, Chapter, SplitterItem]] = []  # (drift, chapter, item)
    for ch in question_chapters:
        for item in items:
            if item.q_time_sec is None:
                continue
            drift = abs(item.q_time_sec - ch.time_sec)
            if drift <= tolerance_sec:
                candidates.append((drift, ch, item))
    candidates.sort(key=lambda x: x[0])

    # Greedy assignment: smallest drift first
    assigned_chapters: set[int] = set()  # chapter.time_sec used as key
    used_item_indices: set[int] = set()
    assignments: dict[int, tuple[SplitterItem, int]] = {}  # chapter.time_sec → (item, drift)

    for drift, ch, item in candidates:
        if ch.time_sec in assigned_chapters:
            continue
        if item.index in used_item_indices:
            continue
        assigned_chapters.add(ch.time_sec)
        used_item_indices.add(item.index)
        assignments[ch.time_sec] = (item, drift)

    # Build MatchResult list in chapter order
    results: list[MatchResult] = []
    for ch in question_chapters:
        result = MatchResult(chapter=ch)
        if ch.time_sec in assignments:
            best_item, best_drift = assignments[ch.time_sec]
            result.item = best_item
            result.drift_sec = best_drift

            # Topic check: pass if actual topic is in the allowed list for this section
            allowed_topics = topic_map.get(ch.section) if ch.section else None
            actual_topic = best_item.question_topic
            result.topic_allowed = allowed_topics
            result.topic_actual = actual_topic
            if allowed_topics is not None:
                result.topic_ok = (actual_topic in allowed_topics)

        results.append(result)

    return results


def find_unmatched_items(
    items: list[SplitterItem],
    match_results: list[MatchResult],
) -> list[SplitterItem]:
    matched_indices = {r.item.index for r in match_results if r.item is not None}
    return [it for it in items if it.index not in matched_indices]


def build_section_breakdown(
    match_results: list[MatchResult],
    unmatched_items: list[SplitterItem],
    all_chapters: list[Chapter],
) -> list[dict]:
    """
    For each section, compute:
      - video_q_count: number of question chapters in that section (from video.md)
      - splitter_count: number of matched splitter items + unmatched items whose time
        falls within that section's range
      - topics: set of question_topic values found in the splitter items
      - missing_chapters: question chapters with no matched item
    """
    # Section time boundaries derived from all chapters (sorted)
    section_starts = sorted(
        {c.section: c.time_sec for c in all_chapters if c.section}.items(),
        key=lambda x: x[1],
    )
    # Build ordered list of (section, start_sec, end_sec)
    section_ranges: list[tuple[str, int, int]] = []
    for i, (sec_name, start) in enumerate(section_starts):
        end = section_starts[i + 1][1] if i + 1 < len(section_starts) else 999999
        section_ranges.append((sec_name, start, end))

    def sec_for_time(t: int) -> str | None:
        for sec_name, start, end in reversed(section_ranges):
            if t >= start:
                return sec_name
        return None

    # Count question chapters per section
    section_video_q: dict[str, list[Chapter]] = {s: [] for s, _, _ in section_ranges}
    for ch in all_chapters:
        if ch.is_question and ch.section:
            section_video_q.setdefault(ch.section, []).append(ch)

    # Matched splitter items per section
    section_matched: dict[str, list[SplitterItem]] = {s: [] for s, _, _ in section_ranges}
    section_missing: dict[str, list[Chapter]] = {s: [] for s, _, _ in section_ranges}
    for r in match_results:
        sec = r.chapter.section
        if not sec:
            continue
        if r.item:
            section_matched.setdefault(sec, []).append(r.item)
        else:
            section_missing.setdefault(sec, []).append(r.chapter)

    # Unmatched splitter items — assign to section by time
    section_unmatched_extra: dict[str, list[SplitterItem]] = {s: [] for s, _, _ in section_ranges}
    for it in unmatched_items:
        if it.q_time_sec is not None:
            sec = sec_for_time(it.q_time_sec)
            if sec:
                section_unmatched_extra.setdefault(sec, []).append(it)

    rows = []
    for sec_name, _, _ in section_ranges:
        video_qs = section_video_q.get(sec_name, [])
        matched = section_matched.get(sec_name, [])
        extra = section_unmatched_extra.get(sec_name, [])
        missing = section_missing.get(sec_name, [])
        all_splitter = matched + extra
        topics = sorted({it.question_topic for it in all_splitter if it.question_topic})
        rows.append({
            "section": sec_name,
            "video_q_count": len(video_qs),
            "splitter_count": len(all_splitter),
            "delta": len(all_splitter) - len(video_qs),
            "topics": topics,
            "missing_chapters": missing,
        })
    return rows


# ─── Commentary helpers ───────────────────────────────────────────────────────

def _build_commentary(
    match_results: list["MatchResult"],
    unmatched_items: list["SplitterItem"],
    non_q_chapters: list["Chapter"],
    coverage_pct: float,
    topic_pct: float,
    topic_checks: list["MatchResult"],
    tolerance_sec: int,
    *,
    window_not_recognized: int = 0,
) -> list[str]:
    """
    Produce an analytical plain-language commentary section.

    Logic:
    - Assess coverage and flag whether misses are likely false positives
      (case setups / preambles absorbed into the next question) or genuine misses.
    - Note skipped non-question chapters and explain why.
    - Highlight topic mismatches.
    - Give a concrete recommendation.
    """
    lines: list[str] = []

    total_q = len(match_results)
    missed_results = [r for r in match_results if r.item is None]
    matched_results = [r for r in match_results if r.item is not None]

    # ── Покрытие (окна глав) ─────────────────────────────────────────────────
    if window_not_recognized > 0:
        lines.append(
            f"**{window_not_recognized} вопросных глав без item в ±{tolerance_sec} с** (❌ не распознан). "
            f"Coverage: **{coverage_pct:.0f}%**. "
            "См. сводную таблицу и фрагменты транскрипта без Q&A."
        )
    elif coverage_pct == 100:
        lines.append(
            f"**Покрытие по окнам глав — 100%.** Все {total_q} вопросных глав содержат ≥1 item "
            "в временном окне [тайм-код главы … следующая глава)."
        )
    elif coverage_pct >= 90:
        lines.append(
            f"**Покрытие высокое ({coverage_pct:.0f}%** — {len(missed_results)} тайм-код"
            f"{'а' if len(missed_results) == 1 else 'а' if len(missed_results) < 5 else 'ов'} "
            f"из {total_q} не покрыт{'о' if len(missed_results) == 1 else 'о' if len(missed_results) < 5 else 'о'}). "
            "Хороший результат. Пропуски ниже, скорее всего, ложные срабатывания валидатора "
            "(постановки кейсов, переходные тайм-коды) — не реальные пропуски сплиттера. "
            "Проверьте вручную перед повторным запуском."
        )
    elif coverage_pct >= 70:
        lines.append(
            f"**Покрытие среднее ({coverage_pct:.0f}%** — {len(missed_results)} из {total_q} "
            "тайм-кодов не покрыто). Часть вопросов пропущена. Проверьте непокрытые тайм-коды "
            "и транскрипт в указанных временных отметках перед повторным запуском сплиттера."
        )
    else:
        lines.append(
            f"**Покрытие низкое ({coverage_pct:.0f}%** — {len(missed_results)} из {total_q} "
            "тайм-кодов не покрыто). Серьёзный провал сплиттера. Пересмотрите промпты и перезапустите."
        )
    lines.append("")

    # ── Исключённые главы ─────────────────────────────────────────────────────
    if non_q_chapters:
        lines.append(
            f"**{len(non_q_chapters)} тайм-код{'а' if len(non_q_chapters) < 5 else 'ов'} исключено из чеклиста** "
            "как вводные, переходные или постановочные (не самостоятельные вопросы интервью):"
        )
        for c in non_q_chapters:
            lines.append(f"- `{c.time_str}` *{c.title}*")
        lines.append(
            "\nЭти тайм-коды не засчитываются как пропуски. Если какой-то из них нужно считать "
            "вопросом — удалите его префикс из `EXPLANATION_PREFIXES` в валидаторе."
        )
        lines.append("")

    # ── Анализ пропущенных глав ───────────────────────────────────────────────
    if missed_results:
        lines.append(f"**Анализ {len(missed_results)} непокрытых тайм-кодов:**\n")
        for r in missed_results:
            ch = r.chapter
            # Find nearest matched item by absolute time distance
            nearest_item: Optional["SplitterItem"] = None
            nearest_drift = float("inf")
            for mr in matched_results:
                if mr.item and mr.item.q_time_sec is not None:
                    d = abs(mr.item.q_time_sec - ch.time_sec)
                    if d < nearest_drift:
                        nearest_drift = d
                        nearest_item = mr.item

            if nearest_item and nearest_drift <= tolerance_sec:
                lines.append(
                    f"- `{ch.time_str}` **{ch.title}** — ближайший item #{nearest_item.index} "
                    f"в `{nearest_item.q_time_str}` ({int(nearest_drift)} сек) находится "
                    f"в пределах ±{tolerance_sec}с, но **уже сопоставлен с другим тайм-кодом**. "
                    "Обычно это означает, что два тайм-кода видео описывают один и тот же вопрос: "
                    "одна — постановку задачи, другая — сам вопрос. Сплиттер правильно захватил "
                    "один item, который был присвоен тайм-коду с меньшим Δt. "
                    "**Что делать:** добавьте префикс заголовка этого тайм-кода в `EXPLANATION_PREFIXES` "
                    "(вероятно, это постановочный/переходный тайм-код, а не самостоятельный вопрос)."
                )
            elif nearest_item and nearest_drift <= 120:
                lines.append(
                    f"- `{ch.time_str}` **{ch.title}** — ближайший найденный item "
                    f"#{nearest_item.index} в `{nearest_item.q_time_str}` "
                    f"({int(nearest_drift)} сек — за пределами окна ±{tolerance_sec}с). "
                    "Скорее всего, это **постановка кейса / вводный сегмент** — авторы видео "
                    "поставили тайм-код на начало темы, а фактический вопрос прозвучал позже. "
                    "Сплиттер вопрос нашёл правильно; ограничение на стороне валидатора. "
                    "**Что делать:** добавьте префикс этого тайм-кода в `EXPLANATION_PREFIXES`, "
                    "или используйте `--tolerance` > 120с для интервью с длинными вводными."
                )
            elif nearest_item and nearest_drift <= tolerance_sec * 2:
                lines.append(
                    f"- `{ch.time_str}` **{ch.title}** — ближайший item "
                    f"#{nearest_item.index} в `{nearest_item.q_time_str}` "
                    f"({int(nearest_drift)} сек). Пограничный случай: чуть за пределами допуска. "
                    "Проверьте, правильно ли сплиттер проставил тайм-код, или вопрос был "
                    "слит со следующим."
                )
            else:
                lines.append(
                    f"- `{ch.time_str}` **{ch.title}** — **близкого item нет** "
                    f"(ближайший на расстоянии {int(nearest_drift)} сек). "
                    "Это **реальный пропуск**: сплиттер не извлёк ни одного вопроса "
                    "из этого фрагмента транскрипта. Откройте транскрипт в указанном тайм-коде "
                    "и проверьте: был ли вопрос задан, или тайм-код — комментарий / объяснение?"
                )
        lines.append("")

    # ── Лишние items сплиттера ────────────────────────────────────────────────
    if unmatched_items:
        lines.append(
            f"**{len(unmatched_items)} item{'а' if len(unmatched_items) < 5 else 'ов'} сплиттера без тайм-кода в описании видео.** "
            "Это ожидаемо: авторы видео маркировали только крупные тематические сегменты, "
            "а не каждый уточняющий вопрос. Скорее всего, это правомерные дополнительные "
            "вопросы, которые сплиттер верно захватил за пределами чеклиста."
        )
        lines.append("")

    # ── Несоответствия тем ────────────────────────────────────────────────────
    topic_fails = [r for r in topic_checks if not r.topic_ok]
    if topic_fails:
        lines.append(
            f"**{len(topic_fails)} несоответстви{'е' if len(topic_fails) == 1 else 'я' if len(topic_fails) < 5 else 'й'} тем:** "
            "метка `question_topic` в JSON сплиттера не совпадает с ожидаемыми темами секции. "
            "Либо модель поставила неверную метку, либо нужно обновить секционную карту:"
        )
        for r in topic_fails:
            allowed_str = " / ".join(f"`{t}`" for t in (r.topic_allowed or []))
            lines.append(
                f"- `{r.chapter.time_str}` **{r.chapter.title}** "
                f"→ получено `{r.topic_actual}`, ожидалось {allowed_str}"
            )
        lines.append("")
    elif topic_checks and topic_pct == 100:
        lines.append(
            f"**Разметка тем согласована (100%).** Все {len(topic_checks)} сопоставленных "
            "item'а имеют `question_topic`, совпадающий с ожидаемой секцией."
        )
        lines.append("")

    # ── Итоговая рекомендация ─────────────────────────────────────────────────
    lines.append("**Рекомендация:**")
    if window_not_recognized > 0:
        lines.append(
            f"Есть {window_not_recognized} глав(ы) без Q&A в окне YouTube — см. ❌ в разделе "
            "«Главы YouTube» и цитаты транскрипта. Перезапустите шаг 2 (новая версия json) "
            "или уточните `EXPLANATION_PREFIXES` / главы video.md."
        )
    elif coverage_pct == 100 and (not topic_checks or topic_pct == 100):
        lines.append("Действий не требуется — вывод полностью совпадает с эталоном.")
    elif coverage_pct >= 90 and not missed_results:
        lines.append("Результат хороший. Повторный запуск не нужен.")
    elif coverage_pct >= 90 and missed_results:
        # Check if all misses are likely false positives (nearby items within 2× tolerance)
        all_fp = all(
            any(
                mr.item and mr.item.q_time_sec is not None
                and abs(mr.item.q_time_sec - r.chapter.time_sec) <= 120
                for mr in matched_results
            )
            for r in missed_results
        )
        if all_fp:
            lines.append(
                "Все непокрытые тайм-коды выглядят как постановочные сегменты, а не реальные "
                "пропуски сплиттера. Повторный запуск не нужен. Рекомендуется добавить "
                "их префиксы в `EXPLANATION_PREFIXES`, чтобы они автоматически исключались."
            )
        else:
            lines.append(
                "Большинство тайм-кодов покрыто. Проверьте непокрытые тайм-коды выше: "
                "определите, какие из них — реальные пропуски, а какие — ложные срабатывания "
                "валидатора, прежде чем решать о повторном запуске."
            )
    else:
        lines.append(
            "Перезапустите сплиттер с обновлёнными промптами. Сосредоточьтесь "
            "на временных отметках непокрытых тайм-кодов, указанных выше."
        )

    return lines


# ─── Report ───────────────────────────────────────────────────────────────────

def build_report(
    match_results: list[MatchResult],
    unmatched_items: list[SplitterItem],
    all_chapters: list[Chapter],
    section_rows: list[dict],
    splitter_path: Path,
    video_path: Path,
    tolerance_sec: int,
    section_topic_map: dict[str, list[str]] | None = None,
    validation_body: dict[str, list[str]] | None = None,
    gaps_section_lines: list[str] | None = None,
    coverage_stats: dict[str, int | float] | None = None,
    json_contract_lines: list[str] | None = None,
    metrics_howto_lines: list[str] | None = None,
    items_count: int | None = None,
    *,
    json_contract_ok: bool = True,
    check3_lines: list[str] | None = None,
    llm_verdicts: dict | None = None,
    pipeline_run_summary_lines: list[str] | None = None,
) -> str:
    lines: list[str] = []

    total_q_chapters = len(match_results)
    tolerance_matched = sum(1 for r in match_results if r.item is not None)
    topic_checks = [r for r in match_results if r.topic_ok is not None]
    topic_ok_count = sum(1 for r in topic_checks if r.topic_ok)
    drifts = [r.drift_sec for r in match_results if r.drift_sec is not None]
    avg_drift = sum(drifts) / len(drifts) if drifts else None
    max_drift = max(drifts) if drifts else None
    tolerance_pct = tolerance_matched / total_q_chapters * 100 if total_q_chapters else 0
    topic_pct = topic_ok_count / len(topic_checks) * 100 if topic_checks else 100

    if coverage_stats:
        matched = int(coverage_stats["recognized"])
        window_not_rec = int(coverage_stats["not_recognized"])
        window_total = int(coverage_stats["total"])
        coverage_pct = float(coverage_stats["pct"])
    else:
        matched = tolerance_matched
        window_not_rec = total_q_chapters - tolerance_matched
        window_total = total_q_chapters
        coverage_pct = tolerance_pct

    excel_path = splitter_path.with_suffix(".xlsx")
    topic_map = section_topic_map or {}

    lines.append(loc.t("report_title") + "\n")
    lines.append("")
    lines.append(loc.t("interview_language_line", lang=loc.lang) + "\n")
    lines.append("")
    if pipeline_run_summary_lines:
        lines.extend(pipeline_run_summary_lines)
    lines.append(loc.t("artifacts_heading") + "\n")
    lines.append(loc.t("artifact_json", path=splitter_path))
    if excel_path.exists():
        lines.append(loc.t("artifact_xlsx", path=excel_path))
    lines.append(loc.t("artifact_video", path=video_path))
    lines.append(loc.t("tolerance_line", tol=tolerance_sec))
    lines.append("")

    # Verdict
    if window_not_rec > 0:
        if coverage_pct >= 70 and topic_pct >= 70:
            word = (
                loc.t("chapter_word_1")
                if window_not_rec == 1
                else loc.t("chapter_word_n")
            )
            verdict = loc.t(
                "verdict_partial_chapters", n=window_not_rec, word=word
            )
        else:
            verdict = loc.t("verdict_fail")
    elif coverage_pct >= 90 and topic_pct >= 90 and json_contract_ok:
        verdict = loc.t("verdict_pass")
    elif coverage_pct >= 70 and topic_pct >= 70 and json_contract_ok:
        verdict = loc.t("verdict_partial")
    else:
        verdict = loc.t("verdict_fail")

    topic_consistency_value = (
        f"{topic_ok_count}/{len(topic_checks)} ({topic_pct:.0f}%)"
        if topic_checks else ("N/A" if loc.lang == "en" else "Н/Д")
    )
    json_status = "✅" if json_contract_ok else "❌"
    json_result = (
        loc.t("items_count", n=items_count or 0) + ", " + loc.t("json_schema_ok")
        if json_contract_ok
        else loc.t("json_schema_fail")
    )
    yt_status = (
        "✅"
        if coverage_pct >= 90 and topic_pct >= 90 and window_not_rec == 0
        else ("⚠️" if coverage_pct >= 70 and topic_pct >= 70 else "❌")
    )
    yt_result = (
        f"Coverage {coverage_pct:.0f}% ({matched}/{window_total}), "
        f"Topic consistency {topic_pct:.0f}%"
        if topic_checks
        else f"Coverage {coverage_pct:.0f}% ({matched}/{window_total}), Topic consistency Н/Д"
    )
    llm_status = "⏳"
    llm_result = loc.t("llm_step_pending")
    if llm_verdicts:
        n = len(llm_verdicts)
        both = sum(
            1 for v in llm_verdicts.values()
            if v.time_alignment_ok and v.content_alignment_ok
        )
        if both == n:
            llm_status = "✅"
            llm_result = loc.t("llm_all_ok", n=n)
        elif both >= n * 0.7:
            llm_status = "⚠️"
            llm_result = (
                f"{both}/{n} chapters OK"
                if loc.lang == "en"
                else f"{both}/{n} глав без замечаний"
            )
        else:
            llm_status = "❌"
            llm_result = (
                f"{both}/{n} chapters OK"
                if loc.lang == "en"
                else f"{both}/{n} глав ок"
            )

    from splitter_validate_chapters import build_unified_pipeline_checks_table

    lines.extend(
        build_unified_pipeline_checks_table(
            verdict=verdict,
            json_status=json_status,
            json_result=json_result,
            yt_status=yt_status,
            yt_result=yt_result,
            yt_goal="Coverage ≥90%, Topic consistency ≥90%",
            llm_status=llm_status,
            llm_result=llm_result,
            has_video_rubrics=bool(topic_map),
        )
    )
    lines.append("---\n")

    if json_contract_lines:
        lines.extend(json_contract_lines)
        lines.append("")

    lines.append("---\n")
    lines.append(loc.t("check2_title") + "\n")
    lines.append("")

    from splitter_validate_chapters import build_check2_glossary

    lines.extend(build_check2_glossary())

    if metrics_howto_lines:
        lines.extend(metrics_howto_lines)

    if validation_body:
        for key in (
            "youtube_intro",
            "section_audit",
            "index",
            "unrecognized",
            "chapter_details",
            "speaker_mix",
        ):
            section = validation_body.get(key) or []
            if section:
                lines.extend(section)
        lines.append("")

    if check3_lines:
        lines.extend(check3_lines)
        lines.append("")

    if gaps_section_lines:
        lines.extend(gaps_section_lines)
        lines.append("")

    items_all, _ = parse_splitter_json(splitter_path)
    short_items = [it for it in items_all if it.short_answer]
    if short_items:
        lines.append("#### Короткие ответы кандидата (≤4 слов)\n")
        lines.append(
            "Проверьте по транскрипту: это **осмысленный** короткий ответ на вопрос, "
            "а не обрезанный span или пропуск речи кандидата.\n"
        )
        lines.append("| Item | Время | Ответ |")
        lines.append("|------|-------|-------|")
        for it in short_items:
            lines.append(f"| #{it.index} | {it.q_time_str or '—'} | {it.a_text_preview} |")
        lines.append("")

    return "\n".join(lines) + "\n"


# ─── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Validate splitter JSON output against YouTube video.md chapters."
    )
    parser.add_argument("--splitter", required=True, help="Path to splitter output JSON")
    parser.add_argument("--video", required=True, help="Path to video.md")
    parser.add_argument(
        "--tolerance", type=int, default=90,
        help="Max allowed timing drift in seconds for a match (default: 90)"
    )
    parser.add_argument(
        "--section-config",
        help=(
            "Optional JSON: coarse sections + allowed question_topic values per section. "
            "Keys: 'section_timecodes' (name→HH:MM:SS) and 'topic_map' (name→[topics]); "
            "top-level keys starting with '_' are ignored (documentation). "
            "See step4-validate-chapters/section_topic_map.example.json. If omitted, section/topic checks are skipped."
        ),
    )
    parser.add_argument("--out", help="Write report to this .md file (default: print to stdout)")
    parser.add_argument(
        "--time-from", default=None,
        help="Filter video chapters: only include chapters at or after this timestamp (HH:MM:SS)"
    )
    parser.add_argument(
        "--time-to", default=None,
        help="Filter video chapters: only include chapters before or at this timestamp (HH:MM:SS)"
    )
    parser.add_argument(
        "--prepare-llm",
        action="store_true",
        help="Append LLM validation appendix to the same *.validation.vN.md (step 5 input)",
    )
    parser.add_argument(
        "--llm-json",
        default=None,
        help="Path to LLM validation JSON to merge into the report",
    )
    args = parser.parse_args()

    splitter_path = Path(args.splitter)
    video_path = Path(args.video)
    activate_locale(detect_language_for_folder(video_path.parent))

    if not splitter_path.exists():
        print(f"ERROR: splitter file not found: {splitter_path}", file=sys.stderr)
        sys.exit(1)
    if not video_path.exists():
        print(f"ERROR: video.md not found: {video_path}", file=sys.stderr)
        sys.exit(1)

    # Load optional section config; merge with auto-parse from video.md Description
    section_timecodes: dict[str, str] = {}
    section_topic_map: dict[str, list[str]] = {}
    if args.section_config:
        cfg_path = Path(args.section_config)
        if not cfg_path.exists():
            print(f"ERROR: section-config not found: {cfg_path}", file=sys.stderr)
            sys.exit(1)
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))

        def _strip_meta_keys(d: object) -> dict:
            if not isinstance(d, dict):
                return {}
            return {k: v for k, v in d.items() if isinstance(k, str) and not str(k).startswith("_")}

        section_timecodes = _strip_meta_keys(cfg.get("section_timecodes") or {})
        section_topic_map = _strip_meta_keys(cfg.get("topic_map") or {})

    video_text = video_path.read_text(encoding="utf-8")
    auto_sections = parse_section_timecodes_from_description(video_text)
    if auto_sections:
        for name, ts in auto_sections.items():
            section_timecodes.setdefault(name, ts)
        print(
            f"Sections from video.md Description: {', '.join(sorted(auto_sections))}",
            file=sys.stderr,
        )
    if section_timecodes and not section_topic_map:
        section_topic_map = {
            k: KARPOV_MOCK_TOPIC_MAP[k]
            for k in section_timecodes
            if k in KARPOV_MOCK_TOPIC_MAP
        }

    chapters = parse_video_md(video_path, section_timecodes=section_timecodes or None)

    # Apply time_offset_seconds from video.md (multi-candidate clips with relative timecodes).
    # chapter.time_str keeps absolute value for display; time_sec is shifted to match item times.
    time_offset = read_time_offset_seconds(video_text)
    if time_offset:
        import dataclasses
        chapters = [dataclasses.replace(c, time_sec=c.time_sec - time_offset) for c in chapters]
        print(f"time_offset_seconds={time_offset} applied to chapter times", file=sys.stderr)

    # Apply time range filter if requested
    if args.time_from or args.time_to:
        tf = _ts_to_sec(args.time_from) if args.time_from else 0
        tt = _ts_to_sec(args.time_to) if args.time_to else 10**9
        chapters = [c for c in chapters if tf <= c.time_sec <= tt]
    items, raw_items = parse_splitter_json(splitter_path)
    from splitter_validate_chapters import (
        assign_items_to_primary_chapters,
        build_chapter_blocks,
        build_chapter_coverage_states,
        build_check3_semantic_section,
        build_json_contract_section,
        build_match_results_from_states,
        build_metrics_howto,
        build_validation_body,
        build_transcript_gaps_section,
        coverage_stats_from_states,
        find_transcript_gaps,
        group_items_by_question_chapter,
        load_llm_verdicts,
        load_semantic_json_from_report,
        load_timecoded_transcript,
        llm_json_sidecar_path,
        prepare_step5_llm_in_pipeline_log,
        save_semantic_json_to_report,
        validate_json_contract,
        SEMANTIC_HEADING,
    )

    question_chapters = [c for c in chapters if c.is_question]
    item_primary = assign_items_to_primary_chapters(
        question_chapters, items, args.tolerance
    )
    states = build_chapter_coverage_states(
        chapters, items, args.tolerance, item_primary
    )
    assignments = group_items_by_question_chapter(
        question_chapters, items, args.tolerance
    )
    coverage_stats = coverage_stats_from_states(states)
    match_results = build_match_results_from_states(
        states, items, section_topic_map
    )
    unmatched_items = [it for it in items if it.index not in item_primary]
    section_rows = build_section_breakdown(match_results, unmatched_items, chapters)
    transcript_lines = load_timecoded_transcript(video_path.parent)

    q_bounds = None
    if question_chapters:
        q_bounds = (question_chapters[0].time_sec, question_chapters[-1].time_sec)
    gaps = find_transcript_gaps(
        transcript_lines, raw_items, bounds=q_bounds
    )

    llm_json_path = Path(args.llm_json) if args.llm_json else None
    if args.out and llm_json_path is None:
        llm_json_path = llm_json_sidecar_path(Path(args.out))
    llm_verdicts = load_llm_verdicts(llm_json_path)

    schema_path = SKILL_DIR / "step1-prepare" / "splitter_output_schema.json"
    json_ok, json_issues, json_summary = validate_json_contract(splitter_path, schema_path)
    json_contract_lines = build_json_contract_section(
        splitter_path,
        schema_path,
        ok=json_ok,
        issues=json_issues,
        summary=json_summary,
    )
    metrics_howto_lines = build_metrics_howto(args.tolerance, section_topic_map)
    check3_lines = build_check3_semantic_section(llm_verdicts)

    validation_body = build_validation_body(
        chapters,
        items,
        raw_items,
        states,
        assignments,
        args.tolerance,
        section_topic_map=section_topic_map,
        transcript_lines=transcript_lines,
        llm_verdicts=llm_verdicts,
    )
    gaps_lines = build_transcript_gaps_section(gaps)

    pipeline_run_summary_lines: list[str] = []
    try:
        skill_dir = Path(__file__).resolve().parents[1]
        if str(skill_dir) not in sys.path:
            sys.path.insert(0, str(skill_dir))
        from artifact_paths import pipeline_log_md_from_json  # noqa: WPS433
        from run_manifest import build_pipeline_run_summary_for_report, load_run  # noqa: WPS433

        pl_md = pipeline_log_md_from_json(splitter_path)
        if pl_md.exists():
            run_manifest = load_run(pl_md)
            pipeline_run_summary_lines = build_pipeline_run_summary_for_report(
                run_manifest, pl_md
            )
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        pipeline_run_summary_lines = [
            "## Прогон пайплайна\n",
            f"_Журнал не найден или без `PIPELINE_MANIFEST`: {exc}. "
            "Запустите `splitter_prepare_prompt.py` для этого интервью._\n",
            "",
        ]

    report = build_report(
        match_results, unmatched_items, chapters, section_rows,
        splitter_path, video_path, args.tolerance,
        section_topic_map=section_topic_map,
        validation_body=validation_body,
        gaps_section_lines=gaps_lines,
        coverage_stats=coverage_stats,
        json_contract_lines=json_contract_lines,
        metrics_howto_lines=metrics_howto_lines,
        items_count=len(items),
        json_contract_ok=json_ok,
        check3_lines=check3_lines,
        llm_verdicts=llm_verdicts,
        pipeline_run_summary_lines=pipeline_run_summary_lines or None,
    )

    if args.out:
        out_path = Path(args.out)
        semantic_preserved = load_semantic_json_from_report(out_path)
        out_path.write_text(report, encoding="utf-8")
        if semantic_preserved:
            save_semantic_json_to_report(out_path, semantic_preserved)
        if args.prepare_llm:
            skill_dir = Path(__file__).resolve().parents[1]
            if str(skill_dir) not in sys.path:
                sys.path.insert(0, str(skill_dir))
            from artifact_paths import pipeline_log_md_from_json  # noqa: WPS433

            pl_md = pipeline_log_md_from_json(splitter_path)
            blocks = build_chapter_blocks(chapters, items, raw_items)
            prepare_step5_llm_in_pipeline_log(
                blocks, video_path, out_path, pl_md
            )
            if pl_md.exists():
                from run_manifest import load_run, record_llm_input, save_run  # noqa: WPS433

                cfg_path = SKILL_DIR / "step1-prepare" / "run_config.json"
                val_model = None
                if cfg_path.exists():
                    val_cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
                    vi = val_cfg.get("validation_inference") or val_cfg.get("inference") or {}
                    val_model = vi.get("model")
                try:
                    run = load_run(pl_md)
                    record_llm_input(
                        run,
                        step=5,
                        name="semantic_validation",
                        model=val_model,
                        log_md=pl_md,
                    )
                    save_run(run, pl_md)
                except (FileNotFoundError, ValueError):
                    pass
            print(f"Step 5 LLM input: {pl_md}")
            print(f"Save semantic JSON: end of {out_path} ({SEMANTIC_HEADING})")
        print(f"Report written to: {out_path}")
    else:
        print(report)

    if args.prepare_llm and not args.out:
        print("ERROR: --prepare-llm requires --out", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
