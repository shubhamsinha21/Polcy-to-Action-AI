import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

URL = "https://api.groq.com/openai/v1/chat/completions"

def ask_llm(prompt):

    if not API_KEY:
        return "ERROR: GROQ_API_KEY not found."

    try:
        response = requests.post(
            URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3.1-8b-instant",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3
            }
        )

        data = response.json()

        if "choices" in data:
            return data["choices"][0]["message"]["content"]

        return f"Groq API Error: {data}"

    except Exception as e:
        return f"Request failed: {str(e)}"

def explain_eligibility(user, scheme):

    prompt = f"""
You are a government policy advisor.

User Profile:
{user}

Scheme:
{scheme['scheme_name']}

Benefit:
{scheme['benefit']}

Explain clearly why the user qualifies for this scheme.
Keep the explanation simple.
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