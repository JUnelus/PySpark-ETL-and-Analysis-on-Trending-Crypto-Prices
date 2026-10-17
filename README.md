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

![Last Update](https://img.shields.io/badge/last%20update-2026--10--17%2001%3A32%20UTC-blue)

- Pipeline run time: **2026-10-17 01:32 UTC**
- Snapshot date: **2026-10-17**
- Coins tracked: **15**
- Avg daily price change: **-1.06%**

- Top gainer: **TRX (0.54%)**
- Top loser: **ZEC (-6.91%)**

### Trend Charts

![Daily Price Change](artifacts/charts/daily_price_change.png)

![Market Cap Snapshot](artifacts/charts/market_cap_snapshot.png)

### Top Coins Snapshot

| Coin | Symbol | Price | Daily Change | Trend |
|---|---:|---:|---:|---|
| Bitcoin | BTC | $81,462.0000 | -0.88% | Sideways |
| Ethereum | ETH | $2,418.3800 | -0.64% | Sideways |
| Tether | USDT | $0.9991 | 0.01% | Sideways |
| BNB | BNB | $719.4000 | -1.15% | Bearish |
| XRP | XRP | $1.3000 | -2.26% | Bearish |
| USDC | USDC | $0.9998 | 0.03% | Sideways |
| Solana | SOL | $104.4100 | -0.79% | Sideways |
| TRON | TRX | $0.3354 | 0.54% | Sideways |
| Figure Heloc | FIGR_HELOC | $1.0360 | 0.48% | Sideways |
| Zcash | ZEC | $1,145.2600 | -6.91% | Bearish |

<!-- AUTO-GENERATED-SECTION:END -->
