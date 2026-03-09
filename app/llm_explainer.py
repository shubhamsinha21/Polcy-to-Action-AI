import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

URL = "https://api.groq.com/openai/v1/chat/completions"


def generate_explanation(user_data, scheme):

    if not GROQ_API_KEY:
        return "No Groq API key configured."

    prompt = f"""
User Profile:
{user_data}

Government Scheme:
{scheme['scheme_name']}

Benefit:
{scheme['benefit']}

Explain clearly why the user qualifies.
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

    try:
        return response.json()["choices"][0]["message"]["content"]
    except:
        return "LLM explanation unavailable."