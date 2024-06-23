"""
MACD hex:
Calculates The Moving Average Convergence/Divergence for a given stock ticker.
Helps with identification of price trends and measurement oftrend momentum. 
Also, it shows points for buying and selling. However, it needs other factors and 
ratios cause if used alone it might generate false signals. Great with RSI.
Base calculations are given in the comment. For now MACD is limited to the 
shorter period.
"""

from ema_hex import calc_ema

# MACD = 12-PeriodEMA − 26-PeriodEMA
# EMAs - 12 periods and 26 periods Exponential Moving Average

# TODO Add macd signal and short/long timeframe options through 
# an additional method argument


def calc_macd(ticker: str):
    """Retrieve specified stock data range and calculate its MACD"""

    ema12 = calc_ema(ticker, 12)
    ema26 = calc_ema(ticker, 26)

    # Calculate MACD (the difference between 12-period EMA and 26-period EMA)
    macd = ema12["ema"] - ema26["ema"]

    return macd
