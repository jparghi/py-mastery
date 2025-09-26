"""OOP examples: classes, inheritance, polymorphism, dataclasses alternative."""

class Shape:
    def area(self) -> float:
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w = w
        self.h = h
    def area(self) -> float:
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r: float):
        self.r = r
    def area(self) -> float:
        from math import pi
        return pi * self.r * self.r

def describe(shape: Shape) -> str:
    return f"{shape.__class__.__name__} area = {shape.area():.2f}"

if __name__ == "__main__":
    print(describe(Rectangle(3, 4)))
    print(describe(Circle(2.5)))
