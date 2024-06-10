import csv
from datetime import datetime
from geopy.geocoders import Nominatim

def get_location():
    # Create a geolocator object
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Use your preferred method to get the coordinates (latitude and longitude)
    # Here, we'll just use an example set of coordinates
    # For example, you could use an IP address to location service to get the actual location
    latitude = 40.7128
    longitude = -74.0060

    # Get the location information
    location = geolocator.reverse((latitude, longitude), language='en')
    return location.address

def record_entry():
    # Get current date and time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Get location
    location = get_location()

    # Prepare the data to be written to CSV
    data = [current_time, location]

    # Specify the CSV file name
    csv_file = 'recorded_data.csv'

    # Write data to CSV file
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        print(f"Recorded: {data}")

# Run the function to record the entry
record_entry()
