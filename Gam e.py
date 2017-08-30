    # Made by TruKave Co. ()
# Help from Jess & Seth

import pygame
import random
import math
import sys
import os
import time

noclip = False

# OBJECTS:
class Player(pygame.sprite.Sprite):
    # Spawn a player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.momentumX = 0
        self.momentumY = 0

        #gravity vars
        self.collide_delta = 0
        self.jump_delta = 6
        
        self.deaths = 0
        self.damage = 0
        
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
        
    def update(self, enemy_list, ground_list):
        currentX = self.rect.x
        nextX = currentX + self.momentumX
        self.rect.x = nextX

        currentY = self.rect.y
        nextY = currentY + self.momentumY
        self.rect.y = nextY

        #gravity
        #self.collide_delta < 7 and
        if self.jump_delta < 10:
            self.jump_delta = 6*2
            self.momentumY -= 25 #jump height

            self.collide_delta +=6
            self.jump_delta += 6

    
        
        ground_hit_list = pygame.sprite.spritecollide (self, ground_list, False)
        if self.momentumX > 0:
            for ground in ground_hit_list:
                self.rect.y = currentY
                self.rect.x = currentX+9
                self.momentumY = 0
                self.collide_delta = 0 #stop jumping
        if self.momentumY > 0:
            for ground in ground_hit_list:
                self.rect.y = currentY
                self.momentumY = 0
                self.collide_delta = 0 #stop jumping
        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        static_hit_list = pygame.sprite.spritecollide(self, static_list, False)
        '''for enemy in enemy_hit_list:
                self.rect.x = 100
                self.deaths += 1
                print(self.deaths)'''
        if self.damage == 0:
            for enemy in enemy_hit_list:
                if self.rect.colliderect(enemy):
                    self.damage = self.rect.colliderect(enemy)
                    print(self.deaths)
            for static in static_hit_list:
                if self.rect.colliderect(static):
                    self.damage = self.rect.colliderect(static)
                    print(self.deaths)
        if self.damage == 1:
            if not noclip:
                idx = self.rect.collidelist(enemy_hit_list)
                if idx == -1:
                    self.damage = 0
                    self.deaths += 1
                    self.rect.x = 100
                    
    def jump (self, ground_list):
        self.jump_delta = 0
        
    def gravity(self):
        self.momentumY += 1

        if self.rect.y > 1003 and self.momentumY>= 0:
            self.momentumY = 0
            self.rect.y = screenY-20
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

class Static(pygame.sprite.Sprite):
    #x location, y location, img width, img heighm img file
    def __init__ (self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([imgw, imgh])
        self.image.convert_alpha()
        self.image.set_colorkey(alpha)
        self.blockpic = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

        #paint image into blocks
        self.image.blit(self.blockpic, (0,0), (0,0,imgw,imgh))


def level1():
    #create level 1
    static_list = pygame.sprite.Group()
    spike = Static(800, 846, 64, 64,os.path.join('images', 'enemyu b.png'))
    spike0 = Static(800, 50, 64, 500,os.path.join('images', 'enemy c.png'))
    static_list.add(spike) #after each block
    static_list.add(spike0)
    return static_list

# SETUP
screenSize = [1920, 1080]
screenY = 1080
screenX = 1920
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

static_list = level1() #set stage to Level 1

player = Player() # Spawning player.
player.rect.x = 100
player.rect.y = 836
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
movesteps = 5
forwardX = 600
backwardX = 50

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
                player.jump(ground_list)
            if event.key == ord('a'):
                print("Left")
                player.control(-movesteps, 0)
            if event.key == ord('s'):
                print("QuickDown")
            if event.key == ord('d'):
                print("Right")
                player.control(movesteps, 0)
    #scroll forward
    if player.rect.x >= forwardX:
        scroll = player.rect.x - forwardX
        player.rect.x = forwardX
        for static in static_list:
            static.rect.x -= scroll
        for enemy in enemy_list:
            enemy.rect.x -= scroll
    #scroll backward
    if player.rect.x <= backwardX:
        scroll = player.rect.x + backwardX
        #min(1, (backwardX - player.rect.x))
        player.rect.x = backwardX
        for static in static_list:
            static.rect.x += scroll
        for enemy in enemy_list:
            enemy.rect.x += scroll
            
    if redin:
        a += 0.2
    elif redde:
        a -= 0.2
    if greenin:
        b += 0.2
    elif greende:
        b -= 0.2
    if bluein:
        c += 0.2
    elif bluede:
        c -= 0.2
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
    
    ground_list.draw(screen)
    static_list.draw(screen) #draw platform on screen
    player.gravity() 
    player.update(enemy_list, ground_list)
    movingsprites.draw(screen)
    enemy_list.draw(screen)
    enemy.move()
    pygame.display.flip()
    clock.tick(fps)
                
