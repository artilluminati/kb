import turtle
import random

def main():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    turtle.fillcolor(random.choice(colors))
    turtle.pencolor("blue")
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(100, -100)
    turtle.pendown()

    turtle.fillcolor(random.choice(colors))
    turtle.pencolor("red")
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()

    turtle.done()

if __name__ == "__main__":
    main()
