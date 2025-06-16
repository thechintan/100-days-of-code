a=4
b="4"
print(a is b) #exact loacation of object in memory, compares identity
print(a==b,"\n") #compares value

a=[1,2,43]
b=[1,2,43]
print(a is b)
print(a==b,"\n")

a=3
b=3
print(a is b)
print(a==b,"\n")

a="Hari"
b="Hari"
print(a is b)
print(a==b,"\n")

a=(1,2,3)
b=(1,2,3)
print(a is b)
print(a==b,"\n")

a=None
b=None
print(a is b)
print(a==b,"\n")