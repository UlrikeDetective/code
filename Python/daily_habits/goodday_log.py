import csv
from datetime import datetime
import os

class GoodThingsLog:
    def __init__(self, filename):
        self.filename = filename
        self.fieldnames = ['Date', 'First good thing', 'Second good thing', 'Third good thing', 'Honorary mentions']
        self.check_and_create_file()

    def check_and_create_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                writer.writeheader()

    def add_log(self, first, second, third, honorary):
        current_date = datetime.now().strftime('%Y-%m-%d')  # Get current date
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writerow({
                'Date': current_date,
                'First good thing': first,
                'Second good thing': second,
                'Third good thing': third,
                'Honorary mentions': honorary
            })

    def display_logs(self):
        with open(self.filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for idx, row in enumerate(reader, start=1):
                print(f"Good things Log #{idx}:")
                for key, value in row.items():
                    print(f"{key}: {value}")
                print("\n")


def main():
    filename = 'good_things_log.csv'
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
            if not os.path.exists(filename):
                print("No logs to display.")
            else:
                good_things_log.display_logs()

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
