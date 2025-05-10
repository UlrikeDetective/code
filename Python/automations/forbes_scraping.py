import requests
import json
import csv
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the Forbes Real-Time Billionaires page
url = "https://www.forbes.com/real-time-billionaires/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Step 2: Find the JSON data embedded in the HTML
script_tag = soup.find("script", type="application/ld+json")

if script_tag is None:
    raise ValueError("Could not find the JSON data on the page. The structure of the page may have changed.")

try:
    json_data = json.loads(script_tag.string)
except json.JSONDecodeError as e:
    raise ValueError(f"Error parsing JSON data: {e}")

# Step 3: Extract the list of billionaires
billionaires_list = json_data.get("itemListElement", [])

if not billionaires_list:
    raise ValueError("No billionaires data found in the JSON.")

# Step 4: Create a CSV file and write the headers
with open('forbes_billionaires.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(["Rank", "Name", "Net Worth", "Change", "Age", "Source", "Country/Territory"])
    
    # Step 5: Loop through each billionaire and extract the required information
    for billionaire in billionaires_list:
        name = billionaire["name"]
        position = billionaire["position"]
        
        # Fetching the billionaire's profile page to get additional details
        profile_url = billionaire["url"]
        profile_response = requests.get(profile_url, headers=headers)
        profile_soup = BeautifulSoup(profile_response.content, "html.parser")
        
        # Extracting details from the profile page
        try:
            net_worth = profile_soup.find("div", class_="profile-info__net-worth").text.strip()
        except AttributeError:
            net_worth = "N/A"
        
        try:
            change = profile_soup.find("div", class_="profile-info__change").text.strip()
        except AttributeError:
            change = "N/A"
        
        try:
            age = profile_soup.find("div", class_="profile-info__age").text.strip().split()[0]
        except AttributeError:
            age = "N/A"
        
        try:
            source = profile_soup.find("div", class_="profile-info__source").text.strip()
        except AttributeError:
            source = "N/A"
        
        try:
            country = profile_soup.find("div", class_="profile-info__country").text.strip()
        except AttributeError:
            country = "N/A"
        
        # Write the data to the CSV file
        writer.writerow([position, name, net_worth, change, age, source, country])

print("Data has been saved to forbes_billionaires.csv")
