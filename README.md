# Book Scraper

A Python web scraper that extracts book data from [books.toscrape.com](https://books.toscrape.com) and analyses the results.

## What it does

- Scrapes 1000 books across 50 pages
- Extracts title, price, rating, and stock status
- Exports data to Excel with multiple sheets (All Books, 5 Stars, Alphabetical)

## Tech Stack

- Python
- BeautifulSoup4
- Requests
- Openpyxl

## How to run

Install dependencies:
pip install -r requirements.txt

Scrape data:
python scraper.py

Analyse data:
python analyse.py
