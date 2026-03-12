import json

from app.llm_engine import ask_llm
from app.rule_engine import check_eligibility
from app.ranking_engine import rank_schemes
from app.vector_store import search_schemes


def extract_user_profile(message):

    prompt = f"""
Extract the user profile from this message.

Return JSON in this format:

{{
"occupation": "",
"state": "",
"income": number,
"land_owned": true/false
}}

Message:
{message}
"""

    response = ask_llm(prompt)

    try:

        profile = json.loads(response)

        return profile

    except:

        return None


def run_policy_chat(message):

    # Try to extract user profile
    user = extract_user_profile(message)

    # If profile found → run eligibility engine
    if user:

        schemes = check_eligibility(user)

        if not schemes:

            return "No schemes found for your profile."

        ranked = rank_schemes(user, schemes)

        result = "Here are schemes based on your profile:\n\n"

        for scheme, score in ranked[:3]:

            result += f"{scheme['scheme_name']}\n"
            result += f"Benefit: {scheme['benefit']}\n\n"

        return result

    # Otherwise use vector search (RAG)

    results = search_schemes(message)

    result = "Here are relevant schemes:\n\n"

    for s in results:

        result += f"{s['scheme_name']}\n"
        result += f"Benefit: {s['benefit']}\n\n"

    return result