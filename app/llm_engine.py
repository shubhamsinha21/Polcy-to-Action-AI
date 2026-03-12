import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_KEY = st.secrets("GROQ_API_KEY")

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
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.3,
                "max_tokens": 300
            },
            timeout=30
        )

        data = response.json()

        if "choices" in data:
            return data["choices"][0]["message"]["content"]

        return f"Groq API Error: {data}"

    except Exception as e:
        return f"Request failed: {str(e)}"


# ⭐ NEW FUNCTION (FOR COPILOT)
def call_llm(prompt):
    return ask_llm(prompt)


def explain_eligibility(user, scheme):

    prompt = f"""
You are a government policy advisor.

User profile:
Occupation: {user['occupation']}
State: {user['state']}
Income: {user['income']}
Land Owned: {user['land_owned']}

Scheme:
{scheme['scheme_name']}

Benefit:
{scheme['benefit']}

Explain clearly why the user qualifies for this scheme.
Keep the explanation simple and practical.
"""

    return ask_llm(prompt)