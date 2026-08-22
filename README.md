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

![Last Update](https://img.shields.io/badge/last%20update-2026--08--22%2001%3A49%20UTC-blue)

- Pipeline run time: **2026-08-22 01:49 UTC**
- Snapshot date: **2026-08-22**
- Coins tracked: **15**
- Avg daily price change: **6.23%**

- Top gainer: **ZEC (30.23%)**
- Top loser: **USDS (0.01%)**

### Trend Charts

![Daily Price Change](artifacts/charts/daily_price_change.png)

![Market Cap Snapshot](artifacts/charts/market_cap_snapshot.png)

### Top Coins Snapshot

| Coin | Symbol | Price | Daily Change | Trend |
|---|---:|---:|---:|---|
| Bitcoin | BTC | $77,952.0000 | 3.23% | Bullish |
| Ethereum | ETH | $2,516.3300 | 6.26% | Bullish |
| Tether | USDT | $0.9999 | 0.02% | Sideways |
| XRP | XRP | $1.5000 | 15.38% | Bullish |
| BNB | BNB | $689.0700 | 3.60% | Bullish |
| USDC | USDC | $1.0000 | 0.02% | Sideways |
| Solana | SOL | $93.8000 | 5.05% | Bullish |
| TRON | TRX | $0.3440 | 1.73% | Bullish |
| Figure Heloc | FIGR_HELOC | $1.0300 | 0.39% | Sideways |
| Hyperliquid | HYPE | $76.3000 | 2.18% | Bullish |

<!-- AUTO-GENERATED-SECTION:END -->
