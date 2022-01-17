#!/usr/bin/env python3

from random import randint
from colorama import Fore

def showInstructions():
  #print a main menu and the instructions
  print(Fore.GREEN +'''
Final Boss Casting Game

===============================================
Instructions:
  -The objective of the game is to cast down 
  the final boss.
  -You will be asked to guess a number between 
  1 and 7.
  -You will have 3 attempts to guess correctly. 
  -If you guess correct, you will get a 5x
  bonus on your cast.
  -Incorrect guesses result in taking x5 damage.
  -You each start off with 100 health
  -You will roll a die to determine how much 
  damage you will inflict on your opponent.
    -Example: If you guessed correct, and you 
    rolled a 6, you will inflict 30 damage to 
    the boss. If you guess incorrect, and you
    roll a 6, you take 30 damage.
  -Defeat the final boss or forever be shamed!
===============================================
  ''')

die = 6
boss_health = 100
player_health = 100
tries = 0
roll = randint(1, die)
attack_boss = boss_health - roll
attack_player = player_health - roll

showInstructions()

def main():
    while boss_health != 0 or player_health != 0:

            a = random.randint(1, 7)
            g = int(raw_input(Fore.WHITE + "Enter a number between 1 and 7:\n> "))
            
            if g == a:
                r = input(Fore.BLUE + "Enter 'cast' to attack the boss!\n ").lower()
                if r == "cast":
                    attack_boss()
            
            elif g > a:
                g = int(raw_input(Fore.RED + "Too high, try again: "))
                tries += 1

            elif g < a:
                g = int(raw_input(Fore.RED + "Too low, try again: "))
                tries += 1 

            else:
                attack_player()
            
main()
