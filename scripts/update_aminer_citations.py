#!/usr/bin/env python3
import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.request import Request, urlopen

SOURCE_URL = "https://www.aminer.cn/pub/6902b576163c01c85010bc38/a-survey-on-efficient-vision-language-action-models"
PROXY_URL = "https://r.jina.ai/http://" + SOURCE_URL
OUTPUT_PATH = Path(__file__).resolve().parents[1] / "assets" / "data" / "aminer_citations.json"
PAPER_ID = "6902b576163c01c85010bc38"
TITLE = "A Survey on Efficient Vision-Language-Action Models"


def fetch_text(url: str) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def parse_counts(text: str) -> tuple[int, int | None]:
    match = re.search(r"Cited\*\*(\d+)\*\*\|Views\s+(\d+)", text)
    if match:
        return int(match.group(1)), int(match.group(2))

    fallback = re.search(r"Cited\D+(\d+)", text)
    if not fallback:
        raise ValueError("Unable to parse citation count from AMiner response")

    return int(fallback.group(1)), None


def main() -> int:
    markdown = fetch_text(PROXY_URL)
    citations, views = parse_counts(markdown)
    now = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")

    data = {
        "updated_at": now,
        "publications": {
            PAPER_ID: {
                "title": TITLE,
                "num_citations": citations,
                "views": views,
                "source_url": SOURCE_URL,
            }
        },
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(f"Updated {OUTPUT_PATH} with {citations} citations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
