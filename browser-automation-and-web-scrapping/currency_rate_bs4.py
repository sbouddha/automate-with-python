from bs4 import BeautifulSoup
import requests


from_curr = 'NOK'
to_curr = 'INR'
URL = f"https://www.x-rates.com/calculator/?from={from_curr}&to={to_curr}&amount=1"

xpath_rate = '/html/body/div[2]/div/div[3]/div[1]/div/div[1]/div/div/span[2]/text()'

response = requests.get(URL, verify=False).text

soup = BeautifulSoup(response, 'html.parser')
rate_str = (soup.find(class_="ccOutputRslt").text)

rate = (rate_str.split(" ")[0].strip())
print(rate)
