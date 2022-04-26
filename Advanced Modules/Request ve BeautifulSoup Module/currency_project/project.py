from bs4 import BeautifulSoup
import requests

url = "http://data.fixer.io/api/latest?access_key=2c0387fa0a73518016f612d3bf418328"
response = requests.get(url)
json = response.json()
USD = json["rates"]["USD"]
TR = json["rates"]["TRY"]
total = TR / USD
print(total)