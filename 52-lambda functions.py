# def double(x):
#     return x*2
# print(double(5))

#       ==

# double = lambda x: x*2 # x leta hai 2*x return karta hai
# print(double(5))

# avg= lambda x,y,z:(x+y+z)/3
# print(avg(3,5,10))

# def apply(function,value):
#     return 11+function(value)
# cube= lambda x: x*x*x
# print(apply(cube,2))
#         ==
def apply(fn,value):
    return 11+fn(value)
print(apply(lambda x:x*x*x,2))
