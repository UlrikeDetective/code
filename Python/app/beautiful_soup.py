import requests
from bs4 import BeautifulSoup

# Fetch the webpage
url = "https://www.lovebigisland.com/hawaii-blog/"
response = requests.get(url)
html_content = response.content

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find and extract data
title = soup.find("h1").text
paragraphs = [p.text for p in soup.find_all("p")]

print("Title:", title)
print("Paragraphs:", paragraphs)