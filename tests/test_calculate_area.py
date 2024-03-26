from math import pi
import unittest

from circle import Circle
from figure import Figure
from triangel import Triangle

class TestCalculateArea(unittest.TestCase):
    def test_calculate_area(self):
        class TestFigure(Figure):
            def area(self):
                return 10
            

        self.assertAlmostEqual(TestFigure("Test").area(), 10)
        self.assertAlmostEqual(Figure.calculate_area(Circle(3)), 9 * pi)
        self.assertAlmostEqual(Figure.calculate_area(Triangle(3,4,5)), 6 )
                               


    def test_invalid_type_class_calculate_area(self):
        with self.assertRaises(TypeError):
            Figure.calculate_area(10)


if __name__ == '__main__':
    unittest.main()