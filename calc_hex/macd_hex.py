"""
MACD hex:
Calculates The Moving Average Convergence/Divergence for a given stock ticker.
Helps with identification of price trends and measurement oftrend momentum. 
Also, it shows points for buying and selling. However, it needs other factors and 
ratios cause if used alone it might generate false signals. Great with RSI.
Base calculations are given in the comment. For now MACD is limited to the 
shorter period.
"""

import numpy as np
from . import ema_hex as ema

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
        
    local_ema_l = ema.EMA(ticker, period_l)   
    local_ema_s = ema.EMA(ticker, period_l)   

    ema_s = local_ema_l.calc_ema()
    ema_l = local_ema_l.calc_ema()

    # Calculate MACD (the difference between shorter-period EMA and longer-period EMA)
    macd = ema_s["ema"] - ema_l["ema"]
    signal = macd.ewm(span=s_line, adjust=False).mean()

    return macd, signal


def trade_signals(ticker: str, timeframe: str):
    """Return buy/sell points on the basis of MACD and it's signal line"""

    macd, signal = calc_macd(ticker, timeframe)

    signals = np.where(macd > signal, 1, -1)
    signals = np.where(macd.isnull(), 0, signals)


macd, horizontal = calc_macd("NVDA", "long")
