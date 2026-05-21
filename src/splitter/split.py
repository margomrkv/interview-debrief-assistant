"""Transcript → Q&A: one LLM call, mirroring the ``/splitter`` skill (step 2).

``split_transcript`` is the live-backend Stage-1 entry point, analogous to
``src.assessor.assess.assess_one`` for Stage 2: a pure function, one model call,
JSON in / list-of-items out. The system prompt is the self-contained
``prompts/splitter.txt`` (UI single-call variant of the ``/splitter`` skill, with
the output schema inlined) — one file, no separate schema dependency.

Client choice: ``litellm.completion`` with ``response_format=json_object`` —
the repo standardises on LiteLLM + DSPy (no LangChain). The model defaults to
``llm_factory.SPLITTER_MODEL_ID`` (``anthropic/claude-sonnet-4-6`` — one-shot
full-transcript extraction needs a strong model; see am-best-offer-4r0); override
with the ``SPLITTER_MODEL`` env var. Output is parsed via ``_extract_json_object``
(provider-agnostic: Anthropic wraps JSON in a ```json fence, OpenAI does not).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Callable

from src.common.llm_factory import SPLITTER_MODEL_ID  # also runs load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[2]
SYSTEM_PROMPT_PATH = REPO_ROOT / "prompts" / "splitter.txt"

MAX_TOKENS = 128000


def _detect_language(text: str) -> str:
    """`ru` if Cyrillic dominates the alphabetic characters, else `en`."""
    cyr = sum("Ѐ" <= ch <= "ӿ" for ch in text)
    lat = sum(("a" <= ch <= "z") or ("A" <= ch <= "Z") for ch in text)
    return "ru" if cyr > lat else "en"


_TIME_RE = re.compile(r"\b(\d{1,2}:\d{2}(?::\d{2})?)\b")


def _last_timestamp(text: str) -> str | None:
    """Last MM:SS / HH:MM:SS marker in the transcript — the interview's end time.

    Fed to the model as TRANSCRIPT_END_TIME so it can self-check it extracted all
    the way to the end (the splitter's failure mode is stopping early).
    """
    matches = _TIME_RE.findall(text)
    return matches[-1] if matches else None


def _user_message(transcript_text: str, source_id: str) -> str:
    """Assemble the step-2 user prompt: INPUT DATA + transcript (schema is in the
    system prompt)."""
    language = _detect_language(transcript_text)
    end_time = _last_timestamp(transcript_text) or "unknown"
    return (
        "INPUT DATA:\n"
        f"- source_id: {source_id}\n"
        "- splitter_mode: split_only\n"
        f"- INTERVIEW_LANGUAGE: {language}\n"
        f"- TRANSCRIPT_END_TIME: {end_time}\n\n"
        "PRIMARY_TRANSCRIPT:\n"
        f"{transcript_text}"
    )


def _extract_json_object(content: str) -> str:
    """Slice the outermost ``{...}`` so a fenced/prefixed body still parses.

    Anthropic ignores ``response_format=json_object`` and wraps output in a
    ```json fence; OpenAI honours it. Taking first ``{`` … last ``}`` makes the
    parser provider-agnostic. Returns ``content`` unchanged when no object is
    found (so ``json.loads`` raises a clear error).
    """
    start, end = content.find("{"), content.rfind("}")
    return content[start:end + 1] if 0 <= start < end else content


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
        choice = resp.choices[0]
        content = choice.message.content or ""
        finish = getattr(choice, "finish_reason", None)
        usage = getattr(resp, "usage", None)
        try:
            items = json.loads(_extract_json_object(content)).get("items", [])
            items = items if isinstance(items, list) else []
        except json.JSONDecodeError as je:
            # Truncated / non-JSON body — log the tail so we can see where it cut.
            print(f"[splitter] {source_id!r}: JSON parse failed ({je}); "
                  f"finish_reason={finish} len={len(content)} usage={usage} "
                  f"tail={content[-200:]!r}", file=sys.stderr)
            return []
        # Diagnostic: a 'length' finish or a low item count vs transcript size points
        # at output truncation / model under-extraction (see am-best-offer-4r0).
        print(f"[splitter] {source_id!r}: items={len(items)} "
              f"finish_reason={finish} content_chars={len(content)} usage={usage}",
              file=sys.stderr)
        return items
    except Exception as exc:  # noqa: BLE001 — splitter must never break the stream
        print(f"[splitter] split_transcript({source_id!r}) failed: {exc}",
              file=sys.stderr)
        return []
