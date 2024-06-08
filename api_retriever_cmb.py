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

def retrieve_last_price(stock_ticker):
    """Retrieve stock data example"""
    price_api_uri = f"https://api.tiingo.com/iex/{stock_ticker}?token={PRICE_API_KEY}"
    headers = {"Content-Type": "application/json"}

    price_res = requests.get(price_api_uri, headers=headers, timeout=10)
    latest_price_json = float((price_res.json())[0].get("last"))

    print(f" yo {latest_price_json}")
    return latest_price_json
