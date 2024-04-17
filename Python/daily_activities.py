import csv
from datetime import datetime
import os

file_exists = os.path.isfile('daily_activities_datascience.csv')

print("Thank you for showing up today!")

activities = []  # List to store activity details
activity_id_counter = 1  # Initialize the activity ID counter
total_activities = 0  # Initialize the total number of activities done

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
    
    Adobe_activity = input("Any Adobe today? Y or N? ")
    if Adobe_activity.upper() == 'Y':
        program = input("Which program? (AI, PS, Pdf, etc.): ")
    
    Websites_activity = input("Any Websites today? Y or N? ")
    if Websites_activity.upper() == 'Y':
        specify = input("Please specify (e.g., HTML, CSS): ")
    
    Json_activity = input("Any Json today? Y or N? ")
    while Json_activity.upper() not in {'Y', 'N'}:
        print("Invalid input. Please enter Y or N.")
        Json_activity = input("Any Json today? Y or N? ")
    
    Others_activity = input("Any others today? Y or N? ")
    if Others_activity.upper() == 'Y':
        specify_other = input("Please specify: ")
    
    Tech_reading_activity = input("Any Tech Reading today? Y or N? ")
    if Tech_reading_activity.upper() == 'Y':
        magazines = input("What magazines? (e.g., Medium, Wired): ")
    
    Learning_activity = input("Any Learning today? Y or N? ")
    if Learning_activity.upper() == 'Y':
        course = input("What course? (e.g., Coursera, Udemy): ")
    
    Tech_listings_activity = input("Any Tech Listings today? Y or N? ")
    if Tech_listings_activity.upper() == 'Y':
        podcasts = input("What podcasts/audiobooks? ")
    
    Data_analytics_activity = input("Did you do any data analytics today? Y or N? ")
    if Data_analytics_activity.upper() == 'Y':
        analytics = input("Please specify? ")
    
    Projects_activity = input("Any Projects today? Y or N? ")
    if Projects_activity.upper() == 'Y':
        project = input("What project? ")
    
    Networking_activity = input("Any Networking today? Y or N? ")
    if Networking_activity.upper() == 'Y':
        networking_event = input("What networking event? (e.g., Conference name): ")
    
    # Generate an ID if at least one activity is marked as 'Y'
    activity_id = f"DataScience{activity_id_counter:03}" if any(a.upper() == 'Y' for a in [R_activity, SQL_activity, Python_activity, Github_activity, Kaggle_activity, Terminal_activity, Excel_activity, Adobe_activity, Websites_activity, Json_activity, Others_activity, Tech_reading_activity, Learning_activity, Tech_listings_activity, Projects_activity, Networking_activity]) else None
    
    # Calculate the total tracker
    total_tracker = (R_activity.upper() == 'Y') + \
                    (SQL_activity.upper() == 'Y') + \
                    (Python_activity.upper() == 'Y') + \
                    (Github_activity.upper() == 'Y') + \
                    (Kaggle_activity.upper() == 'Y') + \
                    (Terminal_activity.upper() == 'Y') + \
                    (Excel_activity.upper() == 'Y') + \
                    (Adobe_activity.upper() == 'Y') + \
                    (Websites_activity.upper() == 'Y') + \
                    (Json_activity.upper() == 'Y') + \
                    (Others_activity.upper() == 'Y') + \
                    (Tech_reading_activity.upper() == 'Y') + \
                    (Learning_activity.upper() == 'Y') + \
                    (Tech_listings_activity.upper() == 'Y') + \
                    (Data_analytics_activity.upper() == 'Y') + \
                    (Projects_activity.upper() == 'Y') + \
                    (Networking_activity.upper() == 'Y')
    
    # Increment the total number of activities done
    total_activities += total_tracker
    
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
        'Adobe': Adobe_activity.upper(),
        'Websites': Websites_activity.upper(),
        'Json': Json_activity.upper(),
        'Others': Others_activity.upper(),
        'Tech_reading': Tech_reading_activity.upper(),
        'Learning': Learning_activity.upper(),
        'Tech_listings': Tech_listings_activity.upper(),
        'Data_analytics': Data_analytics_activity.upper(),
        'Projects': Projects_activity.upper(),
        'Networking': Networking_activity.upper(),
        'program': program if Adobe_activity.upper() == 'Y' else None,
        'specify': specify if Websites_activity.upper() == 'Y' else None,
        'specify_other': specify_other if Others_activity.upper() == 'Y' else None,
        'magazines': magazines if Tech_reading_activity.upper() == 'Y' else None,
        'course': course if Learning_activity.upper() == 'Y' else None,
        'podcast': podcasts if Tech_listings_activity.upper() == 'Y' else None,
        'analytics': analytics if Data_analytics_activity.upper() == 'Y' else None,
        'networking_event': networking_event if Networking_activity.upper() == 'Y' else None,
        'daily_total': total_tracker,
        'date': datetime.now().strftime("%Y-%m-%d")  # Current date in YYYY-MM-DD format
    })

    
    # Increment the activity ID counter
    activity_id_counter += 1

# Append the activities to the CSV file if it exists, otherwise create a new file
# Append the activities to the CSV file if it exists, otherwise create a new file
if activities:  # Only proceed if there are activities to write
    with open('daily_activities_datascience.csv', mode='a', newline='') as file:
        fieldnames = ['activity_id', 'daily_total', 'date', 'R', 'SQL', 'Python', 'Github', 'Kaggle', 'Terminal', 'Excel', 'Adobe', 'Websites', 'Json', 'Others', 'Tech_reading', 'Learning', 'Tech_listings', 'Data_analytics', 'Projects', 'Networking', 'name', 'program', 'specify', 'specify_other', 'magazines', 'course', 'podcast', 'analytics', 'networking_event']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()  # Write header only if the file is newly created
        writer.writerows(activities)

# Determine the message based on the total number of activities done
if total_activities == 0:
    print("Digital detoxing?")
elif 1 <= total_activities <= 3:
    print("Hard day at work or lazy day?")
elif 4 <= total_activities <= 6:
    print("Not bad")
elif 7 <= total_activities <= 10:
    print("Excellent")
else:
    print("Olympic gold medal ;.)")

