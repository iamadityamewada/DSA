# t = (23,45,23,1)
# print(t)

# s = {3,4,2,5,6,7,6,8.1,1}
# print(s)


# dic = {
#     "name":"Aditya",
#     "college":"LNCT",
#     'age':"21"
# }

# print(dic)

# print(dic["age"])
# print(dic.get("com","key not available"))

# slice return slice part of same data types
# tupple unique unordered collection
# set is same like set in math.... unordered 

# dic = {
#     "name":"Aditya",
#     "college":"LNCT",
#     'age':"21",
#     "company":{
#         "name":"tcs",
#         "salary":"11LPA",
#         "Address":{
#             "city":{
#             "name":"Indore"
#         }
#     }
# }
# }

# print(dic["company"]["Address"]["city"])

#dictionary is iterable and return key value in i 

dic = {
    "name":"Aditya",
    "college":"LNCT",
    'age':"21",
    "company":{
        "name":"tcs",
        "salary":"11LPA",
        "Address":{
            "city":{
            "name":"Indore"
        }
    }
}
}

for i in dic:
    print(i, dic[i])

