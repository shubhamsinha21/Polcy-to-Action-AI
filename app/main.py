import streamlit as st
import json
from rule_engine import check_eligibility
from llm_explainer import generate_explanation

# Load scheme data
with open("data/schemes.json", "r") as f:
    schemes = json.load(f)

st.set_page_config(page_title="Policy-to-Action AI", layout="centered")

st.title("🚦 Policy-to-Action AI")
st.write("Personalized Government Scheme Eligibility Engine")

st.divider()

# User Input Section
st.subheader("Enter Your Details")

occupation = st.selectbox("Occupation", ["Farmer", "Student", "Business"])
land_owned = st.checkbox("Do you own agricultural land?")
income = st.number_input("Annual Income (₹)", min_value=0, step=10000)

user_data = {
    "occupation": occupation,
    "land_owned": land_owned,
    "income": income
}

st.divider()

if st.button("Check Eligibility"):

    st.subheader("Eligibility Results")

    found_scheme = False

    for scheme in schemes:
        eligible, confidence = check_eligibility(user_data, scheme)

        if eligible:
            found_scheme = True

            st.success(f"✅ Eligible for {scheme['scheme_name']}")
            st.write(f"**Benefit:** {scheme['benefit']}")
            st.write(f"**Match Confidence:** {confidence*100:.0f}%")

            explanation = generate_explanation(user_data, scheme)
            st.info(explanation)

            st.write("### Required Documents")
            for doc in scheme["documents"]:
                st.write(f"- {doc}")

            st.write("### How to Apply")
            st.write(scheme["apply_process"])

            st.divider()

    if not found_scheme:
        st.error("❌ No matching schemes found based on provided details.")