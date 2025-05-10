import sqlite3
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect("trends.db")
cursor = conn.cursor()

# Create a table for daily trends
cursor.execute('''CREATE TABLE IF NOT EXISTS daily_trends (
    id INTEGER PRIMARY KEY,
    date DATE,
    trend_name TEXT,
    searches INTEGER,
    source TEXT,
    interest_over_time TEXT
)''')

conn.commit()
conn.close()