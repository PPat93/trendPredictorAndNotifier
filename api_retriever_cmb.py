"""
API data retriever comb:
Sends data to Integrator -> Analyzer;
Sends API request to retrieve needed values;
Receives response with retrieved values;
Extract values from the response and deletes everything that is not needed;1
"""

# TODO - to be expanded and refactoredto be able to retrieve different metrics and symbols with various settings

import os
import requests

FUNDAMENTAL_API_KEY = os.environ.get("fundamentalRetrieverApiKey")
PRICE_API_KEY = os.environ.get("realtimeRetrieverApiKey")
HEADERS = {"Content-Type": "application/json"}


# shared with crypto price - max 50 reqs/hour, 1000 reqs/day
def retrieve_last_stock_price(stock_ticker):
    """Retrieve latest stock price"""
    price_api_uri = f"https://api.tiingo.com/iex/{stock_ticker}?token={PRICE_API_KEY}"

    price_res = requests.get(price_api_uri, headers=HEADERS, timeout=10)
    price_json = price_res.json()

    return price_json


# max 25 reqs/day
def retrieve_stock_fundamental_data(stock_ticker):
    """Retrieve fundamental data for the specified stock"""
    fundamental_api_uri = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={stock_ticker}&apikey={FUNDAMENTAL_API_KEY}"

    fundamental_res = requests.get(fundamental_api_uri, headers=HEADERS, timeout=10)
    fundamental_json = fundamental_res.json()

    return fundamental_json


# shared with stock price - max 50 reqs/hour, 1000 reqs/day
def retrieve_last_crypto_price(crypto_ticker):
    """Retrieve latest crypto price"""
    crypto_api_uri = f"https://api.tiingo.com/tiingo/crypto/top?tickers={crypto_ticker}&token={PRICE_API_KEY}"

    crypto_res = requests.get(crypto_api_uri, headers=HEADERS, timeout=10)
    crypto_json = crypto_res.json()

    return crypto_json
