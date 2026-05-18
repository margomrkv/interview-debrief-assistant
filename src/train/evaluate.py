"""Evaluate a saved evaluator-prompt artifact on the test split.

Reads kb/evaluator_prompt_<vN>.md, applies it as the signature instructions on
a fresh ScoringEvaluator, runs predictions over kb/splits.json test items,
and writes kb/reports/eval_<vN>_test.md.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

import dspy

from src.train.dspy_modules import (
    METRICS,
    ScoringEvaluator,
    accuracy_pm1,
    bootstrap_ci_95,
    mae_raw,
)
from src.train.llm_factory import TASK_MODEL_ID, task_lm
from src.train.train import INPUT_FIELDS, _load_data, _predict_one

REPO_ROOT = Path(__file__).resolve().parents[2]


def _strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end == -1:
        return text
    return text[end + 4 :].lstrip("\n")


def _load_prompt(path: Path) -> str:
    return _strip_frontmatter(path.read_text())


def _which_split(name: str) -> str:
    return "train" if name == "train" else "test"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--prompt", type=Path, required=True, help="Path to kb/evaluator_prompt_vN.md")
    p.add_argument("--split", choices=["train", "test"], default="test")
    p.add_argument("--out", type=Path, default=None)
    args = p.parse_args()

    prompt = _load_prompt(args.prompt)
    train, test, splits_meta = _load_data()
    examples = test if args.split == "test" else train

    student = ScoringEvaluator()
    student.score.signature = student.score.signature.with_instructions(prompt)

    dspy.configure(lm=task_lm())
    print(f"evaluating {len(examples)} {args.split} examples with prompt={args.prompt.name} on {TASK_MODEL_ID}")
    preds = [_predict_one(student, ex) for ex in examples]
    fails = sum(1 for p in preds if getattr(p, "_error", None))

    mae = mae_raw(preds, examples)
    acc = accuracy_pm1(preds, examples)
    med, lo, hi = bootstrap_ci_95(preds, examples)

    per_source_errs: dict[str, list[int]] = defaultdict(list)
    per_metric_errs: dict[str, list[int]] = defaultdict(list)
    for pr, ex in zip(preds, examples):
        if getattr(pr, "_error", None):
            continue
        for m in METRICS:
            ref = ex.reference_score.get(m)
            pv = getattr(pr, m, None)
            if ref is None or pv is None:
                continue
            try:
                e = abs(int(pv) - ref)
                per_source_errs[ex.source_id].append(e)
                per_metric_errs[m].append(e)
            except (TypeError, ValueError):
                pass

    worst = []
    for pr, ex in zip(preds, examples):
        if getattr(pr, "_error", None):
            continue
        errs = []
        for m in METRICS:
            ref = ex.reference_score.get(m)
            pv = getattr(pr, m, None)
            if ref is None or pv is None:
                continue
            try:
                errs.append(abs(int(pv) - ref))
            except (TypeError, ValueError):
                pass
        if errs:
            worst.append((sum(errs) / len(errs), ex, pr))
    worst.sort(key=lambda t: -t[0])

    version = args.prompt.stem.replace("evaluator_prompt_", "")
    out = args.out or (REPO_ROOT / "kb" / "reports" / f"eval_{version}_{args.split}.md")
    out.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        f"# Eval report — {version} ({args.split})",
        "",
        f"- prompt: `{args.prompt.relative_to(REPO_ROOT)}`",
        f"- task model: `{TASK_MODEL_ID}`",
        f"- examples: {len(examples)} (failures: {fails})",
        "",
        "## Aggregate",
        "",
        f"- MAE: **{mae:.3f}** (95% CI: [{lo:.3f}, {hi:.3f}])",
        f"- accuracy ±1: **{acc:.3f}**",
        "",
        "## MAE per metric",
        "",
        "| metric | MAE |",
        "|---|---|",
    ]
    for m in METRICS:
        es = per_metric_errs.get(m, [])
        lines.append(f"| {m} | {(sum(es)/len(es) if es else 0.0):.3f} |")

    lines += ["", "## MAE per source_id", "", "| source_id | MAE | n |", "|---|---|---|"]
    for src, es in sorted(per_source_errs.items(), key=lambda kv: -(sum(kv[1]) / len(kv[1]) if kv[1] else 0)):
        lines.append(f"| {src} | {(sum(es)/len(es) if es else 0.0):.3f} | {len(es)} |")

    lines += ["", "## Worst 20 cases", ""]
    for i, (avg_err, ex, pr) in enumerate(worst[:20], 1):
        ref = ex.reference_score
        pred = {m: getattr(pr, m, None) for m in METRICS}
        lines.append(
            f"{i}. avg_err={avg_err:.2f} src={ex.source_id} "
            f"ref={ref} pred={pred} q={ex.interviewer_question[:80]!r}"
        )

    out.write_text("\n".join(lines) + "\n")
    print(f"wrote {out.relative_to(REPO_ROOT)}")
    print(f"MAE={mae:.3f}  acc±1={acc:.3f}  CI=[{lo:.3f},{hi:.3f}]  failures={fails}")


if __name__ == "__main__":
    main()
