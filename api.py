from fastapi import FastAPI
from scraper_m3u8 import scrape_with_playwright, scrape_with_selenium, scrape_simple

app = FastAPI()

@app.get("/scrape")
def scrape(url: str):
    links = []

    try:
        links = scrape_with_playwright(url)
    except:
        try:
            links = scrape_with_selenium(url)
        except:
            links = scrape_simple(url)

    return {
        "status": "ok",
        "count": len(links),
        "streams": links
    }
