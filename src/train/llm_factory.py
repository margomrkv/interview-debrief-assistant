"""Single source of truth for the 3 LLM roles in the scoring-prompt trainer.

Roles (see plan §"Fixed decisions" D4-D6):
    TASK_LM   — model being trained (cheap, what production targets)
    PROMPT_LM — MIPROv2 prompt-mutation generator (needs meta-cognition)
    LABEL_LM  — golden-set labeler (reserved; not invoked in v1, labels already exist)
"""
from __future__ import annotations

import os
from pathlib import Path

import dspy
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(REPO_ROOT / ".env")


def _require(env_var: str) -> None:
    if not os.getenv(env_var):
        raise RuntimeError(
            f"{env_var} is not set. Copy .env.example to .env and fill in the keys."
        )


def make_lm(model_id: str, max_tokens: int = 500) -> dspy.LM:
    """Build a dspy.LM with built-in retry. DSPy 3.x handles backoff via num_retries."""
    return dspy.LM(model_id, max_tokens=max_tokens, num_retries=5)


TASK_MODEL_ID = "openrouter/nvidia/nemotron-3-super-120b-a12b:free"
PROMPT_MODEL_ID = "anthropic/claude-sonnet-4-6"
LABEL_MODEL_ID = "anthropic/claude-opus-4-7"


def task_lm() -> dspy.LM:
    _require("OPENROUTER_API_KEY")
    return make_lm(TASK_MODEL_ID, max_tokens=2500)


def prompt_lm() -> dspy.LM:
    _require("ANTHROPIC_API_KEY")
    return make_lm(PROMPT_MODEL_ID, max_tokens=2000)


def label_lm() -> dspy.LM:
    _require("ANTHROPIC_API_KEY")
    return make_lm(LABEL_MODEL_ID, max_tokens=1500)
