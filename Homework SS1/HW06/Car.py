
#CAR CLASS
class Car:

    #ATTRIBUTES
    def __init__(self, yearModel, make, speed):
        self.yearModel = yearModel
        self.make = make
        self.speed = speed

    #GET SPEED
    def get_speed(self):
        return self.speed

    def set_speed(self, newSpeed):
        self.speed = newSpeed

    #Add 5 to speed
    def accelerate(self):
       return (self.speed + 5)

    #Substract 5 from speed
    def brake(self):
        return (self.speed - 5)

#TEST
myCar = Car(2020, "BMW", 180)

print("Accelerate speed:")
for i in range(5):
    accSpeed = myCar.accelerate()
    myCar.speed = accSpeed
    print(str(i) + ": " + str(accSpeed))

print("Brake speed: ")
for i in range(5):
    braSpeed = myCar.brake()
    myCar.speed = braSpeed
    print(str(i) + ": " + str(braSpeed))