"""Splitter run protocol: {basename}.vN.run.json + human-readable .run.md"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from artifact_paths import paths_for_run

SKILL_DIR = Path(__file__).resolve().parent
REPO_ROOT = SKILL_DIR.parents[2]


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


def write_run_md(run: dict, path: Path) -> None:
    lines = [
        f"# Splitter run v{run['version']}",
        "",
        f"- **Interview folder:** `{run.get('transcript_folder', '—')}`",
        f"- **Source ID:** `{run.get('source_id', '—')}`",
        f"- **Splitter mode:** `{run.get('splitter_mode', '—')}`",
        f"- **Started:** {run.get('started_at', '—')}",
        f"- **Last updated:** {run.get('updated_at', '—')}",
        "",
        f"Фильтр в Finder/IDE: `*{run['basename']}.v{run['version']}*` — все файлы одного прогона.",
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
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


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
    artifacts = paths_for_run(output_dir, basename, version)
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
        "artifacts": {k: _rel(v) for k, v in artifacts.items()},
        "steps": [],
    }
    append_step(
        run,
        step_id=1,
        name="prepare",
        llm=False,
        model=None,
        inputs=inputs,
        outputs={
            "llm_input": _rel(artifacts["llm_input"]),
            "user_prompt": _rel(artifacts["user_prompt"]),
        },
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


def save_run(run: dict, run_json_path: Path) -> None:
    run_json_path.parent.mkdir(parents=True, exist_ok=True)
    run_json_path.write_text(json.dumps(run, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_run_md(run, run_json_path.with_suffix(".md"))


def load_run(run_json_path: Path) -> dict:
    return json.loads(run_json_path.read_text(encoding="utf-8"))
