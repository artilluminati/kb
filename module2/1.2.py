import turtle

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

def move_turtle():
    t = turtle.Turtle()
    while True:
        direction = input("Введите направление (вперед, назад, влево, вправо): ")
        distance = int(input("Введите расстояние: "))
        if direction == "вперед":
            t.forward(distance)
        elif direction == "назад":
            t.backward(distance)
        elif direction == "влево":
            t.left(distance)
        elif direction == "вправо":
            t.right(distance)
        else:
            print("Неверное направление")

# Пример использования
print(f'Факториал 5 = {factorial(5)}')
move_turtle()