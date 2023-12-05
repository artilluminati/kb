import turtle
import math
import random

t = turtle.Turtle()

a = 200
b = 100
t.speed(0)
t.penup()
t.goto(a, 0)
t.pendown()
for i in range(0, 360, 1):
    radian = math.radians(i)
    x = a * math.cos(radian)
    y = b * math.sin(radian)
    t.goto(x, y)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for _ in range(100):
    t.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    radius = random.randint(10, 50)
    t.goto(x, y-radius)
    t.pendown()
    t.fillcolor(random.choice(colors))
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

turtle.done()