"""Apply a trained evaluator prompt to one splitter JSON → predictions JSON.

Thin argparse → `src.ar.score.score_interview` wrapper.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from src.ar.score import score_interview

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
    args = p.parse_args()

    out = score_interview(
        splitter_json=args.splitter.resolve(),
        prompt_path=args.prompt.resolve(),
        out_path=args.out.resolve() if args.out else None,
    )
    try:
        rel = out.relative_to(REPO_ROOT)
        print(f"wrote {rel}")
    except ValueError:
        print(f"wrote {out}")


if __name__ == "__main__":
    main()
