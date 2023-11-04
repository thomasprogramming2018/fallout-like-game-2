import pygame

from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
import time
from pygame.time import *
import random as rand

class Pathfinder:
    def __init__(self, matrix, npc):

        self.matrix= [
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        self.grid = Grid(matrix=self.matrix)
        self.path = []

        self.ttoBody = pygame.sprite.GroupSingle(npc)
        self.Body = npc
        self.empty_path()
        self.clicked = False
        self.click = False
        
    def empty_path(self):
        self.path = []

    def create_path(self):
        # start
        start_x, start_y = self.ttoBody.sprite.get_coord()
        start_x, start_y = self.Body.get_coord()
        start = self.grid.node(start_x, start_y)

        # end
        mouse_pos = pygame.mouse.get_pos()
        
        if self.click == True:

            self.px = mouse_pos[0]
            self.click = False
            self.py = mouse_pos[1]
        
            #self.px = self.Body.rect.x
            #self.py = self.Body.rect.y
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
    

class PlayerNpc(pygame.sprite.Sprite):
    def __init__(self, group, rx, ry, empty_path, id):
        super().__init__()
        self.did = 2
        self.direction = "right-down"
        
        self.isAnimating = False
        self.sprites = []
        
        self.sprites.append(pygame.image.load(f"objects/ui/coursor/ACRSHAIR.bmp"))
        self.currentSprite = 0
        self.image = self.sprites[self.currentSprite]

        self.clicked = False

        self.turn = False

        self.id = id

        self.rhp = 100

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

        self.isEnemy = False
        
        self.pos = self.rect.center
        
        self.empty_path = empty_path

        self.path_index = 0
        
        self.degree = "down"
        self.frame = 0
        self.damage = 3
        self.dead = False
        self.collision_rects = []
        self.empty_path = empty_path
        self.isShot = True
    def shoot(self):
        if self.weapon == "shotgun":
            self.damage = 10
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
             
    def update(self):
        self.old_rect = self.rect.copy()
        self.didit = False

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
            self.sprites.clear()
            self.sprites.append(pygame.image.load(f"objects/ui/mappoint.png"))
            self.image = pygame.image.load(f"objects/ui/mappoint.png")
            
        else:
            self.moving = True
            self.sprites.clear()
            self.sprites.append(pygame.image.load(f"objects/ui/coursor/ACRSHAIR.bmp"))
            self.image = pygame.image.load(f"objects/ui/coursor/ACRSHAIR.bmp")
            


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