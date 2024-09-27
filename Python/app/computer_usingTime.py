import time
from datetime import datetime

def log_computer_usage():
    with open('usage_log.txt', 'a') as log:
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"Computer started at {start_time}\n")
        try:
            while True:
                time.sleep(60)  # Log usage every minute
        except KeyboardInterrupt:
            end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"Computer shutdown at {end_time}\n")

log_computer_usage()