import schedule
import time

def post_to_DataScience():
    # Placeholder function body
    print("Posting to Data Science")

def post_to_livingHealthy():
    # Placeholder function body
    print("Posting to Living Healthy")

def post_to_good_things():
    # Placeholder function body
    print("Posting to Good Things")

def post_to_journal():
    # Placeholder function body
    print("Posting to Journal")

# Schedule posts to run at specific times
schedule.every().day.at("21:40").do(post_to_DataScience)
schedule.every().day.at("21:45").do(post_to_livingHealthy)
schedule.every().day.at("21:50").do(post_to_good_things)
schedule.every().day.at("21:55").do(post_to_journal)

# Keep the script running to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
