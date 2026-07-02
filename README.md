# PySpark-ETL-and-Analysis-on-Trending-Crypto-Prices

Daily ETL and trend analysis project for top cryptocurrencies using Python, PySpark, and GitHub Actions.

## What this project does

- Pulls the latest top crypto market data from CoinGecko.
- Stores both the latest snapshot and a daily history CSV.
- Runs a PySpark ETL job to compute day-over-day trend metrics.
- Generates daily charts and a trend summary report.
- Auto-updates this `README.md` and commits changes from GitHub Actions on a schedule.

## Project structure

- `fetch_crypto_data.py`: Download and persist the latest and historical data.
- `pyspark_etl.py`: Compute trend metrics in PySpark.
- `analysis/exploratory_analysis.py`: Build charts and daily summary artifacts.
- `update_readme.py`: Inject latest metrics/charts/table into the README.
- `pipeline.py`: Orchestrate all steps end-to-end.
- `.github/workflows/daily_pipeline.yml`: Daily automated run and commit.

## Quick start (local)

```bash
python -m pip install -r requirements.txt
python pipeline.py
```

If you already have data and only want to re-run ETL/analysis:

```bash
python pipeline.py --skip-fetch
```

## Automated daily updates (GitHub Actions)

The workflow runs daily and can also be triggered manually.
It updates:

- `data/crypto_prices.csv`
- `data/crypto_prices_history.csv`
- `output/trends_report.csv`
- `output/latest_trends.csv`
- `artifacts/charts/*.png`
- `artifacts/reports/daily_summary.*`
- `README.md`

<!-- AUTO-GENERATED-SECTION:START -->
## Latest Automated Update

![Last Update](https://img.shields.io/badge/last%20update-2026--07--02%2001%3A59%20UTC-blue)

- Pipeline run time: **2026-07-02 01:59 UTC**
- Snapshot date: **2026-07-02**
- Coins tracked: **15**
- Avg daily price change: **1.0%**

- Top gainer: **SOL (5.6%)**
- Top loser: **HYPE (-2.45%)**

### Trend Charts

![Daily Price Change](artifacts/charts/daily_price_change.png)

![Market Cap Snapshot](artifacts/charts/market_cap_snapshot.png)

### Top Coins Snapshot

| Coin | Symbol | Price | Daily Change | Trend |
|---|---:|---:|---:|---|
| Bitcoin | BTC | $60,078.0000 | 2.34% | Bullish |
| Ethereum | ETH | $1,617.2200 | 2.59% | Bullish |
| Tether | USDT | $0.9989 | 0.04% | Sideways |
| BNB | BNB | $549.6900 | 0.42% | Sideways |
| USDC | USDC | $0.9997 | 0.01% | Sideways |
| XRP | XRP | $1.0560 | 1.44% | Bullish |
| Solana | SOL | $78.0200 | 5.60% | Bullish |
| TRON | TRX | $0.3161 | 0.53% | Sideways |
| Figure Heloc | FIGR_HELOC | $1.0280 | 1.38% | Bullish |
| Hyperliquid | HYPE | $62.8100 | -2.45% | Bearish |

<!-- AUTO-GENERATED-SECTION:END -->
