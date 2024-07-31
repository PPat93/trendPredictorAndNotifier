import yfinance as yf
import datetime as dt
from dateutil.relativedelta import relativedelta


def get_div(ticker):
    today = dt.date.today()
    last_year = dt.date.today() - relativedelta(years=3, days=1)
    divs = yf.download(ticker, last_year, today, actions=True, interval="1mo")
    print(divs["Dividends"])


# def replace
# with open(
#     "D:\\projekty_py\\trend_predictor\\utils\\paths.csv", encoding="utf-8"
# ) as input_file, open("outfile.csv", "w", encoding="utf-8") as output_file:

#     for line in input_file:

#         line = str(line).replace("C:\\Users\\Piotrek\\Downloads\\wse stocks\\", "")
#         line = str(line).replace(".txt", "")
#         output_file.write(line)

get_div("vrg.wa")
