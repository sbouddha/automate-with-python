from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://automated.pythonanywhere.com/login/"
XPATH_USERNAME = '//*[@id="id_username"]'
XPATH_PASSWORD = '//*[@id="id_password"]'
XPATH_HOME_BUTTON = '/html/body/nav/div/a'


def get_driver():
    # Set options to make browsing easier
    options = Options()
    options.set_preference("excludeSwitches", "enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-feature=AutomaticControlled")

    # Use the options when creating the Firefox driver
    driver = webdriver.Firefox(options=options)
    driver.get(URL)
    return driver


def sign_in():
    driver = get_driver()
    time.sleep(1)
    username_box = driver.find_element(By.XPATH, XPATH_USERNAME)
    password_box = driver.find_element(By.XPATH, XPATH_PASSWORD)

    username_box.send_keys("automated")
    password_box.send_keys("automatedautomated")

    button = driver.find_element(By.CSS_SELECTOR, "form button")
    time.sleep(1)
    button.click()

    # Click home
    home_button = driver.find_element(By.XPATH, XPATH_HOME_BUTTON)
    time.sleep(1)
    home_button.click()


sign_in()
