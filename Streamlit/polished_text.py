import streamlit as st
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

st.title("Polish your title")
que = st.text_input("Make your question: ")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents= que + ",this is a question. Give me the same question more accurate way."
)

st.markdown(response.text)