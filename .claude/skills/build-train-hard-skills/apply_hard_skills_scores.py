#!/usr/bin/env python3
"""
Apply reference_score to train/hard_skills.json.

Policy: score only from interviewer_feedback or reference_answer.
Scale 1..5 per md/assessors.md (simplification 2026-05-11).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATH = ROOT / "train" / "hard_skills.json"

# (idx, factual, focus, clarity, signal_source, rationale)
# 8 items are intentionally absent from this dict — they receive reference_score=null.
SCORES = {
    # === avito_product_analyst_middle_20240404 (0..15) ===
    0:  (5, 4, 4, "feedback", "behavioral self-intro; интервьюер повторил ответ без критики, ответ структурный"),
    1:  (3, 4, 4, "feedback", "feedback: 'ожидали услышать что посмотришь план запроса' — ключевой триггер не упомянут; перечислил фильтрацию/агрегации правильно"),
    2:  (2, 2, 2, "feedback", "ответ фрагментарный ('ну джоины например, шесть джоинов'); интервьюер не получил содержательного ответа про план запроса"),
    3:  (4, 4, 4, "feedback", "feedback: 'рассказал какие задачи решал, понятно что опыт есть' — нейтрально-позитивно"),
    4:  (5, 4, 4, "feedback", "feedback: 'поделился, давай двигаться дальше'; 'для миддла это окей' — нейтральное прохождение"),
    5:  (5, 4, 4, "feedback", "feedback: 'Миддл уровень, есть повод поговорить дальше'; критика только в гипотетическом сеньорном русле"),
    6:  (5, 4, 4, "feedback", "feedback echo без критики; behavioral описание процесса бэклога"),
    7:  (5, 4, 4, "feedback", "feedback повторяет ответ; структурное описание квартального планирования"),
    8:  (5, 4, 4, "feedback", "feedback echo; behavioral про работу с заказчиками"),
    9:  (5, 4, 4, "feedback", "feedback echo; behavioral про отказы заказчикам"),
    10: (5, 4, 4, "feedback", "feedback: 'задача midle level... вполне супер' — явная положительная оценка для уровня"),
    11: (5, 2, 2, "feedback", "feedback: 'не очень получилось понять насколько это сложная задача' — интервьюер не смог оценить из-за абстрактности ответа"),
    12: (4, 4, 3, "both",     "ref: правильная стратегия (>3.5) и EV=4.25; candidate правильную стратегию назвал, расчёт прервал ('замялся')"),
    13: (5, 4, 4, "feedback", "feedback echo, без критики; case-вопрос"),
    14: (5, 4, 5, "feedback", "feedback: 'сразу начал с метрик — это здорово', 'гипотезу сформулировал академично'; минор — 'не сказал сразу для пользователя и компании одновременно'"),
    15: (5, 5, 5, "feedback", "feedback: 'видно что большой опыт', 'эту секцию закрываю — достаточно информации' — strong сигнал"),

    # === junior_аналитик_karpov_courses_20210913_sasha (16..23) ===
    16: (4, 4, 3, "both",     "ref принял решение через индексы как валидное; feedback: 'круто первый вопрос защите'"),
    17: (4, 4, 4, "feedback", "feedback: 'абсолютно верно... сначала пошло не так с сепаратором' — небольшая помеха, в целом ок"),
    18: (5, 5, 4, "feedback", "feedback: 'мне нравится что ты пишешь через df.section.unique', цикл был бы хуже"),
    19: (4, 4, 3, "both",     "feedback: 'неплохо... вторая задача знаешь 5 с минусом' — решение валидно но не оптимально (лишнее pivot)"),
    20: (2, 3, 2, "feedback", "feedback: 'эти задачи решения на 5 а не на ноль' — изначально ноль из-за фильтра в обратную сторону"),
    21: (5, 4, 3, "feedback", "feedback: 'теперь эти задачи решения на 5' — после правильной самокоррекции"),
    22: (4, 4, 3, "both",     "ref: '4 с плюсом' — решение работает, но более красиво через agg([max,min]) сразу"),
    23: (5, 3, 3, "feedback", "feedback: 'слушай саша на самом деле хорошо хорошо' — короткое одобрение"),

    # === junior_аналитик_karpov_courses_20210913_yegor (24..31) ===
    24: (3, 3, 2, "feedback", "минимальный ответ 'отсюда'; интервьюер просто описывает данные дальше — без явной критики или похвалы"),
    25: (2, 2, 2, "feedback", "candidate сразу попросил подсказку — не было попытки решить"),
    26: (4, 4, 3, "feedback", "feedback: 'логика абсолютно корректно', но clickhouse-specific переписать пришлось"),
    27: (1, 1, 1, "feedback", "candidate_answer пустой — missing"),
    28: (4, 4, 3, "feedback", "feedback: '5 с минусом' — короткое 'я думаю аккаунт distinct' было правильно но без раскрытия uniq"),
    29: (5, 4, 4, "feedback", "feedback: 'абсолютно валидны, человек явно с конструкции HAVING знаком'"),
    30: (3, 3, 3, "feedback", "feedback: решение синтаксически правильное, но не заметил аномалию (23000 дней = бот) — критика data quality awareness"),
    31: (2, 3, 2, "feedback", "feedback: 'что меня смущает что у тебя группировка по day и user' — логическая ошибка в group by"),

    # === karpov_junior_ds_20220330 (32..54) ===
    32: (2, 2, 2, "reference", "ref: правильно — tuple/float immutable, dict mutable; candidate путается ('теплые', 'наборы значений')"),
    33: (4, 4, 3, "reference", "ref подтверждает true; candidate дал правильный ответ но без объяснения причины"),
    34: (2, 3, 2, "reference", "ref: нужен .copy() или dict(a); candidate 'b = a, потом добавляется z=99' — фундаментально неверно (та же ссылка)"),
    35: (1, 1, 1, "reference", "candidate: 'ничего сказать' — фактически без ответа"),
    36: (2, 2, 2, "feedback", "candidate: 'нет не пользовался'; интервьюер дал один пример декоратора и двинулся дальше — не было ответа"),
    37: (5, 4, 4, "feedback", "feedback: 'про дизайн в целом всё правильно, клёво про AA-тест, MDE'; минор — 'не сказал в каких долях делим'"),
    38: (4, 4, 3, "reference", "ref: chi-square/bootstrap; candidate назвал критерий для долей и формулу — частично правильно (z-тест для долей)"),
    39: (4, 4, 3, "reference", "ref: нормальность — спорное ограничение; candidate назвал стандартный учебный ответ (N, нормальность)"),
    40: (4, 4, 4, "feedback", "feedback: 'супер, Shapiro-Wilk уже хорошо'; интервьюер не указал что Levene — для дисперсии, не для нормальности"),
    # 41: unscored (no fb, no ref)
    42: (5, 5, 4, "feedback", "feedback: 'супер, этого достаточно'; короткий точный ответ 'ЦПТ'"),
    43: (1, 1, 1, "reference", "candidate_answer пустой — missing"),
    # 44: unscored
    # 45: unscored
    46: (5, 5, 4, "reference", "ref совпадает 100%: 100/25/125/150/5000 — все цифры верны"),
    47: (5, 4, 3, "reference", "ref: 'dt[g] = dt.get(g, 0) + i' — candidate пришёл к точно этому решению, с детурами"),
    # 48: unscored
    # 49: unscored
    # 50: unscored
    51: (4, 4, 4, "reference", "ref: лучший способ — больше данных; candidate назвал 3 валидных (регуляризация, мультиколлинеарность, CV) но пропустил 'больше данных'"),
    52: (3, 4, 4, "reference", "ref: 'всё правильно описал, только говорил дисперсия — правильно энтропия' — терминологическая ошибка"),
    # 53: unscored
    54: (5, 5, 4, "reference", "ref: candidate точно угадал — RF берёт случайное подмножество шумных признаков, LR находит сигнал среди шума"),

    # === karpov_product_analyst_junior_20210624_pasha (55..69) ===
    55: (5, 3, 3, "feedback", "behavioral self-report; feedback echo без критики; ответ слегка рассеянный"),
    56: (2, 2, 2, "feedback", "candidate ответил 'очень редко но пользуюсь' — это не ответ на содержательный вопрос про алёрты; интервьюер продолжает setup"),
    57: (4, 4, 3, "feedback", "правильный подход — определить нормальное поведение, посмотреть распределение по времени дня"),
    58: (4, 4, 3, "feedback", "candidate описал график со скосом к вечеру, провёл аналогию со звонками; feedback echo"),
    59: (4, 4, 3, "feedback", "ответ верный (диапазоны на 5-минутку, учёт выходных); feedback добавил праздники как итерация"),
    60: (5, 5, 5, "feedback", "feedback: 'конечно, конечно. И вот это неделя к неделе — это очень важная история' — strong"),
    61: (4, 4, 3, "feedback", "feedback echo принимает ответ ('окно должно быть ограничено')"),
    62: (5, 4, 4, "feedback", "feedback: 'очень понравился твой первый ответ — пусть бизнес решает. Очень хороший подход'"),
    63: (4, 4, 3, "both",     "ref/feedback: 'точно... уйти от точечной оценки к распределению — это очень важно'; candidate сам пришёл к stddev/Z"),
    64: (3, 4, 4, "both",     "ref: '10/10' — описать процедуру; candidate дал распространённую но неверную интерпретацию '5% шанс не попасть'; feedback: 'хороший ответ' с поправкой"),
    65: (3, 4, 4, "both",     "то же что 64 — повторение того же ответа на тот же по сути вопрос"),
    66: (5, 4, 3, "feedback", "feedback: 'нормальный, хороший подход' — приемлемая прикидка"),
    # 67: unscored (no fb, no ref)
    68: (3, 4, 3, "feedback", "candidate просто умножил на 30, не учёл уникальных пользователей; feedback echo без критики"),
    69: (3, 3, 3, "feedback", "feedback (это ref ниже): 'можно было пойти от целевой аудитории...' — мягкая альтернатива, ответ не разорван"),

    # === karpov_product_analyst_junior_vyacheslav_20210624 (70..88) ===
    70: (3, 3, 3, "feedback", "candidate определил p-value как уровень значимости (терминологическая путаница); пример с монеткой длинный и не до конца ясен"),
    71: (3, 4, 3, "both",     "ref: 'вероятности равны/не равны'; candidate сказал 'честная/специальная' — суть та же но менее формально"),
    72: (4, 4, 3, "feedback", "candidate правильно посчитал 1/2^20, упомянул 5% порог; feedback echo"),
    73: (2, 3, 3, "both",     "ref: правильно 'такого или ещё более сильно выраженного'; candidate согласился с неточной формулировкой ('такие различия' без 'или более')"),
    74: (3, 3, 3, "both",     "ref/feedback: правильное определение 'в обе стороны'; candidate дал очень краткое 'не знаем в какую сторону'"),
    75: (4, 4, 3, "both",     "candidate дал валидную бизнес-причину (маркетинг); ref добавил денежный фрейминг"),
    76: (2, 2, 2, "feedback", "candidate очень кратко 'информацию о лайках, времени на сайте' — нет end-to-end pipeline'а"),
    77: (4, 4, 4, "feedback", "feedback: 'очень хорошая мысль' про географию; candidate назвал 4 фичи"),
    78: (2, 2, 3, "feedback", "candidate не ответил, спросил уточнение ('ставит или получает'); интервьюер сам дал хинт про нормирование"),
    79: (3, 4, 4, "both",     "candidate: 'на количество друзей'; feedback: 'конечно, конечно' принял; ref предлагает 'на количество просмотренных постов'"),
    80: (3, 3, 3, "feedback", "candidate указал валидную проблему (фон); feedback продолжает спрашивать как считать — ответ неполный"),
    81: (3, 3, 3, "feedback", "candidate: 'среднее в секундах в год либо в день'; feedback продолжает уточнять — ответ неполный"),
    82: (5, 4, 4, "feedback", "feedback: 'абсолютно верно'; candidate сам предложил 'новые друзья за период'"),
    83: (3, 4, 4, "feedback", "candidate: '2 недели' — произвольный порог; feedback: 'почему две а не три?' — пушит к статистическому обоснованию"),
    84: (3, 3, 3, "both",     "ref: смотреть историю предыдущих дропов; candidate ушёл в прогноз активности — близко но не туда; feedback корректирует"),
    85: (4, 4, 4, "feedback", "feedback: 'засчитано', 'скорее всего и не зайдёт' — принято; интуитивный аргумент валиден"),
    86: (4, 4, 4, "feedback", "feedback: 'why not, да? применили градиентный бустинг' — принял"),
    87: (3, 3, 3, "feedback", "candidate: 'отправить сообщение или уведомление'; feedback пушит к конкретике"),
    88: (4, 4, 4, "feedback", "feedback: 'идея правильная' про push о подписках"),
}

UNSCORED_INDICES = {41, 44, 45, 48, 49, 50, 53, 67}


def aggregate(fc: int, fo: int, cl: int, candidate_empty: bool) -> str:
    if candidate_empty:
        return "missing"
    vals = [fc, fo, cl]
    mn = min(vals)
    s = sum(vals)
    if mn == 5:
        return "strong"
    if 1 in vals:
        return "weak"
    if mn >= 3 and s >= 11:
        return "adequate"
    return "weak"


def main():
    data = json.loads(PATH.read_text(encoding="utf-8"))
    items = data["items"]
    assert len(items) == 89

    for i, it in enumerate(items):
        cand = (it.get("candidate_answer") or {}).get("text") or ""
        cand_empty = not cand.strip()

        if i in UNSCORED_INDICES:
            it["reference_score"] = None
            it["unscored_reason"] = "no_interviewer_signal"
            continue

        if i not in SCORES:
            raise RuntimeError(f"item {i} ({it['source_id']}) has no score assigned")

        fc, fo, cl, src, rat = SCORES[i]
        # missing case (empty answer) — force aggregate=missing
        if cand_empty:
            fc, fo, cl = 1, 1, 1
        agg = aggregate(fc, fo, cl, cand_empty)
        it["reference_score"] = {
            "factual_correctness": fc,
            "focus": fo,
            "clarity": cl,
            "aggregate": agg,
            "signal_source": src,
            "rationale": rat,
        }

    data["labeling"] = {
        "labeled_at": "2026-05-16",
        "labeler": "claude-code-opus-4-7",
        "criteria_source": "md/assessors.md (1..5, симплификация 2026-05-11)",
        "policy": "score only from interviewer_feedback and/or reference_answer; no industry baseline",
        "stats": {
            "total": len(items),
            "labeled": sum(1 for it in items if it.get("reference_score") is not None),
            "unscored": sum(1 for it in items if it.get("reference_score") is None),
        },
    }
    # Move 'labeling' to come right after 'split_strategy' for readability
    ordered = {}
    for k in data:
        if k == "items":
            continue
        ordered[k] = data[k]
    ordered["items"] = data["items"]
    data = ordered

    PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {PATH}")
    print(f"labeled={data['labeling']['stats']['labeled']}, unscored={data['labeling']['stats']['unscored']}, total={data['labeling']['stats']['total']}")


if __name__ == "__main__":
    main()
