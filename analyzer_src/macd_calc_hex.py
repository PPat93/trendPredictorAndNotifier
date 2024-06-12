"""
MACD hex:
Calculates The Moving Average Convergence/Divergence for a given stock ticker.

"""

import talib
import yfinance as yf


def calc_macd(ticker: str, start_date: str, end_date: str):
    """Retrieve specified stock data range and calculate its MACD"""

    data_res = yf.download(ticker, start_date, end_date)

    return data_res["MACD"]
