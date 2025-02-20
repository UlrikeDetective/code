from flask import Flask, render_template_string, jsonify
import sqlite3
import warnings
import json
from datetime import datetime, timedelta
from time import sleep
from pytrends.request import TrendReq

warnings.filterwarnings("ignore", category=FutureWarning)

app = Flask(__name__)

# Function to fetch daily Google trends
def fetch_daily_trends():
    try:
        pytrends = TrendReq(hl="en-US", tz=360)
        pytrends.build_payload(kw_list=["example keyword"])  # Replace with desired keywords
        daily_trends = pytrends.trending_searches(pn="united_states")  # Replace with desired region "united_states"
        
        # Debugging information
        print("Fetched daily trends:", daily_trends.head())

        # Save to SQLite
        conn = sqlite3.connect("trendsUSA.db")
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS daily_trends (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                trend_name TEXT,
                searches INTEGER,
                interest_over_time TEXT
            )
        """)

        # Insert data into the database
        for trend in daily_trends.values.tolist():
            cursor.execute("""
                INSERT INTO daily_trends (date, trend_name, searches, interest_over_time)
                VALUES (?, ?, ?, ?)
            """, (datetime.now().strftime("%Y-%m-%d"), trend[0], 0, json.dumps([0] * 30)))  # Dummy data for `interest_over_time`

        conn.commit()
        conn.close()

        sleep(60)  # Respect API rate limits
        return True
    except Exception as e:
        print(f"Error occurred while fetching trends: {e}")
        return False


@app.route("/")
def index():
    # Fetch data from the SQLite database
    conn = sqlite3.connect("trends.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, trend_name, searches, interest_over_time FROM daily_trends ORDER BY date DESC LIMIT 10")
    trends = cursor.fetchall()
    conn.close()

    # HTML Template
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Google Trends</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div class="container mt-5">
        <h2 class="text-center">Daily Google Trends</h2>
        <button id="getTrends" class="btn btn-primary mb-4">Get Daily Trends</button>
        <div class="alert alert-success d-none" id="successMessage">Data imported successfully!</div>
        <div class="alert alert-info d-none" id="alreadyFetchedMessage">Today's trends have already been fetched.</div>
        <div class="alert alert-info d-none" id="loadingMessage">Fetching data, please wait...</div>
        <table class="table">
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Trend</th>
                    <th>Avg Interest</th>
                    <th>Interest Over Time</th>
                </tr>
            </thead>
            <tbody>
                {% for trend in trends %}
                    <tr>
                        <td>{{ trend[1] }}</td> <!-- Date -->
                        <td>{{ trend[2] }}</td> <!-- Trend Name -->
                        <td>{{ trend[3] }}</td> <!-- Average Searches -->
                        <td>
                            <canvas id="chart{{ trend[0] }}" style="width: 100%; height: 150px;"></canvas>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>

    <script>
        const trends = {{ trends | tojson }};
        trends.forEach(trend => {
            const ctx = document.getElementById(`chart${trend[0]}`).getContext('2d');
            const interestData = JSON.parse(trend[4]);

            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: Array.from({length: interestData.length}, (_, i) => `Day ${i + 1}`),
                    datasets: [{
                        label: trend[2],
                        data: interestData,
                        fill: false,
                        borderColor: 'green',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        x: { title: { display: true, text: "Date" } },
                        y: { title: { display: true, text: "Interest" }, beginAtZero: true }
                    }
                }
            });
        });

        document.getElementById("getTrends").onclick = function() {
            document.getElementById("loadingMessage").classList.remove("d-none");
            fetch("/fetch_trends").then(response => response.json()).then(data => {
                document.getElementById("loadingMessage").classList.add("d-none");
                if (data.success) {
                    location.reload();
                } else {
                    console.error("Error fetching trends:", data.error);
                }
            });
        };
    </script>
</body>
</html>
    """

    return render_template_string(html, trends=trends)


@app.route("/fetch_trends")
def fetch_trends():
    try:
        data_fetched = fetch_daily_trends()
        return jsonify(success=True, already_fetched=not data_fetched)
    except Exception as e:
        return jsonify(success=False, error=str(e))


if __name__ == "__main__":
    app.run(debug=True)
