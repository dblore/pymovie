import requests
from bs4 import BeautifulSoup

def film_names():
    global filmURL
    
    URL = "https://www.imdb.com/calendar?region=GB&ref_=rlm"
    mainPage = requests.get(URL)
    
    home = BeautifulSoup(mainPage.content, 'html.parser')

    index = home.find(id="main")
    links = index.find_all('a')

    for link in links:
        title = link.text
        url = link.get('href')
        filmURL = "https://www.imdb.com" + url
        print("{}: {}".format(title, filmURL))

def main():
    film_names()

if __name__ == "__main__":
    main()