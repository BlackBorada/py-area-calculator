from math import sqrt
from figure import Figure

class Triangle(Figure):
    def __init__(self, a, b, c) -> None:
        if not isinstance(a, (int, float)) or \
           not isinstance(b, (int, float)) or \
           not isinstance(c, (int, float)):
            raise TypeError("Стороны должны быть числом.")

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны треугольника должны быть больше 0")
        
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Сумма двух сторон треугольника должна быть больше третьей")
        
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s- self.a) * (s - self.b) * (s - self.c))
    
    def is_right(self):
        sides = sorted([self.a, self.b, self.c])
        return  (sides[0] ** 2 + sides[1] ** 2) == sides[2] ** 2