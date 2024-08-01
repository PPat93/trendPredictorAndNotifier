import yfinance as yf
import datetime as dt
from dateutil.relativedelta import relativedelta


def get_div(ticker):
    today = dt.date.today()
    last_year = dt.date.today() - relativedelta(years=3, days=1)
    res = yf.download(ticker, last_year, today, actions=True, interval="1mo")
    divs = res["Dividends"]
    print(ticker + "  " + str(divs.iloc[0]))


with open(
    "D:\\projekty_py\\trend_predictor\\utils\\tickerTest.csv", encoding="utf-8"
) as input_file:

    for line in input_file:
        full_ticker = f"{line.strip()}.wa"
        print(full_ticker)
        get_div(full_ticker)
