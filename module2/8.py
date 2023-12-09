import random
import turtle


def check_click(x, y):
  if turtle.distance(x, y) < 50:
    return True


def generate_random_color():
  colors = ["red", "orange", "yellow", "green", "blue", "purple"]
  return random.choice(colors)


class RandomShape:

  def __init__(self):
    self.t = turtle.Turtle()

  def random_circle(self, x, y):
    self.t.penup()
    self.t.goto(x, y)
    self.t.pendown()
    self.t.fillcolor(generate_random_color())
    self.t.begin_fill()
    radius = random.randint(10, 100)
    self.t.circle(radius)
    self.t.end_fill()

  def clear_screen(self, x, y):
    self.t.clear()


# Пример использования класса
rs = RandomShape()

turtle.onscreenclick(rs.random_circle)
turtle.onscreenclick(rs.clear_screen, 3)


def __main__():
  isRunning = True
  while isRunning:
    rs.random_circle(random.randint(-200, 200), random.randint(-200, 200))


if __name__ == __main__():
  __main__()
turtle.mainloop()
