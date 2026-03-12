from vector_search import search_schemes
from llm_engine import call_llm


def run_policy_chat(user_query):

    query = user_query.lower()

    # keywords that indicate scheme related questions
    scheme_keywords = [
        "scheme",
        "yojana",
        "kisan",
        "loan",
        "farmer",
        "subsidy",
        "pm",
        "credit card"
    ]

    # check intent
    if any(word in query for word in scheme_keywords):

        schemes = search_schemes(query)

        if not schemes:
            return "No relevant schemes found."

        context = ""

        for s in schemes:
            context += f"""
Scheme: {s['scheme_name']}
Benefit: {s['benefit']}
"""

        prompt = f"""
You are a government policy assistant.

Use the schemes below to answer the question.

User Question:
{user_query}

Schemes:
{context}

Explain clearly and simply.
"""

        return call_llm(prompt)

    else:

        # general knowledge question
        prompt = f"""
You are a helpful policy assistant.

Answer this question clearly:

{user_query}
"""

        return call_llm(prompt)