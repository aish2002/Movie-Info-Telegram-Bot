import requests
import re
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import itertools
#url1='https://www.imdb.com/chart/top/'
url = 'https://www.imdb.com/search/title/'
#html = urllib.request.urlopen(url)
#soup = BeautifulSoup(html, "html.parser")
genre=input("Genre: ")
r=requests.get(url+'?genres='+genre)
soup=BeautifulSoup(r.text,"html.parser")
title = soup.find('title')
if title.string == 'IMDb: Advanced Title Search - IMDb':
   print("Sorry,No such genre.Try again")
else:
    print(title.string)
#print(soup.prettify())
tags = soup('a')
'''rating = soup.find("span", {"itemprop" : "ratingValue"})
for rate,r in rating.items():
    print(rate)'''
for tag in tags:
    '''if "" in str(tag):
    print(tag)'''
    movie=re.search('<a href=\"/title/.*>(.*?)</a>',str(tag))
    try:
        print(movie.group(1))
    except :
        pass

