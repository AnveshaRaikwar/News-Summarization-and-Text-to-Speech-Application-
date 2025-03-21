def comparative_analysis(articles):
    sentiment_count = {"Positive": 0, "Negative": 0, "Neutral": 0}
    coverage_differences = []
    all_topics = []
    
    for i, article in enumerate(articles):
        sentiment_count[article["Sentiment"]] += 1
        all_topics.append(set(article["Topics"]))
        if i > 0:
            coverage_differences.append({
                "Comparison": f"Article {i} highlights {article['Summary'][:50]}..., while Article {i+1} focuses on {articles[i-1]['Summary'][:50]}...",
                "Impact": "Different angles on the company news affecting market perception."
            })
    
    common_topics = set.intersection(*all_topics) if all_topics else set()
    topic_overlap = {
        "Common Topics": list(common_topics),
        "Unique Topics in Article 1": list(all_topics[0] - common_topics) if all_topics else [],
        "Unique Topics in Article 2": list(all_topics[1] - common_topics) if len(all_topics) > 1 else []
    }
    
    return {
        "Sentiment Distribution": sentiment_count,
        "Coverage Differences": coverage_differences,
        "Topic Overlap": topic_overlap
    }
