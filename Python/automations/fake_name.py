# Fake name generator

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
            "country": country,
            "fav_city": city,
            "Color": color,
            "Favorite Fruit": fake.random_element(["Apple", "Banana", "Orange", "Grapefruit", "Mango", "Pineapple", "Strawberry", "Blueberry", "Raspberry", "Blackberry", "Kiwi", "Watermelon", "Honeydew melon", "Cantaloupe", "Grape", "Peach", "Pear", "Fig", "Pomegranate", "Dragon fruit"]),
            "Favorite Country": fake.random_element(['USA', 'UK', 'Spain', 'France', 'India', 'Sweden', 'Italy', 'South Africa']),
            "Lorem Ipsum Text": fake.text(),
        }
        data.append(entry)

    return pd.DataFrame(data)

if __name__ == "__main__":
    num_entries = 100  # You can adjust the number of entries you want to generate
    fake_data_df = generate_fake_data(num_entries)

    # Save generated data to a CSV file
    fake_data_df.to_csv('fake_data_with_geo_colors.csv', index=False)

