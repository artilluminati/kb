class Warrior:
    def __init__(self, name, health, damage):
        self._name = name
        self._health = health
        self._damage = damage

    def attack(self, enemy):
        enemy._health -= self._damage
        print(f"{self._name} атакует {enemy._name} и наносит {self._damage} урона!")

    def is_alive(self):
        return self._health > 0


class Mage:
    def __init__(self, name, health, spell_damage):
        self._name = name
        self._health = health
        self._spell_damage = spell_damage

    def cast_spell(self, enemy):
        enemy._health -= self._spell_damage
        print(f"{self._name} колдует и наносит {self._spell_damage} урона {enemy._name}!")

    def is_alive(self):
        return self._health > 0


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
            print(f"У Мага осталось {mage._health} единиц здоровья.")
        if warrior.is_alive():
            print(f"У Воина осталось {warrior._health} единиц здоровья.")

    if warrior.is_alive():
        print("Воин одержал победу!")
    elif mage.is_alive():
        print("Маг одержал победу!")


if __name__ == "__main__":
    main()
