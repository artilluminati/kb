import turtle as t

def draw_square():
    for i in range(4):
        t.forward(100)
        t.left(90)

def draw_rect(w, h):
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def main():
    draw_square()

    t.penup()
    t.goto(0, 200)

    t.pendown()
    draw_rect(100, 50)

    t.penup()
    t.goto(100, 200)

    t.pendown()
    draw_rect(200, 50)
    t.done()

if __name__ == "__main__":
    main()