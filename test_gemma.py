
import streamlit as st
from google import genai

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

response = client.models.generate_content(
    model="gemma-4-26b-a4b-it",
    contents="Reply with exactly: CampusClarity connection works."
)

print(response.text)
