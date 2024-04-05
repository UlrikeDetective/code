# new tasks
# don't overwrite
# only asks one time per session for the date
# print the total expances (per session, day, month, year)


import pandas as pd

class FinanceTracker:
    def __init__(self):
        self.transactions = pd.DataFrame(columns=['Date', 'Description', 'Amount'])
    
    def add_transaction(self, date, description, amount):
        new_transaction = pd.DataFrame([[date, description, amount]], columns=['Date', 'Description', 'Amount'])
        if self.transactions.empty:
            self.transactions = new_transaction
        else:
            self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)
    
    def add_new_transaction_interactively(self):
        while True:
            date = input("Enter the date (YYYY-MM-DD): ")
            if len(date) == 10 and date.count('-') == 2:
                try:
                    pd.to_datetime(date)
                    break
                except ValueError:
                    print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
            else:
                print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

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


# Add new transactions interactively using a while loop
while True:
    add_more = input("Do you want to add another transaction? (yes/no): ")
    if add_more.lower() == 'yes':
        tracker.add_new_transaction_interactively()
    elif add_more.lower() == 'no':
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Print out the results
print("Transactions:")
print(tracker.transactions)

# Define the file path where you want to save the CSV file
file_path = 'financial_tracker.csv'

# Save the DataFrame to a CSV file using the object created (tracker.transactions)
tracker.transactions.to_csv(file_path, index=False)


