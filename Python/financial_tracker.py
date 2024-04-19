# new tasks

# new csv file per day, month (sum), year (sum) - balance sheet

# new tasks

# new csv file per day, month (sum), year (sum) - balance sheet

import pandas as pd
import os
from datetime import datetime

class FinanceTracker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.load_transactions()

    def load_transactions(self):
        if os.path.exists(self.file_path):
            self.transactions = pd.read_csv(self.file_path)
            self.transactions['Date'] = pd.to_datetime(self.transactions['Date']).dt.strftime('%Y-%m-%d')
            self.transactions['Time'] = pd.to_datetime(self.transactions['Time']).dt.strftime('%H:%M:%S')  # Convert "Time" column to correct format
        else:
            self.transactions = pd.DataFrame(columns=['ID', 'Date', 'Time', 'Description', 'Amount'])

    def add_transaction(self, date, description, amount):
        new_transaction = pd.DataFrame([[datetime.now().strftime('%Y-%m-%d %H:%M:%S'), date, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), description, amount]], columns=['ID', 'Date', 'Time', 'Description', 'Amount'])
        self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)

    def add_new_transaction_interactively(self):
        while True:
            description = input("Enter the description: ")
            if any(char.isalpha() for char in description):
                break
            else:
                print("Description must contain at least one letter.")

        while True:
            try:
                amount = float(input("Enter the amount (positive for income, negative for expense): "))
                break
            except ValueError:
                print("Invalid amount. Please enter a valid number.")

        self.add_transaction(datetime.now().strftime("%Y-%m-%d"), description, amount)

    def calculate_total_per_session(self):
        return self.transactions['Amount'].sum()

    def save_transactions(self):
        self.transactions.to_csv(self.file_path, mode='a', header=not os.path.exists(self.file_path), index=False)

file_path = '/Users/ulrike_imac_air/projects/analysis_my_life/data/daily_activities/financial_tracker.csv'
tracker = FinanceTracker(file_path)

while True:
    add_more = input("Do you want to add another transaction? (yes/no): ")
    if add_more.lower() == 'yes':
        tracker.add_new_transaction_interactively()
    elif add_more.lower() == 'no':
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

tracker.save_transactions()



