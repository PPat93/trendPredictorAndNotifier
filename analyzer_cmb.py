"""
Analyzer comb:
Sends/Receives data from Integrator Comb: <-> Database, <- API Data Retriever, ->Mailer;
Compares received stock price with previously stored reference price/time data;
Saves compared data as a new reference if expected;
Remove old reference data if expected;
"""

from api_retriever_cmb import retrieve_last_stock_price
from  trendPredictor.analyzer_src.rsi_calc_hex import calc_rsi

def run_trend_analysis(ticker: str, start_date: str, end_date: str):

    latest_price = float((retrieve_last_stock_price(ticker))[0].get("last"))
    
    calculated_rsi = calc_rsi(ticker, start_date, end_date)
    calculated_macd = calc_macd(ticker, start_date, end_date)

    trend_is_reversed = (
        False  # TODO bool returned with a value if the trend was reversed
    )
    return trend_is_reversed