import requests
from bs4 import BeautifulSoup

load_url = 'https://www.google.com/search?client=firefox-b-d&q=docker'
data = requests.get(load_url)
html = BeautifulSoup(data.content, 'html.parser')

for element in html.find_all('h3'):
  print(element.text)
