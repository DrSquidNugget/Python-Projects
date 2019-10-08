# Title:   RockPaperScissors.py
# Purpose: Game of Rock Paper Scissors
# Author:  DrSquidNugget
# Date:    01/02/2019
#
import random

rulematrix = [[0,2,2],[2,0,1],[1,2,0]]

player1answer = input("Player 1 Chooses? ")
#player2answer = input("Player 2 Chooses? ")
player2answer = random.randrange(0,2)

player1answer= int(player1answer)
player2answer= int(player2answer)

print("Player 2's answer is ",player2answer,sep='')
print("Result: ",end='')
winner = rulematrix[player2answer][player1answer]
print(winner)

