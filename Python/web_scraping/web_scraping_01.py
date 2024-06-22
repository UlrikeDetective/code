# Scraping Large Datasets with Generators

import requests
from bs4 import BeautifulSoup
import csv

def product_scraper(start_page, end_page):
    for page_num in range(start_page, end_page + 1):
        url = f"https://www.roxy-germany.de/sale/{page_num}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for product_element in soup.find_all('div', class_='product'):
            product_name = product_element.find('h3').text.strip()
            product_price = product_element.find('span', class_='price').text.strip()
            yield {'name': product_name, 'price': product_price}

# Usage
product_gen = product_scraper(1, 10)

# Open a CSV file to write the output
with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Write the header row
    for product in product_gen:
        writer.writerow(product)  # Write each product row
