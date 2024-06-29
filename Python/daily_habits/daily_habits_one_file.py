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
        writer.writerows(data)

def check_and_get_unique_entry(file_path, date, log_type):
    if os.path.isfile(file_path):
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get('date') == date and row.get('log_type') == log_type:
                    return None
    return date

def habit_tracker(filename, habit_questions, log_type):
    activities = []
    activity_id_counter = 1
    today_date = datetime.now().strftime("%Y-%m-%d")
    
    if not check_and_get_unique_entry(filename, today_date, log_type):
        print(f"Today's entries for {log_type} already exist. Exiting.")
        return

    while True:
        name = input(f"Any activities for the {log_type} habit tracker today? (Enter 'quit' to stop): ")
        if name.lower() == 'quit':
            break

        activity_data = {'date': today_date, 'log_type': log_type}
        for activity, prompt in habit_questions:
            activity_data[activity] = get_activity_input(prompt)
            if activity_data[activity] == 'Y':
                if activity == "biking_duration":
                    activity_data['biking_duration'] = input("How many minutes of biking did you do today? ")
                elif activity == "steps":
                    activity_data['steps'] = input("How many steps did you do today? ")
                elif activity == "other_sport":
                    activity_data['other_sport'] = input("What other sport did you do today? ")
                elif activity == "book":
                    activity_data['book'] = input("What book did you read today? ")
                elif activity == "listening":
                    activity_data['listening'] = input("What audiobook or podcast did you listen to today? ")
                elif activity == "adobe":
                    activity_data['adobe'] = input("Any Adobe tools used today? ")
                elif activity == "website":
                    activity_data['website'] = input("Any web development today? ")
                elif activity == "others":
                    activity_data['others'] = input("Any other tech activities today? ")
                elif activity == "career":
                    activity_data['career'] = input("Did you work on your career today? ")
                elif activity == "networking":
                    activity_data['networking'] = input("Did you do any networking today? ")
                elif activity == "tech_learning":
                    activity_data['tech_learning'] = input("Any tech learning today? ")
                elif activity == "tech_reading":
                    activity_data['tech_reading'] = input("Any tech reading today? ")
                elif activity == "tech_listing":
                    activity_data['tech_listing'] = input("Any tech listing today? ")

        activity_id = f"Habit{activity_id_counter:03}" if any(v == 'Y' for v in activity_data.values()) else None
        total_tracker = sum(1 for v in activity_data.values() if v == 'Y')

        activity_data.update({
            'activity_id': activity_id,
            'daily_total': total_tracker,
        })
        activities.append(activity_data)
        activity_id_counter += 1

    if activities:
        fieldnames = ['activity_id', 'date', 'log_type', 'daily_total'] + [q[0] for q in habit_questions]
        append_to_csv(filename, fieldnames, activities)

def get_location():
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng, g.city, g.state, g.country
    else:
        return None, None, None, None

def record_entry(filename):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    latlng, city, state, country = get_location()
    data = [{
        'Timestamp': current_time,
        'Latitude and Longitude': latlng,
        'City': city,
        'State': state,
        'Country': country,
        'log_type': 'Location'
    }]
    file_exists = os.path.isfile(filename)
    fieldnames = ['Timestamp', 'Latitude and Longitude', 'City', 'State', 'Country', 'log_type']
    append_to_csv(filename, fieldnames, data)
    print(f"Recorded: {data}")

def add_log_entry(filename):
    header = ['date', 'data_science_programme', 'focus', 'focus_level', 'how_did_it_go', 'log_type']
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
    file_exists = os.path.isfile(filename) and os.path.getsize(filename) > 0
    date = datetime.now().strftime('%Y-%m-%d')
    data_science_programme = input("Main used Data Science programme of the day: ")
    focus = input("One thing you focused on: ")
    print("Choose the level of focus:")
    for idx, level in enumerate(focus_levels, start=1):
        print(f"{idx}. {level}")
    focus_level_idx = int(input("Enter the number corresponding to the focus level: "))
    focus_level = focus_levels[focus_level_idx - 1]
    print("How did it go?")
    for key, value in how_did_it_go_choices.items():
        print(f"{key}. {value}")
    how_did_it_go = input("Enter the number corresponding to your experience: ")
    how_did_it_go = how_did_it_go_choices[how_did_it_go]
    log_entry = [{
        'date': date,
        'data_science_programme': data_science_programme,
        'focus': focus,
        'focus_level': focus_level,
        'how_did_it_go': how_did_it_go,
        'log_type': 'Data Science Log'
    }]
    append_to_csv(filename, header, log_entry)
    print("Log entry added successfully!")

def good_things_log(filename):
    class GoodThingsLog:
        def __init__(self, filename):
            self.filename = filename
            self.fieldnames = ['date', 'first_good_thing', 'second_good_thing', 'third_good_thing', 'honorary_mentions', 'log_type']
            self.check_and_create_file()

        def check_and_create_file(self):
            if not os.path.exists(self.filename):
                with open(self.filename, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                    writer.writeheader()

        def add_log(self, first, second, third, honorary):
            current_date = datetime.now().strftime('%Y-%m-%d')
            if not check_and_get_unique_entry(self.filename, current_date, 'Good Things Log'):
                print("Today's good things log already exists. Exiting.")
                return
            with open(self.filename, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                writer.writerow({
                    'date': current_date,
                    'first_good_thing': first,
                    'second_good_thing': second,
                    'third_good_thing': third,
                    'honorary_mentions': honorary,
                    'log_type': 'Good Things Log'
                })

        def display_logs(self):
            with open(self.filename, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for idx, row in enumerate(reader, start=1):
                    print(f"Good things Log #{idx}:")
                    for key, value in row.items():
                        print(f"{key}: {value}")
                    print("\n")

    good_things_log = GoodThingsLog(filename)

    while True:
        print("\nGood Things Log Menu:")
        print("1. Add a new log")
        print("2. Display all logs")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            first = input("Enter first good thing: ")
            second = input("Enter second good thing: ")
            third = input("Enter third good thing: ")
            honorary = input("Enter honorary mentions: ")

            good_things_log.add_log(first, second, third, honorary)
            print("Log added successfully!")

        elif choice == "2":
            good_things_log.display_logs()

        elif choice == "3":
            print("Exiting Good Things Log.")
            break

        else:
            print("Invalid choice. Please try again.")

def main():
    record_entry('daily_tracker.csv')
    
    data_science_habit_questions = [
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
        ("tech_listing", "Any tech listing today? (Y/N): ")
    ]
    habit_tracker('daily_tracker.csv', data_science_habit_questions, 'Data Science')
    
    living_healthy_habit_questions = [
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
    habit_tracker('daily_tracker.csv', living_healthy_habit_questions, 'Living Healthy')

    add_log_entry('daily_tracker.csv')

    good_things_log('daily_tracker.csv')

if __name__ == "__main__":
    main()
