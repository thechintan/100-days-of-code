dic= {
    'jay':20000,
    "ritesh":40000,
    "Chintan":9000000,
    "Harry":3440000      
}

# print(dic)
# print(dic["Chintan"])
# print(dic.get("ritesh")) #dictionary baar ni argument daiye to none print kare,error throw naa kare 
# print(dic.keys())
# print(dic.values())

# for key in dic.keys():
#     print(dic[key])

print(dic.items())
for key,value in dic.items():
    print(f"The value corresponding to tne key {key} is {value} ")

