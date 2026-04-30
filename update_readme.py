from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

README_PATH = Path("README.md")
SUMMARY_PATH = Path("artifacts/reports/daily_summary.json")
LATEST_TRENDS_PATH = Path("output/latest_trends.csv")
START_MARKER = "<!-- AUTO-GENERATED-SECTION:START -->"
END_MARKER = "<!-- AUTO-GENERATED-SECTION:END -->"


def _build_table(df: pd.DataFrame) -> str:
    table_df = df[["name", "symbol", "current_price", "daily_price_change_pct", "trend_label"]].copy()
    table_df["symbol"] = table_df["symbol"].str.upper()
    table_df["current_price"] = table_df["current_price"].map(lambda v: f"${v:,.4f}")
    table_df["daily_price_change_pct"] = table_df["daily_price_change_pct"].map(
        lambda v: "N/A" if pd.isna(v) else f"{v:.2f}%"
    )

    lines = ["| Coin | Symbol | Price | Daily Change | Trend |", "|---|---:|---:|---:|---|"]
    for _, row in table_df.iterrows():
        lines.append(
            f"| {row['name']} | {row['symbol']} | {row['current_price']} | {row['daily_price_change_pct']} | {row['trend_label']} |"
        )
    return "\n".join(lines)


def update_readme() -> None:
    if not README_PATH.exists():
        raise FileNotFoundError("README.md not found")
    if not SUMMARY_PATH.exists():
        raise FileNotFoundError(f"Expected summary file not found: {SUMMARY_PATH}")
    if not LATEST_TRENDS_PATH.exists():
        raise FileNotFoundError(f"Expected latest trends file not found: {LATEST_TRENDS_PATH}")

    summary = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
    latest_df = pd.read_csv(str(LATEST_TRENDS_PATH)).sort_values("market_cap_rank").head(10)

    update_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    badge_timestamp = update_time.replace("-", "--").replace(" ", "%20").replace(":", "%3A")

    top_gainer = summary.get("top_gainer") or {}
    top_loser = summary.get("top_loser") or {}
    avg_change = summary.get("avg_daily_price_change_pct")
    avg_change_display = "N/A" if avg_change is None else f"{avg_change}%"

    generated_block = "\n".join(
        [
            START_MARKER,
            "## Latest Automated Update",
            "",
            f"![Last Update](https://img.shields.io/badge/last%20update-{badge_timestamp}-blue)",
            "",
            f"- Pipeline run time: **{update_time}**",
            f"- Snapshot date: **{summary.get('snapshot_date', 'N/A')}**",
            f"- Coins tracked: **{summary.get('coins_tracked', 'N/A')}**",
            f"- Avg daily price change: **{avg_change_display}**",
            "",
            f"- Top gainer: **{top_gainer.get('symbol', 'N/A')} ({top_gainer.get('change_pct', 'N/A')}%)**",
            f"- Top loser: **{top_loser.get('symbol', 'N/A')} ({top_loser.get('change_pct', 'N/A')}%)**",
            "",
            "### Trend Charts",
            "",
            "![Daily Price Change](artifacts/charts/daily_price_change.png)",
            "",
            "![Market Cap Snapshot](artifacts/charts/market_cap_snapshot.png)",
            "",
            "### Top Coins Snapshot",
            "",
            _build_table(latest_df),
            "",
            END_MARKER,
        ]
    )

    readme_content = README_PATH.read_text(encoding="utf-8")
    if START_MARKER in readme_content and END_MARKER in readme_content:
        start_idx = readme_content.index(START_MARKER)
        end_idx = readme_content.index(END_MARKER) + len(END_MARKER)
        new_content = readme_content[:start_idx] + generated_block + readme_content[end_idx:]
    else:
        new_content = readme_content.rstrip() + "\n\n" + generated_block + "\n"

    README_PATH.write_text(new_content, encoding="utf-8")


if __name__ == "__main__":
    update_readme()




