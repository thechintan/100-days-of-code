class employee:
    def __init__(self):
        self.__name="Chintan"

a=employee()
#print(a.__name) #can't access directly
print(a._employee__name) #can be accessed directly