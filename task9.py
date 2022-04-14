import os
import json
import time
import random

with open ("mytask5.json","r+") as f:
    a=json.load(f)
    # print(a)

    def fun(n):
        print(n)

        for i in a:
            path="//home/admin123/python/web_scraping/task9/9thtask"+i["Name"]+".json"
            if os.path.exists(path):
                pass
            else:
                creat=open(path,"w")
                json.dump(i,creat,indent=4)
            time.sleep(n)  
    b=random.randint(1,3)  
    fun(b)   