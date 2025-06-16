class employee:
    name="Hari"
    def __len__(self):
        i=0
        for c in self.name:
            i+=1
        return i
e=employee()
print(e.name)
print(len(e))