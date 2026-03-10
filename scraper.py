import requests
from bs4 import BeautifulSoup
import pandas as pd


BASE_URL = "https://quotes.toscrape.com/page/{}/"


def scrape_quotes(pages=10):
    quotes = []
    authors = []

    for page in range(1, pages + 1):
        url = BASE_URL.format(page)

        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            for quote in soup.find_all("span", class_="text"):
                quotes.append(quote.text)

            for author in soup.find_all("small", class_="author"):
                authors.append(author.text)

            print(f"Scraped page {page}")

        except Exception as e:
            print(f"Error scraping page {page}: {e}")

    return quotes, authors


def save_to_csv(quotes, authors):
    data = {"Quote": quotes, "Author": authors}
    df = pd.DataFrame(data)
    df.to_csv("quotes_data.csv", index=False)
    print("Data saved to quotes_data.csv")


if __name__ == "__main__":
    quotes, authors = scrape_quotes(10)
    save_to_csv(quotes, authors)