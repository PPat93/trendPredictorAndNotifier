"""
EMA hex:
Calculates Exponential Moving Average for a given stock ticker.
"""

import yfinance as yf

# EMA = Price(today)×k+EMA(yesterday)×(1−k); where: k=2÷(N+1), n = number of days
# the above calculation formula assumes 1 day = 1 period


def calc_ema(ticker: str, period: int):
    """Retrieve specified stock and calculate its EMA"""

    # todo attach dates to automatically calculate expected period for retrieval - starting from current day"
    # something like: startd_date = {today}, end_date = {today - period}
    res = yf.download(ticker, interval="1d")
    
    res["EMA"] = res["Close"].ewm(span=period, adjust=False).mean()

    return res["EMA"]

calc_ema("nvda", 12)
