"""Chapter-centric validation report and LLM validation bundle."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SKILL_DIR = Path(__file__).resolve().parent.parent
STEP4_DIR = Path(__file__).resolve().parent
PROMPT_DIR = SKILL_DIR / "step5-validate-llm"

import sys

if str(SKILL_DIR) not in sys.path:
    sys.path.insert(0, str(SKILL_DIR))
from interview_locale import locale as loc  # noqa: E402


@dataclass
class ChapterBlock:
    chapter: Any
    window_end_str: str
    window_end_sec: int  # exclusive upper bound for transcript excerpt
    items: list[Any]
    raw_items: list[dict]
    recognition: str  # skipped | not_recognized | single | multiple


_TIME_LINE = re.compile(r"^\[(\d{2}):(\d{2}):(\d{2})\]\s*(.*)$")


def _ts_to_sec(ts: str) -> int:
    parts = [int(p) for p in ts.strip().split(":")]
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    return int(parts[0])


def _sec_to_ts(sec: int) -> str:
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def load_timecoded_transcript(interview_folder: Path) -> list[tuple[int, str]]:
    """Parse timecodes.txt (preferred) into (seconds, text) pairs."""
    path = interview_folder / "timecodes.txt"
    if not path.exists():
        return []
    out: list[tuple[int, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = _TIME_LINE.match(line.strip())
        if not m:
            continue
        sec = _ts_to_sec(f"{m.group(1)}:{m.group(2)}:{m.group(3)}")
        out.append((sec, m.group(4).strip()))
    return out


def transcript_excerpt(
    lines: list[tuple[int, str]],
    start_sec: int,
    end_sec: int,
    *,
    max_chars: int = 2000,
) -> str:
    """Verbatim transcript lines in [start_sec, end_sec)."""
    if not lines:
        return "_(нет `timecodes.txt` — цитату транскрипта показать нельзя)_"
    parts: list[str] = []
    for sec, text in lines:
        if start_sec <= sec < end_sec:
            parts.append(f"[{_sec_to_ts(sec)}] {text}")
    if not parts:
        return "_(в интервале главы нет строк с тайм-кодами в `timecodes.txt`)_"
    body = "\n".join(parts)
    if len(body) > max_chars:
        return body[:max_chars] + "\n\n… _(обрезано, см. `timecodes.txt`)_"
    return body


LEAD_IN_PREFIXES = ("Подводка к", "подводка к")

# YouTube chapters that are interviewer explanations of a prior task (not standalone Q&A).
EXPLANATION_TITLE_PREFIXES = ("Объяснение", "Разбор")

TRACE_FIELDS = ("reference_answer", "interviewer_feedback", "interviewer_question", "candidate_answer")

# Heuristic markers for missed-chapter classification (Russian mock interviews).
_CANDIDATE_TURN_MARKERS = (
    "я читала",
    "я думаю",
    "наверное",
    "давайте я",
    "нет не пользовался",
    "не слышал",
    "не знаю",
    "у меня",
    "я бы ",
    "я могу",
)
_INTERVIEWER_SELF_ANSWER_MARKERS = (
    "на самом деле",
    "соответственно",
    "честный рандом",
    "мы будем пробовать",
    "вариант ответа",
    "здесь нужно сказать",
    "правильный вариант",
    "на будущее",
)

# Heuristic: interviewer phrases inside candidate_answer (ASR / splitter speaker bleed).
_INTERVIEWER_PHRASES_IN_ANSWER = (
    "давайте я приведу",
    "давай я приведу",
    "я понял",
    "окей хорошо",
    "ну я тогда",
    "с твоего позволения",
    "не буду распространяться",
    "переходите к следующей",
    "следующей секции",
    "следующей теме",
)
_CANDIDATE_PHRASES_IN_ANSWER = (
    "я читала",
    "я читал",
    "не пользовался",
    "не пользовалась",
    "на практике",
    "не слышал",
    "не знаю",
)

# Candidate-first phrasing misplaced into interviewer_question (behavioral ASR).
_CANDIDATE_MARKERS_IN_QUESTION = (
    "я знаю что",
    "я просто лично",
    "какой-то как будто классический вопрос",
    "у нас команда",
    "мы собрали",
    "я считаю что",
    "я бы сказал",
)

# Interviewer pivot phrases inside candidate_answer (question echoed or not cut).
_INTERVIEWER_PIVOT_IN_ANSWER = (
    "как ты команду",
    "получается ты можешь",
    "следующий вопрос",
    "а второй вопрос",
    "тогда такой вопрос",
    "но теперь ты руководитель",
)

_TRUNCATED_QUESTION_ENDINGS = (
    " не что",
    " не",
    " должен быть",
    " еще не",
    " уже были",
    " справа будем",
    " манифест",
)


def is_lead_in_title(title: str) -> bool:
    t = title.strip()
    return any(t.startswith(p) for p in LEAD_IN_PREFIXES)


def is_explanation_title(title: str) -> bool:
    t = title.strip()
    return any(t.startswith(p) for p in EXPLANATION_TITLE_PREFIXES)


def _field_time_sec(field: dict | None) -> int | None:
    if not field or not field.get("time"):
        return None
    return _ts_to_sec(str(field["time"]))


def _sorted_chapters(all_chapters: list[Any]) -> list[Any]:
    return sorted(all_chapters, key=lambda c: c.time_sec)


def _is_countable_question(ch: Any) -> bool:
    return ch.is_question and not is_lead_in_title(ch.title)


def find_next_question_chapter(ch: Any, all_chapters: list[Any]) -> Any | None:
    for c in _sorted_chapters(all_chapters):
        if c.time_sec > ch.time_sec and _is_countable_question(c):
            return c
    return None


def find_prev_question_chapter(ch: Any, all_chapters: list[Any]) -> Any | None:
    prev = None
    for c in _sorted_chapters(all_chapters):
        if c.time_sec >= ch.time_sec:
            break
        if _is_countable_question(c):
            prev = c
    return prev


def find_items_with_field_in_window(
    raw_items: list[dict],
    start_sec: int,
    end_sec: int,
    field_names: tuple[str, ...] = TRACE_FIELDS,
) -> list[tuple[int, str, str]]:
    """(1-based item index, field name, HH:MM:SS) for fields whose time falls in [start, end)."""
    hits: list[tuple[int, str, str]] = []
    for idx, raw in enumerate(raw_items, start=1):
        for field in field_names:
            f = raw.get(field) or {}
            if not f.get("text"):
                continue
            t_sec = _field_time_sec(f)
            if t_sec is not None and start_sec <= t_sec < end_sec:
                hits.append((idx, field, str(f.get("time"))))
    hits.sort(key=lambda x: (_ts_to_sec(x[2]), x[0]))
    return hits


def format_json_trace(links: list[tuple[int, str, str]], *, empty: str = "—") -> str:
    if not links:
        return empty
    parts = [f"#{i} `{field}` (`{t}`)" for i, field, t in links]
    return " → ".join(parts)


def trace_explanation_placement(
    ch: Any,
    all_chapters: list[Any],
    raw_items: list[dict],
) -> tuple[str, list[str]]:
    """Where explanation-chapter speech landed in splitter JSON."""
    end_sec = _chapter_end_sec(ch, all_chapters)
    in_window = find_items_with_field_in_window(
        raw_items,
        ch.time_sec,
        end_sec,
        ("reference_answer", "interviewer_feedback"),
    )
    detail: list[str] = []
    if in_window:
        summary = format_json_trace(in_window)
        detail.append(
            "- **Куда в JSON:** " + summary
            + " — речь интервьюера на интервале «разбора» попала в sidecar-поля item."
        )
        return summary, detail

    prev = find_prev_question_chapter(ch, all_chapters)
    if prev:
        prev_end = _chapter_end_sec(prev, all_chapters)
        spill = find_items_with_field_in_window(
            raw_items,
            max(ch.time_sec - 30, prev.time_sec),
            min(end_sec + 30, prev_end + 180),
            ("reference_answer", "interviewer_feedback"),
        )
        if spill:
            summary = format_json_trace(spill)
            detail.append(
                f"- **Куда в JSON:** {summary} "
                f"(рядом с задачей `{prev.time_str}` — {prev.title[:50]}…)"
            )
            detail.append(
                "- **Проверка:** тайм-код `reference_answer` / `interviewer_feedback` "
                "должен попадать в интервал этой главы YouTube."
            )
            return summary, detail

    detail.append(
        "- **Куда в JSON:** _не найдено_ — в item нет `reference_answer` / "
        "`interviewer_feedback` с тайм-кодом в интервале главы; проверьте вручную."
    )
    return "не найдено", detail


def trace_lead_in_placement(
    ch: Any,
    all_chapters: list[Any],
    items: list[Any],
    raw_items: list[dict],
    assignments: dict[int, list[int]],
) -> tuple[str, list[str]]:
    """Where lead-in chapter text should appear in JSON."""
    next_ch = find_next_question_chapter(ch, all_chapters)
    detail: list[str] = []
    if not next_ch:
        return "—", ["- **Куда в JSON:** _следующая вопросная глава не найдена_"]

    indices = assignments.get(next_ch.time_sec, [])
    end_sec = _chapter_end_sec(ch, all_chapters)
    if not indices:
        for it in items:
            if it.q_time_sec is not None and ch.time_sec <= it.q_time_sec < end_sec:
                indices.append(it.index)
        indices = sorted(set(indices))

    detail.append(
        f"- **Следующая глава YouTube:** `{next_ch.time_str}` — {next_ch.title}"
    )
    if indices:
        first = indices[0]
        raw = raw_items[first - 1]
        q = (raw.get("interviewer_question") or {}).get("text") or ""
        q_preview = (q[:120] + "…") if len(q) > 120 else q
        items_s = ", ".join(f"#{i}" for i in indices)
        summary = f"→ {items_s} `interviewer_question`"
        detail.append(f"- **Куда в JSON:** {summary}")
        detail.append(
            f"- **Ожидание:** текст подводки — в начале `interviewer_question` item #{first}."
        )
        if q_preview:
            detail.append(f"- **Начало вопроса в JSON:** «{q_preview}»")
        return summary, detail

    prev_ch = find_prev_question_chapter(ch, all_chapters)
    if prev_ch and assignments.get(prev_ch.time_sec):
        prev_indices = assignments[prev_ch.time_sec]
        last_idx = prev_indices[-1]
        raw = raw_items[last_idx - 1]
        q = (raw.get("interviewer_question") or {}).get("text") or ""
        q_preview = (q[:100] + "…") if len(q) > 100 else q
        summary = f"→ #{last_idx} `interviewer_question` (пред. глава)"
        detail.append(
            f"- **Куда в JSON:** {summary} — следующая глава `{next_ch.time_str}` "
            "без item; подводка, вероятно, в конце/начале вопроса предыдущей темы."
        )
        detail.append(
            f"- **Предыдущая глава:** `{prev_ch.time_str}` — {prev_ch.title}"
        )
        if q_preview:
            detail.append(f"- **Вопрос item #{last_idx}:** «{q_preview}»")
        return summary, detail

    detail.append(
        "- **Куда в JSON:** _items не найдены_ — подводка должна быть в "
        f"`interviewer_question` главы `{next_ch.time_str}`, но Q&A ещё не извлечён."
    )
    return "→ ? (нет items)", detail


def classify_missed_chapter(
    ch: Any,
    all_chapters: list[Any],
    transcript_lines: list[tuple[int, str]],
    assignments: dict[int, list[int]],
    items: list[Any],
    tolerance_sec: int,
) -> tuple[str, list[str]]:
    """Why a question chapter has no item in ±tolerance; what to do."""
    end_sec = _chapter_end_sec(ch, all_chapters, default_tail_sec=tolerance_sec * 2)
    lines_in_window = [(s, t) for s, t in transcript_lines if ch.time_sec <= s < end_sec]
    blob = " ".join(t.lower() for _, t in lines_in_window)

    cand_hits = sum(1 for m in _CANDIDATE_TURN_MARKERS if m in blob)
    iv_hits = sum(1 for m in _INTERVIEWER_SELF_ANSWER_MARKERS if m in blob)

    if iv_hits >= 2 and cand_hits <= 1:
        summary = "интервьюер сам ответил"
        return summary, [
            "- **Гипотеза:** интервьюер задал вопрос и сразу дал развёрнутый ответ "
            "(turn кандидата нет или минимален).",
            "- **Что нужно в JSON:** отдельный item — `interviewer_question` (вопрос), "
            "`candidate_answer`: `{\"text\": null, \"time\": null}`, "
            "ответ интервьюера в `reference_answer`.",
            "- **Проверка:** см. транскрипт ниже; если паттерн совпадает — не «пропуск», "
            "а неверный тип item.",
        ]

    # Item whose question time is very close to this chapter marker (not merely same tolerance bucket).
    near_items: list[tuple[int, int]] = []
    for it in items:
        if it.q_time_sec is None:
            continue
        drift = it.q_time_sec - ch.time_sec
        if abs(drift) <= min(45, tolerance_sec // 2):
            near_items.append((it.index, drift))
    if near_items:
        parts = ", ".join(f"#{idx} (Δt={d:+d} с)" for idx, d in near_items[:3])
        return "рядом по времени", [
            f"- **Гипотеза:** item уже есть рядом с маркером главы: {parts}.",
            "- **Проверка:** сравните смысл `interviewer_question` с заголовком YouTube.",
        ]

    if "?" in blob or "как " in blob or "что " in blob:
        summary = "пропуск сплиттера"
        return summary, [
            "- **Гипотеза:** в транскрипте есть вопрос, но сплиттер не создал item.",
            "- **Действие:** перезапуск шага 2 (новая версия json) или ручное добавление item.",
        ]

    return "неясно", [
        "- **Гипотеза:** не удалось классифицировать автоматически.",
        "- **Действие:** просмотрите транскрипт; при необходимости — `EXPLANATION_PREFIXES` "
        "или правка `video.md`.",
    ]


def json_trace_for_chapter(
    ch: Any,
    all_chapters: list[Any],
    items: list[Any],
    raw_items: list[dict],
    assignments: dict[int, list[int]],
    item_indices: list[int],
    *,
    is_lead_in: bool,
    tolerance_sec: int,
    transcript_lines: list[tuple[int, str]] | None,
) -> str:
    """One-line «куда в JSON» for the index table."""
    if is_lead_in:
        summary, _ = trace_lead_in_placement(ch, all_chapters, items, raw_items, assignments)
        return summary.replace("|", "/")[:52]
    if not ch.is_question:
        if is_explanation_title(ch.title):
            summary, _ = trace_explanation_placement(ch, all_chapters, raw_items)
            return summary.replace("|", "/")[:52]
        return "—"
    if item_indices:
        return ", ".join(f"#{i}" for i in item_indices)
    if transcript_lines:
        summary, _ = classify_missed_chapter(
            ch, all_chapters, transcript_lines, assignments, items, tolerance_sec
        )
        return f"❌ {summary}"[:52]
    return "❌ нет item"


@dataclass
class NearbyItemRef:
    """Q&A в допуске от маркера этой главы, но привязан к другой главе YouTube."""

    item_index: int
    primary_chapter_time: int
    primary_chapter_label: str
    drift_to_marker_sec: int


@dataclass
class ChapterCoverageState:
    """Состояние одной главы YouTube после сопоставления с Q&A."""

    chapter: Any
    primary_indices: list[int]
    window_indices: list[int]
    nearby_elsewhere: list[NearbyItemRef]
    status: str  # recognized | nearby | missing | lead_in | skip


def chapter_window_item_indices(
    chapter_start_sec: int,
    chapter_end_sec: int,
    items: list[Any],
) -> list[int]:
    """Все items, чей вопрос попадает в полуинтервал [маркер главы, следующая глава)."""
    return sorted(
        it.index
        for it in items
        if it.q_time_sec is not None
        and chapter_start_sec <= it.q_time_sec < chapter_end_sec
    )


def _countable_question_chapters(chapters: list[Any]) -> list[Any]:
    return [
        ch
        for ch in chapters
        if ch.is_question and not is_lead_in_title(ch.title)
    ]


def assign_items_to_primary_chapters(
    question_chapters: list[Any],
    items: list[Any],
    tolerance_sec: int,
) -> dict[int, int]:
    """
    Каждый item → не более одной вопросной главы: ближайший маркер в ±tolerance.
    Возвращает {item_index: chapter.time_sec}.
    """
    countable = _countable_question_chapters(question_chapters)
    out: dict[int, int] = {}
    for it in items:
        if it.q_time_sec is None:
            continue
        best_ch: Any | None = None
        best_drift = tolerance_sec + 1
        for ch in countable:
            drift = abs(it.q_time_sec - ch.time_sec)
            if drift <= tolerance_sec and drift < best_drift:
                best_drift = drift
                best_ch = ch
        if best_ch is not None:
            out[it.index] = best_ch.time_sec
    return out


def build_chapter_coverage_states(
    all_chapters: list[Any],
    items: list[Any],
    tolerance_sec: int,
    item_primary: dict[int, int],
) -> dict[int, ChapterCoverageState]:
    """По каждой главе YouTube — свои Q&A и соседние, привязанные к другим маркерам."""
    ch_by_key = {ch.time_sec: ch for ch in all_chapters}
    ordered = sorted(all_chapters, key=lambda c: c.time_sec)
    end_by_ch: dict[int, int] = {
        ch.time_sec: (
            ordered[i + 1].time_sec if i + 1 < len(ordered) else 10**9
        )
        for i, ch in enumerate(ordered)
    }
    states: dict[int, ChapterCoverageState] = {}

    for ch in ordered:
        if is_lead_in_title(ch.title):
            states[ch.time_sec] = ChapterCoverageState(
                chapter=ch,
                primary_indices=[],
                window_indices=[],
                nearby_elsewhere=[],
                status="lead_in",
            )
            continue
        if not ch.is_question:
            states[ch.time_sec] = ChapterCoverageState(
                chapter=ch,
                primary_indices=[],
                window_indices=[],
                nearby_elsewhere=[],
                status="skip",
            )
            continue

        primary = sorted(
            idx for idx, key in item_primary.items() if key == ch.time_sec
        )
        nearby: list[NearbyItemRef] = []
        for it in items:
            if it.q_time_sec is None or it.index in item_primary:
                continue
            drift = abs(it.q_time_sec - ch.time_sec)
            if drift > tolerance_sec:
                continue
            pk = item_primary[it.index]
            other = ch_by_key.get(pk)
            label = f"`{other.time_str}`" if other else "?"
            nearby.append(
                NearbyItemRef(
                    item_index=it.index,
                    primary_chapter_time=pk,
                    primary_chapter_label=label,
                    drift_to_marker_sec=drift,
                )
            )
        nearby.sort(key=lambda r: r.drift_to_marker_sec)

        if primary:
            status = "recognized"
        elif nearby:
            status = "nearby"
        else:
            status = "missing"

        window = chapter_window_item_indices(
            ch.time_sec, end_by_ch[ch.time_sec], items
        )
        states[ch.time_sec] = ChapterCoverageState(
            chapter=ch,
            primary_indices=primary,
            window_indices=window,
            nearby_elsewhere=nearby,
            status=status,
        )
    return states


def group_items_by_question_chapter(
    question_chapters: list[Any],
    items: list[Any],
    tolerance_sec: int,
) -> dict[int, list[int]]:
    """Главная привязка item → глава (каждый item не более чем в одной главе)."""
    item_primary = assign_items_to_primary_chapters(
        question_chapters, items, tolerance_sec
    )
    keys = [ch.time_sec for ch in question_chapters]
    out: dict[int, list[int]] = {k: [] for k in keys}
    for idx, key in item_primary.items():
        if key in out:
            out[key].append(idx)
    for key in out:
        out[key].sort(
            key=lambda i: items[i - 1].q_time_sec or 0,
        )
    return out


def coverage_stats_from_states(
    states: dict[int, ChapterCoverageState],
) -> dict[str, int | float]:
    """Покрытие: глава с своими Q&A или с Q&A рядом (привязаны к соседнему маркеру)."""
    q = [
        s
        for s in states.values()
        if s.chapter.is_question and not is_lead_in_title(s.chapter.title)
    ]
    ok = sum(1 for s in q if s.status in ("recognized", "nearby"))
    strict = sum(1 for s in q if s.status == "recognized")
    missing = sum(1 for s in q if s.status == "missing")
    total = len(q)
    return {
        "recognized": ok,
        "recognized_strict": strict,
        "nearby_only": ok - strict,
        "not_recognized": missing,
        "total": total,
        "pct": ok / total * 100 if total else 100.0,
    }


def chapter_tolerance_stats(
    question_chapters: list[Any],
    assignments: dict[int, list[int]],
) -> dict[str, int | float]:
    """Back-compat wrapper when only assignments dict is available."""
    q = [ch for ch in question_chapters if not is_lead_in_title(ch.title)]
    recognized = sum(1 for ch in q if assignments.get(ch.time_sec))
    total = len(q)
    return {
        "recognized": recognized,
        "recognized_strict": recognized,
        "nearby_only": 0,
        "not_recognized": total - recognized,
        "total": total,
        "pct": recognized / total * 100 if total else 100.0,
    }


def _status_label_from_state(state: ChapterCoverageState) -> str:
    if state.status == "lead_in":
        return "lead-in" if loc.lang == "en" else "подводка"
    if state.status == "skip":
        return "skip" if loc.lang == "en" else "пропуск"
    if state.status == "recognized":
        n = len(state.primary_indices)
        if n == 1:
            return loc.t("status_recognized_one")
        return loc.t("status_recognized_many", n=n)
    if state.status == "nearby":
        ref = state.nearby_elsewhere[0]
        if loc.lang == "en":
            return f"{loc.t('status_nearby')} ({ref.primary_chapter_label})"
        return f"рядом ({ref.primary_chapter_label})"
    return loc.t("status_missing")


def _linked_field_md(label: str, field: dict | None) -> str:
    if not field or not field.get("text"):
        return f"- **{label}:** —"
    t = field.get("time") or "—"
    text = str(field.get("text")).replace("\n", " ").strip()
    return f"- **{label}** (`{t}`): {text}"


def _status_label(
    ch: Any,
    item_indices: list[int],
    *,
    is_lead_in: bool,
) -> str:
    if is_lead_in:
        return "подводка"
    if not ch.is_question:
        return "пропуск"
    if not item_indices:
        return "не распознан"
    if len(item_indices) == 1:
        return "распознан (1 Q&A)"
    return f"распознан ({len(item_indices)} Q&A)"


def _status_short(
    ch: Any,
    item_indices: list[int],
    *,
    is_lead_in: bool,
) -> str:
    return _status_label(ch, item_indices, is_lead_in=is_lead_in)


def _merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not intervals:
        return []
    sorted_iv = sorted(intervals, key=lambda x: x[0])
    merged = [sorted_iv[0]]
    for start, end in sorted_iv[1:]:
        prev_s, prev_e = merged[-1]
        if start <= prev_e + 1:
            merged[-1] = (prev_s, max(prev_e, end))
        else:
            merged.append((start, end))
    return merged


def _item_time_bounds(raw: dict, next_q_sec: int | None) -> tuple[int, int] | None:
    q = raw.get("interviewer_question") or {}
    if not q.get("time"):
        return None
    start = _ts_to_sec(q["time"])
    end = start
    for key in ("candidate_answer", "reference_answer", "interviewer_feedback"):
        f = raw.get(key) or {}
        if f.get("time"):
            end = max(end, _ts_to_sec(f["time"]))
    if next_q_sec is not None and next_q_sec > start:
        end = max(end, next_q_sec - 1)
    return start, end


def find_transcript_gaps(
    transcript_lines: list[tuple[int, str]],
    raw_items: list[dict],
    *,
    bounds: tuple[int, int] | None = None,
    min_gap_sec: int = 25,
    min_lines: int = 4,
) -> list[dict[str, Any]]:
    """Intervals of timecoded transcript not covered by any splitter item span."""
    if not transcript_lines:
        return []

    ordered = sorted(
        enumerate(raw_items, start=1),
        key=lambda pair: _ts_to_sec(
            (pair[1].get("interviewer_question") or {}).get("time") or "99:99:99"
        ),
    )
    spans: list[tuple[int, int]] = []
    for pos, (idx, raw) in enumerate(ordered):
        next_q = None
        if pos + 1 < len(ordered):
            nq = ordered[pos + 1][1].get("interviewer_question") or {}
            if nq.get("time"):
                next_q = _ts_to_sec(nq["time"])
        bounds_pair = _item_time_bounds(raw, next_q)
        if bounds_pair:
            spans.append(bounds_pair)
    covered = _merge_intervals(spans)

    lo = bounds[0] if bounds else transcript_lines[0][0]
    hi = bounds[1] if bounds else transcript_lines[-1][0]

    gaps: list[tuple[int, int]] = []
    cursor = lo
    for start, end in covered:
        if start > cursor:
            gaps.append((cursor, start))
        cursor = max(cursor, end + 1)
    if cursor < hi:
        gaps.append((cursor, hi))

    results: list[dict[str, Any]] = []
    for g_start, g_end in gaps:
        if g_end - g_start < min_gap_sec:
            continue
        lines_in_gap = [(s, t) for s, t in transcript_lines if g_start <= s <= g_end]
        if len(lines_in_gap) < min_lines:
            continue
        quote = "\n".join(f"[{_sec_to_ts(s)}] {t}" for s, t in lines_in_gap)
        results.append(
            {
                "start_sec": g_start,
                "end_sec": g_end,
                "start_str": _sec_to_ts(g_start),
                "end_str": _sec_to_ts(g_end),
                "duration_sec": g_end - g_start,
                "line_count": len(lines_in_gap),
                "quote": quote,
            }
        )
    return results


def _chapter_end_sec(ch: Any, all_chapters: list[Any], *, default_tail_sec: int = 120) -> int:
    for c in sorted(all_chapters, key=lambda x: x.time_sec):
        if c.time_sec > ch.time_sec:
            return c.time_sec
    return ch.time_sec + default_tail_sec


def exclusion_reason(title: str) -> str:
    """Human-readable why a YouTube chapter is not checked as a question."""
    from splitter_validate_video import EXPLANATION_PREFIXES

    t = title.strip()
    for prefix in EXPLANATION_PREFIXES:
        if t.startswith(prefix):
            return f"заголовок «{prefix}…» → служебная глава, не вопрос"
    return "не классифицирован как вопрос (нет совпадения с `EXPLANATION_PREFIXES`)"


def _reason_short(
    ch: Any,
    item_indices: list[int],
    *,
    is_lead_in: bool,
) -> str:
    if is_lead_in:
        return "подводка; текст — в следующем вопросе JSON"
    if not ch.is_question:
        return exclusion_reason(ch.title)
    if not item_indices:
        return "нет извлечённого Q&A в ±tolerance"
    n = len(item_indices)
    return f"{n} item" if n == 1 else f"{n} items"


def _tokenize_lower(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower(), flags=re.UNICODE)


def _common_word_prefix_len(q: str, a: str) -> int:
    qw, aw = _tokenize_lower(q), _tokenize_lower(a)
    n = 0
    for i in range(min(len(qw), len(aw))):
        if qw[i] == aw[i]:
            n += 1
        else:
            break
    return n


def detect_qa_duplicate_prefix(
    question: str | None, answer: str | None, *, min_words: int = 6
) -> str | None:
    """Q and A must not share a long verbatim word prefix (echo / mis-cut span)."""
    q, a = (question or "").strip(), (answer or "").strip()
    if not q or not a:
        return None
    n = _common_word_prefix_len(q, a)
    if n >= min_words:
        return (
            f"первые {n} слов совпадают в `interviewer_question` и `candidate_answer` "
            "(дубль / эхо вопроса в ответе). Переразметьте span по ролям."
        )
    # Substring overlap: question chunk inside answer opening
    qn = " ".join(_tokenize_lower(q))
    an = " ".join(_tokenize_lower(a))
    if len(qn) >= 40:
        chunk = qn[: min(len(qn), 80)]
        if chunk in an[: max(len(an), 120)]:
            return (
                "начало `candidate_answer` содержит тот же фрагмент, что и вопрос "
                "(вероятно один timecode-span на двоих). Разделите реплики."
            )
    return None


def detect_truncated_question(text: str | None) -> str | None:
    if not text or not str(text).strip():
        return None
    t = str(text).strip()
    low = t.lower()
    if any(low.endswith(end) for end in _TRUNCATED_QUESTION_ENDINGS):
        return (
            "обрывок ASR в `interviewer_question` (фраза не закончена). "
            "На шаге 2: склейте следующие реплики интервьюера в PRIMARY_TRANSCRIPT "
            "(не подставляйте заголовок YouTube — video.md только для валидации)."
        )
    if re.search(r"еще не\s+\w{1,12}$", low):
        return (
            "обрывок ASR в `interviewer_question` («…еще не …» без продолжения). "
            "Склейте с следующей строкой интервьюера в timecodes."
        )
    if len(t) < 28 and "?" not in t:
        return (
            "слишком короткий обрывок в `interviewer_question` — на шаге 2 склейте "
            "соседние реплики интервьюера в транскрипте; не парафразируйте по video.md."
        )
    return None


def detect_candidate_text_in_question(text: str | None) -> str | None:
    if not text:
        return None
    low = str(text).lower()
    for m in _CANDIDATE_MARKERS_IN_QUESTION:
        if m in low:
            return (
                f"в `interviewer_question` фраза кандидата («{m}»…). "
                "Перенесите в `candidate_answer`, в вопросе — только интервьюер."
            )
    return None


def detect_feedback_overlaps_answer(
    answer: str | None,
    feedback: str | None,
    reference: str | None = None,
    *,
    min_words: int = 8,
) -> str | None:
    """Feedback/reference must not repeat large spans from candidate_answer."""
    a = (answer or "").strip()
    if not a:
        return None
    for label, other in (
        ("interviewer_feedback", feedback),
        ("reference_answer", reference),
    ):
        o = (other or "").strip()
        if not o:
            continue
        if o in a or a in o:
            return (
                f"текст `{label}` повторяется в `candidate_answer` (или наоборот). "
                "Оставьте реплику только в одном поле."
            )
        # Opening of feedback often duplicates a clause already in the answer
        o_words = _tokenize_lower(o)
        a_words = _tokenize_lower(a)
        if len(o_words) >= 6:
            o_head = " ".join(o_words[:12])
            if o_head in " ".join(a_words):
                return (
                    f"начало `{label}` уже есть в `candidate_answer` "
                    f"(«{' '.join(o_words[:6])}»…). Перенесите в feedback только новую речь интервьюера."
                )
        n = _common_word_prefix_len(o, a)
        if n >= min_words:
            return (
                f"первые {n} слов совпадают в `{label}` и `candidate_answer` — "
                "вероятно одна реплика размазана по полям."
            )
    return None


def detect_interviewer_pivot_in_answer(text: str | None) -> str | None:
    if not text:
        return None
    low = str(text).lower()
    for m in _INTERVIEWER_PIVOT_IN_ANSWER:
        if m in low:
            return (
                f"в `candidate_answer` реплика/вопрос интервьюера («{m}»…). "
                "Обрежьте ответ до начала turn кандидата."
            )
    return None


def detect_speaker_mix_in_answer(text: str | None) -> str | None:
    """Return warning if candidate_answer likely mixes interviewer and candidate speech."""
    if not text or not str(text).strip():
        return None
    t = str(text).lower()
    iv = [m for m in _INTERVIEWER_PHRASES_IN_ANSWER if m in t]
    cand = [m for m in _CANDIDATE_PHRASES_IN_ANSWER if m in t]
    if iv and cand:
        return (
            "в `candidate_answer` вероятно смешаны реплики интервьюера и кандидата "
            f"(интервьюер: «{iv[0]}»…; кандидат: «{cand[0]}»…). "
            "Нужно разрезать span по смене говорящего (system prompt §11)."
        )
    return None


def build_speaker_mix_warnings(raw_items: list[dict]) -> list[str]:
    """Deterministic warnings for role boundaries in Q/A fields."""
    hits: list[tuple[int, str]] = []
    for idx, raw in enumerate(raw_items, start=1):
        q = (raw.get("interviewer_question") or {}).get("text")
        a = (raw.get("candidate_answer") or {}).get("text")
        fb = (raw.get("interviewer_feedback") or {}).get("text")
        ref = (raw.get("reference_answer") or {}).get("text")
        for detector in (
            lambda: detect_qa_duplicate_prefix(q, a),
            lambda: detect_truncated_question(q),
            lambda: detect_candidate_text_in_question(q),
            lambda: detect_interviewer_pivot_in_answer(a),
            lambda: detect_speaker_mix_in_answer(a),
            lambda: detect_feedback_overlaps_answer(a, fb, ref),
        ):
            msg = detector()
            if msg:
                hits.append((idx, msg))
    if not hits:
        return []
    lines = [
        loc.t("speaker_mix_title") + "\n",
        loc.t("speaker_mix_intro") + "\n",
    ]
    for idx, msg in hits:
        lines.append(f"- **Item #{idx}:** {msg}")
    lines.append("")
    return lines


def chapter_for_tolerance_marker(
    item: Any,
    question_chapters: list[Any],
    tolerance_sec: int,
) -> Any | None:
    """Nearest countable question chapter within ±tolerance (for coverage index)."""
    if item.q_time_sec is None:
        return None
    best: Any | None = None
    best_drift = tolerance_sec + 1
    for ch in question_chapters:
        if is_lead_in_title(ch.title):
            continue
        drift = abs(item.q_time_sec - ch.time_sec)
        if drift <= tolerance_sec and drift < best_drift:
            best_drift = drift
            best = ch
    return best


def validate_json_contract(
    splitter_path: Path,
    schema_path: Path | None = None,
) -> tuple[bool, list[str], dict[str, Any]]:
    """
    Load splitter JSON and check contract (schema + required fields).
    Returns (ok, issue_lines, summary_dict).
    """
    summary: dict[str, Any] = {"items_count": 0, "source_id": None, "splitter_mode": None}
    issues: list[str] = []
    try:
        data = json.loads(splitter_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return False, [f"JSON не парсится: {e}"], summary

    for key in ("source_id", "splitter_mode", "items"):
        if key not in data:
            issues.append(f"нет обязательного поля `{key}`")
    summary["source_id"] = data.get("source_id")
    summary["splitter_mode"] = data.get("splitter_mode")
    items = data.get("items")
    if not isinstance(items, list):
        issues.append("`items` должен быть массивом")
        return False, issues, summary
    summary["items_count"] = len(items)

    schema_validated = False
    if schema_path and schema_path.exists():
        try:
            import jsonschema  # type: ignore
        except ImportError as e:
            issues.append(
                "пакет `jsonschema` не установлен — установите: "
                "`pip install jsonschema` или `pip install -e '.[dev]'` из корня репозитория"
            )
            return False, issues, summary
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        try:
            jsonschema.validate(data, schema)
            schema_validated = True
        except jsonschema.ValidationError as e:
            path = ".".join(str(p) for p in e.absolute_path) or "(корень)"
            issues.append(f"не соответствует схеме: {e.message} (поле: {path})")
        except Exception as e:
            issues.append(f"ошибка валидации схемы: {e}")
    summary["schema_validated"] = schema_validated

    required_item = (
        "interviewer_question",
        "candidate_answer",
        "reference_answer",
        "interviewer_feedback",
        "question_type",
        "question_topic",
        "interview_stage",
    )
    for i, it in enumerate(items, start=1):
        if not isinstance(it, dict):
            issues.append(f"item #{i}: не объект")
            continue
        for f in required_item:
            if f not in it:
                issues.append(f"item #{i}: нет поля `{f}`")
    hard_issues = [x for x in issues if not x.startswith("_")]
    return len(hard_issues) == 0, issues, summary


def build_json_contract_section(
    splitter_path: Path,
    schema_path: Path | None = None,
    *,
    ok: bool | None = None,
    issues: list[str] | None = None,
    summary: dict[str, Any] | None = None,
) -> list[str]:
    if ok is None or summary is None:
        ok, issues, summary = validate_json_contract(splitter_path, schema_path)
    issues = issues or []
    summary = summary or {}
    parse_ok = summary.get("items_count") is not None and not any(
        "JSON не парсится" in i for i in issues
    )
    schema_ok = bool(summary.get("schema_validated"))
    schema_missing_pkg = any("jsonschema" in i for i in issues)
    lines = [
        loc.t("check1_title") + "\n",
        loc.t("check1_intro") + "\n",
        "",
        f"- **Файл:** `{splitter_path}`",
    ]
    if schema_path and schema_path.exists():
        repo_root = SKILL_DIR.parents[2]
        try:
            lines.append(f"- **Схема:** `{schema_path.relative_to(repo_root)}`")
        except ValueError:
            lines.append(f"- **Схема:** `{schema_path}`")
    lines.append(
        f"- **Парсинг JSON:** {'✅ успешно' if parse_ok else '❌ ошибка'}"
    )
    if schema_path and schema_path.exists():
        if schema_ok:
            lines.append("- **JSON Schema:** ✅ полностью соответствует схеме")
        elif schema_missing_pkg:
            lines.append(
                "- **JSON Schema:** ❌ не выполнено (установите `jsonschema`)"
            )
        else:
            lines.append("- **JSON Schema:** ❌ есть отклонения (см. ниже)")
    lines.append(f"- **Пар Q&A (`items`):** {summary.get('items_count', 0)}")
    lines.append(f"- **`source_id`:** `{summary.get('source_id')}`")
    lines.append(f"- **`splitter_mode`:** `{summary.get('splitter_mode')}`")
    lines.append("")
    hard = [i for i in issues if not str(i).startswith("_")]
    if hard:
        lines.append("**Замечания:**")
        for iss in hard:
            lines.append(f"- {iss}")
        lines.append("")
    return lines


def build_metrics_howto(
    tolerance_sec: int,
    section_topic_map: dict[str, list[str]] | None,
) -> list[str]:
    """How coverage and topic consistency are computed (under check 2)."""
    lines = [
        "#### Как считаем (проверка 2)\n",
        f"1. **Сопоставление по времени.** У каждого тайм-кода с вопросом на YouTube ищем пары Q&A "
        f"в JSON, у которых время вопроса (`interviewer_question.time`) отличается от маркера "
        f"не больше чем на **{tolerance_sec} с** (в обе стороны). Одна пара Q&A относится "
        "только к одному ближайшему маркеру.\n",
        "",
        "2. **Статус маркера.**",
        "   - **распознан** — рядом с маркером есть «свои» Q&A;",
        "   - **рядом** — своих нет, но в пределах порога есть Q&A у соседнего маркера (не считаем пропуском);",
        "   - **не распознан** — в пределах порога нет ни одной пары (грубая ошибка);",
        "   - **подводка / пропуск** — служебные главы, в метрики не входят.\n",
        "",
        "3. **Coverage** — доля вопросных маркеров со статусом «распознан» или «рядом» "
        "(цель в сводке: ≥90%).\n",
        "",
        "4. **Topic consistency** — у «своих» Q&A поле `question_topic` входит в список тем "
        "для секции интервью из Description `video.md` (цель: ≥90%). "
        "Тема в JSON может отличаться от заголовка главы YouTube — это нормально, если вопрос "
        "по смыслу из той же секции.\n",
    ]
    topic_map = section_topic_map or {}
    if topic_map:
        lines.append("")
        lines.append("Допустимые темы по секциям:")
        for sec, allowed in topic_map.items():
            lines.append(f"- **{sec}** → {', '.join(f'`{t}`' for t in allowed)}")
    else:
        lines.append(
            "\n_Секции в Description не заданы — согласованность тем не считается._"
        )
    lines.append("")
    return lines


def build_unified_pipeline_checks_table(
    *,
    verdict: str,
    json_status: str,
    json_result: str,
    yt_status: str,
    yt_result: str,
    yt_goal: str,
    llm_status: str,
    llm_result: str,
    has_video_rubrics: bool,
) -> list[str]:
    """Single overview: pipeline steps, criteria, status, result (no duplicate summary blocks)."""
    if loc.lang == "en":
        c2_criterion = (
            "If `video.md` has chapters and section rubrics: "
            "**Coverage** >90%, **Topic consistency** >90%"
            if has_video_rubrics
            else "Align YouTube chapter timestamps with Q&A in JSON (no section rubrics in Description)"
        )
        rows = [
            ("**1**", "Prepare (`pipeline-log.md`)", "—", "—", "—", "—", "—"),
            (
                "**2**",
                "LLM → JSON",
                "**Check 1**",
                "Valid JSON per `splitter_output_schema.json`",
                json_status,
                json_result,
                "parse + JSON Schema",
            ),
            ("**3**", "Excel", "—", "—", "—", "—", "—"),
            (
                "**4**",
                "Match `video.md`",
                "**Check 2**",
                c2_criterion,
                yt_status,
                yt_result,
                yt_goal,
            ),
            (
                "**5**",
                "LLM (agent)",
                "**Check 3**",
                "Field meaning and timestamps vs chapter title and labels",
                llm_status,
                llm_result,
                "does not block verdict",
            ),
        ]
        header = "| Step | Action | Check in file | Criterion | Status | Result | Goal |"
    else:
        c2_criterion = (
            "Если в `video.md` есть тайм-коды и рубрики секций: "
            "**Coverage** >90%, **Topic consistency** >90%"
            if has_video_rubrics
            else "Сверка тайм-кодов YouTube с Q&A в JSON (рубрики в Description не заданы)"
        )
        rows = [
            ("**1**", "Подготовка (`pipeline-log.md`)", "—", "—", "—", "—", "—"),
            (
                "**2**",
                "LLM → JSON",
                "**Проверка 1**",
                "Валидный JSON по `splitter_output_schema.json`",
                json_status,
                json_result,
                "парсинг + JSON Schema",
            ),
            ("**3**", "Excel", "—", "—", "—", "—", "—"),
            (
                "**4**",
                "Сверка с `video.md`",
                "**Проверка 2**",
                c2_criterion,
                yt_status,
                yt_result,
                yt_goal,
            ),
            (
                "**5**",
                "LLM (агент)",
                "**Проверка 3**",
                "Смысл и тайм-коды полей vs заголовок главы и метки",
                llm_status,
                llm_result,
                "не блокирует вердикт",
            ),
        ]
        header = "| Шаг | Действие | Проверка в файле | Критерий | Статус | Результат | Цель |"
    lines = [
        loc.t("how_check_title") + "\n",
        f"{loc.t('verdict_heading')} {verdict}\n",
        loc.t("pipeline_steps_note") + "\n",
        "",
        header,
        "|-----|----------|------------------|----------|--------|-----------|------|",
    ]
    for step, action, check, crit, status, result, goal in rows:
        lines.append(
            f"| {step} | {action} | {check} | {crit} | {status} | {result} | {goal} |"
        )
    lines.append("")
    return lines


def build_check2_glossary() -> list[str]:
    """Short definitions before YouTube check details."""
    return [
        "#### Термины (проверка 2)\n",
        "- **Маркер** — тайм-код в `video.md` (строка в блоке Chapters): точка на шкале видео.\n",
        "- **Вопросная глава** — маркер с реальным вопросом интервью; участвует в Coverage.\n",
        "- **Служебная глава** — вступление, подводка (🔗), разбор задачи, пауза; "
        "в Coverage **не входит**, но в сводной таблице ниже указано, **куда ушла** речь в JSON.\n",
        "",
    ]


def build_check3_semantic_section(
    llm_verdicts: dict[str, LlmChapterVerdict] | None,
    *,
    auto_skipped_reason: str | None = None,
) -> list[str]:
    """Step 5 — semantic LLM validation block inside the report body."""
    lines = [
        loc.t("check3_title") + "\n",
        loc.t("check3_intro") + "\n",
        "",
    ]
    if auto_skipped_reason:
        lines.append(f"- **Статус:** ⏭ пропущен — {auto_skipped_reason}")
        lines.append("")
        return lines
    if not llm_verdicts:
        lines.append(
            "_Результаты появятся после шага 5 пайплайна (агент выполняет в том же чате, как шаг 2)._"
        )
        lines.append("")
        return lines
    n = len(llm_verdicts)
    t_ok = sum(1 for v in llm_verdicts.values() if v.time_alignment_ok)
    c_ok = sum(1 for v in llm_verdicts.values() if v.content_alignment_ok)
    both = sum(
        1 for v in llm_verdicts.values()
        if v.time_alignment_ok and v.content_alignment_ok
    )
    if both == n:
        status = "✅"
        brief = f"все {n} глав без замечаний"
    elif both >= n * 0.7:
        status = "⚠️"
        brief = f"{both}/{n} глав без замечаний"
    else:
        status = "❌"
        brief = f"много замечаний ({both}/{n} глав ок)"
    lines.append(f"- **Статус:** {status} {brief}")
    lines.append(
        f"- **Тайм-коды полей:** {t_ok}/{n} ок · **Смысл/метки:** {c_ok}/{n} ок"
    )
    notes = [v for v in llm_verdicts.values() if v.notes.strip()]
    if notes:
        lines.append(f"- **Глав с комментарием LLM:** {len(notes)} (см. детали по главам)")
    lines.append("")
    return lines


def build_section_topic_audit(
    states: dict[int, ChapterCoverageState],
    items: list[Any],
    raw_items: list[dict],
    section_topic_map: dict[str, list[str]] | None,
) -> list[str]:
    """Explain per-section video vs splitter counts and topic rubric mismatches."""
    topic_map = section_topic_map or {}
    if not topic_map:
        return []
    by_sec: dict[str, list[ChapterCoverageState]] = {}
    for st in states.values():
        if st.status in ("lead_in", "skip") or not st.chapter.is_question:
            continue
        sec = st.chapter.section or "Без секции"
        by_sec.setdefault(sec, []).append(st)
    lines = [
        "#### По секциям интервью\n",
        "",
        "| Секция | Тайм-кодов на YouTube | Распознанных Q&A | Темы в JSON | Пояснение |",
        "|--------|----------------------|------------------|-------------|-----------|",
    ]
    for sec in sorted(by_sec.keys()):
        rows = sorted(by_sec[sec], key=lambda s: s.chapter.time_sec)
        video_n = len(rows)
        primary_ids: set[int] = set()
        for st in rows:
            primary_ids.update(st.primary_indices)
        splitter_n = len(primary_ids)
        delta = splitter_n - video_n
        topics = sorted(
            {
                raw_items[i - 1].get("question_topic")
                for i in primary_ids
                if raw_items[i - 1].get("question_topic")
            }
        )
        topics_str = ", ".join(f"`{t}`" for t in topics) if topics else "—"
        allowed = topic_map.get(sec)
        topic_warns: list[str] = []
        if allowed:
            for st in rows:
                for idx in st.primary_indices:
                    t = raw_items[idx - 1].get("question_topic")
                    if t and t not in allowed:
                        topic_warns.append(
                            f"`{st.chapter.time_str}` → `{t}` (допустимо: {', '.join(allowed)})"
                        )
        missing_n = sum(1 for st in rows if st.status == "missing")
        nearby_n = sum(1 for st in rows if st.status == "nearby")
        parts: list[str] = []
        if delta == 0 and not topic_warns and missing_n == 0:
            parts.append("Совпадает: у каждого маркера есть свои Q&A.")
        else:
            if delta > 0:
                parts.append(
                    f"+{delta}: сплиттер добавил пары без отдельного маркера YouTube "
                    "(уточняющие вопросы внутри секции — нормально)."
                )
            if delta < 0:
                parts.append(
                    f"{delta}: у {abs(delta)} маркеров нет «своих» Q&A "
                    f"(не распознан: {missing_n}, рядом у соседа: {nearby_n})."
                )
            if topic_warns:
                parts.append(
                    "Тема JSON вне списка секции (часто ок, если вопрос из смежной подтемы): "
                    + "; ".join(topic_warns[:3])
                )
                if len(topic_warns) > 3:
                    parts.append(f"… ещё {len(topic_warns) - 3}")
        if allowed and topics:
            off = [t for t in topics if t not in allowed]
            if off and not topic_warns:
                parts.append(
                    f"Темы {', '.join(f'`{t}`' for t in off)} не в списке секции — "
                    "проверьте по смыслу вопроса, не только по названию рубрики."
                )
        lines.append(
            f"| {sec} | {video_n} | {splitter_n} | "
            f"{topics_str} | {' '.join(parts) or '—'} |"
        )
    lines.append("")
    return lines


def build_service_chapters_appendix(
    all_chapters: list[Any],
    items: list[Any],
    raw_items: list[dict],
    assignments: dict[int, list[int]],
) -> list[str]:
    """Lead-ins and excluded chapters: placement in JSON only (no transcript duplicate)."""
    service = [
        c
        for c in all_chapters
        if is_lead_in_title(c.title)
        or (not c.is_question and not is_lead_in_title(c.title))
    ]
    if not service:
        return []
    lines = [
        "### Служебные главы YouTube (подводки, интро, разбор)\n",
        "Не входят в **покрытие**. Транскрипт здесь не повторяем — только **куда ушли** в JSON.\n",
        "",
        "| Тайм-код | Тип | Заголовок | Куда в JSON |",
        "|----------|-----|-----------|-------------|",
    ]
    for ch in sorted(service, key=lambda c: c.time_sec):
        if is_lead_in_title(ch.title):
            kind = "подводка"
            _, trace = trace_lead_in_placement(
                ch, all_chapters, items, raw_items, assignments
            )
            dest = " ".join(
                t.replace("- **", "").replace("**", "")
                for t in trace
                if t.startswith("- **")
            )[:120] or "—"
        else:
            kind = "исключено"
            dest = exclusion_reason(ch.title)
            if is_explanation_title(ch.title):
                _, trace = trace_explanation_placement(ch, all_chapters, raw_items)
                for t in trace:
                    if "Item #" in t or "reference" in t.lower():
                        dest = t.strip("- ")[:100]
                        break
        title = ch.title.replace("|", "/")
        if len(title) > 36:
            title = title[:33] + "…"
        lines.append(f"| `{ch.time_str}` | {kind} | {title} | {dest} |")
    lines.append("")
    return lines


def chapter_for_item_window(
    item: Any,
    ordered_chapters: list[Any],
) -> Any | None:
    """Глава YouTube, в чьё окно [маркер … следующая глава) попадает вопрос item."""
    if item.q_time_sec is None:
        return None
    for i, ch in enumerate(ordered_chapters):
        end = (
            ordered_chapters[i + 1].time_sec
            if i + 1 < len(ordered_chapters)
            else 10**9
        )
        if ch.time_sec <= item.q_time_sec < end:
            return ch
    return None


def build_validation_index_table(
    all_chapters: list[Any],
    states: dict[int, ChapterCoverageState],
    items: list[Any],
    raw_items: list[dict],
    tolerance_sec: int,
    transcript_lines: list[tuple[int, str]] | None = None,
    llm_verdicts: dict[str, LlmChapterVerdict] | None = None,
) -> list[str]:
    """Compact index: one row per YouTube chapter."""
    lines = [
        loc.t("yt_table_title") + "\n",
        loc.t("yt_table_intro") + "\n",
        "",
        "| # | YT | Заголовок | Секция | Привязка (4) | Q&A | Темы | Смысл (5) | Куда в JSON |",
        "|---|-----|-----------|--------|--------------|-----|------|-----------|-------------|",
    ]
    llm_verdicts = llm_verdicts or {}
    q_num = 0
    for ch in sorted(all_chapters, key=lambda c: c.time_sec):
        st = states[ch.time_sec]
        if _is_countable_question(ch):
            q_num += 1
            num = str(q_num)
        else:
            num = "—"
        status_short = _status_label_from_state(st)
        sem = _semantic_short_label(llm_verdicts.get(ch.time_str))
        sec = (ch.section or "—").replace("|", "/")
        if len(sec) > 18:
            sec = sec[:15] + "…"
        indices = st.primary_indices
        items_s = ", ".join(f"#{i}" for i in indices) if indices else "—"
        topics: list[str] = []
        for idx in indices:
            t = raw_items[idx - 1].get("question_topic")
            if t and t not in topics:
                topics.append(str(t))
        topics_s = ", ".join(f"`{t}`" for t in topics) if topics else "—"
        note = "—"
        if st.status == "nearby" and st.nearby_elsewhere:
            refs = ", ".join(
                f"#{r.item_index}→{r.primary_chapter_label}"
                for r in st.nearby_elsewhere[:3]
            )
            note = f"рядом: {refs}"
        elif st.status in ("lead_in", "skip"):
            trace = json_trace_for_chapter(
                ch,
                all_chapters,
                items,
                raw_items,
                {st.chapter.time_sec: st.primary_indices for st in states.values()},
                indices,
                is_lead_in=st.status == "lead_in",
                tolerance_sec=tolerance_sec,
                transcript_lines=transcript_lines,
            )
            note = trace.replace("|", "/")[:48]
        title = ch.title.replace("|", "/")
        if len(title) > 36:
            title = title[:33] + "…"
        lines.append(
            f"| {num} | `{ch.time_str}` | {title} | {sec} | {status_short} | "
            f"{items_s} | {topics_s} | {sem} | {note} |"
        )
    lines.append("")
    return lines


def build_section_overview(
    states: dict[int, ChapterCoverageState],
) -> list[str]:
    """Group question chapters by YouTube interview section (рубрика)."""
    by_sec: dict[str, list[ChapterCoverageState]] = {}
    for st in states.values():
        if st.status in ("lead_in", "skip"):
            continue
        if not st.chapter.is_question:
            continue
        sec = st.chapter.section or "Без секции"
        by_sec.setdefault(sec, []).append(st)
    if not by_sec:
        return []
    lines = [
        "### По секциям интервью (рубрики из video.md)\n",
        "Одна секция (Python, ML, …) обычно содержит **несколько** тайм-кодов-вопросов. "
        "Ниже — как они соотнесены с Q&A.\n",
    ]
    for sec in sorted(by_sec.keys()):
        rows = sorted(by_sec[sec], key=lambda s: s.chapter.time_sec)
        lines.append(f"#### {sec}\n")
        lines.append("| YT | Заголовок | Статус | Q&A |")
        lines.append("|-----|-----------|--------|-----|")
        for st in rows:
            ch = st.chapter
            title = ch.title.replace("|", "/")
            if len(title) > 42:
                title = title[:39] + "…"
            qa = ", ".join(f"#{i}" for i in st.primary_indices) or "—"
            lines.append(
                f"| `{ch.time_str}` | {title} | {_status_label_from_state(st)} | {qa} |"
            )
        lines.append("")
    return lines


def build_excluded_chapters_section(
    all_chapters: list[Any],
    raw_items: list[dict],
    transcript_lines: list[tuple[int, str]] | None,
) -> list[str]:
    excluded = [
        c for c in all_chapters if not c.is_question and not is_lead_in_title(c.title)
    ]
    if not excluded:
        return []
    lines = [
        "## Исключённые главы (не вопросы)\n",
        "Не входят в **Coverage**. Для глав **«Объяснение» / «Разбор»** проверяем, что речь интервьюера "
        "попала в `reference_answer` или `interviewer_feedback` соседней задачи (не отдельный item).\n",
    ]
    for ch in sorted(excluded, key=lambda c: c.time_sec):
        end_sec = _chapter_end_sec(ch, all_chapters)
        lines.append(f"### `{ch.time_str}` — {ch.title}\n")
        if ch.section:
            lines.append(f"- **Секция YouTube:** {ch.section}")
        lines.append(f"- **Почему исключено:** {exclusion_reason(ch.title)}")
        if is_explanation_title(ch.title):
            _, trace_lines = trace_explanation_placement(ch, all_chapters, raw_items)
            lines.extend(trace_lines)
        lines.append("")
        if transcript_lines:
            lines.append("**Транскрипт на интервале главы:**")
            lines.append("")
            lines.append("```text")
            lines.append(
                transcript_excerpt(transcript_lines, ch.time_sec, end_sec, max_chars=1800)
            )
            lines.append("```")
            lines.append("")
    return lines


def build_lead_in_chapters_section(
    all_chapters: list[Any],
    items: list[Any],
    raw_items: list[dict],
    assignments: dict[int, list[int]],
    transcript_lines: list[tuple[int, str]] | None,
) -> list[str]:
    lead_ins = [c for c in all_chapters if is_lead_in_title(c.title)]
    if not lead_ins:
        return []
    lines = [
        "## Подводки\n",
        "Отдельный item в Coverage **не считается**. Текст подводки должен попасть в "
        "`interviewer_question` **следующей** вопросной главы — ниже указано, в какой item.\n",
    ]
    for ch in sorted(lead_ins, key=lambda c: c.time_sec):
        end_sec = _chapter_end_sec(ch, all_chapters)
        lines.append(f"### `{ch.time_str}` — {ch.title}\n")
        if ch.section:
            lines.append(f"- **Секция:** {ch.section}")
        _, trace_lines = trace_lead_in_placement(
            ch, all_chapters, items, raw_items, assignments
        )
        lines.extend(trace_lines)
        lines.append("")
        if transcript_lines:
            lines.append("**Транскрипт:**")
            lines.append("")
            lines.append("```text")
            lines.append(
                transcript_excerpt(transcript_lines, ch.time_sec, end_sec, max_chars=1200)
            )
            lines.append("```")
            lines.append("")
    return lines


def build_recognized_questions_section(
    all_chapters: list[Any],
    items: list[Any],
    raw_items: list[dict],
    assignments: dict[int, list[int]],
    llm_verdicts: dict[str, LlmChapterVerdict] | None = None,
) -> list[str]:
    """Full Q&A texts only for chapters with extracted items."""
    llm_verdicts = llm_verdicts or {}
    recognized = [
        ch
        for ch in sorted(all_chapters, key=lambda c: c.time_sec)
        if ch.is_question
        and not is_lead_in_title(ch.title)
        and assignments.get(ch.time_sec)
    ]
    if not recognized:
        return ["## Распознанные вопросы\n\n_Нет глав с извлечённым Q&A._\n"]
    lines = [
        "## Распознанные вопросы (примеры Q&A)\n",
        "Полные тексты из JSON сплиттера. **Δt** — только у **первого** item в группе "
        "(время вопроса − тайм-код YouTube).\n",
    ]
    q_num = 0
    for ch in recognized:
        q_num += 1
        item_indices = assignments[ch.time_sec]
        lines.append(f"### {q_num}. `{ch.time_str}` — {ch.title}\n")
        lines.append(f"**Статус:** {_status_label(ch, item_indices, is_lead_in=False)}")
        if ch.section:
            lines.append(f"- **Секция YouTube:** {ch.section}")
        lines.append("")
        verdict = llm_verdicts.get(ch.time_str)
        if verdict and verdict.notes.strip():
            lines.append(f"- **Шаг 5:** {verdict.notes.strip()}")
        for pos, idx in enumerate(item_indices):
            it = items[idx - 1]
            raw = raw_items[idx - 1]
            if pos == 0:
                drift = (it.q_time_sec or 0) - ch.time_sec
                lines.append(
                    f"- **Δt (первый item #{idx}):** {drift:+d} с "
                    f"(вопрос `{it.q_time_str or '—'}` vs глава `{ch.time_str}`)"
                )
                lines.append("")
            elif pos == 1:
                lines.append(
                    "_Дополнительные items в той же теме (Δt к маркеру главы не считаем):_\n"
                )
            lines.extend(_format_item_block(idx, raw))
    return lines


def build_unrecognized_questions_section(
    all_chapters: list[Any],
    states: dict[int, ChapterCoverageState],
    items: list[Any],
    tolerance_sec: int,
    transcript_lines: list[tuple[int, str]] | None,
    llm_verdicts: dict[str, LlmChapterVerdict] | None = None,
) -> list[str]:
    llm_verdicts = llm_verdicts or {}
    assignments = {
        st.chapter.time_sec: st.primary_indices for st in states.values()
    }
    missed = [
        st.chapter
        for st in sorted(states.values(), key=lambda s: s.chapter.time_sec)
        if st.status == "missing"
    ]
    if not missed:
        return []
    lines = [
        "### Главы без Q&A рядом с маркером\n",
        f"В пределах ±{tolerance_sec} с от тайм-кода **нет ни одной** извлечённой пары. "
        "Ниже — гипотеза по транскрипту.\n",
    ]
    for ch in missed:
        lines.append(f"#### `{ch.time_str}` — {ch.title}\n")
        if ch.section:
            lines.append(f"- **Секция интервью:** {ch.section}")
        if transcript_lines:
            _, hypo_lines = classify_missed_chapter(
                ch, all_chapters, transcript_lines, assignments, items, tolerance_sec
            )
            lines.extend(hypo_lines)
        lines.append("")
        verdict = llm_verdicts.get(ch.time_str)
        if verdict and verdict.notes.strip():
            lines.append(f"- **LLM:** {verdict.notes.strip()}")
            lines.append("")
        if transcript_lines:
            end_sec = _chapter_end_sec(ch, all_chapters, default_tail_sec=tolerance_sec * 2)
            lines.append("**Транскрипт:**")
            lines.append("")
            lines.append("```text")
            lines.append(
                transcript_excerpt(transcript_lines, ch.time_sec, end_sec, max_chars=2500)
            )
            lines.append("```")
            lines.append("")
    return lines


def build_validation_body(
    all_chapters: list[Any],
    items: list[Any],
    raw_items: list[dict],
    states: dict[int, ChapterCoverageState],
    assignments: dict[int, list[int]],
    tolerance_sec: int,
    section_topic_map: dict[str, list[str]] | None = None,
    transcript_lines: list[tuple[int, str]] | None = None,
    llm_verdicts: dict[str, LlmChapterVerdict] | None = None,
) -> dict[str, list[str]]:
    """Structured validation sections for a single human-readable report."""
    llm_verdicts = llm_verdicts or {}
    chapter_details = build_chapter_details_section(
        states,
        items,
        raw_items,
        section_topic_map,
        llm_verdicts,
    )
    return {
        "youtube_intro": [],
        "section_audit": build_section_topic_audit(
            states, items, raw_items, section_topic_map
        ),
        "index": build_validation_index_table(
            all_chapters,
            states,
            items,
            raw_items,
            tolerance_sec,
            transcript_lines,
            llm_verdicts,
        ),
        "unrecognized": build_unrecognized_questions_section(
            all_chapters,
            states,
            items,
            tolerance_sec,
            transcript_lines,
            llm_verdicts,
        ),
        "chapter_details": chapter_details,
        "speaker_mix": build_speaker_mix_warnings(raw_items),
    }


def build_master_validation_section(
    all_chapters: list[Any],
    items: list[Any],
    raw_items: list[dict],
    states: dict[int, ChapterCoverageState],
    assignments: dict[int, list[int]],
    tolerance_sec: int,
    section_topic_map: dict[str, list[str]] | None = None,
    transcript_lines: list[tuple[int, str]] | None = None,
    llm_verdicts: dict[str, LlmChapterVerdict] | None = None,
) -> list[str]:
    """Flatten validation body sections (legacy helper)."""
    body = build_validation_body(
        all_chapters,
        items,
        raw_items,
        states,
        assignments,
        tolerance_sec,
        section_topic_map,
        transcript_lines,
        llm_verdicts,
    )
    out: list[str] = []
    for key in (
        "youtube_intro",
        "section_audit",
        "index",
        "unrecognized",
        "chapter_details",
        "speaker_mix",
    ):
        if body.get(key):
            out.extend(body[key])
    return out


def build_transcript_gaps_section(
    gaps: list[dict[str, Any]],
) -> list[str]:
    lines = [
        loc.t("gaps_title") + "\n",
        loc.t("gaps_intro") + "\n",
    ]
    if not gaps:
        lines.append(loc.t("gaps_none") + "\n")
        return lines

    lines.append(f"**Найдено фрагментов:** {len(gaps)}\n")
    for i, gap in enumerate(gaps, start=1):
        lines.append(
            f"### {i}. `{gap['start_str']}` — `{gap['end_str']}` "
            f"({gap['duration_sec']} с, {gap['line_count']} строк)"
        )
        lines.append("")
        lines.append("```text")
        lines.append(gap["quote"])
        lines.append("```")
        lines.append("")
    return lines


def chapter_window_stats(blocks: list[ChapterBlock]) -> dict[str, int | float]:
    """Coverage aligned with «Главы YouTube» (strict chapter windows)."""
    q = [b for b in blocks if b.recognition != "skipped"]
    recognized = sum(1 for b in q if b.recognition in ("single", "multiple"))
    not_rec = sum(1 for b in q if b.recognition == "not_recognized")
    total = len(q)
    pct = recognized / total * 100 if total else 100.0
    return {
        "recognized": recognized,
        "not_recognized": not_rec,
        "total": total,
        "pct": pct,
    }


@dataclass
class LlmChapterVerdict:
    chapter_time: str
    time_alignment_ok: bool
    content_alignment_ok: bool
    notes: str


def build_chapter_blocks(
    chapters: list[Any],
    items: list[Any],
    raw_items: list[dict],
) -> list[ChapterBlock]:
    ordered = sorted(chapters, key=lambda c: c.time_sec)
    blocks: list[ChapterBlock] = []
    for i, ch in enumerate(ordered):
        end_sec = ordered[i + 1].time_sec if i + 1 < len(ordered) else 10**9
        end_str = ordered[i + 1].time_str if i + 1 < len(ordered) else "конец"
        if not ch.is_question:
            blocks.append(ChapterBlock(ch, end_str, end_sec, [], [], "skipped"))
            continue
        matched = [
            it
            for it in items
            if it.q_time_sec is not None and ch.time_sec <= it.q_time_sec < end_sec
        ]
        matched.sort(key=lambda x: x.q_time_sec or 0)
        raw_matched = [raw_items[it.index - 1] for it in matched]
        if not matched:
            rec = "not_recognized"
        elif len(matched) == 1:
            rec = "single"
        else:
            rec = "multiple"
        blocks.append(ChapterBlock(ch, end_str, end_sec, matched, raw_matched, rec))
    return blocks


def _field_md(label: str, field: dict | None) -> str:
    if not field or not field.get("text"):
        return f"- **{label}:** —"
    t = field.get("time") or "—"
    text = str(field.get("text")).replace("\n", " ").strip()
    return f"- **{label}** (`{t}`): {text}"


def _format_item_block(index: int, raw: dict) -> list[str]:
    meta = []
    if raw.get("question_topic"):
        meta.append(f"`{raw['question_topic']}`")
    if raw.get("question_type"):
        meta.append(f"type={raw['question_type']}")
    if raw.get("interview_stage"):
        meta.append(f"stage={raw['interview_stage']}")
    meta_s = " · ".join(meta) if meta else "—"
    lines = [f"#### Item #{index}", ""]
    lines.append(_field_md(loc.t("field_question"), raw.get("interviewer_question")))
    lines.append(_field_md(loc.t("field_answer"), raw.get("candidate_answer")))
    lines.append(_field_md(loc.t("field_reference"), raw.get("reference_answer")))
    lines.append(_field_md(loc.t("field_feedback"), raw.get("interviewer_feedback")))
    lines.append(f"- **{loc.t('field_labels')}:** {meta_s}")
    lines.append("")
    return lines


def _recognition_label(rec: str, n: int) -> str:
    if rec == "skipped":
        return "— *исключено* (глава не считается отдельным вопросом)"
    if rec == "not_recognized":
        return "❌ **не распознан** — грубая ошибка (нет Q&A в окне главы)"
    if rec == "single":
        return "✅ **распознан** — один Q&A"
    return f"✅ **распознано несколько вопросов** — {n} Q&A"


def _semantic_short_label(verdict: LlmChapterVerdict | None) -> str:
    if verdict is None:
        return "⏳"
    if verdict.time_alignment_ok and verdict.content_alignment_ok:
        return "✅"
    if verdict.time_alignment_ok or verdict.content_alignment_ok:
        return "⚠️"
    return "❌"


def _chapter_integrated_verdict_lines(
    st: ChapterCoverageState,
    verdict: LlmChapterVerdict | None,
) -> list[str]:
    """Merge step 4 (marker binding) and step 5 (semantic) for one chapter."""
    ch = st.chapter
    if st.status == "missing":
        s4 = f"❌ к маркеру `{ch.time_str}` нет своих Q&A (шаг 4)"
    elif st.status == "nearby":
        ref = st.nearby_elsewhere[0] if st.nearby_elsewhere else None
        lbl = ref.primary_chapter_label if ref else "сосед"
        s4 = f"⚠️ свои Q&A у маркера нет; рядом item #{ref.item_index if ref else '?'} → {lbl} (шаг 4)"
    elif st.status == "recognized":
        n_pri = len(st.primary_indices)
        s4 = (
            f"✅ у маркера {n_pri} Q&A"
            if n_pri != 1
            else "✅ у маркера 1 Q&A"
        )
    else:
        s4 = _status_label_from_state(st)

    if verdict is None:
        s5 = "⏳ смысл не проверен (шаг 5)"
    elif verdict.time_alignment_ok and verdict.content_alignment_ok:
        s5 = "✅ по смыслу и тайм-кодам полей всё сходится (шаг 5)"
    else:
        issues: list[str] = []
        if not verdict.time_alignment_ok:
            issues.append("тайм-коды полей")
        if not verdict.content_alignment_ok:
            issues.append("тексты/метки")
        s5 = f"⚠️ шаг 5: {' и '.join(issues)}"
        if verdict.notes.strip():
            s5 += f" ({verdict.notes.strip()})"

    return [f"- **Проверка главы:** {s4} · {s5}", ""]


SEMANTIC_SECTION_START = "<!-- SEMANTIC_VALIDATION -->"
SEMANTIC_SECTION_END = "<!-- /SEMANTIC_VALIDATION -->"
SEMANTIC_HEADING = "## Semantic validation (step 5)"


def load_semantic_json_from_report(report_md: Path) -> dict | None:
    """Parse step-5 LLM JSON embedded in validation-report.md."""
    if not report_md.exists():
        return None
    text = report_md.read_text(encoding="utf-8")
    block_re = re.compile(
        rf"{re.escape(SEMANTIC_SECTION_START)}.*?```json\s*(?P<body>.*?)\s*```.*?{re.escape(SEMANTIC_SECTION_END)}",
        re.DOTALL,
    )
    m = block_re.search(text)
    if m:
        return json.loads(m.group("body"))
    if SEMANTIC_HEADING in text:
        m2 = re.search(
            rf"{re.escape(SEMANTIC_HEADING)}.*?```json\s*(?P<body>.*?)\s*```",
            text,
            re.DOTALL,
        )
        if m2:
            return json.loads(m2.group("body"))
    return None


def save_semantic_json_to_report(report_md: Path, data: dict) -> None:
    """Write step-5 LLM response into validation-report.md (replaces sidecar .json)."""
    block = (
        f"{SEMANTIC_SECTION_START}\n\n"
        f"{SEMANTIC_HEADING}\n\n"
        "Машинный ответ LLM (шаг 5). Валидатор читает этот блок при повторном прогоне.\n\n"
        f"```json\n{json.dumps(data, ensure_ascii=False, indent=2)}\n```\n\n"
        f"{SEMANTIC_SECTION_END}\n"
    )
    report_md.parent.mkdir(parents=True, exist_ok=True)
    text = report_md.read_text(encoding="utf-8") if report_md.exists() else ""
    section_re = re.compile(
        rf"{re.escape(SEMANTIC_SECTION_START)}.*?{re.escape(SEMANTIC_SECTION_END)}",
        re.DOTALL,
    )
    if section_re.search(text):
        text = section_re.sub(block, text, count=1)
    else:
        text = text.rstrip() + "\n\n" + block
    report_md.write_text(text, encoding="utf-8")


def load_llm_verdicts(path: Path | None) -> dict[str, LlmChapterVerdict]:
    if not path or not path.exists():
        return {}
    data: dict | None = None
    if path.suffix == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
    else:
        data = load_semantic_json_from_report(path)
        if data is None:
            import sys

            skill_dir = Path(__file__).resolve().parents[1]
            if str(skill_dir) not in sys.path:
                sys.path.insert(0, str(skill_dir))
            from artifact_paths import validation_semantic_json_from_report  # noqa: WPS433

            legacy = validation_semantic_json_from_report(path)
            if legacy.exists():
                data = json.loads(legacy.read_text(encoding="utf-8"))
    if not data:
        return {}
    out: dict[str, LlmChapterVerdict] = {}
    for ch in data.get("chapters", []):
        t = ch.get("chapter_time")
        if not t:
            continue
        out[t] = LlmChapterVerdict(
            chapter_time=t,
            time_alignment_ok=bool(ch.get("time_alignment_ok")),
            content_alignment_ok=bool(ch.get("content_alignment_ok")),
            notes=str(ch.get("notes") or ""),
        )
    return out


def build_match_results_from_states(
    states: dict[int, ChapterCoverageState],
    items: list[Any],
    section_topic_map: dict[str, list[str]] | None,
) -> list[Any]:
    """MatchResult list for commentary / topic metrics (first primary item per chapter)."""
    from splitter_validate_video import MatchResult

    topic_map = section_topic_map or {}
    results: list[Any] = []
    for st in sorted(
        (s for s in states.values() if s.chapter.is_question and not is_lead_in_title(s.chapter.title)),
        key=lambda s: s.chapter.time_sec,
    ):
        ch = st.chapter
        r = MatchResult(chapter=ch)
        if st.primary_indices:
            it = items[st.primary_indices[0] - 1]
            r.item = it
            if it.q_time_sec is not None:
                r.drift_sec = abs(it.q_time_sec - ch.time_sec)
            allowed = topic_map.get(ch.section) if ch.section else None
            r.topic_allowed = allowed
            r.topic_actual = it.question_topic
            if allowed is not None:
                r.topic_ok = it.question_topic in allowed
        results.append(r)
    return results


def build_chapter_details_section(
    states: dict[int, ChapterCoverageState],
    items: list[Any],
    raw_items: list[dict],
    section_topic_map: dict[str, list[str]] | None,
    llm_verdicts: dict[str, LlmChapterVerdict] | None = None,
) -> list[str]:
    """Раздел 3: по каждой вопросной главе YouTube — что распознано и с какой темой."""
    llm_verdicts = llm_verdicts or {}
    topic_map = section_topic_map or {}
    lines = [
        loc.t("chapter_details_title") + "\n",
        loc.t("chapter_details_intro") + "\n",
        "",
    ]
    q_num = 0
    for st in sorted(
        (s for s in states.values() if s.status not in ("lead_in", "skip")),
        key=lambda s: s.chapter.time_sec,
    ):
        ch = st.chapter
        if not ch.is_question or is_lead_in_title(ch.title):
            continue
        q_num += 1
        detail_idxs = st.primary_indices
        lines.append(f"### {q_num}. `{ch.time_str}` — {ch.title}\n")
        if ch.section:
            lines.append(f"- **Секция интервью (YouTube):** {ch.section}")
        verdict = llm_verdicts.get(ch.time_str)
        lines.extend(_chapter_integrated_verdict_lines(st, verdict))

        if st.status == "missing":
            lines.append(
                "_В пределах допуска от маркера нет ни одной пары Q&A — грубая ошибка "
                "или вопрос не задавался (проверьте транскрипт)._"
            )
            lines.append("")
            continue

        if detail_idxs:
            lines.append(loc.t("qa_at_marker") + "\n")
            lines.append(
                f"| {loc.t('table_item')} | Δt | `question_topic` | {loc.t('col_question_start')} |"
            )
            lines.append("|------|-----|------------------|----------------|")
            allowed = topic_map.get(ch.section) if ch.section else None
            topic_off_list = False
            for idx in detail_idxs:
                it = items[idx - 1]
                raw = raw_items[idx - 1]
                drift = (it.q_time_sec or 0) - ch.time_sec
                topic = raw.get("question_topic") or "—"
                qtxt = (raw.get("interviewer_question") or {}).get("text") or ""
                preview = (qtxt[:70] + "…") if len(qtxt) > 70 else qtxt
                topic_flag = ""
                if allowed is not None and topic != "—":
                    ok_topic = topic in allowed
                    topic_flag = " ✓" if ok_topic else " ⚠"
                    if not ok_topic:
                        topic_off_list = True
                lines.append(
                    f"| #{idx} | {drift:+d} с | `{topic}`{topic_flag} | {preview} |"
                )
            if allowed is not None:
                lines.append("")
                hint = (
                    " ⚠ — у части items тема вне списка секции (часто нормально для смежной подтемы)."
                    if topic_off_list
                    else ""
                )
                lines.append(
                    f"_Допустимые темы для секции «{ch.section}»: "
                    f"{', '.join(f'`{t}`' for t in allowed)}.{hint}_"
                )
            lines.append("")

        if st.nearby_elsewhere:
            lines.append(
                "**Рядом с маркером, но привязаны к другой главе** (не считается пропуском)\n"
            )
            lines.append("| Item | Главная глава | Δt к этому маркеру |")
            lines.append("|------|---------------|-------------------|")
            for ref in st.nearby_elsewhere:
                lines.append(
                    f"| #{ref.item_index} | {ref.primary_chapter_label} | "
                    f"{ref.drift_to_marker_sec:+d} с |"
                )
            lines.append("")

        for idx in detail_idxs:
            block = _format_item_block(idx, raw_items[idx - 1])
            warn = _item_boundary_warnings(raw_items[idx - 1])
            if warn:
                block.insert(1, f"- **⚠️ границы реплик:** {warn}")
            lines.extend(block)

    return lines


def _item_boundary_warnings(raw: dict) -> str | None:
    """One-line summary of role-boundary issues for an item block."""
    q = (raw.get("interviewer_question") or {}).get("text")
    a = (raw.get("candidate_answer") or {}).get("text")
    fb = (raw.get("interviewer_feedback") or {}).get("text")
    ref = (raw.get("reference_answer") or {}).get("text")
    for detector in (
        lambda: detect_qa_duplicate_prefix(q, a),
        lambda: detect_truncated_question(q),
        lambda: detect_candidate_text_in_question(q),
        lambda: detect_interviewer_pivot_in_answer(a),
        lambda: detect_speaker_mix_in_answer(a),
        lambda: detect_feedback_overlaps_answer(a, fb, ref),
    ):
        msg = detector()
        if msg:
            return msg
    return None


def build_llm_validation_payload(
    blocks: list[ChapterBlock],
    video_path: Path,
    report_md: Path,
) -> str:
    """Plain-text payload for LLM step 5."""
    system = (PROMPT_DIR / "validation_llm_system_prompt.txt").read_text(encoding="utf-8")
    from interview_locale import step5_notes_language_line  # noqa: WPS433

    system = system.replace("{{NOTES_LANGUAGE}}", step5_notes_language_line(loc.lang))
    schema = (PROMPT_DIR / "validation_llm_output_schema.json").read_text(encoding="utf-8")
    parts = [
        "=" * 70,
        "SYSTEM",
        "=" * 70,
        system.strip(),
        "",
        "=" * 70,
        "OUTPUT SCHEMA",
        "=" * 70,
        schema.strip(),
        "",
        "=" * 70,
        "CHAPTERS TO VALIDATE",
        "=" * 70,
        f"video.md: {video_path}",
        "",
    ]
    for block in blocks:
        if block.recognition == "skipped":
            continue
        ch = block.chapter
        parts.append(f"--- CHAPTER `{ch.time_str}` — {ch.title} ---")
        parts.append(f"window: {ch.time_str} .. {block.window_end_str}")
        parts.append(f"recognition_status: {block.recognition} ({len(block.items)} items)")
        parts.append("")
        if not block.items:
            parts.append("(no items extracted)")
        for it, raw in zip(block.items, block.raw_items):
            parts.append(f"ITEM #{it.index}")
            for key in (
                "interviewer_question",
                "candidate_answer",
                "reference_answer",
                "interviewer_feedback",
            ):
                f = raw.get(key) or {}
                parts.append(f"  {key}: time={f.get('time')} text={f.get('text')!r}")
            parts.append(f"  question_topic: {raw.get('question_topic')}")
            parts.append("")
    parts.append(
        f"SAVE JSON: вставьте ответ в конец файла {report_md} "
        f"в секцию «{SEMANTIC_HEADING.strip('# ')}» "
        f"(между {SEMANTIC_SECTION_START} и {SEMANTIC_SECTION_END}, блок ```json)."
    )
    run_cfg = SKILL_DIR / "step1-prepare" / "run_config.json"
    if run_cfg.exists():
        cfg = json.loads(run_cfg.read_text(encoding="utf-8"))
        inf = cfg.get("inference") or {}
        val = cfg.get("validation_inference") or inf
        model = val.get("model")
        temp = val.get("temperature")
        if model is not None or temp is not None:
            parts += [
                "",
                "=" * 70,
                "RUNTIME_HINTS (from step1-prepare/run_config.json)",
                "=" * 70,
                "Required model for step 5 — do not substitute another model without user approval.",
            ]
            if model is not None:
                parts.append(f"Required model: {model}")
            if temp is not None:
                parts.append(f"Required temperature: {temp}")
    return "\n".join(parts)


def validation_report_step5_notice(
    pipeline_log_md: Path,
    report_md: Path,
) -> list[str]:
    """Short pointer in validation-report (prompt in pipeline-log; answer in this file)."""
    return [
        "---",
        "",
        "## Шаг 5 — семантическая проверка (LLM)",
        "",
        f"- **Вход для модели:** `{pipeline_log_md}` — секция `<!-- LLM_INPUT_STEP_5 -->`",
        f"- **Ответ модели (JSON):** в конце **этого файла** — `{SEMANTIC_HEADING}` "
        f"(`{SEMANTIC_SECTION_START}` … `{SEMANTIC_SECTION_END}`)",
        "- После сохранения JSON перезапустите валидатор (тот же `--out`) — появятся строки «Шаг 5».",
        "",
        f"_{SEMANTIC_HEADING} будет заполнена после шага 5._",
        "",
    ]


def prepare_step5_llm_in_pipeline_log(
    blocks: list[ChapterBlock],
    video_path: Path,
    report_md: Path,
    pipeline_log_md: Path,
) -> None:
    """Write step 5 model input into pipeline-log.md."""
    payload = build_llm_validation_payload(blocks, video_path, report_md)
    try:
        from run_manifest import set_llm_input_section  # noqa: WPS433

        set_llm_input_section(
            pipeline_log_md,
            5,
            "Шаг 5 — семантическая валидация глав",
            payload,
        )
    except ImportError:
        pipeline_log_md.parent.mkdir(parents=True, exist_ok=True)
        pipeline_log_md.write_text(payload, encoding="utf-8")


def build_llm_validation_appendix(
    blocks: list[ChapterBlock],
    video_path: Path,
    out_json_path: Path,
) -> list[str]:
    """Deprecated: appendix moved to pipeline-log.md. Kept for API compat — returns []."""
    return []


def llm_json_sidecar_path(validation_report_md: Path) -> Path:
    """Step 5 data source: validation-report.md (legacy *.validation-semantic.json optional)."""
    return validation_report_md
