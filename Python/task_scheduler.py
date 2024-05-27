import schedule
import time

def remind_task(task):
    print(f"Reminder: {task}")

# Schedule tasks to run at specific times
schedule.every().day.at("21:45").do(remind_task, task="daily habits report")
schedule.every().monday.at("07:30").do(remind_task, task="Check tasks for the week")
schedule.every().friday.at("16:00").do(remind_task, task="Start weekend")

# Keep the script running to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
