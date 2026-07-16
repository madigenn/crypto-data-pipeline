import requests
import pandas as pd
from datetime import datetime

def fetch_crypto_data():
    """Scarica dati di mercato delle top 50 criptovalute da CoinGecko"""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "eur",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params)
    response.raise_for_status()  # solleva errore se la richiesta fallisce

    data = response.json()
    df = pd.DataFrame(data)

    return df
def save_raw_data(df):
    """Salva i dati grezzi in formato CSV con timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"../data/raw_crypto_data_{timestamp}.csv"
    df.to_csv(filename, index=False)
    print(f"✅ Dati salvati in: {filename}")
    print(f"📊 Righe: {len(df)} | Colonne: {len(df.columns)}")

if __name__ == "__main__":
    print("🔄 Scaricamento dati da CoinGecko...")
    df = fetch_crypto_data()
    save_raw_data(df)
    print("✅ Completato!")
