from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

API_KEY = os.environ["GEMINI_API_KEY"]

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hi my name is Atharva. I love to build systems, I'm a devops engineer. Write a short bio about me."
)

print(response.text)
