#!/usr/bin/env3 python3

from colorama import Fore

def showInstructions():
  #print a main menu and the commands
  print('''
Tears of the Inferno
========
Commands:
  go [direction]
  open [doors/windows]
  get [item]
''')
# Functions

def cls():
    print("\n" * 10)
def start_room():
    cls()
    start_room_option = ["1", "2"]
    user_choice =""
    while user_choice not in start_room_option:
        print('''You bolt upright! You smell smoke! AGHHHGHHGH! You blacked out from a long night out on the town. You don't know who's house this is. You're in a closet. Bleary eyed, you open the door and are faced with either going left or right. Which way do you go?\n1- Stay in the closet and go back to sleep.\n2- Open the door exit the closet. ''')

        user_choice = str(input("Enter option number: "))
    print("You have selected " + user_choice)
    if user_choice == start_room_option[0]:
        room01()
    elif user_choice == start_room_option[1]:
        room02()
    
def room01():
    print("\n \n --> You have decided to stay in the closet and go back to sleep ")

def room02():
    print("\n \n --> You have decided to exit the closet. You are in a long hall now ")
    
