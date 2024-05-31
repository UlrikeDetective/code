# Stock data

import yfinance as yf

STK = input("Enter share name: ")

data = yf.Ticker(STK).history(period="Id")

last_market_price = data['Close'].iloc[-1]

print("Last market price:", last_market_price)
