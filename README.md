## 🚦 Policy-to-Action AI

Government Scheme Eligibility & Decision Engine (Groq + Rule Engine)

## 📌 Problem Statement

- Government schemes are often difficult to understand due to:
- Complex eligibility conditions
- Legal language
- Lack of personalization
- Scattered documentation
- Citizens struggle to determine:
- Whether they qualify
- What documents are required

## How to apply

This project converts structured scheme rules into personalized action plans using a dynamic rule engine and LLM-based explanation layer.

## 🧠 Solution Overview

- Policy-to-Action AI is a modular system that:
- Collects structured scheme eligibility rules
- Accepts user profile input
- Evaluates eligibility dynamically
- Generates structured action plans
- Uses Groq-hosted LLaMA 3 for intelligent explanations

## 🏗 Architecture

User Input
     ↓
Rule Engine (Dynamic Evaluation)
     ↓
Eligible Schemes
     ↓
Groq LLM Explanation Layer
     ↓
Structured Action Plan Output

## ⚙️ Tech Stack

- Python
- Streamlit
- Custom Rule Engine
- Groq API (LLaMA 3)
- JSON-based scheme database

## 🚀 Features

- Dynamic eligibility rule evaluation
- Confidence scoring
- Modular architecture
- LLM-powered explanation layer
- Easily extendable scheme database

## 📂 Project Structure

```
policy-to-action-ai/
│
├── app/
│   ├── main.py
│   ├── rule_engine.py
│   ├── llm_explainer.py
│
├── data/
│   └── schemes.json
│
├── requirements.txt
├── .env.example
└── README.md
```


### ▶️ How to Run

```
git clone <your-repo-url>
cd policy-to-action-ai
pip install -r requirements.txt

Create .env file:

GROQ_API_KEY=your_key_here

Run:

streamlit run app/main.py
```

## 🧪 Example Use Case

Input:

- Occupation: Farmer

- Land Owned: Yes

- Income: ₹200000

Output:

- Eligible schemes

- Benefit details

- Required documents

- Application steps

- AI-generated explanation