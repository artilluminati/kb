import turtle as t
import random
from time import sleep

attemps = 3
sc = t.Screen()
sc.setup(400, 400)
number = random.randint(1, 10)
print(number)

def main():
    global attemps, number
    while attemps > 0:
        usernum = int(t.textinput("Угадай число", "Ваше число от 1 до 10"))

        attemps -= 1
        if usernum == number:
            t.clear()
            t.write(f"Вы угадали, число {number}", move=False, align='left', font=('Arial', 8, 'normal'))
            sleep(2);
            break
        else:

            t.write(f"Попробуйте снова", move=False, align='left', font=('Arial', 8, 'normal'))

    t.done()


if __name__ == "__main__":
    main()