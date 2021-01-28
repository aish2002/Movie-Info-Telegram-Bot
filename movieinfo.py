import requests
import re
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import itertools
#url1='https://www.imdb.com/chart/top/'
url = 'https://www.imdb.com/find?q='
movie=input("Movie: ")
r=requests.get(url+movie+'&ref_=nv_sr_sm')
soup=BeautifulSoup(r.text,"html.parser")
title = soup.find('title')
#print(title.string)
#print(soup.prettify())
tags = soup('a')
pre_url=""
count=0
lis=[]
for tag in tags:
    if(count>2):
        break
    m=re.search('<a href=.*>(.*?)</a>',str(tag))
    try:
        #if(str(m.group(1)).lower()==movie.lower()):
        link=re.search('/title/(.*?)/',str(m))
        new_url='https://www.imdb.com'+str(link.group(0))
        #print(new_url)
        if new_url!=pre_url:
            html=requests.get(new_url)
            soup2=BeautifulSoup(html.text,"html.parser")
            movietitle=soup2.find('title').string.replace('- IMDb',' ')
            a=soup2('a')
            span=soup2('director')
            for item in span:
                print(item)
            #print("Genre : ",end=" ")
            genrestring="Genre : "
            for j in a:
                genre=re.search('<a href=\"/search/title\?genres=.*> (.*?)</a>',str(j))
                try:
                   # print(genre.group(1),end=" ")
                   genrestring+=genre.group(1)+' '
                  # str=genre.group(1)
                   #print(str)
                except:
                    pass
            atag=soup2('strong')
            for i in atag:
                rating=re.search('<strong title=\"(.*?) based',str(i))
                try:
                    #print("\nIMDb Rating : "+rating.group(1))
                    rstring="IMDb Rating : "+rating.group(1)
                except:
                    pass
            #print("For more details : "+new_url)
            details="For more details : "+new_url
            lis.append(movietitle)
            lis.append(genrestring)
            lis.append(rstring)
            lis.append(details)
            pre_url=new_url
            count+=1
    except :
        pass
print(*lis,sep='\n')
    