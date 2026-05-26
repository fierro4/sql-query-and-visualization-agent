import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("AIzaSyAkXOdaxdIWGhLVZqyZEZvhvn4KDCxa3Dc")
)

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Say hello")

print(response.text)