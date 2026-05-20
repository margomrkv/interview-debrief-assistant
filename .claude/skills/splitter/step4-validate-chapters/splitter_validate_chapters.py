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


def group_items_by_question_chapter(
    question_chapters: list[Any],
    items: list[Any],
    tolerance_sec: int,
) -> dict[int, list[int]]:
    """Map chapter.time_sec → sorted item indices (1-based) within ±tolerance of chapter marker."""
    keys = [ch.time_sec for ch in question_chapters]
    out: dict[int, list[int]] = {k: [] for k in keys}
    for it in items:
        if it.q_time_sec is None:
            continue
        best_key: int | None = None
        best_drift = tolerance_sec + 1
        for ch in question_chapters:
            drift = abs(it.q_time_sec - ch.time_sec)
            if drift <= tolerance_sec and drift < best_drift:
                best_drift = drift
                best_key = ch.time_sec
        if best_key is not None:
            out[best_key].append(it.index)
    for key in out:
        out[key].sort(
            key=lambda idx: items[idx - 1].q_time_sec
            if items[idx - 1].q_time_sec is not None
            else 0,
        )
    return out


def chapter_tolerance_stats(
    question_chapters: list[Any],
    assignments: dict[int, list[int]],
) -> dict[str, int | float]:
    """Coverage: question chapters with ≥1 item within tolerance (excluding lead-ins)."""
    q = [ch for ch in question_chapters if not is_lead_in_title(ch.title)]
    recognized = sum(1 for ch in q if assignments.get(ch.time_sec))
    not_rec = len(q) - recognized
    total = len(q)
    pct = recognized / total * 100 if total else 100.0
    return {
        "recognized": recognized,
        "not_recognized": not_rec,
        "total": total,
        "pct": pct,
    }


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
        return "🔗 подводка (следующая вопросная глава)"
    if not ch.is_question:
        return "— исключено"
    if not item_indices:
        return "❌ не распознан"
    if len(item_indices) == 1:
        return "✅ распознан — один Q&A"
    return f"✅ распознано несколько Q&A — {len(item_indices)}"


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


def build_validation_primer(tolerance_sec: int) -> list[str]:
    """What validation checks — orientation block at top of report."""
    return [
        "## Что проверяем\n",
        "Сплиттер **не видел** `video.md` при извлечении. Описание YouTube — **внешний эталон** для проверки результата.\n",
        "| Проверка | Эталон | Результат сплиттера | Когда проблема |",
        "|----------|--------|---------------------|----------------|",
        f"| **Покрытие** | Глава-вопрос в `video.md` (тайм-код + заголовок) | ≥1 item с `interviewer_question.time` в **±{tolerance_sec} с** от маркера | ❌ нет item — пропуск вопроса |",
        "| **Тайм-коды** | Маркер YouTube vs время вопроса в JSON | **Δt** у первого item в группе | вне ±tolerance или нет item |",
        "| **Тема** | Секция из описания видео | `question_topic` item'а | тема не из допустимого списка секции |",
        "| **Смысл** | Заголовок главы YouTube | текст `interviewer_question` | шаг 5 (LLM), опционально |",
        "| **Куда в JSON** | Подводка / разбор / пропуск | поле и item # | см. колонку в таблице и разделы ниже |",
        "| **Доп. Q&A** | — | items без маркера YouTube | **не ошибка**, если уточняющие вопросы внутри темы |",
        "",
        "**Важно:** items **больше**, чем глав на YouTube, — нормально. **Меньше** (пропущенная глава-вопрос) — ошибка сплиттера.\n",
        "",
        "**Подводки (🔗):** отдельный item не нужен — текст должен быть в `interviewer_question` **следующей** вопросной главы.\n",
        "",
        "**Разбор / объяснение:** отдельный item не нужен — речь интервьюера должна быть в `reference_answer` "
        "или `interviewer_feedback` item **предыдущей** задачи (проверяем тайм-код поля).\n",
        "",
        "| Статус в таблице | Значение |",
        "|------------------|----------|",
        "| ✅ | есть извлечённый Q&A в ±tolerance |",
        "| ❌ | вопросная глава без Q&A — см. гипотезу в «Куда в JSON» |",
        "| 🔗 | подводка → следующий `interviewer_question` |",
        "| — | исключено (вступление, разбор, конец) — Coverage не считается |",
        "",
    ]


def build_validation_index_table(
    all_chapters: list[Any],
    assignments: dict[int, list[int]],
    items: list[Any],
    raw_items: list[dict],
    tolerance_sec: int,
    transcript_lines: list[tuple[int, str]] | None = None,
) -> list[str]:
    """All YouTube chapters — compact index with JSON trace column."""
    lines = [
        "## Все главы YouTube\n",
        "Сводка по каждой главе из `video.md`. Колонка **Куда в JSON** — куда сплиттер должен был "
        "положить речь (items, поля). Детали — в разделах «Подводки», «Исключённые», «Не распознанные».\n",
        "| # | YT | Заголовок | Статус | Куда в JSON | Items | Δt (1-й) |",
        "|---|-----|-----------|--------|-------------|-------|----------|",
    ]
    q_num = 0
    for ch in sorted(all_chapters, key=lambda c: c.time_sec):
        lead_in = is_lead_in_title(ch.title)
        if _is_countable_question(ch):
            q_num += 1
            num = str(q_num)
        else:
            num = "—"
        indices = assignments.get(ch.time_sec, []) if _is_countable_question(ch) else []
        status = _status_label(ch, indices, is_lead_in=lead_in)
        if status.startswith("✅"):
            status_short = "✅"
        elif status.startswith("❌"):
            status_short = "❌"
        elif status.startswith("🔗"):
            status_short = "🔗"
        else:
            status_short = "—"
        trace = json_trace_for_chapter(
            ch,
            all_chapters,
            items,
            raw_items,
            assignments,
            indices,
            is_lead_in=lead_in,
            tolerance_sec=tolerance_sec,
            transcript_lines=transcript_lines,
        )
        items_s = ", ".join(f"#{i}" for i in indices) if indices else "—"
        drift_s = "—"
        if indices:
            it = items[indices[0] - 1]
            if it.q_time_sec is not None:
                drift_s = f"{(it.q_time_sec - ch.time_sec):+d}с"
        title = ch.title.replace("|", "/")
        if len(title) > 40:
            title = title[:37] + "…"
        trace = trace.replace("|", "/")
        if len(trace) > 44:
            trace = trace[:41] + "…"
        lines.append(
            f"| {num} | `{ch.time_str}` | {title} | {status_short} | {trace} | {items_s} | {drift_s} |"
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
        "## Подводки (🔗)\n",
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
        if verdict:
            lines.extend(_llm_line(verdict).splitlines())
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
    assignments: dict[int, list[int]],
    items: list[Any],
    tolerance_sec: int,
    transcript_lines: list[tuple[int, str]] | None,
    llm_verdicts: dict[str, LlmChapterVerdict] | None = None,
) -> list[str]:
    llm_verdicts = llm_verdicts or {}
    missed = [
        ch
        for ch in sorted(all_chapters, key=lambda c: c.time_sec)
        if ch.is_question
        and not is_lead_in_title(ch.title)
        and not assignments.get(ch.time_sec)
    ]
    if not missed:
        return []
    lines = [
        "## Не распознанные вопросы (❌)\n",
        f"Вопросные главы YouTube **без** item в ±{tolerance_sec} с от маркера. "
        "Не всегда это «пропуск»: ниже — **гипотеза** (самоответ интервьюера, смещение в соседнюю главу, "
        "реальный пропуск) и что должно быть в JSON.\n",
    ]
    for ch in missed:
        lines.append(f"### `{ch.time_str}` — {ch.title}\n")
        if ch.section:
            lines.append(f"- **Секция YouTube:** {ch.section}")
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
    question_chapters: list[Any],
    items: list[Any],
    raw_items: list[dict],
    assignments: dict[int, list[int]],
    tolerance_sec: int,
    transcript_lines: list[tuple[int, str]] | None = None,
    llm_verdicts: dict[str, LlmChapterVerdict] | None = None,
) -> dict[str, list[str]]:
    """Structured validation sections for a single human-readable report."""
    llm_verdicts = llm_verdicts or {}
    return {
        "primer": build_validation_primer(tolerance_sec),
        "index": build_validation_index_table(
            all_chapters,
            assignments,
            items,
            raw_items,
            tolerance_sec,
            transcript_lines,
        ),
        "excluded": build_excluded_chapters_section(
            all_chapters, raw_items, transcript_lines
        ),
        "lead_ins": build_lead_in_chapters_section(
            all_chapters, items, raw_items, assignments, transcript_lines
        ),
        "recognized": build_recognized_questions_section(
            all_chapters, items, raw_items, assignments, llm_verdicts
        ),
        "unrecognized": build_unrecognized_questions_section(
            all_chapters,
            assignments,
            items,
            tolerance_sec,
            transcript_lines,
            llm_verdicts,
        ),
    }


def build_master_validation_section(
    all_chapters: list[Any],
    question_chapters: list[Any],
    items: list[Any],
    raw_items: list[dict],
    assignments: dict[int, list[int]],
    tolerance_sec: int,
    transcript_lines: list[tuple[int, str]] | None = None,
    llm_verdicts: dict[str, LlmChapterVerdict] | None = None,
) -> list[str]:
    """Flatten validation body sections (legacy helper)."""
    body = build_validation_body(
        all_chapters,
        question_chapters,
        items,
        raw_items,
        assignments,
        tolerance_sec,
        transcript_lines,
        llm_verdicts,
    )
    out: list[str] = []
    for key in ("primer", "index", "excluded", "lead_ins", "unrecognized", "recognized"):
        if body.get(key):
            out.extend(body[key])
    return out


def build_transcript_gaps_section(
    gaps: list[dict[str, Any]],
) -> list[str]:
    lines = [
        "## Фрагменты транскрипта без Q&A в JSON\n",
        "Интервалы `timecodes.txt`, не попавшие в span ни одного item сплиттера "
        "(от `interviewer_question.time` до конца ответа / reference / feedback / следующего вопроса). "
        "Проверьте, не пропущен ли вопрос или это служебная речь.\n",
    ]
    if not gaps:
        lines.append("_Крупных непокрытых фрагментов не найдено (порог: ≥25 с, ≥4 строк с тайм-кодом)._\n")
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
    lines.append(_field_md("Вопрос", raw.get("interviewer_question")))
    lines.append(_field_md("Ответ кандидата", raw.get("candidate_answer")))
    lines.append(_field_md("Reference answer", raw.get("reference_answer")))
    lines.append(_field_md("Interviewer feedback", raw.get("interviewer_feedback")))
    lines.append(f"- **Метки:** {meta_s}")
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


def _llm_line(verdict: LlmChapterVerdict | None) -> str:
    if verdict is None:
        return "- **LLM (смысл и тайм-коды):** _не проверялось_ — запустите шаг LLM-валидации\n"
    t_icon = "✅" if verdict.time_alignment_ok else "❌"
    c_icon = "✅" if verdict.content_alignment_ok else "❌"
    lines = [
        f"- **LLM — тайм-коды:** {t_icon} {'ок' if verdict.time_alignment_ok else 'проблема'}",
        f"- **LLM — содержание:** {c_icon} {'ок' if verdict.content_alignment_ok else 'проблема'}",
    ]
    if verdict.notes.strip():
        lines.append(f"- **LLM — комментарий:** {verdict.notes.strip()}")
    lines.append("")
    return "\n".join(lines) + "\n"


def load_llm_verdicts(path: Path | None) -> dict[str, LlmChapterVerdict]:
    if not path or not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
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


def build_youtube_chapters_section(
    blocks: list[ChapterBlock],
    llm_verdicts: dict[str, LlmChapterVerdict] | None = None,
    transcript_lines: list[tuple[int, str]] | None = None,
) -> list[str]:
    llm_verdicts = llm_verdicts or {}
    lines = [
        "## Главы YouTube\n",
        "Список глав из `video.md` (## Chapters). Для каждой главы — статус распознавания "
        "и извлечённые пары Q&A (если есть).\n",
        "| Статус | Значение |",
        "|--------|----------|",
        "| ❌ не распознан | в окне главы нет ни одного item — **грубая ошибка** |",
        "| ✅ один Q&A | ровно один item в окне |",
        "| ✅ несколько Q&A | два и более items в окне одной главы |",
        "| — исключено | служебная глава (вступление, разбор, …) |",
        "",
    ]
    q_num = 0
    for block in blocks:
        ch = block.chapter
        if block.recognition != "skipped":
            q_num += 1
            heading = f"### {q_num}. `{ch.time_str}` — {ch.title}"
        else:
            heading = f"### `{ch.time_str}` — {ch.title}"
        lines.append(heading)
        lines.append("")
        lines.append(f"**Статус:** {_recognition_label(block.recognition, len(block.items))}")
        lines.append("")
        if block.recognition == "skipped" and transcript_lines is not None:
            excerpt = transcript_excerpt(
                transcript_lines,
                ch.time_sec,
                block.window_end_sec,
            )
            lines.append("**Цитата из транскрипта** (интервал главы, для проверки исключения):")
            lines.append("")
            lines.append("```text")
            lines.append(excerpt)
            lines.append("```")
            lines.append("")
        if block.recognition != "skipped":
            lines.append(
                f"- **Окно главы:** `{ch.time_str}` — `{block.window_end_str}` "
                f"(item попадает сюда по `interviewer_question.time`)"
            )
            lines.append("")
            lines.extend(_llm_line(llm_verdicts.get(ch.time_str)).splitlines())
            if block.items:
                lines.append("")
        for it, raw in zip(block.items, block.raw_items):
            lines.extend(_format_item_block(it.index, raw))
        if block.recognition == "not_recognized":
            if transcript_lines is not None:
                excerpt = transcript_excerpt(
                    transcript_lines,
                    ch.time_sec,
                    block.window_end_sec,
                )
                lines.append("**Цитата из транскрипта** (в окне главы нет items — проверьте пропуск):")
                lines.append("")
                lines.append("```text")
                lines.append(excerpt)
                lines.append("```")
                lines.append("")
            lines.append(
                "> Проверьте транскрипт в этом интервале: возможно, сплиттер пропустил вопрос "
                "или глава YouTube — постановка/переход (добавьте префикс в `EXPLANATION_PREFIXES`).\n"
            )
    return lines


def build_llm_validation_payload(
    blocks: list[ChapterBlock],
    video_path: Path,
    out_json_path: Path,
) -> str:
    """Plain-text payload for LLM step 5 (embedded in the single validation .md)."""
    system = (PROMPT_DIR / "validation_llm_system_prompt.txt").read_text(encoding="utf-8")
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
    parts.append(f"SAVE JSON TO: {out_json_path}")
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


def build_llm_validation_appendix(
    blocks: list[ChapterBlock],
    video_path: Path,
    out_json_path: Path,
) -> list[str]:
    """Markdown appendix in the same *.qa-split.validation.vN.md (not a second report file)."""
    payload = build_llm_validation_payload(blocks, video_path, out_json_path)
    return [
        "---",
        "",
        "## Приложение: LLM-валидация (шаг 5)",
        "",
        "Часть **этого же** файла отчёта. Отдельный `*.validation.llm-input*.txt` не создаётся.",
        f"Сохраните ответ модели в: `{out_json_path}`",
        "Затем перезапустите валидатор с `--llm-json` — строки LLM появятся в таблице выше.",
        "",
        "```text",
        payload,
        "```",
        "",
    ]


def llm_json_sidecar_path(validation_md: Path) -> Path:
    """JSON path for step 5 (machine artifact merged back into the .md report)."""
    import re
    import sys

    parent = validation_md.parent
    skill_dir = Path(__file__).resolve().parents[1]
    if str(skill_dir) not in sys.path:
        sys.path.insert(0, str(skill_dir))
    try:
        from artifact_paths import validation_llm_json_from_validation_md

        return validation_llm_json_from_validation_md(validation_md)
    except ImportError:
        pass
    m = re.match(r"^(?P<base>.+)\.qa-split\.validation\.v(?P<n>\d+)\.md$", validation_md.name)
    if m:
        b, n = m.group("base"), m.group("n")
        return parent / f"{b}.qa-split.validation.llm.v{n}.json"
    return parent / f"{validation_md.stem}.llm.json"
