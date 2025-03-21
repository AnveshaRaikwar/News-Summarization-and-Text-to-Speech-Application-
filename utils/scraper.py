import requests
from bs4 import BeautifulSoup
import os

API_KEY = "fc712e2ed95941f68c99dae23e7b24b4"

def fetch_news(company):
    url = f"https://newsapi.org/v2/everything?q={company}&apiKey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return []
    
    data = response.json()
    articles = data.get("articles", [])

    # Ensure we extract only relevant articles with content
    extracted_articles = []
    for article in articles:
        if article.get("content"):  # Ensure the article has content
            extracted_articles.append({
                "title": article["title"],
                "content": article["content"]
            })

    return extracted_articles[:10]  # Limit to 10 articles

def extract_article_content(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        return " ".join([p.text for p in paragraphs]) if paragraphs else "Content not available."
    except requests.exceptions.RequestException as e:
        return f"Error fetching content: {str(e)}"