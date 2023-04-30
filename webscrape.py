import requests
import json
from bs4 import BeautifulSoup

url = "https://www.fandango.com/movies-in-theaters"
r = requests.get(url)

#Creating a BeautifulSoup object and passing the content of the site and the parser library
soup = BeautifulSoup(r.content, 'lxml')

#Collecting all of the postercards available
movieCards = soup.find_all('li', class_ = 'poster-card poster-card__fluid browse-movielist--item')

dict = []

#For loop iterates over all of the collected movieCards and the info collected to their respective attribute in the dictionary
for cards in movieCards:
    movieTitle = cards.find('span', class_ = 'heading-style-1 browse-movielist--title poster-card--title').text
    case = {
        "title": {movieTitle},
        "date": "",
        "time": "",
        "description": "",
        "theater": "",
        "location": ""
    }
    dict.append(case)

jsonString = json.dumps(dict, indent = 4, default = str)

with open("movies.json", "w") as f:
    f.write(jsonString)