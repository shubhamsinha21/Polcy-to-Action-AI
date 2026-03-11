import json
from llm_engine import ask_llm
from rule_engine import check_eligibility
from ranking_engine import rank_schemes


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

    user = extract_user_profile(message)

    if not user:
        return "Sorry, I could not understand your profile."

    schemes = check_eligibility(user)

    if not schemes:
        return "No schemes found for your profile."

    ranked = rank_schemes(user, schemes)

    result = "Here are the best schemes for you:\n\n"

    for scheme, score in ranked[:3]:

        result += f"{scheme['scheme_name']}\n"
        result += f"Benefit: {scheme['benefit']}\n\n"

    return result