import json
import csv
from datetime import datetime

# Load JSON data
with open('DATA.json', "r") as json_file:
    data = json.load(json_file)

# Extract relevant information and write to CSV
csv_file = 'data.csv'


with open(csv_file, "w", newline="") as csvfile:
    fieldnames = ["Timestamp", "Latitude", "Longitude", "Distance", "ActivityType"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for item in data["timelineObjects"]:
        if "activitySegment" in item:
            activity = item["activitySegment"]
            start_location = activity.get("startLocation", {})
            end_location = activity.get("endLocation", {})
            start_timestamp = activity["duration"]["startTimestamp"]
            start_timestamp = datetime.fromisoformat(start_timestamp.replace("Z", ""))
            end_timestamp = activity["duration"]["endTimestamp"]
            end_timestamp = datetime.fromisoformat(end_timestamp.replace("Z", ""))
            activity_type = activity["activityType"]

            # Check if "latitudeE7" and "longitudeE7" keys exist
            if "latitudeE7" in start_location and "longitudeE7" in start_location:
                start_latitude = start_location["latitudeE7"]
                start_longitude = start_location["longitudeE7"]
            else:
                start_latitude = None
                start_longitude = None

            if "latitudeE7" in end_location and "longitudeE7" in end_location:
                end_latitude = end_location["latitudeE7"]
                end_longitude = end_location["longitudeE7"]
            else:
                end_latitude = None
                end_longitude = None

            # Check if "distance" key exists
            if "distance" in activity:
                distance = activity["distance"]
            else:
                distance = None

            # Write start location data
            writer.writerow({
                "Timestamp": start_timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                "Latitude": start_latitude,
                "Longitude": start_longitude,
                "Distance": distance,
                "ActivityType": activity_type
            })

            # Write end location data
            writer.writerow({
                "Timestamp": end_timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                "Latitude": end_latitude,
                "Longitude": end_longitude
            })

        if "waypointPath" in item:
            waypoints = item["waypointPath"]["waypoints"]
            for waypoint in waypoints:
                waypoint_timestamp = start_timestamp + (end_timestamp - start_timestamp) * ((waypoint["latE7"] - start_location.get("latitudeE7", 0)) / (end_location.get("latitudeE7", 1) - start_location.get("latitudeE7", 0)))
                writer.writerow({
                    "Timestamp": waypoint_timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "Latitude": waypoint.get("latE7", None),
                    "Longitude": waypoint.get("lngE7", None)
                })

        if "simplifiedRawPath" in item:
            simplified_raw_path = item["simplifiedRawPath"]["points"]
            for point in simplified_raw_path:
                point_timestamp = datetime.fromisoformat(point["timestamp"].replace("Z", ""))
                writer.writerow({
                    "Timestamp": point_timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "Latitude": point.get("latE7", None),
                    "Longitude": point.get("lngE7", None)
                })

print(f"Data written to {csv_file}")
