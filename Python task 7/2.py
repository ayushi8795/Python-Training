#Method overriding example
class Shape:
    def area(self):
        print("The area of shape is: 0 ")

class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        area1 = self.length*self.length
        print("The length of square is: ",area1)

sq = Square(4)
sh = Shape()
sq.area()
sh.area()


