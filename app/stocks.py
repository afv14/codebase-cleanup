

print("STOCKS REPORT...")


from app.alphavantage_service import fetch_stocks_data

symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"
fetch_stocks_data(symbol)
=======
import os
from dotenv import load_dotenv
from pandas import read_csv

from app.utils import to_usd
from app.alphavantage_service import fetch_stocks_data

load_dotenv()

symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"
fetch_stocks_data(symbol)

