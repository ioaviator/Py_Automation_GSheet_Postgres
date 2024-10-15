import csv

import lxml
import requests
from bs4 import BeautifulSoup


def extract():

    url = "https://docs.google.com/spreadsheets/d/1UK8mr6wzSlAYiopCwOO3Va8ekINX52BGty_V-qO7q8c/gviz/tq?tqx=out:html&tq&gid=1"

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
