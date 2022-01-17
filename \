#!/usr/bin/env python3

## lock combo

import math
from random import randint
from colorama import Fore

def instructions():
  print(Fore.YELLOW + '''
Safe Cracker Game
===============================================

Instructions:
  -This is a guessing game in which you will 
  try and figure out a lock combination. 
  -The model lock sequence consists of 3 
  numbers. 
  -The dial goes from 0 to 10. You will start 
  at 0 and go up to the first, then down to the 
  second, then back up to the third. 
  -You will be given prompts to gauge how close
  you are. 
  -If it takes you more than 3 attempts for each
  target, the lock will shut forever.

===============================================
  ''')

instructions()

def target_1(): 
    
    # Taking Inputs
    lower = 0
 
    # Taking Inputs
    upper = 10

    # Keeping score
    score = 0
           
    x = randint(lower, upper)
    print(Fore.RED + "\n\tYou've only ", round(math.log(upper - lower + 1, 2)),
    " chances to guess the target!\n")
        
    count = 1
    
    while count < math.log(upper - lower + 1, 2):
        count += 1
        guess = int(input(Fore.YELLOW + "Guess a number:\n> "))
        temp_str = {
                    1: "Extremely Hot",
                    2: "Hot",
                    3: "Warmer",
                    4: "Warm",
                    5: "Neutral",
                    6: "Cold",
                    7: "Colder",
                    8: "Icy",
                    9: "Frozen",
                    10: "Arctic Circle"
                    }
        distance = abs(guess - x)
            
        if guess == x:
            print(Fore.RED + 'Face Melt!')
            target_2()

        elif distance == 1:
            print(Fore.RED + temp_str[1])
        elif distance == 2:
            print(Fore.RED + temp_str[2])
        elif distance == 3:
            print(Fore.RED + temp_str[3])
        elif distance == 4:
            print(Fore.RED + temp_str[4])
        elif distance == 5:
            print(Fore.WHITE + temp_str[5])
        elif distance == 6:
            print(Fore.BLUE + temp_str[6])
        elif distance == 7:
            print(Fore.BLUE + temp_str[7])
        elif distance == 8:
            print(Fore.BLUE + temp_str[8])
        elif distance == 9:
            print(Fore.BLUE + temp_str[9])
        elif distance == 10:
            print(Fore.BLUE + temp_str[10])



        if count >= math.log(upper - lower + 1, 2):
            print(Fore.YELLOW + "\nThe number is %d" % x)
            print(Fore.YELLOW + "\tThe safe is locked forever!")
            break
    

def target_2():
    
    # Taking Inputs
    lower = 0

    # Taking Inputs
    upper = 10

    # Keeping score
    #score = 1 

    x = randint(lower, upper)
    print(Fore.RED + "\n\tYou've only ", round(math.log(upper - lower + 1, 2)),
    "chances to guess the target!\n")

    count = 1

    while count < math.log(upper - lower + 1, 2):
        count += 1
        guess = int(input(Fore.YELLOW + "Guess a number:\n> "))
        temp_str = {
                    1: "Extremely Hot",
                    2: "Hot",
                    3: "Warmer",
                    4: "Warm",
                    5: "Neutral",
                    6: "Cold",
                    7: "Colder",
                    8: "Icy",
                    9: "Frozen",
                    10: "Arctic Circle"
                    }
        distance = abs(guess - x)

        if guess == x:
            print(Fore.RED + 'Face Melt!')
            target_3()
            
            

        elif distance == 1:
            print(Fore.RED + temp_str[1])
        elif distance == 2:
            print(Fore.RED + temp_str[2])
        elif distance == 3:
            print(Fore.RED + temp_str[3])
        elif distance == 4:
            print(Fore.RED + temp_str[4])
        elif distance == 5:
            print(Fore.WHITE + temp_str[5])
        elif distance == 6:
            print(Fore.BLUE + temp_str[6])
        elif distance == 7:
            print(Fore.BLUE + temp_str[7])
        elif distance == 8:
            print(Fore.BLUE + temp_str[8])
        elif distance == 9:
            print(Fore.BLUE + temp_str[9])
        elif distance == 10:
            print(Fore.BLUE + temp_str[10])



        if count >= math.log(upper - lower + 1, 2):
            guess == False
            print(Fore.YELLOW + "\nThe number is %d" % x)
            print(Fore.YELLOW + "\tThe safe is locked forever!")
            break
        

def target_3():

    # Taking Inputs
    lower = 0

    # Taking Inputs
    upper = 10

    # Keeping score
            

    x = randint(lower, upper)
    print(Fore.RED + "\n\tYou've only ", round(math.log(upper - lower + 1, 2)),
    " chances to guess the target!\n")

    count = 1
    #guess = int(input(Fore.YELLOW + "Guess a number:\n> "))
    #while guess != x and count != 4: 
    while count < math.log(upper - lower + 1, 2):  #I can't get this to end when guess == x 
        count += 1
        guess = int(input(Fore.YELLOW + "Guess a number:\n> "))
        temp_str = {
                    1: "Extremely Hot",
                    2: "Hot",
                    3: "Warmer",
                    4: "Warm",
                    5: "Neutral",
                    6: "Cold",
                    7: "Colder",
                    8: "Icy",
                    9: "Frozen",
                    10: "Arctic Circle"
                    }
        distance = abs(guess - x)

        if guess == x:
            print(Fore.RED + 'Face Melt!')
            end()
            break
             
        elif distance == 1:
            print(Fore.RED + temp_str[1])
        elif distance == 2:
            print(Fore.RED + temp_str[2])
        elif distance == 3:
            print(Fore.RED + temp_str[3])
        elif distance == 4:
            print(Fore.RED + temp_str[4])
        elif distance == 5:
            print(Fore.WHITE + temp_str[5])
        elif distance == 6:
            print(Fore.BLUE + temp_str[6])
        elif distance == 7:
            print(Fore.BLUE + temp_str[7])
        elif distance == 8:
            print(Fore.BLUE + temp_str[8])
        elif distance == 9:
            print(Fore.BLUE + temp_str[9])
        elif distance == 10:
            print(Fore.BLUE + temp_str[10])



        if count >= math.log(upper - lower + 1, 1):
            print(Fore.YELLOW + "\nThe number is %d" % x)
            print(Fore.YELLOW + "\tThe safe is locked forevere")
            break
    
    

def end():
    print(Fore.GREEN + "You have mastered the safe!")
    
def main():
    target_1()
main()
