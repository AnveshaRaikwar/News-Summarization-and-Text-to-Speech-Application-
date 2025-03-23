from fastapi import FastAPI
import requests
from utils.summarizer import summarize_text
from utils.sentiment import analyze_sentiment
from utils.topic_extraction import extract_topics
from utils.tts import generate_tts
import logging

# Initialize FastAPI app
app = FastAPI()

NEWS_API_KEY = "fc712e2ed95941f68c99dae23e7b24b4"  # Your NewsAPI key
url = "https://newsapi.org/v2/everything"

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def fetch_news(company_name):
    """
    Fetches top 10 news articles about the given company from NewsAPI.
    """
    params = {
        "q": company_name,
        "apiKey": NEWS_API_KEY
    }
    
    # Send a GET request to the NewsAPI
    response = requests.get(url, params=params)
    
    logging.debug(f"Response Status Code: {response.status_code}")
    logging.debug(f"Response Text: {response.text}")
    
    if response.status_code != 200:
        logging.error(f"Error: {response.status_code}")
        return []

    try:
        data = response.json()  # Try to parse the JSON
    except ValueError:
        logging.error(f"Non-JSON response: {response.text}")  # If it's not a valid JSON, log the raw response
        return []

    if data.get("status") != "ok" or "articles" not in data:
        logging.error("Error: No articles found or status is not 'ok'.")
        return []

    return data["articles"][:10]  # Fetch only the top 10 articles

@app.get("/news/{company_name}")
def get_news(company_name: str):
    """
    API endpoint to get news, analyze sentiment, summarize, extract topics, and generate TTS.
    """
    articles = fetch_news(company_name)
    
    if not articles:
        return {"error": "No sufficient news articles found."}
    
    processed_articles = []
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    
    for article in articles:
        text = article.get("content") or article.get("description") or "No content available."
        summary = summarize_text(text)
        sentiment = analyze_sentiment(summary)
        topics = extract_topics(summary)
        
        processed_articles.append({
            "Title": article["title"],
            "Summary": summary,
            "Sentiment": sentiment,
            "Topics": topics
        })
        sentiment_counts[sentiment] += 1

    comparisons = []
    for i in range(len(processed_articles) - 1):
        comparisons.append({
            "Comparison": f"Article {i+1} discusses {processed_articles[i]['Topics'][0]}, whereas Article {i+2} highlights {processed_articles[i+1]['Topics'][0]}.",
            "Sentiment Impact": f"The first article has a {processed_articles[i]['Sentiment']} sentiment, whereas the second has a {processed_articles[i+1]['Sentiment']} sentiment."
        })

    all_topics = [set(a["Topics"]) for a in processed_articles]
    common_topics = list(set.intersection(*all_topics)) if len(all_topics) > 1 else []
    
    topic_overlap = {
        "Common Topics": common_topics,
        "Unique Topics": [list(topics - set(common_topics)) for topics in all_topics]
    }

    final_sentiment_analysis = f"{company_name}'s latest news coverage is mostly " + ("positive." if sentiment_counts["Positive"] > sentiment_counts["Negative"] else "negative.")
    tts_file = generate_tts(final_sentiment_analysis)

    final_report = {
        "Company": company_name,
        "Articles": processed_articles,
        "Comparative Sentiment Score": {
            "Sentiment Distribution": sentiment_counts,
            "Coverage Differences": comparisons,
            "Topic Overlap": topic_overlap
        },
        "Final Sentiment Analysis": final_sentiment_analysis,
        "Audio": tts_file
    }

    return final_report

# Run the FastAPI app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
