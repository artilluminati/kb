import random


def getRand(a: int, b: int):
    randVal = random.randint(a, b)
    return randVal


def getRandYield(a: int, b: int):
    while True:
        randVal = random.randint(a, b)
        yield randVal

a = int(input("от: "))
b = int(input("до: "))

print(getRand(a, b))

print(next(getRandYield(a, b)))