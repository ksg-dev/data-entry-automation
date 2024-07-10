# Responsible for scraping zillow clone site and structuring data
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

ZILLOW_URL = os.environ["ZILLOW_CLONE_URL"]


class ZillowData:
    def __init__(self):
        self.data_content = self.get_data()
        self.property_dict = self.make_soup()


    def get_data(self):
        response = requests.get(ZILLOW_URL)
        content = response.text
        return content

    def make_soup(self):
        content = self.get_data()
        soup = BeautifulSoup(content, "html.parser")
        listing_container = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

        all_listings = [listing.getText().strip() for listing in listing_container]

        all_addresses = []
        all_rents = []
        all_links = []
        properties = {}

        # Get all links to property pages
        for item in listing_container:
            link = item.find("a").get("href")
            all_links.append(link)

        # Separate address and rent and append to lists
        for listing in all_listings:
            if "|" in listing:
                first = listing.split(" | ", maxsplit=1)[1]
            else:
                first = listing.split(", ", maxsplit=1)[1]

            address, other = first.split("\n", maxsplit=1)
            next_piece = other.split("$")[1]
            rent = next_piece.split("\n", maxsplit=1)[0].split(" ")[0].strip("/mo").strip("+")

            all_addresses.append(address.strip())
            all_rents.append(f"${rent}")

        for n in range(len(all_addresses)):
            properties[n] = {
                "address": all_addresses[n],
                "rent": all_rents[n],
                "link": all_links[n]
            }

        """
        # properties structured like selenium events dict
        {
            0: {
                "address": 'address-string',
                "rent": '$2,876',
                "link": 'https:iaedfoanewfo'
            },
            1: {
                "address": address - string,
                "rent": $2, 876,
        "link": 'https:iaedfoanewfo'
            },
        }
        """
        return properties


# zillow = ZillowData()
# zillow.make_soup()
