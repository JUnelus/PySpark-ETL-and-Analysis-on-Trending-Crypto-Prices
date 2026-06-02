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

![Last Update](https://img.shields.io/badge/last%20update-2026--06--02%2002%3A04%20UTC-blue)

- Pipeline run time: **2026-06-02 02:04 UTC**
- Snapshot date: **2026-06-02**
- Coins tracked: **15**
- Avg daily price change: **-1.27%**

- Top gainer: **FIGR_HELOC (2.46%)**
- Top loser: **ADA (-5.57%)**

### Trend Charts

![Daily Price Change](artifacts/charts/daily_price_change.png)

![Market Cap Snapshot](artifacts/charts/market_cap_snapshot.png)

### Top Coins Snapshot

| Coin | Symbol | Price | Daily Change | Trend |
|---|---:|---:|---:|---|
| Bitcoin | BTC | $70,595.0000 | -3.53% | Bearish |
| Ethereum | ETH | $1,976.5600 | -0.75% | Sideways |
| Tether | USDT | $0.9986 | 0.00% | Sideways |
| BNB | BNB | $684.7300 | -1.35% | Bearish |
| XRP | XRP | $1.2800 | -3.03% | Bearish |
| USDC | USDC | $0.9997 | 0.01% | Sideways |
| Solana | SOL | $79.9900 | -2.06% | Bearish |
| TRON | TRX | $0.3425 | -2.28% | Bearish |
| Figure Heloc | FIGR_HELOC | $1.0420 | 2.46% | Bullish |
| Hyperliquid | HYPE | $72.8300 | 1.58% | Bullish |

<!-- AUTO-GENERATED-SECTION:END -->
