from tkinter import *
import requests
import csv
from bs4 import BeautifulSoup


root=Tk()
root.title("Web Scrapping")
root.geometry("700x640")
root.minsize(700,640)
root.configure(bg="#000000")

Label(root, text="Parsing HTML with the BeautifulSoup Module", font=("times new roman", 20, "bold")).pack(fill=X)

e=Entry(root,width=50)
e.insert(0,"enter the URL:")
e.pack()

def webscrape():
    URL = e.get()
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




mybutton= Button(root,text="RUN",command=webscrape)
mybutton.pack()

root.mainloop()