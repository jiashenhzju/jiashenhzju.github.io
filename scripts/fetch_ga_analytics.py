#!/usr/bin/env python3
"""从 Google Analytics 4 (Data API) 拉取访客地理数据，写入 assets/json/analytics.json。

由 .github/workflows/update-analytics.yml 定时调用。

需要两个环境变量：
- GA_PROPERTY_ID:      GA4 资源 ID（纯数字，例如 123456789）
- GA_CREDENTIALS_JSON: Google 服务账号密钥 JSON 的完整内容（作为 GitHub Secret 注入）

若缺少任一变量，脚本会打印提示并以 0 退出（不报错），保留现有 analytics.json。
"""

import json
import os
import sys
from datetime import date
from pathlib import Path

OUTPUT_PATH = Path(__file__).resolve().parent.parent / "assets" / "json" / "analytics.json"
START_DATE = "2026-07-01"  # 统计起始日期，可按需修改


def main() -> int:
    property_id = os.environ.get("GA_PROPERTY_ID", "").strip()
    creds_json = os.environ.get("GA_CREDENTIALS_JSON", "").strip()

    if not property_id or not creds_json:
        print(
            "跳过：未配置 GA_PROPERTY_ID / GA_CREDENTIALS_JSON，"
            "保留现有 analytics.json。"
        )
        return 0

    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import (
        DateRange,
        Dimension,
        Metric,
        RunReportRequest,
    )
    from google.oauth2 import service_account

    credentials = service_account.Credentials.from_service_account_info(
        json.loads(creds_json)
    )
    client = BetaAnalyticsDataClient(credentials=credentials)

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="country")],
        metrics=[Metric(name="screenPageViews"), Metric(name="totalUsers")],
        date_ranges=[DateRange(start_date=START_DATE, end_date="today")],
    )
    response = client.run_report(request)

    geo_data = []
    total_page_views = 0
    total_visitors = 0
    for row in response.rows:
        country = row.dimension_values[0].value
        page_views = int(row.metric_values[0].value or 0)
        users = int(row.metric_values[1].value or 0)
        total_page_views += page_views
        total_visitors += users
        if country and country != "(not set)":
            geo_data.append({"country": country, "visitors": users})

    geo_data.sort(key=lambda x: x["visitors"], reverse=True)

    payload = {
        "totalPageViews": total_page_views,
        "totalVisitors": total_visitors,
        "lastUpdated": date.today().isoformat(),
        "geoData": geo_data,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"已写入 {OUTPUT_PATH}：{total_page_views} 次浏览，{len(geo_data)} 个国家。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
