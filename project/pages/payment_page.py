import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from project.base.base_class import Base


class Payment_page(Base):

    def __init__(self, driver, ):
        super().__init__(driver)
        self.driver = driver

    # Locators

    finish_button = "//*[@id='finish']"


    # Getters

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))



    # Actions

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish button")



    # Methods

    def payment(self):
        self.get_current_url()
        self.click_finish_button()
        self.assert_url("https://www.saucedemo.com/checkout-complete.html")

