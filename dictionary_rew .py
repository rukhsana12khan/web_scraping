'one'
# a=["one","two","three","four","five"]
# b=[1,2,3,4,5]
# s={}
# for i in a:
#     for j in b:
#         if i==j:
#             s[i]+=1
#         else:
#             s[i]=1
# print(s)         
'two'
# s={}
# i=0
# while i<=6:
#     a=input("enter your name")
#     b=int(input("enter your no"))
#     s[a]=b
#     i+=1
# print(s)    
"three"
# a="rukhsanarukk"
# s={}
# for i in a:
#     if i in s:
#         s[i]+=1
#     else:
#         s[i]=1
# print(s)        

"four"

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)
# print(dict1)

"five"

# s = {"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}
#         }
#     }
# }
# print(s["class"]["student"]["marks"]["history"]) 

"six"

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# s={}
# for i in employees:
#     s[i]==defaults
# print(s)

"seven"

# employees = {'Kelly':3, 'Emma':5,'rmu':0}
# defaults = {"designation": 'Developer', "salary": 8000}
# # defaults=[2,9,]
# res = dict.fromkeys(employees, defaults)
# print(res)

"eight"

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# sample_dict.pop("age")
# sample_dict.pop("city")
# print(sample_dict)        

"nine"

# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in sample_dict.values():
#     print("200 present in dict")

"ten"

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# sample_dict.popitem()
# # print(sample_dict)
# sample_dict["location"]="new york"
# print(sample_dict)

"eleven"

# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75}
# b=min(sample_dict)
# print(b)

"12"

# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# sample_dict["emp3"]["salary"]=8500
# print(sample_dict)

"13"
# dict1 = {1: "Bitcoin", 2: "Ethereum"}
# a=[]
# a.append(dict1)
# # print(a)
# dict1[3]="rukhsana"
# a.append(dict1)
# print(a)

"14"
# def fun(n):
#     print(n)
#     if n!=10:
#         return fun(n+1)    
# n=int(input("enter"))
# a=fun(n)
# print(a)

"15"
# def num(a,b):
#     def fun():
#         print("hello rukhsana")
#     print("hello prerna")
#     fun() 
#     d=a+b
#     print(d)
# num(4,6)    

"16"
# a=[1,2,3,4,5,6,7,8,9,10,11,12]
# s=[]
# i=0
# while i<len(a):
#     d=[]
#     d.append(a[i])
#     i+=1
#     s.append(d)
# print(s)    

"17"

# user = int(input())
# count = 2
# while(count<user):
#     count = count + 1
#     if count % 5 == 0:
#         print ("wow!! lots of chocolates")
#         count = count + 1
#         break
#     if count % 3 == 0:
#         print ("choco")
#     if count % 7 == 0:
#         print ("late")
#     if count % 11 == 0:
#         print ("chocolate")
#     else:
#         print("not here")
#     count = count + 3
# Count = count + 1
# print (count)

"18"
# for count in range(1, 10):
#     print (count)
# count =+ 1

"19"

# name=input("enter")
# b=name[-1::-1]
# if b==name:
#     print("palindtrom")
# else:
#     print("not palindrom")

"20"
# a="rukhsana"
# count=0
# i=0
# while i<len(a):
#     if a[i]=="a" or a[i]=="i" or a[i]=="o" or a[i]=="e" or a[i]=="u" or a[i]=="A" or a[i]=="E" or a[i]=="I" or a[i]=="O" or a[i]=="U":

#         count+=1
      
#     i+=1
# print(count)   
# 

"21"
   
# d={"a":2,"b":{"c":6,"g":{"d":8}}}      
# a=[]
# for x in d:
#     if type(d[x]) == int:
#         a.append(d[x])
#     elif type(d[x]) == dict:
#         for y in d[x]:
#             if type(d[x][y])==int:
#                 a.append(d[x][y])
#             elif type(d[x][y])==dict:
#                 for z in d[x][y]:
#                     if type(d[x][y][z])==int:
#                         a.append(d[x][y][z])              
# print(a)

"22"
# a=["I am from navgurukul"]
# i=0
# while i<len(a):
#     # print(a[i])
#     b=a[i].split()
#     # print(b)
#     j=0
#     while j<len(b):
#         # print(b[j])
#         k=0
#         count=0
#         while k<len(b[j]):
#             # print(b[j][k])
#             if b[j][k] in b[j]:
#                 count+=1
 
               
#             k+=1
#         print(b[j],"=",count)    
#         j+=1
#     i+=1
     
"23"

# a="my name is rukhsana"
# b=a.split()
# # print(b)
# s={}
# i=0
# count=0
# while i<len(b):
#     count+=1
#     # print(count)
#     s[b[i]]=count
#     i+=1
# print(s)
   

"24"

# d={"a":3,"c":2,"d":{"k":4,"l":{"e":7}}}
# sum=0
# s=[]
# for i in d:
#     if type(d[i])==int:
#         s.append(d[i])
#     elif type(d[i])==dict:
#         for j in d[i]:
#             # print(d[i][j])   
#              if type(d[i][j])==int:
#                  s.append(d[i][j])
#              elif type(d[i][j])==dict:
#                  for k in d[i][j]:
#                     #  print(d[i][j][k]) 
#                     s.append(d[i][j][k])  
# # print(s)
# m=s
# u=0
# while u<len(m):
#     sum+=m[u]
#     u+=1
# print(sum)    

"25"

# a={"a":45,"b":{"c":[55,33],"d":(1,2)}}
# s=[]
# i={}
# for i in a:
#     if type(a[i])==int:
#         s.append(a[i])
#         # print(s)
#     elif type(a[i])==dict:
#         for j in a[i]:
#             # print(a[i][j])   
#             if type(a[i][j])==list:
#                 for k in a[i][j]:
#                     # print(k)
#                    s.append(k)
#                    if type(a[i][j])==tuple:
#                        for n in a[i]
#                        print(k)


# print(s)                   


"26"

# d1={"a":10,"b":6}
# d2={"c":20,"d":33}
# k={}
# for i in d1:
#     k[i]=d1[i]
# for i in d2:
#     k[i]=d2[i]
# print(k)

"27"
# s=[]
# a=int(input("enter"))
# i=0
# d=0
# while a>i:
#     d=(d*10)+(a%10)
#     a=a//10
# s.append(d)
# print(s)    

"28"
# d={}
# a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# for i in a:
#     # print(a[i])
#     for j in a[i]:
#         # print(j)
#         d[i]=j
# print(d)        

"29"
# def fun(a,b):
#     d=a+b
#     print(d)
# def num(r,k):
#     s=(fun(23,8))
#     m=r-k
#     print(m)
# num(90,8)    
"30"

# a=["hello hii","welcomei","RUKHSANA"]
# i=0
# while i<len(a):
#     b=a[i].split()
#     j=0
#     while j<len(b):
#         k=0
#         count=0
#         while k<len(b[j]):
#             if b[j][k] in b[j]:
#                 count+=1
#             k+=1
#         print(b[j],count) 
#         j+=1    
#     i+=1

"31"


# n=int(input("enter"))
# a={}
# i=1
# a[i]=n
# while i<=n:
#     m=[]
#     j=1
#     while j<=10:
#         table=i*j
#         m.append(table)
#         j+=1
#     a[i]=m   
#     i+=1 
# print(a) 

"32"

# a=int(input("enter"))
# i=1
# n=1
# while i<=10:
#     print(a,"*",(n),"=",n*a)
#     i+=1
#     n+=1.5
       
"33"

# a=["pop","123","xyz","121"]
# i=0
# count=0
# while i<len(a):
#     if a[i][0]==a[i][-1]:
#         count+=1
#      i+=1
# print(count)
# 
"34"    

# b=int(input("enter"))
# a=["p","q"]
# i=0
# c=0
# while i<len(a):
#         c=c+1
#         print(c)
#         i+=1
# # print(c)
   

# i=0
# while i<=10:
#     if i%2==0:
#         pass
#     else:
#         print(i)
 #     i+=1   
 # 
 # 
"35"    
# i=1
# while i<=100:
#     b=1
#     count=0
#     while b<=i:
#         if i%b==0:
#             count+=1
#         b+=1
#     if count==2:
#         print("prime",i)
#     i+=1            

"36"
# a=int(input("enter"))
# i=1
# c=0
# while i<=a:
#     if a%i==0:
#         c+=1
#     i+=1
# if c==2:
#     print("prime")

"37"
# a=int(input("enter"))
# i=0
# r=0
# while a>0:
#     r=r*10+(a%10)
#     a=a//10
# print(r)    

"38"
a=input("enter")
b=

        







