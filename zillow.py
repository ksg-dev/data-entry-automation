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


    def get_data(self):
        response = requests.get(ZILLOW_URL)
        content = response.text
        return content

    def make_soup(self):
        content = self.get_data()
        soup = BeautifulSoup(content, "html.parser")
        listing_container = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")


        for item in all_listings:
            prop = item.getText().strip()
            prop.replace("\n\n", "\n")
        # property_dict
        print(all_listings)
        # for each in listings[:5]:
        #     print(each)

zillow = ZillowData()
zillow.make_soup()
