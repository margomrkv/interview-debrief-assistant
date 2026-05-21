---
name: download-transcript
description: Запускает `scripts/transcript_downloader/main.py` для скачивания транскрипта YouTube-видео или плейлиста. Принимает URL; slug/date/bucket/playlist-name собирает по NAMING.md и метаданным YouTube.
---

# Skill: Скачивание YouTube-транскрипта

## Назначение

Обёртка над `scripts/transcript_downloader/main.py`:

1. Классифицирует YouTube URL (video vs playlist).
2. Подтягивает метаданные через `yt-dlp -J`, собирает **имя папки по конвенции репозитория**.
3. Запускает CLI, отчитывает путь.

**Канон именования и дерево каталогов:** `scripts/transcript_downloader/NAMING.md` (зеркало: `data/knowledgebase/raw/README.md`).  
При сомнениях по role/level/target — смотреть title/description в метаданных YouTube.

## Конвенция (кратко)

### Дерево

```text
data/knowledgebase/raw/
├── mock-interviews/<publisher>/   # mock-собесы
├── real-interviews/<publisher>/   # real (novoselov, …)
├── youtube-sessions/<publisher>/  # лайвы, разборы
├── own/                           # свои интервью
├── single_videos/                 # staging (если не указан --bucket)
└── _template/
```

### Имя leaf-папки (mock / real)

```text
{kind}-{role}-{level}[-{target}]-{publisher}[-{candidate}][-{topic}]-{YYYY-MM-DD}
```

| Сегмент | Примеры | Правило |
|---------|---------|---------|
| `kind` | `mock`, `real` | всегда первым |
| `role` | `data-scientist`, `data-analyst`, `product-analyst` | главный ключ сортировки |
| `level` | `junior`, `middle`, `senior` | E5/E6 → `senior`; если неясно — спросить |
| `target` | `amazon`, `avito`, `sber` | работодатель в кейсе; нет — пропустить |
| `publisher` | `karpov`, `interview-query`, `novoselov` | **не** `vadim` |
| `candidate` | `sasha`, `yegor` | только split одного ролика |
| `topic` | `fraud-model`, `ml`, `v1` | при коллизии |
| date | `2022-03-30` | всегда последний, kebab |

**Workshop:** track в слоте role — `mock-behavioral-senior-karpov-v1-2022-11-10`, `mock-system-design-senior-karpov-v3-2022-03-24`.

**Session:** `session-{topic}-{publisher}-{YYYY-MM-DD}` под `youtube-sessions/`.

### Файлы в папке интервью

| Файл | Назначение |
|------|------------|
| `video.md` | метаданные + chapters + description |
| `transcript.txt` | плейн-текст |
| `timecodes.txt` | `[HH:MM:SS] …` (вход splitter) |
| `feedback.md` | фидбек по chapter (если найден) |

CLI создаёт эти файлы автоматически.

## Вход скилла

Обязательно: YouTube URL (первый токен с `http`).

Опционально `key=value` / флаги:

| Флаг | Режим | Описание |
|------|-------|----------|
| `slug=<base>` | video | leaf **без даты** (CLI добавит `-YYYY-MM-DD`) |
| `date=<YYYYMMDD>` | video | из `upload_date` или вручную |
| `bucket=<path>` | video | под `data/knowledgebase/raw/`, напр. `mock-interviews/karpov` |
| `playlist-name=<path>` | playlist | бакет, напр. `mock-interviews/karpov` |
| `lang=<csv>` | оба | default `ru,en` |
| `overwrite` | оба | перезапись |

Если URL нет — спросить. Не выдумывать.

## Publisher → bucket

| Источник | `--bucket` / `--playlist-name` | сегмент `publisher` в slug |
|----------|--------------------------------|----------------------------|
| karpov.courses | `mock-interviews/karpov` | `karpov` |
| Interview Query | `mock-interviews/interview-query` | `interview-query` |
| interviewing.io | `mock-interviews/interviewing-io` | `interviewing-io` |
| DataInterview | `mock-interviews/datainterview` | `datainterview` |
| DataEngineers Pro | `mock-interviews/dataengineers-pro` | `dataengineers-pro` |
| Avito Tech | `mock-interviews/avito` | `avito` |
| Vadim Novoselov | `real-interviews/novoselov` | `novoselov` |
| Yandex Practicum (live) | `youtube-sessions/yandex-practicum` | `yandex-practicum` |

## Алгоритм

### 1. Парсинг args

URL — первый `http*`-токен. `key=value` в словарь; `overwrite` — bool.

### 2. Классификация URL

Как в `main.py:classify_url`:

- `watch?v=` → video (даже с `&list=`)
- `playlist?list=` без `v=` → playlist
- `youtu.be`, `shorts`, `embed` → video

Проверка флагов: video + `playlist-name` → ошибка; playlist + `slug`/`date` → ошибка.

### 3a. Single video — slug, date, bucket

Метаданные:

```bash
uv run yt-dlp -J --skip-download "<url>" 2>/dev/null | jq -r '{title, upload_date, channel}'
```

`auto_date` = `upload_date` (`YYYYMMDD`).  
Предложить leaf slug по NAMING.md (без даты), опираясь на title/channel:

1. **bucket** — `mock-interviews/<publisher>` или `real-interviews/<publisher>` (novoselov → real, karpov / interview-query → mock).
2. **role** — из title (`Data Scientist` → `data-scientist`, …).
3. **level** — `junior` / `middle` / `senior` из title; E5/E6 → `senior`.
4. **target** — компания в кейсе (`Amazon`, `Avito`, …) lowercase; если generic Karpov mock — пропустить.
5. **publisher** — сегмент в slug (из таблицы выше).
6. **topic** — если нужно (fraud-model, ml, …).
7. **candidate** — только если пользователь делает split.

Собрать **slug без** префикса mock/real, напр. `data-scientist-junior-karpov` или `data-scientist-senior-amazon-fraud-model-interview-query`.

AskUserQuestion (если флаги не переданы):

- **slug** (Recommended: собранный по паттерну; Other: правка)
- **date** (Recommended: `auto_date`; Other: `YYYYMMDD`)
- **bucket** (Recommended: из таблицы publisher; Other: `single_videos` только если staging)

Валидация: `date` = `^\d{8}$`; slug без пробелов, lowercase, kebab.

### 3b. Playlist — playlist-name

```bash
uv run yt-dlp -J --flat-playlist --skip-download "<url>" 2>/dev/null | jq -r '.title'
```

AskUserQuestion: `playlist-name` — Recommended `mock-interviews/<publisher>` или `real-interviews/novoselov` (не slugified title плейлиста, если известен источник).

После выкачки: **каждую** вложенную папку переименовать в hiring-паттерн (title → role/level/target вручную или по `video.md`).

### 4. Команда

```bash
# single
uv run python scripts/transcript_downloader/main.py "<url>" \
  --slug "<leaf-without-date>" \
  --date <YYYYMMDD> \
  --bucket "<path-under-transcripts>"

# playlist
uv run python scripts/transcript_downloader/main.py "<url>" \
  --playlist-name "<path-under-transcripts>"
```

Добавить `--lang` / `--overwrite` при необходимости. Показать команду перед запуском.

### 5. Запуск

Bash, cwd = корень репо, timeout 300000ms.

### 6. Отчёт

- **Single:** `wrote: data/knowledgebase/raw/<bucket>/<slug>-<YYYY-MM-DD>/`
  - Если `bucket=single_videos` — напомнить перенести в `mock-interviews/…` / `real-interviews/…`.
  - Перечислить файлы: `video.md`, `transcript.txt`, `timecodes.txt`, (+`feedback.md`).
- **Playlist:** summary + список `wrote:`; напомнить переименовать leaf'ы по NAMING.md.
- `warn: folder exists` — не ошибка; предложить `overwrite`.
- exit 1/2 — цитировать stderr.

Скилл **не переименовывает** папки после CLI сам — только подсказывает `mv` по NAMING.md.

## Примеры slug (без даты)

```text
data-scientist-junior-karpov
data-analyst-junior-karpov-sasha
product-analyst-middle-avito-avito
data-scientist-senior-amazon-fraud-model-datainterview
data-scientist-middle-sber-novoselov
behavioral-senior-karpov-v1
session-analytics-newcomer-live-yandex-practicum
```

## CLI → итоговый путь

```text
data/knowledgebase/raw/<bucket>/<slug>-<YYYY-MM-DD>/
```

Пример:

```bash
uv run python scripts/transcript_downloader/main.py "https://www.youtube.com/watch?v=Us_TKT8ZL2E" \
  --slug data-scientist-junior-karpov \
  --date 20220330 \
  --bucket mock-interviews/karpov
# → data/knowledgebase/raw/mock-interviews/karpov/data-scientist-junior-karpov-2022-03-30/
```

## Ограничения

- Только YouTube.
- Один URL за вызов.
- Playlist: auto-slug из title ≠ финальный паттерн — нужен rename.
- Multi-candidate: один URL → несколько папок вручную / `scripts/reorganize_transcripts.py`.

## Ссылки

- `scripts/transcript_downloader/NAMING.md` — полная спецификация
- `scripts/transcript_downloader/spec.md`, `arch.md` — поведение CLI
- `data/knowledgebase/raw/aliases.yaml` — история переименований
