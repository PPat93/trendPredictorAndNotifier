"""
Analyzer comb:
Sends/Receives data from Integrator Comb: <-> Database, <- API Data Retriever, ->Mailer;
Compares received stock price with previously stored reference price/time data;
Saves compared data as a new reference if expected;
Remove old reference data if expected;
"""

import calc_hex.rsi_hex as rsi
import calc_hex.macd_hex as macd
import calc_hex.ema_hex as ema
import calc_hex.fibonacci_retracements_hex as fibs
from . import api_retriever_cmb as retriever


def run_trend_analysis(
    ticker: str,
    start_date: str,
    end_date: str,
    timeframe: str,
    period: int,
    trend_direction: str,
):

    ema_new = ema.EMA(ticker, period)
    fibonacci_new = fibs.FibonacciRetrace(ticker, start_date, end_date, trend_direction)
    rsi_new = rsi.RSI(ticker, start_date, end_date)
    macd_new = macd.MACD(ticker, timeframe)

    latest_price = float((retriever.retrieve_last_stock_price(ticker))[0].get("last"))

    calculated_rsi = rsi_new.calc_rsi()
    calculated_fibonacci = fibonacci_new.calc_fib_retr()
    calculated_ema = ema_new.calc_ema()
    calculated_macd = macd_new.calc_macd()

    trend_is_reversed = (
        False  # TODO bool returned with a value if the trend was reversed
    )

    return trend_is_reversed
