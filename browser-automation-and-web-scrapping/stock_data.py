import requests

URL = "https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=345427200&period2=1683417600&interval=1d&events=history&includeAdjustedClose=true"
filename = "apple_stocks.csv"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
}

response = requests.get(URL, verify=False, headers=headers)
response.raise_for_status()  # Check if the request was successful

with open(filename, 'wb') as file:
    file.write(response.content)
