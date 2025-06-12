import requests
from bs4 import BeautifulSoup
from datetime import datetime
from models.assignment import Assignment   # or whichever model
from storage.data_manager import get_data_manager

def fetch_olx_listings(url: str) -> list[dict]:
    """
    Fetch the page at `url`, parse out raw listing data, and return a list of dicts.
    """
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()  # fail fast on HTTP errors

    soup = BeautifulSoup(resp.text, "html.parser")
    listings = []
    # … we’ll fill this in next …
    for item in soup.select(".list-item"):  # adjust selector as needed
        title = item.select_one(".title").get_text(strip=True)
        price = item.select_one(".price").get_text(strip=True)
        date_str = item.select_one(".date").get_text(strip=True)
        link = item.select_one("a")["href"]

        # Parse date, handle different formats if needed
        try:
            date_posted = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            date_posted = datetime.now()  # fallback to now if parsing fails

        listings.append({
            "title": title,
            "price": price,
            "date_posted": date_posted,
            "link": link
        })
    return listings
def parse_price(raw_price: str) -> float | None:
    # strip currency & spaces
    cleaned = raw_price.replace("UZS", "").replace("\u202f", "").replace(",", "").strip()
    return float(cleaned) if cleaned.isdigit() else None
def clean_text(val: str) -> str:
    return " ".join(val.split()).strip()

def now_iso() -> str:
    """
    Return the current time in ISO 8601 format.
    """
    return datetime.now().isoformat(timespec='seconds')

def clean_listing(raw: dict) -> dict:
    """
    Given a raw dict from fetch_olx_listings, return a normalized record.
    """
    return {
        "title":      clean_text(raw["title"]),
        "price":      parse_price(raw.get("price_raw", "")),
        "url":        raw["url"],            # already a URL string
        "scraped_at": now_iso(),
    }
