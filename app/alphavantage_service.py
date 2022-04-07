import os
from dotenv import load_dotenv
import requests
import json
from app.utils import to_usd
from pandas import read_csv

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")


def fetch_crypto_data(symbol):
    """
    This function was created to fetch crypto stock data from the alpha vantage API.
    This function will return a short summary of the most recent stock price for the
    crypto currency called upon.
    This function accepts crypto ticker symbols as a string data type.
    This function will return a series of printed statements of alias data types.
    
    Example of invoking the function.
    Invoke like this: fetch_crypto_data(BTC)
    Example return value:
    "BTC
    2022-04-07
    $43,515.00"

    """
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)

    tsd = parsed_response["Time Series (Digital Currency Daily)"]

    dates = list(tsd.keys())
    latest_date = dates[0]
    latest = tsd[latest_date]


    print(symbol)
    print(latest_date)
    print(to_usd(float(latest['4a. close (USD)'])))



def fetch_stocks_data(symbol):
    """
    This function was created to provide the latest stock price information.
    This function will return a short summary of the most recent stock price for the
    ticker symbol called upon.
    This function accepts ticker symbols as a string data type.
    This function will return a series of printed statements of series data types.
    
    Example of invoking the function.
    Invoke like this: fetch_stocks_data(GOOGL)
    Example return value:
    "GOOGL
    2022-04-06
    $2,730.96"
    
    """

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"

    df = read_csv(url)

    latest = df.iloc[0]

    print(symbol)
    print(latest["timestamp"])
    print(to_usd(latest["close"]))


def fetch_unemployment_data():
    """
    This function was created to provide a time series graph of unemployment rates.
    This function will send the user to an external server that provides autogenerates a time series graph.
    This function does need to accept any parameters to provide a graph of the unemployment rates.
    This function will return a graph of unemployment rates.
    
    Example of invoking the function.
    Invoke like this: fetch_unemployment_data()
    Example return value: a time series graph of unemployment rates
    
    """

    url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)

    return parsed_response