def extract_topics(text):
    keywords = {
        "Electric Vehicles": ["EV", "electric car", "battery", "charging"],
        "Stock Market": ["shares", "stock", "investors", "market"],
        "Innovation": ["technology", "breakthrough", "AI", "research"],
        "Regulations": ["law", "compliance", "government", "rules"],
        "Autonomous Vehicles": ["self-driving", "autopilot", "AI", "Lidar"]
    }
    topics = []
    for topic, words in keywords.items():
        if any(word.lower() in text.lower() for word in words):
            topics.append(topic)
    return topics if topics else ["General"]