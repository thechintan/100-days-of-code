####DELETE
# class student:
#     def __init__(self,name):
#         self.name=name
# s1=student('shradha')
# del s1  #deletes s1
# print(s1)



####PRIVATE ATTRIBUTES AND METHOD
# class account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass ##acc pass ni aagal __ lagavva thi private thai jay

# acc1=account("12345","abcde")
# print(acc1.acc_no)
# print(acc1.__acc_pass) #private thayel chhe so error avse


# class account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass ##acc pass ni aagal __ lagavva thi private thai jay

#     def reset_pass(self):
#         print(self.__acc_pass) #class ni andar chhe atle private nai thay

# acc1=account("12345","abcde")
# print(acc1.acc_no)
# print(acc1.reset_pass())




###INHERITANCE::::

# class car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class ToyotaCar(car):
#     def __init__(self,name):
#         self.name=name

# class Fortuner(ToyotaCar):
#     def __init__(self,brand):
#         self.brand=brand

# car1= ToyotaCar("Fortuner")
# car2= ToyotaCar("Priyus")
# print(car1.start())

# car3=Fortuner("diesel")
# car3.start()



# class A:
#     varA="welcome to class A"

# class B:
#     varB="welcome to class B"

# class C(A,B): #A ane B banne ni property inherite kare
#     varC="welcome to class C"

# c1=C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)




##SUPER METHOD 

# class car:
#     def __init__(self,type):
#         self.type=type

#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class ToyotaCar(car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name
#         super().start()

# car1= ToyotaCar("Prius","electric")
# print(car1.type)



##CLASS METHODS
# class person:
#     name="anonymous"

#     def changename(self,name):
#         self.name= name

# p1= person()
# p1.changename("rahulkumar")
# print(p1.name)
# print(person.name)

# class person:
#     name="anonymous"

#     def changename(self,name):
#         person.name= name #OR self.__class__.name ="rahulkumar"

# p1= person()
# p1.changename("rahulkumar")
# print(p1.name)
# print(person.name)

# class person:
#     name="anonymous"

#     @classmethod
#     def changename(cls,name):
#         cls.name=name

# p1= person()
# p1.changename("rahulkumar")
# print(p1.name)
# print(person.name)


# #PROPERTY

# class student:
#     def __init__(self,phy,chem,maths):
#         self.phy=phy
#         self.chem=chem
#         self.maths=maths

#         #def calcpercentage(self):
#         #   self.percentage=str{(self.phy+self.chem+self.maths)/3+"%"}

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem+self.maths)/3)+"%"
# stu1=student(98,97,99)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.percentage)




# ##POLYMORPHISM
# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def showNumber(self):
#         print(self.real,'i +',self.img,'j')

#     def __add__(self,num2):  #__add is a dunder function, it's a logic of addition
#         newReal=self.real+ num2.real
#         newImg = self.img + num2.img
#         return complex (newReal,newImg)

#     def __sub__(self,num2):  #__sub is a dunder function, it's a logic of substraction
#         newReal=self.real-num2.real
#         newImg = self.img - num2.img
#         return complex (newReal,newImg)
    
# num1=complex(1,3) 
# num1.showNumber()     

# num2=complex(4,6)
# num2.showNumber()

# num3= num1+num2
# num3.showNumber()

# num4= num1-num2
# num4.showNumber()


#PRACTICE-Define a circle class to 
#create a circle with radius r
#using the constructor. define an area() method
#of the class which calculates the area of the circle.
#define a perimeter() method of the class which allows
#you to calculate the perimeter of the circle
class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*((self.radius)**2)
    
    def perimeter(self):
        return 2*3.14*self.radius
    
c1=circle(21)
print(c1.area())
print(c1.perimeter())

#Qn- define an employee class with attributes
#role,department and salary.This class also a
#showDetails() method.
#Create an engineer class that inherits properties
#from Employee and has additional attributes:name and age

class employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetails(self):
        print("role =",self.role)
        print("department =",self.department)
        print("salary =",self.salary)

class engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75,000")

e1=employee("accountant","finance","20000")
e1.showDetails()

eng1=engineer("elon musk",57)
eng1.showDetails()


#create a class called order which stores item and its price
#use dunder function __gt__() to convey that:
#order1>order2 if price of order1>price of order2

class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,odr2):
        return self.price>odr2.price
    
odr1=order("chips",20)
odr2=order("tea",15)

print(odr1>odr2)