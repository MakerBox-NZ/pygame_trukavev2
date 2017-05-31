# Made by TruKave Co. ()
# Help from Jess & Seth

import pygame
import random
import math
import sys
import os
import time

# OBJECTS:
player = pygame.image.load(os.path.join('images', 'player.png')).convert()

# SETUP
screenSize = [960, 720]

fps = 60
afps = 6

clock = pygame.time.Clock()
pygame.init()

main = True

screen = pygame.display.set_mode(screenSize)

# MAIN LOOP/GAME
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
screen.fill([0,0,0])
pygame.display.flip()
clock.tick(fps)
                
