import turtle


class GeometricShape:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def draw_circle(self):
        t = turtle.Turtle()
        t.color(self.color)
        t.pensize(self.size)
        t.circle(100)

    def draw_triangle(self):
        t = turtle.Turtle()
        t.color(self.color)
        t.pensize(self.size)
        for _ in range(3):
            t.forward(100)
            t.left(120)

    def draw_square(self):
        t = turtle.Turtle()
        t.color(self.color)
        t.pensize(self.size)
        for _ in range(4):
            t.forward(100)
            t.left(90)


shape = GeometricShape("red", 3)
shape.draw_circle()

shape2 = GeometricShape("blue", 2)
shape2.draw_triangle()

shape3 = GeometricShape("green", 4)
shape3.draw_square()

turtle.done()