import streamlit as st
from rule_engine import check_eligibility, load_schemes
from ranking_engine import rank_schemes
from simulator import simulate_income_change
from llm_engine import explain_eligibility

st.title("🚦 Policy-to-Action AI")
st.subheader("AI-powered Government Scheme Advisor")

occupation = st.selectbox("Occupation", ["Farmer"])
state = st.selectbox("State", ["Bihar", "UP", "MP"])
income = st.number_input("Annual Income", value=200000)
land = st.checkbox("Do you own agricultural land?")

user = {
    "occupation": occupation,
    "state": state,
    "income": income,
    "land_owned": land
}

if st.button("Check Schemes"):

    schemes = check_eligibility(user)

    if not schemes:
        st.warning("No schemes found")
    else:

        ranked = rank_schemes(user, schemes)

        st.header("Top Schemes For You")

        for scheme, score in ranked:

            st.subheader(f"{scheme['scheme_name']} (Score: {score})")
            st.write("Benefit:", scheme["benefit"])
            st.write("Deadline:", scheme["deadline"])
            st.write("Apply:", scheme["apply_link"])

            st.write("Documents:", ", ".join(scheme["documents"]))

            explanation = explain_eligibility(user, scheme)

            st.write("AI Explanation:")
            st.write(explanation)

            st.divider()

st.header("Policy Impact Simulator")

new_income = st.number_input("Simulate income change", value=500000)

if st.button("Run Simulation"):

    schemes = load_schemes()

    lost, retained = simulate_income_change(user, schemes, new_income)

    st.subheader("If income becomes:", new_income)

    st.write("❌ Schemes you may lose:")
    st.write(lost)

    st.write("✅ Schemes you retain:")
    st.write(retained)