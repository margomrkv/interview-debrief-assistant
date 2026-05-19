"""Orchestrate build_splits -> train -> evaluate as a single command.

Generates run_id once and threads it through train.py / evaluate.py via --run-id.
All steps run as subprocesses to isolate dspy state (Phoenix, dspy.settings) and
avoid loading dspy in steps that do not need it. Each subprocess receives
`--log-file <runs/<id>/logs/pipeline.log>` so stdout from all three steps is
mirrored into a single file alongside the rest of the run artifacts.
"""
from __future__ import annotations

import argparse
import datetime as dt
import subprocess
import sys
from pathlib import Path

from src.common.logging_setup import configure_logging

REPO_ROOT = Path(__file__).resolve().parents[1]
RUNS_DIR = REPO_ROOT / "runs"


def _local_run_id() -> str:
    return dt.datetime.now().astimezone().strftime("%Y-%m-%d_%H-%M-%S")


def _banner(logger, step: int, total: int, name: str) -> None:
    title = f" STEP {step}/{total} — {name} "
    width = max(48, len(title) + 4)
    bar = "═" * (width - 2)
    pad = width - 2 - len(title)
    logger.info("")
    logger.info("╔%s╗", bar)
    logger.info("║%s%s║", title, " " * pad)
    logger.info("╚%s╝", bar)


def _run(cmd: list[str], logger) -> None:
    logger.info("$ %s", " ".join(cmd))
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
    p.add_argument(
        "--verbose",
        action="store_true",
        help="DEBUG-level logging in every step (e.g. CostCallback throttled stats).",
    )
    args = p.parse_args()

    run_id = args.run_id or _local_run_id()
    run_dir = RUNS_DIR / run_id
    log_file = run_dir / "logs" / "pipeline.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logger = configure_logging("orchestrator", log_file=log_file, verbose=args.verbose)
    logger.info("run_id=%s → %s/", run_id, run_dir.relative_to(REPO_ROOT))
    logger.info("log file: %s", log_file.relative_to(REPO_ROOT))

    total_steps = 2 + (0 if args.skip_eval else (2 if args.eval_splits == "both" else 1))

    common_flags = ["--log-file", str(log_file)]
    if args.verbose:
        common_flags.append("--verbose")

    # Step 1 — build_splits
    _banner(logger, 1, total_steps, "build_splits")
    build_cmd = [sys.executable, "-m", "src.kb.build_splits", *common_flags]
    if args.smoke:
        build_cmd.append("--smoke")
    _run(build_cmd, logger)

    # Step 2 — train
    _banner(logger, 2, total_steps, "train (DSPy MIPROv2)")
    train_cmd = [
        sys.executable, "-m", "src.kb.train",
        "--run-id", run_id,
        "--num-trials", str(args.num_trials),
        *common_flags,
    ]
    if args.num_candidates is not None:
        train_cmd += ["--num-candidates", str(args.num_candidates)]
    if args.prompt_model is not None:
        train_cmd += ["--prompt-model", args.prompt_model]
    if args.no_phoenix:
        train_cmd.append("--no-phoenix")
    _run(train_cmd, logger)

    # Step 3 — evaluate
    eval_splits: list[str] = []
    if not args.skip_eval:
        eval_splits = ["test", "train"] if args.eval_splits == "both" else [args.eval_splits]
        for i, split in enumerate(eval_splits):
            _banner(logger, 3 + i, total_steps, f"evaluate ({split} split)")
            _run(
                [
                    sys.executable, "-m", "src.common.evaluate",
                    "--run-id", run_id,
                    "--split", split,
                    *common_flags,
                ],
                logger,
            )

    # Summary — only list artifacts that actually exist.
    logger.info("")
    logger.info("=== Done. Artifacts in %s/ ===", run_dir.relative_to(REPO_ROOT))
    candidates = [
        run_dir / "evaluator_prompt.md",
        run_dir / "train_report.md",
        run_dir / "logs" / "train.jsonl",
        run_dir / "logs" / "train.trace.jsonl",
        run_dir / "logs" / "pipeline.log",
    ] + [run_dir / f"eval_{s}.md" for s in eval_splits]
    for path in candidates:
        marker = "✓" if path.exists() else "·"
        logger.info("  %s %s", marker, path.relative_to(REPO_ROOT))


if __name__ == "__main__":
    main()
