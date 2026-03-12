import pdfplumber
import json
from llm_engine import ask_llm
import fitz
import warnings

warnings.filterwarnings("ignore")


def extract_text_from_pdf(uploaded_file):

    text = ""

    try:

        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        for page in pdf:

            text += page.get_text()

    except Exception:
        pass

    return text


def extract_text_from_pdf(file):

    text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:
            text += page.extract_text() + "\n"

    return text


def extract_scheme_from_policy(pdf_text):

    prompt = f"""
You are a policy analyst.

From the following government policy document text, extract scheme information.

Return JSON in this format:

{{
"scheme_name": "",
"occupation": "Farmer or Student or Business",
"income_limit": number,
"state": "All or state name",
"land_required": true/false,
"benefit": "",
"documents": [],
"deadline": "",
"apply_link": ""
}}

Policy Text:
{pdf_text}
"""

    response = ask_llm(prompt)

    return response


def save_scheme_to_db(json_string):

    try:

        new_scheme = json.loads(json_string)

        with open("data/schemes.json", "r") as f:
            schemes = json.load(f)

        schemes.append(new_scheme)

        with open("data/schemes.json", "w") as f:
            json.dump(schemes, f, indent=2)

        return True

    except Exception as e:

        return str(e)