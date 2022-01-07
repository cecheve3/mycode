#!/usr/bin/env python3
"""Number guessing game!"""

import random
from random import randint

num = randint(1, 100)

while True:
    guess = input("Guess a number (between 1 and 100), or 'q' to end the session: ") 
        
    if guess.casefold() == "q":
       print("end session")
       break
   
    try:
       user_guess= int(guess)
    
    except ValueError:
       print(f"Invalid input: {user_input}. Please pick again. ")
       continue

    if user_guess > num:
       print("Too high!")

    elif user_guess < num:
       print("Too low!")

    else:
       print("Correct!")
       break


