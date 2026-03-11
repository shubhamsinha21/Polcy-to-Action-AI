import streamlit as st

from rule_engine import check_eligibility, load_schemes
from ranking_engine import rank_schemes
from simulator import simulate_income_change
from llm_engine import explain_eligibility


st.set_page_config(page_title="Policy-to-Action AI", layout="wide")

st.title("🚦 Policy-to-Action AI")
st.subheader("AI-powered Government Scheme Advisor")


# -----------------------------
# USER INPUT SECTION
# -----------------------------

st.header("Enter Your Details")

occupation = st.selectbox(
    "Occupation",
    ["Farmer"]
)

state = st.selectbox(
    "State",
    ["Bihar", "UP", "MP"]
)

income = st.number_input(
    "Annual Income (₹)",
    value=200000
)

land = st.checkbox(
    "Do you own agricultural land?"
)

user = {
    "occupation": occupation,
    "state": state,
    "income": income,
    "land_owned": land
}


# -----------------------------
# SCHEME CHECKER
# -----------------------------

if st.button("Check Eligible Schemes"):

    schemes = check_eligibility(user)

    if not schemes:
        st.warning("No schemes found for this profile.")

    else:

        ranked = rank_schemes(user, schemes)

        st.header("Top Schemes For You")

        for scheme, score in ranked:

            st.subheader(f"{scheme['scheme_name']}  (Score: {score})")

            st.write("**Benefit:**", scheme["benefit"])
            st.write("**Deadline:**", scheme["deadline"])
            st.write("**Apply Here:**", scheme["apply_link"])

            st.write("**Required Documents:**")
            for doc in scheme["documents"]:
                st.write(f"• {doc}")

            explanation = explain_eligibility(user, scheme)

            st.write("**AI Explanation:**")
            st.write(explanation)

            st.divider()


# -----------------------------
# POLICY IMPACT SIMULATOR
# -----------------------------

st.header("Policy Impact Simulator")

new_income = st.number_input(
    "Simulate new income level (₹)",
    value=500000
)

if st.button("Run Simulation"):

    schemes = load_schemes()

    lost, retained = simulate_income_change(user, schemes, new_income)

    st.subheader(f"If income becomes ₹{new_income}")

    st.write("### ❌ Schemes You May Lose")

    if lost:
        for scheme in lost:
            st.write(f"• {scheme}")
    else:
        st.write("None")

    st.write("### ✅ Schemes You Still Qualify For")

    if retained:
        for scheme in retained:
            st.write(f"• {scheme}")
    else:
        st.write("None")