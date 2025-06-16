#use the newsAPI and the requests module to fetch the daily news related to different topics.
#explore and make application

import requests
import json

query= input("what type of news are you interested in?: ")
# Base URL for NewsAPI
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-05-05&sortBy=publishedAt&apiKey=378129df826546d699b35a6ea69196fb"
r=requests.get(url)
news=json.loads(r.text)
#print(news,type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print('--------------------------------------------')   