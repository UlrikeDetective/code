import calendar

def highlight_weekends(year, month):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    month_str = cal.formatmonth(year, month)
    month_weeks = cal.monthdayscalendar(year, month)
    
    lines = month_str.split('\n')
    header = lines[:2]
    days_lines = lines[2:]

    # Create a mapping of days to their corresponding colored string
    day_color_map = {}
    for week in month_weeks:
        for day in week:
            if day == 0:  # 0 means day outside the current month
                continue
            if calendar.weekday(year, month, day) in (calendar.SATURDAY, calendar.SUNDAY):
                day_color_map[day] = f'\033[91m{day:2}\033[0m'  # Red color
            else:
                day_color_map[day] = f'{day:2}'

    # Highlight the weekends in the calendar lines
    highlighted_days_lines = []
    for line in days_lines:
        highlighted_line = ''
        for token in line.split():
            if token.isdigit():
                day = int(token)
                highlighted_line += day_color_map[day] + ' '
            else:
                highlighted_line += token + ' '
        highlighted_days_lines.append(highlighted_line.rstrip())

    # Join the lines back together
    highlighted_month_str = '\n'.join(header + highlighted_days_lines)
    print(highlighted_month_str)

year = int(input("Enter the year of the required calendar: "))
month = int(input("Enter the month of the required calendar: "))
highlight_weekends(year, month)
