import math

from shapes.Shape import Shape


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    # метод расчета переметра
    def perimeter(self):
        return (self.side_a + self.side_b + self.side_c) / 2

    # метод расчета площади по формуле Герона (по трем сторонам)
    def area(self):
        perimeter = self.perimeter()
        return math.sqrt(perimeter * (perimeter - self.side_a) * (perimeter - self.side_b) * (perimeter - self.side_c))
