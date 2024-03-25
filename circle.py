from math import pi
from .figure import Figure

class Circle(Figure):
    def __init__(self, radius) -> None:
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2