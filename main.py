import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/calendar?region=GB&ref_=rlm"
baseURL = "https://www.imdb.com"
mainPage = requests.get(URL)

home = BeautifulSoup(mainPage.content, 'html.parser')

main = home.find(id="main")
links = main.find_all('a')
dates = main.find_all('h4')

for link in links:
    title = link.text
    url = link.get('href')

    filmURL = "https://www.imdb.com" + url

    filmPage = requests.get(filmURL)
    
    film = BeautifulSoup(filmPage.content, 'html.parser')

    mainFilm = film.find_all('div', {'class': 'subtext'})
    
    for div in mainFilm:
        print (div.find('a')['href'])

    #print("{} - {}".format(title, filmURL))