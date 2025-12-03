import json
from pathlib import Path

import requests

from bs4 import BeautifulSoup, Tag


def open_soup_menu(catalog_url: str) -> list[Tag]:
    response = requests.get(catalog_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    return soup.select(".rugaciuni .text a")


def main() -> None:
    # Starters are said at the beginning of each prayer, so we'll only need that once
    starter_url = "https://doxologia.ro/rugaciuni-care-se-citesc-inainte-de-orice-acatist"
    catalog_url = "https://doxologia.ro/acatiste"

    menu: list[Tag] = open_soup_menu(catalog_url)

    # Prepare content
    content = {
        starter_url: "Rugăciuni care se citesc înainte de orice Acatist",
        **{item.get("href"): item.text.strip() for item in menu}
    }

    print("Fetch catalog...")
    with open("catalog.json", "w") as f:
        json.dump(content, f)
    print("Saved to file! (`catalog.json`) ✅")


if __name__ == '__main__':
    if Path("catalog.json").exists():
        print(
            "Catalog already present. If you want to refetch it, please delete `catalog.json` file and rerun.\n"
            " -> Overwrite is disallowed on purpose to avoid losing custom catalog.\n"
            " -> Run `save_book.py` script to download catalog content.\n"
        )
    else:
        main()
