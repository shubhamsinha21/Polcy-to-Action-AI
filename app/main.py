import streamlit as st

from data_loader import load_schemes
from rule_engine import check_eligibility
from llm_engine import explain_eligibility, parse_user_query
from recommender import recommend_schemes

schemes = load_schemes()

st.title("🚦 Policy-to-Action AI")
st.write("AI-powered Government Scheme Eligibility Checker")

mode = st.radio(
    "Choose Input Mode",
    ["Form Input", "Natural Language"]
)

if mode == "Natural Language":

    query = st.text_input(
        "Describe your situation",
        "I am a farmer from Bihar with income 2 lakh"
    )

    if st.button("Analyze"):

        result = parse_user_query(query)
        st.write("Parsed profile:")
        st.write(result)

else:

    st.subheader("Enter Your Details")

    occupation = st.selectbox(
        "Occupation",
        ["Farmer", "Student", "Business"]
    )

    state = st.selectbox(
        "State",
        ["Bihar", "UP", "Delhi"]
    )

    income = st.number_input(
        "Income",
        min_value=0
    )

    land_owned = st.checkbox("Own agricultural land")

    user_data = {
        "occupation": occupation,
        "state": state,
        "income": income,
        "land_owned": land_owned
    }

    if st.button("Check Schemes"):

        found = False

        for scheme in schemes:

            if "All" not in scheme["states"] and state not in scheme["states"]:
                continue

            eligible, confidence, rule_results = check_eligibility(user_data, scheme)

            if eligible:

                found = True

                st.success(f"Eligible for {scheme['scheme_name']}")

                st.write("Benefit:", scheme["benefit"])
                st.write("Confidence:", confidence)

                st.write("Documents:")
                for doc in scheme["documents"]:
                    st.write("-", doc)

                explanation = explain_eligibility(user_data, scheme)

                st.info(explanation)

        if not found:

            st.warning("No schemes matched")

            rec = recommend_schemes(user_data, schemes)

            if rec:
                st.write("You may explore:")
                for r in rec:
                    st.write("-", r)