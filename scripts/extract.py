import csv

import lxml
import requests
from bs4 import BeautifulSoup


def extract(url):

    html = requests.get(url).text

    soup = BeautifulSoup(html, "lxml")

    table = soup.find("table")
    # Extract the headers
    headers = [
        header.get_text(strip=True) for header in table.find_all("tr")[0].find_all("td")
    ]

    # Extract the rows
    rows = []
    for row in table.find_all("tr")[1:]:
        cols = [col.get_text(strip=True) for col in row.find_all("td")]
        rows.append(cols)

    return (headers, rows)
