"""
API data retriever comb:
Sends data to Integrator -> Analyzer;
Sends API request to retrieve needed values;
Receives response with retrieved values;
Extract values from the response and deletes everything that is not needed;
"""

import os
import requests

api_key = os.environ.get("OPENAI_API_KEY")

api_uri = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&\
            interval=5min&apikey={api_key}&outputsize=compact"

r = requests.get(api_uri, timeout=10)

# print(f"Status: {r.status_code}, Res: {r.content}")
