import turtle


class Shape:
    def draw(self):
        pass


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def draw(self):
        turtle.forward(self.side_length)
        turtle.right(90)
        turtle.forward(self.side_length)
        turtle.right(90)
        turtle.forward(self.side_length)
        turtle.right(90)
        turtle.forward(self.side_length)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        turtle.circle(self.radius)


class Triangle(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def draw(self):
        for _ in range(3):
            turtle.forward(self.side_length)
            turtle.left(120)


# Пример использования
def main():
    square = Square(100)
    circle = Circle(50)
    triangle = Triangle(100)

    turtle.speed(1)

    square.draw()
    circle.draw()
    triangle.draw()

    turtle.done()


if __name__ == "__main__":
    main()