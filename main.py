import os

from scripts.extract import extract
from scripts.load_to_csv import load_to_csv


def main(url, filename):
    data = extract(url)
    load_2_csv = load_to_csv(data, filename)

    return load_2_csv


url = "https://docs.google.com/spreadsheets/d/1UK8mr6wzSlAYiopCwOO3Va8ekINX52BGty_V-qO7q8c/gviz/tq?tqx=out:html&tq&gid=1"

filename = "output.csv"

if __name__ == "__main__":
    main(url, filename)
