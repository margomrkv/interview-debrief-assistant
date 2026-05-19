"""Evaluate a saved evaluator-prompt artifact on the test split.

Reads runs/<ts>/evaluator_prompt.md, applies it as the signature instructions on
a fresh ScoringEvaluator (via shared `run_evaluation`), runs predictions over
kb/splits.json test items, and writes the report next to the prompt as
runs/<ts>/eval_<split>.md.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from src.common.dataset import load_split_examples
from src.common.dspy_modules import METRICS
from src.common.eval_runner import run_evaluation
from src.common.llm_factory import TASK_MODEL_ID

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CORPUS = REPO_ROOT / "train" / "hard_skills.json"
DEFAULT_SPLITS = REPO_ROOT / "kb" / "splits.json"


def _strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end == -1:
        return text
    return text[end + 4 :].lstrip("\n")


def _load_prompt(path: Path) -> str:
    return _strip_frontmatter(path.read_text())


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--prompt",
        type=Path,
        default=None,
        help="Path to runs/<ts>/evaluator_prompt.md (default: derived from --run-id).",
    )
    p.add_argument(
        "--run-id",
        default=None,
        help="Run identifier; if --prompt is omitted, resolves to runs/<run-id>/evaluator_prompt.md.",
    )
    p.add_argument("--split", choices=["train", "test"], default="test")
    p.add_argument("--out", type=Path, default=None)
    p.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    p.add_argument("--splits", type=Path, default=DEFAULT_SPLITS)
    args = p.parse_args()

    if args.prompt is None:
        if args.run_id is None:
            p.error("either --prompt or --run-id must be provided")
        args.prompt = REPO_ROOT / "runs" / args.run_id / "evaluator_prompt.md"

    args.prompt = args.prompt.resolve()
    prompt = _load_prompt(args.prompt)
    train, test, _ = load_split_examples(args.corpus, args.splits)
    examples = test if args.split == "test" else train

    print(f"evaluating {len(examples)} {args.split} examples with prompt={args.prompt.name} on {TASK_MODEL_ID}")
    metrics = run_evaluation(prompt, examples)

    run_label = args.prompt.parent.name
    out = (args.out or (args.prompt.parent / f"eval_{args.split}.md")).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        f"# Eval report — {run_label} ({args.split})",
        "",
        f"- prompt: `{args.prompt.relative_to(REPO_ROOT)}`",
        f"- task model: `{TASK_MODEL_ID}`",
        f"- examples: {len(examples)} (failures: {metrics['fails']})",
        "",
        "## Aggregate",
        "",
        f"- MAE: **{metrics['mae']:.3f}** (95% CI: [{metrics['ci_low']:.3f}, {metrics['ci_high']:.3f}])",
        f"- accuracy ±1: **{metrics['accuracy_pm1']:.3f}**",
        "",
        "## MAE per metric",
        "",
        "| metric | MAE |",
        "|---|---|",
    ]
    for m in METRICS:
        lines.append(f"| {m} | {metrics['per_metric_mae'][m]:.3f} |")

    lines += ["", "## MAE per source_id", "", "| source_id | MAE | n |", "|---|---|---|"]
    for src, mae in sorted(metrics["per_source_mae"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {src} | {mae:.3f} | {metrics['per_source_n'][src]} |")

    lines += ["", "## Worst 20 cases", ""]
    for i, (avg_err, ex, pr) in enumerate(metrics["worst"], 1):
        ref = ex.reference_score
        pred = {m: getattr(pr, m, None) for m in METRICS}
        lines.append(
            f"{i}. avg_err={avg_err:.2f} src={ex.source_id} "
            f"ref={ref} pred={pred} q={ex.interviewer_question[:80]!r}"
        )

    out.write_text("\n".join(lines) + "\n")
    print(f"wrote {out.relative_to(REPO_ROOT)}")
    print(
        f"MAE={metrics['mae']:.3f}  acc±1={metrics['accuracy_pm1']:.3f}  "
        f"CI=[{metrics['ci_low']:.3f},{metrics['ci_high']:.3f}]  failures={metrics['fails']}"
    )


if __name__ == "__main__":
    main()
