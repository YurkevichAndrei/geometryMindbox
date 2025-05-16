import math

from shapes.Shape import Shape


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    # метод расчета переметра
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    # метод расчета площади по формуле Герона (по трем сторонам)
    def area(self):
        poluperimeter = self.perimeter() / 2
        return math.sqrt(poluperimeter * (poluperimeter - self.side_a) * (poluperimeter - self.side_b) * (poluperimeter - self.side_c))

    # метод проверки является ли треугольник прямоугольным
    def is_right_triangle(self):
        sides = [self.side_a, self.side_b, self.side_c]
        sides.sort()
        return sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2
