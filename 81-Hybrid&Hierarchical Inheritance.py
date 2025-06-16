#Hybrid inheritance--
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass



#Hierarchical--
#Hiarchy--       CEO
#                 |
#        -----------------------
#        |          |          |
#    manager1   manager2    manager3
#        |          |          |
#     ------    --------     --------
#     |    |    |      |     |      |
#  empl1  emp2  emp3  emp4  emp5   emp6

class baseclass:
    pass

class D1(baseclass):
    pass

class D2(baseclass):
    pass

class D3(D1):
    pass