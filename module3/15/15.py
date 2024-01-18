import os
import sqlite3
import turtle

if os.path.isfile('coords.db'):
    connection = sqlite3.connect('coords.db')

    cur = connection.cursor()
    data = cur.execute("SELECT * FROM coords")
    data = cur.fetchall()
else:
    print('База данных или таблица отсутствует. Создайте ее с помощью "createdb.py"')


print(data)
class PainterClass(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color = "black"

    def paintCoords(self, x1, y1, x2, y2):
        self.pencolor(self.color)
        self.penup()
        self.goto(x1, y1)
        self.pendown()
        self.goto(x2, y2)


painter = PainterClass()

painter.paintCoords(data['x1'], data['y1'], data['x2'], data['y2'])
turtle.done()
