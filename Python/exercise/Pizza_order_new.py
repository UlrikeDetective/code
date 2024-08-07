import csv
from datetime import datetime
import os

file_exists = os.path.isfile('pizza_delivery.csv')

print("Thank you for choosing Python Pizza Deliveries!")

orders = {}  # Dictionary to store order details

order_id_counter = 0  # Initialize the order ID counter

extras = {
    'vegetables': {'onions': 1, 'peppers': 1, 'mushrooms': 1, 'courgette': 1, 'aubergine': 1, 'broccoli': 1, 'olives': 1, 'pineapple': 1},
    'protein': {'chicken': 1, 'pulled pork': 1, 'bacon': 1, 'crispy tofu': 1, 'fried egg': 1},
    'greens': {'rocket': 1, 'spinach': 1, 'basil': 1}
}

while True:
    name = input("What is your name? Do you want to order a pizza? (Enter 'quit' to stop): ")
    if name.lower() == 'quit':
        break

    size_valid = False
    while not size_valid:
        size = input("What size pizza do you want? S, M, or L? ")
        if size.upper() in {'S', 'M', 'L'}:
            size_valid = True
        else:
            print("Invalid pizza size. Please enter S, M, or L.")

    pepperoni_valid = False
    while not pepperoni_valid:
        add_pepperoni = input("Do you want pepperoni? Y or N? ")
        if add_pepperoni.upper() in {'Y', 'N'}:
            pepperoni_valid = True
        else:
            print("Invalid input. Please enter Y or N.")

    cheese_valid = False
    while not cheese_valid:
        extra_cheese = input("Do you want extra cheese? Y or N? ")
        if extra_cheese.upper() in {'Y', 'N'}:
            cheese_valid = True
        else:
            print("Invalid input. Please enter Y or N.")

    additional_extras = []
    while True:
        extra_type = input("Do you want to add any extras? Type 'vegetables', 'protein', 'greens' or 'done' to finish: ")
        if extra_type.lower() == 'done':
            break
        if extra_type.lower() not in ['vegetables', 'protein', 'greens']:
            print("Invalid input. Please choose from 'vegetables', 'protein', 'greens', or 'done'.")
            continue
        available_extras = extras.get(extra_type.lower(), {})
        while True:
            extra_choice = input(f"Choose from {', '.join(available_extras.keys())} or type 'done' to finish selecting {extra_type}: ")
            if extra_choice.lower() == 'done':
                break
            if extra_choice.lower() not in available_extras:
                print("Invalid input. Please choose from the available options.")
                continue
            additional_extras.append(extra_choice.lower())

    drink_valid = False
    while not drink_valid:
        drink = input("Do you want to add a drink? Y or N? ")
        if drink.upper() in {'Y', 'N'}:
            drink_valid = True
        else:
            print("Invalid input. Please enter Y or N.")
    
    # Calculate the cost of the pizza and each item
    size_cost = {'S': 10, 'M': 15, 'L': 20}
    pepperoni_cost = 2 if add_pepperoni.upper() == 'Y' else 0
    cheese_cost = 1 if extra_cheese.upper() == 'Y' else 0
    drink_cost = 1 if drink.upper() == 'Y' else 0
    extra_cost = len(additional_extras)

    total_cost = size_cost.get(size.upper(), 0) + pepperoni_cost + cheese_cost + drink_cost + extra_cost

    # Print the bill for the order
    print("Your order summary:")
    print(f"Size: {size.upper()} - ${size_cost.get(size.upper(), 0)}")
    print(f"Pepperoni: {'Yes' if add_pepperoni.upper() == 'Y' else 'No'} - ${pepperoni_cost}")
    print(f"Extra Cheese: {'Yes' if extra_cheese.upper() == 'Y' else 'No'} - ${cheese_cost}")
    print(f"Drink: {'Yes' if drink.upper() == 'Y' else 'No'} - ${drink_cost}")
    if additional_extras:
        print("Additional Extras:")
        for extra in additional_extras:
            print(f"  {extra.capitalize()} - $1")
    print(f"Total cost: ${total_cost}")
    print()

    # Increment the order ID for each new order
    order_id_counter += 1
    order_id_str = f"PYPIZZA{order_id_counter:03}"  # Format the order ID as PYPIZZA001, PYPIZZA002, etc.
    
    # Store the order details in the orders dictionary
    orders[order_id_str] = {
        'name': name,
        'size': size.upper(),
        'add_pepperoni': add_pepperoni.upper(),
        'extra_cheese': extra_cheese.upper(),
        'additional_extras': ', '.join(additional_extras),
        'drink': drink.upper(),
        'size_cost': size_cost.get(size.upper(), 0),
        'pepperoni_cost': pepperoni_cost,
        'cheese_cost': cheese_cost,
        'drink_cost': drink_cost,
        'extra_cost': extra_cost,
        'total_cost': total_cost,
        'order_date': datetime.now().strftime("%Y-%m-%d")  # Current date in YYYY-MM-DD format
    }

# Append the orders to the CSV file if it exists, otherwise create a new file
if orders:  # Only proceed if there are orders to write
    with open('pizza_delivery.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['order_id', 'name', 'size', 'add_pepperoni', 'extra_cheese', 'additional_extras', 'drink', 'size_cost', 'pepperoni_cost', 'cheese_cost', 'drink_cost', 'extra_cost', 'total_cost', 'order_date'])
        if not file_exists:
            writer.writeheader()  # Write header only if the file is newly created
        for order_id, order_details in orders.items():
            writer.writerow({'order_id': order_id, 'name': order_details['name'], 'size': order_details['size'],
                             'add_pepperoni': order_details['add_pepperoni'], 'extra_cheese': order_details['extra_cheese'],
                             'additional_extras': order_details['additional_extras'], 'drink': order_details['drink'],
                             'size_cost': order_details['size_cost'], 'pepperoni_cost': order_details['pepperoni_cost'],
                             'cheese_cost': order_details['cheese_cost'], 'drink_cost': order_details['drink_cost'],
                             'extra_cost': order_details['extra_cost'], 'total_cost': order_details['total_cost'],
                             'order_date': order_details['order_date']})

# Next task
# Faker node.js
