import unittest
import math
import random

from shapes.Circle import Circle


class TestCircle(unittest.TestCase):
    def test_area(self):
        for i in range(5):
            print("\nTest Number: ", i+1)
            r = random.randint(1, 1000)
            print(r)
            circle = Circle(radius=r)
            expected_area = math.pi * r ** 2
            self.assertAlmostEqual(circle.area(), expected_area, places=5)


if __name__ == '__main__':
    unittest.main()
