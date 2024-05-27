import csv
import datetime

def log_expense(amount, category):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('expenses.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, amount, category])
    print(f"Logged expense: {timestamp}, Amount: {amount}, Category: {category}")

# Example call to log an expense
log_expense(30, 'Utilities')
log_expense(15, 'Coffee')
log_expense(75, 'Dining Out')


# Function to read back and print the contents of the CSV file
def read_expenses():
    with open('expenses.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(', '.join(row))

# Call the read function to verify the logged expense
read_expenses()

