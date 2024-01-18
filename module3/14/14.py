import sqlite3

connection = sqlite3.connect('users.db')

cur = connection.cursor()
cur.execute("CREATE TABLE users (user VARCHAR, password VARCHAR)")

cur.execute('INSERT INTO users (user, password) VALUES ("vasya", "12345678")')

connection.commit()

connection.close()
