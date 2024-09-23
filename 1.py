import random


# Класс Hero
class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    # Метод атаки
    def attack(self, other):
        damage = random.randint(1, self.attack_power)  # Генерация случайного урона
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    # Метод проверки жив ли герой
    def is_alive(self):
        return self.health > 0


# Класс Game
class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    # Метод начала игры
    def start(self):
        print("Начинаем игру 'Битва героев'!")
        print(f"Игрок: {self.player.name} против Компьютера")

        while self.player.is_alive() and self.computer.is_alive():
            self.round()

        self.declare_winner()

    # Метод одного раунда боя
    def round(self):
        # Ход игрока
        self.player.attack(self.computer)
        if self.computer.is_alive():
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")
        else:
            print(f"{self.computer.name} побежден!")
            return

        # Ход компьютера
        self.computer.attack(self.player)
        if self.player.is_alive():
            print(f"У {self.player.name} осталось {self.player.health} здоровья.")
        else:
            print(f"{self.player.name} побежден!")

    # Метод объявления победителя
    def declare_winner(self):
        if self.player.is_alive():
            print(f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")


# Запуск игры
if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
