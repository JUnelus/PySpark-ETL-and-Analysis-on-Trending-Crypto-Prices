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

![Last Update](https://img.shields.io/badge/last%20update-2026--08--12%2001%3A57%20UTC-blue)

- Pipeline run time: **2026-08-12 01:57 UTC**
- Snapshot date: **2026-08-12**
- Coins tracked: **15**
- Avg daily price change: **0.29%**

- Top gainer: **FIGR_HELOC (3.49%)**
- Top loser: **LEO (-4.62%)**

### Trend Charts

![Daily Price Change](artifacts/charts/daily_price_change.png)

![Market Cap Snapshot](artifacts/charts/market_cap_snapshot.png)

### Top Coins Snapshot

| Coin | Symbol | Price | Daily Change | Trend |
|---|---:|---:|---:|---|
| Bitcoin | BTC | $63,789.0000 | -0.34% | Sideways |
| Ethereum | ETH | $1,883.2200 | 0.36% | Sideways |
| Tether | USDT | $0.9992 | 0.00% | Sideways |
| BNB | BNB | $618.4800 | 3.14% | Bullish |
| USDC | USDC | $0.9996 | 0.00% | Sideways |
| XRP | XRP | $1.0220 | 0.69% | Sideways |
| Solana | SOL | $76.4300 | 0.55% | Sideways |
| TRON | TRX | $0.3344 | 1.11% | Bullish |
| Figure Heloc | FIGR_HELOC | $1.0380 | 3.49% | Bullish |
| Hyperliquid | HYPE | $54.5900 | -1.46% | Bearish |

<!-- AUTO-GENERATED-SECTION:END -->
