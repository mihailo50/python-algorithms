# from bs4 import BeautifulSoup

# import requests, sys

# url = 'http://www.imdb.com/chart/top'

# response = requests.get(url)

# soup = BeautifulSoup(response.text, features='lxml')

# tr = soup.findChildren("tr")
# tr = iter(tr)

# for movie in tr:
#     title = movie.find('td', {'class': 'titleColumn'} ).find('a').contents[0]
#     year = movie.find('td', {'class': 'titleColumn'} ).find('span', {'class': 'secondaryInfo'}).contents[0]
#     rating = movie.find('td', {'class': 'ratingColumn imdbRating'} ).find('strong').contents[0]
#     row = title + ' - ' + year + ' ' + ' ' + rating
 
#     print(row)

try:
    if '1' != 1:
        raise "someError"
    else:
        print("someError has not occured")
except "someError":
    print ("someError has occured")
