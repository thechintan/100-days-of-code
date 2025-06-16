class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the name is {self.name}")

class dancer:
    def __init__(self,dance):
        self.dance=dance
    
    def show(self):
        print(f"the dance is {self.dance}")
        
class danceremployee(dancer,employee): #dancer pela so anu pela print thase the dance is garba
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name

o=danceremployee('garba','chintan')
print(o.name,'loves to play',o.dance)
o.show()
print(danceremployee.mro())