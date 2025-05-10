# Stock trends

from pytrends.request import TrendReq
import matplotlib.pyplot as plt

# Function to get Google Trends data
def get_google_trends_data(keywords, timeframe='today 3-m', geo='US'):
    pytrends = TrendReq(hl='en-US', tz=360)

    # Build the payload
    pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo=geo, gprop='')

    # Get interest over time
    interest_over_time_df = pytrends.interest_over_time()

    return interest_over_time_df

# Example keywords related to your article
STOCKS = ["AMZN", "MSFT", "META", "AAPL", "GOOG"]

# Fetch Google Trends data
trends_data = get_google_trends_data(STOCKS)

# Plot the data
plt.figure(figsize=(20, 12))
trends_data.plot(title='Trends for STOCKS')
plt.xlabel('Date')
plt.ylabel('Interest Over Time')
plt.show()
