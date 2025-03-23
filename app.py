import streamlit as st
import requests

API_URL = "https://anvesharaikwar-news-summarization-n-tts.hf.space/news/"

# Set page configuration
st.set_page_config(page_title="News Summarization & Analysis", page_icon="📢", layout="wide")

# Header with violet gradient background
st.markdown("""
    <style>
        .header {
            font-size: 36px;
            color: white;
            font-weight: bold;
            text-align: center;
            background: linear-gradient(135deg, #8e44ad, #9b59b6);
            padding: 20px;
            width: 75%;
            margin: 0 auto;
        }
        .input-section, .output-section {
            width: 60%;
            margin: 20px auto;
        }
    </style>
    <div class="header">📢 News Sentiment & Comparative Analysis</div>
""", unsafe_allow_html=True)

# Input section for company name
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
                    st.markdown('<div class="output-section">', unsafe_allow_html=True)

                    st.subheader(f"📰 News Articles for {company_name}")
                    for i, article in enumerate(data["Articles"]):
                        st.markdown(f"### {i+1}. {article['Title']}")
                        st.write(f"**Summary:** {article['Summary']}")
                        st.write(f"**Sentiment:** {article['Sentiment']}")
                        st.write(f"**Topics:** {', '.join(article['Topics'])}")
                        st.write("---")

                    st.subheader("📊 Comparative Sentiment & Topic Analysis")
                    st.write("### 🔄 Comparative Sentiment Differences:")
                    for comparison in data["Comparative Sentiment Score"]["Coverage Differences"]:
                        st.write(f"- {comparison['Comparison']}")
                        st.write(f"  - **Sentiment Shift:** {comparison['Sentiment Impact']}")

                    st.write("### 🔍 Topic Overlap:")
                    st.write(f"**Common Topics:** {', '.join(data['Comparative Sentiment Score']['Topic Overlap']['Common Topics'])}")
                    for i, unique_topics in enumerate(data["Comparative Sentiment Score"]["Topic Overlap"]["Unique Topics"]):
                        st.write(f"**Unique Topics in Article {i+1}:** {', '.join(unique_topics)}")

                    st.subheader("📢 Overall Sentiment Analysis")
                    st.write(data["Final Sentiment Analysis"])

                    st.audio(data["Audio"], format="audio/mp3")
                    st.markdown('</div>', unsafe_allow_html=True)

            else:
                st.error("Failed to fetch data. Please try again.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error: {e}")

