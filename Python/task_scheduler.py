import schedule
import time

def remind_task(task):
    # Code to remind about task
# Schedule reminders for important tasks
schedule.every().day.at("10:00").do(remind_task, task="Review project report")
schedule.every().monday.at("14:00").do(remind_task, task="Team meeting")
schedule.every().friday.at("16:00").do(remind_task, task="Submit weekly report")
# Keep the script running to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
