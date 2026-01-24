# shapes/circle.py

from .shape import Shape  # файл внутри пакета shapes/
import math


class Circle(Shape):
    def __init__(self, color: str, radius: float):
        super().__init__(color)

        if radius <= 0:
            raise ValueError("Radius must be positive")

        self._radius = radius

    def get_area(self) -> float:
        return math.pi * (self._radius ** 2)

    def get_perimeter(self) -> float:
        return 2 * math.pi * self._radius

    def __str__(self) -> str:
        return f"Circle ({self._color}) | R: {self._radius}"
