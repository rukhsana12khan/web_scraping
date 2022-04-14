# import json
# from bs4 import BeautifulSoup
# from task5 import get_movie_list_details

# director=get_movie_list_details() 
# def analyse_movies_directors():
#     d={}
#     for i in director:
#         # print(i)
#         dir_name=i["Director"]
#         # print(dir_name)
#         for j in dir_name:
#             if j not in d:
#                 dir_name=j
#                 d[j]=1
#             else:
#                 d[j]+=1
#     print(d)
#     with open("task7.json","w+") as file7:
#         json.dump(d,file7,indent=4)
#         return d
# analyse_movies_directors()

from task5 import get_movie_list_details
import json
movie_list = get_movie_list_details() 
def movies_language():
    lan_list=[]
    for i in movie_list:
        if "Director" in i:
    
            for j in i["Director"]:
                lan_list.append(j)
        lan_dict={}
        for i in lan_list:
            if i in lan_dict:
                lan_dict[i]=lan_dict[i]+1
            else:
                lan_dict[i]=1
    with open("task7_.json","w") as file:
        json.dump(lan_dict, file, indent = 4)
movies_language()