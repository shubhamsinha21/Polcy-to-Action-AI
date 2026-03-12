import streamlit as st

from rule_engine import check_eligibility, load_schemes
from ranking_engine import rank_schemes
from simulator import simulate_income_change
from llm_engine import explain_eligibility
from pdf_extractor import extract_text_from_pdf, extract_scheme_from_policy, save_scheme_to_db
from web_scraper import discover_new_schemes
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
# POLICY IMPACT SIMULATOR
# ==========================

st.header("Policy Impact Simulator")

new_income = st.number_input(
    "Simulate new income level (₹)",
    min_value=0,
    value=500000
)

if st.button("Run Simulation"):

    schemes = load_schemes()

    lost, retained = simulate_income_change(
        user,
        schemes,
        new_income
    )

    st.subheader(f"If income becomes ₹{new_income}")

    st.write("❌ Schemes you may lose:")

    if lost:

        for s in lost:
            st.write(f"• {s}")

    else:

        st.write("None")

    st.write("✅ Schemes you retain:")

    if retained:

        for s in retained:
            st.write(f"• {s}")

    else:

        st.write("None")


# ==========================
# POLICY PDF UPLOAD
# ==========================

st.header("Upload Government Policy")

uploaded_file = st.file_uploader(
    "Upload policy PDF",
    type="pdf"
)

if uploaded_file:

    st.success("PDF uploaded successfully.")

    pdf_text = extract_text_from_pdf(uploaded_file)

    if st.button("Extract Scheme Using AI"):

        scheme_json = extract_scheme_from_policy(pdf_text)

        st.subheader("Extracted Scheme Data")

        st.code(scheme_json)

        if st.button("Save Scheme to Database"):

            result = save_scheme_to_db(scheme_json)

            if result is True:

                st.success("Scheme added successfully!")

            else:

                st.error(result)


# ==========================
# AUTO POLICY DISCOVERY
# ==========================

st.header("Auto Discover Government Schemes")

st.write(
    "Scan government websites and automatically discover new schemes using AI."
)

if st.button("Run AI Policy Discovery"):

    new_schemes = discover_new_schemes()

    if new_schemes:

        st.success(f"{len(new_schemes)} new schemes discovered!")

        for s in new_schemes:

            st.code(s)

    else:

        st.warning("No new schemes discovered.")
        

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