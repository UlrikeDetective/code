# app.py
from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime
import sqlite3
import json

def fetch_daily_trends():
    pytrends = TrendReq()
    today = datetime.today().date()

    conn = sqlite3.connect("trends.db")
    cursor = conn.cursor()

    # Check if today’s trends are already in the database
    cursor.execute("SELECT * FROM daily_trends WHERE date = ?", (today,))
    if cursor.fetchone():
        conn.close()
        return False  # Return False if data for today already exists

    # Fetch and process trending data (as in the original code)
    trending_data = pytrends.trending_searches(pn='united_states')
    trending_data.columns = ["trend_name"]

    for index, row in trending_data.iterrows():
        trend_name = row["trend_name"]
        pytrends.build_payload([trend_name])
        interest_over_time_df = pytrends.interest_over_time()
        if not interest_over_time_df.empty:
            interest_values = interest_over_time_df[trend_name].tolist()
            interest_json = json.dumps(interest_values)
            avg_search_interest = sum(interest_values) / len(interest_values)
            cursor.execute(
                '''INSERT INTO daily_trends (date, trend_name, searches, source, interest_over_time) 
                VALUES (?, ?, ?, ?, ?)''',
                (today, trend_name, avg_search_interest, "Google Trends", interest_json)
            )
    
    conn.commit()
    conn.close()
    return True  # Return True if data was fetched and inserted
 