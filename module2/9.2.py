# Текстовая игра "Битва классов"

class Warrior:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, enemy):
        enemy.health -= self.damage
        print(f"{self.name} атакует {enemy.name} и наносит {self.damage} урона!")

    def is_alive(self):
        return self.health > 0


class Mage:
    def __init__(self, name, health, spell_damage):
        self.name = name
        self.health = health
        self.spell_damage = spell_damage

    def cast_spell(self, enemy):
        enemy.health -= self.spell_damage
        print(f"{self.name} колдует и наносит {self.spell_damage} урона {enemy.name}!")

    def is_alive(self):
        return self.health > 0


def main():
    warrior = Warrior("Воин", 100, 20)
    mage = Mage("Маг", 80, 30)

    while warrior.is_alive() and mage.is_alive():
        action = input("Выберите действие для Воина (атака) или Мага (колдовство): ")

        if action.lower() == "атака":
            warrior.attack(mage)
        elif action.lower() == "колдовство":
            mage.cast_spell(warrior)
        else:
            print("Неверное действие! Выберите атаку или колдовство.")

        if mage.is_alive():
            print(f"У Мага осталось {mage.health} единиц здоровья.")
        if warrior.is_alive():
            print(f"У Воина осталось {warrior.health} единиц здоровья.")

    if warrior.is_alive():
        print("Воин одержал победу!")
    elif mage.is_alive():
        print("Маг одержал победу!")


if __name__ == "__main__":
    main()