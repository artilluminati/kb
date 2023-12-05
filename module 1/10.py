import turtle as t

def main():
    numbers = [int(i)**2 for i in input("Введите последовательность чисел через пробел: ").split()]

    print(numbers)

    t.write(f"{str(numbers)[1:-1]}", move=False, align='left', font=('Arial', 8, 'normal'))

    t.done()

if __name__ == "__main__":
    main()