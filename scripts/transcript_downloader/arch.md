# Architecture

Парная документация к [`spec.md`](spec.md).

## Tooling

- `youtube-transcript-api` — субтитры (unofficial: скрапит внутренний endpoint YouTube; официальный `captions.download` требует OAuth + владения каналом).
- `yt-dlp` как библиотека — раскрытие плейлиста в `[{id, title, upload_date}]` через `YoutubeDL({'extract_flat': True})`.
- Один `main.py` + `pyproject.toml` (PEP 621).

## CLI

```
single:    python main.py <video-url>    --slug SLUG --date YYYYMMDD   [--lang ru,en] [--overwrite]
playlist:  python main.py <playlist-url> --playlist-name NAME          [--lang ru,en] [--overwrite]
```

- **Single video**: `--slug` и `--date` обязательны. `--playlist-name` запрещён. Папка → `transcripts/single_videos/<slug>-<YYYYMMDD>/`.
- **Playlist**: `--playlist-name` обязателен. `--slug`/`--date` запрещены. Для каждого видео создаётся своя папка: `slug` = slugified title из YouTube, `date` = `upload_date` из yt-dlp в формате `YYYYMMDD`. Папка → `transcripts/<playlist-name>/<slug>-<YYYYMMDD>/`. Пользователь при необходимости переименовывает вложенные папки под convention (`mock-<company>-<role>-<level>-YYYY-MM-DD/` и т.п.) руками.
- `--lang` — приоритетный список языков, default `ru,en`.
- `--overwrite` — иначе skip+warn при существующей папке.

Корень репо определяется через `git rev-parse --show-toplevel`.

## Выход (на каждую папку)

Совпадает с `transcripts/mock-template/`:

- `link.txt` — исходный URL видео
- `transcript.txt` — плейн-текст (snippets склеены пробелами, нормализованы)
- `timecodes.txt` — построчно `[mm:ss] text` (или `[hh:mm:ss]` если длительность > часа)

Все три файла создаются всегда.

## Поток исполнения

- `classify_url(url)` → `("video", id)` или `("playlist", id)`. Правила: `list=` без `v=` → playlist; `v=` (даже с `list=`) → video. Паттерны video_id: `watch?v=`, `youtu.be/<id>`, `shorts/<id>`, `embed/<id>`.
- `expand_playlist(url)` → `list[{id, title, upload_date}]` через `yt_dlp`.
- `fetch_transcript(video_id, lang_priority)` → порядок: manual(priority) → generated(priority) → first manual → first generated.
- `write_folder(out_dir, url, snippets, overwrite)` → `mkdir -p`, пишет три файла, skip+warn при конфликте без `--overwrite`.
- `main()` — single: один вызов; playlist: цикл, ошибки на отдельных видео → stderr+continue, summary в конце.

## Exit codes

- `0` — всё ок (single: папка записана; playlist: ≥1 папка записана).
- `1` — транскрипт не получен (single) / ни одной папки не записано (playlist).
- `2` — невалидный URL / конфликт флагов (отсутствуют `--slug`/`--date` для single; отсутствует `--playlist-name` для playlist; либо переданы флаги не того режима).

## Не делаем

- Режимов lecture/universal нет.
- Whisper / ASR fallback.
- Кеш.
- Скачивание видео/аудио.
- Авто-ретраи.
