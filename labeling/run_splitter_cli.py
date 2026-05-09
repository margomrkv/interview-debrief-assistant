#!/usr/bin/env python3
"""Run splitter extraction via Anthropic API and validate output.

Model and defaults are read from labeling/config/splitter_run_config.json.
A run manifest is saved alongside each output file as <output>.run_manifest.json.

Usage example:
  python labeling/run_splitter_cli.py \
    --source-id karpov_junior_ds_20220330 \
    --mode raw_split \
    --transcript transcripts/.../transcript.txt \
    --out labeling/data/karpov_junior_ds_20220330.splitter.v3.raw.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_CONFIG_PATH = "labeling/config/splitter_run_config.json"


def _load_text(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"File not found: {path}")
    return path.read_text(encoding="utf-8")


def _sha256_short(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:12]


def _load_run_config(root: Path) -> dict[str, Any]:
    config_path = root / DEFAULT_CONFIG_PATH
    if config_path.exists():
        return json.loads(config_path.read_text(encoding="utf-8"))
    return {}


def _resolve_user_prompt(mode: str, run_config: dict[str, Any], root: Path) -> Path:
    key = f"user_prompt_{mode}"
    if key in run_config:
        return root / run_config[key]
    if mode == "raw_split":
        return root / "labeling/prompts/user_prompt_template_v2.txt"
    return root / "labeling/prompts/user_prompt_template_mock_assisted_v2.txt"


def _extract_json(text: str) -> dict[str, Any]:
    candidate = text.strip()
    if candidate.startswith("```"):
        candidate = candidate.strip("`")
        if candidate.startswith("json"):
            candidate = candidate[4:].strip()
    try:
        return json.loads(candidate)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Model output is not valid JSON: {exc}") from exc


def _validate_against_schema(data: dict[str, Any], schema: dict[str, Any]) -> None:
    """Strict LinkedText schema validation."""
    req_top = schema.get("required", [])
    for key in req_top:
        if key not in data:
            raise SystemExit(f"Validation failed: missing top-level key `{key}`")

    allowed_top = set(schema.get("properties", {}).keys())
    extra_top = set(data.keys()) - allowed_top
    if extra_top:
        raise SystemExit(f"Validation failed: extra top-level keys: {sorted(extra_top)}")

    mode_enum = schema["properties"]["splitter_mode"]["enum"]
    if data["splitter_mode"] not in mode_enum:
        raise SystemExit(f"Validation failed: bad splitter_mode `{data['splitter_mode']}`")

    item_schema = schema["properties"]["items"]["items"]
    req_item = item_schema["required"]
    item_props = item_schema["properties"]
    qtype_enum = set(item_props["question_type"]["enum"])
    qtopic_enum = set(item_props["question_topic"]["enum"])
    stage_enum = set(item_props["interview_stage"]["enum"])
    allowed_item = set(item_props.keys())

    if not isinstance(data["items"], list):
        raise SystemExit("Validation failed: `items` must be a list")

    def _is_allowed_type(value: Any, allowed_types: list[str]) -> bool:
        type_checks: dict[str, Any] = {
            "string": lambda v: isinstance(v, str),
            "null": lambda v: v is None,
            "object": lambda v: isinstance(v, dict),
            "array": lambda v: isinstance(v, list),
            "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
            "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
            "boolean": lambda v: isinstance(v, bool),
        }
        return any(type_checks[t](value) for t in allowed_types if t in type_checks)

    linked_field_schemas = {
        "interviewer_question": item_props["interviewer_question"],
        "candidate_answer": item_props["candidate_answer"],
        "reference_answer": item_props["reference_answer"],
        "interviewer_feedback": item_props["interviewer_feedback"],
    }

    for i, item in enumerate(data["items"], start=1):
        missing = [k for k in req_item if k not in item]
        if missing:
            raise SystemExit(f"Validation failed: item #{i} missing fields: {missing}")
        extra = set(item.keys()) - allowed_item
        if extra:
            raise SystemExit(f"Validation failed: item #{i} has extra fields: {sorted(extra)}")
        if item["question_type"] not in qtype_enum:
            raise SystemExit(f"Validation failed: item #{i} bad question_type `{item['question_type']}`")
        if item["question_topic"] not in qtopic_enum:
            raise SystemExit(f"Validation failed: item #{i} bad question_topic `{item['question_topic']}`")
        if item["interview_stage"] not in stage_enum:
            raise SystemExit(
                f"Validation failed: item #{i} bad interview_stage `{item['interview_stage']}`"
            )
        for linked_key, linked_schema in linked_field_schemas.items():
            linked = item.get(linked_key)
            if not isinstance(linked, dict):
                raise SystemExit(f"Validation failed: item #{i} `{linked_key}` must be an object")
            if set(linked.keys()) != {"text", "time"}:
                raise SystemExit(
                    f"Validation failed: item #{i} `{linked_key}` must contain only `text` and `time`"
                )
            text_allowed = linked_schema["properties"]["text"]["type"]
            time_allowed = linked_schema["properties"]["time"]["type"]
            text_allowed = text_allowed if isinstance(text_allowed, list) else [text_allowed]
            time_allowed = time_allowed if isinstance(time_allowed, list) else [time_allowed]
            if not _is_allowed_type(linked.get("text"), text_allowed):
                raise SystemExit(
                    f"Validation failed: item #{i} `{linked_key}.text` has invalid type/value"
                )
            if not _is_allowed_type(linked.get("time"), time_allowed):
                raise SystemExit(
                    f"Validation failed: item #{i} `{linked_key}.time` has invalid type/value"
                )


def main() -> None:
    root = Path.cwd()
    run_config = _load_run_config(root)

    parser = argparse.ArgumentParser(
        description="Run splitter extraction through Anthropic API.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--source-id", required=True, help="Unique source id for output JSON")
    parser.add_argument("--mode", choices=["raw_split", "mock_assisted_split"], required=True)
    parser.add_argument("--transcript", required=True, help="Path to transcript.txt")
    parser.add_argument("--timecodes", default=None, help="Path to timecodes.txt (mock_assisted only)")
    parser.add_argument("--video", default=None, help="Path to video.md (mock_assisted only)")
    parser.add_argument("--feedback", default=None, help="Path to feedback.md (mock_assisted only)")
    parser.add_argument(
        "--system-prompt",
        default=run_config.get("system_prompt", "labeling/prompts/system_prompt_v2.txt"),
        help="Path to system prompt",
    )
    parser.add_argument(
        "--user-prompt",
        default=None,
        help="Path to user prompt template (resolved from config by mode if omitted)",
    )
    parser.add_argument(
        "--schema",
        default=run_config.get("schema", "labeling/prompts/splitter_output_schema_v1.json"),
        help="Path to splitter schema JSON",
    )
    parser.add_argument("--out", required=True, help="Path to output JSON file")
    parser.add_argument(
        "--model",
        default=run_config.get("model"),
        help="Anthropic model name (defaults to value in splitter_run_config.json)",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=run_config.get("max_tokens", 16000),
    )
    args = parser.parse_args()

    if not args.model:
        raise SystemExit(
            "No model specified. Set `model` in labeling/config/splitter_run_config.json or pass --model."
        )

    try:
        import anthropic  # type: ignore
    except ImportError as exc:
        raise SystemExit("Dependency missing. Install with: pip install anthropic") from exc

    system_prompt_path = root / args.system_prompt
    user_prompt_path = (
        (root / args.user_prompt)
        if args.user_prompt
        else _resolve_user_prompt(args.mode, run_config, root)
    )
    schema_path = root / args.schema
    transcript_path = root / args.transcript
    out_path = root / args.out

    system_prompt = _load_text(system_prompt_path)
    user_prompt = _load_text(user_prompt_path)
    schema_text = _load_text(schema_path)
    transcript_text = _load_text(transcript_path)

    payload_blocks = [
        f"SOURCE_ID: {args.source_id}",
        f"SPLITTER_MODE: {args.mode}",
        "TRANSCRIPT_TXT:",
        transcript_text,
    ]

    sidecars_used: dict[str, str] = {}
    if args.mode == "mock_assisted_split":
        for flag, label in [
            (args.timecodes, "TIMECODES_TXT"),
            (args.video, "VIDEO_MD"),
            (args.feedback, "FEEDBACK_MD"),
        ]:
            if flag:
                content = _load_text(root / flag)
                payload_blocks.extend([f"{label}:", content])
                sidecars_used[label] = flag

    user_content = (
        user_prompt.strip()
        + "\n\n"
        + "Important: output must validate against this schema.\n"
        + schema_text
        + "\n\n"
        + "\n".join(payload_blocks)
    )

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("ANTHROPIC_API_KEY is not set")

    run_ts = datetime.now(timezone.utc).isoformat()
    manifest: dict[str, Any] = {
        "run_timestamp_utc": run_ts,
        "model": args.model,
        "temperature": run_config.get("temperature", 0),
        "max_tokens": args.max_tokens,
        "mode": args.mode,
        "source_id": args.source_id,
        "paths": {
            "system_prompt": str(system_prompt_path.relative_to(root)),
            "user_prompt": str(user_prompt_path.relative_to(root)),
            "schema": str(schema_path.relative_to(root)),
            "transcript": str(transcript_path.relative_to(root)),
            "output": str(out_path.relative_to(root)),
        },
        "prompt_hashes": {
            "system_prompt_sha256": _sha256_short(system_prompt),
            "user_prompt_sha256": _sha256_short(user_prompt),
            "schema_sha256": _sha256_short(schema_text),
            "transcript_sha256": _sha256_short(transcript_text),
        },
        "sidecars": sidecars_used,
    }

    print("Run config:")
    print(f"  model:         {args.model}")
    print(f"  mode:          {args.mode}")
    print(f"  temperature:   {run_config.get('temperature', 0)}")
    print(f"  system_prompt: {system_prompt_path}")
    print(f"  user_prompt:   {user_prompt_path}")
    print(f"  schema:        {schema_path}")
    print(f"  transcript:    {transcript_path}")
    print(f"  output:        {out_path}")

    client = anthropic.Anthropic(api_key=api_key)
    resp = client.messages.create(
        model=args.model,
        max_tokens=args.max_tokens,
        temperature=run_config.get("temperature", 0),
        system=system_prompt,
        messages=[{"role": "user", "content": user_content}],
    )

    if not resp.content:
        raise SystemExit("Empty model response")
    text_parts = [part.text for part in resp.content if getattr(part, "type", "") == "text"]
    raw_output = "\n".join(text_parts).strip()
    data = _extract_json(raw_output)

    schema = json.loads(schema_text)
    _validate_against_schema(data, schema)

    manifest["items_count"] = len(data.get("items", []))
    manifest["validation"] = "passed"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    manifest_path = out_path.with_suffix("").with_suffix(".run_manifest.json")
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Saved validated splitter JSON: {out_path}")
    print(f"Saved run manifest:            {manifest_path}")


if __name__ == "__main__":
    main()
