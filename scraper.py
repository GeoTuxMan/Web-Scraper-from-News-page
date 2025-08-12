"""
scraper.py <url> <num_items> <output.csv>
"""
import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape(url, n):
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, "lxml")
    items = []
    # generic: find <a> with headline-like text (this is a best-effort template)
    for a in soup.find_all('a', limit=n):
        text = a.get_text(strip=True)
        href = a.get('href')
        if text:
            items.append({"title": text, "link": href})
    return items

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python scraper.py <url> <num> <output.csv>")
    else:
        url = sys.argv[1]
        n = int(sys.argv[2])
        out = sys.argv[3]
        rows = scrape(url, n)
        pd.DataFrame(rows).to_csv(out, index=False)
        print("Saved", out)
