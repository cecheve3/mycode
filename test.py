#!/usr/bin/env python3

class Player:
    def __init__(self,name):
        self.name = name
        self.position = 0
        self.guess = 0

    def getNumberOfTries(self):
        return self.position

    def getPlayerName(self):
        return self.name

    def play(self):
        try:
            self.guess = int(input("Enter an integer from 1 to 99: "))
            self.position+=1
            return self.guess
        except Exception as error:
            print(error)
            return None


import random
p1 = Player("Player 1")
p2 = Player("Player 2")
P3 = Player("Player 3")
P4 = Player("Player 4")
P5 = Player("Player 5")
players = []
players.append(p1) #addding player
players.append(p2)
players.append(p3)
Players.append(p4)
Players.append(p5)
n1 = random.randint(1, 99)
end_zone = 5
##print(n1) #for debug
while players:
    for player in players:
        print(player.getPlayerName() + " turn:  " + str(end_zone - player.positon) + " positions to victory")
        guess = player.play()
        if guess == n1:
            player.position+=1
        elif guess > n1:
            print ("guess is high")
        else:
            print(player.getPlayerName()," you guessed it")
            players.clear() # exit game
            break #exit loop
        if player.getNumberOfTries == NUMBER_OF_TRIES:
            print(player.getPlayerName(), " out of chances")
            players.remove(player)

