"""Transcript → Q&A: one LLM call, mirroring the ``/splitter`` skill (step 2).

``split_transcript`` is the live-backend Stage-1 entry point, analogous to
``src.assessor.assess.assess_one`` for Stage 2: a pure function, one model call,
JSON in / list-of-items out. The system prompt and output schema are loaded from
the ``/splitter`` skill so this code and the manual skill never drift.

Client choice: ``litellm.completion`` with ``response_format=json_object`` —
the repo standardises on LiteLLM + DSPy (no LangChain). The model defaults to
``llm_factory.SPLITTER_MODEL_ID`` (``openrouter/openai/gpt-5.4-nano``); override
with the ``SPLITTER_MODEL`` env var.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Callable

from src.common.llm_factory import SPLITTER_MODEL_ID  # also runs load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[2]
_SKILL = REPO_ROOT / ".claude" / "skills" / "splitter" / "step1-prepare"
SYSTEM_PROMPT_PATH = _SKILL / "splitter_system_prompt.txt"
SCHEMA_PATH = _SKILL / "splitter_output_schema.json"

MAX_TOKENS = 8000


def _detect_language(text: str) -> str:
    """`ru` if Cyrillic dominates the alphabetic characters, else `en`."""
    cyr = sum("Ѐ" <= ch <= "ӿ" for ch in text)
    lat = sum(("a" <= ch <= "z") or ("A" <= ch <= "Z") for ch in text)
    return "ru" if cyr > lat else "en"


def _user_message(transcript_text: str, source_id: str) -> str:
    """Assemble the step-2 user prompt: schema + INPUT DATA + transcript."""
    schema = SCHEMA_PATH.read_text(encoding="utf-8")
    language = _detect_language(transcript_text)
    return (
        "OUTPUT SCHEMA (follow exactly, no extra keys):\n"
        f"{schema}\n\n"
        "INPUT DATA:\n"
        f"- source_id: {source_id}\n"
        "- splitter_mode: split_only\n"
        f"- INTERVIEW_LANGUAGE: {language}\n\n"
        "PRIMARY_TRANSCRIPT:\n"
        f"{transcript_text}"
    )


def split_transcript(
    transcript_text: str,
    source_id: str,
    *,
    complete: Callable[..., Any] | None = None,
) -> list[dict[str, Any]]:
    """Split one transcript into splitter-schema items (raw dicts).

    `complete` is the LiteLLM-compatible completion callable; defaults to
    ``litellm.completion`` and is injected in tests to avoid the network. Returns
    ``items`` from the model's JSON, or ``[]`` on any failure (the caller's stage
    degrades to zero items rather than crashing the stream).
    """
    if not transcript_text.strip():
        return []

    if complete is None:
        import litellm  # lazy: keep import off the emulator path

        complete = litellm.completion

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")},
        {"role": "user", "content": _user_message(transcript_text, source_id)},
    ]

    try:
        resp = complete(
            model=SPLITTER_MODEL_ID,
            messages=messages,
            temperature=0,
            max_tokens=MAX_TOKENS,
            response_format={"type": "json_object"},
        )
        content = resp.choices[0].message.content
        items = json.loads(content).get("items", [])
        return items if isinstance(items, list) else []
    except Exception as exc:  # noqa: BLE001 — splitter must never break the stream
        print(f"[splitter] split_transcript({source_id!r}) failed: {exc}",
              file=sys.stderr)
        return []
