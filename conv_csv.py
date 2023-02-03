import requests
import csv
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='default')

books = results.find_all('article')

# Open a CSV file for writing
with open('books.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Title', 'Price'])  # write the header row
    
    # Loop through each book and write the data to the CSV file
    for book in books:
        title = book.h3.a.text
        price = book.find('p', class_='price_color').text
        writer.writerow([title, price])
