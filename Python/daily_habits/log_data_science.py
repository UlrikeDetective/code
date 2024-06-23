import csv
from datetime import datetime
import os

def add_log_entry(filename='data_science_log.csv'):
    # Define the header
    header = ['Date', 'Data Science Programme', 'Focus', 'Focus Level', 'How Did It Go']
    
    # Define fixed choices
    focus_levels = ['Beginner', 'Beginner/Intermediate', 'Intermediate', 'Intermediate/Advanced', 'Advanced', 'All level', 'None']
    how_did_it_go_choices = {
        '0': '0 = bad day - no Data Science',
        '1': '1 = aweful',
        '2': '2 = maybe another day',
        '3': '3 = still a lot to learn',
        '4': '4 = fine',
        '5': '5 = good',
        '6': '6 = Knowledge is rising',
        '7': '7 = fantastic',
        '8': '8 = good day / holiday - sorry no Data Science'
    }
    
    # Check if the file exists and is not empty
    file_exists = os.path.isfile(filename) and os.path.getsize(filename) > 0

    # Get current date
    date = datetime.now().strftime('%Y-%m-%d')

    # Prompt user for input
    data_science_programme = input("Main used Data Science programme of the day: ")
    focus = input("One thing you focused on: ")
    
    # Prompt for focus level
    print("Choose the level of focus:")
    for idx, level in enumerate(focus_levels, start=1):
        print(f"{idx}. {level}")
    focus_level_idx = int(input("Enter the number corresponding to the focus level: "))
    focus_level = focus_levels[focus_level_idx - 1]
    
    # Prompt for how did it go
    print("How did it go?")
    for key, value in how_did_it_go_choices.items():
        print(f"{key}. {value}")
    how_did_it_go = input("Enter the number corresponding to your experience: ")
    how_did_it_go = how_did_it_go_choices[how_did_it_go]
    
    # Prepare log entry
    log_entry = [date, data_science_programme, focus, focus_level, how_did_it_go]

    # Write log entry to CSV file
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header if the file does not exist or is empty
        if not file_exists:
            writer.writerow(header)
        
        writer.writerow(log_entry)

    print("Log entry added successfully!")

# Run the function to add a new log entry
add_log_entry()
