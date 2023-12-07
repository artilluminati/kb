import turtle

t = turtle.Turtle()


for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.getcanvas().postscript(file="drawing.eps")

turtle.done()