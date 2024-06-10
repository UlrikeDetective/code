import csv
from datetime import datetime
import geocoder

def get_location():
    # Get the location based on the IP address
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng, g.city, g.state, g.country
    else:
        return None, None, None, None

def record_entry():
    # Get current date and time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Get location
    latlng, city, state, country = get_location()

    # Prepare the data to be written to CSV
    data = [current_time, latlng, city, state, country]

    # Specify the CSV file name
    csv_file = 'recorded_data.csv'

    # Write data to CSV file
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        print(f"Recorded: {data}")

# Run the function to record the entry
record_entry()
