import json
# from bs4 import BeautifulSoup
from task5 import get_movie_list_details

language=get_movie_list_details()
def analyse_movies_language():
    dict={}
    for i in language:
        if "Language" in i:
            Language=i["Language"]
            for j in Language:
                if j not in dict:
                    dict[j]=1
                else:
                    dict[j]+=1
                    print(dict)
            else:
                continue
    
    with open("task6.json","w+")as files:
        json.dump(dict,files,indent=4)
analyse_movies_language()