class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
        
    def make_sound(self):
        print("sound made by the animal")

class Dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species="Dog")
        self.breed=breed

    def make_sound(self):
        print("Bark!")

D=Dog("Breuno","German Shepherd")
D.make_sound()

a=animal("Dog","Dog")
a.make_sound()