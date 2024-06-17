from faker import Faker
import random
import pandas as pd

fake = Faker()

def generate_fake_data(num_entries=100):
    data = []

    for _ in range(num_entries):
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        color = fake.color_name()
        country = fake.country()
        city = fake.city()
        
        entry = {
            "Name": fake.name(),
            "Address": fake.address(),
            "Email": fake.email(),
            "Phone Number": fake.phone_number(),
            "Date of Birth": fake.date_of_birth(minimum_age=18, maximum_age=85).strftime("%Y-%m-%d"),
            "Random Number": random.randint(1, 100),
            "Job Title": fake.job(),
            "Company": fake.company(),
            "Latitude": latitude,
            "Longitude": longitude,
            "Country": country,
            "Favorite City": city,
            "Color": color,
            "Favorite Fruit": fake.random_element(["Apple", "Banana", "Orange", "Grapefruit", "Mango", "Pineapple", "Strawberry", "Blueberry", "Raspberry", "Blackberry", "Kiwi", "Watermelon", "Honeydew melon", "Cantaloupe", "Grape", "Peach", "Pear", "Fig", "Pomegranate", "Dragon fruit"]),
            "Favorite Vegetarian Dish": fake.random_element(["Creamy Tomato Pasta with Spinach and Sun-dried Tomatoes", "Lentil Shepherd's Pie", "Black Bean Burgers with Chipotle Mayo", "Thai Peanut Curry with Vegetables", "Mushroom Risotto with Truffle Oil", "Stuffed Portobello Mushrooms with Goat Cheese", "Vegetable Fajitas with Guacamole", "Greek Salad with Pita Bread", "Minestrone Soup", "Sweet Potato and Black Bean Enchiladas", "Roasted Brussels Sprouts with Balsamic Glaze", "Vegetable Pot Pie", "Cauliflower Steaks with Chimichurri Sauce", "Chickpea Salad Sandwiches", "Quinoa Fried Rice with Edamame", "Ratatouille", "Lentil Soup with Lemon", "Rainbow Veggie Wraps", "Baked Tofu with Teriyaki Glaze", "Creamy Corn Chowder", "Vegetarian Chili", "Falafel Pita Pockets", "Mac and Cheese with Roasted Vegetables"]),
            "Favorite Country": fake.random_element(["Thailand", "Vietnam", "Cambodia", "Laos", "Myanmar (Burma)", "Indonesia", "Philippines", "Malaysia", "Nepal", "India", "Sri Lanka", "Peru", "Bolivia", "Ecuador", "Colombia", "Chile", "Argentina", "Brazil", "Morocco", "South Africa", "New Zealand", "Australia", "Iceland", "Czech Republic", "Poland"]),
            "Favorite Island": fake.random_element(["Bali, Indonesia", "Palawan, Philippines", "Boracay, Philippines", "Langkawi, Malaysia", "Phi Phi Islands, Thailand", "Maldives", "Seychelles", "Mauritius", "Santorini, Greece", "Mykonos, Greece", "Majorca, Spain", "Tenerife, Spain", "Madeira, Portugal", "Kauai, Hawaii, USA", "Maui, Hawaii, USA", "Oahu, Hawaii, USA", "Fiji", "Cook Islands", "Whitsunday Islands, Australia", "Great Barrier Island, New Zealand", "Isle of Skye, Scotland"]),
            "Lorem Ipsum Text": fake.text(),
            "Favorite 20th Century American Book": fake.random_element(["The Great Gatsby by F. Scott Fitzgerald", "To Kill a Mockingbird by Harper Lee", "The Catcher in the Rye by J. D. Salinger", "Invisible Man by Ralph Ellison", "One Flew Over the Cuckoo's Nest by Ken Kesey", "Beloved by Toni Morrison", "The Grapes of Wrath by John Steinbeck", "Fahrenheit 451 by Ray Bradbury", "In Cold Blood by Truman Capote", "On the Road by Jack Kerouac"]),
            "Favorite Sport (to watch)": fake.random_element(["Football (American)", "Basketball", "Baseball", "Soccer", "Tennis", "Hockey", "Handball", "Volleyball", "Sport climbing", "Surfing", "Kayaking", "Athletics", "Swimming", "Skateboarding"]),
            "Favorite Hobby": fake.random_element(["Reading", "Hiking", "Cooking", "Playing Music", "Coding", "Photography", "Yoga", "Traveling", "Dancing", "Painting", "Sleeping"]),
        }
        data.append(entry)

    return pd.DataFrame(data)

if __name__ == "__main__":
    num_entries = 100  # You can adjust the number of entries you want to generate
    fake_data_df = generate_fake_data(num_entries)

    # Save generated data to a CSV file
    fake_data_df.to_csv('fake_data.csv', index=False)
