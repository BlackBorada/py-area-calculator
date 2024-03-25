from math import pi
from figure import Figure


class Circle(Figure):
    def __init__(self, radius) -> None:
        if not isinstance(radius, (int,float)):
            raise TypeError("Радиус дожен быть числом.")
        
        if radius <= 0:
            raise ValueError("Радиус круга не может быть 0 или отрицательным.")
        
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2