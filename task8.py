from task1 import scrape_top_list
import json
import os
import requests
t1=scrape_top_list()
# print(t1)
with open("mytask1.json","r+")as file:
    a=json.load(file)
    # print(a)
def text():
    for i in a:
        path="/home/admin123/python/web_scraping/8task/task8"+i["movie_name"]+".text"
        # print(path)
        path=""+i["movie_name"]+".text"
        # print(path)
        if os.path.exists(path):
            pass
        else:
            create=open("/home/admin123/python/web_scraping/8task/task8" + i["movie_name"] + "text","w+")
            b=open(path,"w")
            url=requests.get(i["URL"])
            create1=create.write(url.text)
            create.close()
text()