import os

from dotenv import load_dotenv

from scripts.extract import extract
from scripts.load_to_csv import load_to_csv

load_dotenv()


def main(url, filename):
    data = extract(url)
    load_to_csv(data, filename)

    return


url = os.getenv("URL")
filename = os.getenv("FILENAME")

if __name__ == "__main__":
    main(url, filename)
