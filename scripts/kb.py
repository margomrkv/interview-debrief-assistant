"""Train the scoring-evaluator prompt and evaluate on the held-out test split.

Thin argparse → `src.kb.train.run_kb_pipeline` wrapper. All real work happens
in-process via direct Python calls — no subprocess fan-out.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from src.common.llm_factory import PROMPT_MODEL_ALIASES
from src.kb.train import run_kb_pipeline

REPO_ROOT = Path(__file__).resolve().parents[1]


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
    args = p.parse_args()

    run_dir = run_kb_pipeline(
        num_trials=args.num_trials,
        num_candidates=args.num_candidates,
        prompt_model=args.prompt_model,
        smoke=args.smoke,
        no_phoenix=args.no_phoenix,
        eval_splits=args.eval_splits,
        run_id=args.run_id,
    )

    print(f"\n=== Done. Artifacts in {run_dir.relative_to(REPO_ROOT)}/ ===")
    eval_splits = [] if args.eval_splits == "none" else (
        ["test", "train"] if args.eval_splits == "both" else [args.eval_splits]
    )
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
