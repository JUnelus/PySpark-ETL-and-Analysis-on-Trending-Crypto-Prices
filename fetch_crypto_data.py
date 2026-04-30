from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import pandas as pd
import requests


API_URL = "https://api.coingecko.com/api/v3/coins/markets"
DATA_DIR = Path("data")
LATEST_PATH = DATA_DIR / "crypto_prices.csv"
HISTORY_PATH = DATA_DIR / "crypto_prices_history.csv"


def _request_with_retries(url: str, params: dict, retries: int = 3, timeout: int = 30) -> list[dict]:
    last_error: Exception | None = None
    for _ in range(retries):
        try:
            response = requests.get(url, params=params, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as exc:
            last_error = exc
    raise RuntimeError(f"Could not fetch data from CoinGecko after {retries} attempts") from last_error


def _safe_columns(df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
    present = [column for column in columns if column in df.columns]
    return df[present].copy()


def fetch_top_crypto(vs_currency: str = "usd", per_page: int = 15) -> pd.DataFrame:
    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": per_page,
        "page": 1,
        "sparkline": False,
    }
    payload = _request_with_retries(API_URL, params)
    if not isinstance(payload, list) or not payload:
        raise RuntimeError("CoinGecko returned an empty payload")

    now_utc = datetime.now(timezone.utc)
    df = pd.DataFrame(payload)
    df = _safe_columns(
        df,
        [
            "id",
            "symbol",
            "name",
            "current_price",
            "market_cap",
            "market_cap_rank",
            "total_volume",
            "high_24h",
            "low_24h",
            "price_change_percentage_24h",
            "last_updated",
        ],
    )

    df["fetched_at"] = now_utc.isoformat()
    df["snapshot_date"] = now_utc.date().isoformat()
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.sort_values("market_cap_rank", inplace=True)
    df.to_csv(LATEST_PATH, index=False)

    if HISTORY_PATH.exists():
        history_df = pd.read_csv(HISTORY_PATH)
        history_df = history_df[history_df["snapshot_date"] != now_utc.date().isoformat()]
        history_df = pd.concat([history_df, df], ignore_index=True)
    else:
        history_df = df.copy()

    history_df.sort_values(["snapshot_date", "market_cap_rank"], inplace=True)
    history_df.to_csv(HISTORY_PATH, index=False)
    return df


if __name__ == "__main__":
    fetch_top_crypto()
