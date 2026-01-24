# shapes/rectangle.py

from .shape import Shape


class Rectangle(Shape):
    def __init__(self, color: str, width: float, height: float):
        super().__init__(color)

        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")

        self._width = width
        self._height = height

    def get_area(self) -> float:
        return self._width * self._height

    def get_perimeter(self) -> float:
        return 2 * (self._width + self._height)

    def __str__(self) -> str:
        return f"Rectangle ({self._color}) | {self._width} x {self._height}"
