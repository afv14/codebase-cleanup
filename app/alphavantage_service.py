import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")


def fetch_crypto_data(symbol):
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    # url = ...
    # make a request
    # return some data
    return "TODO"


def fetch_stocks_data(symbol):
    # url = ...
    # make a request
    # return some data
    return "TODO"


def fetch_unemployment_data():
    # url = ...
    # make a request
    # return some data
    return "TODO"