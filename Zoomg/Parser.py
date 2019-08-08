import feedparser
import re
from bs4 import BeautifulSoup
import requests
d = feedparser.parse('https://www.zoomg.ir/category/cinema-news/feed/')
#print(d["entries"][0]["summary"])
data = {}
data_list=[]
sample="https://www.aparat.com"
def getdata():
    for i in range(len(d["entries"])):
        data["title"]=d["entries"][i]["title"]
        data["link"]=d["entries"][i]["link"]
        pic=d["entries"][i]["summary"]
        data["pic"]=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', pic)
        url=data["link"]
        print(data["link"])
        page=requests.get(url)
        soup = BeautifulSoup(page.text,"html.parser")
        for articlebody in soup.find_all("div",{"class":"article-section"}):
            data["article"]=articlebody.text
        for articlesummry in soup.find_all("div",{"class":"article-summery"}):
            data["article_summry"]=articlesummry.text
        for tags in soup.find_all("a",{"itemprop":"keywords"}):
            data["tags"]=tags.text
        data_list.append(data)
    return data_list
def senddata(data):
    import requests

    url = "http://api.thut.ir/bot/posts/"

    headers = {
        'Authentication': "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6IkFsaSIsImV4cCI6MTU2NTMzMTM2MCwiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTU2NTI0NDk2MH0.onfD2oMpudkYr3-Fo1CT0kzFYZ9LJrO4b65pt7mvDfw",
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "507c22ad-2eac-4fa4-82f4-af3686fbf152,f5a8ef68-d55e-46d7-8ece-362e72f9fd13",
        'Host': "api.thut.ir",
        'Cookie': "csrftoken=TtybKH2Td2Qly49dkgWuJ7vvFLzIugYjtnUXvtnkuv1sabk3sX3L5SvYfoTTCs7q",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
print(getdata())

