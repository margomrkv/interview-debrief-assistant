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


def make_lm(
    model_id: str,
    max_tokens: int = 500,
    extra_body: dict | None = None,
) -> dspy.LM:
    """Build a dspy.LM with built-in retry. DSPy 3.x handles backoff via num_retries.

    `extra_body` is forwarded to LiteLLM as provider-specific request params
    (e.g. OpenRouter's `reasoning: {exclude: true}` for reasoning-models).
    """
    kwargs: dict = {"max_tokens": max_tokens, "num_retries": 8}
    if extra_body:
        kwargs["extra_body"] = extra_body
    return dspy.LM(model_id, **kwargs)


#TASK_MODEL_ID = "openrouter/nvidia/nemotron-3-super-120b-a12b:free"
TASK_MODEL_ID = "openrouter/google/gemma-4-26b-a4b-it"
# Default proposer: Haiku 4.5. Picked over Sonnet for ~3-4× lower cost; DSPy
# community evidence (issue #1596, paper 2406.11695) suggests smaller proposer
# performs as well or better. Override via prompt_lm(model_id=...) or
# `train.py --prompt-model {sonnet|haiku|gpt-4o-mini|gemini-flash}`.
PROMPT_MODEL_ID = "anthropic/claude-haiku-4-5-20251001"
LABEL_MODEL_ID = "anthropic/claude-opus-4-7"

# Short aliases for the --prompt-model CLI flag (A/B testing the MIPROv2 proposer).
# See am-best-offer-351 for rationale (DSPy #1596, paper 2406.11695).
PROMPT_MODEL_ALIASES: dict[str, str] = {
    "sonnet": "anthropic/claude-sonnet-4-6",
    "haiku": "anthropic/claude-haiku-4-5-20251001",
    "gpt-4o-mini": "openai/gpt-4o-mini",
    "gemini-flash": "gemini/gemini-2.5-flash"
}

# Per-provider env var requirement for prompt_lm overrides.
_PROVIDER_ENV: dict[str, str] = {
    "anthropic/": "ANTHROPIC_API_KEY",
    "openai/": "OPENAI_API_KEY",
    "gemini/": "GEMINI_API_KEY",
    "openrouter/": "OPENROUTER_API_KEY",
}


def resolve_prompt_model_id(name_or_id: str | None) -> str:
    """Map a short alias (e.g. 'haiku') to a fully-qualified model id.

    Passes through any value containing a `/` as a raw model id (e.g.
    `anthropic/claude-sonnet-4-6`). None falls back to the default PROMPT_MODEL_ID
    (currently Haiku 4.5).
    """
    if name_or_id is None:
        return PROMPT_MODEL_ID
    if name_or_id in PROMPT_MODEL_ALIASES:
        return PROMPT_MODEL_ALIASES[name_or_id]
    if "/" in name_or_id:
        return name_or_id
    raise ValueError(
        f"Unknown prompt-model alias {name_or_id!r}. "
        f"Known: {sorted(PROMPT_MODEL_ALIASES)} or pass a provider/model id."
    )


def _require_for_model(model_id: str) -> None:
    for prefix, env_var in _PROVIDER_ENV.items():
        if model_id.startswith(prefix):
            _require(env_var)
            return
    # Unknown provider — let LiteLLM surface a clear error at call time.


def task_lm() -> dspy.LM:
    # Disable OpenRouter's native reasoning channel so the full max_tokens budget
    # goes to the JSON output. Nemotron is a reasoning model; without this, the
    # hidden `reasoning_content` channel routinely eats the budget and the
    # adapter fails to parse missing fields (~46% example-fail rate observed in
    # train_v1 logs; see plans/nemotron-sharded-duckling.md).
    _require("OPENROUTER_API_KEY")
    return make_lm(
        TASK_MODEL_ID,
        max_tokens=4000,
        extra_body={"reasoning": {"exclude": True}},
    )


def prompt_lm(model_id: str | None = None) -> dspy.LM:
    """Build the MIPROv2 prompt-proposer LM.

    `model_id` accepts either a short alias from PROMPT_MODEL_ALIASES
    (e.g. 'sonnet') or a fully-qualified provider/model id. None → default Haiku.
    """
    resolved = resolve_prompt_model_id(model_id)
    _require_for_model(resolved)
    return make_lm(resolved, max_tokens=2000)


def label_lm() -> dspy.LM:
    _require("OPENROUTER_API_KEY")
    return make_lm(LABEL_MODEL_ID, max_tokens=1500)
