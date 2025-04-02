import os
import sys
import time
import requests
import loguru
import bs4

def scrape_data_point():
    """
    Scrapes the main headline from The Daily Pennsylvanian home page.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/"
    }

    req = requests.get("https://www.thedp.com", headers=headers)

    loguru.logger.info(f"Request URL: {req.url}")
    loguru.logger.info(f"Request status code: {req.status_code}")

    if req.status_code == 403:
        loguru.logger.error("Access forbidden (403). The website is blocking the request.")
        return None

    if req.ok:
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        target_element = soup.find("a", class_="frontpage-link")
        data_point = "" if target_element is None else target_element.text
        loguru.logger.info(f"Data point: {data_point}")
        return data_point

if __name__ == "__main__":
    loguru.logger.add("scrape.log", rotation="1 day")

    loguru.logger.info("Creating data directory if it does not exist")
    try:
        os.makedirs("data", exist_ok=True)
    except Exception as e:
        loguru.logger.error(f"Failed to create data directory: {e}")
        sys.exit(1)

    loguru.logger.info("Starting scrape")
    time.sleep(10)  # Respect Crawl-delay from robots.txt

    try:
        data_point = scrape_data_point()
    except Exception as e:
        loguru.logger.error(f"Failed to scrape data point: {e}")
        data_point = None
