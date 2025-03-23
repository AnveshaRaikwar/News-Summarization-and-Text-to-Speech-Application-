import streamlit as st
import requests
import subprocess

# Start FastAPI server in the background
subprocess.Popen(["python", "fastapi_server.py"])

API_URL = "http://127.0.0.1:7860/news/"  # Make sure FastAPI server is running on this URL

# Set page configuration
st.set_page_config(page_title="News Summarization & Analysis", page_icon="📢", layout="centered")

# Custom CSS styles
st.markdown("""
    <style>
        .header {
            font-size: 36px;
            color: white;
            font-weight: bold;
            text-align: center;
            padding: 20px;
            background: linear-gradient(135deg, #8e44ad 0%, #9b59b6 100%); /* Violet Gradient */
            border-radius: 10px;
            width: 75%;
            margin: 0 auto;
        }
        .input-container {
            width: 50%;
            margin: 0 auto;
            padding: 20px;
            background-color: #f0f0f0;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .button {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
        }
        .button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">📢 News Sentiment & Comparative Analysis</div>', unsafe_allow_html=True)

# Input section in a centered box
with st.container():
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    
    # Create a centered text input for the company name
    company_name = st.text_input("Enter a company name:", "Tesla")
    
    if st.button("Analyze News"):
        with st.spinner("Fetching and analyzing news..."):
            try:
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

                        # Comparative Sentiment Analysis
                        st.subheader("📊 Comparative Sentiment & Topic Analysis")
                        st.write("### 🔄 Comparative Sentiment Differences:")
                        for comparison in data["Comparative Sentiment Score"]["Coverage Differences"]:
                            st.write(f"- {comparison['Comparison']}")
                            st.write(f"  - **Sentiment Shift:** {comparison['Sentiment Impact']}")

                        st.write("### 🔍 Topic Overlap:")
                        st.write(f"**Common Topics:** {', '.join(data['Comparative Sentiment Score']['Topic Overlap']['Common Topics'])}")
                        for i, unique_topics in enumerate(data["Comparative Sentiment Score"]["Topic Overlap"]["Unique Topics"]):
                            st.write(f"**Unique Topics in Article {i+1}:** {', '.join(unique_topics)}")

                        # Final Sentiment Analysis
                        st.subheader("📢 Overall Sentiment Analysis")
                        st.write(data["Final Sentiment Analysis"])

                        # Hindi TTS Audio Output
                        st.audio(data["Audio"], format="audio/mp3")
                else:
                    st.error("Failed to fetch data. Please try again.")
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)
