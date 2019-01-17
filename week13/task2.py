class Animal:
    def __init__(self,_name,_type,_legs,_canSwim,_canFly):
        self.c_name = _name # string
        self.c_type = _type # string
        self.c_legs = _legs # int 
        self.c_canSwim = _canSwim # boolean
        self.c_canFly = _canFly # boolean

    def swim(self):
        if self._canSwim:
            print(self._name, "can swim")
        else:
            print(self._name, "cannot swim")

    def fly(self):
        if self._canFly:
            print(self._name, "can fly")
        else:
            print(self._name, "cannot fly")

class Mammal(Animal):
    def __init__(self,_name,_type,_legs,_canSwim,_canFly,_hasHair,_sound):
        super().__init__(_name,_type,_legs,_canSwim,_canFly)
        self.c_hasHair = _hasHair
        self.c_sound = _sound
    
    def speak(self):
        if self.c_sound == "":
            print("No sound")
        else:
            print(self.c_sound)

class Insect(Animal):
    def __init__(self,_name,_type,_legs,_canSwim,_canFly):
        super().__init__(_name,_type,_legs,_canSwim,_canFly)

bird1 = Mammal("Hedwig","owl",2,False,True,True,"Too wit, Too woo")
print(bird1.c_name)
bird1.speak()

butterfly1 = Insect("Butterfree","Blue Morpho",6,False,True,)
print(butterfly1.c_name)





