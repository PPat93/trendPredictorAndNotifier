"""
EMA hex:
Calculates Exponential Moving Average for a given stock ticker.
"""

from datetime import date, timedelta
import yfinance as yf

# EMA = Price(today)×k+EMA(yesterday)×(1−k); where: k=2÷(N+1), n = number of days
# the above calculation formula assumes 1 day = 1 period


def calc_ema(ticker: str, period: int):
    """Retrieve specified stock and calculate its EMA"""

    current_date = str(date.today())
    start_date = str(date.today() - timedelta(days=period))
    
    # TODO exclude holidays

    res = yf.download(ticker, start_date, current_date)

    res["EMA"] = res["Close"].ewm(span=period, adjust=False).mean()

    return res["EMA"]


print(calc_ema("nvda", 12))
