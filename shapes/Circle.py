import math

from Shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # метод расчета площади
    def area(self):
        return math.pi * self.radius ** 2
