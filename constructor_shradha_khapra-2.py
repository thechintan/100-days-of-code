####constructor####
class student:

    #default constructors-->only self parameter, execute nahi hota
    def __init__(self): #short form of initialization #fullname ni jagya e name lakhiye to pan same output
       print("adding new student in database...")
    
    #parameterized constructors
    def __init__(self, fullname,marks): #short form of initialization #fullname ni jagya e name lakhiye to pan same output
        self.name=fullname
        self.marks=marks
        print("adding new student in database...")
    
s1=student("karn",98)
print(s1.name,s1.marks)  #karan  

s2= student("arjun",87)
print(s2.name,s2.marks)