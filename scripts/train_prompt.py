"""Orchestrate build_splits -> train -> evaluate as a single command.

Generates run_id once and threads it through train.py / evaluate.py via --run-id.
All steps run as subprocesses to isolate dspy state (Phoenix, dspy.settings) and
avoid loading dspy in steps that do not need it.
"""
from __future__ import annotations

import argparse
import datetime as dt
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RUNS_DIR = REPO_ROOT / "runs"


def _local_run_id() -> str:
    return dt.datetime.now().astimezone().strftime("%Y-%m-%d_%H-%M-%S")


def _run(cmd: list[str]) -> None:
    print(f"\n$ {' '.join(cmd)}", flush=True)
    subprocess.run(cmd, check=True, cwd=REPO_ROOT)


def main() -> None:
    p = argparse.ArgumentParser(
        description="Run build_splits -> train -> evaluate as one pipeline.",
    )
    p.add_argument("--run-id", default=None, help="Override run_id (default: now() in local TZ).")
    p.add_argument("--smoke", action="store_true", help="Pass --smoke to build_splits (2 source_ids).")
    p.add_argument("--num-trials", type=int, default=3, help="train --num-trials (default: 3).")
    p.add_argument(
        "--num-candidates",
        type=int,
        default=None,
        help="train --num-candidates (default: None → train mirrors --num-trials).",
    )
    p.add_argument(
        "--prompt-model",
        default=None,
        help="train --prompt-model alias or full id (default: None → train uses sonnet).",
    )
    p.add_argument("--no-phoenix", action="store_true", help="Pass --no-phoenix to train.")
    p.add_argument(
        "--eval-splits",
        choices=["test", "train", "both"],
        default="test",
        help="Which split(s) to evaluate. 'both' runs evaluate twice (default: test).",
    )
    p.add_argument("--skip-eval", action="store_true", help="Skip the evaluate step.")
    args = p.parse_args()

    run_id = args.run_id or _local_run_id()
    run_dir = RUNS_DIR / run_id
    print(f"run_id={run_id}  → {run_dir.relative_to(REPO_ROOT)}/", flush=True)

    # Step 1 — build_splits
    build_cmd = [sys.executable, "-m", "src.kb.build_splits"]
    if args.smoke:
        build_cmd.append("--smoke")
    _run(build_cmd)

    # Step 2 — train
    train_cmd = [
        sys.executable, "-m", "src.kb.train",
        "--run-id", run_id,
        "--num-trials", str(args.num_trials),
    ]
    if args.num_candidates is not None:
        train_cmd += ["--num-candidates", str(args.num_candidates)]
    if args.prompt_model is not None:
        train_cmd += ["--prompt-model", args.prompt_model]
    if args.no_phoenix:
        train_cmd.append("--no-phoenix")
    _run(train_cmd)

    # Step 3 — evaluate
    eval_splits: list[str] = []
    if not args.skip_eval:
        eval_splits = ["test", "train"] if args.eval_splits == "both" else [args.eval_splits]
        for split in eval_splits:
            _run([
                sys.executable, "-m", "src.common.evaluate",
                "--run-id", run_id,
                "--split", split,
            ])

    # Summary — only list artifacts that actually exist.
    print(f"\n=== Done. Artifacts in {run_dir.relative_to(REPO_ROOT)}/ ===")
    candidates = [
        run_dir / "evaluator_prompt.md",
        run_dir / "train_report.md",
        run_dir / "logs" / "train.jsonl",
        run_dir / "logs" / "train.trace.jsonl",
    ] + [run_dir / f"eval_{s}.md" for s in eval_splits]
    for path in candidates:
        marker = "✓" if path.exists() else "·"
        print(f"  {marker} {path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
