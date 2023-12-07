import turtle

class Hero:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.t = turtle.Turtle()

    def move_forward(self, distance):

        self.t.color(self.color)
        self.t.pensize(self.size)
        self.t.forward(distance)

    def move_backward(self, distance):
        self.t.color(self.color)
        self.t.pensize(self.size)
        self.t.backward(distance)

    def move_left(self, angle):
        self.t.color(self.color)
        self.t.pensize(self.size)
        self.t.left(angle)

    def move_right(self, angle):
        self.t.color(self.color)
        self.t.pensize(self.size)
        self.t.right(angle)

    def draw_object(self, object_type):
        if object_type == "tree":
            self.t.color(self.color)
            self.t.pensize(self.size)
            # Нарисовать дерево
            self.t.left(90)
            self.t.forward(100)
            self.t.right(90)
            self.t.circle(50)
            self.t.penup()
            self.t.right(90)
            self.t.forward(100)
            self.t.left(90)
            self.t.pendown()
        elif object_type == "house":
            self.t.color(self.color)
            self.t.pensize(self.size)
            # Нарисовать дом
            self.t.penup()
            self.t.left(90)
            self.t.forward(100)
            self.t.pendown()
            self.t.right(90)
            self.t.forward(100)
            self.t.left(120)
            self.t.forward(100)
            self.t.left(120)
            self.t.forward(100)
            self.t.left(30)
            for _ in range(4):
                self.t.forward(100)
                self.t.left(90)
            self.t.penup()
            self.t.forward(100)
            self.t.left(90)
            self.t.pendown()

hero = Hero("blue", 3)
hero.move_forward(100)
hero.draw_object("tree")
hero.move_forward(100)
hero.draw_object("house")

turtle.done()