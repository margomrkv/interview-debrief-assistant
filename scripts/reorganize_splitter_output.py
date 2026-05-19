#!/usr/bin/env python3
"""One-shot migration: flat splitter_output/ → mock-interviews|real-interviews/<publisher>/<slug>/.

Naming: {slug}.qa-split[.<artifact>].v{N}.{ext}
Deletes: *.annotation.*, Excel ~$ locks, template.* raw bundles.
Merges duplicate interviews; junior_data_scientist v1 → v5 on canonical junior DS folder.
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "splitter_output"

# legacy source_id → transcripts path (leaf parent = publisher dir)
OLD_TO_REL: dict[str, str] = {
    "avito_product_analyst_middle_20240404": "mock-interviews/avito/mock-product-analyst-middle-avito-avito-2024-04-04",
    "karpov_junior_ds_20220330": "mock-interviews/karpov/mock-data-scientist-junior-karpov-2022-03-30",
    "junior_data_scientist_собеседование_karpov_courses_20220330": "mock-interviews/karpov/mock-data-scientist-junior-karpov-2022-03-30",
    "karpov_junior_ml_20230309": "mock-interviews/karpov/mock-ml-engineer-junior-karpov-2023-03-09",
    "karpov_middle_ds_ml_20220626": "mock-interviews/karpov/mock-data-scientist-middle-karpov-ml-2022-06-26",
    "karpov_middle_ds_python_20220702": "mock-interviews/karpov/mock-data-scientist-middle-karpov-python-2022-07-02",
    "junior_аналитик_данных_собеседование_karpov_courses_20210913_sasha": "mock-interviews/karpov/mock-data-analyst-junior-karpov-sasha-2021-09-13",
    "junior_аналитик_данных_собеседование_karpov_courses_20210913_yegor": "mock-interviews/karpov/mock-data-analyst-junior-karpov-yegor-2021-09-13",
    "karpov_product_analyst_junior_vyacheslav_20210624": "mock-interviews/karpov/mock-data-analyst-junior-karpov-vyacheslav-2021-06-24",
    "karpov_product_analyst_junior_20210624_pasha": "mock-interviews/karpov/mock-data-analyst-junior-karpov-pasha-2021-06-24",
    "karpov_product_analyst_junior_20210624": "mock-interviews/karpov/mock-data-analyst-junior-karpov-pasha-2021-06-24",
    "karpov_senior_da_babushkin_20240523": "mock-interviews/karpov/mock-data-analyst-senior-karpov-2024-05-23",
    "karpov_игровой_аналитик_20211120": "mock-interviews/karpov/mock-game-analyst-middle-karpov-2021-11-20",
    "karpov_behavioral_v1_20221110": "mock-interviews/karpov/mock-behavioral-senior-karpov-v1-2022-11-10",
    "karpov_behavioral_v2_20221215": "mock-interviews/karpov/mock-behavioral-senior-karpov-v2-2022-12-15",
    "karpov_behavioral_v3_20230121": "mock-interviews/karpov/mock-behavioral-senior-karpov-v3-2023-01-21",
    "karpov_ml_sysdesign_v1_20210803": "mock-interviews/karpov/mock-ml-system-design-senior-karpov-v1-2021-08-03",
    "karpov_ml_sysdesign_v2_20210828": "mock-interviews/karpov/mock-ml-system-design-senior-karpov-v2-2021-08-28",
    "karpov_ml_sysdesign_v3_20210919": "mock-interviews/karpov/mock-ml-system-design-senior-karpov-v3-2021-09-19",
    "karpov_system_design_v1_20220119": "mock-interviews/karpov/mock-system-design-senior-karpov-v1-2022-01-19",
    "karpov_system_design_v2_20220228": "mock-interviews/karpov/mock-system-design-senior-karpov-v2-2022-02-28",
    "karpov_system_design_v3_20220324": "mock-interviews/karpov/mock-system-design-senior-karpov-v3-2022-03-24",
    "karpov_system_design_v4_20220505": "mock-interviews/karpov/mock-system-design-senior-karpov-v4-2022-05-05",
    "karpov_system_design_babushkin_20230714": "mock-interviews/karpov/mock-system-design-senior-karpov-2023-07-14",
    "karpov_ab_тесты_babushkin_20240119": "mock-interviews/karpov/mock-ab-testing-senior-karpov-2024-01-19",
    "amazon_business_intelligence_mock_interview_duplicate_products_20200529": "mock-interviews/interview-query/mock-business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29",
}

# duplicate source_id: remap version (old v1 of duplicate → last+1)
VERSION_REMAP: dict[tuple[str, int], int] = {
    ("junior_data_scientist_собеседование_karpov_courses_20220330", 1): 5,
}

SPLITTER_MOCK = re.compile(
    r"^(?P<sid>.+)\.splitter\.v(?P<ver>\d+)\.mock\.(?P<tail>.+)$"
)
SPLITTER_PLAIN = re.compile(r"^(?P<sid>.+)\.splitter\.v(?P<ver>\d+)\.(?P<tail>json|xlsx)$")
PROMPT_ONLY = re.compile(r"^(?P<sid>.+)\.prompt\.txt$")


def slug_from_rel(rel: str) -> str:
    return rel.rsplit("/", 1)[-1]


def source_id_from_slug(slug: str) -> str:
    return slug.replace("-", "_")


def new_name(slug: str, artifact: str | None, version: int | None, ext: str) -> str:
    if artifact == "prompt":
        return f"{slug}.qa-split.prompt.txt"
    if version is None:
        raise ValueError("version required")
    if artifact is None:
        return f"{slug}.qa-split.v{version}.{ext}"
    return f"{slug}.qa-split.{artifact}.v{version}.{ext}"


def map_artifact(tail: str) -> tuple[str | None, str]:
    if tail == "json":
        return None, "json"
    if tail == "xlsx":
        return None, "xlsx"
    if tail == "validation.md":
        return "validation", "md"
    if tail == "user_prompt.txt":
        return "user-prompt", "txt"
    if tail == "splitter_llm_input.txt":
        return "llm-input", "txt"
    raise ValueError(f"unknown tail: {tail}")


def parse_file(name: str) -> tuple[str, ...]:
    if name == ".gitkeep":
        return ("keep",)
    if name.startswith("~$"):
        return ("delete", "excel-lock")
    if name.startswith("template."):
        return ("delete", "template")
    if ".annotation." in name:
        return ("delete", "annotation")
    m = PROMPT_ONLY.match(name)
    if m:
        return ("move", m.group("sid"), "prompt", 0)
    m = SPLITTER_MOCK.match(name)
    if m:
        return ("move", m.group("sid"), m.group("ver"), m.group("tail"))
    m = SPLITTER_PLAIN.match(name)
    if m:
        return ("move", m.group("sid"), m.group("ver"), m.group("tail"))
    return ("unknown", name)


def remap_version(sid: str, ver: int) -> int:
    key = (sid, ver)
    if key in VERSION_REMAP:
        return VERSION_REMAP[key]
    return ver


def patch_json(path: Path, slug: str) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    new_sid = source_id_from_slug(slug)
    if data.get("source_id") != new_sid:
        data["source_id"] = new_sid
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def patch_validation(path: Path, slug: str, version: int) -> None:
    text = path.read_text(encoding="utf-8")
    rel_dir = path.parent.relative_to(REPO)
    base = f"{slug}.qa-split"
    repl = {
        f"{base}.v{version}.json": f"{rel_dir}/{base}.v{version}.json",
        f"{base}.v{version}.xlsx": f"{rel_dir}/{base}.v{version}.xlsx",
    }
    # replace old labeling/data and splitter_output flat paths
    for old_line in text.splitlines():
        if "labeling/data/" in old_line or "splitter_output/" in old_line:
            pass
    json_name = f"{base}.v{version}.json"
    xlsx_name = f"{base}.v{version}.xlsx"
    text = re.sub(
        r"`[^`]*\.splitter\.v\d+[^`]*\.json`",
        f"`{rel_dir}/{json_name}`",
        text,
    )
    text = re.sub(
        r"`[^`]*\.splitter\.v\d+[^`]*\.xlsx`",
        f"`{rel_dir}/{xlsx_name}`",
        text,
    )
    path.write_text(text, encoding="utf-8")


def main() -> int:
    if not OUT.is_dir():
        print("splitter_output/ missing", file=sys.stderr)
        return 1

    staged: list[tuple[Path, Path, str, int | None]] = []
    deleted: list[str] = []
    unknown: list[str] = []

    for src in sorted(OUT.iterdir()):
        if not src.is_file() or src.parent != OUT:
            continue
        parsed = parse_file(src.name)
        kind = parsed[0]
        if kind == "keep":
            continue
        if kind == "delete":
            src.unlink()
            deleted.append(src.name)
            continue
        if kind == "unknown":
            unknown.append(parsed[1])
            continue

        sid = parsed[1]
        if sid not in OLD_TO_REL:
            unknown.append(src.name)
            continue

        rel = OLD_TO_REL[sid]
        slug = slug_from_rel(rel)
        dest_dir = OUT / rel
        dest_dir.mkdir(parents=True, exist_ok=True)

        if parsed[2] == "prompt":
            dest = dest_dir / new_name(slug, "prompt", None, "txt")
            staged.append((src, dest, slug, None))
            continue

        ver = remap_version(sid, int(parsed[2]))
        artifact_key, ext = map_artifact(parsed[3])
        if artifact_key is None:
            dest = dest_dir / new_name(slug, None, ver, ext)
        else:
            dest = dest_dir / new_name(slug, artifact_key, ver, ext)
        staged.append((src, dest, slug, ver))

    if unknown:
        print("UNKNOWN files (not migrated):", file=sys.stderr)
        for u in unknown:
            print(f"  {u}", file=sys.stderr)
        return 1

    for src, dest, slug, ver in staged:
        if dest.exists():
            if dest.name.endswith(".qa-split.prompt.txt"):
                src.unlink()
                print(f"skip duplicate prompt: {src.name}")
                continue
            print(f"ERROR: target exists: {dest}", file=sys.stderr)
            return 1
        shutil.move(str(src), str(dest))
        if dest.suffix == ".json":
            patch_json(dest, slug)
        elif dest.name.endswith(".validation.md") and ver is not None:
            patch_validation(dest, slug, ver)

    # remove empty flat leftovers except .gitkeep
    for src in list(OUT.iterdir()):
        if src.is_file() and src.name != ".gitkeep":
            print(f"WARN: leftover file: {src.name}", file=sys.stderr)

    print(f"moved: {len(staged)}")
    print(f"deleted: {len(deleted)}")
    for d in deleted:
        print(f"  - {d}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
