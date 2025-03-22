import streamlit as st
import requests
import subprocess

# Start FastAPI server in the background
subprocess.Popen(["python", "fastapi_server.py"])

API_URL = "https://anvesharaikwar-news-summarization-n-tts.hf.space/news/"

st.title("📢 News Sentiment & Comparative Analysis")

company_name = st.text_input("Enter a company name:", "Tesla")

if st.button("Analyze News"):
    with st.spinner("Fetching and analyzing news..."):
        response = requests.get(API_URL + company_name)
        
        if response.status_code == 200:
            data = response.json()
            
            if "error" in data:
                st.error(data["error"])
            else:
                st.subheader(f"📰 News Articles for {company_name}")
                
                for i, article in enumerate(data["Articles"]):
                    st.markdown(f"### {i+1}. {article['Title']}")
                    st.write(f"**Summary:** {article['Summary']}")
                    st.write(f"**Sentiment:** {article['Sentiment']}")
                    st.write(f"**Topics:** {', '.join(article['Topics'])}")
                    st.write("---")

                # 🔥 Comparative Analysis Section
                st.subheader("📊 Comparative Sentiment & Topic Analysis")
                
                st.write("### 🔄 Comparative Sentiment Differences:")
                for comparison in data["Comparative Sentiment Score"]["Coverage Differences"]:
                    st.write(f"- {comparison['Comparison']}")
                    st.write(f"  - **Sentiment Shift:** {comparison['Sentiment Impact']}")
                
                st.write("### 🔍 Topic Overlap:")
                st.write(f"**Common Topics:** {', '.join(data['Comparative Sentiment Score']['Topic Overlap']['Common Topics'])}")
                
                for i, unique_topics in enumerate(data["Comparative Sentiment Score"]["Topic Overlap"]["Unique Topics"]):
                    st.write(f"**Unique Topics in Article {i+1}:** {', '.join(unique_topics)}")

                # 🔥 Final Sentiment Analysis
                st.subheader("📢 Overall Sentiment Analysis")
                st.write(data["Final Sentiment Analysis"])

                # 🔊 Hindi TTS Audio Output
                st.audio(data["Audio"], format="audio/mp3")

        else:
            st.error("Failed to fetch data. Please try again.")
