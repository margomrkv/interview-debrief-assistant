# Оптимизация Claude Code для splitter pipeline

## Проблема

Claude Code читает файлы последовательно (один вызов = один файл), а генерация токенов
в потребительской очереди медленнее, чем в Cursor. Для прогона сплиттера без оптимизации
это 5–10 минут вместо 1–2 минут в Cursor.

## Оптимизация 1 — убрать подтверждения (сразу, бесплатно)

Запускать Claude Code из терминала с флагом:

```bash
cd /Users/mm/projects/ds-final-project
claude --dangerously-skip-permissions
```

Или в настройках PyCharm-плагина найти опцию "Auto-approve tool calls" / разрешения.

Это убирает паузы на `y/n` при записи файлов и запуске скриптов.
Экономия: 2–4 минуты на прогон.

---

## Оптимизация 2 — prepare_prompt.py (главная)

Вместо того чтобы Claude Code читал 5 файлов по одному, скрипт собирает всё в один текстовый
файл. Claude Code делает **1 чтение** вместо 5.

### Использование

```bash
# Сгенерировать готовый промпт для интервью
python3 labeling/prepare_prompt.py \
  --folder transcripts/mock-avito-product-analyst-middle-2024-04-04

# Для raw_split режима
python3 labeling/prepare_prompt.py \
  --folder transcripts/karpov-courses-собеседования/junior-data-scientist-... \
  --mode raw_split
```

Скрипт создаёт файл `labeling/data/<source_id>.prompt.txt`.

### Затем в Claude Code

```
Прочитай файл labeling/data/avito_product_analyst_middle_20240404.prompt.txt
и выполни задачу из него. Результат сохрани в
labeling/data/avito_product_analyst_middle_20240404.splitter.v2.mock.json
```

Всё. Claude Code делает: 1 чтение → генерация JSON → 1 запись → 2 скрипта.
Итого 4–5 шагов вместо 9–12.

---

## Оптимизация 3 — чёткое задание в первом сообщении

Вместо: «запусти сплиттер на авито»

Писать сразу:

```
Прочитай labeling/data/avito_product_analyst_middle_20240404.prompt.txt
Выполни Q&A extraction согласно инструкциям в файле.
Результат → labeling/data/avito_product_analyst_middle_20240404.splitter.v2.mock.json
Затем запусти:
  python3 labeling/splitter_json_to_excel.py labeling/data/avito_...json --out labeling/data/avito_...xlsx
  python3 labeling/validate_splitter_vs_video.py --splitter labeling/data/avito_...json --video transcripts/mock-avito-product-analyst-middle-2024-04-04/video.md --tolerance 120 --out labeling/data/avito_...validation.md
```

Конкретные пути = меньше уточняющих вопросов от модели = меньше лишних шагов.

---

## Ожидаемый результат после оптимизаций

| Шаг | Без оптимизации | С оптимизацией |
|-----|----------------|----------------|
| Чтение файлов | 5 × 15–30 сек = 2 мин | 1 × 15 сек |
| Подтверждения | 4 × 10 сек = 40 сек | 0 сек |
| Генерация JSON | 3–8 мин | 3–8 мин (не меняется) |
| Запуск скриптов | 2 × 30 сек = 1 мин | 2 × 10 сек |
| **Итого** | **6–12 мин** | **4–9 мин** |

Генерацию JSON ускорить нельзя — это физическое ограничение серверной очереди.
