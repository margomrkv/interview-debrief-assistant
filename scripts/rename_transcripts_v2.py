#!/usr/bin/env python3
"""Rename transcript leaf folders to hiring pattern (2026-05 v2).

Pattern:
  {kind}-{role}-{level}[-{target}]-{publisher}[-{candidate}][-{topic}]-{YYYY-MM-DD}

Publisher: novoselov (not vadim) for Vadim Novoselov channel.
"""

from __future__ import annotations

import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
T = REPO / "transcripts"

# old relative path (under transcripts/) -> new relative path
RENAMES: dict[str, str] = {
    # --- avito ---
    "mock-interviews/avito/avito-middle-product-analyst-20240404": "mock-interviews/avito/mock-product-analyst-middle-avito-avito-2024-04-04",
    # --- karpov hiring ---
    "mock-interviews/karpov/karpov-junior-data-scientist-20220330": "mock-interviews/karpov/mock-data-scientist-junior-karpov-2022-03-30",
    "mock-interviews/karpov/karpov-junior-ml-engineer-20230309": "mock-interviews/karpov/mock-ml-engineer-junior-karpov-2023-03-09",
    "mock-interviews/karpov/karpov-middle-data-scientist-ml-20220626": "mock-interviews/karpov/mock-data-scientist-middle-karpov-ml-2022-06-26",
    "mock-interviews/karpov/karpov-middle-data-scientist-python-20220702": "mock-interviews/karpov/mock-data-scientist-middle-karpov-python-2022-07-02",
    "mock-interviews/karpov/karpov-junior-data-analyst-sasha-20210913": "mock-interviews/karpov/mock-data-analyst-junior-karpov-sasha-2021-09-13",
    "mock-interviews/karpov/karpov-junior-data-analyst-yegor-20210913": "mock-interviews/karpov/mock-data-analyst-junior-karpov-yegor-2021-09-13",
    "mock-interviews/karpov/karpov-junior-data-analyst-vyacheslav-20210624": "mock-interviews/karpov/mock-data-analyst-junior-karpov-vyacheslav-2021-06-24",
    "mock-interviews/karpov/karpov-junior-data-analyst-pasha-20210624": "mock-interviews/karpov/mock-data-analyst-junior-karpov-pasha-2021-06-24",
    "mock-interviews/karpov/karpov-game-analyst-20211120": "mock-interviews/karpov/mock-game-analyst-middle-karpov-2021-11-20",
    "mock-interviews/karpov/karpov-senior-data-analyst-20240523": "mock-interviews/karpov/mock-data-analyst-senior-karpov-2024-05-23",
    # karpov workshops (role slot = track; level senior default)
    "mock-interviews/karpov/karpov-behavioral-v1-20221110": "mock-interviews/karpov/mock-behavioral-senior-karpov-v1-2022-11-10",
    "mock-interviews/karpov/karpov-behavioral-v2-20221215": "mock-interviews/karpov/mock-behavioral-senior-karpov-v2-2022-12-15",
    "mock-interviews/karpov/karpov-behavioral-v3-20230121": "mock-interviews/karpov/mock-behavioral-senior-karpov-v3-2023-01-21",
    "mock-interviews/karpov/karpov-ml-system-design-v1-20210803": "mock-interviews/karpov/mock-ml-system-design-senior-karpov-v1-2021-08-03",
    "mock-interviews/karpov/karpov-ml-system-design-v2-20210828": "mock-interviews/karpov/mock-ml-system-design-senior-karpov-v2-2021-08-28",
    "mock-interviews/karpov/karpov-ml-system-design-v3-20210919": "mock-interviews/karpov/mock-ml-system-design-senior-karpov-v3-2021-09-19",
    "mock-interviews/karpov/karpov-system-design-v1-20220119": "mock-interviews/karpov/mock-system-design-senior-karpov-v1-2022-01-19",
    "mock-interviews/karpov/karpov-system-design-v2-20220228": "mock-interviews/karpov/mock-system-design-senior-karpov-v2-2022-02-28",
    "mock-interviews/karpov/karpov-system-design-v3-20220324": "mock-interviews/karpov/mock-system-design-senior-karpov-v3-2022-03-24",
    "mock-interviews/karpov/karpov-system-design-v4-20220505": "mock-interviews/karpov/mock-system-design-senior-karpov-v4-2022-05-05",
    "mock-interviews/karpov/karpov-system-design-20230714": "mock-interviews/karpov/mock-system-design-senior-karpov-2023-07-14",
    "mock-interviews/karpov/karpov-ab-testing-20240119": "mock-interviews/karpov/mock-ab-testing-senior-karpov-2024-01-19",
    # --- datainterview ---
    "mock-interviews/datainterview/amazon-data-scientist-ab-testing-20220127": "mock-interviews/datainterview/mock-data-scientist-senior-amazon-ab-testing-datainterview-2022-01-27",
    "mock-interviews/datainterview/amazon-data-scientist-fraud-model-20220106": "mock-interviews/datainterview/mock-data-scientist-senior-amazon-fraud-model-datainterview-2022-01-06",
    "mock-interviews/datainterview/doordash-data-scientist-commentary-20210215": "mock-interviews/datainterview/mock-data-scientist-senior-doordash-commentary-datainterview-2021-02-15",
    "mock-interviews/datainterview/facebook-data-scientist-churn-sql-20210930": "mock-interviews/datainterview/mock-data-scientist-senior-facebook-churn-sql-datainterview-2021-09-30",
    "mock-interviews/datainterview/facebook-data-scientist-segment-influencers-20201224": "mock-interviews/datainterview/mock-data-scientist-senior-facebook-segment-influencers-datainterview-2020-12-24",
    "mock-interviews/datainterview/meta-data-scientist-call-suggestion-ab-20211126": "mock-interviews/datainterview/mock-data-scientist-senior-meta-call-suggestion-ab-datainterview-2021-11-26",
    "mock-interviews/datainterview/uber-data-scientist-coach-20220428": "mock-interviews/datainterview/mock-data-scientist-senior-uber-coach-datainterview-2022-04-28",
    # --- interview-query ---
    "mock-interviews/interview-query/amazon-business-intelligence-duplicate-products-20200529": "mock-interviews/interview-query/mock-business-intelligence-middle-amazon-duplicate-products-interview-query-2020-05-29",
    "mock-interviews/interview-query/amazon-data-engineer-tips-20200521": "mock-interviews/interview-query/mock-data-engineer-middle-amazon-tips-interview-query-2020-05-21",
    "mock-interviews/interview-query/amazon-sql-conversation-distribution-20220131": "mock-interviews/interview-query/mock-data-analyst-middle-amazon-sql-conversation-interview-query-2022-01-31",
    "mock-interviews/interview-query/dropbox-data-scientist-20210728": "mock-interviews/interview-query/mock-data-scientist-senior-dropbox-interview-query-2021-07-28",
    "mock-interviews/interview-query/facebook-product-investigation-fill-rate-20200706": "mock-interviews/interview-query/mock-product-analyst-middle-facebook-fill-rate-interview-query-2020-07-06",
    "mock-interviews/interview-query/google-ml-system-design-20200826": "mock-interviews/interview-query/mock-ml-engineer-senior-google-ml-system-design-interview-query-2020-08-26",
    "mock-interviews/interview-query/linkedin-data-scientist-feedback-20200909": "mock-interviews/interview-query/mock-data-scientist-senior-linkedin-interview-query-2020-09-09",
    "mock-interviews/interview-query/linkedin-ml-recommendation-engine-20210622": "mock-interviews/interview-query/mock-ml-engineer-senior-linkedin-recommendation-engine-interview-query-2021-06-22",
    "mock-interviews/interview-query/meta-ml-illegal-items-20220118": "mock-interviews/interview-query/mock-ml-engineer-senior-meta-illegal-items-interview-query-2022-01-18",
    "mock-interviews/interview-query/meta-product-sense-friend-requests-20220421": "mock-interviews/interview-query/mock-product-analyst-senior-meta-friend-requests-interview-query-2022-04-21",
    "mock-interviews/interview-query/netflix-ml-type-ahead-20200514": "mock-interviews/interview-query/mock-ml-engineer-senior-netflix-type-ahead-interview-query-2020-05-14",
    "mock-interviews/interview-query/uber-data-scientist-ride-requests-20200723": "mock-interviews/interview-query/mock-data-scientist-senior-uber-ride-requests-interview-query-2020-07-23",
    "mock-interviews/interview-query/verizon-senior-data-scientist-fraud-case-20260224": "mock-interviews/interview-query/mock-data-scientist-senior-verizon-fraud-case-interview-query-2026-02-24",
    "mock-interviews/interview-query/walmart-data-scientist-underpricing-20200804": "mock-interviews/interview-query/mock-data-scientist-senior-walmart-underpricing-interview-query-2020-08-04",
    # --- interviewing.io ---
    "mock-interviews/interviewing-io/faang-ml-system-design-ab-platform-20260323": "mock-interviews/interviewing-io/mock-ml-engineer-senior-faang-ab-platform-interviewing-io-2026-03-23",
    "mock-interviews/interviewing-io/google-ml-system-design-newsfeed-20251111": "mock-interviews/interviewing-io/mock-ml-engineer-senior-google-newsfeed-interviewing-io-2025-11-11",
    "mock-interviews/interviewing-io/google-technical-data-wrangling-20200428": "mock-interviews/interviewing-io/mock-data-scientist-middle-google-data-wrangling-interviewing-io-2020-04-28",
    "mock-interviews/interviewing-io/meta-e5-e6-ml-system-design-instagram-reels-20250805": "mock-interviews/interviewing-io/mock-ml-engineer-senior-meta-instagram-reels-interviewing-io-2025-08-05",
    "mock-interviews/interviewing-io/meta-e6-ml-system-design-fraud-20250812": "mock-interviews/interviewing-io/mock-ml-engineer-senior-meta-fraud-scam-interviewing-io-2025-08-12",
    "mock-interviews/interviewing-io/meta-ml-system-design-ml-platform-20250603": "mock-interviews/interviewing-io/mock-ml-engineer-senior-meta-ml-platform-interviewing-io-2025-06-03",
    "mock-interviews/interviewing-io/meta-ml-system-design-yelp-recs-20260410": "mock-interviews/interviewing-io/mock-ml-engineer-senior-meta-yelp-recs-interviewing-io-2026-04-10",
    "mock-interviews/interviewing-io/meta-python-xml-parser-20211104": "mock-interviews/interviewing-io/mock-software-engineer-middle-meta-xml-parser-interviewing-io-2021-11-04",
    "mock-interviews/interviewing-io/meta-staff-ml-system-design-harmful-content-20230819": "mock-interviews/interviewing-io/mock-ml-engineer-senior-meta-harmful-content-interviewing-io-2023-08-19",
    # --- dataengineers-pro ---
    "mock-interviews/dataengineers-pro/junior-data-engineer-practice-20250218": "mock-interviews/dataengineers-pro/mock-data-engineer-junior-dataengineers-pro-practice-2025-02-18",
    "mock-interviews/dataengineers-pro/junior-data-engineer-rzv-s1e5-20240902": "mock-interviews/dataengineers-pro/mock-data-engineer-junior-dataengineers-pro-rzv-s1e5-2024-09-02",
    "mock-interviews/dataengineers-pro/middle-data-engineer-rzv-s1e4-20240727": "mock-interviews/dataengineers-pro/mock-data-engineer-middle-dataengineers-pro-rzv-s1e4-2024-07-27",
    "mock-interviews/dataengineers-pro/middle-data-engineer-rzv-s2e1-20250318": "mock-interviews/dataengineers-pro/mock-data-engineer-middle-dataengineers-pro-rzv-s2e1-2025-03-18",
    "mock-interviews/dataengineers-pro/middle-data-engineer-rzv-s2e2-20250318": "mock-interviews/dataengineers-pro/mock-data-engineer-middle-dataengineers-pro-rzv-s2e2-2025-03-18",
    "mock-interviews/dataengineers-pro/senior-data-engineer-rzv-s1e7-20241002": "mock-interviews/dataengineers-pro/mock-data-engineer-senior-dataengineers-pro-rzv-s1e7-2024-10-02",
    "mock-interviews/dataengineers-pro/tinkoff-data-engineer-dwh-connect-20240410": "mock-interviews/dataengineers-pro/mock-data-engineer-middle-tinkoff-dwh-connect-dataengineers-pro-2024-04-10",
    # --- real: vadim-novoselov -> novoselov ---
    "real-interviews/vadim-novoselov/sber-data-scientist-20230721": "real-interviews/novoselov/real-data-scientist-middle-sber-novoselov-2023-07-21",
    "real-interviews/vadim-novoselov/yandex-data-scientist-ml-20230725": "real-interviews/novoselov/real-data-scientist-senior-yandex-ml-novoselov-2023-07-25",
    "real-interviews/vadim-novoselov/1xbet-data-scientist-20230802": "real-interviews/novoselov/real-data-scientist-senior-1xbet-novoselov-2023-08-02",
    "real-interviews/vadim-novoselov/general-data-science-theory-20230806": "real-interviews/novoselov/real-data-scientist-middle-novoselov-theory-2023-08-06",
    "real-interviews/vadim-novoselov/raiffeisen-data-scientist-20230816": "real-interviews/novoselov/real-data-scientist-middle-raiffeisen-novoselov-2023-08-16",
    "real-interviews/vadim-novoselov/vk-data-science-algorithms-20230827": "real-interviews/novoselov/real-data-scientist-middle-vk-algorithms-novoselov-2023-08-27",
    "real-interviews/vadim-novoselov/gosuslugi-data-scientist-20231117": "real-interviews/novoselov/real-data-scientist-middle-gosuslugi-novoselov-2023-11-17",
    "real-interviews/vadim-novoselov/general-data-scientist-live-coding-20231126": "real-interviews/novoselov/real-data-scientist-senior-novoselov-live-coding-2023-11-26",
    "real-interviews/vadim-novoselov/junior-data-scientist-answers-20240926": "real-interviews/novoselov/real-data-scientist-junior-novoselov-answers-2024-09-26",
    "real-interviews/vadim-novoselov/moex-data-scientist-ml-system-design-20241113": "real-interviews/novoselov/real-data-scientist-senior-moex-ml-system-design-novoselov-2024-11-13",
    "real-interviews/vadim-novoselov/mytona-data-analyst-20241120": "real-interviews/novoselov/real-data-analyst-middle-mytona-novoselov-2024-11-20",
    "real-interviews/vadim-novoselov/samokat-data-scientist-ml-20260225": "real-interviews/novoselov/real-data-scientist-senior-samokat-ml-novoselov-2026-02-25",
    # --- youtube sessions (session- prefix, publisher before date) ---
    "youtube-sessions/dataengineers-pro/data-engineer-spark-interview-tips-20231215": "youtube-sessions/dataengineers-pro/session-data-engineer-spark-tips-dataengineers-pro-2023-12-15",
    "youtube-sessions/yandex-practicum/analytics-newcomer-live-20250601": "youtube-sessions/yandex-practicum/session-analytics-newcomer-live-yandex-practicum-2025-06-01",
    "youtube-sessions/yandex-practicum/ba-da-resume-review-20250930": "youtube-sessions/yandex-practicum/session-ba-da-resume-review-yandex-practicum-2025-09-30",
}

BUCKET_RENAMES = {
    "real-interviews/vadim-novoselov/source.txt": "real-interviews/novoselov/source.txt",
}


def main() -> None:
    applied: list[tuple[str, str]] = []
    for old_rel, new_rel in RENAMES.items():
        src, dst = T / old_rel, T / new_rel
        if not src.exists():
            print(f"SKIP missing: {old_rel}")
            continue
        if dst.exists():
            raise SystemExit(f"Destination exists: {dst}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
        applied.append((old_rel, new_rel))
        print(f"OK {old_rel} -> {new_rel}")

    for old_rel, new_rel in BUCKET_RENAMES.items():
        src, dst = T / old_rel, T / new_rel
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            applied.append((old_rel, new_rel))

    # remove empty vadim-novoselov bucket
    old_bucket = T / "real-interviews/vadim-novoselov"
    if old_bucket.is_dir() and not any(old_bucket.iterdir()):
        old_bucket.rmdir()
        print("Removed empty real-interviews/vadim-novoselov")

    # append to aliases
    aliases_path = T / "aliases.yaml"
    lines = aliases_path.read_text(encoding="utf-8").splitlines()
    lines.append("")
    lines.append("# v2 renames (2026-05-19)")
    for old, new in applied:
        lines.append(f"  {old}: {new}")
    aliases_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nApplied {len(applied)} renames; updated aliases.yaml")


if __name__ == "__main__":
    main()
