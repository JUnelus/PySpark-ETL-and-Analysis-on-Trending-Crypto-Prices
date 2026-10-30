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

![Last Update](https://img.shields.io/badge/last%20update-2026--10--30%2001%3A23%20UTC-blue)

- Pipeline run time: **2026-10-30 01:23 UTC**
- Snapshot date: **2026-10-30**
- Coins tracked: **15**
- Avg daily price change: **-1.78%**

- Top gainer: **HYPE (9.82%)**
- Top loser: **XRP (-9.02%)**

### Trend Charts

![Daily Price Change](artifacts/charts/daily_price_change.png)

![Market Cap Snapshot](artifacts/charts/market_cap_snapshot.png)

### Top Coins Snapshot

| Coin | Symbol | Price | Daily Change | Trend |
|---|---:|---:|---:|---|
| Bitcoin | BTC | $76,924.0000 | -4.60% | Bearish |
| Ethereum | ETH | $2,212.2600 | -5.59% | Bearish |
| Tether | USDT | $0.9984 | -0.04% | Sideways |
| BNB | BNB | $699.3600 | -5.85% | Bearish |
| XRP | XRP | $1.2100 | -9.02% | Bearish |
| USDC | USDC | $0.9992 | -0.02% | Sideways |
| Solana | SOL | $94.0000 | -7.08% | Bearish |
| TRON | TRX | $0.3603 | 8.80% | Bullish |
| Figure Heloc | FIGR_HELOC | $1.0310 | 0.10% | Sideways |
| Hyperliquid | HYPE | $89.7300 | 9.82% | Bullish |

<!-- AUTO-GENERATED-SECTION:END -->
