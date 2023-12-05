from icecream import install
install()

def print_age_name():
    const = 12
    name = str(input('Введите имя: '))
    age = int(input('Введите возраст: '))
    print(f'Вас зовут {name}')
    print(f'Вам {age} лет')
    print(f'Посчитанное значение равно {age * const}')

def task1():
    data = input('Введите информацию о своём хобби:\n')
    print(data)

def task2a(a, b):
    c = a
    a = b
    b = c

    return a, b

def task2b(a, b):
    a, b = b, a

    return a, b


def types(arr):
    for e in arr:
        print(f'{e} : {type(e)}')

if __name__ == '__main__':
    # print_age_name()

    # task1()
    #
    # a = int(input('\nA: '))
    # b = int(input('B: '))
    # ic(task2a(a, b))
    #
    # ic(task2b(a, b))

    a = 145
    b = 'str'
    c = True
    d = [1, 2, 3, 'str']

    types([a, b, c, d])


