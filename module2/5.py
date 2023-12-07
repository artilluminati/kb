class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Имя:", self.name, "\nВозраст:", self.age, "\nПол:", self.gender)

person1 = Human("Кондратий", 25, "мужской")
person2 = Human("Глаша", 30, "женский")

person1.introduce()
person2.introduce()