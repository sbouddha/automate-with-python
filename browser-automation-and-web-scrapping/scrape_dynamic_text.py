from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

URL = "https://automated.pythonanywhere.com/"
XPATH_TEXT_LOC = '/html/body/div[1]/div/h1[2]'


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


def get_whole_line():
    driver = get_driver()
    time.sleep(2)
    fetch_text = driver.find_element(By.XPATH, XPATH_TEXT_LOC)
    return fetch_text.text


def get_num():
    whole_line = get_whole_line()
    get_dyn_num = int(whole_line.split(":")[-1].strip())
    print(get_dyn_num)


get_num()
