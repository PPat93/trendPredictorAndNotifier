"""
RSI hex:
Calculates The Relative Strength Index for a given stock ticker.
The given time intervals will be used to determine the range of calculations.
Window parameter defines how much the old data influences the new data. 
    - Scientificly: Specifies decay in terms of center of mass. 
    - The larger the window, the greater the influence of older data on newer data.
Worth using with other ratios - great with MACD.
Base calculations are given in the comment. However, the Ta-Lib library was used 
for the calculations.
"""

import talib
import yfinance as yf

# def calc_rsi(data, window=14, adjust=False):
#     delta = data["Close"].diff(1).dropna()
#     loss = delta.copy()
#     gains = delta.copy()

#     gains[gains < 0] = 0
#     loss[loss > 0] = 0

#     gain_ewm = gains.ewm(com=window - 1, adjust=adjust).mean()
#     loss_ewm = abs(loss.ewm(com=window - 1, adjust=adjust).mean())

#     RS = gain_ewm / loss_ewm
#     RSI = 100 - 100 / (1 + RS)
#     return RSI


def calc_rsi(ticker: str, start_date: str, end_date: str):
    """Retrieve specified stock data range and calculate its RSI"""

    data_res = yf.download(tickers=ticker, start=start_date, end=end_date)

    # pylint: disable=no-member
    data_res["RSI"] = talib.RSI(data_res["Close"], 14)

    return data_res["RSI"]
