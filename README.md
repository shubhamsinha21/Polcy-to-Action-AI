# 🚦 YojanaAI
### AI-powered Government Scheme Discovery & Advisor

YojanaAI is an AI-powered platform that helps citizens discover **government schemes they are eligible for** based on their personal profile such as occupation, income, state, and land ownership.

The system also includes an **AI policy copilot** that answers questions about public policies and government programs.

---

# 🌍 Problem

Many citizens are unaware of government welfare schemes they qualify for.

Challenges include:

- Lack of awareness
- Complex eligibility criteria
- Scattered policy information
- Difficult navigation of government portals

YojanaAI solves this by using **AI + rule-based eligibility analysis** to recommend relevant schemes instantly.

---

# 🚀 Features

### 🔎 Scheme Eligibility Advisor
Users enter basic information:

- Occupation
- State
- Annual income
- Land ownership

The system returns **government schemes they are eligible for**.

---

### 🤖 AI Policy Copilot

Users can ask natural language questions like:

- *Explain PM Kisan Yojana*
- *Loan schemes for entrepreneurs*
- *What is public policy?*

The AI assistant provides **clear explanations using LLMs**.

---

### 📚 Semantic Scheme Search

Search government schemes using natural keywords like:

- `education`
- `loan`
- `krishi`

Powered by **vector search for semantic matching**.

---

# 🧠 Architecture

User Input
↓
Rule Engine (Eligibility Check)
↓
Ranking Engine
↓
AI Explanation (LLM)
↓
Streamlit Dashboard


AI Copilot Flow:


User Question
↓
Intent Detection
↓
Vector Search (Scheme Knowledge Base)
↓
LLM Response (Groq API)


---

# 🛠 Tech Stack

| Component | Technology |
|--------|--------|
Frontend | Streamlit |
Backend | Python |
LLM | Groq API (LLaMA 3) |
Vector Search | FAISS |
Data | JSON Scheme Database |

---

# 📂 Project Structure

yojanaai
│
├── app
│ ├── main.py
│ ├── rule_engine.py
│ ├── ranking_engine.py
│ ├── vector_search.py
│ ├── chat_engine.py
│ └── llm_engine.py
│
├── data
│ └── schemes.json
│
├── requirements.txt
└── README.md


---

# ⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/yojanaai.git

cd yojanaai


Create virtual environment:


python -m venv venv
source venv/bin/activate


Install dependencies:


pip install -r requirements.txt


Add your Groq API key:


GROQ_API_KEY=your_api_key_here


---

# ▶️ Run the Application


streamlit run app/main.py


The app will start at:


http://localhost:8501


---

# 📊 Example Use Cases

### Farmer

Input:


Occupation: Farmer
Income: ₹200000


Output:


PM-KISAN
Kisan Credit Card


---

### Student

Input:


Occupation: Student
Income: ₹50000


Output:


Post Matric Scholarship
National Scholarship Portal


---

# 🌟 Future Improvements

- Real-time scheme scraping from government portals
- Personalized scheme alerts
- Mobile-friendly interface
- Multi-language support
- Integration with government APIs

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve the dataset or features, feel free to open a PR.

---

# 📜 License

MIT License

---

# 👨‍💻 Author

**Shubham Sinha**

AI Engineer | Building AI systems for real-world problems
