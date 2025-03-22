from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/news/{query}")
def get_news(query: str):
    url = f"https://www.google.com/search?q={query}+news"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to fetch news"}

    soup = BeautifulSoup(response.text, "html.parser")
    headlines = [h.text for h in soup.find_all("h3")[:5]]  # Extracting top 5 headlines

    return {"query": query, "headlines": headlines}
