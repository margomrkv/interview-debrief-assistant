#!/usr/bin/env python3
"""Optional headless step 5: calls litellm with ANTHROPIC_API_KEY.

In Cursor, step 5 runs like step 2 — the agent reads LLM_INPUT_STEP_5 from
pipeline-log.md and uses the subscription model (no shell API key).
Use this script only for CI/automation without an IDE agent.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
SKILL_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_DIR / "step4-validate-chapters"))
sys.path.insert(0, str(SKILL_DIR))

from run_manifest import _LLM_SECTION_RE  # noqa: E402

from splitter_validate_chapters import (  # noqa: E402
    save_semantic_json_to_report,
)


def _load_llm_step5_payload(pipeline_log: Path) -> tuple[str, str]:
    text = pipeline_log.read_text(encoding="utf-8")
    m = None
    for candidate in _LLM_SECTION_RE.finditer(text):
        if candidate.group("step") == "5":
            m = candidate
            break
    if not m:
        raise RuntimeError(
            f"No LLM_INPUT_STEP_5 in {pipeline_log}. Run splitter_post.sh with --video first."
        )
    body = m.group(0)
    fence = re.search(r"```(?:text)?\s*\n(.*?)```", body, re.DOTALL)
    if fence:
        body = fence.group(1)
    sys_m = re.search(
        r"={70}\s*SYSTEM\s*={70}\s*(?P<sys>.*?)(?=\s*={70}\s*OUTPUT SCHEMA)",
        body,
        re.DOTALL,
    )
    user_m = re.search(
        r"={70}\s*CHAPTERS TO VALIDATE\s*={70}\s*(?P<user>.*?)(?=\s*SAVE JSON:|\s*={70}\s*RUNTIME_HINTS)",
        body,
        re.DOTALL,
    )
    if not sys_m or not user_m:
        raise RuntimeError("Could not parse step-5 payload (SYSTEM / CHAPTERS sections).")
    return sys_m.group("sys").strip(), user_m.group("user").strip()


def _model_id_from_run_config() -> tuple[str, float]:
    cfg_path = SKILL_DIR / "step1-prepare" / "run_config.json"
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    vi = cfg.get("validation_inference") or cfg.get("inference") or {}
    model = vi.get("model", "claude-sonnet-4-6")
    temp = float(vi.get("temperature", 0))
    if "/" not in model:
        model = f"anthropic/{model}"
    return model, temp


def _call_llm(system: str, user: str, model: str, temperature: float) -> dict:
    import litellm

    resp = litellm.completion(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        temperature=temperature,
    )
    raw = (resp.choices[0].message.content or "").strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    return json.loads(raw)


def _revalidate(json_path: Path, video_path: Path, report_path: Path, section_config: str | None) -> None:
    cmd = [
        sys.executable,
        str(SKILL_DIR / "step4-validate-chapters" / "splitter_validate_video.py"),
        "--splitter",
        str(json_path),
        "--video",
        str(video_path),
        "--out",
        str(report_path),
        "--prepare-llm",
    ]
    if section_config:
        cmd.extend(["--section-config", section_config])
    subprocess.run(cmd, check=True, cwd=str(REPO_ROOT))


def main() -> int:
    parser = argparse.ArgumentParser(description="Splitter step 5: semantic LLM validation")
    parser.add_argument("--json", required=True, help="Path to *.qa-split.json")
    parser.add_argument("--video", required=True, help="Path to video.md")
    parser.add_argument("--report", help="Path to validation-report.md (default: derive from json)")
    parser.add_argument("--pipeline-log", help="Path to pipeline-log.md (default: derive from json)")
    parser.add_argument("--section-config", help="Same as validate_video --section-config")
    parser.add_argument(
        "--skip-if-no-key",
        action="store_true",
        default=True,
        help="Exit 0 if ANTHROPIC_API_KEY missing (default: true)",
    )
    args = parser.parse_args()

    json_path = Path(args.json)
    if not json_path.is_absolute():
        json_path = REPO_ROOT / json_path
    video_path = Path(args.video)
    if not video_path.is_absolute():
        video_path = REPO_ROOT / video_path

    from artifact_paths import (  # noqa: WPS433
        pipeline_log_md_from_json,
        validation_report_from_json,
    )

    if args.report:
        report_path = Path(args.report)
        if not report_path.is_absolute():
            report_path = REPO_ROOT / report_path
    else:
        report_path = validation_report_from_json(json_path)

    pipeline_log = (
        Path(args.pipeline_log)
        if args.pipeline_log
        else pipeline_log_md_from_json(json_path)
    )
    if not pipeline_log.is_absolute():
        pipeline_log = REPO_ROOT / pipeline_log

    if not os.getenv("ANTHROPIC_API_KEY"):
        if args.skip_if_no_key:
            os.environ["SPLITTER_STEP5_SKIPPED"] = "нет `ANTHROPIC_API_KEY` в окружении"
            _revalidate(json_path, video_path, report_path, args.section_config)
            print("Step 5 skipped (no ANTHROPIC_API_KEY); validation report refreshed.")
            return 0
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        return 1

    system, user = _load_llm_step5_payload(pipeline_log)
    model, temp = _model_id_from_run_config()
    print(f"Step 5 LLM: {model} (temperature={temp})")
    data = _call_llm(system, user, model, temp)
    save_semantic_json_to_report(report_path, data)
    _revalidate(json_path, video_path, report_path, args.section_config)
    print(f"Step 5 done; report updated: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
