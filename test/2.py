
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

age = int(input("Введите возраст: "))
age_category = determine_age_category(age)
print("Ваша категория:", age_category)