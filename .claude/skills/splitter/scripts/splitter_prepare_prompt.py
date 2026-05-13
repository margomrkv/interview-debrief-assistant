#!/usr/bin/env python3
"""
splitter_prepare_prompt.py (lives under .claude/skills/splitter/scripts/)

Writes per-run artifacts:
- splitter_output/<base>.user_prompt.txt — вход + схема (история / user message).
- splitter_output/<base>.splitter_llm_input.txt — system + user + схема (один файл для модели / subagent).

Режим: video.md в папке интервью → mock_assisted_split, иначе raw_split.
Транскрипт mock: timecodes.txt предпочтительно, иначе transcript.txt.

Выход JSON/xlsx/validation: splitter_output/ в корне репозитория (не внутри skill).
Имена: `<source_id>.splitter.v<N>.<mock|raw>.{json|xlsx|validation.md|user_prompt.txt|splitter_llm_input.txt|…}`.
Версия `vN`: если `--version` не задан, скрипт смотрит все файлы в splitter_output с этим `source_id` и режимом (`mock` или `raw`), берёт максимальный уже занятый `N` и ставит **следующий**; если таких файлов нет — **v1**.

В каждый user-файл добавляется RUNTIME_HINTS из `config/splitter_run_config.json` (`inference.*`) — для оператора и воспроизводимости; скрипты не дергают API.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# __file__ = .../<repo>/.claude/skills/splitter/scripts/splitter_prepare_prompt.py
SKILL_DIR = Path(__file__).resolve().parent.parent
# SKILL_DIR = …/splitter → parents[2] = <repo> (parents[0]=skills, [1]=.claude)
REPO_ROOT = SKILL_DIR.parents[2]

# Printed in user bundle — path from repo root
SKILL_SH = ".claude/skills/splitter"


def _load_config() -> dict:
    p = SKILL_DIR / "config" / "splitter_run_config.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {}


def _resolve_artifact(path_str: str) -> Path:
    p = Path(path_str)
    if p.is_absolute():
        return p
    return SKILL_DIR / p


def _infer_source_id(folder: Path) -> str:
    name = folder.name
    name = re.sub(r"^mock-", "", name)
    name = re.sub(r"(\d{4})-(\d{2})-(\d{2})$", r"\1\2\3", name)
    name = name.replace("-", "_")
    return name


def _next_version(output_dir: Path, source_id: str, mode_tag: str) -> int:
    """Next version index for this source_id and mode (mock | raw).

    Scans splitter_output for any file matching:
      <source_id>.splitter.v*.<mode_tag>.*
    (json, xlsx, validation.md, user_prompt.txt, splitter_llm_input.txt, etc.)
    If none exist, returns 1. Otherwise returns max(found N) + 1.
    """
    pattern = f"{source_id}.splitter.v*.{mode_tag}.*"
    used: set[int] = set()
    for f in output_dir.glob(pattern):
        m = re.search(r"\.splitter\.v(\d+)\.", f.name)
        if m:
            used.add(int(m.group(1)))
    if not used:
        return 1
    return max(used) + 1


def main() -> None:
    config = _load_config()

    parser = argparse.ArgumentParser(
        description="Prepare splitter user prompt + splitter_llm_input (system+user+schema) for one interview folder."
    )
    parser.add_argument("--folder", required=True, help="Path to interview folder (relative to repo root)")
    parser.add_argument(
        "--mode", choices=["raw_split", "mock_assisted_split"], default=None,
        help="Default: mock if video.md exists, else raw.",
    )
    parser.add_argument("--source-id", default=None)
    parser.add_argument(
        "--version",
        type=int,
        default=None,
        help="Force vN. If omitted: next version from splitter_output/<source_id>.splitter.v*.<mock|raw>.* (max N + 1, or 1 if none).",
    )
    parser.add_argument("--out-user-prompt", default=None)
    parser.add_argument("--transcript-file", default=None)
    parser.add_argument("--source-id-suffix", default=None)
    args = parser.parse_args()

    folder = REPO_ROOT / args.folder
    if not folder.exists():
        print(f"ERROR: folder not found: {folder}", file=sys.stderr)
        sys.exit(1)

    has_video_md = (folder / "video.md").exists()
    has_timecodes = (folder / "timecodes.txt").exists()
    has_transcript = (folder / "transcript.txt").exists()

    mode = args.mode
    if mode is None:
        mode = "mock_assisted_split" if has_video_md else "raw_split"

    source_id = args.source_id or (_infer_source_id(folder) + (args.source_id_suffix or ""))
    mode_tag = "mock" if mode == "mock_assisted_split" else "raw"
    output_dir = REPO_ROOT / "splitter_output"
    output_dir.mkdir(parents=True, exist_ok=True)
    version = args.version or _next_version(output_dir, source_id, mode_tag)

    base_name = f"{source_id}.splitter.v{version}.{mode_tag}"
    out_json = output_dir / f"{base_name}.json"
    out_xlsx = output_dir / f"{base_name}.xlsx"
    out_validation = output_dir / f"{base_name}.validation.md"
    out_user = Path(args.out_user_prompt) if args.out_user_prompt else output_dir / f"{base_name}.user_prompt.txt"
    out_llm_input = output_dir / f"{base_name}.splitter_llm_input.txt"

    sys_prompt_path = _resolve_artifact(
        config.get("system_prompt", "prompt,output_schema/splitter_system_prompt.txt")
    )
    schema_path = _resolve_artifact(
        config.get("schema", "prompt,output_schema/splitter_output_schema.json")
    )

    def read(p: Path) -> str:
        if not p.exists():
            print(f"WARNING: file not found: {p}", file=sys.stderr)
            return ""
        return p.read_text(encoding="utf-8")

    system_prompt = read(sys_prompt_path)
    schema_text = read(schema_path)

    if args.transcript_file:
        tf = Path(args.transcript_file)
        if not tf.is_absolute():
            tf = REPO_ROOT / tf
        if not tf.exists():
            print(f"ERROR: --transcript-file not found: {tf}", file=sys.stderr)
            sys.exit(1)
        transcript_text = tf.read_text(encoding="utf-8")
        transcript_label = "TIMECODES_TXT" if mode == "mock_assisted_split" else "TRANSCRIPT_TXT"
    elif mode == "mock_assisted_split":
        if has_timecodes:
            transcript_text = read(folder / "timecodes.txt")
            transcript_label = "TIMECODES_TXT"
        elif has_transcript:
            transcript_text = read(folder / "transcript.txt")
            transcript_label = "TRANSCRIPT_TXT"
        else:
            print("ERROR: mock mode needs timecodes.txt or transcript.txt", file=sys.stderr)
            sys.exit(1)
    else:
        if not has_transcript:
            print("ERROR: raw_split needs transcript.txt in folder", file=sys.stderr)
            sys.exit(1)
        transcript_text = read(folder / "transcript.txt")
        transcript_label = "TRANSCRIPT_TXT"

    sidecars: list[tuple[str, str]] = []
    if mode == "mock_assisted_split":
        fp = folder / "feedback.md"
        if fp.exists():
            sidecars.append(("FEEDBACK_MD", read(fp)))

    try:
        sys_prompt_rel = sys_prompt_path.relative_to(REPO_ROOT)
    except ValueError:
        sys_prompt_rel = sys_prompt_path

    user_blocks = [
        "Task: Q&A extraction for the transcript below. Match the system prompt used in this run",
        f"(repository file: {sys_prompt_rel}).",
        "Return a single JSON object only (no markdown fences).",
        "",
        "=" * 70,
        "OUTPUT SCHEMA (contract)",
        "=" * 70,
        schema_text.strip(),
        "",
        "=" * 70,
        "INPUT DATA",
        "=" * 70,
        f"SOURCE_ID: {source_id}",
        f"SPLITTER_MODE: {mode}",
        f"INTERVIEW_FOLDER: {args.folder}",
        f"PRIMARY_TRANSCRIPT ({transcript_label}):",
        transcript_text.strip(),
    ]
    for label, content in sidecars:
        user_blocks.append("")
        user_blocks.append(f"{label}:")
        user_blocks.append(content.strip())

    # Echo inference hints from config into every run artifact (for reproducibility; Python does not call APIs).
    inf = config.get("inference")
    if isinstance(inf, dict):
        model, temp, mt = inf.get("model"), inf.get("temperature"), inf.get("max_tokens")
    else:
        model = config.get("model")
        temp = config.get("temperature")
        mt = config.get("max_tokens")
    if any(v is not None for v in (model, temp, mt)):
        user_blocks += [
            "",
            "=" * 70,
            "RUNTIME_HINTS (from config/splitter_run_config.json)",
            "=" * 70,
            "These fields are for the human operator or chat/Cloud client. splitter_prepare_prompt.py does not call any LLM API.",
        ]
        if model is not None:
            user_blocks.append(f"Suggested model: {model}")
        if temp is not None:
            user_blocks.append(f"Suggested temperature: {temp}")
        if mt is not None:
            user_blocks.append(f"Suggested max_tokens: {mt}")
        user_blocks.append("")

    py = f"python3 {SKILL_SH}/scripts/splitter_json_to_excel.py"
    py_val = f"python3 {SKILL_SH}/scripts/splitter_validate_video.py"

    user_blocks += [
        "",
        "=" * 70,
        "OUTPUT PATHS (post-processing)",
        "=" * 70,
        f"Save JSON to: {out_json.relative_to(REPO_ROOT)}",
        "",
        "Then:",
        f"  {py} {out_json.relative_to(REPO_ROOT)} --out {out_xlsx.relative_to(REPO_ROOT)}",
        "",
    ]
    if has_video_md:
        sec_example = f"{SKILL_SH}/config/section_topic_map.example.json"
        user_blocks += [
            "Validation (video.md offline only — never paste into the model):",
            f"  {py_val} \\",
            f"    --splitter {out_json.relative_to(REPO_ROOT)} \\",
            f"    --video {args.folder}/video.md \\",
            f"    --tolerance 120 \\",
            f"    --out {out_validation.relative_to(REPO_ROOT)}",
            "",
            "Optional: pass --section-config <path.json> for section/topic checks (see template):",
            f"  {sec_example}",
            "",
        ]
    else:
        user_blocks += [
            "No video.md in folder — skip splitter_validate_video.py for this interview.",
            "",
        ]

    user_text = "\n".join(user_blocks)

    bundle_sections = [
        "=" * 70,
        f"SYSTEM PROMPT ({sys_prompt_rel})",
        "=" * 70,
        system_prompt.strip(),
        "",
        "=" * 70,
        "USER PROMPT (variable input + schema)",
        "=" * 70,
        user_text.strip(),
    ]
    combined_llm_input = "\n".join(bundle_sections)

    out_user.parent.mkdir(parents=True, exist_ok=True)
    out_user.write_text(user_text, encoding="utf-8")
    out_llm_input.write_text(combined_llm_input, encoding="utf-8")

    print(f"User prompt:   {out_user.relative_to(REPO_ROOT)}")
    print(f"LLM input:     {out_llm_input.relative_to(REPO_ROOT)}")
    print(f"Output JSON:   {out_json.relative_to(REPO_ROOT)}")
    print(f"Output Excel:  {out_xlsx.relative_to(REPO_ROOT)}")
    if has_video_md:
        print(f"Validation:    {out_validation.relative_to(REPO_ROOT)}")
    print(f"Mode:          {mode}  (auto: video.md={'yes' if has_video_md else 'no'})")
    print(f"Source ID:     {source_id}")
    print(f"Version:       v{version}")
    print()
    print(f"Skill (orchestration): {SKILL_SH}/SKILL.md")
    print("Per-run user prompts (.user_prompt.txt) and LLM input (.splitter_llm_input.txt) live under splitter_output/.")
    print(f"Cloud / subagent: use {out_llm_input.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
