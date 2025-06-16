#Changing Tuples indirectly

# countries=('Spain','Italy','india','England','germany')
# temp= list(countries)
# temp.append('russia') #adding item
# temp.pop(3)           #Removing item
# temp[2]="Finland"     #Changing item
# countries=tuple(temp)

# print(countries)

# countries1=("Nepal","Afghanistan","SriLanka")
# countries2=("India","Vietnam","China")
# southeastAsia=countries1+countries2
# print(southeastAsia)




tuple1=(0,1,2,3,2,3,1,3,2,3)

#res=tuple1.count(3)  #counts all 3 in tuple
#print('count of 3 in this ttuple is',res)

# res=tuple1.index(3)  #shows index of first 3 in tuple
# print(res)

#res=len(tuple1)

res=tuple1.index(3,4,8)  #4 se 8 tak slicing karke uske bich me 3 dhundhega
print(res)

