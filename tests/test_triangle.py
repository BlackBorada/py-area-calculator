import unittest
from triangel import Triangle

class TestTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertAlmostEqual(Triangle(3,4,5).area(), 6)

    def test_ivalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(0, 4, 5)
        with self.assertRaises(ValueError):
            Triangle(3, -4, 5)
        with self.assertRaises(ValueError):
            Triangle(3, 4, 0)

    def test_degenerate_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 2)


if __name__ == '__main__':
    unittest.main()
