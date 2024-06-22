# Scraping Infinite Scrolling Websites

import requests
from bs4 import BeautifulSoup
import csv

def infinite_scroll_scraper(start_page=1):
    page_num = start_page
    while True:
        url = f"https://www.zara.com/de/de/damen-kleider-special-prices-l1093.html?v1=2416373={page_num}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        article_elements = soup.find_all('article')
        for article_element in article_elements:
            article_title = article_element.find('h2').text.strip()
            article_content = article_element.find('p').text.strip()
            yield {'title': article_title, 'content': article_content}
        # Check if there are more pages to scrape
        if not soup.find('a', class_='next-page'):
            break
        page_num += 1

# Usage
article_gen = infinite_scroll_scraper()
for article in article_gen:
    print(article)

# Open a CSV file to write the output
with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Write the header row
    for product in product_gen:
        writer.writerow(product)  # Write each product row
