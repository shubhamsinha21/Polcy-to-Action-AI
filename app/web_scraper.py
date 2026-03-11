import requests
from bs4 import BeautifulSoup
import json
import urllib3

from pdf_extractor import extract_scheme_from_policy, save_scheme_to_db

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def fetch_policy_pages():

    urls = [
        "https://pmkisan.gov.in/",
        "https://dbtagriculture.bihar.gov.in/",
        "https://www.india.gov.in/"
    ]

    pages = []

    for url in urls:

        try:

            response = requests.get(url, timeout=10, verify=False)

            soup = BeautifulSoup(response.text, "lxml")

            text = soup.get_text()

            pages.append(text[:4000])

        except Exception as e:

            print("Scraping error:", e)

    return pages


def create_basic_scheme(text):

    return {
        "scheme_name": "Discovered Government Scheme",
        "occupation": "Farmer",
        "income_limit": 500000,
        "state": "All",
        "land_required": False,
        "benefit": text[:120],
        "documents": ["Aadhaar"],
        "deadline": "Rolling",
        "apply_link": "https://india.gov.in"
    }


def discover_new_schemes():

    pages = fetch_policy_pages()

    added = []

    for page in pages:

        try:

            scheme_json = extract_scheme_from_policy(page)

            result = save_scheme_to_db(scheme_json)

            if result is True:

                added.append(scheme_json)

        except:

            basic_scheme = create_basic_scheme(page)

            save_scheme_to_db(json.dumps(basic_scheme))

            added.append(basic_scheme)

    return added