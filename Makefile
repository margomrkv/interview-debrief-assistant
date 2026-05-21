# Makefile — запуск UI (src/ui/app.py). См. docs/spec/ui.md и src/ui/README.md.
#
# Бэкенды:
#   emulator — проигрывает заранее посчитанные данные (data/emulator-data), без LLM
#   live     — реальный пайплайн: Splitter (1 запрос) + Scoring (N запросов) через LLM
#
# Порт переопределяется: make ui-live PORT=8011

PYTHON ?= uv run python
APP    := src/ui/app.py

# Обучение: src/kb/kb.py (build_splits → MIPROv2 train → evaluate).
# Доп. флаги через ARGS, напр.: make train ARGS="--num-trials 5 --prompt-model sonnet"
TRAIN := src/kb/kb.py
ARGS  ?=

.PHONY: ui ui-emulator ui-live train train-smoke

## ui: запустить UI в режиме эмулятора (по умолчанию)
ui: ui-emulator

## ui-emulator: UI на данных из data/emulator-data (без вызовов модели)
ui-emulator:
	$(PYTHON) $(APP) 18000

## ui-live: UI с реальным LLM-бэкендом (Splitter + per-item Scoring)
ui-live:
	UI_BACKEND=live $(PYTHON) $(APP) 18100

## train: полный прогон обучения evaluator-промпта (платная модель!) → runs/<run_id>/
train:
	$(PYTHON) $(TRAIN) $(ARGS)

## train-smoke: быстрый дешёвый цикл (2 source_id, 17/7 QA) для проверки пайплайна
train-smoke:
	$(PYTHON) $(TRAIN) --smoke $(ARGS)
