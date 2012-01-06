import pygame
from pygame.locals import *

import random

import sprites
from constants import *

class Thing:
    def __init__(self, game, **kargs):
        self.game       = game
        
        self.color      = kargs.get('color', BLACK)
        
        self.holdable   = kargs.get('holdable', 0)
        self.holding    = None
        
        self.frozen     = kargs.get('frozen', 1)
        self.image      = kargs.get('image', None)
        
        self.rect       = Rect( kargs.get('x', SCREEN_WIDTH/2  - kargs.get('w', 5)/2),
                                kargs.get('y', SCREEN_HEIGHT/2 - kargs.get('h', 5)/2),
                                kargs.get('w', 5),
                                kargs.get('h', 5) )
        
        self.speed = kargs.get('speed', 1)
        self.xmove_tick = 0.0
        self.ymove_tick = 0.0
    
        self.parent = None
    
    def update(self):
        self.check_collisions()
    
    def draw(self, screen):
        if self.color == None:
            return
        elif self.color == WALL:
            pygame.draw.rect(screen, self.parent.wall_color, self.rect)
        elif self.image:
            draw_point = self.rect.centerx - self.image.get_width() /2, \
                         self.rect.centery - self.image.get_height()/2
            screen.blit(self.image, draw_point)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
    
    def hitting_wall(self):
        for obj in self.parent.objects:
            if obj == self or obj.__class__ != Wall: continue

            if self.rect.colliderect(obj.rect):
                return True
                break
        
        return False
    
    def move(self, dest):
        self.parent.remove(self)
        dest.add(self)
    
    def right(self):
        self.xmove_tick += self.speed
        while self.xmove_tick > 1.0:
            self.xmove_tick -= 1.0 
            if self.hitting_wall(): continue
            self.rect.x += 1
            if self.holding:
                self.holding.rect.x += 1
        if self.hitting_wall():
            self.rect.x -= 1
            if self.holding:
                self.holding.rect.x -= 1
    
    def left(self):
        self.xmove_tick += self.speed
        while self.xmove_tick > 1.0:
            self.xmove_tick -= 1.0
            if self.hitting_wall(): continue
            self.rect.x -= 1
            if self.holding:
                self.holding.rect.x -= 1
        if self.hitting_wall():
            self.rect.x += 1
            if self.holding:
                self.holding.rect.x += 1
    
    def down(self):
        self.ymove_tick += self.speed
        while self.ymove_tick > 1.0:
            self.ymove_tick -= 1.0
            if self.hitting_wall(): continue
            self.rect.y += 1
            if self.holding:
                self.holding.rect.y += 1
        if self.hitting_wall():
            self.rect.y -= 1
            if self.holding:
                self.holding.rect.y -= 1
    
    def up(self):
        self.ymove_tick += self.speed
        while self.ymove_tick > 1.0:
            self.ymove_tick -= 1.0
            if self.hitting_wall(): continue
            self.rect.y -= 1
            if self.holding:
                self.holding.rect.y -= 1
        if self.hitting_wall():
            self.rect.y += 1
            if self.holding:
                self.holding.rect.y += 1
    
    def check_collisions(self):
        for obj in self.parent.objects:
            if self == obj: continue
            if self.rect.colliderect(obj):
                self.collide(obj)
    
    def drop_item(self):
        if self.holding:
            self.holding.holdable = 1
            self.holding = None
    
    def collide(self, obj):
        print 'hit with', obj
        if obj.__class__ == Trigger:
            if obj.dir == 'east':
                self.rect.left = 0
            elif obj.dir == 'west':
                self.rect.right = SCREEN_WIDTH
            elif obj.dir == 'north':
                self.rect.bottom = SCREEN_HEIGHT
            elif obj.dir == 'south':
                self.rect.top = 0
            self.move(obj.dest)
        
        elif issubclass(obj.__class__, Item):
            print'pickup!', obj, obj.holdable
            if obj.holdable:
                self.holding = obj
                if self.rect.x > obj.rect.x:
                    obj.rect.x -= 1
                else:
                    obj.rect.x += 1
                if self.rect.y > obj.rect.y:
                    obj.rect.y -= 1
                else:
                    obj.rect.y += 1

class Trigger(Thing):
    def __init__(self, game, **kargs):
        self.dest = kargs.get('dest', None)
        self.dir = kargs.get('dir', None)

        Thing.__init__(self, game, color=None, **kargs)

class Wall(Thing):
    def __init__(self, game, **kargs):
        Thing.__init__(self, game, color=WALL, **kargs)
    
    def update(self):
        pass

class Player(Thing):
    def __init__(self, game, **kargs):
        Thing.__init__(self, game, color=WALL, w=4, h=4, speed=1.2, **kargs)
    
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[K_RIGHT] and not keys[K_LEFT]:  self.right()
        if keys[K_LEFT]  and not keys[K_RIGHT]: self.left()
        if keys[K_UP]    and not keys[K_DOWN]:  self.up()
        if keys[K_DOWN]  and not keys[K_UP]:    self.down()
        
        if keys[K_SPACE] or keys[K_RETURN]:
            self.drop_item()
        
        if keys[K_a]:
            for o in self.parent.objects:
                print o, o.rect
            print
            print
        
        Thing.update(self)
    
    def collide(self, obj):
        if obj.__class__ == Wall:
            pass
        Thing.collide(self, obj)

class Dragon(Thing):
    def __init__(self, game, **kargs):
        Thing.__init__(self, game, w=6, h=10, speed=0.8, image=sprites.dragon,**kargs)
    
    def update(self):
        player = self.game.player

        if player in self.parent.objects:
            if self.rect.x < player.rect.x:
                self.right()
            elif self.rect.x > player.rect.x:
                self.left()
            if self.rect.y > player.rect.y:
                self.up()
            elif self.rect.y < player.rect.y:
                self.down()
        
        Thing.update(self)

class HappyDragon(Thing):
    def __init__(self, game, **kargs):
        Thing.__init__(self, game, w=7, h=7, speed=0.7, image=sprites.smile,**kargs)
        self.tick = random.randrange(50)
        self.dir = random.randrange(9)-1
    
    def update(self):
        if self.tick:
            self.tick -= 1
        else:
            self.tick = 50
            self.dir = random.randrange(9)-1
        
        # Directions smiley can go in:
        #     0
        #   7   1
        # 6  -1   2
        #   5   3
        #     4

        if self.dir in (1,2,3):
            self.right()
        if self.dir in (5,4,3):
            self.down()
        if self.dir in (7,6,5):
            self.left()
        if self.dir in (7,0,1):
            self.up()
        
        Thing.update(self)

class Jeremy(Thing):
    def __init__(self, game, **kargs):
        Thing.__init__(self, game, w=6, h=10, **kargs)

class Item(Thing):
    def __init__(self, game, **kargs):
        Thing.__init__(self, game, holdable=1, **kargs)

class LevelMarker(Item):
    def __init__(self, game, **kargs):
        self.level = kargs.get('level', 1)
        Thing.__init__(self, game, **kargs)
        self.holdable = 1

class LevelChanger(Thing):
    def __init__(self, game, **kargs):
        Thing.__init__(self, game, w=10, h=10, image=sprites.level_changer, **kargs)
        self.change_level(-1)
    
    def collide(self, obj):
        if obj.__class__ == LevelMarker:
            if obj.level != self.level:
                self.change_level(2)
        else:
            self.change_level(2)
    
    def change_level(self, level):
        self.level = level
        self.game.load_level(self.level)
    
    def get_level(self):
        found = None
        error = 0
        for obj in self.parent.objects:
            if obj.__class__ != LevelMarker: error =1

            if self.rect.collide_rect(obj.rect):
                if found:
                    error = 1
                else:
                    found = obj
        if error:
            return -1
        elif found:
            return found.level
        else:
            return -1
