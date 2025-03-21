# News Summarization and Text-to-Speech Application

📌 Objective 
Developed a web-based application that extracts key details from multiple news articles related 
to a given company, performs sentiment analysis, conducts a comparative analysis, and 
generates a text-to-speech (TTS) output in Hindi. Allow users to input a 
company name and receive a structured sentiment report along with an audio output. 

✨ Features

Web Scraping: Extracts news articles using BeautifulSoup.

Summarization: Uses Hugging Face models (BART/T5) for concise news summaries.

Sentiment Analysis: Analyzes positive, negative, and neutral sentiments.

Comparative Sentiment Analysis: Evaluates sentiment trends across multiple articles.

Text-to-Speech Conversion: Converts summaries to Hindi speech using gTTS.

Topic Extraction: Identifies key topics from summarized news.

API Communication: FastAPI backend serving APIs for frontend integration.

Structured Reports: Generates structured output with sentiment distribution.

🛠️ Tech Stack

Backend: FastAPI, Uvicorn, BeautifulSoup4, Requests

AI Models: Hugging Face Transformers (BART, T5), Torch, NLTK

Sentiment Analysis:Textblob

Text-to-Speech (TTS): gTTS (Google Text-to-Speech), deep_translator

Frontend: Streamlit

Deployment: Hugging Face Spaces, GitHub

🚀 Installation

1️⃣ Clone the Repository:

git clone https://github.com/your-username/News_Summarization_TTS.git
cd News_Summarization_TTS

2️⃣ Install Dependencies:

pip install -r requirements.txt

3️⃣ Run the FastAPI Backend:

python -m uvicorn main:app --reload

4️⃣ Start the Streamlit Frontend:

python -m streamlit run app.py





📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.




