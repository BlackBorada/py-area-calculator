import unittest
from math import pi
from circle import Circle


class TestCircle(unittest.TestCase):
    def test_valid_circle(self):
        self.assertAlmostEqual(Circle(3).area(), 9 * pi)

    def test_invalid_radius_type(self):
        with self.assertRaises(TypeError):
            Circle("test")
        with self.assertRaises(TypeError):
            Circle([3])
        with self.assertRaises(TypeError):
            Circle({3})

    def test_invalid_radious_value(self):
        with self.assertRaises(ValueError):
            Circle(0)
        with self.assertRaises(ValueError):
            Circle(-3)

if __name__ == '__main__':
    unittest.main()