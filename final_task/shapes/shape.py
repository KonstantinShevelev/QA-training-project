# shapes/shape.py

import math


class Shape:
    def __init__(self, color: str):
        self._color = color

    def get_area(self) -> float:
        # Заглушка: переопределяется в дочерних классах
        return 0.0

    def get_perimeter(self) -> float:
        # Заглушка: переопределяется в дочерних классах
        return 0.0

    def __str__(self) -> str:
        return f"Shape (Color: {self._color})"
