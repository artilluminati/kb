class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Меня зовут {self.name} и мне {self.age}.")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Поздравьте меня с днем рождения! Мне уже {self.age}.")

petr = Human('Петр', 87)

petr.introduce()

petr.celebrate_birthday()