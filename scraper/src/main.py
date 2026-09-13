import requests
from pathlib import Path
from bs4 import BeautifulSoup

URL = 'https://books.toscrape.com/'
TIMEOUT = 5

CACHE_FILE = Path("cache/catalogue-page-1.html")

HEADERS = {
    "user-agent": "FlyRankInternship-A9/1.0 (+https://github.com/basselamr1/flyrank-backend-scraper-assignment)"
}

def fetch_and_cache():

    if(CACHE_FILE.exists()):
        html = CACHE_FILE.read_text(encoding='utf-8')
        print("CACHE HIT")
        print(f"Response size: {len(html)} bytes")
        return html
    
    print("FETCH")
    response = requests.get(url=URL, headers= HEADERS, timeout= TIMEOUT)
    response.raise_for_status()
    html = response.text
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(html, encoding='utf-8')
    print(f"Response size: {len(html)} bytes")
    return html

if __name__ == "__main__":
    fetch_and_cache()