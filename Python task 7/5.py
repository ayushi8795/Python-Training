class Person:
    def __init__(self,age):
        if age < 0:
            age = 0
            self.age = age
            print("Age is not valid, setting age to 0.")
        else:
            self.age = age
    def amIOld(self):
        if self.age == 0:
            pass
        elif (0 < self.age < 13):
            print("You are young")
        elif (13 <= self.age <= 19):
            print("You are a teenager")
        else:
            print("You are old")
    def yearPasses(self,variable):
        self.variable = variable
        if self.age == 0:
            pass
        else:
            return print(self.variable + self.age)

a = Person(-1)
a.amIOld()
a.yearPasses(3)

