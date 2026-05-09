#!/usr/bin/env python3
"""
prepare_prompt.py

Собирает все входные файлы для splitter в один текстовый файл.
Это позволяет Claude Code прочитать один файл вместо 5–7,
сокращая количество tool-вызовов и время на накладные расходы.

Использование:
  python3 labeling/prepare_prompt.py \
    --folder transcripts/mock-avito-product-analyst-middle-2024-04-04

  python3 labeling/prepare_prompt.py \
    --folder transcripts/.../junior-data-scientist-... \
    --mode raw_split \
    --version 5

Выходной файл: labeling/data/<source_id>.prompt.txt
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


CONFIG_PATH = "labeling/config/splitter_run_config.json"


def _load_config(root: Path) -> dict:
    p = root / CONFIG_PATH
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {}


def _infer_source_id(folder: Path) -> str:
    """Derive source_id from folder name."""
    name = folder.name
    # Remove common prefixes
    name = re.sub(r"^mock-", "", name)
    # Replace hyphens, collapse date part (YYYY-MM-DD → YYYYMMDD)
    name = re.sub(r"(\d{4})-(\d{2})-(\d{2})$", r"\1\2\3", name)
    name = name.replace("-", "_")
    return name


def _next_version(data_dir: Path, source_id: str, mode_tag: str) -> int:
    existing = list(data_dir.glob(f"{source_id}.splitter.v*.{mode_tag}.json"))
    used = set()
    for f in existing:
        m = re.search(r"\.v(\d+)\.", f.name)
        if m:
            used.add(int(m.group(1)))
    v = 1
    while v in used:
        v += 1
    return v


def main() -> None:
    root = Path.cwd()
    config = _load_config(root)

    parser = argparse.ArgumentParser(
        description="Prepare a single prompt file for Claude Code splitter run."
    )
    parser.add_argument(
        "--folder", required=True,
        help="Path to interview folder (relative to repo root)"
    )
    parser.add_argument(
        "--mode", choices=["raw_split", "mock_assisted_split"], default=None,
        help="Splitter mode. Auto-detected if omitted."
    )
    parser.add_argument(
        "--source-id", default=None,
        help="Source ID for output JSON. Auto-derived from folder name if omitted."
    )
    parser.add_argument(
        "--version", type=int, default=None,
        help="Version number for output files. Auto-detected if omitted."
    )
    parser.add_argument(
        "--out", default=None,
        help="Output prompt file path. Default: labeling/data/<source_id>.prompt.txt"
    )
    parser.add_argument(
        "--transcript-file", default=None,
        help="Use this file as transcript instead of folder/timecodes.txt or folder/transcript.txt (useful for split multi-candidate transcripts)"
    )
    parser.add_argument(
        "--source-id-suffix", default=None,
        help="Append suffix to auto-derived source_id (e.g. '_pasha' for multi-candidate splits)"
    )
    args = parser.parse_args()

    folder = root / args.folder
    if not folder.exists():
        print(f"ERROR: folder not found: {folder}", file=sys.stderr)
        sys.exit(1)

    # Detect mode
    has_timecodes = (folder / "timecodes.txt").exists()
    has_transcript = (folder / "transcript.txt").exists()
    mode = args.mode or ("mock_assisted_split" if has_timecodes else "raw_split")

    # Source ID and version
    source_id = args.source_id or (_infer_source_id(folder) + (args.source_id_suffix or ""))
    mode_tag = "mock" if mode == "mock_assisted_split" else "raw"
    data_dir = root / "labeling" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    version = args.version or _next_version(data_dir, source_id, mode_tag)

    # Output paths
    base_name = f"{source_id}.splitter.v{version}.{mode_tag}"
    out_prompt = Path(args.out) if args.out else data_dir / f"{source_id}.prompt.txt"
    out_json = data_dir / f"{base_name}.json"
    out_xlsx = data_dir / f"{base_name}.xlsx"
    out_validation = data_dir / f"{base_name}.validation.md"

    # Read prompts
    sys_prompt_path = root / config.get("system_prompt", "labeling/prompts/system_prompt_v2.txt")
    if mode == "mock_assisted_split":
        user_prompt_path = root / config.get(
            "user_prompt_mock_assisted_split",
            "labeling/prompts/user_prompt_template_mock_assisted_v2.txt"
        )
    else:
        user_prompt_path = root / config.get(
            "user_prompt_raw_split",
            "labeling/prompts/user_prompt_template_v2.txt"
        )
    schema_path = root / config.get("schema", "labeling/prompts/splitter_output_schema_v1.json")

    def read(p: Path) -> str:
        if not p.exists():
            print(f"WARNING: file not found: {p}", file=sys.stderr)
            return ""
        return p.read_text(encoding="utf-8")

    system_prompt = read(sys_prompt_path)
    user_prompt = read(user_prompt_path)
    schema_text = read(schema_path)

    # Build transcript payload
    if args.transcript_file:
        tf = Path(args.transcript_file)
        if not tf.exists():
            print(f"ERROR: --transcript-file not found: {tf}", file=sys.stderr)
            sys.exit(1)
        transcript_text = tf.read_text(encoding="utf-8")
        transcript_label = "TIMECODES_TXT" if mode == "mock_assisted_split" else "TRANSCRIPT_TXT"
    elif mode == "mock_assisted_split" and has_timecodes:
        transcript_text = read(folder / "timecodes.txt")
        transcript_label = "TIMECODES_TXT"
    elif has_transcript:
        transcript_text = read(folder / "transcript.txt")
        transcript_label = "TRANSCRIPT_TXT"
    else:
        print("ERROR: no transcript.txt or timecodes.txt found", file=sys.stderr)
        sys.exit(1)

    # Sidecars (mock_assisted only, video.md excluded intentionally)
    sidecars = []
    if mode == "mock_assisted_split":
        feedback_path = folder / "feedback.md"
        if feedback_path.exists():
            sidecars.append(("FEEDBACK_MD", read(feedback_path)))

    # Assemble full prompt
    sections = [
        "=" * 70,
        "SYSTEM PROMPT",
        "=" * 70,
        system_prompt.strip(),
        "",
        "=" * 70,
        "USER PROMPT TEMPLATE",
        "=" * 70,
        user_prompt.strip(),
        "",
        "=" * 70,
        "OUTPUT SCHEMA",
        "=" * 70,
        schema_text.strip(),
        "",
        "=" * 70,
        "INPUT DATA",
        "=" * 70,
        f"SOURCE_ID: {source_id}",
        f"SPLITTER_MODE: {mode}",
        f"{transcript_label}:",
        transcript_text.strip(),
    ]
    for label, content in sidecars:
        sections += [f"\n{label}:", content.strip()]

    sections += [
        "",
        "=" * 70,
        "OUTPUT INSTRUCTIONS",
        "=" * 70,
        f"Save the JSON output to: {out_json.relative_to(root)}",
        "",
        "After saving JSON, run:",
        f"  python3 labeling/splitter_json_to_excel.py {out_json.relative_to(root)} --out {out_xlsx.relative_to(root)}",
        "",
        "Then run validation:",
        f"  python3 labeling/validate_splitter_vs_video.py \\",
        f"    --splitter {out_json.relative_to(root)} \\",
        f"    --video {args.folder}/video.md \\",
        f"    --tolerance 120 \\",
        f"    --out {out_validation.relative_to(root)}",
        "",
        "NOTE: video.md is for validation ONLY — do not use it for extraction.",
    ]

    full_text = "\n".join(sections)
    out_prompt.write_text(full_text, encoding="utf-8")

    print(f"Prompt file:   {out_prompt.relative_to(root)}")
    print(f"Output JSON:   {out_json.relative_to(root)}")
    print(f"Output Excel:  {out_xlsx.relative_to(root)}")
    print(f"Validation:    {out_validation.relative_to(root)}")
    print(f"Mode:          {mode}")
    print(f"Source ID:     {source_id}")
    print(f"Version:       v{version}")
    print()
    print("Next step — paste this into Claude Code:")
    print(f'  "Прочитай файл {out_prompt.relative_to(root)} и выполни задачу из него."')


if __name__ == "__main__":
    main()
