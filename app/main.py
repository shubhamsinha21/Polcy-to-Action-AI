import streamlit as st

from rule_engine import check_eligibility, load_schemes
from ranking_engine import rank_schemes
from llm_engine import explain_eligibility
from chat_engine import run_policy_chat
from vector_search import search_schemes


# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Policy-to-Action AI",
    layout="wide"
)

st.title("🚦 Policy-to-Action AI")
st.subheader("AI-powered Government Scheme Advisor")


# ==========================
# USER PROFILE INPUT
# ==========================

st.header("Enter Your Details")

occupation = st.selectbox(
    "Occupation",
    ["Farmer", "Student", "Entrepreneur", "Other"]
)

state = st.selectbox(
    "State",
    ["Bihar", "Uttar Pradesh", "Madhya Pradesh", "All"]
)

income = st.number_input(
    "Annual Income (₹)",
    min_value=0,
    value=200000
)

land = st.checkbox("Do you own agricultural land?")


user = {
    "occupation": occupation,
    "state": state,
    "income": income,
    "land_owned": land
}


# ==========================
# SCHEME ELIGIBILITY CHECKER
# ==========================

st.header("Scheme Eligibility Checker")

if st.button("🔎 Check Eligible Schemes"):
    
    schemes = check_eligibility(user)

    if not schemes:

        st.warning("No schemes found for this profile.")

    else:

        ranked = rank_schemes(user, schemes)

        st.header("Top Schemes For You")

        for scheme, score in ranked:

            st.subheader(f"{scheme['scheme_name']} (Score: {score})")

            st.write("Benefit:", scheme["benefit"])

            st.write("Deadline:", scheme["deadline"])

            st.write("Apply Here:", scheme["apply_link"])

            st.write("Required Documents:")

            for doc in scheme["documents"]:
                st.write(f"• {doc}")

            explanation = explain_eligibility(user, scheme)

            st.write("AI Explanation:")
            st.write(explanation)

            st.divider()


# ==========================
# AI POLICY COPILOT
# ==========================

st.header("🤖 AI Policy Copilot")

st.write("Ask questions about government schemes.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_message = st.text_input("Ask something:")

if st.button("Send"):

    response = run_policy_chat(user_message)

    st.session_state.chat_history.append(("You", user_message))
    st.session_state.chat_history.append(("AI", response))

for role, msg in st.session_state.chat_history:

    if role == "You":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)
        
        
st.header("🔎 Search Government Schemes")

query = st.text_input("Search schemes")

if st.button("Search"):

    results = search_schemes(query)

    for r in results:

        st.subheader(r["scheme_name"])
        st.write(r["benefit"])