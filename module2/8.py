import turtle
import random

class RandomShape:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(1)
        self.t.pensize(3)

    def draw_random_shape(self):
        shape = random.choice(["square", "circle", "triangle"])
        self.t.penup()
        randX = random.randint(-200, 200)
        randY = random.randint(-200, 200)
        self.t.goto(randX, randY)
        self.t.pendown()
        if shape == "square":
            for i in range(4):
                self.t.forward(100)
                self.t.left(90)
        elif shape == "circle":
            self.t.circle(50)
        elif shape == "triangle":
            for i in range(3):
                self.t.forward(100)
                self.t.left(120)

    def clear_screen(self, x, y):
        self.t.clear()
        self.draw_random_shape()

rs = RandomShape()

turtle.onscreenclick(rs.clear_screen, 1)

rs.draw_random_shape()

turtle.mainloop()
