import feedparser
import re
from bs4 import BeautifulSoup
import requests
d = feedparser.parse('https://www.zoomg.ir/category/cinema-news/feed/')
#print(d["entries"][0]["summary"])
data = {}
data_list=[]
sample="https://www.aparat.com"
for i in range(len(d["entries"])):
    data["title"]=d["entries"][i]["title"]
    data["link"]=d["entries"][i]["link"]
    print(data["link"])
    data["tags"]=d["entries"][i]["tags"]
    pic=d["entries"][i]["summary"]
    data["pic"]=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', pic)
    url=data["link"]
    page=requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    for articlebody in soup.find_all("div",{"class":"article-section"}):
        data["article"]=articlebody.text
    for articlesummry in soup.find_all("div",{"class":"article-summery"}):
        data["article_summry"]=articlesummry.text
    for video in soup.find_all("a"):
        print(video)
    data_list.append(data)
print(data_list)

