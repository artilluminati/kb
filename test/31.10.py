def checkNum(n):
    if n>0:
        return 'положительное'
    elif n<0:
        return 'отрицательное'
    else:
        return 'равно нулю'

a = int(input())
b = int(input())

sum = a + b

for x in [a,b,sum]:
    print(x, checkNum(x))


def determine_age_category(age):
    if age < 0:
        return "Invalid age"
    elif age < 6:
        return "0+"
    elif age < 12:
        return "6+"
    elif age < 16:
        return "12+"
    elif age < 18:
        return "16+"
    else:
        return "18+"

age = int(input("Enter the age: "))
age_category = determine_age_category(age)
print("The age category is:", age_category)