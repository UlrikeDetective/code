# Stock data

import yfinance as yf

STK = input("Enter share name: ")

try:
    data = yf.Ticker(STK).history(period="1d")
    if data.empty:
        raise ValueError("No data retrieved. Please check the stock symbol or try again later.")
    
    last_market_price = data['Close'].iloc[-1]
    print("Last market price:", last_market_price)
except ValueError as e:
    print(e)
except IndexError:
    print("The data retrieved does not contain enough information.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
