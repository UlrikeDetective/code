import csv
from datetime import datetime
import os

file_exists = os.path.isfile('daily_activities_datascience.csv')

print("Thank you for showing up today!")

activities = []  # List to store activity details
activity_id_counter = 1  # Initialize the activity ID counter

while True:
    name = input("Any activities for the habit tracker - DataScience, today? (Enter 'quit' to stop): ")
    if name.lower() == 'quit':
        break
    
    R_activity = input("Any R today? Y or N? ")
    while R_activity.upper() not in {'Y', 'N'}:
        print("Invalid input. Please enter Y or N.")
        R_activity = input("Any R today? Y or N? ")
    
    SQL_activity = input("Any SQL today? Y or N? ")
    while SQL_activity.upper() not in {'Y', 'N'}:
        print("Invalid input. Please enter Y or N.")
        SQL_activity = input("Any SQL today? Y or N? ")
    
    Python_activity = input("Any Python today? Y or N? ")
    while Python_activity.upper() not in {'Y', 'N'}:
        print("Invalid input. Please enter Y or N.")
        Python_activity = input("Any Python today? Y or N? ")
    
    Github_activity = input("Any Github today? Y or N? ")
    while Github_activity.upper() not in {'Y', 'N'}:
        print("Invalid input. Please enter Y or N.")
        Github_activity = input("Any Github today? Y or N? ")
    
    Kaggle_activity = input("Any Kaggle today? Y or N? ")
    while Kaggle_activity.upper() not in {'Y', 'N'}:
        print("Invalid input. Please enter Y or N.")
        Kaggle_activity = input("Any Kaggle today? Y or N? ")
    
    Terminal_activity = input("Any Terminal today? Y or N? ")
    while Terminal_activity.upper() not in {'Y', 'N'}:
        print("Invalid input. Please enter Y or N.")
        Terminal_activity = input("Any Terminal today? Y or N? ")
    
    Excel_activity = input("Any Excel today? Y or N? ")
    while Excel_activity.upper() not in {'Y', 'N'}:
        print("Invalid input. Please enter Y or N.")
        Excel_activity = input("Any Excel today? Y or N? ")
    
    Tech_reading_activity = input("Any Tech Reading today? Y or N? ")
    while Tech_reading_activity.upper() not in {'Y', 'N'}:
        print("Invalid input. Please enter Y or N.")
        Tech_reading_activity = input("Any Tech Reading today? Y or N? ")
    
    Learning_activity = input("Any Learning today? Y or N? ")
    while Learning_activity.upper() not in {'Y', 'N'}:
        print("Invalid input. Please enter Y or N.")
        Learning_activity = input("Any Learning today? Y or N? ")
    
    Data_analytics_activity = input("Any Data Analytics today? Y or N? ")
    while Data_analytics_activity.upper() not in {'Y', 'N'}:
        print("Invalid input. Please enter Y or N.")
        Data_analytics_activity = input("Any Data Analytics today? Y or N? ")
    
    Tech_listings_activity = input("Any Tech Listings today? Y or N? ")
    while Tech_listings_activity.upper() not in {'Y', 'N'}:
        print("Invalid input. Please enter Y or N.")
        Tech_listings_activity = input("Any Tech Listings today? Y or N? ")
    
    Projects_activity = input("Any Projects today? Y or N? ")
    while Projects_activity.upper() not in {'Y', 'N'}:
        print("Invalid input. Please enter Y or N.")
        Projects_activity = input("Any Projects today? Y or N? ")
    
    # Generate an ID if at least one activity is marked as 'Y'
    activity_id = f"DataScience{activity_id_counter:03}" if any(a.upper() == 'Y' for a in [R_activity, SQL_activity, Python_activity, Github_activity, Kaggle_activity, Terminal_activity, Excel_activity, Tech_reading_activity, Learning_activity, Data_analytics_activity, Tech_listings_activity, Projects_activity]) else None
    
    # Calculate the total tracker
    total_tracker = (R_activity.upper() == 'Y') + \
                    (SQL_activity.upper() == 'Y') + \
                    (Python_activity.upper() == 'Y') + \
                    (Github_activity.upper() == 'Y') + \
                    (Kaggle_activity.upper() == 'Y') + \
                    (Terminal_activity.upper() == 'Y') + \
                    (Excel_activity.upper() == 'Y') + \
                    (Tech_reading_activity.upper() == 'Y') + \
                    (Learning_activity.upper() == 'Y') + \
                    (Data_analytics_activity.upper() == 'Y') + \
                    (Tech_listings_activity.upper() == 'Y') + \
                    (Projects_activity.upper() == 'Y')
    
    # Print the total habit tracker of the day
    print("Your daily activity tracker is:")
    print(f"Daily activity tracker: {total_tracker}")
    print()

    # Store the activity details in the activities list
    activities.append({
        'activity_id': activity_id,
        'R': R_activity.upper(),
        'SQL': SQL_activity.upper(),
        'Python': Python_activity.upper(),
        'Github': Github_activity.upper(),
        'Kaggle': Kaggle_activity.upper(),
        'Terminal': Terminal_activity.upper(),
        'Excel': Excel_activity.upper(),
        'Tech_reading': Tech_reading_activity.upper(),
        'Learning': Learning_activity.upper(),
        'Data_analytics': Data_analytics_activity.upper(),
        'Tech_listings': Tech_listings_activity.upper(),
        'Projects': Projects_activity.upper(),
        'daily_total': total_tracker,
        'date': datetime.now().strftime("%Y-%m-%d")  # Current date in YYYY-MM-DD format
    })
    
    # Increment the activity ID counter
    activity_id_counter += 1

# Append the activities to the CSV file if it exists, otherwise create a new file
if activities:  # Only proceed if there are activities to write
    with open('daily_activities_datascience.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['activity_id', 'R', 'SQL', 'Python', 'Github', 'Kaggle', 'Terminal', 'Excel', 'Tech_reading', 'Learning', 'Data_analytics', 'Tech_listings', 'Projects', 'daily_total', 'date'])
        if not file_exists:
            writer.writeheader()  # Write header only if the file is newly created
        writer.writerows(activities)

