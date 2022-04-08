

print("STOCKS REPORT...")

from app.alphavantage_service import fetch_stocks_data

symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"
fetch_stocks_data(symbol)