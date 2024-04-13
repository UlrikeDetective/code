# new tasks

# new csv file per day, month (sum), year (sum) - balance sheet

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
            self.transactions['Date'] = pd.to_datetime(self.transactions['Date'])
            self.transactions['Date'] = self.transactions['Date'].dt.strftime('%Y-%m-%d')
            self.transactions['Time'] = pd.to_datetime(self.transactions['Date']).dt.strftime('%H:%M:%S')
        else:
            self.transactions = pd.DataFrame(columns=['ID', 'Date', 'Time', 'Description', 'Amount'])

    def add_transaction(self, date, description, amount):
        new_transaction = pd.DataFrame([[str(datetime.now()), date, description, amount]], columns=['ID', 'Date', 'Description', 'Amount'])
        if self.transactions.empty:
            self.transactions = new_transaction
        else:
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
        if not os.path.exists(self.file_path):
            self.transactions.to_csv(self.file_path, index=False)
        else:
            self.transactions.to_csv(self.file_path, mode='a', header=False, index=False)

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

# Calculate and print total per session
print("Total per session:", tracker.calculate_total_per_session())


