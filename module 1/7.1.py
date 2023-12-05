import turtle

def draw_square(color):
    turtle.color(color)
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def draw_circle(color):
    turtle.color(color)
    turtle.circle(50)

def draw_triangle(color):
    turtle.color(color)
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

def main():
    user_color = input("Введите цвет: ")

    turtle.speed(1)

    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    draw_square(user_color)

    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    draw_circle(user_color)

    turtle.penup()
    turtle.goto(200, 0)
    turtle.pendown()
    draw_triangle(user_color)

    turtle.done()

if __name__ == "__main__":
    main()
