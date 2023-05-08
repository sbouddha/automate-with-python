from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
from datetime import datetime as dt

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


def clean_text(text):
    get_dyn_num = float(text.split(":")[-1].strip())
    return get_dyn_num


def write_file(text):
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)


def main():
    driver = get_driver()
    while True:
        time.sleep(2)
        whole_text_line = driver.find_element(By.XPATH, XPATH_TEXT_LOC)
        text = str(clean_text(whole_text_line.text))
        write_file(text)


main()
