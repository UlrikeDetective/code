import pandas as pd
import os

class FinanceTracker:
    def __init__(self):
        self.transactions = pd.DataFrame(columns=['Date', 'Description', 'Amount'])
    
    def add_transaction(self, date, description, amount):
        new_transaction = pd.DataFrame([[date, description, amount]], columns=['Date', 'Description', 'Amount'])
        self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)

# Example usage
tracker = FinanceTracker()

# Loop to continuously add transactions
while True:
    new_entry = input("Do you have a new transaction to add? (yes/no): ")
    
    if new_entry.lower() == 'yes':
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))  # Assuming amount is a float value
        tracker.add_transaction(date, description, amount)
    elif new_entry.lower() == 'no':
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Print out the results
print("\nTransactions:")
print(tracker.transactions)

# Define the file path where you want to save the CSV file
file_path = 'financial_tracker.csv'

# Save the DataFrame to a CSV file in append mode
if os.path.exists(file_path):
    tracker.transactions.to_csv(file_path, mode='a', header=False, index=False)
else:
    tracker.transactions.to_csv(file_path, mode='w', index=False)

