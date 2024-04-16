import csv
from datetime import datetime
import os

file_exists = os.path.isfile('daily_activities_datascience.csv')

print("Thank you for showing up today!")

activities = []  # List to store activity details

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
    
    # Calculate the total tracker
    total_tracker = (R_activity.upper() == 'Y') + \
                    (SQL_activity.upper() == 'Y') + \
                    (Python_activity.upper() == 'Y') + \
                    (Github_activity.upper() == 'Y') + \
                    (Kaggle_activity.upper() == 'Y') + \
                    (Terminal_activity.upper() == 'Y') + \
                    (Excel_activity.upper() == 'Y')
    
    # Print the total habit tracker of the day
    print("Your daily activity tracker is:")
    print(f"Daily activity tracker: {total_tracker}")
    print()

    # Store the activity details in the activities list
    activities.append({
        'name': name,
        'R': R_activity.upper(),
        'SQL': SQL_activity.upper(),
        'Python': Python_activity.upper(),
        'Github': Github_activity.upper(),
        'Kaggle': Kaggle_activity.upper(),
        'Terminal': Terminal_activity.upper(),
        'Excel': Excel_activity.upper(),
        'daily_total': total_tracker,
        'date': datetime.now().strftime("%Y-%m-%d")  # Current date in YYYY-MM-DD format
    })

# Append the activities to the CSV file if it exists, otherwise create a new file
if activities:  # Only proceed if there are activities to write
    with open('daily_activities_datascience.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'R', 'SQL', 'Python', 'Github', 'Kaggle', 'Terminal', 'Excel', 'daily_total', 'date'])
        if not file_exists:
            writer.writeheader()  # Write header only if the file is newly created
        writer.writerows(activities)
