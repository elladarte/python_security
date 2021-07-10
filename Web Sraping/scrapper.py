from bs4 import BeautifulSoup
import requests

url = ''
site = requests.get(url)

soup = BeautifulSoup(site, 'html.parser')

print(soup.prettify())