"""
MACD hex:
Calculates The Moving Average Convergence/Divergence for a given stock ticker.
Helps with identification of price trends and measurement oftrend momentum. 
Also, it shows points for buying and selling. However, it needs other factors and 
ratios cause if used alone it might generate false signals. Great with RSI.
Base calculations are given in the comment.
"""

import yfinance as yf

# MACD = 12-PeriodEMA − 26-PeriodEMA
# EMAs - 12 periods and 26 periods Exponential Moving Average


def calc_macd(ticker: str, start_date: str, end_date: str, interval):
    """Retrieve specified stock data range and calculate its MACD"""

    res = yf.download(ticker, start_date, end_date, interval=interval)

    res["EMA12"] = res["Close"].ewm(span=12, adjust=False).mean()
    res["EMA26"] = res["Close"].ewm(span=26, adjust=False).mean()

    # Calculate MACD (the difference between 12-period EMA and 26-period EMA)
    res["MACD"] = res["EMA12"] - res["EMA26"]

    return res["MACD"]
