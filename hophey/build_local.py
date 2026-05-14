#!/usr/bin/env python3
"""Build index.html locally using pre-fetched data from Databricks MCP.

This script is used for local development when the full generate_report.py
cannot connect to Databricks directly (e.g., no databricks-sql-connector).
For production/CI use generate_report.py instead.
"""

import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent / "template.html"
OUTPUT_PATH = Path(__file__).parent / "index.html"
DATA_PATH = Path(__file__).parent / "report_data.json"


def _week_boundaries():
    today = datetime.now().date()
    last_sunday = today - timedelta(days=today.isoweekday())
    four_weeks_ago_monday = last_sunday - timedelta(days=27)
    return str(four_weeks_ago_monday), str(last_sunday)


def main():
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    js_data = f"const REPORT_DATA = {json.dumps(data, ensure_ascii=False, default=str)};"
    html = template.replace("/*__REPORT_DATA__*/", js_data)
    OUTPUT_PATH.write_text(html, encoding="utf-8")
    print(f"Done! Report written to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
