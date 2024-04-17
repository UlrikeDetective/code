import csv
from datetime import datetime
import os

file_exists = os.path.isfile('daily_activities_living_healthy.csv')

print("Thank you for showing up today!")

activities = []  # List to store activity details
activity_id_counter = 1  # Initialize the activity ID counter
total_activities = 0  # Initialize the total number of activities done

while True:
    name = input("Any activities for the habit tracker - Living Healthy, today? (Enter 'quit' to stop): ")
    if name.lower() == 'quit':
        break
    
    # Activity inputs and validation
    activities_input = [
        ("Yoga", "Any Yoga today? Y or N? "),
        ("Meditate", "Any Meditation today? Y or N? "),
        ("Kayak", "Any Kayak today? Y or N? "),
        ("Bouldern", "Any Bouldering today? Y or N? "),
        ("6k Steps", "Did you achieve 6k steps today? Y or N? "),
        ("Bike ride", "Any Bike ride today? Y or N? "),
        ("other sports", "Any other sport activities today? Y or N? "),
        ("Reading", "Did you do any Reading today? Y or N? "),
        ("Audiobook", "Did you listen to any Audiobooks today? Y or N? "),
        ("Eat Fruit", "Did you eat Fruit today? Y or N? "),
        ("Eat Vegetables", "Did you eat Vegetables today? Y or N? "),
        ("2L water/tea", "Did you drink 2L of water/tea today? Y or N? ")
    ]

    activity_data = {}
    for activity, prompt in activities_input:
        answer = input(prompt)
        while answer.upper() not in {'Y', 'N'}:
            print("Invalid input. Please enter Y or N.")
            answer = input(prompt)
        activity_data[activity] = answer.upper()

    # Generate an ID if at least one activity is marked as 'Y'
    activity_id = f"LivingHealthy{activity_id_counter:03}" if any(a.upper() == 'Y' for a in activity_data.values()) else None

    # Calculate the total tracker
    total_tracker = sum(1 for value in activity_data.values() if value == 'Y')
    
    # Increment the total number of activities done
    total_activities += total_tracker

    # Print the total habit tracker of the day
    print("Your daily activity tracker is:")
    print(f"Daily activity tracker: {total_tracker}")
    print()

    # Store the activity details in the activities list
    activity_data.update({
        'activity_id': activity_id,
        'daily_total': total_tracker,
        'date': datetime.now().strftime("%Y-%m-%d")  # Current date in YYYY-MM-DD format
    })
    activities.append(activity_data)

    # Increment the activity ID counter
    activity_id_counter += 1

# Append the activities to the CSV file if it exists, otherwise create a new file
if activities:  # Only proceed if there are activities to write
    with open('daily_activities_living_healthy.csv', mode='a', newline='') as file:
        fieldnames = ['activity_id', 'Yoga', 'Meditate', 'Kayak', 'Bouldern', '6k Steps', 'Bike ride', 'other sports', 'Reading', 'Audiobook', 'Eat Fruit', 'Eat Vegetables', '2L water/tea', 'daily_total', 'date']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()  # Write header only if the file is newly created
        writer.writerows(activities)

# Determine the message based on the total number of activities done
if total_activities == 0:
    print("Are you alive?")
elif 1 <= total_activities <= 3:
    print("Hard day at work?")
elif 4 <= total_activities <= 6:
    print("Not bad")
elif 7 <= total_activities <= 10:
    print("Excellent")
else:
    print("Olympic gold medal ;.)")

