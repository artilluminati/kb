class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} ест")

    def sleep(self):
        print(f"{self.name} спит")

    def work(self):
        print(f"{self.name} работает")

class EsportsPlayer(Human):
    def play_game(self):
        print(f"{self.name} играет")

    def practice(self):
        print(f"{self.name} готовится к турниру")

class GameDesigner(Human):
    def design_game(self):
        print(f"{self.name} разрабатывает дизайн игры")

    def brainstorm(self):
        print(f"{self.name} проводит мозговой штурм")

person1 = Human("Алексей", 25)
player1 = EsportsPlayer("Персострат", 30)
designer1 = GameDesigner("Тролебузина", 28)

person1.eat()
person1.sleep()
person1.work()

player1.eat()
player1.play_game()
player1.practice()

designer1.work()
designer1.design_game()
designer1.brainstorm()