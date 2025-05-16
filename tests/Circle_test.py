import unittest
import math

from shapes.Circle import Circle


class MyTestCase(unittest.TestCase):
    def test_area_5(self):
        r = 5
        circle = Circle(radius=r)
        expected_area = 78.53982
        self.assertAlmostEqual(circle.area(), expected_area, places=5)

    def test_area_125(self):
        r = 125
        circle = Circle(radius=r)
        expected_area = 49087.38521
        self.assertAlmostEqual(circle.area(), expected_area, places=5)

    def test_area_13_5(self):
        r = 13.5
        circle = Circle(radius=r)
        expected_area = 572.55526
        self.assertAlmostEqual(circle.area(), expected_area, places=5)


if __name__ == '__main__':
    unittest.main()

