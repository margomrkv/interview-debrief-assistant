---
name: download-transcript
description: Запускает `scripts/transcript_downloader/main.py` для скачивания транскрипта YouTube-видео или плейлиста. Принимает URL, остальные аргументы (slug/date/playlist-name/lang/overwrite) подтягивает из YouTube-метаданных и уточняет у пользователя.
---

# Skill: Скачивание YouTube-транскрипта

## Назначение

Тонкая обёртка над существующим CLI `scripts/transcript_downloader/main.py`:
1. Классифицирует YouTube URL (video vs playlist).
2. Для недостающих аргументов тянет подсказки из YouTube через `yt-dlp -J` и спрашивает пользователя через AskUserQuestion.
3. Собирает команду, запускает CLI через `uv run`, рапортует результат.

Код CLI не дублируем — скилл только инструктирует, как вызвать существующий скрипт.

## Вход

Один обязательный токен — YouTube URL (первый токен args, начинающийся с `http`).

Опциональные `key=value` флаги в args:
- `slug=<slug>` — для single video
- `date=<YYYYMMDD>` — для single video
- `playlist-name=<name>` — для playlist
- `lang=<csv>` — приоритет языков (default `ru,en`)
- `overwrite` — перезаписать существующую папку (bool-флаг, без `=`)

Если URL в args нет — спросить у пользователя. Не выдумывать.

## Конфигурация

- **Рабочий каталог:** корень репо (`git rev-parse --show-toplevel`).
- **CLI скрипт:** `scripts/transcript_downloader/main.py` (запуск: `uv run python scripts/transcript_downloader/main.py`).
- **Куда пишутся результаты:**
  - single: `transcripts/single_videos/<slug>-<YYYYMMDD>/`
  - playlist: `transcripts/<playlist-name>/<slug>-<YYYYMMDD>/` + `transcripts/<playlist-name>/link.txt`
- **Конвенция именования папок** (из `CLAUDE.md`):
  - Mock-интервью: `mock-<company>-<role>-<level>-YYYY-MM-DD`
  - Собственные интервью: `<person>-<company>-YYYYMMDD` (без дефисов в дате)
  - Скилл **не переименовывает** автоматически — только предлагает шаблоны в вариантах AskUserQuestion.

## Алгоритм

### Шаг 1: Парсинг args

- Выделить URL — первый токен, начинающийся с `http`.
- Остальные токены: `key=value` → в словарь; голый токен `overwrite` → bool-флаг.
- Неизвестные ключи — сообщить и остановиться.

### Шаг 2: Классификация URL

Без Python — руками по правилам (совпадает с `classify_url` в `main.py`):

- `youtube.com/watch?v=<ID>` (даже если ещё есть `&list=`) → **video**, `video_id = <ID>`.
- `youtube.com/playlist?list=<LID>` (нет `v=`) → **playlist**, `list_id = <LID>`.
- `youtu.be/<ID>`, `youtube.com/shorts/<ID>`, `youtube.com/embed/<ID>` → **video**.
- Иначе — сказать «не могу распарсить URL» и остановиться.

Проверить совместимость переданных флагов с режимом:
- video URL + `playlist-name=` → ошибка, остановиться.
- playlist URL + `slug=` или `date=` → ошибка, остановиться.

### Шаг 3a: Single video — доопределение slug/date

Если **оба** флага `slug` и `date` переданы — пропустить этот шаг.

Иначе вытянуть метаданные:

```bash
uv run yt-dlp -J --skip-download "<url>" 2>/dev/null | jq -r '{title, upload_date}'
```

Из ответа:
- `auto_slug` = slugify(title), по правилам `main.py:slugify()`:
  - lowercase,
  - все non-word-символы (включая пробелы, юникодные — `re.UNICODE`) → `-`,
  - схлопнуть `-+` → `-`,
  - strip `-`,
  - если пусто — `untitled`.
- `auto_date` = `upload_date` (yt-dlp возвращает уже в `YYYYMMDD`).

Дальше AskUserQuestion — **два вопроса**:

1. **slug** (если не передан):
   - опция 1 (Recommended): `auto_slug`
   - опция 2: `mock-<company>-<role>-<level>` (пользователь допишет через "Other" если выбрал эту категорию)
   - опция 3: `<person>-<company>` (аналогично через "Other")
   - "Other" для свободного ввода

2. **date** (если не передан):
   - опция 1 (Recommended): `auto_date` (из upload_date)
   - опция 2 (Other): вручную `YYYYMMDD`

Если слот для шаблона (`mock-...`, `<person>-...`) выбран без заполнения — попросить пользователя через повторный AskUserQuestion заполнить free-form.

**Валидация:** `date` должен matches `^\d{8}$`. slug не пустой, без пробелов (слаги в CLI пойдут в имя папки, пробелы ломают конвенцию).

### Шаг 3b: Playlist — доопределение playlist-name

Если `playlist-name` передан — пропустить.

Иначе:

```bash
uv run yt-dlp -J --flat-playlist --skip-download "<url>" 2>/dev/null | jq -r '.title'
```

`auto_name` = slugify(playlist title) по тому же алгоритму.

AskUserQuestion — один вопрос:
- опция 1 (Recommended): `auto_name`
- опция 2: `<source>-<kind>` (e.g. `karpov-courses-собеседования`) через Other
- "Other" для свободного ввода

Валидация: непустой, без пробелов, без слэшей.

### Шаг 4: Формирование команды

Базовая команда:
```
uv run python scripts/transcript_downloader/main.py "<url>" <mode-flags>
```

Где `<mode-flags>`:
- single: `--slug "<slug>" --date <YYYYMMDD>`
- playlist: `--playlist-name "<name>"`

Добавить:
- `--lang <csv>` если пользователь передал `lang=` и он отличается от `ru,en`.
- `--overwrite` если передан bool-флаг `overwrite`.

**Перед запуском** напечатать собранную команду одной строкой — для прозрачности. Не спрашивать подтверждение: сам вызов скилла = согласие.

### Шаг 5: Запуск

Через Bash, рабочая директория — корень репо. Таймаут 300000ms (плейлист может быть долгим).

### Шаг 6: Отчёт

Распарсить stdout/stderr CLI:

- **Single video:**
  - exit 0 → «wrote: transcripts/single_videos/<slug>-<date>/» + заметить наличие `feedback.txt` если было `(+feedback)` в stdout.
  - exit 1 → сказать причину из stderr (транскрипт не найден / skip без overwrite / meta-ошибка).
  - exit 2 → ошибка флагов/URL, процитировать stderr.
  - Если папка создана и имя не совпадает с конвенцией (`mock-…` / `<person>-…-YYYYMMDD`) — **мягко предложить** примеры переименования:
    ```
    mv transcripts/single_videos/<slug>-<date>/ transcripts/mock-<company>-<role>-<level>-YYYY-MM-DD/
    ```
    Не выполнять автоматически.

- **Playlist:**
  - exit 0 → показать summary-строку из stderr (`summary: ok=X skipped=Y failed=Z`) + путь бакета.
  - exit 1 → «ни одной папки не записано», показать stderr.
  - Перечислить записанные подпапки (те, что в stdout `wrote: …`).
  - Предложить: «если нужно переименовать вложенные папки под конвенцию `mock-…` — скажи, подготовлю `mv` команды».

## Нюансы

- yt-dlp может тянуть метаданные 2–10 секунд — нормально, не ретраить.
- Если `yt-dlp -J` упал (приватное видео, геоблок) — показать ошибку и попросить пользователя ввести slug/date/playlist-name вручную, не останавливаться.
- В slug допустима кириллица (`re.UNICODE` в `slugify`), поэтому всегда quoting в bash.
- `--lang ru,en` — дефолт CLI, не передавать явно если совпадает.
- Если пользователь уже запускал скилл на этом URL и папка существует — CLI напечатает `warn: folder exists, skipping`. Это **не ошибка**, но скилл должен чётко это сказать и предложить `overwrite` как опцию.
- Не кэшируем и не логируем URL/метаданные отдельно — CLI сам пишет `link.txt`.

## Ограничения

- Только YouTube. Другие платформы CLI не поддерживает.
- Только интервью (по spec) — скилл не валидирует тип контента, на совести пользователя.
- Не запускаем несколько URL за раз. Один вызов = один URL (video или playlist).
- Не переименовываем папки автоматически под конвенцию — только подсказываем.

## Пример сессии

```
user: /download-transcript https://www.youtube.com/watch?v=dQw4w9WgXcQ
assistant: [классифицирует как video, тянет yt-dlp -J, получает title="Rick Astley - Never Gonna Give You Up", upload_date="20091025"]
           [AskUserQuestion: slug? (предлагает "rick-astley-never-gonna-give-you-up" или mock-/person- шаблон); date? (предлагает 20091025)]
user: [выбирает шаблон, заполняет "mock-rickroll-demo-junior"]
assistant: Команда: uv run python scripts/transcript_downloader/main.py "https://..." --slug "mock-rickroll-demo-junior" --date 20091025
           [Bash]
           wrote: transcripts/single_videos/mock-rickroll-demo-junior-20091025/
           Если хочешь переименовать под конвенцию mock-<company>-<role>-<level>-YYYY-MM-DD:
             mv transcripts/single_videos/mock-rickroll-demo-junior-20091025/ transcripts/mock-rickroll-demo-junior-2009-10-25/
```
