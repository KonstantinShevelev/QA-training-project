# shapes/triangle.py


import math
from .shape import Shape


class Triangle(Shape):
    def __init__(self, color: str, a: float, b: float, c: float):
        super().__init__(color)

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive")

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle! Sum of two sides must be > third.")

        self._a = a
        self._b = b
        self._c = c

    def get_perimeter(self) -> float:
        return self._a + self._b + self._c

    def get_area(self) -> float:
        s = self.get_perimeter() / 2
        return math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))

    def __str__(self) -> str:
        return f"Triangle ({self._color}) | Sides: {self._a}, {self._b}, {self._c}"