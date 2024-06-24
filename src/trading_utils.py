import os

import pandas as pd
import pandas_ta as ta
from dotenv import load_dotenv
from pybit.unified_trading import HTTP

load_dotenv()
BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")


async def fetch_kline_data(symbol="SOLUSDT", interval="60"):
    session = HTTP(testnet=False, api_key=BYBIT_API_KEY, api_secret=BYBIT_API_SECRET)

    data = session.get_kline(
        category="inverse",
        symbol=symbol,
        interval=interval,
    )

    return data["result"]


def calculate_rsi(data, no_periods=14):
    candles = data["list"]

    df = pd.DataFrame(
        candles,
        columns=[
            "start_time_ms",
            "open_price",
            "highest_price",
            "lowest_price",
            "close_price",
            "trade_volume",
            "turnover",
        ],
    )

    if "close_price" in df.columns:
        df["close_price"] = df["close_price"].astype(float)
    else:
        raise ValueError("Column 'close_price' not found in data.")

    rsi = ta.rsi(df["close_price"], length=no_periods)
    return rsi
