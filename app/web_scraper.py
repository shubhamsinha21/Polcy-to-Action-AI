import requests
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings("ignore")


def discover_new_schemes():

    urls = [
        "https://www.india.gov.in/my-government/schemes",
        "https://www.nabard.org",
    ]

    discovered = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    for url in urls:

        try:

            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )

            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            links = soup.find_all("a")

            for link in links:

                text = link.text.strip()

                if len(text) > 10 and "scheme" in text.lower():

                    discovered.append(text)

        except Exception:
            continue

    return list(set(discovered))