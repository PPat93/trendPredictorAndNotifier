"""
EMA hex:
Calculates Exponential Moving Average for a given stock ticker.
"""

from datetime import date, timedelta
import yfinance as yf
import math
import pandas as pd

# EMA = Price(today)×k+EMA(yesterday)×(1−k); where: k=2÷(N+1), n = number of days
# the above calculation formula assumes 1 day = 1 period


def calc_ema(ticker: str, period: int):
    """Retrieve specified stock and calculate its EMA"""

    current_date = str(date.today())

    # Exclude weekends and potential holidays
    # "period" - period itself; "period/7*2" - number of average weekend days per each week
    # retrieved; "+2" - two more days in case that data is retrieved on Sunday;
    # "potential_public_holidays" - in case there are multiple holidays/free days/no trading
    # during longer periods retrieved;
    if period > 150:
        potential_public_holidays = 200
    elif period < 7:
        potential_public_holidays = 5
    else:
        potential_public_holidays = 50

    period_retrieved = (
        period + math.ceil(period / 7 * 2) + 2 + potential_public_holidays
    )
    print("per ret " + str(period_retrieved))
    start_date = str(date.today() - timedelta(days=period_retrieved))
    # start_date = str(date.today() - timedelta(days=period))
    res = yf.download(ticker, start=start_date, end=current_date)
    print("dates: " + start_date + " end " + current_date)
    print("pre")
    print(res)
    print(period)
    res2 = res.tail(period)
    print("post")
    print(res2)

    res["EMA"] = res["Close"].ewm(span=period, adjust=False).mean()

    return res["EMA"]


calc_ema("nvda", 500)
