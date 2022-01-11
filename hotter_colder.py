#!/usr/bin/env python3

#troll crossing
#3 attempts to guess a number 1-6
#if you guess correctly you pass to the next
#guess wrong. you die

import random
from colorama import Fore

def show_instructions():
    print(Fore.GREEN +'''
    Troll Toll
    ==========
    Guess 1-6
    ''')

def show_status():
    print('----------------------------')
    print(Fore.WHITE + "You are travelling through the forest to get to your G-ma's house. The forest is filled with trolls and they love playing games. Outwit them or get eaten. ")

show_instructions()

while True:
    
    show_status()

move
