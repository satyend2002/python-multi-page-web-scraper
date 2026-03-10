# Python Multi Page Web Scraper

## Project Overview

This project is a Python web scraping tool that collects quotes and their authors from multiple pages of the website **https://quotes.toscrape.com**.
The script automatically navigates through several pages, extracts the required data, and stores the results in a CSV file.

## Features

* Scrapes quotes and author names from multiple pages
* Automatically loops through website pagination
* Stores extracted data in CSV format
* Clean and simple Python implementation
* Easy to modify for scraping other websites

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas

## Installation

Clone the repository:

git clone https://github.com/satyend2002/python-multi-page-scraper.git

Navigate to the project folder:

cd python-multi-page-scraper

Install required libraries:

pip install -r requirements.txt

## Run the Script

python scraper.py

## Output

After running the script, a file named **all_quotes.csv** will be generated containing the scraped data.

Example output:

Quote,Author
"The world as we have created it...",Albert Einstein
"It is our choices...",J.K. Rowling

## Use Cases

* Learning web scraping with Python
* Data collection for analysis
* Automation of repetitive data extraction tasks

## Author

Satyendra Dwivedi
Python Backend Developer
