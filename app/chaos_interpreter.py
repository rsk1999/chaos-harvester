import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_chaos(raw_input):
    response = openai.ChatCompletion.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You extract valuable signals from noise."},
            {"role": "user", "content": raw_input}
        ]
    )
    return response['choices'][0]['message']['content']

def analyze_chaos(raw_input):
    return f"(⚠️ Mock Insight) {raw_input[:40]}... was flagged as strategic noise."
