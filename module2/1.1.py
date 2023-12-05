import turtle

def draw_square():
    t = turtle.Turtle()
    for _ in range(4):
        t.forward(100)
        t.right(90)
    turtle.done()

def get_user_data():
    full_name = input("Введите ваше ФИО: ")
    email = input("Введите вашу почту: ")
    phone_number = input("Введите ваш номер телефона: ")
    return full_name, email, phone_number

draw_square()
user_data = get_user_data()
print(user_data)