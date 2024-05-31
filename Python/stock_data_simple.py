# Stock data

# code not working yet. bug

import yfinance as yf

STK = input("Enter share name: ")

try:
    # Fetch the last day's worth of minute data
    data = yf.Ticker(STK).history(period="3mo", interval="1m")
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
