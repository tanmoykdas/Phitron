from google import genai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

st.title("Gemini Chat bot")

que = st.text_input("Enter you question here")

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=que
)
st.divider()

st.write(f"Gemini says: {response.text}")