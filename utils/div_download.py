import datetime as dt
import yfinance as yf
from dateutil.relativedelta import relativedelta

# Dividend analysis funcionality - development ON HOLD
# Reason - unfavorable dividends taxation laws,
# not profitable enough in comparison with investing in ordinary stocks
# not worth wasting time (at least - for now)


def get_div(ticker, timeframe, interval):
    """Retrieve dividends values for specified 'ticker', during last 'timeframe' returned by each 'interval'"""
    today = dt.date.today()
    last_year = dt.date.today() - relativedelta(years=timeframe)
    res = yf.download(ticker, last_year, today, actions=True, interval=interval)
    divs = res["Dividends"]
    print(divs)


# No sure what I was about to do here - probably wanted to extract data from
# file, line by line - each line with a single ticker, append exchange symbol
# to each ticker and retrieve dividends for each stock. Not finished, because
# of the reason explained eariler.
with open(
    "D:\\projekty_py\\trend_predictor\\utils\\tickerTest.csv", encoding="utf-8"
) as input_file:

    for line in input_file:
        full_ticker = f"{line.strip()}.wa"
        print(full_ticker)

get_div("CMA", 3, "3mo")
