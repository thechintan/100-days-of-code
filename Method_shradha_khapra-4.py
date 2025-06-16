# class student:
#     college_name="IITRAM"
    
#     def welcome(self):  #welcome is a METHOD
#         print("welcome student")  

# s1=student()
# s1.welcome()



# # Practice-->create a student class that 
# # takes name and marks of 3 subjects 
# # as arguments in constructor.
# # then create a method to print the average.
# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def average_marks(self):
#         sum=0
#         for i in self.marks:
#             sum=sum+i #99,98,97 is i
#         print(f"hi {self.name} you average score is - {sum/3}")

# s1=student("Chintan",[99,98,97])
# s1.average_marks()

# s1.name="Shradha" #changing attribute's value
# s1.average_marks()



# ##STATIC METHOD-class level method, self ni jarur naa pade
# class student:

#     @staticmethod  #decorator
#     def hello(): 
#         print("hello")  

# s1=student()
# s1.hello()



#create account class with two attributes-
#balance and account no. ..create method for
#debit,credit and printing the money

class account:
    def __init__(self,balance,acc):
        self.balance=balance
        self.account_no=acc

    #debit method
    def debit(self,amount):
        self.balance-=amount #balance=balance-amount
        print(f"Rs. {amount} was debited")
        print("Total balance is Rs. ",self.get_balance())

    def credit(self,amount):
        self.balance=self.balance+amount
        print(f"Rs. {amount} was credited")
        print("Total balance is Rs. ",self.get_balance())

    def get_balance(self):
        return self.balance

acc1=account(10000,123)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)