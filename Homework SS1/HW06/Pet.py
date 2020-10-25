
#PET CLASS
class Pet:
    #ATTRIBUTES
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

    #SETTERS
    def set_name(self, newName):
        self.name = newName

    def set_type(self, newType):
        self.type = newType

    def set_age(self, newAge):
        self.age = newAge

    #GETTERS
    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_age(self):
        return self.age

#TEST
myPet = Pet("Cuties", "Cat", 2)
myPet.name = "BabyBus"
print(myPet.name)