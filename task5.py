import json
from task1 import scrape_top_list
from task4 import  movie_details

with open("mytask1.json","r") as file:
    data = json.load(file)

movies=scrape_top_list()
def get_movie_list_details():
    list=[]
    for i in data:
        a=i["URL"]
        # print(a)
        b= movie_details(a)
        list.append(b)
        # print(list)
    with open ("task5.json", "w+") as f:
        json.dump(list,f, indent=4)
    return list
get_movie_list_details()  


# import requests
# from bs4 import BeautifulSoup
# import json
# from task1 import scrape_top_list
# from task4 import movie_details
# movie=scrape_top_list()
# # ten_movies=movie[1:]
# def get_movie_detailes():
#     details=[]
#     for i in movie:
#         t=i["URL"]
#         # print(t,"kkkkkkkkkkkkkkkk")
#         a=movie_details(t)
#         # print(a,"jjjjjjjj")
#         details.append(a)
#         print(details)
#     with open("task5.json","w+") as file:
#         json.dump(details,file,indent=4)           
# get_movie_detailes()