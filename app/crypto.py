


print("CRYPTO REPORT...")

import os
import json
from dotenv import load_dotenv
import requests

from app.utils import to_usd
from app.alphavantage_service import fetch_crypto_data

load_dotenv()

symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"
fetch_crypto_data(symbol)