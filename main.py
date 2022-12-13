import os
from random import randint
import settings

from time import sleep

# Basic Text Adventure Game
# By Andrew Tijerina, 12/2022

# 1.) Welcome player, what is your name?
#   Take input from the player and store as the player name.
#   This will change begin the game and set all intial variables to their default state.

# 2.) Choose your class? (Warrior, Mage, Human, Dark Elf)
#   Each class will have their own strengths and weakness, player can choose to learn more if needed.

# 3.) You have 10 points to apply to your stats, choose wisely
#   Points will be stored in the associated player class and only adjusted when player reachs next level.

# 4.) Each class will start in their home town, and will need to explore using direction inputs.
#   Player will receive basic instructions on navigating and interacting with items and NPCs

# 5.) After receiving the quest, the player will leave the town and capable of being attacked.
#   This will set the player variable to allow attacks on the player and will happen at random.
#   As player progresses, lower level enemies will no longer attack and higher level enemies will.

# 6.) Random events will occur in which the player will need to attack, XP will be calculated and added as necessary
# 7.) Story will drive each individual player towards a goal to reach.
# 8.) Player will have an onboard inventory to collect items dropped by enemies and from chests, etc.
# 9.) World will have a store a market system that player can buy and sell items.
# 10.) Long-term, story will eventually be fleshed out to a 2-D RPG.

# def progress(self, count=0, width=30):
#     left = width * count // 30
#     right = width - left
    
#     tags = "#" * left
#     spaces = " " * right
#     count = f"{count}'s"

#     print("\r[", tags, spaces, "] ", count, sep="", end="", flush=True)

def clear_screen():
    os.system('clear')


class Character():
    def __init__(self) -> None:
        self.name: str = ""
        self.level: int = 0
        self.race: str = ""
        self.health: int = 0
        self.magic: int = 0
        self.energy: int = 0
    



    def do_damage(self, enemy):
        pass

class Player(Character):

    def __init__(self) -> None:
        Character.__init__(self)
        self.level = 1

    def text_input(self) -> str:

        commands = {'help': "Enter a response and navigate through the game, type quit to leave and help to pull up this menu at any time.",
                    'quit': "Until next time!",
                    'status': "Current Status:",
                    'inventory': "Current Inventory:",}

        text = input (">> ")
        text = text.lower()
        text = text.strip()

        for key, value in commands.items():

            if text == key:
                print(value)

        # if text in commands.keys():
        #     print(commands["help"])

        # if text in commands.keys():
        #     print(commands["quit"])
        #     settings.game_started = False

        # if text in commands.keys():
        #     print(commands["status"])
        #     print(f"HP: {player.health}, MP: {player.magic}, Energy: {player.energy}")

        # if text in commands.keys():
        #     print(commands["inventory"])
        #     print("You currently have nothing in your inventory")

        # else:
        #     return text
            
    def set_stats(self, **stats):

        for key, value in stats.items():
            if key == "name":
                self.name = value

            if key == "race":
                self.race = valuehelpo

            if key == "hp":
                self.hp = value

            if key == "mp":
                self.mp = value

            if key == "energy":
                self.energy = value

    def progress(self, count=0):
        os.system('clear')
        print(f"Timer: {count}")

class Enemy(Character):
    def __init__(self):
        Character.__init__(self, player)
        self.tough_factor = randint(0, player.level)

    def goblin(self):
        self.level: int = 1
        self.name: str = "A Goblin"
        self.health: int = randint(1, player.health * self.tough_factor)

    def troll(self):
        self.level: int = 1
        self.name: str = "A Troll"
        self.health: int = randint(2, player.health * self.tough_factor)



player = Player()


while settings.game_started:

    clear_screen()

    print("It is a cold night and a storm is coming. You have found yourself exposed to the elements. You must seek shelter inside a nearby cave. ")
    player.text_input()

    sleep(5)


    #     print("You quickly make your way inside the cave just as the storm comes in.")
    # if player.text_input() == "stay outside":
    #     print("Not only is the cold setting in but you find yourself in the midst of the worst winter storm in decades.")
    # else:
    #     print("I don't understand")
