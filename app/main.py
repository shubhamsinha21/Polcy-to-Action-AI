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
    page_icon="🚦",
    layout="wide"
)

# ==========================
# CUSTOM THEME
# ==========================

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F8FAFC;
    }

    h1, h2, h3 {
        color: #1E3A8A;
    }

    .scheme-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }

    .apply-btn {
        background-color: #10B981;
        padding: 8px 14px;
        border-radius: 6px;
        color: white;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("🚦 YojanaAI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🔎 Scheme Advisor",
        "🤖 AI Copilot",
        "📚 Scheme Search"
    ]
)

# ==========================
# HOME PAGE
# ==========================

if page == "🏠 Home":

    st.title("🚦 YojanaAI")

    st.markdown(
        """
AI-powered Government Scheme Advisor.**

### Features

✅ Eligibility-based scheme discovery  
✅ AI explanation of scheme benefits  
✅ AI policy assistant  
✅ Semantic search of government programs
"""
    )

# ==========================
# SCHEME ADVISOR
# ==========================

elif page == "🔎 Scheme Advisor":

    st.title("🔎 Scheme Eligibility Advisor")

    col1, col2 = st.columns(2)

    with col1:

        occupation = st.selectbox(
            "Occupation",
            ["Farmer", "Student", "Entrepreneur", "Other"]
        )

        state = st.selectbox(
            "State",
            ["Bihar", "Uttar Pradesh", "Madhya Pradesh", "All"]
        )

    with col2:

        income = st.number_input(
            "Annual Income (₹)",
            min_value=0,
            value=200000
        )

        land = st.checkbox("Own agricultural land")

    user = {
        "occupation": occupation,
        "state": state,
        "income": income,
        "land_owned": land
    }

    if st.button("🔎 Check Eligible Schemes"):

        schemes = check_eligibility(user)

        if not schemes:

            st.warning("No schemes found for this profile.")

        else:

            ranked = rank_schemes(user, schemes)

            st.subheader("Top Schemes For You")

            for scheme, score in ranked:

                st.markdown(
                    f"""
                    <div class="scheme-card">
                    <h3>{scheme['scheme_name']}</h3>

                    <b>Benefit:</b> {scheme['benefit']} <br>
                    <b>Deadline:</b> {scheme['deadline']} <br>
                    <b>Score:</b> {score} <br><br>

                    <b>Documents Required:</b>
                    <ul>
                    {''.join([f"<li>{doc}</li>" for doc in scheme['documents']])}
                    </ul>

                    <a href="{scheme['apply_link']}" target="_blank" class="apply-btn">
                    Apply Here
                    </a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                explanation = explain_eligibility(user, scheme)

                st.info(explanation)

# ==========================
# AI POLICY COPILOT
# ==========================

elif page == "🤖 AI Copilot":

    st.title("🤖 AI Policy Copilot")

    st.write("Ask questions about government schemes and policies.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_message = st.text_input("Ask your question")

    if st.button("Send"):

        response = run_policy_chat(user_message)

        st.session_state.chat_history.append(("user", user_message))
        st.session_state.chat_history.append(("assistant", response))

    for role, msg in st.session_state.chat_history:

        if role == "user":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)

# ==========================
# SCHEME SEARCH
# ==========================

elif page == "📚 Scheme Search":

    st.title("📚 Search Government Schemes")

    query = st.text_input("Search schemes")

    if st.button("Search"):

        results = search_schemes(query)

        for r in results:

            st.markdown(
                f"""
                <div class="scheme-card">
                <h3>{r['scheme_name']}</h3>
                <p>{r['benefit']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )