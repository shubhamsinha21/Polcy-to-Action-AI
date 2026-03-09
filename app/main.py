import streamlit as st
from rule_engine import check_eligibility
from llm_explainer import generate_explanation
from data_loader import load_schemes

schemes = load_schemes()

st.set_page_config(page_title="Policy-to-Action AI")

st.title("🚦 Policy-to-Action AI")
st.write("AI-powered Government Scheme Eligibility Checker")

st.divider()

st.subheader("Enter Your Details")

name = st.text_input("Name")

occupation = st.selectbox(
    "Occupation",
    ["Farmer", "Student", "Business"]
)

state = st.selectbox(
    "State",
    ["Bihar", "Uttar Pradesh", "Delhi", "Other"]
)

land_owned = st.checkbox("Do you own agricultural land?")

income = st.number_input(
    "Annual Income",
    min_value=0
)

user_data = {
    "name": name,
    "occupation": occupation,
    "state": state,
    "land_owned": land_owned,
    "income": income
}

st.divider()

if st.button("Check Eligible Schemes"):

    st.subheader("Results")

    found = False

    for scheme in schemes:

        if "states" in scheme:
            if "All" not in scheme["states"] and state not in scheme["states"]:
                continue

        eligible, confidence, rule_results = check_eligibility(user_data, scheme)

        if eligible:

            found = True

            st.success(f"Eligible for {scheme['scheme_name']}")

            st.write("Benefit:", scheme["benefit"])
            st.write("Confidence:", f"{confidence*100:.0f}%")

            st.write("Documents Required:")
            for doc in scheme["documents"]:
                st.write("-", doc)

            st.write("Application Process:")
            st.write(scheme["apply_process"])

            explanation = generate_explanation(user_data, scheme)

            st.info(explanation)

            st.divider()

    if not found:
        st.error("No schemes matched your profile.")