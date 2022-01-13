#!/usr/bin/env python3

from random import randint
from colorama import Fore
die = 6
move = True
collected = 0
death = 6

def instruction():
    print(Fore.GREEN + '''The game is simple. To win you must collect 15 or more marbles. You will roll the dice as many times as it takes. Each dice roll will equal the amount of marbles you pick up. If you roll a 6 though, you die.''')

instruction()

while move:
    user_roll = input(Fore.BLUE + "Prepare to roll and seal your fate. Type 'cast' to roll or 'q' to quit.\n> ").lower()
    if user_roll == 'cast':
        roll = randint(1, die)
        if roll != death:
            collected+= roll
            print(Fore.WHITE + roll.__str__() + " marbles added to your score.")
            print("You now have: " + collected.__str__())
            if collected == 15 or collected == 16 or collected == 17 or collected == 18 or collected == 19:
                print("Fate has smiled upon you today, you live to fight another day.")
                break

        else:
            move == False
            print(Fore.RED + "You rolled 6! A portal has opened beneath you and you have fallen into the void. RIP.")
            break
    elif user_roll == 'q':
        print("You have chosen to flee.")
    else: 
        move == False
        print("You collected: " + points.__str__())
