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
