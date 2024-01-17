class Gamer:
    def it_specialist(self):
        print("Я геймер")

class Designer:
    def it_specialist(self):
        print("Я дизайнер")

class Programmer:
    def it_specialist(self):
        print("Я программист")

gamer = Gamer()
designer = Designer()
programmer = Programmer()

gamer.it_specialist()
designer.it_specialist()
programmer.it_specialist()