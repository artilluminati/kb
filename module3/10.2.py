import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        print(f"Имя фигуры: {self.name}. Площадь фигуры: неизвестно")

class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__("Прямоугольник")
        self.a = a
        self.b = b

    def area(self):
        print(f"Имя фигуры: {self.name}. Площадь фигуры: {self.a * self.b}")

class Circle(Shape):
    def __init__(self, r):
        super().__init__("Окружность")
        self.r = r

    def area(self):
        print(f"Имя фигуры: {self.name}. Площадь фигуры: {math.pi * self.r ** 2}")

class Curved_trapezoid(Shape):
    def __init__(self):
        super().__init__("Криволинейная трапеция")

def area_of_shape(shape):
    shape.area()

rectangle = Rectangle(2, 5)
circle = Circle(5)
curved_trapezoid = Curved_trapezoid()

area_of_shape(rectangle)
area_of_shape(circle)
area_of_shape(curved_trapezoid)