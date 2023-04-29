import requests
from bs4 import BeautifulSoup

url = "https://www.fandango.com/movies-in-theaters"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
print(soup.prettify())