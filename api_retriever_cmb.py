"""
API data retriever comb:
Sends data to Integrator -> Analyzer;
Sends API request to retrieve needed values;
Receives response with retrieved values;
Extract values from the response and deletes everything that is not needed;
"""

import os
import requests

API_KEY = os.environ.get("predictorRetrieverApiKey")

# TODO - to be expanded and refactoredto be able to retrieve different metrics and symbols with various settings
def retrieve_data(stock_ticker):
    """Retrieve stock data example"""
    api_uri= f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_ticker}&interval=5min&apikey={API_KEY}&outputsize=compact"
    res = requests.get(api_uri, timeout=10)
    retrieved_data = res.content
    print(f"Status: {res.status_code}, Res: {retrieved_data}")
    return res
