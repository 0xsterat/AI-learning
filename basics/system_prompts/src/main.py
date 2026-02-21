from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["GEMINI_API_KEY"]
user_prompt = "Describe a pizza in one sentence"
client = genai.Client(api_key=API_KEY)

print("="*80)
print("System Prompt: You are a fancy food critic")
print("="*80)
response2 = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=user_prompt,
    config=types.GenerateContentConfig(
        system_instruction="You are a sophisticated fine dining food critic. Use fancy culinary terms, discuss flavor profiles, and sound like you know fancy restaurants."
    )
)
print(response2.text)