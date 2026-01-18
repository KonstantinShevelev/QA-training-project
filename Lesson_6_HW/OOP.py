class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
        else:
            print("Error: Value must be over 0!")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value > 0:
            self.__height = value
        else:
            print("Error: Value must be over 0!")

    def __str__(self):
        return f"Rectangle {self.width}x{self.height}"

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return (self.width * self.height) + (other.width * other.height)
        return NotImplemented

rect1 = Rectangle(5, 4)
print(rect1.height)
rect2 = Rectangle(10, 2)
rect3 = Rectangle(10,0)
print(rect1)
print(rect1 + rect2)
rect1.width = -5
print(rect2.width)
rect2.width = 20
print(rect2.width)