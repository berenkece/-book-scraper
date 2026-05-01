import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://books.toscrape.com"
all_books = []

for page in range(1,51):
    url = base_url.format(page)
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text.strip()
        rating = book.find("p", class_="star-rating")["class"][1]
        stock = book.find("p", class_="instock availability").text.strip()

        all_books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "stock": stock
        })

    print(f"page {page} scraped - {len(books)} books collected")

print(f"\nTotal books collected: {len(all_books)}")

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price", "rating", "stock"])
    writer.writeheader()
    writer.writerows(all_books)

print("Data saved to books.csv")
