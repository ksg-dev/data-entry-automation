# Responsible for using selenium to complete google form using bs scraped data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

load_dotenv()

FORM_URL = os.environ["GOOGLE_FORM_URL"]

class FormFiller:
    def __init__(self, property_dict):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.property_dict = property_dict

    def fill_form(self, prop_dict):
        prop_dict = self.property_dict
        address = prop_dict["address"]
        rent = prop_dict["link"]
        link = prop_dict["link"]

        self.driver.get(FORM_URL)
