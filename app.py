import streamlit as st
import requests
import subprocess

# Start FastAPI server in the background
subprocess.Popen(["python", "fastapi_server.py"])

API_URL = "http://localhost:7860/news/"  # Ensure the URL matches the FastAPI backend URL

# Set the page configuration for the frontend
st.set_page_config(page_title="News Sentiment & Analysis", page_icon="📢", layout="wide")

# Add a custom header with color
st.markdown("""
    <style>
        .header {
            font-size: 36px;
            color: #ffffff;
            font-weight: bold;
            text-align: center;
            padding: 20px;
            background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
            border-radius: 10px;
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
            background: linear-gradient(135deg, #7b8dff 0%, #b19bff 100%);
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
        .logos {
            display: flex;
            justify-content: space-evenly;
            flex-wrap: wrap;
            gap: 20px;
            padding: 20px;
            height: 100%;
        }
        .logo {
            width: 100px;
            height: 100px;
            background-color: #f1f1f1;
            border-radius: 10px;
            padding: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">📢 News Sentiment & Comparative Analysis</div>', unsafe_allow_html=True)

# Create two columns for company input and company logos
col1, col2 = st.columns([1, 1])  # Equal space for both columns

# Left Column - Company Logos
with col1:
    st.markdown('<h3>🖼️ Company Logos</h3>', unsafe_allow_html=True)
    
    logos = [
        {"name": "Tesla", "image": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Tesla_Motors_logo.png"},
        {"name": "Apple", "image": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_%28black%29.svg"},
        {"name": "Microsoft", "image": "https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo_%282012%29.svg"},
        {"name": "Google", "image": "https://upload.wikimedia.org/wikipedia/commons/2/29/Google_logo.svg"},
        {"name": "Amazon", "image": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg"},
        {"name": "Facebook", "image": "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg"}
    ]
    
    # Display logos with a clickable hover effect for each company
    st.markdown('<div class="logos">', unsafe_allow_html=True)
    
    for logo in logos:
        st.markdown(f'<div class="logo"><img src="{logo["image"]}" width="80" height="80" alt="{logo["name"]} Logo"/></div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Right Column - Empty (No content in this column)
with col2:
    pass  # No content in this column
