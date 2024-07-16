import random
# player classes


class Player:
    def weapon_boost(self):
        weapon_choice = input(
            "Pick a weapon boost for your Character: \nFire-1 \nIce-2 \nArcane-3 \n>")
        if weapon_choice == "1":
            self.atk += 100 + (self.atk*2)
            print(f"your damage increased to {self.atk}")
        elif weapon_choice == "2":
            self.atk += 100 + (self.atk*1.5)
            print(f"your damage increased to {self.atk}")
        elif weapon_choice == "3":
            self.atk += 100 + (self.atk*1.2)
            print(f"your damage increased to {self.atk}")
        else:
            print("invalid choice")

    def choose_armor(self):
        armor_choice = input(
            "Pick extra armor for your Character: \nMagic Armor-1 \nBlessing Armor-2 \nFaith Armor-3 \n>")
        if armor_choice == "1":
            self.armor += 300 + (self.armor * 1.2)
            print(f"your armor increased to {self.armor}")
        elif armor_choice == "2":
            self.armor += 500 + (self.armor * 1.5)
            print(f"your armor increased to {self.armor}")
        elif armor_choice == "3":
            self.armor += 400 + (self.armor * 2)
            print(f"your armor increased to {self.armor}")
        else:
            print("invalid choice")

    def base_attack(self, enemy):
        print("-------------------PLAYER ATTACKS!-------------------")
        random_number = random.randint(1, 1000)
        damage = (self.atk + random_number) - enemy.armor
        enemy.health -= damage
        print(
            f"Enemy received {damage} points of damage. \nHealth is now: {enemy.health}")

    def heavy_attack(self, enemy):
        print("-------------------PLAYER ATTACKS!-------------------")
        random_number = random.randint(500, 600)
        damage = (self.atk + random_number) - enemy.armor
        enemy.health -= damage
        print(
            f"Enemy received {damage} points of damage. \nHealth is now: {enemy.health}")

    def special_attack(self, enemy):
        print("-------------------PLAYER ATTACKS!-------------------")
        random_number = random.randint(1000, 5000)
        damage = ((self.atk*0.40) + random_number) - enemy.armor
        enemy.health -= damage
        print(
            f"Enemy received {damage} points of damage. \nHealth is now: {enemy.health}")
        auto_dmg_indicator = random.randint(0, 1)
        if auto_dmg_indicator == 0:
            self.health -= 800
            print("Your attack backfired and did 400 points of damage")
            print(f"Your health now is {self.health}")
        elif auto_dmg_indicator == 1:
            self.health -= 1500
            print("Your attack backfired and did 800 points of damage")
            print(f"Your health now is {self.health}")

    def show_stats(self):
        print("------------------------------")
        print(
            f"your current stats are: \nAttack: {self.atk} \nArmor: {self.armor} \nHealth: {self.health}")
        print("------------------------------")


class Warrior(Player):
    def __init__(self, health=5000, armor=200, atk=100):
        self.health = health
        self.armor = armor
        self.atk = atk


class Knight(Player):
    def __init__(self, health=4000, armor=300, atk=200):
        self.health = health
        self.armor = armor
        self.atk = atk


class Bowman(Player):
    def __init__(self, health=3000, armor=100, atk=300):
        self.health = health
        self.armor = armor
        self.atk = atk
