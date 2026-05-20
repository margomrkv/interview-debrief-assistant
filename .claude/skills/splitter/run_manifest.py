"""Pipeline log: single {basename}.vN.pipeline-log.md (manifest comment + journal + LLM inputs)."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

from artifact_paths import paths_for_run

SKILL_DIR = Path(__file__).resolve().parent
REPO_ROOT = SKILL_DIR.parents[2]

_MANIFEST_RE = re.compile(
    r"<!-- PIPELINE_MANIFEST\s*(?P<json>\{.*?\})\s*-->",
    re.DOTALL,
)
_LLM_SECTION_RE = re.compile(
    r"<!-- LLM_INPUT_STEP_(?P<step>\d+) -->.*?<!-- /LLM_INPUT_STEP_(?P=step) -->",
    re.DOTALL,
)


def _now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S %z")


def _load_config() -> dict:
    p = SKILL_DIR / "step1-prepare" / "run_config.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {}


def _rel(p: Path | str) -> str:
    if isinstance(p, str):
        return p
    try:
        return str(p.relative_to(REPO_ROOT))
    except ValueError:
        return str(p)


def _artifact_paths_for_run(output_dir: Path, basename: str, version: int) -> dict[str, str]:
    arts = paths_for_run(output_dir, basename, version)
    return {
        "json": _rel(arts["json"]),
        "xlsx": _rel(arts["xlsx"]),
        "validation_report_md": _rel(arts["validation_report_md"]),
        "pipeline_log_md": _rel(arts["pipeline_log_md"]),
    }


def llm_input_anchor(step: int) -> str:
    return f"LLM_INPUT_STEP_{step}"


def _parse_pipeline_log_md(text: str) -> tuple[dict | None, str, str]:
    """Return (manifest dict|None, body without manifest/llm, llm_tail markdown)."""
    manifest: dict | None = None
    m = _MANIFEST_RE.search(text)
    if m:
        manifest = json.loads(m.group("json"))
        text = _MANIFEST_RE.sub("", text, count=1).lstrip("\n")
    llm_tail = _extract_llm_sections(text)
    body = text
    if llm_tail:
        idx = body.find("## Входы LLM")
        if idx >= 0:
            body = body[:idx].rstrip()
        else:
            body = _LLM_SECTION_RE.sub("", body).rstrip()
    return manifest, body, llm_tail


def _extract_llm_sections(text: str) -> str:
    if not _LLM_SECTION_RE.search(text):
        idx = text.find("## Входы LLM")
        if idx >= 0:
            return text[idx:].strip() + "\n"
        return ""
    out = ["## Входы LLM (что подавали модели)", ""]
    for m in _LLM_SECTION_RE.finditer(text):
        out.append(m.group(0).strip())
        out.append("")
    return "\n".join(out)


def set_llm_input_section(log_md: Path, step: int, title: str, body: str) -> None:
    """Store full model prompt for a pipeline step inside pipeline-log.md."""
    block = (
        f"<!-- LLM_INPUT_STEP_{step} -->\n\n"
        f"## {title}\n\n"
        f"Модель читает **только этот блок** на шаге {step} (не `video.md`, не другие интервью).\n\n"
        f"```text\n{body.rstrip()}\n```\n\n"
        f"<!-- /LLM_INPUT_STEP_{step} -->\n"
    )
    existing = log_md.read_text(encoding="utf-8") if log_md.exists() else ""
    manifest, main_body, llm_tail = _parse_pipeline_log_md(existing) if existing.strip() else (None, "", "")

    step_re = re.compile(
        rf"<!-- LLM_INPUT_STEP_{step} -->.*?<!-- /LLM_INPUT_STEP_{step} -->",
        re.DOTALL,
    )
    if step_re.search(llm_tail):
        llm_tail = step_re.sub(block, llm_tail, count=1)
    else:
        if "## Входы LLM" not in llm_tail:
            llm_tail = "## Входы LLM (что подавали модели)\n\n" + block
        else:
            llm_tail = llm_tail.rstrip() + "\n\n" + block

    if manifest:
        write_pipeline_log_md(manifest, log_md, llm_tail=llm_tail)
    else:
        stub = main_body or _pipeline_log_header_stub(version=0, basename="")
        log_md.parent.mkdir(parents=True, exist_ok=True)
        log_md.write_text(stub.rstrip() + "\n\n" + llm_tail, encoding="utf-8")


def _pipeline_log_header_stub(*, version: int, basename: str) -> str:
    return (
        f"# Pipeline log v{version}\n\n"
        f"_Журнал прогона `{basename}` — обновляется автоматически; "
        "ниже секции **Входы LLM** заполняются на шагах 2 и 5._\n"
    )


def write_pipeline_log_md(
    run: dict,
    path: Path,
    *,
    llm_tail: str | None = None,
) -> None:
    """Rewrite journal; preserve LLM sections unless llm_tail passed."""
    if llm_tail is None:
        existing = path.read_text(encoding="utf-8") if path.exists() else ""
        _, _, llm_tail = _parse_pipeline_log_md(existing) if existing.strip() else ("", "", "")

    lines = [
        f"# Pipeline log v{run['version']}",
        "",
        "Журнал одного прогона splitter: шаги, модели, артефакты. "
        "**Все промпты для LLM** — в секции [Входы LLM](#входы-llm-что-подавали-модели) ниже "
        "(шаг 2 — извлечение Q&A, шаг 5 — семантическая проверка глав).",
        "",
        f"- **Interview folder:** `{run.get('transcript_folder', '—')}`",
        f"- **Source ID:** `{run.get('source_id', '—')}`",
        f"- **Splitter mode:** `{run.get('splitter_mode', '—')}`",
        f"- **Started:** {run.get('started_at', '—')}",
        f"- **Last updated:** {run.get('updated_at', '—')}",
        "",
        f"Фильтр в IDE: `*{run['basename']}.v{run['version']}*`",
        "",
        "## Models (from run_config.json)",
        "",
    ]
    models = run.get("models") or {}
    for key, spec in models.items():
        if isinstance(spec, dict):
            lines.append(
                f"- **{key}:** `{spec.get('model', '—')}` (temperature {spec.get('temperature', '—')})"
            )
        else:
            lines.append(f"- **{key}:** {spec}")
    lines += [
        "",
        "## Steps",
        "",
        "| # | Step | LLM | Model | In | Out | Duration | Status |",
        "|---|------|-----|-------|----|-----|----------|--------|",
    ]
    for s in run.get("steps", []):
        dur = s.get("duration_sec")
        dur_s = f"{dur}s" if dur is not None else "—"
        ins = "<br>".join(f"`{x}`" for x in (s.get("inputs") or [])[:4])
        outs = "<br>".join(f"`{x}`" for x in (s.get("outputs") or [])[:4])
        lines.append(
            f"| {s.get('id', '—')} | {s.get('name', '—')} | {'yes' if s.get('llm') else 'no'} | "
            f"{s.get('model') or '—'} | {ins or '—'} | {outs or '—'} | {dur_s} | {s.get('status', '—')} |"
        )
    if run.get("notes"):
        lines += ["", "## Notes", "", run["notes"]]
    lines += ["", "## Artifacts (this version)", ""]
    for label, p in (run.get("artifacts") or {}).items():
        lines.append(f"- **{label}:** `{p}`")
    body = "\n".join(lines) + "\n"
    manifest = (
        "<!-- PIPELINE_MANIFEST\n"
        + json.dumps(run, ensure_ascii=False, indent=2)
        + "\n-->\n\n"
    )
    out = manifest + body
    if llm_tail:
        out += "\n" + llm_tail.strip() + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(out, encoding="utf-8")


def init_run(
    *,
    output_dir: Path,
    basename: str,
    version: int,
    transcript_folder: str,
    source_id: str,
    splitter_mode: str,
    inputs: dict[str, str],
) -> dict:
    cfg = _load_config()
    inf = cfg.get("inference") or {}
    val = cfg.get("validation_inference") or inf
    pl_md = paths_for_run(output_dir, basename, version)["pipeline_log_md"]

    run = {
        "version": version,
        "basename": basename,
        "transcript_folder": transcript_folder,
        "source_id": source_id,
        "splitter_mode": splitter_mode,
        "started_at": _now_iso(),
        "updated_at": _now_iso(),
        "models": {
            "step2_qa_extraction": {
                "model": inf.get("model"),
                "temperature": inf.get("temperature"),
            },
            "step5_llm_validation": {
                "model": val.get("model"),
                "temperature": val.get("temperature"),
            },
        },
        "artifacts": _artifact_paths_for_run(output_dir, basename, version),
        "llm_inputs": [],
        "steps": [],
    }
    append_step(
        run,
        step_id=1,
        name="prepare",
        llm=False,
        model=None,
        inputs=inputs,
        outputs={"pipeline_log_md": _rel(pl_md)},
        status="completed",
    )
    return run


def append_step(
    run: dict,
    *,
    step_id: int,
    name: str,
    llm: bool,
    model: str | None,
    inputs: dict[str, str] | list[str] | None = None,
    outputs: dict[str, str] | list[str] | None = None,
    status: str = "completed",
    duration_sec: float | None = None,
    notes: str | None = None,
) -> None:
    def _tolist(x):
        if x is None:
            return []
        if isinstance(x, dict):
            return [_rel(v) for v in x.values()]
        return [_rel(v) for v in x]

    run["steps"] = [s for s in run.get("steps", []) if s.get("id") != step_id]
    run["steps"].append(
        {
            "id": step_id,
            "name": name,
            "llm": llm,
            "model": model,
            "inputs": _tolist(inputs),
            "outputs": _tolist(outputs),
            "status": status,
            "duration_sec": duration_sec,
            "notes": notes,
            "finished_at": _now_iso(),
        }
    )
    run["steps"].sort(key=lambda s: s["id"])
    run["updated_at"] = _now_iso()


def record_llm_input(
    run: dict,
    *,
    step: int,
    name: str,
    model: str | None,
    log_md: Path,
) -> None:
    anchor = llm_input_anchor(step)
    entry = {
        "step": step,
        "name": name,
        "model": model,
        "prompt_location": f"{_rel(log_md)}#{anchor}",
    }
    llm_inputs = [e for e in run.get("llm_inputs", []) if e.get("step") != step]
    llm_inputs.append(entry)
    run["llm_inputs"] = sorted(llm_inputs, key=lambda e: e["step"])


def _resolve_pipeline_log_path(path: Path) -> Path:
    if path.suffix == ".json":
        md = path.with_suffix(".md")
        if md.exists():
            return md
        return md
    return path


def save_run(run: dict, pipeline_log_path: Path) -> None:
    """Persist run manifest + readable journal into pipeline-log.md only."""
    path = _resolve_pipeline_log_path(pipeline_log_path)
    write_pipeline_log_md(run, path)


def load_run(pipeline_log_path: Path) -> dict:
    path = _resolve_pipeline_log_path(pipeline_log_path)
    if path.suffix == ".json" and path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    if not path.exists():
        raise FileNotFoundError(path)
    text = path.read_text(encoding="utf-8")
    manifest, _, _ = _parse_pipeline_log_md(text)
    if manifest:
        return manifest
    raise ValueError(f"No PIPELINE_MANIFEST in {path}")


write_run_md = write_pipeline_log_md
save_pipeline_log = save_run
load_pipeline_log = load_run

_STEP_DISPLAY: dict[int, tuple[str, str]] = {
    1: ("prepare", "1. Подготовка"),
    2: ("qa_extraction", "2. Извлечение Q&A (LLM)"),
    3: ("excel", "3. Excel"),
    4: ("validate_chapters", "4. Валидация по главам"),
    5: ("llm_validation", "5. Семантика глав (LLM)"),
}

_STATUS_ICON = {
    "completed": "✅",
    "failed": "❌",
    "pending": "⏳",
    "running": "▶",
    "skipped": "⏭",
}


def _format_duration_sec(sec: float | None) -> str:
    if sec is None:
        return "—"
    if sec < 1:
        return f"{sec:.2f} с"
    if sec < 60:
        return f"{sec:.0f} с"
    m, s = divmod(int(round(sec)), 60)
    if m < 60:
        return f"{m} мин {s} с" if s else f"{m} мин"
    h, rem = divmod(m, 60)
    return f"{h} ч {rem} мин" if rem else f"{h} ч"


def _wall_clock_span(started: str | None, updated: str | None) -> str | None:
    if not started or not updated or started == "—" or updated == "—":
        return None
    try:
        fmt = "%Y-%m-%d %H:%M:%S"

        def _parse(s: str) -> datetime:
            s = s.strip()
            m = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", s)
            if not m:
                raise ValueError(s)
            return datetime.strptime(m.group(1), fmt)

        t0, t1 = _parse(started), _parse(updated)
        delta = int((t1 - t0).total_seconds())
        if delta < 0:
            return None
        return _format_duration_sec(float(delta))
    except (ValueError, TypeError):
        return None


def build_pipeline_run_summary_for_report(
    run: dict,
    pipeline_log_path: Path,
) -> list[str]:
    """Markdown block for validation-report header: how this interview run completed."""
    ver = run.get("version", "?")
    folder = run.get("transcript_folder", "—")
    log_rel = _rel(pipeline_log_path)
    started = run.get("started_at", "—")
    updated = run.get("updated_at", "—")
    steps = sorted(run.get("steps") or [], key=lambda s: int(s.get("id", 0)))

    sum_sec = sum(
        float(s["duration_sec"])
        for s in steps
        if s.get("duration_sec") is not None
    )
    sum_label = _format_duration_sec(sum_sec) if steps else "—"
    wall = _wall_clock_span(started, updated)

    all_done = all((s.get("status") or "") == "completed" for s in steps if s.get("id"))
    pending = [s for s in steps if (s.get("status") or "") != "completed"]
    if not steps:
        overall = "— нет записей шагов в журнале"
    elif all_done and len(steps) >= 4:
        overall = "✅ все зафиксированные шаги завершены"
    elif pending:
        names = ", ".join(str(s.get("id")) for s in pending)
        overall = f"⚠️ не завершены шаги: {names}"
    else:
        overall = "⚠️ неполный журнал (проверьте pipeline-log)"

    lines = [
        "## Прогон пайплайна\n",
        f"- **Версия:** `v{ver}` · **Интервью:** `{folder}`",
        f"- **Режим:** `{run.get('splitter_mode', '—')}` · **source_id:** `{run.get('source_id', '—')}`",
        f"- **Старт:** {started} · **Обновлено:** {updated}",
    ]
    if wall:
        lines.append(
            f"- **Длительность прогона (стена):** {wall} "
            f"(от старта до последнего обновления журнала)"
        )
    if sum_sec > 0:
        lines.append(
            f"- **Сумма длительностей шагов:** {sum_label} "
            "(только шаги с записанным `duration_sec`; LLM-шаги 2 и 5 — по журналу агента)"
        )
    lines.append(f"- **Итог прогона:** {overall}")
    lines.append(
        f"- **Журнал (технические подробности, промпты LLM, входы/выходы):** "
        f"`{log_rel}` — секции «Steps», «Artifacts», «Входы LLM»"
    )
    lines.append("")
    lines.append("| Шаг | Название | LLM | Модель | Длительность | Статус |")
    lines.append("|-----|----------|-----|--------|--------------|--------|")
    for s in steps:
        sid = int(s.get("id", 0))
        label = _STEP_DISPLAY.get(sid, (s.get("name", "?"), f"{sid}. {s.get('name', '?')}"))[1]
        llm = "да" if s.get("llm") else "нет"
        model = s.get("model") or "—"
        dur = _format_duration_sec(
            float(s["duration_sec"]) if s.get("duration_sec") is not None else None
        )
        st = s.get("status", "—")
        icon = _STATUS_ICON.get(st, st)
        note = f" — {s['notes']}" if s.get("notes") else ""
        lines.append(f"| {sid} | {label} | {llm} | {model} | {dur} | {icon}{note} |")
    lines.append("")
    return lines
