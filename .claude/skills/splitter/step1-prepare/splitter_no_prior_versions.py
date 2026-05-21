"""Enforce «no peek at prior qa-split versions» for step 2.

- Step 1 writes an empty stub for the target vN JSON only.
- After step 2, ``check_prior_leak`` fails if output matches any older v*.qa-split.json.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from artifact_paths import parse_json_path

_RE_NEW_JSON = re.compile(r"^(?P<slug>.+)\.v(?P<ver>\d+)\.qa-split\.json$")
_RE_OLD_JSON = re.compile(r"^(?P<slug>.+)\.qa-split\.v(?P<ver>\d+)\.json$")


def prior_qa_split_paths(output_dir: Path, basename: str, current_version: int) -> list[Path]:
    """All qa-split JSON in folder with version < current_version (canonical + legacy names)."""
    found: list[tuple[int, Path]] = []
    for pattern in (
        f"{basename}.v*.qa-split.json",
        f"{basename}.qa-split.v*.json",
    ):
        for f in sorted(output_dir.glob(pattern)):
            parsed = parse_json_path(f)
            if not parsed or parsed[0] != basename:
                continue
            ver = parsed[1]
            if ver < current_version:
                found.append((ver, f.resolve()))
    return [p for _, p in sorted(found, key=lambda x: x[0])]


def write_stub_qa_split(
    path: Path,
    *,
    source_id: str,
    splitter_mode: str,
) -> None:
    """Create target vN JSON with empty items[] so step 2 must fill from transcript."""
    path.parent.mkdir(parents=True, exist_ok=True)
    stub = {
        "source_id": source_id,
        "splitter_mode": splitter_mode,
        "items": [],
    }
    path.write_text(
        json.dumps(stub, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _item_signature(items: list[dict]) -> str:
    """Stable fingerprint for leak detection (questions + answers, not metadata)."""
    parts: list[str] = []
    for it in items:
        q = it.get("interviewer_question") or {}
        a = it.get("candidate_answer") or {}
        parts.append(
            "|".join(
                [
                    str(q.get("time") or ""),
                    (q.get("text") or "").strip(),
                    str(a.get("time") or ""),
                    (a.get("text") or "").strip(),
                ]
            )
        )
    blob = "\n".join(parts)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def load_qa_split(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check_prior_leak(
    current_json: Path,
    *,
    basename: str | None = None,
    version: int | None = None,
) -> tuple[bool, str]:
    """
    Return (ok, message). ok=False if current file matches any prior version fingerprint.
    """
    parsed = parse_json_path(current_json)
    if not parsed:
        return False, f"not a qa-split JSON path: {current_json}"
    bname, ver = parsed
    if basename:
        bname = basename
    if version is not None:
        ver = version

    priors = prior_qa_split_paths(current_json.parent, bname, ver)
    if not priors:
        return True, ""

    try:
        current = load_qa_split(current_json)
    except (json.JSONDecodeError, OSError) as e:
        return False, f"cannot read current JSON: {e}"

    cur_items = current.get("items") or []
    if not cur_items:
        return True, ""  # stub / not yet extracted

    cur_sig = _item_signature(cur_items)
    for prior_path in priors:
        try:
            prior = load_qa_split(prior_path)
        except (json.JSONDecodeError, OSError):
            continue
        prior_items = prior.get("items") or []
        if not prior_items:
            continue
        prior_sig = _item_signature(prior_items)
        if cur_sig == prior_sig:
            pv = parse_json_path(prior_path)
            pver = pv[1] if pv else "?"
            return (
                False,
                f"IDENTICAL to prior v{pver}: {prior_path.name} "
                f"(sha256 items={cur_sig[:12]}…). Step 2 must re-extract from PRIMARY_TRANSCRIPT only.",
            )
    return True, ""
