#!/usr/bin/env python3
"""
Splitter (mocked) — детерминированный компонент AR-pipeline.

Категория: cross-cutting детерм. компонент (md/arch_agents.md §3.1, §4.2),
симметричный KBRetriever / EvalLogger / HighlighterRenderer.

Контракт:
- stdin: не используется
- argv: <folder> [--fixture <path>]
- stdout: JSON-сериализованный QA[] (схема md/arch_agents.md §5.1)
- stderr: диагностика (счётчики, валидация)
- exit code: 0 = OK, 2 = фикстуры нет, 3 = схема нарушена

Заменяется реальным Splitter-агентом (Phase 1, см. md/arch_agents.md §7)
без изменения контракта вывода — orchestrator переключает только Шаг 2.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

QUESTION_TYPE_VALUES = {"hard_skill", "soft_skill", "behavioral", "hard", "soft"}
INTERVIEW_STAGE_VALUES = {
    "fit_hr",
    "hr_screening",
    "technical_qna",
    "tech_qa",
    "technical_coding",
    "tech_coding",
    "technical_case",
    "tech_case",
    "system_design",
    "behavioral",
    "manager_round",
}

LINKED_TEXT_KEYS = ("text", "transcript_time")
QA_REQUIRED_KEYS = ("question", "candidate_answer", "type", "interview_stage", "topic_tag")


def _err(msg: str) -> None:
    print(f"[splitter-stub] {msg}", file=sys.stderr)


def _validate_linked_text(value: object, path: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(value, dict):
        errors.append(f"{path}: ожидается object, получено {type(value).__name__}")
        return errors
    for key in LINKED_TEXT_KEYS:
        if key not in value:
            errors.append(f"{path}.{key}: отсутствует")
        elif not isinstance(value[key], str):
            errors.append(f"{path}.{key}: ожидается string, получено {type(value[key]).__name__}")
    return errors


def _validate_qa_item(item: object, idx: int) -> list[str]:
    errors: list[str] = []
    if not isinstance(item, dict):
        errors.append(f"qa[{idx}]: ожидается object, получено {type(item).__name__}")
        return errors

    for key in QA_REQUIRED_KEYS:
        if key not in item:
            errors.append(f"qa[{idx}].{key}: отсутствует")

    if "question" in item:
        errors.extend(_validate_linked_text(item["question"], f"qa[{idx}].question"))
    if "candidate_answer" in item:
        errors.extend(_validate_linked_text(item["candidate_answer"], f"qa[{idx}].candidate_answer"))

    if "type" in item:
        if not isinstance(item["type"], str):
            errors.append(f"qa[{idx}].type: ожидается string")
        elif item["type"] not in QUESTION_TYPE_VALUES:
            errors.append(
                f"qa[{idx}].type: '{item['type']}' не из {sorted(QUESTION_TYPE_VALUES)}"
            )

    if "interview_stage" in item and isinstance(item["interview_stage"], str):
        if item["interview_stage"] not in INTERVIEW_STAGE_VALUES:
            errors.append(
                f"qa[{idx}].interview_stage: '{item['interview_stage']}' не из {sorted(INTERVIEW_STAGE_VALUES)}"
            )

    if "topic_tag" in item and not isinstance(item["topic_tag"], str):
        errors.append(f"qa[{idx}].topic_tag: ожидается string")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Splitter (mocked) — читает qa.json и возвращает QA[] по схеме arch_agents §5.1."
    )
    parser.add_argument("folder", help="Папка интервью (содержит qa.json по умолчанию).")
    parser.add_argument(
        "--fixture",
        help="Override пути к фикстуре. Если не задан — используется <folder>/qa.json.",
        default=None,
    )
    args = parser.parse_args()

    folder = Path(args.folder)
    fixture = Path(args.fixture) if args.fixture else folder / "qa.json"

    if not fixture.is_file():
        _err(
            f"фикстура не найдена: {fixture}. "
            "Phase 1 Splitter не интегрирован; положи qa.json в папку интервью или передай --fixture "
            "(см. md/arch_agents.md §7 Phase 1)."
        )
        return 2

    try:
        raw = fixture.read_text(encoding="utf-8")
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        _err(f"невалидный JSON в {fixture}: {exc}")
        return 3

    if not isinstance(data, list):
        _err(f"top-level в {fixture} ожидается array, получено {type(data).__name__}")
        return 3

    all_errors: list[str] = []
    for idx, item in enumerate(data):
        all_errors.extend(_validate_qa_item(item, idx))

    if all_errors:
        _err(f"схема QA[] нарушена ({len(all_errors)} ошибок):")
        for err in all_errors:
            _err(f"  - {err}")
        return 3

    type_counts: dict[str, int] = {}
    for item in data:
        type_counts[item["type"]] = type_counts.get(item["type"], 0) + 1
    counts_str = ", ".join(f"{t}={c}" for t, c in sorted(type_counts.items()))
    _err(f"read {len(data)} items from {fixture}; types: {counts_str}; validation: OK")

    json.dump(data, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
