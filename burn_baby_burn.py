#!/usr/bin/env python3

import random

def showInstructions():
  #print a main menu and the instructions
  print('''
Molly's Game

===============================================
Instructions:
  -Start with 5 players in the game. 
  -You all start at the starting point.
  (position 0)
  -The objective of the game is to make it 
  to the safe zone.
  (position 8)
  -The way to move forward is to guess a 
  number between 1-15.
  -The players that guess the closest move up 
  by one position.
  -The player that guesses the furthest will
  be eliminated.
  
===============================================
  ''')
##players
players= ["P1", "P2", "P3", "P4", "P5"]

showInstructions()
print('''Hi my name's Molly. You have to play my
        game. If you lose, something bad will
        happen. If you win, you can be my 
        friend. Are you ready to play? ''')

molly_number= random.randint(1, 15)

finished_pos= 5
current_player= 1

while finished_pos > 0:
    if current_player == 1:
        guess = int(input("Player_1 please enter a number from 1 to 15, {} moves to win. ".format(finished_pos)))

        finished_pos
