import unittest

from shapes.Triangle import Triangle


class TestCircle(unittest.TestCase):
    def test_area_5_5_5(self):
        triangle = Triangle(5, 5, 5)
        expected_area = 10.82532
        self.assertAlmostEqual(triangle.area(), expected_area, places=5)

    def test_area_15_125_115(self):
        triangle = Triangle(15, 125, 115)
        expected_area = 669.50892
        self.assertAlmostEqual(triangle.area(), expected_area, places=5)

    def test_area_135_1250_1250(self):
        triangle = Triangle(135, 1250, 1250)
        expected_area = 84251.89144
        self.assertAlmostEqual(triangle.area(), expected_area, places=5)

    def test_area_8_8_11313708(self):
        triangle = Triangle(8, 8, 11.313708)
        expected_area = 32
        self.assertAlmostEqual(triangle.area(), expected_area, places=5)


if __name__ == '__main__':
    unittest.main()