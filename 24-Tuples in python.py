#Tuples are immutable datatype as strings,Lists are mutable

tup=(1,5,51,872,"Chintan",True)
#tup=(1)  #1 will be taken as integer
#tup=(1,) #type=tuple
print(type(tup),tup)

print (tup[-1])

if 555 in tup:
    print("yes,present")
else:
    print('Absent')

tup2= tup[1:4]
print(tup2)