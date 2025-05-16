import math

from shapes.Shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # метод расчета площади
    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        pass
