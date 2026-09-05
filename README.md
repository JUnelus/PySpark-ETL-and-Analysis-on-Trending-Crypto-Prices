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

![Last Update](https://img.shields.io/badge/last%20update-2026--09--05%2001%3A32%20UTC-blue)

- Pipeline run time: **2026-09-05 01:32 UTC**
- Snapshot date: **2026-09-05**
- Coins tracked: **15**
- Avg daily price change: **-0.35%**

- Top gainer: **ZEC (8.3%)**
- Top loser: **RAIN (-3.96%)**

### Trend Charts

![Daily Price Change](artifacts/charts/daily_price_change.png)

![Market Cap Snapshot](artifacts/charts/market_cap_snapshot.png)

### Top Coins Snapshot

| Coin | Symbol | Price | Daily Change | Trend |
|---|---:|---:|---:|---|
| Bitcoin | BTC | $79,664.0000 | -1.46% | Bearish |
| Ethereum | ETH | $2,455.4200 | -1.99% | Bearish |
| Tether | USDT | $1.0000 | 0.00% | Sideways |
| BNB | BNB | $722.2000 | 0.28% | Sideways |
| XRP | XRP | $1.4000 | -2.78% | Bearish |
| USDC | USDC | $1.0000 | 0.01% | Sideways |
| Solana | SOL | $102.0000 | -1.49% | Bearish |
| TRON | TRX | $0.3318 | 0.54% | Sideways |
| Figure Heloc | FIGR_HELOC | $1.0380 | 0.58% | Sideways |
| Hyperliquid | HYPE | $84.2300 | -2.96% | Bearish |

<!-- AUTO-GENERATED-SECTION:END -->
