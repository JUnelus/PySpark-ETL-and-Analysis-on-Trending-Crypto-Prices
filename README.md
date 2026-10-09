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

![Last Update](https://img.shields.io/badge/last%20update-2026--10--09%2001%3A49%20UTC-blue)

- Pipeline run time: **2026-10-09 01:49 UTC**
- Snapshot date: **2026-10-09**
- Coins tracked: **15**
- Avg daily price change: **-3.13%**

- Top gainer: **FIGR_HELOC (1.18%)**
- Top loser: **ZEC (-10.33%)**

### Trend Charts

![Daily Price Change](artifacts/charts/daily_price_change.png)

![Market Cap Snapshot](artifacts/charts/market_cap_snapshot.png)

### Top Coins Snapshot

| Coin | Symbol | Price | Daily Change | Trend |
|---|---:|---:|---:|---|
| Bitcoin | BTC | $81,874.0000 | -1.61% | Bearish |
| Ethereum | ETH | $2,481.5200 | -3.86% | Bearish |
| Tether | USDT | $0.9993 | -0.02% | Sideways |
| BNB | BNB | $736.1100 | -4.79% | Bearish |
| XRP | XRP | $1.3900 | -2.80% | Bearish |
| USDC | USDC | $0.9996 | -0.01% | Sideways |
| Solana | SOL | $109.3700 | -5.93% | Bearish |
| TRON | TRX | $0.3323 | -1.06% | Bearish |
| Figure Heloc | FIGR_HELOC | $1.0300 | 1.18% | Bullish |
| Zcash | ZEC | $1,188.9500 | -10.33% | Bearish |

<!-- AUTO-GENERATED-SECTION:END -->
