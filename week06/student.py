
#Student class

class Student:
    #instance attribute
    def __init__(self, name, major):
        self.name = name
        self.major = major

    #instance method
    def school(self, school):
        return "{}, major {}, studies at {}".format(self.name, self.major, school)

    def play(self):
        return "{} is playing badminton".format(self.name)

s1 = Student("Charlie", "IT")


print(s1.school("HANU"))
print(s1.play())
