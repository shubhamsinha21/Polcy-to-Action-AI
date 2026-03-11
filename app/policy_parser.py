import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

URL = "https://api.groq.com/openai/v1/chat/completions"


def parse_policy(text):

    prompt = f"""
Convert the following government policy text into structured JSON.

Format:

{{
  "scheme_name": "",
  "states": [],
  "benefit": "",
  "eligibility_rules": [
    {{"field":"","operator":"","value":""}}
  ],
  "documents": [],
  "apply_process": ""
}}

Policy Text:
{text}
"""

    response = requests.post(
        URL,
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    return response.json()["choices"][0]["message"]["content"]