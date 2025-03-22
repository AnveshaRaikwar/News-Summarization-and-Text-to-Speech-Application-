---
title: News Summarization N Tts
emoji: ⚡
colorFrom: yellow
colorTo: yellow
sdk: streamlit
sdk_version: 1.43.2
app_file: app.py
pinned: false
short_description: News summarization and converting text to speech in hindi
---

# News Summarization and Text-to-Speech Application

📌 Objective 

Developed a web-based application that extracts key details from multiple news articles related 
to a given company, performs sentiment analysis, conducts a comparative analysis, and 
generates a text-to-speech (TTS) output in Hindi. Allow users to input a 
company name and receive a structured sentiment report along with an audio output. 

🚀 Installation

1️⃣ Clone the Repository:

git clone https://github.com/your-username/News_Summarization_TTS.git
cd News_Summarization_TTS

Make sure that python is installed

2️⃣ Install Dependencies:

pip install -r requirements.txt

3️⃣ Run the FastAPI Backend:

python -m uvicorn main:app --reload

4️⃣ Start the Streamlit Frontend:

python -m streamlit run app.py

✨ Phases

- Web Scraping
- Summarization
- Sentiment Analysis
- Comparative Sentiment Analysis
- Text-to-Speech Conversion
- Topic Extraction
- API Communication between frontend and backend



🛠️ Tech Stack

Backend: FastAPI, Uvicorn, BeautifulSoup4, Requests

AI Models: Hugging Face Transformers (BART, T5), Torch, NLTK

Sentiment Analysis:Textblob

Text-to-Speech (TTS): gTTS (Google Text-to-Speech), deep_translator

Frontend: Streamlit

Deployment: Hugging Face Spaces, GitHub

THIRD PARTY API: NEWS API

✨ Description

+ Web Scraping :
  - Fetched news articles using NewsAPI by making an HTTP request.
  - Extracts full article content from URLs using BeautifulSoup.

+ Summarization :
  - Uses a pre-trained model (facebook/bart-large-cnn) from Hugging Face for text summarization.

+ Sentiment Analysis :
  - Uses TextBlob to determine the sentiment of a given text.
  - Calculates polarity:
         Positive sentiment if polarity > 0.
         Negative sentiment if polarity < 0.
         Neutral if polarity = 0.

+ Comparative Sentiment Analysis :
   - Tracks how many articles are positive, negative, or neutral.
   - Finds common and unique topics between articles.

+ Topic Extraction :
  -  Matches predefined keywords to classify articles into topics like Electric Vehicles, Stock Market, Innovation, Regulations, and Autonomous Vehicles.

+ Text-to-Speech Conversion :
  - Uses GoogleTranslator to convert text from any language to Hindi.
  - Uses gTTS (Google Text-to-Speech) to generate an audio file (output.mp3) from the translated text.

+ API Communication :
  - NewsAPI is used to fetch news articles.
  - Uses a pre-trained NLP model (BART/T5) to generate a concise summary of each article.
  - The FastAPI backend serves the API, processing news articles and extracting insights.
  - The API processes news data, applies summarization, sentiment analysis, and topic extraction.
  - The API can be accessed using Postman or any HTTP client

+ Frontend :
  - The frontend of the application is built using Streamlit, which provides an interactive and user-friendly interface for users to analyze news sentiment and listen to Hindi text-to-speech (TTS) output.

+ User Interaction :
  - The user enters a company name in the input field.
  - On clicking "Analyze News", Streamlit makes a request to the FastAPI backend.
  - The analyzed news articles, sentiment insights, and topics are displayed in a structured format.
  - Users can listen to the Hindi TTS summary of the overall sentiment.
  

📌 Assumptions & Limitations

Assumptions:

NewsAPI provides accurate and up-to-date news articles.

Extracted article content is relevant and properly structured.

Sentiment analysis using TextBlob provides a reasonable sentiment classification.

Summarization models (BART/T5) generate meaningful summaries.

Limitations:

NewsAPI Rate Limits: Free-tier API keys have a limited number of requests per day.

Summarization Quality: The model-generated summaries may occasionally miss key details.

Sentiment Analysis Accuracy: TextBlob sentiment analysis may not always capture nuanced sentiments.

Hindi TTS Quality: gTTS provides basic text-to-speech conversion but lacks natural prosody.


📜 License

This project is licensed under the MIT License. See the LICENSE.txt file for more details.

🤝 Contribution

Contributions are welcome! Feel free to fork, submit issues, or make pull requests.

🌐 Live Demo

Check out the deployed project on Hugging Face Spaces
Deployed Project Link : https://huggingface.co/spaces/AnveshaRaikwar/News_Summarization_and_Text_to_Speech_Application

📬 Contact

For any questions, GitHub discussions



