import streamlit as st
import yfinance as yf
import pandas as pd
import datetime as dt

# Function to get stock data
def get_stock_data(ticker):
    end_date = dt.datetime.today().date()
    start_date = end_date - dt.timedelta(days=365)
    stock_data = yf.Ticker(ticker).history(start=start_date, end=end_date)
    return stock_data

# Function to calculate moving averages
def add_moving_averages(data):
    data['20 Day MA'] = data['Close'].rolling(window=20).mean()
    data['50 Day MA'] = data['Close'].rolling(window=50).mean()
    return data

# Streamlit app
st.title("Visualizing Stock Data")

# Input for stock symbol
ticker = st.text_input("Enter stock symbol:", value="NVDA")

# Get stock data
stock_data = get_stock_data(ticker)
stock_data = add_moving_averages(stock_data)

# Get company information
stock_info = yf.Ticker(ticker).info
company_name = stock_info.get('longName', 'N/A')
current_price = stock_info.get('currentPrice', 'N/A')

# Display company name and current price
st.markdown(f"**{company_name}**")
st.markdown(f"**Current Price: {current_price}**")

# Chart for closing prices
st.subheader("Closing Prices over the Past Year")
st.line_chart(stock_data['Close'])

# Chart for volume
st.subheader("Volume of Trades over the Past Year")
st.line_chart(stock_data['Volume'])

# Chart for closing price and moving averages
st.subheader("Closing Price and Moving Averages")
st.line_chart(stock_data[['Close', '20 Day MA', '50 Day MA']])
