#!/usr/bin/env python3
"""CLI: append a step to {basename}.vN.run.json and refresh .run.md"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_DIR.parents[2]
sys.path.insert(0, str(SKILL_DIR))

from run_manifest import append_step, load_run, save_run  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Log splitter pipeline step to run.json")
    parser.add_argument("--run-json", required=True, help="Path to {basename}.vN.run.json")
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

    run_path = Path(args.run_json)
    if not run_path.is_absolute():
        run_path = REPO_ROOT / run_path
    if not run_path.exists():
        print(f"ERROR: run file not found: {run_path}", file=sys.stderr)
        sys.exit(1)

    run = load_run(run_path)
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
    save_run(run, run_path)
    print(f"Updated: {run_path.relative_to(REPO_ROOT)}")
    print(f"Report:  {run_path.with_suffix('.md').relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
