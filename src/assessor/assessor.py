"""Apply a trained evaluator prompt to one splitter JSON → predictions JSON.

Thin argparse → `src.assessor.score.score_interview` wrapper.
"""
from __future__ import annotations

import argparse
from pathlib import Path

# MUST be imported before src.assessor.score (which imports dspy/litellm) so the
# litellm bedrock/sagemaker pre-load warnings are filtered at import time.
from src.common.logging_setup import configure_logging  # noqa: I001

from src.assessor.score import score_interview  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    p = argparse.ArgumentParser(
        description="Score every QA in a splitter JSON with a trained evaluator prompt.",
    )
    p.add_argument(
        "--splitter",
        type=Path,
        required=True,
        help="Path to splitter_output/<sid>.splitter.v<N>.*.json",
    )
    p.add_argument(
        "--prompt",
        type=Path,
        required=True,
        help="Path to runs/<run_id>/evaluator_prompt.md",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output path (default: <splitter parent>/<source_id>.scores.json).",
    )
    p.add_argument(
        "--log-file",
        type=Path,
        default=None,
        help="Mirror logs into this file (append).",
    )
    p.add_argument(
        "--verbose",
        action="store_true",
        help="DEBUG-level logging.",
    )
    args = p.parse_args()

    logger = configure_logging("ar", log_file=args.log_file, verbose=args.verbose)

    out = score_interview(
        splitter_json=args.splitter.resolve(),
        prompt_path=args.prompt.resolve(),
        out_path=args.out.resolve() if args.out else None,
    )
    try:
        logger.info("wrote %s", out.relative_to(REPO_ROOT))
    except ValueError:
        logger.info("wrote %s", out)


if __name__ == "__main__":
    main()
