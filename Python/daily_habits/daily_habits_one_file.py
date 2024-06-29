import csv
from datetime import datetime
import geocoder
import os

def get_activity_input(prompt):
    response = input(prompt).upper()
    while response not in {'Y', 'N'}:
        print("Invalid input. Please enter Y or N.")
        response = input(prompt).upper()
    return response

def append_to_csv(file_path, fieldnames, data):
    file_exists = os.path.isfile(file_path)
    with open(file_path, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

def get_location():
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng, g.city, g.state, g.country
    else:
        return None, None, None, None

def record_habit_log(filename):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    latlng, city, state, country = get_location()

    habit_questions = [
        ("r", "Any R today? (Y/N): "),
        ("sql", "Any SQL today? (Y/N): "),
        ("python", "Any Python today? (Y/N): "),
        ("github", "Any Github today? (Y/N): "),
        ("kaggle", "Any Kaggle or competition today? (Y/N): "),
        ("terminal", "Any Terminal today? (Y/N): "),
        ("excel", "Any Excel today? (Y/N): "),
        ("adobe", "Any Adobe today? (Y/N): "),
        ("website", "Any web development today? (Y/N): "),
        ("others", "Any others today? (Y/N): "),
        ("career", "Did you work on your career today? (Y/N): "),
        ("networking", "Any networking today? (Y/N): "),
        ("tech_learning", "Any tech learning today? (Y/N): "),
        ("tech_reading", "Any tech reading today? (Y/N): "),
        ("tech_listing", "Any tech listing today? (Y/N): "), 
        ("yoga", "Did you do yoga today? (Y/N): "),
        ("meditation", "Did you meditate today? (Y/N): "),
        ("steps", "Did you measure your steps today? (Y/N): "),
        ("biking_duration", "Did you ride a bike today? (Y/N): "),
        ("other_sport", "Did you do any other sport today? (Y/N): "),
        ("fruit", "Did you eat fruits today? (Y/N): "),
        ("vegetables", "Did you eat vegetables today? (Y/N): "),
        ("water", "Did you drink more than two liters of water today? (Y/N): "),
        ("book", "Did you read a book today? (Y/N): "),
        ("listening", "Did you listen to an audiobook or podcast today? (Y/N): ")
    ]

    activity_data = {}
    for activity, prompt in habit_questions:
        activity_data[activity] = get_activity_input(prompt)
        if activity_data[activity] == 'Y':
            activity_data[activity] = input(f"Please specify details for {activity.replace('_', ' ')}: ")

    focus_levels = ['Beginner', 'Beginner/Intermediate', 'Intermediate', 'Intermediate/Advanced', 'Advanced', 'All level', 'None']
    how_did_it_go_choices = {
        '0': '0 = bad day - no Data Science',
        '1': '1 = awful',
        '2': '2 = maybe another day',
        '3': '3 = still a lot to learn',
        '4': '4 = fine',
        '5': '5 = good',
        '6': '6 = Knowledge is rising',
        '7': '7 = fantastic',
        '8': '8 = good day / holiday - sorry no Data Science'
    }
    data_science_programme = input("Main Data Science program used today: ")
    focus = input("One thing you focused on: ")
    print("Choose the level of focus:")
    for idx, level in enumerate(focus_levels, start=1):
        print(f"{idx}. {level}")
    
    focus_level_idx = input("Enter the number corresponding to the focus level: ")
    while not focus_level_idx.isdigit() or int(focus_level_idx) not in range(1, len(focus_levels) + 1):
        print("Invalid input. Please enter a number corresponding to the focus level.")
        focus_level_idx = input("Enter the number corresponding to the focus level: ")
    focus_level = focus_levels[int(focus_level_idx) - 1]

    print("How did it go?")
    for key, value in how_did_it_go_choices.items():
        print(f"{key}. {value}")
    
    how_did_it_go_key = input("Enter the number corresponding to your experience: ")
    while how_did_it_go_key not in how_did_it_go_choices:
        print("Invalid input. Please enter a number corresponding to your experience.")
        how_did_it_go_key = input("Enter the number corresponding to your experience: ")
    how_did_it_go = how_did_it_go_choices[how_did_it_go_key]

    first_good_thing = input("First good thing today: ")
    second_good_thing = input("Second good thing today: ")
    third_good_thing = input("Third good thing today: ")
    honorary_mention = input("Honorary mention today: ")

    log_entry = {
        'Timestamp': current_time,
        'Latitude and Longitude': latlng,
        'City': city,
        'State': state,
        'Country': country,
        'data_science_programme': data_science_programme,
        'focus': focus,
        'focus_level': focus_level,
        'how_did_it_go': how_did_it_go,
        'first': first_good_thing,
        'second': second_good_thing,
        'third': third_good_thing,
        'honorary': honorary_mention
    }

    log_entry.update(activity_data)

    fieldnames = ['Timestamp', 'Latitude and Longitude', 'City', 'State', 'Country', 'data_science_programme', 'focus', 'focus_level', 'how_did_it_go', 'first', 'second', 'third', 'honorary'] + [q[0] for q in habit_questions]
    append_to_csv(filename, fieldnames, log_entry)
    print("Log entry added successfully!")

def main():
    record_habit_log('daily_tracker.csv')

if __name__ == "__main__":
    main()
