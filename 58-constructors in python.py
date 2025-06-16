# class person:
#     name= 'Hari'
#     occ='god'

#     def info(self):
#         print(self.name,'is a',self.occ)

# a=person()
# a.info()

# class person:
#     def __init__(self):
#         print("Hey I am a person")

#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# a=person()
# b=person()
#     OR
# class person:
#     def __init__(self,n,o):
#         print("Hey I am a person")
#         self.name= n
#         self.occ= o

#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# a=person('Hari','god')
# b=person('Chintan','Engineer')

class person:
    def __init__(self,n,o):
        print("Hey I am a person")
        self.name= n
        self.occ= o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person('Hari','god')
b=person('Chintan','Engineer')
a.info()
b.info()