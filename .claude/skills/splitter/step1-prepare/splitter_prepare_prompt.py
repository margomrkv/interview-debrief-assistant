#!/usr/bin/env python3
"""
splitter_prepare_prompt.py — step 1 (prepare), lives in step1-prepare/

Writes per-run artifacts under `splitter_output/` (mirrors `transcripts/` tree):
- `splitter_output/<mock|real>-interviews/<publisher>/<basename>/` — basename **without** mock-/real- prefix
- `.../<basename>.qa-split.llm-input.v<N>.txt` — system + user + schema (subagent input)

Режим: video.md в папке интервью → split_and_validate, иначе split_only.
Транскрипт mock: timecodes.txt предпочтительно, иначе transcript.txt.

Выход JSON/xlsx/validation: same interview folder under `splitter_output/`.
Имена: `{basename}.v<N>.<artifact>.{ext}` — см. `splitter_output/README.md` и `artifact_paths.py`.
Версия `vN`: если `--version` не задан — max среди `{basename}.qa-split.v*.json` в папке + 1 (или 1).

В каждый llm-input добавляется RUNTIME_HINTS из `step1-prepare/run_config.json` (`inference.*`); скрипт API не вызывает.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

STEP_DIR = Path(__file__).resolve().parent
SKILL_DIR = STEP_DIR.parent
REPO_ROOT = SKILL_DIR.parents[2]
sys.path.insert(0, str(SKILL_DIR))

from artifact_paths import next_version, paths_for_run  # noqa: E402

SKILL_SH = ".claude/skills/splitter"

SPLIT_ONLY = "split_only"
SPLIT_AND_VALIDATE = "split_and_validate"
_MODE_ALIASES = {
    "raw_split": SPLIT_ONLY,
    "mock_assisted_split": SPLIT_AND_VALIDATE,
    SPLIT_ONLY: SPLIT_ONLY,
    SPLIT_AND_VALIDATE: SPLIT_AND_VALIDATE,
}


def _normalize_mode(mode: str) -> str:
    if mode not in _MODE_ALIASES:
        raise ValueError(f"unknown splitter mode: {mode}")
    return _MODE_ALIASES[mode]


def _load_config() -> dict:
    p = STEP_DIR / "run_config.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {}


def _resolve_artifact(path_str: str) -> Path:
    p = Path(path_str)
    if p.is_absolute():
        return p
    return STEP_DIR / p


_KIND_PREFIXES = ("mock-", "real-")


def _strip_kind_prefix(name: str) -> str:
    """Remove mock-/real- from leaf names in splitter_output (kind is in parent folder)."""
    for prefix in _KIND_PREFIXES:
        if name.startswith(prefix):
            return name[len(prefix) :]
    return name


def _artifact_basename(folder: Path) -> str:
    """File/folder basename under splitter_output (no mock-/real- prefix)."""
    return _strip_kind_prefix(folder.name)


def _source_id_from_slug(slug: str) -> str:
    return slug.replace("-", "_")


def _output_dir_for_interview(folder: Path) -> Path:
    transcripts = REPO_ROOT / "transcripts"
    try:
        rel = folder.relative_to(transcripts)
        parts = list(rel.parts)
        if parts:
            parts[-1] = _strip_kind_prefix(parts[-1])
        rel = Path(*parts)
    except ValueError:
        kind = "mock-interviews" if folder.name.startswith("mock-") else "real-interviews"
        rel = Path(kind) / "unknown" / _artifact_basename(folder)
    return REPO_ROOT / "splitter_output" / rel


def main() -> None:
    config = _load_config()

    parser = argparse.ArgumentParser(
        description="Prepare splitter user prompt + splitter_llm_input (system+user+schema) for one interview folder."
    )
    parser.add_argument("--folder", required=True, help="Path to interview folder (relative to repo root)")
    parser.add_argument(
        "--mode",
        choices=list(_MODE_ALIASES.keys()),
        default=None,
        help="Default: split_and_validate if video.md exists, else split_only.",
    )
    parser.add_argument("--source-id", default=None)
    parser.add_argument(
        "--version",
        type=int,
        default=None,
        help="Force vN. If omitted: next version from existing *.v*.qa-split.json (or legacy *.qa-split.v*.json).",
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

    if args.mode is not None:
        mode = _normalize_mode(args.mode)
    else:
        mode = SPLIT_AND_VALIDATE if has_video_md else SPLIT_ONLY

    basename = _artifact_basename(folder)
    source_id = args.source_id or (
        _source_id_from_slug(folder.name) + (args.source_id_suffix or "")
    )
    output_dir = _output_dir_for_interview(folder)
    output_dir.mkdir(parents=True, exist_ok=True)
    version = args.version or next_version(output_dir, basename)
    artifacts = paths_for_run(output_dir, basename, version)
    out_json = artifacts["json"]
    out_xlsx = artifacts["xlsx"]
    out_validation = artifacts["validation_md"]
    out_user = (
        Path(args.out_user_prompt)
        if args.out_user_prompt
        else artifacts["user_prompt"]
    )
    out_llm_input = artifacts["llm_input"]
    out_run_json = artifacts["run_json"]

    sys_prompt_path = _resolve_artifact(
        config.get("system_prompt", "splitter_system_prompt.txt")
    )
    schema_path = _resolve_artifact(
        config.get("schema", "splitter_output_schema.json")
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
        transcript_label = (
            "TIMECODES_TXT"
            if "timecodes" in tf.name.lower()
            else "TRANSCRIPT_TXT"
        )
    elif has_timecodes:
        transcript_text = read(folder / "timecodes.txt")
        transcript_label = "TIMECODES_TXT"
    elif has_transcript:
        transcript_text = read(folder / "transcript.txt")
        transcript_label = "TRANSCRIPT_TXT"
    else:
        print("ERROR: need timecodes.txt or transcript.txt in folder", file=sys.stderr)
        sys.exit(1)

    sidecars: list[tuple[str, str]] = []
    if has_video_md:
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
            "RUNTIME_HINTS (from step1-prepare/run_config.json)",
            "=" * 70,
            "Required for step 2 (Q&A extraction). splitter_prepare_prompt.py does not call any LLM API.",
            "Do NOT substitute another model (e.g. GPT) unless the user explicitly overrides.",
        ]
        if model is not None:
            user_blocks.append(f"Required model: {model}")
        if temp is not None:
            user_blocks.append(f"Suggested temperature: {temp}")
        if mt is not None:
            user_blocks.append(f"Suggested max_tokens: {mt}")
        user_blocks.append("")

    py_post = "scripts/splitter_post.sh"
    py = f"python3 {SKILL_SH}/step3-excel/splitter_json_to_excel.py"
    py_val = f"python3 {SKILL_SH}/step4-validate-chapters/splitter_validate_video.py"

    user_blocks += [
        "",
        "=" * 70,
        "OUTPUT PATHS (post-processing)",
        "=" * 70,
        f"Save JSON to: {out_json.relative_to(REPO_ROOT)}",
        "",
        "Then (preferred — no LLM):",
        f"  {py_post} {out_json.relative_to(REPO_ROOT)} \\",
        f"    --video {args.folder}/video.md",
        "",
        "Or manually:",
        f"  {py} {out_json.relative_to(REPO_ROOT)} --out {out_xlsx.relative_to(REPO_ROOT)}",
        "",
    ]
    if has_video_md:
        sec_example = f"{SKILL_SH}/step4-validate-chapters/section_topic_map.karpov_mock.json"
        user_blocks += [
            "Validation (video.md offline only — never paste into the model):",
            f"  {py_val} \\",
            f"    --splitter {out_json.relative_to(REPO_ROOT)} \\",
            f"    --video {args.folder}/video.md \\",
            f"    --tolerance 120 \\",
            f"    --out {out_validation.relative_to(REPO_ROOT)}",
            "",
            "Sections: auto-parsed from `Секция «…»` in video.md Description.",
            "Optional topic_map override:",
            f"  --section-config {sec_example}",
            "",
            "Full procedure: .claude/skills/splitter/SKILL.md",
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

    out_llm_input.parent.mkdir(parents=True, exist_ok=True)
    out_llm_input.write_text(combined_llm_input, encoding="utf-8")
    if args.out_user_prompt:
        out_user.parent.mkdir(parents=True, exist_ok=True)
        out_user.write_text(user_text, encoding="utf-8")
        print(f"User prompt:   {out_user.relative_to(REPO_ROOT)}")

    from run_manifest import init_run, save_run  # noqa: E402

    transcript_input = (
        f"{args.folder}/timecodes.txt" if has_timecodes else f"{args.folder}/transcript.txt"
    )
    run = init_run(
        output_dir=output_dir,
        basename=basename,
        version=version,
        transcript_folder=args.folder,
        source_id=source_id,
        splitter_mode=mode,
        inputs={
            "transcript": transcript_input,
            "system_prompt": str(sys_prompt_rel),
            "schema": str(schema_path.relative_to(REPO_ROOT) if schema_path.is_relative_to(REPO_ROOT) else schema_path),
        },
    )
    save_run(run, out_run_json)

    print(f"Run log:       {out_run_json.relative_to(REPO_ROOT)}")
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
    print("Per-run artifacts live under splitter_output/ (see splitter_output/README.md).")
    print(f"Cloud / subagent: use {out_llm_input.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
