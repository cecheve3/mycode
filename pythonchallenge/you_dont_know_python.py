#!/usr/bin/env python3

import colorama
from colorama import Fore

print(Fore.BLUE + "Welcome to the jung... I mean python quiz")

name= input(Fore.WHITE + "Enter your name: ")

round  = 0
answer = " "


while round < 1000 and answer != "skull":
    answer= input(Fore.WHITE + "what is the hardest part of python? ").lower()
   
    #if answer == "":
       # print(Fore.MAGENTA + "YAY ENDLESS LOOP!" )
    
    if answer == "skull":
        print(Fore.GREEN + "Wow! Amazing! I never knew you had it in you!")
       
    else:
        print(Fore.RED + "Wowwwww! Good thing you're in this class " + name )
        print("Next ones easy. ")
    round += 1
    break
while round < 10000 and answer != "ball python":
    answer= input(Fore.WHITE + "What is the easiest version for beginners?  ").lower()
    
    #if answer == "":
       # print(Fore.MAGENTA + "YAY ENDLESS LOOP!" )
    
    if answer == "ball python":
        print(Fore.GREEN + "Wow! Amazing! I never knew you had it in you!")

    else:
        print(Fore.RED + "Oof! Rough day? " + name )
        print("You got this. ")
    round += 1
    break
while round < 10000 and answer != "true":
    answer= input(Fore.WHITE + "True or False: Python has been known to kill people? ").lower()
    #if answer == "":
       # print(Fore.MAGENTA + "YAY ENDLESS LOOP!" )
    if answer == "true":
        print(Fore.GREEN + "Wow! Amazing! I always knew you could do it!")

    else:
        print(Fore.RED + name + ", SMH... Thank goodness there isn't a cert in this portion " )
        print("Last one. ")
    round += 1
    break
while round < 100000 and answer != 25:
    answer= input(Fore.WHITE + "How many types are there?  ").lower()
    #if answer == "":
       # print(Fore.MAGENTA + "YAY ENDLESS LOOP!" )
    if answer == 25:
        print(Fore.YELLOW + "Go " + name + "! It's your birthday\nAnd we gon' party like it's your birthday" )   
    else:
        print(Fore.RED + "Oh did I forget to mention this quiz is on python snakes?? " )
        print("WOMP WOMP WOMP ")
    round += 1
    break












