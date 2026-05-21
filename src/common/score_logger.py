"""Per-iteration score logger for the scoring-prompt trainer.

DSPy calls the metric `mae_metric(example, pred, trace=None)` once per
(example, prediction) inside every MIPROv2 iteration — both during bootstrap
(demo validation, trace != None) and during trial evaluation (trace = None).
`make_logged_metric` wraps the metric so each call also appends one CSV row:
golden scores (фактические значения) vs the prompt's predicted scores (оценки
промпта), tagged with the current MIPRO phase/trial.

Phase/trial are read by reference from a `CostCallback` (DRY: `MIPROPhaseHandler`
already keeps `current_phase` / `current_trial` up to date on it — we don't
re-parse MIPRO logs here).
"""
from __future__ import annotations

import csv
import logging
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from src.common.cost_callback import CostCallback
from src.common.dspy_modules import METRICS, _pred, _ref

_log = logging.getLogger(__name__)

# Short CSV column suffixes for the three 1..5 metrics, in METRICS order.
_SHORT = ("factual", "focus", "clarity")

_HEADER = (
    ["ts", "phase", "trial", "demoset", "instruction", "source_id", "interview_stage", "question_topic"]
    + [f"ref_{s}" for s in _SHORT]
    + [f"pred_{s}" for s in _SHORT]
    + [f"err_{s}" for s in _SHORT]
    + ["metric", "error"]
)


class ScoreLogger:
    """Writes one CSV row per metric evaluation (ref vs pred + abs error)."""

    def __init__(self, csv_path: Path, phase_ref: CostCallback) -> None:
        self.phase_ref = phase_ref
        self._lock = threading.Lock()
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        self._fp = open(csv_path, "a", encoding="utf-8", newline="")
        self._writer = csv.writer(self._fp)
        self._writer.writerow(_HEADER)
        self._fp.flush()
        self.csv_path = csv_path

    def log(self, example: Any, pred: Any, metric: float | None = None) -> None:
        try:
            refs = [_ref(example, m) for m in METRICS]
            preds = [_pred(pred, m) for m in METRICS]
            errs = [
                (abs(p - r) if (p is not None and r is not None) else "")
                for r, p in zip(refs, preds)
            ]
            row = (
                [
                    datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
                    self.phase_ref.current_phase,
                    self.phase_ref.current_trial,
                    self.phase_ref.current_demoset,
                    self.phase_ref.current_instruction,
                    getattr(example, "source_id", ""),
                    getattr(example, "interview_stage", ""),
                    getattr(example, "question_topic", ""),
                ]
                + [r if r is not None else "" for r in refs]
                + [p if p is not None else "" for p in preds]
                + errs
                + [
                    ("" if metric is None else round(metric, 3)),
                    getattr(pred, "_error", "") or "",
                ]
            )
        except Exception as e:  # never let logging break the optimizer
            _log.debug("ScoreLogger.log failed: %s", e)
            return
        with self._lock:
            self._writer.writerow(row)
            self._fp.flush()

    def close(self) -> None:
        try:
            self._fp.flush()
            self._fp.close()
        except Exception:
            pass

    def __enter__(self) -> "ScoreLogger":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()


def make_logged_metric(
    base_metric: Callable[..., float],
    logger: ScoreLogger,
) -> Callable[..., float]:
    """Wrap `base_metric` so each (example, pred) call also writes a CSV row.

    Returns the unmodified base score; logging is a pure side effect.
    """

    def metric(example: Any, pred: Any, trace: Any = None) -> float:
        score = base_metric(example, pred, trace)
        logger.log(example, pred, score)
        return score

    return metric
