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

def check_and_get_unique_entry(file_path, date, log_type):
    if os.path.isfile(file_path):
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get('date') == date and row.get('log_type') == log_type:
                    return None
    return date

def habit_tracker(filename, habit_questions, log_type):
    today_date = datetime.now().strftime("%Y-%m-%d")

    if not check_and_get_unique_entry(filename, today_date, log_type):
        print(f"Today's entries for {log_type} already exist. Exiting.")
        return

    activity_data = {'date': today_date, 'log_type': log_type}

    all_questions = []
    for activity, prompt in habit_questions:
        all_questions.append(activity.strip())  # Remove trailing whitespaces
        activity_data[activity] = get_activity_input(prompt)

    # Additional functionality for specific activities
    if activity_data.get('biking_duration') == 'Y':
        activity_data['biking_duration'] = input("How many minutes of biking did you do today? ")
    elif activity_data.get('steps') == 'Y':
        activity_data['steps'] = input("How many steps did you do today? ")
    elif activity_data.get('yoga') == 'Y':
        activity_data['yoga'] = input("How many minutes of yoga did you do today? ")
    elif activity_data.get('meditation') == 'Y':
        activity_data['meditation'] = input("How many minutes of meditation did you do today? ")
    elif activity_data.get('other_sport') == 'Y':
        activity_data['other_sport'] = input("What other sport did you do today? ")
    elif activity_data.get('book') == 'Y':
        activity_data['book'] = input("What book did you read today? ")
    elif activity_data.get('listening') == 'Y':
        activity_data['listening'] = input("What audiobook or podcast did you listen to today? ")
    elif activity == "adobe":
        activity_data['adobe'] = input("Any Adobe tools used today? ")
    elif activity == "website":
        activity_data['website'] = input("What web development programs did you use today? ")
    elif activity == "others":
        activity_data['others'] = input("What other programs did you use today? ")
    elif activity == "career":
        activity_data['career'] = input("What did you for your career today? ")
    elif activity == "networking":
        activity_data['networking'] = input("What networking event did you go today? ")
    elif activity == "tech_learning":
        activity_data['tech_learning'] = input("What tech course did you attend today? ")
    elif activity == "tech_reading":
        activity_data['tech_reading'] = input("What tech magazine or book did you read today? ")
    elif activity == "tech_listing":
        activity_data['tech_listing'] = input("What tech podcast or audiobook did you listen to today? ")

    # Calculate daily total of activities marked as 'Y'
    total_tracker = sum(1 for v in activity_data.values() if v == 'Y')
    activity_data['daily_total'] = total_tracker

    # Construct fieldnames including all questions
    fieldnames = ['date', 'log_type', 'daily_total'] + [q[0] for q in habit_questions]

    # Append data to CSV
    append_to_csv(filename, fieldnames, activity_data)

def add_log_entry(filename):
    header = ['date', 'log_type', 'daily_total', 'kaggle', 'github', 'others', 'adobe', 'excel', 'website', 'sql', 'tech_reading', 'r', 'python', 'tech_learning', 'tech_listing', 'terminal', 'career', 'networking']
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
    how_did_it_go = how_did_it_go_choices[input("Enter the number corresponding to your experience: ")]

    log_entry = {
        'date': date,
        'data_science_programme': data_science_programme,
        'focus': focus,
        'focus_level': focus_level,
        'how_did_it_go': how_did_it_go,
        'log_type': 'Data Science Log',
        'kaggle': input("Any Kaggle kernels used today? "),
        'github': input("Any github repositories used today? "),
        'others': input("Any other tools used today? "),
        'adobe': input("Any Adobe tools used today? "),
        'excel': input("Any Excel tools used today? "),
        'website': input("Any website development tools used today? "),
        'sql': input("Any SQL programming used today? "),
        'tech_reading': input("Any tech book, magazine or post used today? "),
        'r': input("Any R programming used today? "),
        'python': input("Any Python programming used today? "),
        'tech_learning': input("Any tech learning, lecture or seminar? "),
        'tech_listing': input("Any tech podcast or lecture listened to today? "),
        'terminal': input("Any terminal activity today? "),
        'career': input("Any career activity today? "),
        'networking': input("Any networking activity today? ")
    }
    append_to_csv(filename, header, log_entry)
    print("Log entry added successfully!")

def good_things_log(filename):
    class GoodThingsLog:
        def __init__(self, filename):
            self.filename = filename
            self.fieldnames = ['date', 'log_type', 'first_good_thing', 'second_good_thing', 'third_good_thing', 'honorary_mentions']
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
                    'log_type': 'Good Things Log',
                    'first_good_thing': first,
                    'second_good_thing': second,
                    'third_good_thing': third,
                    'honorary_mentions': honorary
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
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_location():
    location = geocoder.ip('me')
    return location.address

def record_entry(filename):
    entry_location = get_location()
    entry_date = datetime.now().strftime('%Y-%m-%d')
    entry_time = datetime.now().strftime('%H:%M:%S')

    location_entry = {
        'date': entry_date,
        'time': entry_time,
        'location': entry_location,
        'log_type': 'Location Entry'
    }

    append_to_csv(filename, ['date', 'time', 'location', 'log_type'], location_entry)
    print("Location entry added successfully!")

def show_menu():
    print("1. Habit Tracker")
    print("2. Add Log Entry")
    print("3. Good Things Log")
    print("4. Record Entry Location")
    print("5. Exit")

def main():
    filename = 'activity_log.csv'
    habit_questions = [
        ('biking_duration', "Did you bike today? (Y/N): "),
        ('steps', "Did you take steps today? (Y/N): "),
        ('yoga', "Did you practice yoga today? (Y/N): "),
        ('meditation', "Did you meditate today? (Y/N): "),
        ('other_sport', "Did you do any other sport today? (Y/N): "),
        ('book', "Did you read a book today? (Y/N): "),
        ('listening', "Did you listen to an audiobook or podcast today? (Y/N): "),
        ('adobe', "Did you use any Adobe tools today? (Y/N): "),
        ('website', "Did you use any web development programs today? (Y/N): "),
        ('others', "Did you use any other programs today? (Y/N): "),
        ('career', "Did you do anything for your career today? (Y/N): "),
        ('networking', "Did you attend any networking event today? (Y/N): "),
        ('tech_learning', "Did you attend any tech course today? (Y/N): "),
        ('tech_reading', "Did you read any tech magazine or book today? (Y/N): "),
        ('tech_listing', "Did you listen to any tech podcast or audiobook today? (Y/N): ")
    ]

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            log_type = input("Enter log type for Habit Tracker: ")
            habit_tracker(filename, habit_questions, log_type)

        elif choice == "2":
            add_log_entry(filename)

        elif choice == "3":
            good_things_log(filename)

        elif choice == "4":
            record_entry(filename)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
