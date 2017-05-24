import random
import math
import time
print ("Hello and welcome to the dice-roll game!")
points = 0
pointstotal = 0
lastgame = 0
while True:
    print ("Hit enter to continue!")
    print ("If you REALLY want to, hit 'Q' then enter to quit.")
    a = input()
    if a.lower() == 'q':
        break
    player = random.randint(1, 100)
    computer = random.randint(1, 100)
    points = player - computer
    pointstotal += points
    print ("The computer got " + str(computer) + " points!")
    time.sleep(1)
    print ("You got " + str(player) + " points!")
    time.sleep(1)
    if lastgame == player:
        print ("Twice in a row! Double points!")
        player = player * 2
    if player > computer:
        print ("You win! +" + str(points) + " points!")
    elif computer > player:
        print ("You lose! " + str(points) + " points!")
    else:
        print ("Its a tie! No point gain or loss!")
    print ("You currently have " + str(pointstotal) + " points!")
    print ("The opponent currently has " + str(pointstotal - (pointstotal * 2)) + " points!")
    lastgame = player
    time.sleep(2)
    print(" ")
    

