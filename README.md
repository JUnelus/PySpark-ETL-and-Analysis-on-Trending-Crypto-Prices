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

![Last Update](https://img.shields.io/badge/last%20update-2026--08--23%2001%3A54%20UTC-blue)

- Pipeline run time: **2026-08-23 01:54 UTC**
- Snapshot date: **2026-08-23**
- Coins tracked: **15**
- Avg daily price change: **0.27%**

- Top gainer: **HYPE (5.47%)**
- Top loser: **RAIN (-6.25%)**

### Trend Charts

![Daily Price Change](artifacts/charts/daily_price_change.png)

![Market Cap Snapshot](artifacts/charts/market_cap_snapshot.png)

### Top Coins Snapshot

| Coin | Symbol | Price | Daily Change | Trend |
|---|---:|---:|---:|---|
| Bitcoin | BTC | $77,239.0000 | -0.91% | Sideways |
| Ethereum | ETH | $2,427.2300 | -3.54% | Bearish |
| Tether | USDT | $0.9998 | -0.01% | Sideways |
| XRP | XRP | $1.4900 | -0.67% | Sideways |
| BNB | BNB | $698.5400 | 1.37% | Bullish |
| USDC | USDC | $0.9998 | -0.01% | Sideways |
| Solana | SOL | $96.0500 | 2.40% | Bullish |
| TRON | TRX | $0.3453 | 0.38% | Sideways |
| Figure Heloc | FIGR_HELOC | $1.0000 | -2.91% | Bearish |
| Hyperliquid | HYPE | $80.4700 | 5.47% | Bullish |

<!-- AUTO-GENERATED-SECTION:END -->
