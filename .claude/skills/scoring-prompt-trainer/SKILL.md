---
name: scoring-prompt-trainer
description: Phase 3 trainer для prompt evaluator'а scoring-evaluator. Тонкая обёртка над `scripts/kb.py`, которая прогоняет build_splits → train → evaluate одним процессом и складывает артефакты в `runs/<run_id>/`.
---

# Skill: Scoring Prompt Trainer

## Назначение

Один прогон = один `build_splits → train → evaluate` цикл MIPROv2 над hard-QA golden set'ом. Все артефакты одного прогона живут в `runs/<run_id>/`, где `run_id = YYYY-MM-DD_HH-MM-SS` (локальная TZ, генерируется внутри пайплайна).

После прогона `runs/<run_id>/evaluator_prompt.md` подключается как system-prompt к субагенту `.claude/agents/scoring-evaluator.md`. Папка `runs/` целиком в `.gitignore`.

## Архитектура

```mermaid
flowchart LR
    CLI["scripts/kb.py<br/>(argparse)"] --> API["src.kb.train.run_kb_pipeline(...)"]
    API --> BS["build_splits()"] --> SP["kb/splits.json"]
    API --> TR["MIPROv2.compile + run_evaluation"]
    TR --> AR["runs/&lt;run_id&gt;/evaluator_prompt.md<br/>train_report.md, logs/*"]
    TR --> ER["runs/&lt;run_id&gt;/eval_&lt;split&gt;.md"]
```

Никаких subprocess'ов — всё в одном процессе. Внутри `src/` нет argparse: CLI живёт только в `scripts/kb.py`.

## Запуск

```bash
python scripts/kb.py [options]
```

Параметры (`python scripts/kb.py --help`):

- `--run-id STR` — переопределить run_id (default: now() в локальной TZ).
- `--smoke` — быстрый цикл: 2 source_id, 17/7 QA (вместо 6/57/24).
- `--num-trials INT` — MIPROv2 num_trials (default 3).
- `--num-candidates INT` — MIPROv2 num_candidates (default: зеркалит num-trials).
- `--prompt-model STR` — proposer LM: `haiku` | `sonnet` | `gpt-4o-mini` | `gemini-flash` | полный id (default: `haiku`).
- `--no-phoenix` — отключить Phoenix UI (JSONL trace всё равно пишется).
- `--eval-splits {test,train,both,none}` — какие split'ы прогнать в evaluate (default: `test`; `none` = пропустить).

## Артефакты одного прогона (`runs/<run_id>/`)

- `evaluator_prompt.md` — обученный system prompt + frontmatter с метриками.
- `train_report.md` — MAE per metric/source, worst-20 cases, bootstrap CI.
- `logs/train.jsonl` — per-call cost/tokens/latency (CostCallback).
- `logs/train.trace.jsonl` — полные prompt+response per LM call (PromptTracer).
- `eval_<split>.md` — отчёт по held-out split'у (MAE per metric/source_id, top-20 worst).

## Прерогативы

- **Phoenix UI** на http://localhost:6006 во время прогона (project: `evaluator-train-<run_id>`). Требует `pip install -e ".[tracing]"`.
- **Прод-инференс** (без held-out test, на одном splitter JSON): `python scripts/ar.py --splitter <path> --prompt runs/<run_id>/evaluator_prompt.md` → `splitter_output/<sid>.scores.json`.
- **Если python падает с ошибкой — не правь сам.** Сообщи о падении.
