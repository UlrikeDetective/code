# new tasks
# print the total expances (per session, day, month, year)
# put an ID in for every item
# transcripts only per day, month (sum), year (sum)


import pandas as pd

import os

from datetime import datetime

class FinanceTracker:
    def __init__(self):
        self.file_path = 'financial_tracker.csv'
        self.load_transactions()

    def load_transactions(self):
        if os.path.exists(self.file_path):
            self.transactions = pd.read_csv(self.file_path)
        else:
            self.transactions = pd.DataFrame(columns=['Date', 'Description', 'Amount'])

    def add_transaction(self, date, description, amount):
        new_transaction = pd.DataFrame([[date, description, amount]], columns=['Date', 'Description', 'Amount'])
        self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)

    def add_new_transaction_interactively(self):
        date = datetime.now().strftime("%Y-%m-%d")  # Capture current date
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

        self.add_transaction(date, description, amount)

    def save_transactions(self):
        self.transactions.to_csv(self.file_path, index=False, mode='a', header=not os.path.exists(self.file_path))

# Example usage
tracker = FinanceTracker()

# Add new transactions interactively using a while loop
while True:
    add_more = input("Do you want to add another transaction? (yes/no): ")
    if add_more.lower() == 'yes':
        tracker.add_new_transaction_interactively()
    elif add_more.lower() == 'no':
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Save the transactions to the CSV file
tracker.save_transactions()

# Print out the results
print("Transactions:")
print(tracker.transactions)
