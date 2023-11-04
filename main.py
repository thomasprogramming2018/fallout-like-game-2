import pygame,sys
from pygame.locals import *
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
import time
from pygame.time import *
import random as rand
import pygame_gui
import os
import Aroyo
import npc
import playerMapnpc as mapnpc

import pickle

import json

import socket

import threading

import traceback

import asyncio

#from pygame.surfarray import *

class Player(pygame.sprite.Sprite):
    def __init__(self,groups,obstacles):
        super().__init__()
        
        self.isAnimating = False
        self.sprites = []
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (1).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (2).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (3).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (4).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (5).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (6).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (7).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (8).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (9).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (10).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (11).png'))
        self.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (12).png'))
        self.currentSprite = 0
        self.image = self.sprites[self.currentSprite]
        self.circle_surface = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.obstacles = obstacles

        self.turn = True

        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 600
        self.pos = pygame.math.Vector2(self.rect.topleft)

        self.hp = 100

        self.isWeapon_anim = False
        self.degree = "down"
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.isHoldingNone = False
        
        #online
        self.has_turn = False


        self.ap = 100
        self.ap_max = 100
    def animate(self):
        self.isAnimating = True
    #def move(self, x, y):
        #pygame.rect.Rect.move_ip(x,y)

    def move(self, pressed_keys):
        global moving
        if pressed_keys[K_w] and turn == 0 or pressed_keys[K_w] and turn == 10 or pressed_keys[K_w] and self.turn:#up
            moving = True
            if caps_Running == False:
                self.rect.move_ip(2, -2)
                self.degree = "up"
                self.direction(self.degree)
            else:
                self.rect.move_ip(5, -5)
                self.degree = "up-Run"
                self.direction(self.degree)
        if pressed_keys[K_q] and turn == 0 or pressed_keys[K_q] and turn == 10 or pressed_keys[K_q] and self.turn:#up
            moving = True
            if caps_Running == False:
                self.rect.move_ip(-2, 2)
                self.degree = "up-left"
                self.direction(self.degree)
            else:
                self.rect.move_ip(-5, -5)
                self.degree = "up-left-Run"
                self.direction(self.degree)  
        if pressed_keys[K_x] and turn == 0 or pressed_keys[K_x] and turn == 10 or pressed_keys[K_x] and self.turn:#Down
            moving = True
            if caps_Running == False:
                self.rect.move_ip(4, 4)
                self.degree = "down"
                self.direction(self.degree)
            else:
                self.rect.move_ip(10, 10)
                self.degree = "down-Run"
                self.direction(self.degree)
        if pressed_keys[K_a] and turn == 0 or pressed_keys[K_a] and turn == 10 or pressed_keys[K_a] and self.turn:#left
            moving = True
            if caps_Running == False:
                self.rect.move_ip(-4, 0)
                self.degree = "left"
                self.direction(self.degree)
            
            else:
                self.rect.move_ip(-10, 0)
                self.degree = "left-Run"
                self.direction(self.degree)
        if pressed_keys[K_d] and turn == 0 or pressed_keys[K_d] and turn == 10 or pressed_keys[K_d] and self.turn:#right
            moving = True
            if caps_Running == False:
                self.rect.move_ip(4, 0)
                self.degree = "right"
                self.direction(self.degree)
            else:
                self.rect.move_ip(10, 0)
                self.degree = "right-Run"
                self.direction(self.degree)
        if pressed_keys[K_z] and turn == 0 or pressed_keys[K_z] and turn == 10 or pressed_keys[K_z] and self.turn:#down-left
            moving = True
            if caps_Running == False:
                self.rect.move_ip(-4, 4)
                self.degree = "down-left"
                self.direction(self.degree)
            else:
                self.rect.move_ip(-10, 10)
                self.degree = "down-left-Run"
                self.direction(self.degree)

    def direction(self, degree):    
        try:
            if using_item[0].name != None:
                self.isHoldingNone = False
        except IndexError:
            self.isHoldingNone = True
        if degree == 'up' and self.isHoldingNone == True:
            self.sprites.clear()
            for i in range(0,8):
                self.sprites.append(pygame.image.load(f"objects/animations/Walk/0/frame_{i}_delay-0.1s.png"))
        
        if degree == "down" and self.isHoldingNone == True:
            self.sprites.clear()
            for i in range(0,8):
                self.sprites.append(pygame.image.load(f"objects/animations/Walk/2/frame_{i}_delay-0.1s.png"))
        
        if degree == "right" and self.isHoldingNone == True:
            self.sprites.clear()
            for i in range(0,8):
                self.sprites.append(pygame.image.load(f"objects/animations/Walk/1/frame_{i}_delay-0.1s.png"))
        
        if degree == "left" and self.isHoldingNone == True:
            self.sprites.clear()
            for i in range(0,8):
                self.sprites.append(pygame.image.load(f"objects/animations/Walk/3/frame_{i}_delay-0.1s.png"))
        
        if degree == "right-Run" and self.isHoldingNone == True:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/1/frame_0{i}_delay-0.1s.png"))
        
        if degree == "left-Run" and self.isHoldingNone == True:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/3/frame_0{i}_delay-0.1s.png"))
        
        if degree == "down-Run" and self.isHoldingNone == True:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/2/frame_0{i}_delay-0.1s.png"))
        
        if degree == "up-Run" and self.isHoldingNone == True:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/0/frame_0{i}_delay-0.1s.png"))
        
        if degree == "down-left-Run" and self.isHoldingNone == True:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/4/frame_0{i}_delay-0.1s.png"))
        
        if degree == "up-left-Run" and self.isHoldingNone == True:
            self.sprites.clear()
            #9 frames
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/m1/frame_0{i}_delay-0.1s.png"))
        try:
            if degree == "left"  and using_item[0].name == 'shotgun' or using_item[0].name == 'rifle':
                self.sprites.clear()
                for i in range(0,8):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/walk/4/frame_{i}_delay-0.1s.png"))
        except IndexError:
            pass
        try:
            if degree == "right"  and using_item[0].name == 'shotgun' or using_item[0].name == 'rifle':
                self.sprites.clear()
                for i in range(0,8):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/walk/1/frame_{i}_delay-0.1s.png"))
        except IndexError:
            pass
        try:
            if degree == "up"  and using_item[0].name == 'shotgun' or using_item[0].name == 'rifle':
                self.sprites.clear()
                for i in range(0,8):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/walk/0/frame_{i}_delay-0.1s.png"))
        except IndexError:
            pass
        try:
            if degree == "down"  and using_item[0].name == 'shotgun' or using_item[0].name == 'rifle':
                self.sprites.clear()
                for i in range(0,8):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/walk/2/frame_{i}_delay-0.1s.png"))
        except IndexError:
            pass
    def collision(self):
        collision_sprites = pygame.sprite.spritecollide(self,self.obstacles,False)
        #print(collision_sprites)
        if self.degree == "left" or self.degree == "left-Run":

            for sprite in collision_sprites:
                #if self.rect.left <= sprite.rect.right + 100 and self.old_rect.left >= sprite.old_rect.left:
                if pygame.sprite.collide_mask(sprite,player):
                    #self.rect.left = sprite.rect1.right
                    self.rect.left = self.rect.left + 5
        if self.degree == "right" or self.degree == "right-Run":
    
            for sprite in collision_sprites:
                
                #if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.right:
                if pygame.sprite.collide_mask(sprite,player):
                    #self.rect.right = sprite.rect1.left
                    self.rect.right = self.rect.right - 5
        if self.degree == "down" or self.degree == "down-Run" or self.degree == "down-left" or self.degree == "down-left-Run":
        
            for sprite in collision_sprites:
                #if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.bottom:
                 if pygame.sprite.collide_mask(sprite,player):
                    #self.rect.bottom = sprite.rect1.top
                    self.rect.bottom = self.rect.bottom - 5
        if self.degree == "up" or self.degree == "up-Run" or self.degree == "up-left" or self.degree == "up-left-Run":
            for sprite in collision_sprites:
                #if self.rect.top <= sprite.rect.bottom + 150 and self.old_rect.bottom >= sprite.old_rect.bottom:
                 if pygame.sprite.collide_mask(sprite,player):
                    #self.rect.top = sprite.rect1.bottom
                    self.rect.top = self.rect.top + 5
                    

    def update(self):
        self.old_rect = self.rect.copy()
        if self.isAnimating == True:
            self.currentSprite += 0.3

            if self.currentSprite >= len(self.sprites):
                if self.isWeapon_anim == True:#self.degree == "down" and vvvvv
                    if using_item[0].name == 'shotgun' or using_item[0].name == 'rifle':
                        self.isWeapon_anim = False
                        self.sprites.clear()
                        self.currentSprite = 0
                        self.sprites.append(pygame.image.load(f"objects/animations/rifle/in/2/frame_5_delay-0.1s.png"))
                        
                        #self.isAnimating = False
                else:
                    self.currentSprite = 0
                    self.isAnimating = False
                
            self.image = self.sprites[int(self.currentSprite)]
        self.collision()
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
    def play_shoot(self,target):
        d2x = target.rect.x - player.rect.x
        d2y = target.rect.y - player.rect.y
        try:
            if using_item[0].name == 'shotgun' and playing_online == True:
                self.ap -= 50
        except IndexError:
            pass
        self.ap 
        if target.rect.y > player.rect.y and target.rect.x > player.rect.x and using_item[0].name == 'shotgun' or using_item[0].name == 'rifle':
            self.sprites.clear()
            for i in range(0,4):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/2/frame_{i}_delay-0.1s.png"))
            for i in range(0,4):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/shoot/2/frame_{i}_delay-0.1s.png"))
            for i in range(0,6):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/in/2/frame_{i}_delay-0.1s.png"))
            self.isWeapon_anim = True
        if target.rect.y < player.rect.y and target.rect.x > player.rect.x and using_item[0].name == 'shotgun' or using_item[0].name == 'rifle':
            self.sprites.clear()
            for i in range(0,4):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/0/frame_{i}_delay-0.1s.png"))
            for i in range(0,4):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/shoot/0/frame_{i}_delay-0.1s.png"))
            for i in range(0,6):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/in/0/frame_{i}_delay-0.1s.png"))
            self.isWeapon_anim = True
        if target.rect.y < player.rect.y and target.rect.x < player.rect.x and using_item[0].name == 'shotgun' or using_item[0].name == 'rifle':
            self.sprites.clear()
            for i in range(0,4):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/5/frame_{i}_delay-0.1s.png"))
            for i in range(0,4):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/shoot/5/frame_{i}_delay-0.1s.png"))
            for i in range(0,6):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/in/5/frame_{i}_delay-0.1s.png"))
            self.isWeapon_anim = True
        if target.rect.y > player.rect.y and target.rect.x < player.rect.x and using_item[0].name == 'shotgun' or using_item[0].name == 'rifle':
            self.sprites.clear()
            for i in range(0,4):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/3/frame_{i}_delay-0.1s.png"))
            for i in range(0,4):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/shoot/3/frame_{i}_delay-0.1s.png"))
            for i in range(0,6):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/in/3/frame_{i}_delay-0.1s.png"))
            self.isWeapon_anim = True
        if target.rect.y < player.rect.y +50 and target.rect.y > player.rect.y -50 and target.rect.x > player.rect.x and using_item[0].name == 'shotgun' or using_item[0].name == 'rifle':
            self.sprites.clear()
            for i in range(0,4):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/1/frame_{i}_delay-0.1s.png"))
            for i in range(0,4):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/shoot/1/frame_{i}_delay-0.1s.png"))
            for i in range(0,6):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/in/1/frame_{i}_delay-0.1s.png"))
            self.isWeapon_anim = True
        if target.rect.y < player.rect.y +50 and target.rect.y > player.rect.y -50 and target.rect.x < player.rect.x and using_item[0].name == 'shotgun' or using_item[0].name == 'rifle':
            self.sprites.clear()
            for i in range(0,4):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/4/frame_{i}_delay-0.1s.png"))
            for i in range(0,4):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/shoot/4/frame_{i}_delay-0.1s.png"))
            for i in range(0,6):
                self.sprites.append(pygame.image.load(f"objects/animations/rifle/in/4/frame_{i}_delay-0.1s.png"))
            self.isWeapon_anim = True
    def shoot():
        global current_weapon
        if current_weapon == 1:
            weapon_damage[0]
            return weapon_damage[0]
        if current_weapon == 2:
            weapon_damage[2]
            return weapon_damage[2]


#for tiles with collision on
class Collision_Tile(pygame.sprite.Sprite):
    def __init__(self,groups, rx, ry, image, mask, collision_rect):
        super().__init__(groups)
        self.wall1 = pygame.image.load(image).convert_alpha()
        self.mask1 = pygame.image.load(mask).convert_alpha()
        self.mask2 = pygame.image.load(collision_rect).convert_alpha()
        self.rect = self.wall1.get_rect()
        
        self.mask = pygame.mask.from_surface(self.mask1)
        self.rect1 = self.mask2.get_rect()
        self.rxx = rx
        self.ryy = ry

        self.rect.x = rx#387 
        self.rect.y = ry#420
        self.rect1.x = rx#387 
        self.rect1.y = ry#420
    def update(self):
        self.old_rect = self.rect.copy()


#for tiles with collision off
class none_Collision_Tile(pygame.sprite.Sprite):
    def __init__(self,groups, rx, ry, image):
        super().__init__(groups)
        if loc == 'Aroyo':
            self.wall3 = pygame.image.load(image).convert_alpha()
            
            self.image = image
            self.rect = self.wall3.get_rect()
            self.rxx = rx
            self.ryy = ry 
            self.rect.x = rx#320
            self.rect.y = ry
    def update(self):
        if loc == 'Aroyo':
            self.wall3 = pygame.image.load(self.image).convert_alpha()
 
            self.rect = self.wall3.get_rect()

            self.rect.x = self.rxx 
            self.rect.y = self.ryy

#pause menu
class PauseMenu():
    def __init__(self):
        if paused == True:
            self.menu()
        self.clicked = False
        self.clicked2 = False
        self.clicked3 = False

    def menu(self):
        self.p = pygame.draw.rect(screen, (0,225,100), pygame.Rect(580, 300, 295, 95))
    def update(self):
        if paused == True:   
            self.menu()
            resume_btn.update()
            save_btn.update()
            load_btn.update()
            exit_btn.update()
            if resume_btn.draw():
                self.clicked = True
                self.resume()
            if save_btn.draw():
                self.clicked2 = True
                self.save()
            if load_btn.draw():
                self.clicked3 = True
                self.load()
            if exit_btn.draw():
                return True
        else:
            if self.clicked == True:
                self.clicked = False
            if self.clicked2 == True:
                self.clicked2 = False
            if self.clicked3 == True:
                self.clicked3 = False
    def resume(self):
        if self.clicked == True:
            print("true")
            
            return True
    def save(self):
        if self.clicked2:
            
            return True
            
    def load(self):
        if self.clicked3:
            
            return True
        
#btn for pause menu
class Btn(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image2 = image
        self.rx = x
        self.ry = y
        self.clicked = False
        if paused == True:
            self.menu()
    def menu(self):
        self.btn = pygame.image.load(self.image2).convert_alpha()
        self.rect = self.btn.get_rect()
        self.rect.x = self.rx
        self.rect.y = self.ry
        screen.blit(self.btn,self.rect)
        
    def update(self):
        if paused == True:
            self.menu()
        else:
            pass
    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.cliked = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.cliked = False
            return action

#pathfinder for enemy
class Pathfinder:
    def __init__(self, matrix, toBody):
        self.matrix = matrix
        self.grid = Grid(matrix=matrix)
        self.path = []

        self.ttoBody = pygame.sprite.GroupSingle(toBody)
        self.Body = toBody
        self.empty_path()
    def empty_path(self):
        self.path = []

    def create_path(self):
        # start
        start_x, start_y = self.ttoBody.sprite.get_coord()
        start_x, start_y = self.Body.get_coord()
        start = self.grid.node(start_x, start_y)

        # end
        mouse_pos = pygame.mouse.get_pos()
        self.amountxx = rand.randint(100,150)
        self.amountx = rand.randint(30,self.amountxx)
        self.amounty = rand.randint(30,80)
        self.minusOrPlus = rand.randint(0,1)
        if self.minusOrPlus == 0:
            self.px = player.rect.x - self.amountx
        else:
            self.px = player.rect.x + self.amountx
        self.py = player.rect.y + self.amounty
        end_x, end_y = self.px // 32, self.py // 32
        end = self.grid.node(end_x, end_y)

        # path
        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
        self.path, _ = finder.find_path(start, end, self.grid)
        self.grid.cleanup()
        self.ttoBody.sprite.set_path(self.path)
        self.Body.set_path(self.path)
    def update(self):
        self.ttoBody.update()
    
#enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self, group, rx, ry, hp, image_location, weapon, empty_path, id):
        super().__init__()
        self.did = 2
        self.direction = "right-down"
        
        self.isAnimating = False
        self.sprites = []
        for i in range(1,13):
          self.sprites.append(pygame.image.load(f"{image_location}/{self.did}/playerIdle ({i}).png"))
        self.currentSprite = 0
        self.image = self.sprites[self.currentSprite]

        self.clicked = False

        self.turn = False

        self.id = id

        self.rhp = hp

        self.speed = 3

        self.direction2 = pygame.math.Vector2(0,0)
        
        self.path = []
        self.collision_rects = []
        self.empty_path = empty_path

        self.moving = False

        self.rect = self.image.get_rect()

        self.rxx = rx
        self.ryy = ry
        self.rect.x = rx
        self.rect.y = ry

        
        self.pos = self.rect.center
        
        self.empty_path = empty_path

        self.path_index = 0
        
        self.isWeapon_anim = False

        self.degree = "down"
        self.frame = 0
        self.weapon = weapon
        self.damage = 3
        self.dead = False
        self.collision_rects = []
        self.empty_path = empty_path
        self.isShot = True




        self.isenDead = False
    def shoot(self):
        if self.weapon == "shotgun":
            self.damage = 10
            self.sprites.clear()
            self.isWeapon_anim = True
            
            if player.rect.x < self.rect.x and player.rect.y > self.rect.y -50 and player.rect.y < self.rect.y +50:
                for i in range(0,4):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/4/frame_{i}_delay-0.1s.png"))
                for i in range(0,4):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/shoot/4/frame_{i}_delay-0.1s.png"))
                for i in range(0,6):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/in/4/frame_{i}_delay-0.1s.png"))
            elif player.rect.x < self.rect.x and player.rect.y > self.rect.y:
                for i in range(0,4):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/3/frame_{i}_delay-0.1s.png"))
                for i in range(0,4):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/shoot/3/frame_{i}_delay-0.1s.png"))
                for i in range(0,6):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/in/3/frame_{i}_delay-0.1s.png"))
            elif player.rect.x < self.rect.x and player.rect.y > self.rect.y -50 and player.rect.y < self.rect.y +50:
                for i in range(0,4):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/1/frame_{i}_delay-0.1s.png"))
                for i in range(0,4):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/shoot/1/frame_{i}_delay-0.1s.png"))
                for i in range(0,6):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/in/1/frame_{i}_delay-0.1s.png"))
            elif player.rect.x > self.rect.x and player.rect.y > self.rect.y:
                for i in range(0,4):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/2/frame_{i}_delay-0.1s.png"))
                for i in range(0,4):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/shoot/2/frame_{i}_delay-0.1s.png"))
                for i in range(0,6):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/in/2/frame_{i}_delay-0.1s.png"))
            elif player.rect.x > self.rect.x and player.rect.y < self.rect.y:
                for i in range(0,4):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/0/frame_{i}_delay-0.1s.png"))
                for i in range(0,4):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/shoot/0/frame_{i}_delay-0.1s.png"))
                for i in range(0,6):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/in/0/frame_{i}_delay-0.1s.png"))
            elif player.rect.x < self.rect.x and player.rect.y < self.rect.y:
                
                for i in range(0,4):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/5/frame_{i}_delay-0.1s.png"))
                for i in range(0,4):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/shoot/5/frame_{i}_delay-0.1s.png"))
                for i in range(0,6):
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/in/5/frame_{i}_delay-0.1s.png"))

            return self.damage

    def isDead(self):
        for i in range(1,13):
            self.sprites.append(pygame.image.load("objects/animations/Dead/dead.png"))
        self.dead = True
    def animate(self):
        self.isAnimating = True

    def get_coord(self):
        col = self.rect.centerx // 32
        row = self.rect.centery // 32
        return (col,row)

    def set_path(self,path):
        self.path = path
        self.path_index = 0
        self.create_collision_rects()
        self.get_direction()

    def create_collision_rects(self):
        if self.path:
            self.collision_rects = []
            for point in self.path:
                x = (point[0] * 32) + 16
                y = (point[1] * 32) + 16
                rect = pygame.Rect((x - 2,y - 2),(4,4))
                self.collision_rects.append(rect)

    def get_direction(self):
            if self.collision_rects:
                start = pygame.math.Vector2(self.pos)
                end = pygame.math.Vector2(self.collision_rects[0].center)
                self.direction2 = (end - start).normalize()
            else:
                self.direction2 = pygame.math.Vector2(0,0)
                self.path = []

    def check_collisions(self):
        if self.collision_rects:
            for rect in self.collision_rects:
                if rect.collidepoint(self.pos):
                    del self.collision_rects[0]
                    self.get_direction()
        else:
            if self.empty_path == None:
                pass
            else:
                self.empty_path
    def direction_apply(self):
        
        if self.degree == 'right' and self.moving == True and self.rhp >= 0:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/1/frame_0{i}_delay-0.1s.png"))
        elif self.degree == 'down-Right' and self.moving == True and self.rhp >= 1:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/2/frame_0{i}_delay-0.1s.png"))
        elif self.degree == 'up-Right' and self.moving == True and self.rhp >= 1:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/0/frame_0{i}_delay-0.1s.png"))
        elif self.degree == 'down-Left' and self.moving == True and self.rhp >= 1:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/3/frame_0{i}_delay-0.1s.png"))
        elif self.degree == 'up-Left' and self.moving == True and self.rhp >= 1:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/m1/frame_0{i}_delay-0.1s.png"))
        elif self.degree == 'left' and self.moving == True and self.rhp >= 1:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load(f"objects/animations/Run/3/frame_0{i}_delay-0.1s.png"))
        elif self.moving == False and self.rhp >= 1:
            self.sprites.clear()
            for i in range(0,10):
                self.sprites.append(pygame.image.load("objects/animations/playerIdleSprites/2/playerIdle (1).png"))
                
    def direction_check(self):
        if self.dx > 0:
            if self.dy > 0:
                self.degree = 'down-Right'
            elif self.dy < 0:
                self.degree = 'up-Right'
            else:
                self.degree = 'right'
        if self.dx < 0:
            if self.dy > 0:
                self.degree = 'down-Left'
            elif self.dy < 0:
                self.degree = 'up-Left'
            else:
                self.degree = 'left'
             
    def update(self):
        self.old_rect = self.rect.copy()
        self.didit = False
        if self.currentSprite >= len(self.sprites):
            if self.isWeapon_anim == True:#self.degree == "down" and vvvvv
                if self.weapon == "shotgun" or self.weapon == 'rifle':
                    print('shoot')
                    self.isWeapon_anim = False
                    self.sprites.clear()
                    self.currentSprite = 0
                    self.sprites.append(pygame.image.load(f"objects/animations/rifle/in/2/frame_5_delay-0.1s.png"))

        if self.isAnimating == True:
            self.currentSprite += 0.3

            if self.currentSprite >= len(self.sprites):
                self.currentSprite = 0
                self.isAnimating = False
        self.image = self.sprites[int(self.currentSprite)]
        self.pos += self.direction2 * self.speed
        new_pos = self.pos
        self.check_collisions()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        
        self.rect.x = self.pos.x 
        self.rect.y = self.pos.y

        self.currentX = self.rect.x
        self.currentY = self.rect.y
        self.oldX = self.old_rect.x
        self.oldy = self.old_rect.y
        self.dx = self.currentX - self.oldX
        self.dy = self.currentY - self.oldy 
        if self.currentX - self.oldX == 0:
            self.moving = False
        else:
            self.moving = True
        self.direction_check()
        self.direction_apply()
        global gotAtPos
        if self.path == []:
            
            gotAtPos = True
        else:
            gotAtPos = False
        
        
        #print(self.rect.x, self.rect.y)
        if  new_pos.x <= 0 or new_pos.x > 1320 or new_pos.y <= 0 or new_pos.y > 920:
            self.pos.x = 300
            self.pos.y = 300
        
        pos = pygame.mouse.get_pos()
        global clicked
        action2 = False
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                global enemyid
                #global clicked
                clicked = True
                self.isShot = True
                action2 = True
                self.drawit() 
                enemyid = self.id
                self.clicked = True
                
                
                return action2
        if pygame.mouse.get_pressed()[0] == 0:
            #if pygame.mouse.get_pressed()[0] and self.clicked == True:
            self.clicked = False
            enemyid = self.id
            self.drawit()
            self.isShot = False
            clicked = False
            action2 = False
        
        
            return action2
            
    def drawit(self):
        if self.clicked == True:
            global enemyid
            print('clicked!!!!')
            enemyid = self.id
            global clicked
            clicked = False
            return True
        else:
            return False
class item(pygame.sprite.Sprite):
    def __init__(self, x, y, name, type, amount, ammo, dropped):
        super().__init__()
        self.image = pygame.image.load("objects/animations/Dead/dead.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.type = type
        self.amount = amount
        self.amount_max = 10
        self.clicked = False
        self.isDropped = dropped
        self.ammo_max = 0
        self.ammo = ammo
    def drop(self):
        inventory.remove(self)
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.isDropped = True
    def pickup(self):
        inventory.append(self)
        self.rect.x = 10000
        self.rect.y = 10000
        self.isDropped = False
    def update(self):
        if self.name == 'shotgun':
            if self.isDropped == True:
                self.image = pygame.image.load("objects/Items/Weapons/RIFLE.png")
            if self.isDropped == False:
                self.image = pygame.transform.scale(pygame.image.load("objects/ui/inv/items/SHOTGUN.png"), (135,44))
            self.ammo_max = 2
            self.type = 'weapon'
        if self.name == 'rifle':
            if self.isDropped == True:
                self.image = pygame.image.load("objects/Items/Weapons/RIFLE.png")
            if self.isDropped == False:
                self.image = pygame.transform.scale(pygame.image.load("objects/ui/inv/items/ASSRIFL2.png"), (135,44))
            self.ammo_max = 30
            self.type = 'weapon'
        if self.name == '5mm Ammo':
            if self.isDropped == True:
                self.image = pygame.image.load("objects/Items/ammo/5mm.png")
            if self.isDropped == False:
                self.image = pygame.transform.scale(pygame.image.load("objects/ui/inv/items/5MMAP.png"), (135,62))
            #self.ammo = 60 
            self.type = 'ammo'
        if self.name == 'shotgun shells':
            if self.isDropped == True:
                self.image = pygame.image.load("objects/Items/ammo/5mm.png")
            if self.isDropped == False:
                self.image = pygame.transform.scale(pygame.image.load("objects/ui/inv/items/SHELLS.png"), (135,62))
            #self.ammo = 60 
            self.type = 'ammo'
        if self.type == 'weapon':
            self.amount_max = 10
        if self.type == 'aid':
            self.amount_max = 100 
        if self.type == 'ammo':
            pass
        mousepos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousepos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.pickup()
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        screen.blit(self.image, self.rect)
class inventoryGui(pygame.sprite.Sprite):
    def __init__(self, inv_list):
        super().__init__()
        self.toggled = False
        
        self.inv_list = inv_list
        self.list_position = (1320/2 - 699/2, 920/2 - 577/2)
        self.list_size = (120, 420)
        self.list_font = pygame.font.SysFont(None, 24)
        self.list_item_height = 30
        self.box_position = (1320/2 - 699/2, 920/2 - 577/2)
        self.box_size = (120, 420)
        self.box_color = (255, 255, 255)
        self.box_thickness = 2
        self.clickable_rects = []
        self.list_font = pygame.font.SysFont('fallouty', 24)
        self.clicked1 = False
        self.clicked2 = False
        self.clicked3 = False
        self.clicked4 = False
        self.clicked5 = False
        self.clicked6 = False
        self.clicked7 = False
        self.clicked8 = False
        self.clicked9 = False
        self.button1down = False
        self.button2down = False
        self.search_ammo = False
        self.isOnUsing = False
        self.isOnInv = False
        self.cooldown = 500
        self.display_use = False
        self.display_use2 = False
        self.item_id = 1
        self.item_is = None
        self.ammo_name = None
        self.weapon_ammo_need = None
        self.item_reload = None
        
    def toggle_on(self):
        self.invbox = pygame.transform.scale(pygame.image.load('objects/ui/inv/inv.png'), (899,777))
        self.rect = self.invbox.get_rect()
        self.rect.x = 1320/2 - 899/2
        self.rect.y = 920/2 - 777/2
        
        #manager = pygame_gui.UIManager(screen_size)
        #cont = manager.get_root_container() 
        #self.button_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screen_W/2-199, screen_H/2-163), (100, 50)),
         #                               text='exit', manager=manager,
          #                              container=cont,
           #                             anchors={'bottom': 'bottom',
            #                                     'top': 'top'})

        # Calculate the visible items within the box
              # New list to store clickable regions

        x, y = 1320/2 - 699/2 - 30, 920/2 - 577/2
        x2,y2 = 1320/2 - 699/2 + 200, 920/2 - 577/2 + 530
        global current_page 
        global inventory
        global inventory_width
        global inventory_height
        global using_item
        item_spacing = 10
        item_count = len(inventory)
        start_index = current_page * inventory_width * inventory_height
        end_index = min(start_index + (inventory_width * inventory_height), item_count)

        for i in range(start_index, end_index):
            item = inventory[i]
            item_rect = item.image.get_rect().move(x, y)
            
            screen.blit(item.image, (x, y))

            if item_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked1 == False:
                    
                    #self.cooldown = 0
                    #if self.cooldown == 0:
                     #   pass
                    #self.displayoptionsonmouse(item)
                    self.handle_item_click(item)
                    print('Ammo is: ' + str(item.ammo))
                    self.clicked1 = True
                if pygame.mouse.get_pressed()[0] == 0:
                    #self.cooldown = 500
                    self.clicked1 = False
            if item_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[2] == 1 and self.clicked4 == False:
                    self.cooldown -= 100
                    if self.cooldown <= 0:
                        self.item_id = i
                        self.item_is = item
                        self.display_use = True
                        self.displayoptionsonmouse(item)
                        self.clicked4 = True
                if pygame.mouse.get_pressed()[2] == 0:
                    self.display_use = False
                    self.cooldown = 500
                    self.clicked4 = False
                    
            x += item.image.get_width() + item_spacing
            if (i + 1) % inventory_width == 0:
                x -= 140
                y += item.image.get_height() + item_spacing

        # Draw navigation buttons
        if self.button1down == True:
            self.invupout = pygame.image.load('objects/ui/inv/INVDNIN.png')
        else:
            self.invupout = pygame.image.load('objects/ui/inv/INVDNOUT.png')
        next_button_rect = self.invupout.get_rect()
        next_button_rect.x = 1320/2 - 699/2 + 130
        next_button_rect.y = 920/2 - 577/2 
        screen.blit(self.invupout, next_button_rect)
        if self.button2down == True:
            self.invdownout = pygame.image.load('objects/ui/inv/INVUPIN.png')
        else:
            self.invdownout = pygame.image.load('objects/ui/inv/INVUPDS.png')
        prev_button_rect = self.invupout.get_rect()
        prev_button_rect.x = 1320/2 - 699/2 + 130
        prev_button_rect.y = 920/2 - 577/2 - 30
        screen.blit(self.invdownout, prev_button_rect)
        #next_button_rect = pygame.Rect(700, 500, 80, 40)
        #pygame.draw.rect(screen, (255, 0, 0), next_button_rect)
        #pygame.draw.rect(screen, (0, 0, 0), next_button_rect, 3)
        #pygame.draw.polygon(screen, (0, 0, 0), ((720, 515), (720, 525), (730, 520)))
        #prev_button_rect = pygame.Rect(700, 420, 80, 40)
        #pygame.draw.rect(screen, (255, 0, 0), prev_button_rect)
        #pygame.draw.rect(screen, (0, 0, 0), prev_button_rect, 3)
        #pygame.draw.polygon(screen, (0, 0, 0), ((720, 445), (720, 435), (710, 440)))

        # Check for button clicks
        try:
            if using_item[0] != None:
                using_item_rect = using_item[0].image.get_rect().move(x2, y2)
                screen.blit(using_item[0].image, using_item_rect)
                if using_item_rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[2] == 1 and self.clicked6 == False:
                        self.item_is = using_item[0]
                        self.displayoptionsonmouse(using_item[0])
                        self.display_use2 = True

        except IndexError:
                pass
        if next_button_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked2 == False:
                self.clicked2 = True
                self.button1down = True
                if item_count > 1:
                    current_page = (current_page + 1) % ((item_count - 1) // (inventory_width * inventory_height) + 1)
            if pygame.mouse.get_pressed()[0] == 0:
                self.button1down = False
                self.clicked2 = False
        elif prev_button_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked3 == False:
                self.button2down = True
                self.clicked3 = True
                if item_count > 1:
                    current_page = (current_page - 1) % ((item_count - 1) // (inventory_width * inventory_height) + 1)
            if pygame.mouse.get_pressed()[0] == 0:
                self.button2down = False
                self.clicked3 = False
        
        if self.display_use == True:
            xxpos = pygame.mouse.get_pos()
            screen.blit(self.use,self.userect)
            screen.blit(self.info,self.inforect)
            if self.item_is.type == 'weapon':
                screen.blit(self.reload,self.reloadrect)
            screen.blit(self.drop,self.droprect)
            if self.userect.collidepoint(xxpos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked5 == False:
                    print('used' + str(item.name))
                    self.clicked5 = True
                    self.display_use = False
                    if len(using_item) >= 1:
                        try:
                            inventory.append(using_item[0])
                            inventory.remove(inventory[self.item_id])
                            using_item.clear()
                        except IndexError:
                            print('error')
                    else:
                        inventory.remove(inventory[self.item_id])
                    using_item.append(self.item_is) 
                    
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked5 = False
            if self.reloadrect.collidepoint(xxpos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked9 == False:
                    self.clicked9 = True
                    self.item_reload = item
                    self.display_use = False
                    self.weapon_ammo_need = self.item_is.name
                    self.search_ammo = True
                    self.isOnInv = True
                    #if self.search_ammo == False:
                        
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked9 = False

        print(self.weapon_ammo_need)
        if self.display_use2 == True:
            xxpos = pygame.mouse.get_pos()
            screen.blit(self.use,self.userect)
            screen.blit(self.info,self.inforect)
            if self.item_is.type == 'weapon':
                screen.blit(self.reload,self.reloadrect)
            screen.blit(self.drop,self.droprect)
            if self.userect.collidepoint(xxpos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked7 == False:
                    print('used' + str(item.name))
                    self.clicked7 = True
                    self.display_use2 = False
                    if len(using_item) >= 1:
                        try:
                            inventory.append(using_item[0])
                            #inventory.remove(item)
                            using_item.clear()
                            #using_item[0] = None
                            print(using_item)
                        except IndexError:
                            print('error')

                    #using_item.append(item) 
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked7 = False
            if self.reloadrect.collidepoint(xxpos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked8 == False:
                    self.clicked8 = True
                    self.item_reload = item
                    self.weapon_ammo_need = self.item_is.name
                    self.display_use2 = False
                    self.search_ammo = True
                    self.isOnUsing = True
                    #if self.search_ammo == False:
                        
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked8 = False
                    #using_item[0]
        if self.search_ammo == True:
            for ammo in inventory:
                if ammo.type == 'ammo':
                    if ammo.name == '5mm Ammo' and self.weapon_ammo_need == 'rifle':
                        
                        self.ammo_name = ammo
                        self.search_ammo = False
                        if self.isOnUsing == True:
                            print('did')
                            print(ammo.ammo)
                            ammo.ammo -= using_item[0].ammo_max - using_item[0].ammo
                            using_item[0].ammo += using_item[0].ammo_max - using_item[0].ammo
                            print(ammo.ammo)
                            if self.ammo_name.ammo < 0:
                                using_item[0].ammo -= 1
                                self.ammo_name.ammo += 1
                            if self.ammo_name.ammo == 0:
                                inventory.remove(self.ammo_name)
                            self.isOnUsing = False
                        if self.isOnInv == True:
                            self.ammo_name.ammo -= inventory[self.item_id].ammo_max - inventory[self.item_id].ammo
                            inventory[self.item_id].ammo += inventory[self.item_id].ammo_max - inventory[self.item_id].ammo
                            if self.ammo_name.ammo < 0:
                                using_item[0].ammo -= 1
                                self.ammo_name.ammo += 1
                            if self.ammo_name.ammo == 0:
                                inventory.remove(self.ammo_name)
                            self.isOnInv = False
                        
                        break
                    if ammo.name == 'shotgun shells' and self.weapon_ammo_need == 'shotgun':
                        self.ammo_name = ammo
                        self.search_ammo = False
                        if self.isOnUsing == True:
                            #print('did')
                            #print(ammo.ammo)
                            
                            try:
                                ammo.ammo -= using_item[0].ammo_max - using_item[0].ammo
                                using_item[0].ammo += using_item[0].ammo_max - using_item[0].ammo
                            except IndexError:
                                self.isOnUsing = False
                            #print(ammo.ammo)
                            if self.ammo_name.ammo < 0:
                                using_item[0].ammo -= 1
                                self.ammo_name.ammo += 1
                            if self.ammo_name.ammo == 0:
                                inventory.remove(self.ammo_name)
                            self.isOnUsing = False
                        if self.isOnInv == True:
                            ammo.ammo -= inventory[self.item_id].ammo_max - inventory[self.item_id].ammo
                            inventory[self.item_id].ammo += inventory[self.item_id].ammo_max - inventory[self.item_id].ammo
                            if self.ammo_name.ammo < 0:
                                ammo.ammo -= 1
                                self.ammo_name.ammo += 1
                            if self.ammo_name.ammo == 0:
                                inventory.remove(self.ammo_name)
                            self.isOnInv = False
                        
                        break
                        
    def handle_item_click(self,item):
        
        print("Clicked item:", item.name)
        print("Clicked item:", item.ammo)
    def displayoptionsonmouse(self,item):
        pos = pygame.mouse.get_pos()
        self.use = pygame.image.load('objects/ui/inv/USEGETN.png')
        self.info = pygame.image.load('objects/ui/inv/LOOKN.png')
        self.reload = pygame.image.load('objects/ui/inv/LOADN.png')
        self.drop = pygame.image.load('objects/ui/inv/DROPN.png')

        self.userect = self.use.get_rect()
        self.inforect = self.info.get_rect()
        self.reloadrect = self.reload.get_rect()
        self.droprect = self.drop.get_rect()

        self.userect.x = pos[0]
        self.userect.y = pos[1] - 160#100
        self.inforect.x = pos[0]
        self.inforect.y = pos[1] - 120#140
        self.reloadrect.x = pos[0]
        self.reloadrect.y = pos[1] - 80#180
        self.droprect.x = pos[0]
        self.droprect.y = pos[1] - 40#220
        
        
        
    def update(self):
        if self.toggled == True:
            self.toggle_on()
    

class online_player(pygame.sprite.Sprite):
    def __init__(self, x, y, location, current_sprite, idd):
        super().__init__()
        self.current_sprite_id = current_sprite
        self.current_sprite = pygame.image.load(self.current_sprite_id)
        self.rect = self.current_sprite.get_rect()
        self.x = x
        self.y = y
        self.location = location
        self.id = idd
        self.has_turn = False
        self.clicked = False
        self.got_shot = False
    def update(self):
        self.current_sprite = pygame.image.load(self.current_sprite_id)
        self.rect = self.current_sprite.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.got_shot = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            self.got_shot = False
        font = pygame.font.Font('objects/fonts/Fonts/r_fallouty.ttf', 20)
        text_color = (255, 255, 255)
        text = self.id
        text_color = (255, 255, 255)  # White color

        text_surface = font.render(text, True, text_color)
        screen.blit(text_surface, (self.rect.x, self.rect.y))
        
        
        #if loc == self.location:
        screen.blit(self.current_sprite,plrs.rect)

    
class worldmap(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()      
        #self.mapBox = pygame.image.load('objects/ui/WMAPBOX.jpg')
        self.mapBox = pygame.transform.scale(pygame.image.load('objects/ui/WMAPBOX.png'), (940,780))
        #self.map1 = pygame.image.load('objects/ui/WRLDMP09.jpg')
        self.map1 = pygame.transform.scale(pygame.image.load('objects/ui/WRLDMP09.jpg'), (550,550))

        self.rect1 = self.mapBox.get_rect()
        self.rect2 = self.map1.get_rect()
        
        self.rect1.x = screen_W/2 - self.rect1.width/2
        self.rect1.y = screen_H/2 - self.rect1.height/2

        self.rect2.x = screen_W/2 - self.rect2.width/2 - 100
        self.rect2.y = screen_H/2 - self.rect2.height/2

    def MapUi(self):
        pass

    def update(self):
        if loc == 'wordmp':
            screen.blit(self.map1, self.rect2)
            screen.blit(self.mapBox, self.rect1)
#wayp
class mapWP(pygame.sprite.Sprite):
    def __init__(self, x, y, loc):
        super().__init__()
        self.image = pygame.image.load('objects/ui/mapWp.png')
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.location = 'Aroyo'
        self.x = x
        self.y = y 
        self.location = loc
        self.rect.x,self.rect.y = self.x,self.y
    def update(self):
        if loc == 'wordmp':
            screen.blit(self.image, self.rect)
class mainmenu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('objects/ui/menu.png')
        self.playbutton = pygame.image.load('objects/ui/menu/Button.png')
        self.rect = self.image.get_rect()
        self.rect2 = self.playbutton.get_rect()
        self.rect3 = self.playbutton.get_rect()
        self.rect.x, self.rect.y = screen_W / 2 - 795/2, screen_H / 2 - 491/2
        
        self.rect2.x, self.rect2.y = screen_W / 2 - 41/2 + 160, screen_H / 2 - 36/2 - 180

        self.rect3.x, self.rect3.y = screen_W / 2 - 41/2 + 160, screen_H / 2 - 36/2 - 130

        clicked9 = False
    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.playbutton, self.rect2)
        screen.blit(self.playbutton, self.rect3)

        if self.rect3.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked9 == False:
                global playing
                self.clicked9 = True
                playing = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked9 = False
        if self.rect2.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked9 == False:
                #global playing
                global playing_online 
                global loc
                self.clicked9 = True
                playing = True
                playing_online = True
                loc = 'Aroyo_online'
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked9 = False
class iface(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('objects/ui/iface/IFACE.jpg')
        self.wepB = pygame.image.load('objects/ui/iface/SATTKBUP.jpg')
        try:

            self.wep = using_item[0].image
            self.rect3 = self.wep.get_rect()
        except IndexError:
            self.wep = pygame.image.load('objects/ui/menu/button2.png')
            self.rect3 = self.wep.get_rect()
        self.rect = self.image.get_rect()
        self.rect2 = self.wepB.get_rect()
        
        self.rect.x, self.rect.y = screen_W / 2 - 640/2, screen_H - 99
        
        self.rect2.x, self.rect2.y = screen_W / 2 - 188/2 + 40, screen_H - 70

        self.rect3.x, self.rect3.y = screen_W / 2 - 185/2, screen_H - 54 * 2
    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.wepB, self.rect2)
        screen.blit(self.wep,self.rect3)
        
        try:

            self.wep = using_item[0].image
            self.rect3 = self.wep.get_rect()
        except IndexError:
            self.wep = pygame.image.load('objects/ui/menu/button2.png')
            self.rect3 = self.wep.get_rect()
        self.rect3.x, self.rect3.y = screen_W / 2 - 185/2 + 60, screen_H - 54 * 1.2
class Save_load_system(pygame.sprite.Sprite):
    def __init__(self, save_or_load):
        super().__init__()
        #if true save else load
        self.save_or_load = save_or_load
        self.image = pygame.transform.scale(pygame.image.load('objects/ui/saveSystem/LSGAME.jpg'), (1280,960))
        self.sav_btn = pygame.transform.scale(pygame.image.load('objects/ui/Btns/TINREDUP.jpg'), (28,28))
        self.can_btn = pygame.transform.scale(pygame.image.load('objects/ui/Btns/TINREDUP.jpg'), (28,28))
        self.rect = self.image.get_rect()
        self.sav_btn_rect = self.sav_btn.get_rect()
        self.can_btn_rect = self.can_btn.get_rect()

        self.rect.center = (screen_W / 2, screen_H / 2)
        
        self.sav_btn_rect.center = (screen_W / 2 + 160, screen_H / 2 + 230)

        self.can_btn_rect.center = (screen_W / 2 + 370, screen_H / 2 + 230)

        font_path = "objects/fonts/Fonts/TT0807M_.TTF"  # Update this with your actual font file path
            
        font_path2 = "objects/fonts/Fonts/JH_FALLOUT.TTF"
        if self.save_or_load:
            

            # Load the font
            font = pygame.font.Font(font_path, 36)  # Adjust the size as needed

            # Now you can use the 'font' object to render text
            self.text_surface = font.render("Save Game", True, (252, 240, 131))
            self.text_rect = self.text_surface.get_rect()
            self.text_rect.center = (200, 50)
        self.clicked = False
        self.sav_box_open = False
        self.save_selection = None
    def update(self):
        if self.save_or_load:
            screen.blit(self.image, self.rect)
            screen.blit(self.text_surface, self.text_rect)
        screen.blit(self.sav_btn, self.sav_btn_rect)
        screen.blit(self.can_btn, self.can_btn_rect)
        
        for i in saves:
            i.update()
            if i.got_clicked == True:
                self.save_selection = i
                print(i)
                i.got_clicked = False
        number_of_times_looped = 0
        if self.sav_btn_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                global typing
                self.clicked = True
                self.sav_btn = pygame.transform.scale(pygame.image.load('objects/ui/Btns/TINREDDN.jpg'), (28,28))
                typing = True
                self.sav_box_open = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.sav_btn = pygame.transform.scale(pygame.image.load('objects/ui/Btns/TINREDUP.jpg'), (28,28))
                self.clicked = False
        if self.can_btn_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                global loc
                global in_save
                in_save = False
                loc = 'Aroyo'
                self.clicked = False
                
                self.can_btn = pygame.transform.scale(pygame.image.load('objects/ui/Btns/TINREDDN.jpg'), (28,28))
                
            if pygame.mouse.get_pressed()[0] == 0:
                
                print(in_save)
                self.can_btn = pygame.transform.scale(pygame.image.load('objects/ui/Btns/TINREDUP.jpg'), (28,28))
                
        if self.sav_box_open:
            sav_box.update()
        for filename in os.listdir('SAVES/'):
            if filename.endswith('.pkl'):
                
                with open(f'SAVES/{filename}', 'rb') as file:
                    loaded_data = pickle.load(file)
                    if loaded_data['isLoadable'] == True:
                        saves[number_of_times_looped].name = loaded_data['save_name']
                    number_of_times_looped += 1
class save_name_box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('objects/ui/saveSystem/LSGBOX.jpg'), (580,170))
        self.btn = pygame.transform.scale(pygame.image.load('objects/ui/Btns/TINREDUP.jpg'), (28,28))


        self.rect = self.image.get_rect()
        self.rect2 = self.btn.get_rect()

        self.rect.center = (screen_W / 2, screen_H / 2)

        self.rect2.center = (screen_W / 2, screen_H / 2 + 100)
        
        font_path = "objects/fonts/Fonts/TT0807M_.TTF"  # Update this with your actual font file path
            
        font_path2 = "objects/fonts/Fonts/JH_FALLOUT.TTF"
        # Load the font
        self.font = pygame.font.Font(font_path, 36)  # Adjust the size as needed

        # Now you can use the 'font' object to render text
        self.text_surface = self.font.render("Choose a name", True, (252, 240, 131))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (screen_W / 2, screen_H / 2 - 200)

        
        
        self.clicked = False
    def update(self):
        global sav_text
        self.text_surface2 = self.font.render(sav_text, True, (252, 240, 131))
        self.text_rect2 = self.text_surface2.get_rect()
        self.text_rect2.center = (screen_W / 2, screen_H / 2)
        screen.blit(self.image, self.rect)
        screen.blit(self.text_surface, self.text_rect)
        screen.blit(self.text_surface2, self.text_rect2)
        screen.blit(self.btn, self.rect2)

        if self.rect2.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.btn = pygame.transform.scale(pygame.image.load('objects/ui/Btns/TINREDDN.jpg'), (28,28))
                self.clicked = True
                if len(sav_text) > 0:
                    enemies_save = {}
                    enemy_save1 = {}
                    inv_save = {}
                    inv_save1 = {}
                    using_item_save = {}
                    using_item_save1 = {}

                    enemy_coun = 0
                    inv_coun = 0
                    using_item_coun = 0
                    for i in enemies_a:
                        enemy_coun += 1
                        enemies_save['enemy' + str(enemy_coun)] = enemy_save1['enemyx' + str(enemy_coun)] = i.rect.x#or currentX
                        enemies_save['enemy' + str(enemy_coun)] = enemy_save1['enemyy' + str(enemy_coun)] = i.rect.y
                        enemies_save['enemy' + str(enemy_coun)] = enemy_save1['enemyhp' + str(enemy_coun)] = i.rhp
                        enemies_save['enemy' + str(enemy_coun)] = enemy_save1['enemyx' + str(enemy_coun)],enemy_save1['enemyy' + str(enemy_coun)],enemy_save1['enemyhp' + str(enemy_coun)]
                    
                    for i in inventory:
                        inv_coun += 1
                        inv_save['item' + str(inv_coun)] = inv_save1['item_name' + str(inv_coun)] = i.name
                        inv_save['item' + str(inv_coun)] = inv_save1['item_x' + str(inv_coun)] = i.rect.x
                        inv_save['item' + str(inv_coun)] = inv_save1['item_y' + str(inv_coun)] = i.rect.y
                        inv_save['item' + str(inv_coun)] = inv_save1['item_type' + str(inv_coun)] = i.type
                        inv_save['item' + str(inv_coun)] = inv_save1['item_dropped' + str(inv_coun)] = i.isDropped
                        inv_save['item' + str(inv_coun)] = inv_save1['item_amount' + str(inv_coun)] = i.amount
                        inv_save['item' + str(inv_coun)] = inv_save1['item_ammo' + str(inv_coun)] = i.ammo
                        inv_save['item' + str(inv_coun)] = inv_save1['item_name' + str(inv_coun)], inv_save1['item_x' + str(inv_coun)], inv_save1['item_y' + str(inv_coun)], inv_save1['item_type' + str(inv_coun)], inv_save1['item_dropped' + str(inv_coun)], inv_save1['item_amount' + str(inv_coun)], inv_save1['item_ammo' + str(inv_coun)]
                    
                    for i in using_item:
                        using_item_coun += 1
                        using_item_save['item' + str(inv_coun)] = using_item_save1['item_name' + str(inv_coun)] = i.name
                        using_item_save['item' + str(inv_coun)] = using_item_save1['item_x' + str(inv_coun)] = i.rect.x
                        using_item_save['item' + str(inv_coun)] = using_item_save1['item_y' + str(inv_coun)] = i.rect.y
                        using_item_save['item' + str(inv_coun)] = using_item_save1['item_type' + str(inv_coun)] = i.type
                        using_item_save['item' + str(inv_coun)] = using_item_save1['item_dropped' + str(inv_coun)] = i.isDropped
                        using_item_save['item' + str(inv_coun)] = using_item_save1['item_amount' + str(inv_coun)] = i.amount
                        using_item_save['item' + str(inv_coun)] = using_item_save1['item_ammo' + str(inv_coun)] = i.ammo
                        using_item_save['item' + str(inv_coun)] = using_item_save1['item_name' + str(inv_coun)], using_item_save1['item_x' + str(inv_coun)], using_item_save1['item_y' + str(inv_coun)], using_item_save1['item_type' + str(inv_coun)], using_item_save1['item_dropped' + str(inv_coun)], using_item_save1['item_amount' + str(inv_coun)], using_item_save1['item_ammo' + str(inv_coun)]
                    
                    to_save = {
                        #if is loadable False then dont Load
                        "isLoadable" : True,
                        "loc" : loc,
                        "cmb" : inCombat,
                        "plrhp" : player.hp,
                        "plrx" : player.rect.x,
                        "plry" : player.rect.y,
                        "inv" : inv_save,
                        "invcur" : using_item_save,
                        "enemies" : enemies_save,
                        "save_name" : sav_text
                    }
                    for enemy, enemy1 in enemies_save.items():
                        print(f'{enemy} : {enemy1[0]}')
                    #print(enemies_save['enemy1'])
                    
                    enemies_to_save = {
                        
                    }
                    
                    with open(f'{save_game.save_selection.file}', 'wb') as file:
                        pickle.dump(to_save, file)
            if pygame.mouse.get_pressed()[0] == 0:
                self.btn = pygame.transform.scale(pygame.image.load('objects/ui/Btns/TINREDUP.jpg'), (28,28))
                self.clicked = False
class save_load_item(pygame.sprite.Sprite):
    def __init__(self, x, y, name, file):
        super().__init__()
        self.x = x
        self.y = y
        self.name = name
        self.file = file

        self.clicked = False

        self.got_clicked = False

        font_path = "objects/fonts/Fonts/TT0807M_.TTF"  # Update this with your actual font file path
            
        

        # Load the font
         # Adjust the size as needed

        # Now you can use the 'font' object to render text
        
    def update(self):
        font_path2 = "objects/fonts/Fonts/JH_FALLOUT.TTF"
        font = pygame.font.Font(font_path2, 20) 
        self.text_surface = font.render(f"{self.name}", True, (0, 255, 0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.x, self.y)
        screen.blit(self.text_surface, self.text_rect)
        if self.text_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.got_clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
inventory_width = 1  # Maximum number of items per row
inventory_height = 10  # Maximum number of rows
current_page = 0
#change enemy Turn
def socket_thread(client_socket2):
    try:
        global data
        data = client_socket2.recv(1024)#.decode()
        # Process the received data as needed
        #print("Received data:", data)
    except Exception as e:
        #print("An error occurred:", str(e))
        pass
def changeTurn(enemy_input):
    global turn
    global hp
    global gotAtPos
    global enemy_counter
    global pathfinder_list
    global first_Time
    #enemy_counter = 1
    global ap

    print(1)
    #+2
    if enemy_counter >= len(enemies_a) +3:
        turn = 0 
        enemy_counter = 0
        first_Time = True
        player.turn = True
        enemy_input.turn = False    
        
    else:
        print("first time:" + str(first_Time))
        if first_Time:
            
            first_Time = False
            #-2
            if enemy_counter == 0:
                enemy_counter += 1
            try:
                pathfinder_list[enemy_counter].create_path()
            except IndexError:
                try:
                    pathfinder_list[enemy_counter-3].create_path()
                except IndexError:
                    try:
                        pathfinder_list[enemy_counter-4].create_path()
                    except IndexError:
                        try:
                            pathfinder_list[enemy_counter-2].create_path()
                        except IndexError:
                            pathfinder_list[0].create_path()
            
                        
                        
        else:
            enemy_counter += 1
            print(2)
            try:
                pathfinder_list[enemy_counter].create_path()
            except IndexError:
                try:
                    if pathfinder_list[enemy_counter-3] != None:
                        pathfinder_list[enemy_counter-3].create_path()
                    else:
                        pathfinder_list[enemy_counter-2].create_path()
                except IndexError:
                    try:
                        pathfinder_list[enemy_counter-4].create_path()
                    except IndexError:
                        try:
                            pathfinder_list[enemy_counter-2].create_path()
                        except IndexError:
                            pathfinder_list[0].create_path()
            if enemy_counter >= len(enemies_a):
                first_Time = True
                        
                    #if gotAtPos == True and not first_Time:
                     
        if gotAtPos == True:
            t_end = time.time() + 10
            if time.time() < t_end:
                print("enemy_counter is at: " + str(enemy_counter))
                        
                test = enemy_input.shoot()
                player.hp -= test
                print('did damage: ' + str(test)) 
                print('your hp is:'+ str(hp))
                turn = enemy_counter
                ap = max_ap
                gotAtPos = False
                enemy_input.turn = False
                try:
                    enemies_a[enemy_counter].turn = True
                except IndexError:
                    player.turn = True



#matrix for path finder
matrix = [
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


#tiles sprite set up
doorframe_img = 'objects/tiles/walls/junk_walls/metal_door_frame.png'

##screen setup

moveAmount = 10
moveX = 0
moveY = 0
screen_W = 1320
screen_H = 920
screen_size = (screen_W,screen_H)
back = pygame.display.set_mode((screen_W,screen_H))
screen = pygame.display.set_mode((screen_W,screen_H), pygame.SRCALPHA)





pygame.display.set_caption('Fallout')

#pause menu
paused = False

#Gui gfx
pm = PauseMenu()
resume_img = "objects/Resume_Btn.png"
exit_img = "objects/Exit_Btn.png"
save_img = "objects/save_Btn.png"
load_img = "objects/load_Btn.png"
resume_btn = Btn(580, 300, resume_img) 
save_btn = Btn(580, 400, save_img)
load_btn = Btn(580, 500, load_img)
exit_btn = Btn(580, 600, exit_img) 


#location management
loc = '' 
#Group
all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()
item_sprites = pygame.sprite.Group()
npc_sprites = pygame.sprite.Group()
none_collision_sprites = pygame.sprite.Group()
player_g = pygame.sprite.Group()

#set Player to player
player = Player((player_g), (collision_sprites))

if loc == 'Aroyo':
    #Arroyo buildings
    floor_1 = none_Collision_Tile((all_sprites, none_collision_sprites), 225, 400, 'objects/tiles/Floors/Main/Floor1.png')

    floor_2 = none_Collision_Tile((all_sprites, none_collision_sprites), 295, 430, 'objects/tiles/Floors/Main/Floor1.png')

    floor_3 = none_Collision_Tile((all_sprites, none_collision_sprites), 305, 350, 'objects/tiles/Floors/Main/Floor1.png')

    floor_4 = none_Collision_Tile((all_sprites, none_collision_sprites), 225, 400, 'objects/tiles/Floors/Main/Floor1.png')

    floor_5 = none_Collision_Tile((all_sprites, none_collision_sprites), 225, 400, 'objects/tiles/Floors/Main/Floor1.png')

    floor_6 = none_Collision_Tile((all_sprites, none_collision_sprites), 225, 400, 'objects/tiles/Floors/Main/Floor1.png')

    floor_7 = none_Collision_Tile((all_sprites, none_collision_sprites), 225, 400, 'objects/tiles/Floors/Main/Floor1.png')

    floor_8 = none_Collision_Tile((all_sprites, none_collision_sprites), 225, 400, 'objects/tiles/Floors/Main/Floor1.png')

    wall_one = Collision_Tile((all_sprites, collision_sprites), 387, 420, 'objects/tiles/walls/junk_walls/junk_wall1.png','objects/tiles/walls/junk_walls/junk_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')

    wall_two = Collision_Tile((all_sprites, collision_sprites), 227, 380, 'objects/tiles/walls/junk_walls/junk_wall1.png','objects/tiles/walls/junk_walls/junk_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')

    wall_three = Collision_Tile((all_sprites, collision_sprites), 480, 442, "objects/tiles/walls/junk_walls/junk_wall1.png","objects/tiles/walls/junk_walls/junk_wall_mask.png",'objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')

    #wall_fore = Collision_Tile((all_sprites, collision_sprites), 481, 281, 'objects/tiles/walls/junk_walls/metal_wall.png','objects/tiles/walls/junk_walls/metal_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')

    wall_five = Collision_Tile((all_sprites, collision_sprites), 707, 325, 'objects/tiles/walls/junk_walls/junk_wall1b.png','objects/tiles/walls/junk_walls/junk_wall_mask_b.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')

    #wall_six = Collision_Tile((all_sprites, collision_sprites), 389, 346, 'objects/tiles/walls/junk_walls/junk_wall1.png','objects/tiles/walls/junk_walls/junk_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')

    wall_seven = Collision_Tile((all_sprites, collision_sprites), 614, 400, 'objects/tiles/walls/junk_walls/junk_wall1b.png','objects/tiles/walls/junk_walls/junk_wall_mask_b.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')

    wall_eight = Collision_Tile((all_sprites, collision_sprites), 565, 464, 'objects/tiles/walls/junk_walls/metal_wall.png','objects/tiles/walls/junk_walls/metal_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')

    wall_nine = Collision_Tile((all_sprites, collision_sprites), 229, 300, 'objects/tiles/walls/junk_walls/junk_wall1b.png','objects/tiles/walls/junk_walls/junk_wall_mask_b.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')

    wall_ten = Collision_Tile((all_sprites, collision_sprites), 319, 227, 'objects/tiles/walls/junk_walls/junk_wall1b.png','objects/tiles/walls/junk_walls/junk_wall_mask_b.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')

    wall_eleven = Collision_Tile((all_sprites, collision_sprites), 414, 226, 'objects/tiles/walls/junk_walls/junk_wall1.png','objects/tiles/walls/junk_walls/junk_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')

    wall_twelve = Collision_Tile((all_sprites, collision_sprites), 507, 249, 'objects/tiles/walls/junk_walls/junk_wall1.png','objects/tiles/walls/junk_walls/junk_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')

    wall_thirtn = Collision_Tile((all_sprites, collision_sprites), 598, 272, 'objects/tiles/walls/junk_walls/junk_wall1.png','objects/tiles/walls/junk_walls/junk_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')

    wall_fortn = Collision_Tile((all_sprites, collision_sprites), 690, 296, 'objects/tiles/walls/junk_walls/junk_wall1.png','objects/tiles/walls/junk_walls/junk_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')

    wall_fivetn = Collision_Tile((all_sprites, collision_sprites), 753, 318, 'objects/tiles/walls/junk_walls/metal_wall.png','objects/tiles/walls/junk_walls/metal_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')
    
    wall_drf = none_Collision_Tile((all_sprites, none_collision_sprites), 320, 304, doorframe_img)
                
    wall_sw = Collision_Tile((all_sprites,collision_sprites), 395, 252, "objects/tiles/walls/junk_walls/junk_wall1b.png","objects/tiles/walls/junk_walls/junk_wall_mask_b.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
 

    door_frame = none_Collision_Tile((all_sprites, none_collision_sprites), 320, 400, doorframe_img)

    scenery_car = none_Collision_Tile((all_sprites, none_collision_sprites), 125, 600, 'objects/tiles/walls/scenery/car_junk.png')

#worldMap
if loc == 'wordmp':
    map = none_Collision_Tile((all_sprites, none_collision_sprites), 0,0, 'objects/ui/WMAPBOX.jpg')
    mapimg = none_Collision_Tile((all_sprites, none_collision_sprites), 0,0, 'objects/ui/WRLDMP09.jpg')


#sprite grouping
#player(all_sprites, collision_sprites)

#initialize and other shit
##Game Setup/Game Setup Variables
pygame.init()

manager = pygame_gui.UIManager(screen_size)
cont = manager.get_root_container()



clock = pygame.time.Clock()
bg = pygame.image.load('objects/wasteMap.png')
##Variables


#Sprites
movingSprites = pygame.sprite.Group()
#map sprites
mapsprites = pygame.sprite.Group()
#vazei ton pexti sto group-Join the player into the sprites group
clicked = False
#is running?
running = True
#is caps on
caps_Running = False
#location

#health
max_hp = 100
Current_hp = 100

movingSprites.add(player)
mapObj = worldmap()
#add aroyo enemies
if loc == 'Aroyo':
    
    raider = Enemy((player_g), 100, 100, 100, 'objects/animations/playerIdleSprites', 'shotgun', [],1)
    movingSprites.add(raider)
    pathfinder = Pathfinder(matrix, raider)

    raider2 = Enemy((player_g), 150, 100, 100, 'objects/animations/playerIdleSprites', 'shotgun', [],2)
    movingSprites.add(raider2)
    pathfinder2 = Pathfinder(matrix, raider2)

    raider3 = Enemy((player_g), 130, 130, 100, 'objects/animations/playerIdleSprites', 'shotgun', [],3)
    movingSprites.add(raider3)
    pathfinder3 = Pathfinder(matrix, raider3)

    raider4 = Enemy((player_g), 160, 160, 100, 'objects/animations/playerIdleSprites', 'shotgun', [],3)
    movingSprites.add(raider4)
    pathfinder4 = Pathfinder(matrix, raider4)
    raider.id = 1
    raider2.id = 2
    raider3.id = 2 

    #item drops
    shotgun = item(player.rect.x,player.rect.y, 'shotgun', 'weapon', 1, 2, True)
    shotgun2 = item(player.rect.x - 50,player.rect.y, 'rifle', 'weapon', 1, 0, True)
    rifle = item(player.rect.x - 50,player.rect.y, '5mm Ammo', 'ammo', 1, 60, True)
    shotgunAmmo = item(player.rect.x - 70,player.rect.y, 'shotgun shells', 'ammo', 1, 30, True)
#is player in combat?
inCombat = False

#player variables
ap = 10.0
max_ap = 10.0
#COST = 0.05
ap_cost = 0.00
hp = 100
max_hp = 100
shot = False
moving = False

#inventory system
current_weapon = 1#1 shotgun
weapons_id = [1,2,3,4]#1shotgun, sg shells, pistol, 10mm ammo
ammount = [1,1,1,1]
weapon_damage = [30,40,10,0]
inventory = [] 
inventory_amount = [1,30]
scroll_offset = 0
invi = inventoryGui(inventory)
using_item = []
#aroyo enemies
dead_enemies = []
if loc == 'Aroyo':
    enemies_a = [raider,raider2, raider3, raider4]
    enemies_b = [None, raider,raider2, raider3, raider4]
    pathfinder_list = [None, pathfinder, pathfinder2,pathfinder3,pathfinder4]
    
else: 
    enemies_a = []
    enemies_b = []
    pathfinder_list = []


#turn based variables
finished = True#if finished == true make it false and true after countdown
howManyEnemeisLeft = 0
first_Time = True
turn = 10
enemies = 1
enemy_counter = 0
enemy_counter2 = 1
isFirst = True
enemyid = 0
enemyStoppedMot = True

#set start time for turn based
start_time = pygame.time.get_ticks()

start_time2 = pygame.time.get_ticks()

test_var = True

#is the enemy on the destination?
gotAtPos = False

#Not used for now
current_turn = 1
inventory_clicked = False 
sound = pygame.mixer.Sound('objects/sound/IndustrialJunk.mp3')
sound.play(loops=-1)



#map system
destoryedObjs = False
spawnedObjs = True


enemyShot = False

first_timeloaded = True

didSpawnedPlayernpc = False

diditinwordmp = False

spawnedMapnpc = False

GRunning = True

playing = False

playedTheme = False
john = npc.Npc((player_g), 560, 360, 'objects/animations/playerIdleSprites', 'shotgun', [],3)
movingSprites.add(john)
pathfinder5 = npc.Pathfinder(matrix, john, player)
if loc == 'Aroyo':
    aroyoMapObjs = [wall_one,wall_two,wall_three,wall_five,wall_seven,wall_eight,wall_nine,wall_ten,wall_eleven,wall_twelve,wall_thirtn,wall_fortn,wall_fivetn,floor_1,floor_2,floor_3,floor_4,floor_5,floor_6,floor_7,floor_8,door_frame,wall_drf,wall_sw,scenery_car,raider,raider2,raider3,raider4,pathfinder,pathfinder2,pathfinder3,pathfinder4,pathfinder5]

#iface
intface = iface()

#Save system
#i put 3 because 0 counts aswell
aroyoEnemies = 3
to_save = {
    "loc" : loc,
    "cmb" : inCombat,
    "plrhp" : player.hp,
    "plrx" : player.rect.x,
    "plry" : player.rect.y,
    "inv" : inventory,
    "invcur" : using_item,
    "enemiesa" : enemies_a,
    "enemiesb" : enemies_b,
    "pathlist" : pathfinder_list
}



save1 = save_load_item(200, 100, 'empty save', 'SAVES/save_data.pkl')
save2 = save_load_item(200, 150, 'empty save', 'SAVES/save_data1.pkl')
save3 = save_load_item(200, 200, 'empty save', 'SAVES/save_data2.pkl')
save4 = save_load_item(200, 250, 'empty save', 'SAVES/save_data3.pkl')
save5 = save_load_item(200, 300, 'empty save', 'SAVES/save_data4.pkl')
save6 = save_load_item(200, 350, 'empty save', 'SAVES/save_data5.pkl')
save7 = save_load_item(200, 400, 'empty save', 'SAVES/save_data6.pkl')
save8 = save_load_item(200, 450, 'empty save', 'SAVES/save_data7.pkl')
save9 = save_load_item(200, 500, 'empty save', 'SAVES/save_data8.pkl')
save10 = save_load_item(200, 550, 'empty save', 'SAVES/save_data9.pkl')

saves = [save1, save2, save3, save4, save5, save6, save7, save8, save9, save10]

save_game = Save_load_system(True)

sav_text = ""

in_save = False

in_load = False

typing = False

sav_box = save_name_box()

#menu
menu = mainmenu()

#online
playing_online = False
connected = False
online_players = []
loaded_players = False
players_amount = 0
data = {}
prev_loc = None
first_loaded = True
#online combat
online_combat = False
enemies_online = []
current_online_turn = 0
player_turn_id = None
fight_loc = None
#game loop
while GRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    menu.update()
    pygame.display.flip()
    if playing:
    
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    enemies_save = {}
                    enemy_save1 = {}
                    inv_save = {}
                    inv_save1 = {}
                    using_item_save = {}
                    using_item_save1 = {}

                    enemy_coun = 0
                    inv_coun = 0
                    using_item_coun = 0
                    for i in enemies_a:
                        enemy_coun += 1
                        enemies_save['enemy' + str(enemy_coun)] = enemy_save1['enemyx' + str(enemy_coun)] = i.rect.x#or currentX
                        enemies_save['enemy' + str(enemy_coun)] = enemy_save1['enemyy' + str(enemy_coun)] = i.rect.y
                        enemies_save['enemy' + str(enemy_coun)] = enemy_save1['enemyhp' + str(enemy_coun)] = i.rhp
                        enemies_save['enemy' + str(enemy_coun)] = enemy_save1['enemyx' + str(enemy_coun)],enemy_save1['enemyy' + str(enemy_coun)],enemy_save1['enemyhp' + str(enemy_coun)]
                    
                    for i in inventory:
                        inv_coun += 1
                        inv_save['item' + str(inv_coun)] = inv_save1['item_name' + str(inv_coun)] = i.name
                        inv_save['item' + str(inv_coun)] = inv_save1['item_x' + str(inv_coun)] = i.rect.x
                        inv_save['item' + str(inv_coun)] = inv_save1['item_y' + str(inv_coun)] = i.rect.y
                        inv_save['item' + str(inv_coun)] = inv_save1['item_type' + str(inv_coun)] = i.type
                        inv_save['item' + str(inv_coun)] = inv_save1['item_dropped' + str(inv_coun)] = i.isDropped
                        inv_save['item' + str(inv_coun)] = inv_save1['item_amount' + str(inv_coun)] = i.amount
                        inv_save['item' + str(inv_coun)] = inv_save1['item_ammo' + str(inv_coun)] = i.ammo
                        inv_save['item' + str(inv_coun)] = inv_save1['item_name' + str(inv_coun)], inv_save1['item_x' + str(inv_coun)], inv_save1['item_y' + str(inv_coun)], inv_save1['item_type' + str(inv_coun)], inv_save1['item_dropped' + str(inv_coun)], inv_save1['item_amount' + str(inv_coun)], inv_save1['item_ammo' + str(inv_coun)]
                    
                    for i in using_item:
                        using_item_coun += 1
                        using_item_save['item' + str(inv_coun)] = using_item_save1['item_name' + str(inv_coun)] = i.name
                        using_item_save['item' + str(inv_coun)] = using_item_save1['item_x' + str(inv_coun)] = i.rect.x
                        using_item_save['item' + str(inv_coun)] = using_item_save1['item_y' + str(inv_coun)] = i.rect.y
                        using_item_save['item' + str(inv_coun)] = using_item_save1['item_type' + str(inv_coun)] = i.type
                        using_item_save['item' + str(inv_coun)] = using_item_save1['item_dropped' + str(inv_coun)] = i.isDropped
                        using_item_save['item' + str(inv_coun)] = using_item_save1['item_amount' + str(inv_coun)] = i.amount
                        using_item_save['item' + str(inv_coun)] = using_item_save1['item_ammo' + str(inv_coun)] = i.ammo
                        using_item_save['item' + str(inv_coun)] = using_item_save1['item_name' + str(inv_coun)], using_item_save1['item_x' + str(inv_coun)], using_item_save1['item_y' + str(inv_coun)], using_item_save1['item_type' + str(inv_coun)], using_item_save1['item_dropped' + str(inv_coun)], using_item_save1['item_amount' + str(inv_coun)], using_item_save1['item_ammo' + str(inv_coun)]
                    
                    to_save = {
                        #if is loadable False then dont Load
                        "isLoadable" : True,
                        "loc" : loc,
                        "cmb" : inCombat,
                        "plrhp" : player.hp,
                        "plrx" : player.rect.x,
                        "plry" : player.rect.y,
                        "inv" : inv_save,
                        "invcur" : using_item_save,
                        "enemies" : enemies_save,
                        "save_name" : "save"
                    }
                    for enemy, enemy1 in enemies_save.items():
                        print(f'{enemy} : {enemy1[0]}')
                    #print(enemies_save['enemy1'])
                    
                    enemies_to_save = {
                        
                    }
                    
                    with open('SAVES/save_data1.pkl', 'wb') as file:
                        pickle.dump(to_save, file)
                if typing:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            sav_text = sav_text[:-1]
                        elif event.key == pygame.K_RETURN:
                            print("User Input:", sav_text)
                            sav_text = ""
                        else:
                            if not len(sav_text) > 10:
                                sav_text += event.unicode

                if not typing:
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_h:

                            with open('save_data.pkl', 'rb') as file:
                                loaded_data = pickle.load(file)
                            loc = loaded_data["loc"]
                            inCombat = loaded_data["cmb"]
                            player.hp = loaded_data["plrhp"]
                            player.rect.x = loaded_data["plrx"]
                            player.rect.y = loaded_data["plry"]
                            inventory_load = loaded_data["inv"]
                            using_item_load = loaded_data["invcur"]

                            enemies_toload = loaded_data["enemies"]

                            pygame.mixer.stop()
                            if loc == 'Aroyo':
                                sound = pygame.mixer.Sound('objects/sound/IndustrialJunk.mp3')
                                sound.play(loops=-1)

                            inventory = []
                            using_item = []

                            enemies_a = []
                            enemies_b = [None]
                            pathfinder_list = [None]
                            movingSprites.empty()
                            movingSprites.add(player)
                            player.turn = True
                            for key, i in using_item_load.items():
                                item1 = item(i[1], i[2], i[0], i[3], i[5], i[6], i[4])
                                using_item.append(item1)
                            for key, inv in inventory_load.items():
                                item1 = item(inv[1], inv[2], inv[0], inv[3], inv[5], inv[6], inv[4])
                                inventory.append(item1)
                            for test, enemy in enemies_toload.items():

                                raider = Enemy((player_g), enemy[0], enemy[1], enemy[2], 'objects/animations/playerIdleSprites', 'shotgun', [],3)
                                movingSprites.add(raider)
                                pathfinder = Pathfinder(matrix, raider)

                                enemies_a.append(raider)
                                enemies_b.append(raider)
                                pathfinder_list.append(pathfinder)
                            print(enemies_a)
                        if event.key == pygame.K_a:
                            moving = False
                            player.sprites.clear()
                            player.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/playerIdle (1).png'))

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_d:
                            moving = False
                            player.sprites.clear()
                            player.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/1/playerIdle (1).png'))
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_w:
                            moving = False
                            player.sprites.clear()
                            player.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/0/playerIdle (1).png'))
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_x:
                            moving = False
                            player.sprites.clear()
                            player.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/2/playerIdle (1).png'))
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_q:
                            moving = False
                            player.sprites.clear()
                            player.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/playerIdle-5.png'))
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_z:
                            moving = False
                            player.sprites.clear()
                            player.sprites.append(pygame.image.load('objects/animations/playerIdleSprites/playerIdle-3.png'))
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_CAPSLOCK and caps_Running == False:
                            caps_Running = True
                        elif event.key == pygame.K_CAPSLOCK and caps_Running == True:
                            caps_Running = False
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_ESCAPE and paused == False:
                            paused = True
                        else:
                            paused = False
                    if event.type == pygame.KEYDOWN and loc != 'wordmp':
                        if event.key == pygame.K_i and invi.toggled == False:
                            invi.toggled = True
                        elif event.key == pygame.K_i and invi.toggled == True:
                            invi.toggled = False
            if loc != 'Aroyo':
                if destoryedObjs == False:
                    
                    #spawnedObjs = False
                    #destoryedObjs = True
                    #first_timeloaded = False
                    
                    #
                    # 
                    # 
                    # 
                    # NA TO FTIAJW 
        
        
        
        
        
                    #for object in aroyoMapObjs:
                     #   object = None
                    
                    
                    screen.fill((0, 0, 0))
                    movingSprites.clear(screen, screen)
            if playing_online:
                #player.rect.x = 600
                if connected == False:
                    # Define the server's host and port
                    SERVER_HOST = '193.168.2.6'#127.0.0.1'
                    SERVER_PORT = 49152
                    name_id = str(input('name>'))
                    #position_id = int(input('pos_X>'))
                    # Create a socket to connect to the server
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_socket.connect((SERVER_HOST, SERVER_PORT))
                    #client_socket.setblocking(0)
                    connected = True
                    prev_loc = loc
                    online_damage = 0
                    try:
                        if using_item[0] == None:
                            online_damage = 0
                        if using_item[0].name == 'shotgun':
                            online_damage = weapon_damage[1]
                    except IndexError:
                        pass
                    player_data = {
                        "player_id": name_id,
                        #"current_sprite": player.image,
                        "x" : player.rect.x,
                        "y" : player.rect.y,
                        "loc" : loc,
                        "hp" : player.hp,
                        "shooted_player" : None,
                        "DMG" : online_damage,
                        "has_turn" : player.has_turn,
                        "enemies" : enemies_online
                    }
                    turn_system = {
                        "Aroyo_online" : {
                            "plr_turn_id" : player_turn_id,
                            "cur_on_turn" : current_online_turn
                        }
                    }

                    dropped_items = {
                        "Aroyo_online" : {

                        }
                    }
                    #item drops
                    shotgun = item(player.rect.x,player.rect.y, 'shotgun', 'weapon', 1, 2, True)
                    
                    
                    shotgunAmmo = item(player.rect.x - 70,player.rect.y, 'shotgun shells', 'ammo', 1, 30, True)
                    
                    #data2 = {}
                    #data2[player_data["player_id"]] = player_data
                    #data = json.dumps(data)
                #player.rect.x = position_id
                
                #player_data = {
                  #  "player_id": name_id,
                  #  #"current_sprite": player.image,
                  #  "x" : player.rect.x,
                  #  "y" : player.rect.y,
                  #  "loc" : loc,
                  #  "hp" : player.hp,
                  #  "shooted_player" : None,
                  #  "DMG" : online_damage,
                 #   "has_turn" : player.has_turn
                #}
                try:
                    if using_item[0] == None:
                        online_damage = 0
                    if using_item[0].name == 'shotgun':
                        online_damage = weapon_damage[1]
                except IndexError:
                    pass

                player_data["player_id"] = name_id
                player_data["x"] = player.rect.x
                player_data["y"] = player.rect.y
                player_data["loc"] = loc
                player_data["hp"] = player.hp
                player_data["shooted_player"] = None
                player_data["DMG"] = online_damage
                player_data["has_turn"] = player.has_turn
                
                #data = json.loads(data)
                #data = player_data#[player_data["player_id"]] = player_data
                #data = json.dumps(data)
                player_data2 = {}
                #try:
                #    data = client_socket.recv(1024).decode()
                #except socket.timeout:
                #    print("Socket timed out - no data received")
                #    # Handle the timeout or other errors as needed
                #except Exception as e:
                #    print("An error occurred:", str(e))
                #try:
                #    while True:
                #        chunk = client_socket.recv(1024)
                #        if not chunk:
                #            break  # No more data to receive
                #        data = chunk
                #except BlockingIOError:
                #    pass
                # Deserialize the JSON data into a Python dictionary
                
                socket_comm_thread = threading.Thread(target=socket_thread, args=(client_socket,))
                socket_comm_thread.start()
                socket_comm_thread.join
                try:
                    player_data_received = pickle.loads(data)
                    prev_player_d_r = player_data_received
                    #del player_data_received
                except (pickle.UnpicklingError, TypeError, UnicodeDecodeError) as e:
                    pass
                
                    
                    # Handle the unpickling error
                    #print(f"Error while unpickling data: {e}")
                if bool(data):
                    
                    if player.hp <= 0:
                        player.rect.x = 600
                        player.rect.y = 600
                        player.ap = player.ap_max
                    #print(prev_player_d_r)
                    #print(prev_loc)
                    if prev_loc != loc and "player_data" in prev_player_d_r and name_id in prev_player_d_r["player_data"][prev_loc]:
                        prev_player_d_r["player_data"][prev_loc].pop(name_id, None)
                        prev_player_d_r["player_data"][loc][name_id] = player_data
                        prev_loc = loc
                    if first_loaded:
                        prev_loc = loc
                        first_loaded = False
                    if online_combat == False and "player_data" in prev_player_d_r and fight_loc in prev_player_d_r["player_data"]:
                        for i, playeron in prev_player_d_r["player_data"][loc].items():
                            if playeron["shooted_player"] == name_id:
                                enemies_online.append(playeron["player_id"])
                                enemies_online.append(name_id)
                                online_combat = True
                    if len(online_players) >= 2 and "player_data" in prev_player_d_r:
                        if online_combat == False and player.ap >= 50:
                            for player_s in online_players:
                                if player_s.got_shot == True:
                                    player_s.got_shot = False
                                    player.play_shoot(player_s)
                                    enemies_online.append(player_s.id)
                                    enemies_online.append(name_id)
                                    player_data["shooted_player"] = player_s.id
                                    fight_loc = loc
                                    online_combat = True
                    if online_combat and "player_data" in prev_player_d_r:
                        if len(online_players) >= 2 and len(enemies_online) >= 2:
                            if fight_loc != loc:
                                online_combat = False
                                enemies_online = []
                                current_online_turn = 0
                                player_turn_id = None
                                for i, playeron in prev_player_d_r["player_data"][fight_loc].items():
                                    prev_player_d_r["player_data"][playeron["id"]]["enemies"].remove(name_id)
                            if player.ap == 0:
                                prev_player_d_r["player_data"][name_id]["has_turn"] = False
                                try:
                                    if enemies_online[current_online_turn] != name_id:
                                        for i in online_players:
                                            if i.id == enemies_online[current_online_turn]:
                                                i.has_turn = True
                                        player_turn_id = enemies_online[current_online_turn]
                                        current_online_turn += 1
                                        player.has_turn = False
                                    else:
                                        player.ap = player.ap_max
                                        player.has_turn = True
                                except IndexError:
                                    current_online_turn = 0
                                    if enemies_online[current_online_turn] != name_id:
                                        for i in online_players:
                                            if i.id == enemies_online[current_online_turn]:
                                                i.has_turn = True
                                        player_turn_id = enemies_online[current_online_turn]
                                    else:
                                        player.ap = player.ap_max
                                        player.has_turn = True
                                for enemy1 in prev_player_d_r["player_data"][fight_loc]:
                                    enemy1[player_turn_id]["has_turn"] = True
                            if "turn_system" in prev_player_d_r and fight_loc in prev_player_d_r["turn_system"]:
                                if prev_player_d_r["turn_system"][fight_loc]["plr_turn_id"] == name_id:
                                    print("TURN")
                                    player.has_turn = True
                            if player.has_turn == True:
                                prev_player_d_r["player_data"][fight_loc][player_turn_id]["has_turn"] = False
                                prev_player_d_r["player_data"][fight_loc][name_id]["has_turn"] = True
                            #if player.ap >= 50: #todo add cmb and turn button
                                for player_s in online_players:
                                    if player_s.got_shot == True:
                                        player_s.got_shot = False
                                        player.play_shoot(player_s)
                                        if not player_s.id in enemies_online:
                                            enemies_online.append(player_s.id)
                                        player_data["shooted_player"] = player_s.id
                            if player.ap == 0:
                                prev_player_d_r["player_data"][fight_loc][name_id]["has_turn"] = False
                            for i, playeron in prev_player_d_r["player_data"][fight_loc].items():
                                if playeron["shooted_player"] == name_id and not playeron["player_id"] in enemies_online:
                                    enemies_online.append(playeron["player_id"])
                                    prev_player_d_r["player_data"][fight_loc][playeron["player_id"]]["enemies"] = enemies_online
                                    prev_player_d_r["player_data"][fight_loc][playeron["player_id"]]["DMG"] -= player.hp
                                if playeron["shooted_player"] == name_id and playeron["player_id"] in enemies_online:
                                    prev_player_d_r["player_data"][fight_loc][playeron["player_id"]]["DMG"] -= player.hp
                            turn_system[fight_loc]["plr_turn_id"] = player_turn_id
                            turn_system[fight_loc]["cur_on_turn"] = current_online_turn
                            
                        else:
                            online_combat = False
                    #if not "player_data" in prev_player_d_r:
                        #print(prev_player_d_r)
                    if "player_data" in prev_player_d_r and "conn_id" in prev_player_d_r:
                        #if len(prev_player_d_r["player_data"]) > players_amount:
                        if prev_player_d_r["conn_id"] > players_amount or prev_player_d_r["conn_id"] < players_amount: 
                            print("player_data: ",(prev_player_d_r["player_data"]))
                            print("prev_p_d_r: ",(prev_player_d_r))
                            #prev_player_d_r["player_data"][loc][name_id] = player_data
                            print('current connections: ', str(prev_player_d_r["conn_id"]))
                            loaded_players = False
                            print(f'new players : {len(prev_player_d_r["player_data"][loc])}')
                            #print("loc: ",(prev_player_d_r["player_data"][loc]))
                            
                    if loaded_players == False and "player_data" in prev_player_d_r and "conn_id" in prev_player_d_r:
                        if loc in prev_player_d_r["player_data"]:
                            online_players.clear()
                            for dat, i in prev_player_d_r["player_data"][loc].items():
                                #print('dat: ',str(dat['id']))
                                #print('i: ',str(i['player_id']))
                                #if i["player_id"] != name_id:
                                    #print('adding player')
                                    #print("test",str(i))
                                plr = online_player(i["x"], i["y"], i["loc"], 'objects/animations/playerIdleSprites/3/playerIdle (1).png', i["player_id"])#, i["current_sprite"])
                                online_players.append(plr)
                    if "player_data" in prev_player_d_r and "conn_id" in prev_player_d_r:
                        if loc in prev_player_d_r["player_data"]:
                            #print('found it')
                            for plrs, (i, dat) in zip(online_players, prev_player_d_r["player_data"][loc].items()):
                                #print(plrs)
                                #print(dat['x'])
                                #print('updateting pos')
                                #print("id: ",str(dat['player_id']))
                                if dat['player_id'] != name_id:
                                    #print("xxxxxxxxxxxxxxxxxxxxxxxxxxx: ",str(dat['x']))
                                    #print(prev_player_d_r["player_data"])
                                    plrs.x = dat['x']
                                    plrs.y = dat["y"]
                                    #print("players x: ", (plrs.rect.x))
                                    #plrs.current_sprite_id = dat["current_sprite"]

                                    image = pygame.image.load('objects/animations/playerIdleSprites/3/playerIdle (1).png')
                                #plrs.rect = image.get_rect()
                                #screen.blit(image,plrs.rect)#plrs.current_sprite, plrs.rect)
                    
                    if bool(online_players):
                        for plrs in online_players:
                            if plrs.id != name_id:
                                plrs.update()
                    loaded_players = True
                    if "player_data" in prev_player_d_r and "conn_id" in prev_player_d_r:
                        for i, playerself in prev_player_d_r["player_data"][loc].items():
                            if playerself["player_id"] == name_id:
                                player.hp = playerself["hp"]
                        if bool(online_players):
                            for plrs in online_players:
                                if not plrs.id in prev_player_d_r["player_data"][loc]:
                                    online_players.remove(plrs)
                        #print(prev_player_d_r['player_data'])
                        #print(prev_player_d_r["player_data"])
                        #print(len(prev_player_d_r["player_data"]))
                        players_amount = len(prev_player_d_r["player_data"][loc])
                    #if "conn_id" in prev_player_d_r:
                        #print('connections: ', str(prev_player_d_r["conn_id"]))
                     #   players_amount = prev_player_d_r["conn_id"]
                    # Serialize the dictionary to a JSON string
                    prev_loc = loc
                    shotgun.update()
                    shotgunAmmo.update()
                    data_to_send = {
                        "player_data" : prev_player_d_r["player_data"], 
                        "player_data_rec" : player_data,
                        "turn_system" : turn_system,
                        "dropped_items" : dropped_items
                    }
                    #print("send:    ", str(data_to_send))

                    pickle_data = pickle.dumps(data_to_send)
                    # Send the JSON string to the server

                    client_socket.send(pickle_data)

                    player_data["shooted_player"] = None
                
                #print('data')
                
                #except Exception as e:
                #  print(e)
                #   traceback.print_exc()
                
            
            if loc == 'raiders':
                if diditinwordmp == False:
                    for object in aroyoMapObjs:
                        object = None
                    
                    print('test1')
                    screen.fill((0, 0, 0))
                    movingSprites.add(player)
                    diditinwordmp = True
                    
        
        
            if loc == 'Aroyo':
            
                if spawnedObjs == False and first_timeloaded == False:
                    print('test2')
                    destoryedObjs = False
                    spawnedObjs = True
                    floor_1 = none_Collision_Tile((all_sprites, none_collision_sprites), 225, 400, 'objects/tiles/Floors/Main/Floor1.png')
        
                    floor_2 = none_Collision_Tile((all_sprites, none_collision_sprites), 295, 430, 'objects/tiles/Floors/Main/Floor1.png')
        
                    floor_3 = none_Collision_Tile((all_sprites, none_collision_sprites), 305, 350, 'objects/tiles/Floors/Main/Floor1.png')
        
                    floor_4 = none_Collision_Tile((all_sprites, none_collision_sprites), 225, 400, 'objects/tiles/Floors/Main/Floor1.png')
        
                    floor_5 = none_Collision_Tile((all_sprites, none_collision_sprites), 225, 400, 'objects/tiles/Floors/Main/Floor1.png')
        
                    floor_6 = none_Collision_Tile((all_sprites, none_collision_sprites), 225, 400, 'objects/tiles/Floors/Main/Floor1.png')
        
                    floor_7 = none_Collision_Tile((all_sprites, none_collision_sprites), 225, 400, 'objects/tiles/Floors/Main/Floor1.png')
        
                    floor_8 = none_Collision_Tile((all_sprites, none_collision_sprites), 225, 400, 'objects/tiles/Floors/Main/Floor1.png')
        
                    wall_one = Collision_Tile((all_sprites, collision_sprites), 387, 420, 'objects/tiles/walls/junk_walls/junk_wall1.png','objects/tiles/walls/junk_walls/junk_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')
        
                    wall_two = Collision_Tile((all_sprites, collision_sprites), 227, 380, 'objects/tiles/walls/junk_walls/junk_wall1.png','objects/tiles/walls/junk_walls/junk_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')
        
                    wall_three = Collision_Tile((all_sprites, collision_sprites), 480, 442, "objects/tiles/walls/junk_walls/junk_wall1.png","objects/tiles/walls/junk_walls/junk_wall_mask.png",'objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')
        
                    #wall_fore = Collision_Tile((all_sprites, collision_sprites), 481, 281, 'objects/tiles/walls/junk_walls/metal_wall.png','objects/tiles/walls/junk_walls/metal_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')
        
                    wall_five = Collision_Tile((all_sprites, collision_sprites), 707, 325, 'objects/tiles/walls/junk_walls/junk_wall1b.png','objects/tiles/walls/junk_walls/junk_wall_mask_b.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')
        
                    #wall_six = Collision_Tile((all_sprites, collision_sprites), 389, 346, 'objects/tiles/walls/junk_walls/junk_wall1.png','objects/tiles/walls/junk_walls/junk_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')
        
                    wall_seven = Collision_Tile((all_sprites, collision_sprites), 614, 400, 'objects/tiles/walls/junk_walls/junk_wall1b.png','objects/tiles/walls/junk_walls/junk_wall_mask_b.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')
        
                    wall_eight = Collision_Tile((all_sprites, collision_sprites), 565, 464, 'objects/tiles/walls/junk_walls/metal_wall.png','objects/tiles/walls/junk_walls/metal_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')
        
                    wall_nine = Collision_Tile((all_sprites, collision_sprites), 229, 300, 'objects/tiles/walls/junk_walls/junk_wall1b.png','objects/tiles/walls/junk_walls/junk_wall_mask_b.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')
        
                    wall_ten = Collision_Tile((all_sprites, collision_sprites), 319, 227, 'objects/tiles/walls/junk_walls/junk_wall1b.png','objects/tiles/walls/junk_walls/junk_wall_mask_b.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')
        
                    wall_eleven = Collision_Tile((all_sprites, collision_sprites), 414, 226, 'objects/tiles/walls/junk_walls/junk_wall1.png','objects/tiles/walls/junk_walls/junk_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')
        
                    wall_twelve = Collision_Tile((all_sprites, collision_sprites), 507, 249, 'objects/tiles/walls/junk_walls/junk_wall1.png','objects/tiles/walls/junk_walls/junk_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')
        
                    wall_thirtn = Collision_Tile((all_sprites, collision_sprites), 598, 272, 'objects/tiles/walls/junk_walls/junk_wall1.png','objects/tiles/walls/junk_walls/junk_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')
        
                    wall_fortn = Collision_Tile((all_sprites, collision_sprites), 690, 296, 'objects/tiles/walls/junk_walls/junk_wall1.png','objects/tiles/walls/junk_walls/junk_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')
        
                    wall_fivetn = Collision_Tile((all_sprites, collision_sprites), 753, 318, 'objects/tiles/walls/junk_walls/metal_wall.png','objects/tiles/walls/junk_walls/metal_wall_mask.png','objects/tiles/walls/junk_walls/junk_wall_collision_rect.png')
            
                    wall_drf = none_Collision_Tile((all_sprites, none_collision_sprites), 320, 304, doorframe_img)
                        
                    wall_sw = Collision_Tile((all_sprites,collision_sprites), 395, 252, "objects/tiles/walls/junk_walls/junk_wall1b.png","objects/tiles/walls/junk_walls/junk_wall_mask_b.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
        
        
                    door_frame = none_Collision_Tile((all_sprites, none_collision_sprites), 320, 400, doorframe_img)
        
                    scenery_car = none_Collision_Tile((all_sprites, none_collision_sprites), 125, 600, 'objects/tiles/walls/scenery/car_junk.png')
                    raider = Enemy((player_g), 100, 100, 'objects/animations/playerIdleSprites', 'shotgun', [],1)
                    movingSprites.add(raider)
                    pathfinder = Pathfinder(matrix, raider)
        
                    raider2 = Enemy((player_g), 150, 100, 'objects/animations/playerIdleSprites', 'shotgun', [],2)
                    movingSprites.add(raider2)
                    pathfinder2 = Pathfinder(matrix, raider2)
        
                    raider3 = Enemy((player_g), 130, 130, 'objects/animations/playerIdleSprites', 'shotgun', [],3)
                    movingSprites.add(raider3)
                    pathfinder3 = Pathfinder(matrix, raider3)
        
                    raider4 = Enemy((player_g), 160, 160, 'objects/animations/playerIdleSprites', 'shotgun', [],3)
                    movingSprites.add(raider4)
                    pathfinder4 = Pathfinder(matrix, raider4)
        
                    movingSprites.add(player)
            
            if loc != 'wordmp':
                player.animate()
        
            #print(pygame.mouse.get_pos())
        
            if john.isEnemy == True:
                enemies_a.append(john)
                pathfinder_list.append(pathfinder5)
        
            current_time2 = pygame.time.get_ticks()
            if current_time2 - start_time2 >= 20000:
                pathfinder5.create_path()
                start_time2 = current_time2
            #draw bg of aroyo if in aroyo
            if loc == 'Aroyo':
                if playedTheme == False:
                    sound = pygame.mixer.Sound('objects/sound/IndustrialJunk.mp3')
                    sound.play(loops=-1)
                    playedTheme = True
                for enemy in enemies_a:
                    enemy.update()
                    enemy.animate()
                #raider.update()
                #raider.animate()
                #raider3.update()
                #raider3.animate()
                #raider4.update()
                #raider4.animate()
                john.update()
                john.animate()
                back.blit(bg, (0,0))
                enemies = 2
            #if hp of the player are 0 then stop the game(not using it rn for debug purposes) 
            #if player.hp == 0:
             #   running = False
        
        
            #when player clicks an enemy
            if player.turn:
                if clicked == True:
                
                    for enemy in enemies_a:
                    
                        if clicked == True:
                            
                            if shot == False:
                                #find who he is from list
                                if enemy.id == enemyid  and enemy.clicked == True:
                                    #is the one who got clicked?
                                    #if enemy.clicked == True:
                                    #what weapon does the player used to shoot him?
                                    print('id correct')
                                    if current_weapon == 1 and using_item[0].ammo >= 1:
                                        
                                        try: 
                                            
                                            current_time = pygame.time.get_ticks()
                                            if current_time - start_time >= 5000:
                                                
                                                player.play_shoot(enemy)
                                                
                                                sound = pygame.mixer.Sound('objects/sound/sfx/SHOT11.mp3')
                                                sound.play()
                                                using_item[0].ammo -= 1
                                                print("enemyid:" + str(enemyid))
                                                print("enemy..id:" + str(enemy.id))
                                                enemy.rhp -= weapon_damage[0]
                                                print(str(enemy.rhp))
                                                #enemy.clicked = False
                                                clicked = False
                                                ap -= 5
                                                start_time = current_time
                                        except IndexError:
                                            print("enemyid:" + str(enemyid))
                                    elif current_weapon == 2 and using_item[0].ammo >= 30:
                                        try: 
                                            current_time = pygame.time.get_ticks()
                                            if current_time - start_time >= 5000:
                                                using_item[0].ammo = 0
                                                print("enemyid:" + str(enemyid))
                                                print("enemy..id:" + str(enemy.id))
                                                enemy.rhp -= weapon_damage[1]
                                                print(str(enemy.rhp))
                                                #enemy.clicked = False
                                                clicked = False
                                                ap -= 5
                                                start_time = current_time
                                        except IndexError:
                                            print("enemyid:" + str(enemyid))
                                    #check if dead
                                    if enemy.rhp <= 0:
                                        print('enemyid: ' + str(enemyid))
                                        print(str(enemy) + 'Died')
                                        enemy.sprites.clear()
                                        enemy.isDead()
                                        enemy.speed = 0
                                        print(pathfinder_list)
                                        enemy_counter = 0
                                        #enemies_b[enemyid]
                                        enemies_a.remove(enemy)
                                        enemies_b.remove(enemy)
                                        dead_enemies.append(enemy)
                                        try:
                                            pathfinder_list.remove(pathfinder_list[enemy.id])
                                        except IndexError:
                                            try:
                                                pathfinder_list.remove(pathfinder_list[enemy.id -1])
                                            except IndexError:
                                                pathfinder_list.remove(pathfinder_list[enemy.id -2])
                                        print(pathfinder_list)
                                        print(enemy)
                                        print(len(enemies_a))
        
                                        print(len(enemies_a))
                                        inCombat = False
                                        player.turn = True
                                        
                                    ap - 5
                                    shot = True
                            elif shot == True:
                                shot = False
                    
            #abandond piece of code 
            if bool(enemies_a):
                for enemy in enemies_a:
                    pass
                    #if enemy.rhp <= 0:
                     #   print(str(enemy) + 'Died')
                      #  enemy.sprites.clear()
                       # enemy.sprites.append(pygame.image.load('objects/tiles/walls/junk_walls/junk_wall1.png'))
                    #    #raider.kill()
                     #   print(enemy)
                     #   print(len(enemies_a))
                      #  enemies_a.remove(enemy)
               #         print(len(enemies_a))
                #        inCombat = False
                 #       turn = 10
                  #      break
            if not bool(enemies_a):
                inCombat = False
                turn = 10
        
        
            #if not in comabt we check if there are any enemies left in area and if the enemies are close to 1000x we initialize combat
            if not inCombat:
                if bool(enemies_a):
                    for enemy in enemies_a:
                        if enemy_counter2 >= len(enemies_a) - 1:
                            enemy_counter2 = 1
                        try:
                            distancex = enemies_a[enemy_counter2].rect.x - player.rect.x
                        except IndexError:
                            enemy_counter2 = 1
                        enemy_counter2 += 1
                        if distancex < 1000 and inCombat == False:
                            inCombat = True
                            player.turn = False
                            enemy.turn = True
                            turn = 1
                            break
            if inCombat:
                if not bool(enemies_a):
                    inCombat = False
                    player.turn = True


            #for enemy1 in enemies_a:
             #   enemyStoppedMot = all(not enemy1.moving for enemy1 in enemies_a)
              #  if enemy1.moving:
               #     print('it moves')
                #    enemyStoppedMot = False
          # Change turn
            if inCombat:
                if not player.turn:
                    #first_Time = True
        
                    for enemy in enemies_a:
                        if enemy.turn:
                            #print('turn')
                            enemy.shoot()
                            if enemyShot == False:
                                if enemy.weapon == 'shotgun':
                                    sound = pygame.mixer.Sound('objects/sound/sfx/SHOT11.mp3')
                                    sound.play()    
                                enemyShot = True
                            # Check how much time passed (convert seconds into milliseconds if you want to wait x seconds)
                            # Waiting for 3 seconds
                            current_time = pygame.time.get_ticks()
                            
                            if current_time - start_time >= 3000:# and enemyStoppedMot == True:
                                enemyStoppedMot = True
                                enemyShot = False
                                print('Yes')
                                changeTurn(enemy)
                                start_time = current_time
                if player.turn:
                    #check if the player is moving check if he has enough ap and remove ap with ap_cost else give turn to enemy per millisecond
                    if moving == True:
                        if ap >= ap_cost:
                            ap -= ap_cost
                        else:
                            enemies_a[0].turn = True
                            player.turn = False
                            enemy_counter = 1
                    if ap == 0:
                        enemies_a[0].turn = True
                        player.turn = False
                        enemy_counter = 1
            if loc == 'Aroyo':
                for path in pathfinder_list:
                    if path != None:
                        path.update()
                    
                #pathfinder2.update()
                #pathfinder.update()
                #pathfinder3.update()
                #pathfinder4.update()
        
                #raider2.update()
        
                #raider2.animate()
        
            if loc != 'wordmp':
                player.update()
            for shack in player_g:
                screen.blit(player.sprites, player.rect)
                screen.blit(raider.sprites, raider.rect)
            if pm.save():
                print(in_save)
                if in_save == False:
                    loc = 'save'
                    paused = False
                    in_save = True
            if pm.load():
                loc = 'load'
                paused = False
            #pm stands for pause menu we just check if the player pressed exit if he did we close the game
            if pm.update():
                running = False
            #we just check if the player pressed resume if he did we resume the game
            if pm.resume():
                print('Close')
                paused = False
        
            #if not in world map we add the green area for fast travel
            if loc != 'wordmp' and loc != 'save' and loc != 'load' and loc != 'mainmenu':
                s = pygame.Surface((400,1750))
                s.set_alpha(58)                
                s.fill((0,155,0))           
                screen.blit(s, (1000,0))    
            if player.rect.x >= 1000:
                loc = 'wordmp'
            
        
            if loc == 'wordmp':
                Aroyowayp = mapWP(screen_W/2, screen_H/2, 'Aroyo')
                mapObj.update()
                mapsprites.update()
                mapsprites.draw(screen)
        
            if loc == 'Aroyo':
                wall_one.update()
                wall_two.update()
                door_frame.update()
                scenery_car.update()
            if loc == 'wordmp':
                
                if didSpawnedPlayernpc == False:
                    pygame.mixer.stop()
                    sound = pygame.mixer.Sound('objects/sound/Fallout2.mp3')
                    sound.play(loops=-1)
                    didSpawnedPlayernpc = True
                    if spawnedMapnpc == False:
                        mappnpc = mapnpc.PlayerNpc(mapsprites,500,500,[],1)
                        mapsprites.add(mappnpc)
                        mappath = mapnpc.Pathfinder(matrix,mappnpc)
                        spawnedMapnpc = True
                    clicked9 = False
        
        
                
                if Aroyowayp.rect.collidepoint(mappnpc.rect.x, mappnpc.rect.y):
                    if mappnpc.rect.collidepoint(pygame.mouse.get_pos()):
                        if pygame.mouse.get_pressed()[0] == 1 and clicked9 == False:
                            clicked9 = True
                            loc = Aroyowayp.location
                            player.rect.x = screen_W/2 + 200
                            player.rect.y = screen_H/2 + 200
                            pygame.mixer.stop()
                            pygame.mixer.Sound('objects/sound/IndustrialJunk.mp3').play()
                        if pygame.mouse.get_pressed()[0] == 0:
                            clicked9 = False
        
                            
                Aroyowayp.update()
                mappnpc.update()
                mappath.update
            if loc != 'wordmp' and loc != 'save' and loc != 'load' and loc != 'mainmenu':
                didSpawnedPlayernpc = False
                    
            #check movement keys
            pressed_keys = pygame.key.get_pressed()
            player.move(pressed_keys)
            
            #if player on aroyo we blit the buildings for aroyo 
            for shack in all_sprites:
                if loc == 'Aroyo':
                    screen.blit(floor_1.wall3, floor_1.rect)
                    screen.blit(floor_2.wall3, floor_2.rect)
                    screen.blit(floor_3.wall3, floor_3.rect)
                    screen.blit(floor_4.wall3, floor_4.rect)
                    
        
            #draw player and all_sprites group for all the sprites in game
            if loc != 'wordmp' and loc != 'save' and loc != 'load' and loc != 'mainmenu':
                movingSprites.draw(screen)
                movingSprites.update()
                all_sprites.update()
        
            mask = pygame.mask.from_surface(screen)
            #if player on aroyo we blit the buildings for aroyo 
            for shack in all_sprites:
                if loc == 'Aroyo':
                    
                    circle_radius = 50
                    masked_wall = wall_one.wall1.copy()
                    mask_surface = pygame.Surface(wall_one.wall1.get_size(), pygame.SRCALPHA)
                    if wall_one.rect.collidepoint(player.rect.x, player.rect.y):
                        pygame.draw.circle(mask_surface, (255, 255, 255), (player.rect.x -400, player.rect.y -400), circle_radius)
                    mask = pygame.mask.from_surface(mask_surface)
                    mask_pixels = pygame.surfarray.array_alpha(mask_surface)
                    masked_wall_pixels = pygame.surfarray.pixels_alpha(masked_wall)
                    masked_wall_pixels[mask_pixels == 255] = 0
                    del masked_wall_pixels
        
                    masked_wall2 = wall_two.wall1.copy()
                    mask_surface2 = pygame.Surface(wall_two.wall1.get_size(), pygame.SRCALPHA)
                    if wall_two.rect.collidepoint(player.rect.x, player.rect.y):
                        pygame.draw.circle(mask_surface2, (255, 255, 255), (player.rect.x -200, player.rect.y -350), circle_radius)
                    mask = pygame.mask.from_surface(mask_surface2)
                    mask_pixels2 = pygame.surfarray.array_alpha(mask_surface2)
                    masked_wall_pixels2 = pygame.surfarray.pixels_alpha(masked_wall2)
                    masked_wall_pixels2[mask_pixels2 == 255] = 0
                    del masked_wall_pixels2
        
                    masked_wall3 = door_frame.wall3.copy()
                    mask_surface3 = pygame.Surface(door_frame.wall3.get_size(), pygame.SRCALPHA)
                    if door_frame.rect.collidepoint(player.rect.x, player.rect.y):
                        
                        pygame.draw.circle(mask_surface3, (255, 255, 255), (player.rect.x -300, player.rect.y -400), circle_radius)
                    mask = pygame.mask.from_surface(mask_surface3)
                    mask_pixels3 = pygame.surfarray.array_alpha(mask_surface3)
                    masked_wall_pixels3 = pygame.surfarray.pixels_alpha(masked_wall3)
                    masked_wall_pixels3[mask_pixels3 == 255] = 0
                    del masked_wall_pixels3
        
                    masked_wall4 = wall_three.wall1.copy()
                    mask_surface4 = pygame.Surface(wall_three.wall1.get_size(), pygame.SRCALPHA)
                    if wall_three.rect.collidepoint(player.rect.x, player.rect.y):
                        
                        pygame.draw.circle(mask_surface4, (255, 255, 255), (player.rect.x -450, player.rect.y - 400), circle_radius)
                    mask = pygame.mask.from_surface(mask_surface4)
                    mask_pixels4 = pygame.surfarray.array_alpha(mask_surface4)
                    masked_wall_pixels4 = pygame.surfarray.pixels_alpha(masked_wall4)
                    masked_wall_pixels4[mask_pixels4 == 255] = 0
                    del masked_wall_pixels4
                    
                    screen.blit(wall_nine.wall1, wall_nine.rect)
                    screen.blit(wall_ten.wall1, wall_ten.rect)
                    screen.blit(wall_eleven.wall1, wall_eleven.rect)
                    screen.blit(wall_twelve.wall1, wall_twelve.rect)
                    screen.blit(wall_thirtn.wall1, wall_thirtn.rect)
                    screen.blit(wall_fortn.wall1, wall_fortn.rect)
                    screen.blit(wall_fivetn.wall1, wall_fivetn.rect)
                    screen.blit(wall_drf.wall3, wall_drf.rect)
                    screen.blit(wall_sw.wall1, wall_sw.rect)
        
                    screen.blit(masked_wall, wall_one.rect)
                    screen.blit(masked_wall2, wall_two.rect)
                    screen.blit(masked_wall3, door_frame.rect)
                    screen.blit(masked_wall4, wall_three.rect)
                    #screen.blit(wall_fore.wall1, wall_fore.rect)
                    screen.blit(wall_five.wall1, wall_five.rect)
                    #screen.blit(wall_six.wall1, wall_six.rect)
                    screen.blit(wall_seven.wall1, wall_seven.rect)
                    screen.blit(wall_eight.wall1, wall_eight.rect)
                    
                   
                    
                    #screen.blit(aroyoBar.wall_0.wall1, aroyoBar.wall_0.rect)
                    screen.blit(scenery_car.wall3, scenery_car.rect)
            try:
                if using_item[0].name == 'shotgun':
                    current_weapon = 1
                elif using_item[0].name == 'rifle':
                    current_weapon = 2
            except IndexError:
                pass
            PauseMenu().update()
            clock.tick(60)
            
            for ite in inventory:
                ite.update()
            for u in using_item:
                u.update()
            if loc == 'Aroyo':
                shotgun.update()
                shotgun2.update()
                rifle.update()
                shotgunAmmo.update()
            
            
            if loc != 'wordmp' and loc != 'save' and loc != 'load' and loc != 'mainmenu':
                intface.update()

            if invi.toggled == True:
                invi.toggle_on()
                screen.blit(invi.invbox, invi.rect)
            
            if pygame.mouse.get_pressed()[0] == 1 and loc == 'wordmp' and mappath.clicked == False and mapObj.rect2.collidepoint(pygame.mouse.get_pos()):
                mappath.clicked = True
                mappath.click = True
                mappath.create_path()
            if pygame.mouse.get_pressed()[0] == 0 and loc == 'wordmp':
                mappath.clicked = False
                mappath.click = False
            if loc == 'save':
                save_game.update()
            #inventory update
            invi.update()
        
            #ui draw/update/ui tick
            delta_time = clock.tick(60)/1000.0
            manager.process_events(event)
            manager.update(delta_time)
            manager.draw_ui(screen)
        
            #raider.update()
            pygame.display.flip()
pygame.quit()
sys.exit()
        
    
