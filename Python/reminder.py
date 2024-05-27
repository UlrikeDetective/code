import schedule
import time

def post_to_DataSciense():

def post_to_livingHealthy():

def post_to_good_things():

def post_to_journal():

# Schedule posts to run at specific times
schedule.every().day.at("21:40").do(post_to_DataScience)
schedule.every().day.at("21:45").do(post_to_living_Healthy)
schedule.every().day.at("21:50").do(post_to_good_things)
schedule.every().day.at("21:55").do(post_to_journal)
# Keep the script running to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
