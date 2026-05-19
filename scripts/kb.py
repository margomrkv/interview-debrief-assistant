"""Train the scoring-evaluator prompt and evaluate on the held-out test split.

Thin argparse → `src.kb.train.run_kb_pipeline` wrapper. All real work happens
in-process via direct Python calls — no subprocess fan-out. Stdout is also
mirrored into `runs/<run_id>/logs/pipeline.log` for offline review.
"""
from __future__ import annotations

import argparse
from pathlib import Path

# MUST be imported before src.kb.train (which imports dspy/litellm) so the
# litellm bedrock/sagemaker pre-load warnings are filtered at import time.
from src.common.logging_setup import configure_logging  # noqa: I001

from src.common.llm_factory import PROMPT_MODEL_ALIASES  # noqa: E402
from src.kb.train import default_run_id, run_kb_pipeline  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
RUNS_DIR = REPO_ROOT / "runs"


def main() -> None:
    p = argparse.ArgumentParser(
        description="Build splits → MIPROv2 train → eval on chosen split(s). Single process.",
    )
    p.add_argument("--run-id", default=None, help="Override run_id (default: now() in local TZ).")
    p.add_argument("--smoke", action="store_true", help="Use only first 2 source_ids in splits.")
    p.add_argument("--num-trials", type=int, default=3, help="MIPROv2 num_trials (default 3).")
    p.add_argument(
        "--num-candidates",
        type=int,
        default=None,
        help="MIPROv2 num_candidates (default: mirrors --num-trials).",
    )
    p.add_argument(
        "--prompt-model",
        default=None,
        help=(
            "MIPROv2 proposer LM alias or fully-qualified id. "
            f"Aliases: {sorted(PROMPT_MODEL_ALIASES)}. Default: haiku."
        ),
    )
    p.add_argument("--no-phoenix", action="store_true", help="Disable Phoenix UI (JSONL trace still written).")
    p.add_argument(
        "--eval-splits",
        choices=["test", "train", "both", "none"],
        default="test",
        help="Which split(s) to evaluate after train. 'none' skips eval reports. Default: test.",
    )
    p.add_argument(
        "--log-file",
        type=Path,
        default=None,
        help="Override pipeline log file path (default: runs/<run_id>/logs/pipeline.log).",
    )
    p.add_argument(
        "--verbose",
        action="store_true",
        help="DEBUG-level logging (e.g. CostCallback throttled stats).",
    )
    args = p.parse_args()

    run_id = args.run_id or default_run_id()
    run_dir = RUNS_DIR / run_id
    log_file = args.log_file or (run_dir / "logs" / "pipeline.log")
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logger = configure_logging("kb", log_file=log_file, verbose=args.verbose)
    logger.info("run_id=%s → %s/", run_id, run_dir.relative_to(REPO_ROOT))
    logger.info("log file: %s", log_file.relative_to(REPO_ROOT))

    run_dir = run_kb_pipeline(
        num_trials=args.num_trials,
        num_candidates=args.num_candidates,
        prompt_model=args.prompt_model,
        smoke=args.smoke,
        no_phoenix=args.no_phoenix,
        eval_splits=args.eval_splits,
        run_id=run_id,
    )

    logger.info("")
    logger.info("=== Done. Artifacts in %s/ ===", run_dir.relative_to(REPO_ROOT))
    eval_splits = [] if args.eval_splits == "none" else (
        ["test", "train"] if args.eval_splits == "both" else [args.eval_splits]
    )
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
