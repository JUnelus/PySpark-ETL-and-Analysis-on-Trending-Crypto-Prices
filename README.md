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

![Last Update](https://img.shields.io/badge/last%20update-2026--09--04%2001%3A32%20UTC-blue)

- Pipeline run time: **2026-09-04 01:32 UTC**
- Snapshot date: **2026-09-04**
- Coins tracked: **15**
- Avg daily price change: **3.8%**

- Top gainer: **ZEC (15.05%)**
- Top loser: **USDC (0.01%)**

### Trend Charts

![Daily Price Change](artifacts/charts/daily_price_change.png)

![Market Cap Snapshot](artifacts/charts/market_cap_snapshot.png)

### Top Coins Snapshot

| Coin | Symbol | Price | Daily Change | Trend |
|---|---:|---:|---:|---|
| Bitcoin | BTC | $80,848.0000 | 4.53% | Bullish |
| Ethereum | ETH | $2,505.3400 | 4.92% | Bullish |
| Tether | USDT | $1.0000 | 0.03% | Sideways |
| BNB | BNB | $720.1800 | 4.33% | Bullish |
| XRP | XRP | $1.4400 | 5.88% | Bullish |
| USDC | USDC | $0.9999 | 0.01% | Sideways |
| Solana | SOL | $103.5400 | 3.35% | Bullish |
| TRON | TRX | $0.3300 | 1.56% | Bullish |
| Figure Heloc | FIGR_HELOC | $1.0320 | 1.88% | Bullish |
| Hyperliquid | HYPE | $86.8000 | 6.27% | Bullish |

<!-- AUTO-GENERATED-SECTION:END -->
