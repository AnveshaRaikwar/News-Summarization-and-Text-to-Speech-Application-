import streamlit as st
import requests
import subprocess

# Start FastAPI server in the background
subprocess.Popen(["python", "fastapi_server.py"])

API_URL = "https://anvesharaikwar-news-summarization-n-tts.hf.space/news/"

# Set page configuration
st.set_page_config(page_title="News Summarization & Analysis", page_icon="📢", layout="wide")

# Add custom styles with violet color scheme
st.markdown("""
    <style>
        .header {
            font-size: 36px;
            color: #ffffff;
            font-weight: bold;
            text-align: center;
            padding: 20px;
            background: linear-gradient(135deg, #8e44ad 0%, #9b59b6 100%);  /* Violet Gradient */
            border-radius: 10px;
            width: 75%;
            margin: 0 auto;
        }
        .subheader {
            font-size: 24px;
            color: #333;
            font-weight: bold;
        }
        .info {
            font-size: 18px;
            color: #444;
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
        .card {
            background-color: #f7f7f7;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .content {
            background: linear-gradient(135deg, #7b8dff 0%, #b19bff 100%);  /* Violet Gradient */
            padding: 20px;
            border-radius: 10px;
            color: white;
        }
        .info-box {
            background-color: #ffffff;
            padding: 15px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .error {
            color: #ff0000;
            font-size: 18px;
        }
        .input-section {
            width: 60%;
            margin: 0 auto;
        }
        .output-section {
            width: 60%;
            margin: 20px auto;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">📢 News Sentiment & Comparative Analysis</div>', unsafe_allow_html=True)

# Add space below header
st.markdown("<br><br>", unsafe_allow_html=True)

# Input section inside 60% width
with st.container():
    st.markdown('<div class="input-section">', unsafe_allow_html=True)
    
    # Create a single column for company input (centered)
    company_name = st.text_input("Enter a company name:", "Tesla", key="company_name", label_visibility="visible")
    
    if st.button("Analyze News"):
        with st.spinner("Fetching and analyzing news..."):
            try:
                response = requests.get(API_URL + company_name)

                # Log the raw response text for debugging
                st.write(f"Response Text: {response.text}")

                if response.status_code == 200:
                    try:
                        data = response.json()

                        if "error" in data:
                            st.error(data["error"])
                        else:
                            # Results Section in 60% width
                            st.markdown('<div class="output-section">', unsafe_allow_html=True)

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

                            st.markdown('</div>', unsafe_allow_html=True)

                    except ValueError:
                        st.error("Failed to decode JSON. Please check the API response.")
                else:
                    st.error("Failed to fetch data. Please try again.")
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

