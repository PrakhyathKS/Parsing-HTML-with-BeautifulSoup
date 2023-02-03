import requests
from bs4 import BeautifulSoup
 
# Set the URL that you want to scrape
URL = "https://books.toscrape.com/"
 
# Send an HTTP request to the website and store the response
page = requests.get(URL)
 
# Parse the HTML content of the page
soup = BeautifulSoup(page.content, 'html.parser')
 
# Find all the links on the page
for link in soup.find_all('a'):
    print(link.get('href'))
