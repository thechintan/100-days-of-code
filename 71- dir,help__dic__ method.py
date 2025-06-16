#dir
x= (1,2,3)
print(dir(x))
print(x.__add__)

#__dict__
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p=person("John",30)
print(p.__dict__) #output as a dictionary

#help
print(help(str))
print(help(person))