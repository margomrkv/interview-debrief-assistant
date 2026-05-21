---
author: claude-code-opus-4-7
created_date: 2026-05-21
---

Набор данных для **эмулятора UI** из [[md/ui.md]]. UI работает в два этапа
(Splitter → Scoring); пока самого UI/эмулятора нет, эта папка даёт готовые выходы
каждого этапа для данного интервью, чтобы фронтенд можно было собрать и проверить
без вызовов платной модели. Лежит рядом с самим интервью (на уровне его папки).

## Откуда данные

Интервью `data_scientist_junior_karpov_2022_03_30` (Data Scientist, junior,
karpov.courses, 2022-03-30) — родительская папка этого README. Выбрано как самый
богатый размеченный набор: 36 hard-вопросов, из них 29 с оценками.

Источники (не трогаются, только читаются):
- транскрипт — `../transcript.txt` (вход Splitter, в папке интервью)
- разметка — `data/knowledgebase/train/hard_skills.json` (отфильтрована до этого `source_id`)

## Файлы (по этапам пайплайна)

| Файл               | Этап           | Что внутри                                                      |
|--------------------|----------------|-----------------------------------------------------------------|
| `../transcript.txt`| вход           | То, что пользователь «загружает» в UI (в папке интервью)        |
| `qa.json`          | выход Splitter | Список Q&A (вопрос/ответ + метаданные), **без оценок**          |
| `scores.json`      | выход Scoring  | Три критерия + `aggregate` по каждому Q&A (либо `null`)         |

`qa.json` и `scores.json` связаны общим полем **`id`** (`q01`…`q36`, по порядку
элементов) — UI сопоставляет оценку с вопросом по `id`.

### `qa.json`
```
{ "source_id", "items": [ { "id", "interviewer_question", "candidate_answer",
  "reference_answer", "interviewer_feedback", "question_type", "question_topic",
  "interview_stage", "grade" } ] }
```

### `scores.json`
```
{ "source_id", "labeling": { … "stats": { "total", "labeled", "unscored" } },
  "items": [ { "id", "reference_score": { "factual_correctness", "focus",
  "clarity", "aggregate", "signal_source", "rationale" } | null,
  "unscored_reason"? } ] }
```

Три критерия Scoring — `factual_correctness`, `focus`, `clarity` (шкала 1..10,
калибровка по `grade`). 7 из 36 вопросов без сигнала интервьюера → `reference_score: null`
и `unscored_reason: "no_interviewer_signal"`; UI показывает «нет оценки».

## Чего здесь нет

Overall-вердикт («вывод» из [[md/ui.md]]) **не хранится** — его считает агрегатор
UI из per-item `aggregate`. Также не переносятся `timecodes.txt`, `video.md`,
`feedback.md`, `assessment_items*.csv` — эмулятору они не нужны.
