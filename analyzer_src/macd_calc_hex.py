"""
MACD hex:
Calculates The Moving Average Convergence/Divergence for a given stock ticker.
Helps with identification of price trends and measurement oftrend momentum. 
Also, it shows points for buying and selling. However, it needs other factors and 
ratios cause if used alone it might generate false signals. Great with RSI.
Base calculations are given in the comment.
"""

from ema_hex import calc_ema
import matplotlib.pyplot as plt
import yfinance as yf

# MACD = 12-PeriodEMA − 26-PeriodEMA
# EMAs - 12 periods and 26 periods Exponential Moving Average


def calc_macd(ticker: str):
    """Retrieve specified stock data range and calculate its MACD"""

    ema12 = calc_ema(ticker, 12)
    # print("ema12")
    # print(ema12)
    ema26 = calc_ema(ticker, 26)
    # print("ema26")
    # print(ema26)

    data = yf.download("nvda", end="2024-06-22", start="2024-06-05")
    data["ema_long"] = data["Close"].ewm(span=26, adjust=False).mean()
    data["ema_s"] = data["Close"].ewm(span=12, adjust=False).mean()
    # Calculate MACD (the difference between 12-period EMA and 26-period EMA)
    # TODO - something is not right with macd results, to be che
    datad = data["ema_s"] - data["ema_long"] 
    macd = ema12["ema"] - ema26["ema"]
    fig, axes = plt.subplots(nrows=2, ncols=1)
    datad.plot(ax=axes[0])
    macd.plot(ax=axes[1])
    # axes.plot(data["ema_long"], label="Price", ax=axes[0,0])
    # ax.plot(ema26["ema"], label="Price")
    # ax.scatter(dates_bought, data.loc[dates_bought]['Close'], marker='^', color='green', label='Buy')
    # ax.scatter(dates_sold, data.loc[dates_sold]['Close'], marker='v', color='red', label='Sell')

    plt.show()

    return macd


print(calc_macd("nvda"))
