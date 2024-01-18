import sqlite3
import os

try:
    os.remove("coords.db")
except:
    pass

connection = sqlite3.connect('coords.db')


cur = connection.cursor()

cur.execute("CREATE TABLE coords (x1 INT, y1 VINT, x2 INT, y2 INT)")

def mainLoop():
    command = input("Нажмите чтобы продолжить. Чтобы остановить введите «stop»")
    if command == 'stop':
        return False
    crds = dict(x1=input('x1:'), y1=input('y1:'), x2=input('x2:'), y2=input('y2:'))

    cur.execute(f"INSERT INTO coords (x1, y1, x2, y2) VALUES ({crds['x1']}, {crds['y1']}, {crds['x2']}, {crds['y2']})")



while mainLoop():
    print('Введите новую запись')

connection.commit()