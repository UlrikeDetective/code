import json
import csv

# Load JSON data
with open('data.json') as f:
    data = json.load(f)

# Define CSV file name
csv_file = 'data.csv'

# Open CSV file in write mode
with open(csv_file, 'w', newline='') as csvfile:
    # Define fieldnames for CSV header
    fieldnames = ['trip_id', 'source_latitude', 'source_longitude', 'destination_latitude', 'destination_longitude', 'travel_mode', 'destination']
    
    # Create CSV writer object
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write CSV header
    writer.writeheader()
    
    # Iterate over trips
    for trip in data['trips']:
        trip_id = trip['id']
        source_lat = trip['place_visit'][0]['place']['lat_lng']['latitude']
        source_lng = trip['place_visit'][0]['place']['lat_lng']['longitude']
        destination_lat = trip['place_visit'][1]['place']['lat_lng']['latitude']
        destination_lng = trip['place_visit'][1]['place']['lat_lng']['longitude']
        travel_mode = trip['transition'][0]['route']['travel_mode']
        destination = trip['transition'][0]['route']['transit']['route']['leg'][-2]['destination']  # Assuming destination is always the second last leg
        
        # Write trip data to CSV
        writer.writerow({
            'trip_id': trip_id,
            'source_latitude': source_lat,
            'source_longitude': source_lng,
            'destination_latitude': destination_lat,
            'destination_longitude': destination_lng,
            'travel_mode': travel_mode,
            'destination': destination
        })

print("CSV file generated successfully!")
