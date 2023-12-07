import turtle

class House:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def draw_roof(self):
        t = turtle.Turtle()
        t.color(self.color)
        t.pensize(self.size)
        t.penup()
        t.left(90)
        t.forward(200)
        t.pendown()
        t.right(90)
        t.forward(200)
        t.left(120)
        t.forward(200)
        t.left(120)
        t.forward(200)

    def draw_walls(self):
        t = turtle.Turtle()
        t.color(self.color)
        t.pensize(self.size)
        for _ in range(4):
            t.forward(200)
            t.left(90)

    def draw_house(self):
        self.draw_roof()
        self.draw_walls()

house = House("brown", 5)
house.draw_house()

turtle.done()