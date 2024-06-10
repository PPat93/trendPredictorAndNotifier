"""
Analyzer comb:
Sends/Receives data from Integrator Comb: <-> Database, <- API Data Retriever, ->Mailer;
Compares received stock price with previously stored reference price/time data;
Saves compared data as a new reference if expected;
Remove old reference data if expected;
"""

from api_retriever_cmb import retrieve_last_stock_price
import talib
import yfinance as yf
import matplotlib.pyplot as plt


def run_trend_analysis(ticker: str):

    latest_price = float((retrieve_last_stock_price(ticker))[0].get("last"))

    trend_is_reversed = (
        False  # TODO bool returned with a value if the trend was reversed
    )
    return trend_is_reversed


microsoft = yf.Ticker("NVDA")
dict = microsoft.info
dataRes = yf.download("NVDA", start="2024-06-04", end="2024-06-07", interval="5m")


def RSI(data, window=14, adjust=False):
    delta = data["Close"].diff(1).dropna()
    loss = delta.copy()
    gains = delta.copy()

    gains[gains < 0] = 0
    loss[loss > 0] = 0

    gain_ewm = gains.ewm(com=window - 1, adjust=adjust).mean()
    loss_ewm = abs(loss.ewm(com=window - 1, adjust=adjust).mean())

    RS = gain_ewm / loss_ewm
    RSI = 100 - 100 / (1 + RS)
    return RSI


# RSI(dataRes)
reversed_df = dataRes.iloc[::-1]

# pylint: disable=no-member
dataRes["RSI"] = talib.RSI(reversed_df["Close"], 14)

ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=4, colspan=1)
ax2 = plt.subplot2grid((10, 1), (5, 0), rowspan=4, colspan=1)
ax1.plot(dataRes["Close"], linewidth=2.5)
ax1.set_title("Nvidia usd")
ax2.plot(dataRes["RSI"], color="red", linewidth=1.5)
ax2.axhline(30, linestyle="--", linewidth=1.5, color="grey")
ax2.axhline(70, linestyle="--", linewidth=1.5, color="grey")
ax2.set_title("Nvidia RSI")

plt.show()
