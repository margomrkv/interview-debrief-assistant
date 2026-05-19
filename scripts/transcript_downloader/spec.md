
## Spec

Нужен небольшой скрипт для скачивания транскриптов интервью с YouTube.
Скрипт принимает ссылку на видео или на плейлист и сохраняет транскрипты в текстовые файлы.

### Область

Только интервью. Лекции и произвольные видео — вне скоупа. Именование и структура выходных файлов консистентны с `transcripts/_template/` (см. `transcripts/README.md`, `CLAUDE.md`).

### Вход

- Одна ссылка: на видео или на плейлист YouTube.
- Плейлист = набор разных интервью; каждое видео выгружается в свою отдельную папку.

### Выход

На каждое интервью — папка с тремя файлами (формат `transcripts/_template/`):
- `video.md` — общая информация по видео (url, title, upload_date, duration, channel, chapters. description, view_count, like_count, tags, thumbnail_url, language)
- `transcript.txt` — плейн-текст;
- `timecodes.txt` — строки с префиксом `[mm:ss]` (всегда, не по флагу).
- `feedback.md` - если транскрипт содержит фидбек, то он сохраняется в отдельный файл (опционально, не по флагу).
   в начале frontmatter с указанием названия секции и таймкодов, а дальше — плейн-текст из транскрипта в этих таймкодах.
   Детекция всегда детерминированная: регэксп по title чаптера. Никакой LLM, никакого семантического анализа текста транскрипта.


Иерархия:

- **Playlist**: `transcripts/<playlist-name>/<slug>-<YYYY-MM-DD>/`.
- **Single video**: `transcripts/<bucket>/<slug>-<YYYY-MM-DD>/` (default `--bucket single_videos`).

### Именование

Полная спецификация: [`NAMING.md`](NAMING.md) (дубль в `transcripts/README.md`).

Leaf (mock/real hiring):

```text
{kind}-{role}-{level}[-{target}]-{publisher}[-{candidate}][-{topic}]-{YYYY-MM-DD}
```

- **Single video**: `--slug` = leaf **без даты** (например `mock-data-scientist-junior-karpov`), `--date` = `YYYYMMDD`, `--bucket` = путь под `transcripts/` (например `mock-interviews/karpov`).
- **Playlist**: `--playlist-name` = бакет (`mock-interviews/karpov`, `real-interviews/novoselov`, …). Имя каждой вложенной папки автогенерируется из title YouTube — **после выкачки переименовать** в паттерн выше (скилл `download-transcript` помогает собрать slug).

### Язык

Смесь ru/en возможна, но типичный кейс — ru (интервью). Приоритетный список с fallback (по умолчанию `ru,en`, дальше — первый доступный).

### Архитектура

См. [`arch.md`](arch.md).
