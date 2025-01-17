#5. Load and Visualize the Trek Route
# After completing your trek, load the saved GPS data and plot it on an offline map.

import folium
import csv
def load_gps_data(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        return [(float(row[1]), float(row[2])) for row in reader]
locations = load_gps_data('gps_data.csv')
track_route(locations)
