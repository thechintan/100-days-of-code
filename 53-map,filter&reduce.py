# def cube(x):
#     return x*x*x
# l=[1,2,4,6,4,3]
# newl=[]
# for item in l:
#     newl.append(cube(item))
# print(newl)

#     ==
#MAP
# def cube(x):
#     return x*x*x
# l=[1,2,4,6,4,3]
# newl= list(map(cube,l))
# print(newl)

#FILTER
# l=[1,2,4,6,5,3]
# def filter_function(a):
#     return a>3
# newnewl = list(filter(filter_function,l))
# print(newnewl)

#REDUCE
from functools import reduce

numbers=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,numbers)
print(sum)

#logic 1+2=3 newlist=[3,3,4,5] then 3+3
