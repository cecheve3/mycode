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
  (position 5)
  -The way to move forward is to guess a 
  number between 1-15.
  -The players that guess the closest move up 
  by one position.
  -The player that guesses the furthest will
  be eliminated.
  
===============================================
  ''')
##players

finished= False
guesses= 0
##players= {"P1": {"choice": 0,
  ##              "place": 1},
  ##        "P2": {"choice": 0,
  ##              "place": 1},
  ##        "P3": {"choice": 0,
  ##              "place": 1},
  ##        "P4": {"choice": 0,
  ##              "place": 1},
  ##        "P5": {"choice": 0,
  ##              "place": 1}
  ##      }
            # complete rest of dict
    
print('''Hi my name's Molly. You have to play my
        game. If you lose, something bad will
        happen. If you win, you can be my 
        friend. Are you ready to play? ''')

# while loop that would run until there's only one left or someone has reached the finish line
while finished == False and len(players) <= 1:
        
# have some repeatable code that accepts a guess, saves it to "choice" in the players dictionary
# have some other code that compares each players' choice
   num_guess= 0
   answer= random.randint(1, 15)
   choice= input()
   for x in players:
       while num_guess < 5:
           guess= input(f"{player[x]} > {choice}")
           num_guess +=1
           players["x"]["choice"] +=1
           break

       
# run this line for whichever player bites it
#del players["P1"]




  
