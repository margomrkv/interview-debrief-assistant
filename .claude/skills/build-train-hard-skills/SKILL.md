---
name: build-train-hard-skills
description: Запускает `build_train_hard_skills.py` — собирает `train/hard_skills.json` из `data/knowledgebase/splitted/**/*.v*.qa-split.json`. Берёт последнюю версию (vN) на каждый source_id, фильтрует `question_type in {"hard", "technical_qna"}`, дополняет каждый item полем `source_id`. Аргументов не принимает; перезапись идемпотентна.
author: claude-code-opus-4-7
created_date: 2026-05-16
---

# Skill: Сборка train/hard_skills.json

## Версия

Текущая версия 1.0. Включай версию в summary, который скилл показывает пользователю.

## Назначение

Один прогон → один артефакт `train/hard_skills.json` для обучения `ScoringPromptTrainer` (см. `md/train.md` §Обучение). Это **первый шаг** воркфлоу train: собираем плоский корпус hard-skill Q&A из всех splitter-артефактов, чтобы дальше его можно было размечать как golden set.

Скилл — тонкая обёртка над `.claude/skills/build-train-hard-skills/build_train_hard_skills.py`. Логику сборки в SKILL.md не дублируем: она целиком живёт в скрипте.

## Соответствие train.md

Скилл закрывает один атомарный шаг подготовки данных, упомянутый в `md/train.md`:

> Строится golden set (ручная разметка эталонных оценок по подмножеству Q&A).
> Разбиение train / test на уровне целых mock-сессий (чтобы не протекали коррелированные ответы из одного диалога).

Сам корпус Q&A до этого жил россыпью в `data/knowledgebase/splitted/`. Скилл собирает его в один файл с явным `source_id` на каждом item — это нужно и для последующей разметки, и для группировки при `train/test` split'е по сессиям.

Что **не** делает скилл (вне scope):
- ручную разметку golden set (clarity / completeness / accuracy);
- `train/test` split — это отдельный шаг, когда корпус уже размечен;
- оптимизацию промпта-оценщика по MAPE;
- генерацию `reference_answer` для item'ов, где он `null`.

## Вход

**Без аргументов.** Все параметры захардкожены в скрипте; для изменения — править скрипт (см. «Расширение» ниже).

## Конфигурация

- **Рабочий каталог:** корень репо (`git rev-parse --show-toplevel`).
- **Скрипт:** `.claude/skills/build-train-hard-skills/build_train_hard_skills.py` (Python 3, только stdlib — без `uv run`, без deps).
- **Вход:** `data/knowledgebase/splitted/**/*.v*.qa-split.json` (новый нейминг, регулярка `\.v(\d+)\.qa-split\.json$`) + legacy `data/knowledgebase/splitted/**/*.qa-split.v*.json` (регулярка `\.qa-split\.v(\d+)\.json$`). Рекурсивный обход подпапок (`mock-interviews/<publisher>/<leaf>/`).
- **Выход:** `{project_dir}/train/hard_skills.json`. Папка `train/` создаётся, если её нет.
- **Фильтры внутри скрипта (захардкожены):**
  - `question_type in ACCEPTED_QUESTION_TYPES` (`{"hard", "technical_qna"}`);
  - на каждый `source_id` — запись с максимальным `vN`;
  - item без `source_id` в файле — пропуск с `WARN` (на практике не встречается).

## Артефакт

`train/hard_skills.json` со структурой:

```json
{
  "split_strategy": "по source_id (см. md/train.md §Обучение)",
  "items": [
    {
      "source_id": "<id>",
      "interviewer_question": {"text": "...", "time": "MM:SS"},
      "candidate_answer":     {"text": "...", "time": "MM:SS"},
      "reference_answer":     {"text": "..." | null, "time": "MM:SS" | null},
      "interviewer_feedback": {"text": "..." | null, "time": "MM:SS" | null},
      "question_type": "hard" | "technical_qna",
      "question_topic": "...",
      "interview_stage": "...",
      "grade": "junior" | "middle" | "senior"
    }
  ]
}
```

Item-схема идентична items в `data/knowledgebase/splitted/**/*.v*.qa-split.json`, плюс одно добавленное поле `source_id` (в начале каждого item) и `grade` (в конце, из имени leaf-папки).

## Алгоритм

### Шаг 1: Проверка предусловий

- Текущий каталог = корень репо (если нет — `cd $(git rev-parse --show-toplevel)`).
- Существует `data/knowledgebase/splitted/` с файлами `*.v*.qa-split.json` (>0 штук, рекурсивно). Если нет — остановиться с понятным сообщением: «нет splitter-артефактов для сборки».
- Существует `.claude/skills/build-train-hard-skills/build_train_hard_skills.py`. Если нет — остановиться: «скрипт не найден, скилл не может работать».

### Шаг 2: Запуск

```bash
python3 .claude/skills/build-train-hard-skills/build_train_hard_skills.py
```

Stdout у скрипта пустой; **вся сводка идёт в stderr**. Bash-вызов нужно сделать так, чтобы захватить stderr (`python3 .claude/skills/build-train-hard-skills/build_train_hard_skills.py 2>&1`). Таймаут — дефолтный (скрипт быстрый: <1 сек на ~30 файлах).

### Шаг 3: Парсинг сводки скрипта

Скрипт печатает в stderr блок вида (строки `WARN:` появляются только при проблемах и могут отсутствовать):

```
============================================================
written: train/hard_skills.json
total hard items: <N>
sources with hard items: <K>
  <source_id>                  <count>
  ...
skipped (0 hard items): <M>
  <source_id> (v<N>)
  ...
WARN: no grade in folder name (<G>):
  <source_id> (folder: <leaf-folder>)
  ...
```

Из этого блока вытащить:
- `total_items` = число после `total hard items:` (включает `hard` + `technical_qna`);
- `sources_with_hard` = число после `sources with hard items:` + сам список;
- `skipped_zero_hard` = число после `skipped (0 hard items):` + сам список;
- `missing_grade` = строки после `WARN: no grade in folder name`, если есть (grade не распарсился из имени leaf-папки → в item'е `grade: null`).

Сообщения скрипта исторически говорят «hard items», но фактически считают все `ACCEPTED_QUESTION_TYPES`.

### Шаг 4: Sanity-check

После записи прогнать минимальную валидацию:

```bash
python3 -c "
import json
from collections import Counter
d = json.load(open('train/hard_skills.json'))
items = d['items']
accepted = {'hard', 'technical_qna'}
assert all(i['question_type'] in accepted for i in items), 'unexpected question_type leaked'
assert all('source_id' in i for i in items), 'item without source_id'
sources = {i['source_id'] for i in items}
print(f'OK: {len(items)} items, {len(sources)} sources; by type: {dict(Counter(i[\"question_type\"] for i in items))}')
"
```

Если sanity-check падает — показать ошибку пользователю и **не** перезаписывать (но скрипт уже записал — значит, валидация раньше была невозможна; это сигнал что скрипт сломан, надо чинить его).

### Шаг 5: Отчёт пользователю

Короткий отчёт в одном сообщении:

```
build-train-hard-skills v1.0

wrote: train/hard_skills.json
total: <N> items from <K> sources  (<hard> hard + <technical_qna> technical_qna)

per-source:
  <source_id>                                <count>
  ...

skipped (0 accepted items in latest version): <M> файлов
  - <source_id> (v<vN>)
  - ...

missing grade (если есть): <G>
  - <source_id> (folder: <leaf-folder>)
```

## Расширение

Скилл намеренно без аргументов в v1. Если в будущем понадобится:

- **Другой `question_type`** (`soft` / `behavioral` / `system_design` / …) → дописать в `ACCEPTED_QUESTION_TYPES` в скрипте; если нужен отдельный артефакт — добавить аргумент `--type` и сделать output-имя функцией от type (`train/soft_skills.json` и т.п.).
- **Исключить какой-то `source_id`** → завести в скрипте множество-blacklist и фильтровать по нему (сейчас такого фильтра нет — берутся все source'ы).
- **Другая папка с splitter-артефактами** → параметризовать `SPLITTER_DIR` (сейчас захардкожена в скрипте).
- **Включать annotation.v\*.json как источник оценок** → отдельная задача и отдельный output-файл; не путать с текущим скиллом.

Любое из этих расширений = обновление и SKILL.md, и скрипта одной правкой. Не делать «на всякий случай».

## Нюансы

- Скрипт выбирает «последнюю версию» по числу `vN` в имени файла (`...v7.qa-split.json`), а не по дате. Если когда-нибудь появится `v10` — он корректно победит `v9` (целочисленное сравнение, не лексикографическое).
- Item с `reference_answer == null` и `interviewer_feedback == null` — норма (≈9% корпуса). Скилл их не отбрасывает: это входит в корпус и для них golden score придётся ставить опираясь только на знания судьи-LLM.
- Поле `source_id` дописывается **в начало** item'а (через `{"source_id": ..., **item}`), чтобы при ручном просмотре JSON он был сразу виден.

## Ограничения

- Один прогон = один результат. Без батча.
- Только `question_type in {"hard", "technical_qna"}`. Для других — см. «Расширение».
- Не делает train/test split — для этого пиши отдельный скилл/скрипт, когда golden set будет размечен.
- Не валидирует, что splitter-разбивка хорошая (это работа `splitter_validate_video` из скилла `splitter`).

## Пример сессии

```
user: /build-train-hard-skills
assistant:
  [precheck] data/knowledgebase/splitted/ есть, *.v*.qa-split.json присутствуют; скрипт на месте.
  [run] python3 .claude/skills/build-train-hard-skills/build_train_hard_skills.py
  [parse] total=175, sources=17, skipped(zero accepted)=6
  [sanity] OK: 175 items, 17 sources; by type: {'technical_qna': 74, 'hard': 101}

  build-train-hard-skills v1.0
  wrote: train/hard_skills.json
  total: 175 items from 17 sources  (101 hard + 74 technical_qna)
  per-source:
    data_scientist_junior_karpov_2022_03_30                      35
    ml_engineer_junior_karpov_2023_03_09                         22
    data_analyst_junior_karpov_vyacheslav_2021_06_24             19
    product_analyst_middle_avito_avito_2024_04_04                16
    data_analyst_junior_karpov_pasha_2021_06_24                  15
    game_analyst_middle_karpov_2021_11_20                        15
    ...
  skipped (0 accepted items): 6 файлов (ab-тесты / behavioral_v1 / system-design v1..v4)
```
