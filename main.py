import os
from random import randint
import settings

import enemy, player

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



def clear_screen():
    os.system('clear')

def progress(self, count=0, width=30):
    left = width * count // 30
    right = width - left
    
    tags = "#" * left
    spaces = " " * right
    count = f"{count}'s"

    print("\r[", tags, spaces, "] ", count, sep="", end="", flush=True)

while settings.game_started:                                            # This is our main game loop.

    clear_screen()                                                      # Lets clear the screen before we do anything else.
    player = player.Player()

    if settings.game_setup:                                             # This is the first run, and we need to setup the player.

        print("What is your name? ")
        player_name = player.text_input()
        player.set_stats(name=player_name)

        while settings.confirmed is False:

            print("What is your race? (Warrior, Mage, Human, Dark Elf)")
            player_race = player.text_input()
            player.set_stats(race=player_race)

            if player.race == 'warrior':
                player.set_stats(hp=200, mp=10, energy=300)

            elif player.race == 'mage':
                player.set_stats(hp=100, mp=100, energy=100)

            elif player.race == 'human':
                player.set_stats(hp=150, mp=50, energy=150)

            elif player.race == 'dark elf':
                player.set_stats(hp=100, mp=200, energy=100)

            print(f"Excellent choice, you will make a fine {player.race}, {player.name}")
            sleep(3)

            print(f"Your stats as a {player.race} are as follows: (You can access these anytime by typing status during the game)")
            print(f"Race: {player.race}, Level: {player.level}, [HP: {player.health}, MP: {player.magic}, Energy: {player.energy}]")
            print("Confirm? ")
            player_confirm = player.text_input()

            if player_confirm == "no":
                print("Let's try this again. ")
                sleep(2)

            elif player_confirm == "yes":
                print("Wonderful, let's begin.")
                settings.confirmed = True
                settings.game_setup = False

            else:
                print("I didn't understand, try again. ")
                sleep(2)

        # if text == "help":
        #     print("Enter a response and navigate through the game, type quit to leave and help to pull up this menu at any time.")

        # elif text == 'quit':
        #     print("Until next time!")
        #     settings.game_started = False

        # elif text == 'status' and settings.game_setup is False:
        #     print(f"Current Status: HP {player.health}, MP {player.magic}, Energy {player.energy}")

        # elif text == 'status' and settings.game_setup:
        #     print("You will need to setup your character first.")

        # elif text == 'inventory' and settings.game_setup is False:
        #     print(f"Current Inventory: {player.inventory}")

        # elif text == 'inventory' and settings.game_setup:
        #     print("You will need to setup your character first.")

        print("Loading game elements...")
        sleep(3)

    print("It is a cold night and a storm is coming. You have found yourself exposed to the elements. You must seek shelter inside a nearby cave. ")
    player.text_input()

    sleep(1)
