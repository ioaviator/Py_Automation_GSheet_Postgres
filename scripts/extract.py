import csv
from typing import List, Tuple

import lxml
import requests
from bs4 import BeautifulSoup


def extract(url: str) -> Tuple[List[str], List[List[str]]]:

    html = requests.get(url).text

    soup = BeautifulSoup(html, "lxml")

    table: List = soup.find("table")
    # Extract the headers
    headers: List[str] = [
        header.get_text(strip=True) for header in table.find_all("tr")[0].find_all("td")
    ]

    # Extract the rows
    rows = []
    for row in table.find_all("tr")[1:]:
        cols = [col.get_text(strip=True) for col in row.find_all("td")]
        rows.append(cols)

    return (headers, rows)
