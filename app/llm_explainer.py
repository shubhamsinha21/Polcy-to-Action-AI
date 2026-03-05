import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


def generate_explanation(user_data, scheme):
    if not GROQ_API_KEY:
        return "LLM explanation unavailable. Add GROQ_API_KEY to .env file."

    prompt = f"""
You are a government scheme advisor.

User Profile:
{user_data}

Scheme:
Name: {scheme['scheme_name']}
Benefit: {scheme['benefit']}

Explain clearly in simple language why the user qualifies.
Keep response structured and concise.
"""

    try:
        response = requests.post(
            GROQ_URL,
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-8b-8192",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3
            }
        )

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error generating explanation: {str(e)}"