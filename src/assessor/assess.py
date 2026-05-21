"""Production inference: apply a trained evaluator prompt to one splitter JSON.

`score_interview` reads a `splitter_output/<sid>.splitter.v<N>.*.json`, runs the
prompt artifact from `runs/<run_id>/evaluator_prompt.md` over every QA pair in
production-mirror dspy context (no reference_score needed), and writes a JSON
file next to the splitter input with the predicted scores per item.

This is the only entry point in `src/ar/`. The CLI wrapper lives in
`scripts/ar.py` — there is no argparse here.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.common.dataset import _to_inference_example, load_splitter_examples
from src.common.dspy_modules import METRICS
from src.common.eval_runner import predict_all
from src.common.llm_factory import TASK_MODEL_ID
from src.common.prompt_io import load_prompt_artifact

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROMPT = REPO_ROOT / "prompts" / "scoring.txt"


def _default_out_path(splitter_json: Path, source_id: str) -> Path:
    return splitter_json.parent / f"{source_id}.scores.json"


def _predictions(pred: Any) -> dict[str, int | None]:
    out: dict[str, int | None] = {}
    for m in METRICS:
        v = getattr(pred, m, None)
        if v is None:
            out[m] = None
            continue
        try:
            out[m] = int(v)
        except (TypeError, ValueError):
            out[m] = None
    return out


def assess_one(
    qa: dict[str, Any],
    *,
    prompt_path: Path = DEFAULT_PROMPT,
    lm: Any = None,
) -> dict[str, Any]:
    """Score a single QA pair (one LLM call) — the UI-facing per-item entry.

    `qa` carries the splitter input fields (`interviewer_question`,
    `candidate_answer`, `question_topic`, `interview_stage`). Returns the three
    METRICS as ints plus `error` and `reasoning`; the interview-level rollup is
    the caller's job. An empty/missing `prompt_path` falls back to the signature's
    built-in instructions (see eval_runner.predict_all).
    """
    prompt_text = load_prompt_artifact(prompt_path) if prompt_path.exists() else ""
    ex = _to_inference_example(qa, qa.get("source_id", "live"))
    pred = predict_all(prompt_text, [ex], lm=lm)[0]
    out: dict[str, Any] = dict(_predictions(pred))
    out["error"] = getattr(pred, "_error", None)
    out["reasoning"] = getattr(pred, "reasoning", None)
    return out


def score_interview(
    *,
    splitter_json: Path,
    prompt_path: Path,
    out_path: Path | None = None,
) -> Path:
    """Apply `prompt_path` to every QA in `splitter_json`, write predictions JSON.

    Returns the resolved output path.
    """
    examples, source_id = load_splitter_examples(splitter_json)
    prompt_text = load_prompt_artifact(prompt_path)
    preds = predict_all(prompt_text, examples)

    items: list[dict[str, Any]] = []
    for ex, pr in zip(examples, preds):
        items.append({
            "interviewer_question": ex.interviewer_question,
            "candidate_answer": ex.candidate_answer,
            "question_topic": ex.question_topic,
            "interview_stage": ex.interview_stage,
            "predictions": _predictions(pr),
            "error": getattr(pr, "_error", None),
        })

    result = {
        "source_id": source_id,
        "prompt_path": str(prompt_path),
        "task_model": TASK_MODEL_ID,
        "items": items,
    }

    out = (out_path or _default_out_path(splitter_json, source_id)).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    return out
