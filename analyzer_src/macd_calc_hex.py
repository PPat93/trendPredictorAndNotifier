"""
MACD hex:
Calculates The Moving Average Convergence/Divergence for a given stock ticker.
Helps with identification of price trends and measurement oftrend momentum. 
Also, it shows points for buying and selling. However, it needs other factors and 
ratios cause if used alone it might generate false signals. Great with RSI.
Base calculations are given in the comment. However, the Ta-Lib library was used 
for the calculations.
"""

import talib
import yfinance as yf

# MACD=12-Period EMA − 26-Period EMA

def calc_macd(ticker: str, start_date: str, end_date: str):
    """Retrieve specified stock data range and calculate its MACD"""

    data_res = yf.download(ticker, start_date, end_date)

    return data_res["MACD"]
