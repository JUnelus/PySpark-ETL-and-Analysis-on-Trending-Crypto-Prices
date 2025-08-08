import requests
import pandas as pd
from datetime import datetime

def fetch_top_crypto():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False
    }
    r = requests.get(url, params=params)
    df = pd.DataFrame(r.json())
    df['fetched_at'] = datetime.now()
    df.to_csv('data/crypto_prices.csv', index=False)

if __name__ == "__main__":
    fetch_top_crypto()
