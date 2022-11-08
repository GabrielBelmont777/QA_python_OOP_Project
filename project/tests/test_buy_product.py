# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.service import Service
#
# s = Service('C:\\pythonSelenium\\chromedriver.exe')
# driver = webdriver.Chrome(service=s)
#
# driver.get('https://www.saucedemo.com/')
# driver.maximize_window()
# time.sleep(1000)

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from project.pages.cart_page import Cart_page
from project.pages.client_information_page import Client_Information_page
from project.pages.login_page import Login_page
from project.pages.main_page import Main_page
from project.pages.payment_page import Payment_page


def test_buy_product():
    s = Service('/Users/wild_savage777/Desktop/Автоматизированное тестирование/PythonQA/&/chromedriver 2')
    driver = webdriver.Chrome(service=s)
    print("Start Test")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_Information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment()








    time.sleep(10)











