"""
Fibonacci Retracements hex:
Theoretical lines that helps assesing critical points on charts such
as - supports, resistances, target prices, trend reversals etc. They 
are calculated by taking two important points from the chart (e.g. 52 
weeks low and high) substracting them and dividing calculated distance 
by specified percentage ratios: 23.6%, 38.2%, 50%, 61.8%, and 100%. 
FR must be used with other TA items, as it usually works as the self-
-fulfilling prophecy. It's worth to consider little bit smaller/bigger
percentages to get ahead other traders.
"""

import yfinance as yf


# TODO get rid of trend direction argument and replace it with rsi/macd automatic calculation
def calc_fib_retr(ticker: str, start_date: str, end_date: str, trend_direction: str):
    """Calculate and return Fibonacci Retracement lines"""

    res = yf.download(tickers=ticker, start=start_date, end=end_date)

    res_highest = res["Close"].max()
    res_lowest = res["Close"].min()

    lvl_rates = [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1]
    lvl_lines = []

    dif = res_highest - res_lowest
    
    for x in lvl_rates:
        if trend_direction == "up":
            lvl_lines.append(res_highest - x * dif)
        elif trend_direction == "down": 
            lvl_lines.append(res_lowest + x * dif)
            
    return lvl_lines