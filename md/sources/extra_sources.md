---
title: Дополнительные источники интервью (не скачано)
author: claude-code-opus-4-7
created: 2026-04-30
updated: 2026-04-30
status: draft
related: [[spec]], [[scripts/transcript_downloader/data_interviews_plan.tsv]]
---

# Дополнительные источники интервью

Что попадалось во время поиска и подсчёта, но **не скачано** в `transcripts/`.
Сгруппировано по причине пропуска. Каждый блок — кандидат на доразведку,
если понадобится расширять датасет.

> **Статус YouTube-плана:** все 52 видео из `data_interviews_plan.tsv`
> скачаны (77 транскриптов всего на диске вместе с karpov, anton, mock).
> Этот документ теперь — про источники **за пределами** уже выполненного
> плана.

## 1. Уроки скачивания (для будущих заходов)

- **YouTube агрессивно режет по IP**: после 25-30 последовательных запросов
  через `youtube_transcript_api` любой VPN-узел уходит в IP-блок.
  Минимум помогает: пакеты по 10-15 видео, смена exit-узла между пачками.
- **interviewing.io — нестабильные auto-CC**: 6 из 9 видео упали с
  «No transcripts found», но при retry с другого узла все 6 взялись.
  Фиксирую как класс рисков.
- **yt-dlp иногда требует cookies**: пара видео жалуются «Sign in to
  confirm you're not a bot» — на новом VPN это уходит, но если упрётся
  снова, нужен `--cookies-from-browser` в `resolve_video_meta()`.

## 2. Платные источники — фидбек глубже, но за деньги

| Источник | Что внутри | Цена / доступ |
|---|---|---|
| [Boosty Александра Локиса](https://boosty.to/lokis_alexandr) | 10+ ML System Design / Classic ML mock с детальным фидбеком (NLP, CV, метрики) | по подписке |
| Podlodka Crew Records | Архив записей iOS/QA/Frontend/Teamlead Crew собесов | ~3000₽ за запись |
| [DataInterview Pro](https://www.datainterview.com) | 4000+ вопросов, 10+ курсов, 1-on-1 коучинг с фидбеком (DS/DE/MLE/Quant) | подписка |
| [Hello Interview Premium](https://www.hellointerview.com) | 1ч сессии (mock + 15-20 мин фидбека), эксперты из Google/Meta/Stripe | за сессию |
| [IGotAnOffer mock](https://igotanoffer.com/en/mock-interviews) | PM/TPM/SWE/DS, 45 мин mock + 15 мин разбор | за сессию |

## 3. Каналы вне data-скоупа (но интересно для расширения)

Нашлись при подсчёте, но не подходят под фильтр «только data»:

- **Avito Tech** — `youtube.com/@avitotech`. Из 681 видео только **1
  настоящее открытое собеседование с фидбеком**: «Открытое собеседование —
  технический руководитель» (`-nu4Bjufygw`). Не data, поэтому не скачано.
- **Podlodka Crew (бесплатный канал)** — `youtube.com/@PodlodkaCrew`. Из 41
  видео только 1 «доклад про собес iOS-разработчика». Все mock — в платном
  архиве (см. п. 2).
- **ODS.AI Ru** — 1861 видео, ноль mock-собесов; всё про разборы статей и
  решений хакатонов. Полезно для другого слоя датасета (DS-разговоры), но
  не интервью.

## 4. T-Bank — фрагментированный источник без корпоративного канала

Корпоративного YouTube-канала «T-Bank Tech» с открытыми собеседованиями
**не существует** (`@tbank` — маркетинговый канал, ~5 видео, 0 интервью).
Но контент про T-Bank-собеседования есть у блогеров (через `ytsearch`):

| Канал | Что | Уровень доверия |
|---|---|---|
| Vadim Novoselov | DS/QA в Тинькофф (несколько эпизодов) | ✓ уже скачано |
| Tech Analyst Club | Системный аналитик в Т-Банк | не скачано |
| Mobile Dev | Android-собеседование в Т-Банк (теория) | не скачано |
| Software Developer | Тинькофф Senior + секция по алгоритмам | не скачано |
| itrostik | Гофер / HR-скрининг в Т-Банк | не скачано |
| Daniil Maximum | System Design FE в T-Банк (380к) | не скачано |
| Тихон Галактионов | T-Банк FE на 400к: JS секция | не скачано |
| Код Желтый | Открытое собес Tinkoff DWH Connect | ✓ уже скачано через dataengineers.pro |
| it father | Реальное собеседование в Тинькофф на тимлида | не скачано |

Если нужен «срез T-Bank» — это 8-10 потенциальных эпизодов, но качество
разное и фидбек далеко не везде.

## 5. RU-источники, не дотронутые скриптом

Не на YouTube — нужны отдельные парсеры/скачивание:

- **Подкаст СОБЕС** (Либо/Либо) — `podcast.ru` поиск «Собес». ~20+ выпусков,
  формат: live mock + фидбек + Q&A. DA/DE/BA-эпизоды.
- **Linkmeup «Собес»** — `linkmeup.ru/podcasts`. Закрытая серия из 5 выпусков
  Network/Integration Engineer; на каждое — 60 мин mock + 20 мин разбора.
- **balun.courses (RuTube)** — серия ML System Design mock с тимлидом
  Яндекса; ~50 мин фидбека после интервью.
- **dataengineers.pro: пропущенные эпизоды** — на главной странице
  индексируются только S1E4/E5/E7 + S2E1/E2 + Tinkoff DWH. По нумерации
  очевидны S1E1, S1E2, S1E3, S1E6 — нужно искать на отдельных страницах
  или в архиве RSS.

## 6. Open datasets — есть метки, но не скачано (форм/лицензии)

| Датасет | Размер | Метки | Доступ |
|---|---|---|---|
| [RecruitView](https://huggingface.co/datasets/AI4A-lab/RecruitView) | 2 011 видео | 12 непрерывных шкал (Big Five + interview perf) | gated form, CC BY-NC, не для прод. найма |
| [MIT Interview Dataset](https://roc-hci.com/past-projects/automated-prediction-of-job-interview-performances/) | 138 видео | 16 черт (Likert) + hire-recommendation | по форме |
| HURIT (arXiv:2504.05683) | 3 890 текстовых HR-транскриптов | экспертные оценки + actionable feedback | проверить наличие на HF |
| [Anthropic Interviewer](https://huggingface.co/datasets/Anthropic/AnthropicInterviewer) | 1 250 транскриптов | **меток нет** | публично |

Они дают то, чего нет в YouTube-эпизодах: **готовую разметку «hire / no-hire»
и многомерные оценки**. Кандидат №1 на использование в evaluation-сете —
RecruitView. MIT — для бенчмарка hire-recommendation.

## 7. Сводка по «доступному, но не взятому»

| Слой | Записей-кандидатов | Стоимость доразведки |
|---|---:|---|
| Платные платформы | ~30+ | подписки/оплата |
| RU-блогеры по T-Bank | 8-10 | разовая загрузка |
| RU вне-YouTube (СОБЕС, Linkmeup, balun) | ~30 | отдельные парсеры |
| dataengineers.pro: пропущенные эпизоды | ~4 (S1E1-3, S1E6) | поиск по архиву |
| Open datasets с метками | ~7 200 | формы доступа |
| **Итого потенциально доступного** | **~7 270** | разный уровень усилий |

Уже на диске: **77 транскриптов** (`transcripts/`). Реалистичный «следующий
шаг без боли» — забрать СОБЕС-подкаст (~20 эпизодов RU DA/DE/BA с фидбеком)
и balun.courses RuTube (ML SD mock). Дальше — RecruitView/MIT, если нужны
готовые метки hire-recommendation.
