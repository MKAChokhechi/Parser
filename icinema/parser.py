import feedparser
from bs4 import BeautifulSoup
import requests
d = feedparser.parse('http://icinema.ir/feed')
data={}
output=[]
for i in range(len(d["entries"])):
    data["title"]=d["entries"][i]["title"]
    data["link"]=d["entries"][i]["link"]
    data["description"]=d["entries"][i]["description"]


    url=data["link"]
    page=requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    description = soup.find('meta', attrs={'property':'og:title'}) and soup.find('meta', attrs={'property':"og:description"}) and soup.find('meta', attrs={'property':"og:image"}) and soup.find('meta', attrs={'name':'keywords'})
    if description:
        description = description.get('content')
    print(description)
    #print(soup)

#print(output)