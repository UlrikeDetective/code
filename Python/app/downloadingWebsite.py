import requests

def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

download_file('https://visit.withgoogle.com/events/.pdf', 'sample.pdf')