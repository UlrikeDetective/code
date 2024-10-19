# Build a GPS Tracker: Python Project for Offline Maps 🗺️🚶‍♂️

#The idea is about giving Google Maps a break .
#If you’ve ever trekked, you probably know that Google Maps doesn’t always cover those remote areas 🏞. It might even give you false, overlapping directions on flyovers (been there, done that!). So, instead of relying on Google Maps, we’ll create our own route using GPS for offline maps.
#Here’s the plan: integrate with a tool like OpenStreetMap (OSM) or any app that allows offline map usage. You can download the maps and sync them with GPS coordinates to navigate without internet. With Leaflet.js (using Python’s Folium), you can plot your trekking route on an offline OSM map.
#Not only can you see your path, but you’ll also be able to track the distance traveled. So, we’re basically building a tool to map your trek and keep a log of your journey — perfect for those off-the-grid adventures!
#Tools and Libraries:
#Folium: For basic map visualization (not offline).
#osmnx: Works with OpenStreetMap and can operate offline with pre-downloaded tiles.
#GPSd: To get real-time GPS data while trekking.
#SQLite or CSV: For lightweight local data storage.
#Full Python Project Plan for Offline Maps
#1. Download Offline Map Tiles frist you need to have offline downloaded map of that periticular region where you want to visit, you can also use Use folium or osmnx
#Use folium or osmnx to pre-download map tiles of the region you're trekking through.
#Save them to your local storage to avoid needing internet access during the trek.
#Example: Use tools like MapTiler to download tiles for use in Folium or other frameworks.

#2. GPS Logging
#Install a GPS package to track the trek route while offline.
#For desktop use, GPSd can help, while mobile apps could feed GPS data directly into your Python script.

# sudo apt install gpsd gpsd-clients

# 3. Plotting Route (Offline)
# Store GPS coordinates locally as you trek.
# Once back online, visualize the stored GPS data on the map.
# Example of saving coordinates:

import csv
from datetime import datetime
def save_gps_data(latitude, longitude):
    with open('gps_data.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), latitude, longitude])

# 4. Offline Mapping with osmnx
# osmnx allows the usage of OpenStreetMap data in Python and can be set up for offline use with pre-downloaded tiles.
# Example:

import osmnx as ox
# Load a map of a region, pre-downloaded for offline use
location = 'Kathmandu, Nepal'
G = ox.graph_from_place(location, network_type='walk', simplify=True)
# Visualize the graph locally
ox.plot_graph(G)
