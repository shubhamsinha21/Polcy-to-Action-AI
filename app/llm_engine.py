import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

URL = "https://api.groq.com/openai/v1/chat/completions"


def ask_llm(prompt):

    response = requests.post(
        URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3
        }
    )

    data = response.json()

    if "choices" in data:
        return data["choices"][0]["message"]["content"]

    return f"Groq Error: {data}"


def explain_eligibility(user, scheme):

    prompt = f"""
User profile:
{user}

Scheme:
{scheme['scheme_name']}

Explain clearly why the user qualifies.
"""

    return ask_llm(prompt)


def parse_user_query(query):

    prompt = f"""
Extract structured user profile from this sentence.

Sentence:
{query}

Return JSON with:
occupation
income
state
land_owned
"""

    return ask_llm(prompt)