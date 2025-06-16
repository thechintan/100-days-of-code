class employee:
    companyName="APPLE"
    noOfEmployees=0
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02
        employee.noOfEmployees=employee.noOfEmployees + 1
    def showDetails(self):
        print("The name of the employee is",self.name,"and the raise amount in",employee.noOfEmployees,"sized",self.companyName,"is",self.raise_amount)

emp1=employee("HARRY")
emp1.showDetails()

emp2=employee("RAJ")
emp2.raise_amount=0.3
emp2.companyName="MICROSOFT"
emp2.showDetails()

employee.companyName="GOOGLE"
print(employee.companyName)