from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.use("Agg")


def _plot_price_change(df: pd.DataFrame, output_path: Path) -> None:
	ranked = df.sort_values("daily_price_change_pct", ascending=False).head(10)
	colors = ["#16a34a" if value >= 0 else "#dc2626" for value in ranked["daily_price_change_pct"].fillna(0)]

	plt.figure(figsize=(11, 6))
	plt.bar(ranked["symbol"].str.upper(), ranked["daily_price_change_pct"].fillna(0), color=colors)
	plt.axhline(y=0, color="#6b7280", linewidth=1)
	plt.title("Daily Price Change % (Top Coins)")
	plt.xlabel("Coin")
	plt.ylabel("Daily Price Change %")
	plt.tight_layout()
	plt.savefig(output_path)
	plt.close()


def _plot_market_cap(df: pd.DataFrame, output_path: Path) -> None:
	ranked = df.sort_values("market_cap", ascending=False).head(10)

	plt.figure(figsize=(11, 6))
	plt.bar(ranked["symbol"].str.upper(), ranked["market_cap"] / 1_000_000_000, color="#2563eb")
	plt.title("Market Cap Snapshot (Top Coins)")
	plt.xlabel("Coin")
	plt.ylabel("Market Cap (USD Billions)")
	plt.tight_layout()
	plt.savefig(output_path)
	plt.close()


def generate_daily_analysis(
	latest_trends_path: str = "output/latest_trends.csv",
	charts_dir: str = "artifacts/charts",
	reports_dir: str = "artifacts/reports",
) -> dict:
	latest_path = Path(latest_trends_path)
	if not latest_path.exists():
		raise FileNotFoundError(f"Expected latest trends file not found: {latest_path}")

	df = pd.read_csv(str(latest_path))
	df["daily_price_change_pct"] = pd.to_numeric(df["daily_price_change_pct"], errors="coerce")

	charts_path = Path(charts_dir)
	reports_path = Path(reports_dir)
	charts_path.mkdir(parents=True, exist_ok=True)
	reports_path.mkdir(parents=True, exist_ok=True)

	price_chart = charts_path / "daily_price_change.png"
	market_cap_chart = charts_path / "market_cap_snapshot.png"
	_plot_price_change(df, price_chart)
	_plot_market_cap(df, market_cap_chart)

	valid_change = df.dropna(subset=["daily_price_change_pct"])
	if not valid_change.empty:
		top_gainer_row = valid_change.sort_values("daily_price_change_pct", ascending=False).iloc[0]
		top_loser_row = valid_change.sort_values("daily_price_change_pct", ascending=True).iloc[0]
	else:
		top_gainer_row = None
		top_loser_row = None

	now = datetime.now(timezone.utc)
	summary = {
		"generated_at_utc": now.isoformat(),
		"snapshot_date": str(df["snapshot_date"].iloc[0]) if not df.empty else "",
		"coins_tracked": int(df["id"].nunique()) if "id" in df.columns else int(len(df)),
		"avg_daily_price_change_pct": round(float(valid_change["daily_price_change_pct"].mean()), 2)
		if not valid_change.empty
		else None,
		"top_gainer": {
			"symbol": str(top_gainer_row["symbol"]).upper(),
			"change_pct": round(float(top_gainer_row["daily_price_change_pct"]), 2),
		}
		if top_gainer_row is not None
		else None,
		"top_loser": {
			"symbol": str(top_loser_row["symbol"]).upper(),
			"change_pct": round(float(top_loser_row["daily_price_change_pct"]), 2),
		}
		if top_loser_row is not None
		else None,
	}

	json_path = reports_path / "daily_summary.json"
	md_path = reports_path / "daily_summary.md"
	with json_path.open("w", encoding="utf-8") as fp:
		json.dump(summary, fp, indent=2)

	avg_change_display = (
		"N/A" if summary["avg_daily_price_change_pct"] is None else f"{summary['avg_daily_price_change_pct']}%"
	)

	lines = [
		"# Daily Trend Summary",
		"",
		f"- Generated at (UTC): {summary['generated_at_utc']}",
		f"- Snapshot date: {summary['snapshot_date']}",
		f"- Coins tracked: {summary['coins_tracked']}",
		f"- Average daily price change: {avg_change_display}",
	]
	if summary["top_gainer"]:
		lines.append(
			f"- Top gainer: {summary['top_gainer']['symbol']} ({summary['top_gainer']['change_pct']}%)"
		)
	if summary["top_loser"]:
		lines.append(
			f"- Top loser: {summary['top_loser']['symbol']} ({summary['top_loser']['change_pct']}%)"
		)

	md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
	return summary


if __name__ == "__main__":
	generate_daily_analysis()



