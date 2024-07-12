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
from . import api_retriever_cmb as retriever


def run_trend_analysis(ticker: str, start_date: str, end_date: str, timeframe: str):

    latest_price = float((retriever.retrieve_last_stock_price(ticker))[0].get("last"))

    calculated_rsi = rsi.calc_rsi(ticker, start_date, end_date)
    calculated_macd = macd.calc_macd(ticker, timeframe)

    trend_is_reversed = (
        False  # TODO bool returned with a value if the trend was reversed
    )
    return trend_is_reversed
