# Made by TruKave Co. ()
# Help from Jess & Seth

import pygame
import random
import math
import sys
import os
import time

# OBJECTS:
class Player(pygame.sprite.Sprite):
    # Spawn a player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [ ]
        img = pygame.image.load(os.path.join('images', 'player.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

# SETUP
screenSize = [960, 720]

fps = 60
afps = 6

clock = pygame.time.Clock()
pygame.init()

main = True

screen = pygame.display.set_mode(screenSize)

redin = True
redde = False
greenin = False
greende = False
bluein = False
bluede = False
a = 0
b = 0
c = 0

player = Player() # Spawning player.
player.rect.x = 0
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)

# MAIN LOOP/GAME
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
    if redin:
        a += 1
    elif redde:
        a -= 1
    if greenin:
        b += 1
    if greende:
        b -= 1
    if bluein:
        c += 1
    if bluede:
        c -= 1
    if a == 255:
        bluede = False
        redin = False
        redde = True
        greenin = True
    if b == 255:
        redde = False
        greenin = False
        greende = True
        bluein = True
    if c == 255:
        greende = False
        bluein = False
        bluede = True
        redin = True
    screen.fill([a,b,c])
    pygame.display.flip()
    clock.tick(fps)
                
