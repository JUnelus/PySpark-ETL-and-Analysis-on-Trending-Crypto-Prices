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

![Last Update](https://img.shields.io/badge/last%20update-2026--05--22%2001%3A59%20UTC-blue)

- Pipeline run time: **2026-05-22 01:59 UTC**
- Snapshot date: **2026-05-22**
- Coins tracked: **15**
- Avg daily price change: **0.03%**

- Top gainer: **TRX (1.74%)**
- Top loser: **ZEC (-2.64%)**

### Trend Charts

![Daily Price Change](artifacts/charts/daily_price_change.png)

![Market Cap Snapshot](artifacts/charts/market_cap_snapshot.png)

### Top Coins Snapshot

| Coin | Symbol | Price | Daily Change | Trend |
|---|---:|---:|---:|---|
| Bitcoin | BTC | $77,509.0000 | -0.34% | Sideways |
| Ethereum | ETH | $2,132.8400 | -0.28% | Sideways |
| Tether | USDT | $0.9990 | 0.01% | Sideways |
| BNB | BNB | $658.6200 | 0.96% | Sideways |
| XRP | XRP | $1.3700 | -0.72% | Sideways |
| USDC | USDC | $0.9998 | 0.02% | Sideways |
| Solana | SOL | $86.9300 | 0.58% | Sideways |
| TRON | TRX | $0.3651 | 1.74% | Bullish |
| Figure Heloc | FIGR_HELOC | $1.0220 | -1.26% | Bearish |
| Dogecoin | DOGE | $0.1058 | 1.31% | Bullish |

<!-- AUTO-GENERATED-SECTION:END -->
