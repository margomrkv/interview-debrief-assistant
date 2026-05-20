---
name: build-train-hard-skills
description: Запускает `build_train_hard_skills.py` — собирает `train/hard_skills.json` из `splitter_output/**/*.qa-split.v*.json`. Берёт последнюю версию (vN) на каждый source_id, фильтрует `question_type == "hard"`, дополняет каждый item полем `source_id`. Аргументов не принимает; перезапись идемпотентна.
author: claude-code-opus-4-7
created_date: 2026-05-16
---

# Skill: Сборка train/hard_skills.json

## Версия

Текущая версия 1.0. Включай версию в summary, который скилл показывает пользователю.

## Назначение

Один прогон → один артефакт `train/hard_skills.json` для обучения `ScoringPromptTrainer` (см. `md/train.md` §Обучение). Это **первый шаг** воркфлоу train: собираем плоский корпус hard-skill Q&A из всех splitter-артефактов, чтобы дальше его можно было размечать как golden set.

Скилл — тонкая обёртка над `scripts/build_train_hard_skills.py`. Логику сборки в SKILL.md не дублируем: она целиком живёт в скрипте.

## Соответствие train.md

Скилл закрывает один атомарный шаг подготовки данных, упомянутый в `md/train.md`:

> Строится golden set (ручная разметка эталонных оценок по подмножеству Q&A).
> Разбиение train / test на уровне целых mock-сессий (чтобы не протекали коррелированные ответы из одного диалога).

Сам корпус Q&A до этого жил россыпью в `splitter_output/`. Скилл собирает его в один файл с явным `source_id` на каждом item — это нужно и для последующей разметки, и для группировки при `train/test` split'е по сессиям.

Что **не** делает скилл (вне scope):
- ручную разметку golden set (clarity / completeness / accuracy);
- `train/test` split — это отдельный шаг, когда корпус уже размечен;
- оптимизацию промпта-оценщика по MAPE;
- генерацию `reference_answer` для item'ов, где он `null`.

## Вход

**Без аргументов.** Все параметры захардкожены в скрипте; для изменения — править скрипт (см. «Расширение» ниже).

## Конфигурация

- **Рабочий каталог:** корень репо (`git rev-parse --show-toplevel`).
- **Скрипт:** `scripts/build_train_hard_skills.py` (Python 3, только stdlib — без `uv run`, без deps).
- **Вход:** `splitter_output/*.splitter.v*.json` (паттерн с регуляркой `\.splitter\.v(\d+)\b` в имени).
- **Выход:** `train/hard_skills.json`. Папка `train/` создаётся, если её нет.
- **Фильтры внутри скрипта (захардкожены):**
  - `question_type == "hard"`;
  - на каждый `source_id` — запись с максимальным `vN`;
  - исключённые `source_id` — множество `EXCLUDED_SOURCE_IDS` в скрипте; сейчас один элемент — `junior_data_scientist_собеседование_karpov_courses_20220330` (старое имя сессии karpov_junior_ds_20220330).

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
      "question_type": "hard",
      "question_topic": "...",
      "interview_stage": "...",
      "grade": "junior" | "middle" | "senior"
    }
  ]
}
```

Item-схема идентична items в `splitter_output/*.splitter.v*.json`, плюс одно добавленное поле `source_id` (в начале каждого item).

## Алгоритм

### Шаг 1: Проверка предусловий

- Текущий каталог = корень репо (если нет — `cd $(git rev-parse --show-toplevel)`).
- Существует `splitter_output/` с файлами `*.splitter.v*.json` (>0 штук). Если нет — остановиться с понятным сообщением: «нет splitter-артефактов для сборки».
- Существует `scripts/build_train_hard_skills.py`. Если нет — остановиться: «скрипт не найден, скилл не может работать».

### Шаг 2: Запуск

```bash
python3 scripts/build_train_hard_skills.py
```

Stdout у скрипта пустой; **вся сводка идёт в stderr**. Bash-вызов нужно сделать так, чтобы захватить stderr (например, `python3 scripts/build_train_hard_skills.py 2>&1`). Таймаут — дефолтный (скрипт быстрый: <1 сек на ~30 файлах).

### Шаг 3: Парсинг сводки скрипта

Скрипт печатает в stderr блок вида:

```
skip (excluded duplicate): <filename>
============================================================
written: train/hard_skills.json
total hard items: <N>
sources with hard items: <K>
  <source_id>                  <count>
  ...
skipped (0 hard items): <M>
  <source_id> (v<N>)
  ...
```

Из этого блока вытащить:
- `total_items` = число после `total hard items:`;
- `sources_with_hard` = число после `sources with hard items:` + сам список;
- `skipped_zero_hard` = число после `skipped (0 hard items):` + сам список;
- `excluded_duplicates` = строки `skip (excluded duplicate): ...`.

### Шаг 4: Sanity-check

После записи прогнать минимальную валидацию:

```bash
python3 -c "
import json
d = json.load(open('train/hard_skills.json'))
items = d['items']
assert all(i['question_type']=='hard' for i in items), 'non-hard item leaked'
assert all('source_id' in i for i in items), 'item without source_id'
sources = {i['source_id'] for i in items}
assert 'junior_data_scientist_собеседование_karpov_courses_20220330' not in sources, 'excluded duplicate leaked'
print(f'OK: {len(items)} items, {len(sources)} sources')
"
```

Если sanity-check падает — показать ошибку пользователю и **не** перезаписывать (но скрипт уже записал — значит, валидация раньше была невозможна; это сигнал что скрипт сломан, надо чинить его).

### Шаг 5: Отчёт пользователю

Короткий отчёт в одном сообщении:

```
build-train-hard-skills v1.0

wrote: train/hard_skills.json
total: <N> hard items from <K> sources

per-source:
  <source_id>                                <count>
  ...

skipped (0 hard items in latest version): <M> файлов
  - <source_id> (v<vN>)
  - ...

excluded duplicates: <D>
  - <filename>
```

## Расширение

Скилл намеренно без аргументов в v1. Если в будущем понадобится:

- **Другой `question_type`** (`soft_skill` / `behavioral`) → добавить аргумент `--type` в скрипт и в SKILL.md секцию «Вход»; output-имя сделать функцией от type (`train/soft_skills.json` и т.п.).
- **Дополнить ещё один `source_id`** в чёрный список → дописать в `EXCLUDED_SOURCE_IDS` в скрипте.
- **Другая папка с splitter-артефактами** → параметризовать `SPLITTER_DIR` (сейчас захардкожена в скрипте).
- **Включать annotation.v\*.json как источник оценок** → отдельная задача и отдельный output-файл; не путать с текущим скиллом.

Любое из этих расширений = обновление и SKILL.md, и скрипта одной правкой. Не делать «на всякий случай».

## Нюансы

- Скрипт выбирает «последнюю версию» по числу после `.splitter.v` в имени файла, а не по дате. Если когда-нибудь появится `v10` — он корректно победит `v9` (целочисленное сравнение, не лексикографическое).
- Item с `reference_answer == null` и `interviewer_feedback == null` — норма (≈9% корпуса). Скилл их не отбрасывает: это входит в корпус и для них golden score придётся ставить опираясь только на знания судьи-LLM.
- Поле `source_id` дописывается **в начало** item'а (через `{"source_id": ..., **item}`), чтобы при ручном просмотре JSON он был сразу виден.

## Ограничения

- Один прогон = один результат. Без батча.
- Только `question_type == "hard"`. Для других — см. «Расширение».
- Не делает train/test split — для этого пиши отдельный скилл/скрипт, когда golden set будет размечен.
- Не валидирует, что splitter-разбивка хорошая (это работа `splitter_validate_video` из скилла `splitter`).

## Пример сессии

```
user: /build-train-hard-skills
assistant:
  [precheck] splitter_output/ есть, 27 файлов *.splitter.v*.json; скрипт на месте.
  [run] python3 scripts/build_train_hard_skills.py
  [parse] total=89, sources=6, skipped(zero hard)=17, excluded=1
  [sanity] OK: 89 items, 6 sources

  build-train-hard-skills v1.0
  wrote: train/hard_skills.json
  total: 89 hard items from 6 sources
  per-source:
    avito_product_analyst_middle_20240404                        16
    junior_аналитик_данных_собеседование_karpov_courses_20210913_sasha   8
    junior_аналитик_данных_собеседование_karpov_courses_20210913_yegor   8
    karpov_junior_ds_20220330                                    23
    karpov_product_analyst_junior_20210624_pasha                 15
    karpov_product_analyst_junior_vyacheslav_20210624            19
  skipped (0 hard items): 17 файлов (behavioral / system-design / ml-sysdesign / middle_ds_* / senior_da / игровой_аналитик / ab-тесты)
  excluded duplicates: 1 (junior_data_scientist_собеседование_karpov_courses_20220330.splitter.v1.mock.json)
```
