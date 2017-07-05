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
        self.momentumX = 0
        self.momentumY = 0

        self.deaths = 0
        
        self.images = [ ]
        img = pygame.image.load(os.path.join('images', 'player.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
        
    def control(self, x, y):
        self.momentumX += x
        self.momentumY += y
        
    def update(self, enemy_list):
        currentX = self.rect.x
        nextX = currentX + self.momentumX
        self.rect.x = nextX

        currentY = self.rect.y
        nextY = currentY + self.momentumY
        self.rect.y = nextY

        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        for enemy in enemy_hit_list:
            self.rect.x = 100
            self.deaths += 1
            print(self.deaths)
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img))
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
    def move(self):
        if self.counter >= 0 and self.counter <= 50:
            self.rect.y -= 2
        elif self.counter >= 50 and self.counter <= 100:
            self.rect.y += 2
        else:
            self.counter = 0
            print('reset')

        self.counter += 1

class Ground(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img))
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# SETUP
screenSize = [1920, 1080]

fps = 144
afps = 14

clock = pygame.time.Clock()
pygame.init()

main = True

screen = pygame.display.set_mode(screenSize)
alpha = (0,0,0)
black = (1,1,1)
white = (255,255,255)

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
player.rect.x = 100
player.rect.y = 836
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
movesteps = 5

#enemy code
enemy = Enemy(500,836, 'enemy.png')
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy)

#ground code
ground = Ground(0,900, 'line.png')
ground_list = pygame.sprite.Group()
ground_list.add(ground)

# MAIN LOOP/GAME
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
            if event.key == ord('w'):
                print("Up Stop")
            if event.key == ord('a'):
                print("Left Stop")
                player.control(movesteps, 0)
            if event.key == ord('s'):
                print("QuickDown Stop")
            if event.key == ord('d'):
                print("Right Stop")
                player.control(-movesteps, 0)
        if event.type == pygame.KEYDOWN:
            if event.key == ord('w'):
                print("Up")
            if event.key == ord('a'):
                print("Left")
                player.control(-movesteps, 0)
            if event.key == ord('s'):
                print("QuickDown")
            if event.key == ord('d'):
                print("Right")
                player.control(movesteps, 0)
    if redin:
        a += 0.1
    elif redde:
        a -= 0.1
    if greenin:
        b += 0.1
    elif greende:
        b -= 0.1
    if bluein:
        c += 0.1
    elif bluede:
        c -= 0.1
    if a > 254:
        bluede = False
        redin = False
        redde = True
        greenin = True
        print('green')
    if b > 254:
        redde = False
        greenin = False
        greende = True
        bluein = True
        print('blue')
    if c > 254:
        greende = False
        bluein = False
        bluede = True
        redin = True
        print('red')
    screen.fill([a,b,c])
    player.update(enemy_list)
    movingsprites.draw(screen)
    ground_list.draw(screen)
    enemy_list.draw(screen)
    enemy.move()
    pygame.display.flip()
    clock.tick(fps)
                
