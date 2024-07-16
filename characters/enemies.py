import random
# enemy classes


class Enemy:

    def base_attack(self, player):
        print("-------------------ENEMY ATTACKS!-------------------")
        random_number = random.randint(100, 3000)
        damage = (self.atk + random_number) - player.armor
        player.health -= damage
        print(
            f"You received {damage} points of damage. \nHealth is now: {player.health}")

    def show_stats(self):
        print("------------------------------")
        print(
            f"Enemy current stats are: \nAttack: {self.atk} \nArmor: {self.armor} \nHealth: {self.health}")
        print("------------------------------")


class Dark_Knight(Enemy):
    def __init__(self, health=15000, armor=250, atk=300):
        self.health = health
        self.armor = armor
        self.atk = atk


class Hollow_Walker(Enemy):
    def __init__(self, health=10000, armor=500, atk=200):
        self.health = health
        self.armor = armor
        self.atk = atk


class Cursed_Bowman(Enemy):
    def __init__(self, health=8000, armor=150, atk=180):
        self.health = health
        self.armor = armor
        self.atk = atk
