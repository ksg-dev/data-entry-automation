# Responsible for using selenium to complete google form using bs scraped data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

load_dotenv()

FORM_URL = os.environ["GOOGLE_FORM_URL"]
ADDRESS_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
RENT_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
LINK_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
SUBMIT_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'

class FormFiller:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def fill_form(self, prop_dict):
        address = prop_dict["address"]
        rent = prop_dict["rent"]
        link = prop_dict["link"]

        self.driver.get(FORM_URL)
        time.sleep(2)

        address_field = self.driver.find_element(By.XPATH, value=ADDRESS_XPATH)
        address_field.send_keys(address)

        rent_field = self.driver.find_element(By.XPATH, value=RENT_XPATH)
        rent_field.send_keys(rent)

        link_field = self.driver.find_element(By.XPATH, value=LINK_XPATH)
        link_field.send_keys(link)
        time.sleep(2)

        submit_button = self.driver.find_element(By.XPATH, value=SUBMIT_XPATH)
        submit_button.click()
        time.sleep(3)

        self.driver.quit()



        # print(address)
        # print(rent)
        # print(link)
