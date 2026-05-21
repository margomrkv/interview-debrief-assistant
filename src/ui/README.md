---
author: claude-code-opus-4-7
created_date: 2026-05-21
---

UI-эмулятор для приложения из [[docs/spec/ui.md]]. Показывает двухэтапный разбор
интервью (**Splitter → Scoring**) асинхронно, **без вызовов модели** — оба этапа
*проигрываются* из заранее посчитанных данных.

## Запуск

```bash
python3 src/ui/app.py        # http://127.0.0.1:8000
python3 src/ui/app.py 8011   # другой порт
```

Только stdlib, без установки зависимостей. Аутентификации нет (личный доступ).

## Как устроено

```
src/ui/
├── app.py        # stdlib HTTP-сервер + SSE-стрим двух этапов
├── emulator.py   # слой данных: дискавери emulator-data, джойн qa↔scores по id
└── static/       # одностраничный фронтенд (index.html, app.js, styles.css)
```

Источник данных — папки `emulator-data/` под `data/emulator-data/**/`. Каждая =
одно загружаемое интервью (ключ `source_id`):
- `../transcript.txt` — вход Splitter (то, что «загружает» пользователь);
- `qa.json` — выход Splitter (Q&A + метаданные, без оценок);
- `scores.json` — выход Scoring (`factual_correctness` / `focus` / `clarity` +
  `aggregate`); связан с `qa.json` по полю `id`.

Чтобы добавить интервью в эмулятор — положите рядом с его `transcript.txt` папку
`emulator-data/` с `qa.json` и `scores.json`; сервер подхватит её при перезапуске.

## Поток (SSE `/api/stream`)

`stage(running)` → `split_item` ×N → `stage(done)` → `stage(running)` →
`score_item` ×N → `stage(done)` → `report` → `done`. Карточки Q&A появляются на
первом этапе, оценки доезжают на втором, в конце — вердикт HIRE/NO_HIRE + p(hire),
свёрнутый из per-item оценок (AlignmentReport, md/spec.md §3.4).

## Эндпоинты

| Метод | Путь                          | Назначение                                  |
|-------|-------------------------------|---------------------------------------------|
| GET   | `/api/interviews`             | Каталог интервью для сайдбара               |
| GET   | `/api/transcript?source_id=…` | Текст транскрипта                           |
| GET   | `/api/stream?source_id=…`     | SSE-стрим Splitter→Scoring→report           |
| POST  | `/api/match` `{text}`         | Сопоставить загруженный .txt с `source_id`  |
