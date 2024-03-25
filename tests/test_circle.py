import unittest
from math import pi
from circle import Circle


class TestCircle(unittest.TestCase):
    def test_valid_circle(self):
        self.assertAlmostEqual(Circle(3).area(), 9 * pi)

    def test_invalid_radius_type(self):
        pass

    def test_invalid_radious_value(self):
        pass

if __name__ == '__main__':
    unittest.main()