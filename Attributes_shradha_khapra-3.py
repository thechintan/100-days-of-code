#Attributes == data,value like name and marks
class student:
    college_name="IITRAM" #2 types of attributes-this one is class attr 
    
    def __init__(self,name,marks): 
        self.name=name  #type 2-object attr
        self.marks=marks
        print("adding new student in database...")
    
s1=student("karn",98)
print(s1.name,s1.marks)  #karan  

s2= student("arjun",87)
print(s2.name,s2.marks)

print(s2.college_name) #or student.college_name


class student:
    college_name="IITRAM"
    name="anonymous" #class attribute, agar kisi student ne apna naam nahi likha to uska naam by default anonymous ho jayega

    def __init__(self,name): 
        self.name=name  #object attr > class attr(in terms of preference)
        print("adding new student in database...")
    
s1=student("karn")
print(s1.name)  #karn will be printed
