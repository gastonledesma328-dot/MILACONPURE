from fastapi import FastAPI
from scraper_m3u8 import scrape_with_playwright

app = FastAPI()

@app.get("/scrape")
def scrape(url: str):
    links = scrape_with_playwright(url)

    return {
        "status": "ok",
        "count": len(links),
        "streams": links
    }
