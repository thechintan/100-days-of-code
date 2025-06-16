class employee:
    company="Apple"

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    def changeCompany(self,newComapny):
        self.company=newComapny

e1=employee()
e1.name="harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(employee.company)


class employee:
    company="Apple"

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(self,newComapny):
        self.company=newComapny

e1=employee()
e1.name="harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(employee.company)