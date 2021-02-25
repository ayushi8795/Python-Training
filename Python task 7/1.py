import math
numbers = input("enter coma separated values: ")
numbers = numbers.split(',')
lst =[]
c = 50
h = 30
class squareroot:
    def __init__(self,numbers):
        self.numbers = numbers
    def calculate(self):
        for d in self.numbers:
            d = int(d)
            x = (2*c*d)/h
            q = math.sqrt(x)
            print(q)
            lst.append(q)
        print(lst)

s = squareroot(numbers)
s.calculate()
