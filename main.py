from characters.enemies import Cursed_Bowman, Dark_Knight, Hollow_Walker
from characters.player import Bowman, Knight, Warrior


# character choice function
def character_choice():
    character_choice = input(
        "Pick a character--> \nWarrior: 1 \nKnight: 2 \nBowman: 3 \n>")

    if character_choice == "1":
        player = Warrior()
        # ask for weapon boost and armor choice
        player.show_stats()
        player.weapon_boost()
        player.choose_armor()
        player.show_stats()
        return player
    elif character_choice == "2":
        player = Knight()
        # ask for weapon boost and armor choice
        player.show_stats()
        player.weapon_boost()
        player.choose_armor()
        player.show_stats()
        return player
    elif character_choice == "3":
        player = Bowman()
        # ask for weapon boost and armor choice
        player.show_stats()
        player.weapon_boost()
        player.choose_armor()
        player.show_stats()
        return player
    else:
        print("Invalid value, try again")


# enemy selection function
def enemy_choice():
    enemy_choice = input(
        "Choose an enemy to fight in the arena--> \
            \nDark Knight:1 \
            \nHollow Walker: 2 \
            \nCursed Bowman: 3 \n>"
    )
    if enemy_choice == "1":
        enemy = Dark_Knight()
        enemy.show_stats()
        return enemy
    elif enemy_choice == "2":
        enemy = Hollow_Walker()
        enemy.show_stats()
        return enemy
    elif enemy_choice == "3":
        enemy = Cursed_Bowman()
        enemy.show_stats()
        return enemy
    else:
        print("invalid choice")


# fighting function
def fight(player, enemy):
    print("-----------------FIGHT!--------------------")
    while player.health >= 0 and enemy.health >= 0:
        atk_mode = input(
            "Choose an attack:\
                \nBase attack (Attack + 1 to 1000 bonus points): 1 \
                \nHeavy Attack(Attack + 500 to 600 bonus points): 2 \
                \nSpecial Attack (Attack + 1000 to 5000 bonus points, with self damage risk): 3 \n>"
        )
        if atk_mode == "1":
            player.base_attack(enemy)
            enemy.base_attack(player)
            player.show_stats()
            enemy.show_stats()
        elif atk_mode == "2":
            player.heavy_attack(enemy)
            enemy.base_attack(player)
            player.show_stats()
            enemy.show_stats()
        elif atk_mode == "3":
            player.special_attack(enemy)
            enemy.base_attack(player)
            player.show_stats()
            enemy.show_stats()
    if player.health >= 0 and enemy.health <= 0:
        print("You defeated the enemy!")
    elif enemy.health >= 0 and player.health <= 0:
        print("The Enemy defeated you!")
    elif player.health <= 0 and enemy.health <= 0:
        print("It's a draw.")


# start
# Character choice
player1 = character_choice()
enemy1 = enemy_choice()

# fight
fight(player1, enemy1)
