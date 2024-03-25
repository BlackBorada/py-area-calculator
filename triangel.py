from math import sqrt
from .figure import Figure

class Triangle(Figure):
    def __init__(self, a, b, c) -> None:
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны треугольника должны быть больше 0")
        
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s- self.a) * (s - self.b) * (s - self.c))
    