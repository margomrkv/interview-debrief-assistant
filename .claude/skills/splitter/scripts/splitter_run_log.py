#!/usr/bin/env python3
"""CLI: append a step to {basename}.vN.pipeline-log.md (manifest in HTML comment)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_DIR.parents[2]
sys.path.insert(0, str(SKILL_DIR))

from run_manifest import append_step, load_run, save_run  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Log splitter pipeline step to pipeline-log.md")
    parser.add_argument(
        "--pipeline-log",
        default=None,
        help="Path to {basename}.vN.pipeline-log.md",
    )
    parser.add_argument(
        "--run-json",
        default=None,
        help="Legacy alias for --pipeline-log (.md or old .json)",
    )
    parser.add_argument("--step", type=int, required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--llm", action="store_true")
    parser.add_argument("--model", default=None)
    parser.add_argument("--status", default="completed")
    parser.add_argument("--duration-sec", type=float, default=None)
    parser.add_argument("--input", action="append", default=[], dest="inputs")
    parser.add_argument("--output", action="append", default=[], dest="outputs")
    parser.add_argument("--note", default=None)
    args = parser.parse_args()

    log_arg = args.pipeline_log or args.run_json
    if not log_arg:
        print("ERROR: pass --pipeline-log or --run-json", file=sys.stderr)
        sys.exit(1)

    log_path = Path(log_arg)
    if not log_path.is_absolute():
        log_path = REPO_ROOT / log_path
    if not log_path.exists():
        print(f"ERROR: pipeline log not found: {log_path}", file=sys.stderr)
        sys.exit(1)

    run = load_run(log_path)
    append_step(
        run,
        step_id=args.step,
        name=args.name,
        llm=args.llm,
        model=args.model,
        inputs=args.inputs,
        outputs=args.outputs,
        status=args.status,
        duration_sec=args.duration_sec,
        notes=args.note,
    )
    save_run(run, log_path)
    md_path = log_path if log_path.suffix == ".md" else log_path.with_suffix(".md")
    print(f"Updated: {log_path.relative_to(REPO_ROOT)}")
    print(f"Report:  {md_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
