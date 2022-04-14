from task1 import scrape_top_list
import json
file=open("mytask1.json","r")
data=json.load(file)
# print(data)

def group_by_year(movies):
    d={}
    for i in data:
        top_m_list=[]
        year=i['Year']
        # print(year)
        if year not in d:
            for key in data:
                if year==key['Year']:
                    # print(year)
                    top_m_list.append(key)
            d[year]=top_m_list 
            print(d)
    with open("mytask2.json","w+") as f:
        json.dump(d,f,indent=4) 
        a=json.dumps(d)
group_by_year(movies=scrape_top_list)        

