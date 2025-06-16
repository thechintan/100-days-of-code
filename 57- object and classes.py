class person:
    name="Hari"
    occupation="God"
    networth="Infinite"
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a=person()
b=person()
c=person()
a.name="Shubham"
a.occupation="Accountant"

b.name="Nikita"
b.occupation="HR"
# print(a.name) #if a.name is defined then shubham otherwise hari'll be printed
a.info()
b.info()
c.info()