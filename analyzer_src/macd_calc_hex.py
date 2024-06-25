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


def calc_macd(ticker: str, timeframe: str):
    """Retrieve specified stock data range and calculate its MACD"""

    if timeframe == "short":
        period_s = 12
        period_l = 26
        s_line = 9
    elif timeframe == "long":
        period_s = 24
        period_l = 52
        s_line = 18

    ema_s = calc_ema(ticker, period_s)
    ema_l = calc_ema(ticker, period_l)

    # Calculate MACD (the difference between shorter-period EMA and longer-period EMA)
    macd = ema_s["ema"] - ema_l["ema"]
    signal = macd.ewm(span=s_line, adjust=False).mean()

    return macd, signal
