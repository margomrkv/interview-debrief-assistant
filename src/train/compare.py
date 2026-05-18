"""Compare two evaluator-prompt versions on the test split.

Loads kb/reports/eval_<vA>_test.md and kb/reports/eval_<vB>_test.md generated
by evaluate.py and prints/writes a diff of per-source/per-metric MAE and the
regressions in worst-cases (QA where vB is worse than vA).
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORTS = REPO_ROOT / "kb" / "reports"

_AGG_RE = re.compile(r"-\s+MAE:\s+\*\*([\d.]+)\*\*.*?CI:\s+\[([\d.]+),\s*([\d.]+)\]", re.S)
_ACC_RE = re.compile(r"accuracy\s+±1:\s+\*\*([\d.]+)\*\*")
_TABLE_LINE_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([\d.]+)\s*\|.*?$", re.M)


def _parse_aggregate(report: str) -> dict[str, float]:
    m = _AGG_RE.search(report)
    a = _ACC_RE.search(report)
    if not m or not a:
        raise ValueError("could not parse aggregate metrics from report")
    return {
        "mae": float(m.group(1)),
        "ci_low": float(m.group(2)),
        "ci_high": float(m.group(3)),
        "acc_pm1": float(a.group(1)),
    }


def _parse_table(report: str, section_heading: str) -> dict[str, float]:
    idx = report.find(section_heading)
    if idx == -1:
        return {}
    chunk = report[idx : idx + 4000]
    out: dict[str, float] = {}
    for m in _TABLE_LINE_RE.finditer(chunk):
        key = m.group(1).strip()
        if key in ("metric", "source_id", "---"):
            continue
        try:
            out[key] = float(m.group(2))
        except ValueError:
            continue
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("version_a", help="e.g. v1")
    p.add_argument("version_b", help="e.g. v2")
    p.add_argument("--split", default="test")
    p.add_argument("--out", type=Path, default=None)
    args = p.parse_args()

    a_path = REPORTS / f"eval_{args.version_a}_{args.split}.md"
    b_path = REPORTS / f"eval_{args.version_b}_{args.split}.md"
    if not a_path.exists() or not b_path.exists():
        raise SystemExit(f"missing: {a_path if not a_path.exists() else b_path}")

    a = a_path.read_text()
    b = b_path.read_text()
    a_agg = _parse_aggregate(a)
    b_agg = _parse_aggregate(b)
    a_metric = _parse_table(a, "## MAE per metric")
    b_metric = _parse_table(b, "## MAE per metric")
    a_source = _parse_table(a, "## MAE per source_id")
    b_source = _parse_table(b, "## MAE per source_id")

    lines = [
        f"# Compare — {args.version_a} → {args.version_b} ({args.split})",
        "",
        "## Aggregate",
        "",
        f"- MAE: {a_agg['mae']:.3f} → {b_agg['mae']:.3f}  (Δ={b_agg['mae'] - a_agg['mae']:+.3f})",
        f"- accuracy ±1: {a_agg['acc_pm1']:.3f} → {b_agg['acc_pm1']:.3f}  (Δ={b_agg['acc_pm1'] - a_agg['acc_pm1']:+.3f})",
        f"- CI width: {a_agg['ci_high'] - a_agg['ci_low']:.3f} → {b_agg['ci_high'] - b_agg['ci_low']:.3f}",
        "",
        "## MAE per metric",
        "",
        "| metric | A | B | Δ | regression? |",
        "|---|---|---|---|---|",
    ]
    for k in sorted(set(a_metric) | set(b_metric)):
        va, vb = a_metric.get(k, 0.0), b_metric.get(k, 0.0)
        lines.append(f"| {k} | {va:.3f} | {vb:.3f} | {vb - va:+.3f} | {'yes' if vb > va + 1e-6 else 'no'} |")

    lines += ["", "## MAE per source_id", "", "| source_id | A | B | Δ | regression? |", "|---|---|---|---|---|"]
    regressions = []
    for k in sorted(set(a_source) | set(b_source)):
        va, vb = a_source.get(k, 0.0), b_source.get(k, 0.0)
        is_reg = vb > va + 1e-6
        if is_reg:
            regressions.append((k, va, vb))
        lines.append(f"| {k} | {va:.3f} | {vb:.3f} | {vb - va:+.3f} | {'yes' if is_reg else 'no'} |")

    lines += ["", f"## Regressions: {len(regressions)} source_ids"]
    for k, va, vb in regressions:
        lines.append(f"- {k}: {va:.3f} → {vb:.3f}")

    out_path = args.out or (REPORTS / f"compare_{args.version_a}_{args.version_b}.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + "\n")
    print(f"wrote {out_path.relative_to(REPO_ROOT)}")
    print(f"MAE Δ: {b_agg['mae'] - a_agg['mae']:+.3f}  acc Δ: {b_agg['acc_pm1'] - a_agg['acc_pm1']:+.3f}  regressions: {len(regressions)}")


if __name__ == "__main__":
    main()
