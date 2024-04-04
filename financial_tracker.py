import pandas as pd

class FinanceTracker:
    def __init__(self):
        self.transactions = pd.DataFrame(columns=['Date', 'Description', 'Amount'])
    
    def add_transaction(self, date, description, amount):
        new_transaction = pd.DataFrame([[date, description, amount]], columns=['Date', 'Description', 'Amount'])
        self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)
    
    def add_new_transaction_interactively(self):
        date = input("Enter the date (YYYY-MM-DD): ")
        description = input("Enter the description: ")
        amount = float(input("Enter the amount (positive for income, negative for expense): "))
        self.add_transaction(date, description, amount)

# Example usage
tracker = FinanceTracker()
tracker.add_transaction('2023-01-01', 'Groceries', -50)
tracker.add_transaction('2023-01-02', 'cloth', -150)
tracker.add_transaction('2023-01-03', 'travel', -850)

# Add new transactions interactively
tracker.add_new_transaction_interactively()

# Print out the results
print("Transactions:")
print(tracker.transactions)

# Define the file path where you want to save the CSV file
file_path = 'financial_tracker.csv'

# Save the DataFrame to a CSV file using the object created (tracker.transactions)
tracker.transactions.to_csv(file_path, index=False)

