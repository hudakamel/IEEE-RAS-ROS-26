import math
class Shape:
    def area(self):
        pass  
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
def print_area(shape_object):
    print(shape_object.area())

c = Circle(3)
s = Square(4)
print_area(c)
print_area(s)  