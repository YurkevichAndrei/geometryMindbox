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

    def test_perimeter_5_5_5(self):
        triangle = Triangle(5, 5, 5)
        expected_perimeter = 15
        self.assertAlmostEqual(triangle.perimeter(), expected_perimeter, places=5)

    def test_perimeter_15_125_115(self):
        triangle = Triangle(15, 125, 115)
        expected_perimeter = 255
        self.assertAlmostEqual(triangle.perimeter(), expected_perimeter, places=5)

    def test_perimeter_135_1250_1250(self):
        triangle = Triangle(135, 1250, 1250)
        expected_perimeter = 2635
        self.assertAlmostEqual(triangle.perimeter(), expected_perimeter, places=5)

    def test_perimeter_8_8_11313708(self):
        triangle = Triangle(8, 8, 11.313708)
        expected_perimeter = 27.313708
        self.assertAlmostEqual(triangle.perimeter(), expected_perimeter, places=5)

    def test_is_right_triangle_5_5_5(self):
        triangle = Triangle(5, 5, 5)
        self.assertFalse(triangle.is_right_triangle())

    def test_is_right_triangle_8_8_11313708(self):
        triangle = Triangle(8, 8, 11.313708)
        self.assertTrue(triangle.is_right_triangle())

    def test_is_right_triangle_135_1250_1250(self):
        triangle = Triangle(135, 1250, 1250)
        self.assertFalse(triangle.is_right_triangle())


if __name__ == '__main__':
    unittest.main()