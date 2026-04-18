from google import genai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Give me idea of gemini api key witing 50 words"
)

st.markdown(response.text)