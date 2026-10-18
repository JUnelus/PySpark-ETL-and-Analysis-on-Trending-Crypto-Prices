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

![Last Update](https://img.shields.io/badge/last%20update-2026--10--18%2001%3A35%20UTC-blue)

- Pipeline run time: **2026-10-18 01:35 UTC**
- Snapshot date: **2026-10-18**
- Coins tracked: **15**
- Avg daily price change: **0.15%**

- Top gainer: **XMR (4.94%)**
- Top loser: **HYPE (-1.43%)**

### Trend Charts

![Daily Price Change](artifacts/charts/daily_price_change.png)

![Market Cap Snapshot](artifacts/charts/market_cap_snapshot.png)

### Top Coins Snapshot

| Coin | Symbol | Price | Daily Change | Trend |
|---|---:|---:|---:|---|
| Bitcoin | BTC | $81,542.0000 | 0.10% | Sideways |
| Ethereum | ETH | $2,405.0500 | -0.55% | Sideways |
| Tether | USDT | $0.9991 | 0.01% | Sideways |
| BNB | BNB | $718.6700 | -0.10% | Sideways |
| XRP | XRP | $1.3000 | 0.00% | Sideways |
| USDC | USDC | $0.9998 | -0.01% | Sideways |
| Solana | SOL | $103.5900 | -0.79% | Sideways |
| TRON | TRX | $0.3335 | -0.56% | Sideways |
| Figure Heloc | FIGR_HELOC | $1.0670 | 2.99% | Bullish |
| Zcash | ZEC | $1,133.1400 | -1.06% | Bearish |

<!-- AUTO-GENERATED-SECTION:END -->
