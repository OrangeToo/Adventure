
import pygame
from pygame import *

from constants import *
import objects
import sprites
import util

class Screen:
    def __init__(self, game, **kargs):
        self.game = game
        self.screen = pygame.surface.Surface(SCREEN_SIZE)
        
        self.objects = []
        self.bgcolor = kargs.get('bgcolor', LGRAY)
        self.wall_color = kargs.get('wall_color', YELLOW)
        
        self.dark = kargs.get('dark', False)

    def update(self):
        for obj1 in self.objects:
            obj1.update()
    
    def draw(self):
        self.screen.fill(self.bgcolor)

        for obj in self.objects:
            obj.draw(self.screen)
        
        return self.screen
    
    def add(self, obj):
        self.objects.append(obj)
        obj.parent = self
    
    def remove(self, obj):
        self.objects.remove(obj)
        obj.parent = None
    
    # For one and multi-exits.
    #   example:   a -> b
    def add_north(self, screen):
        self.add( objects.Trigger(self.game, x=0, y=-10, h=10, w=SCREEN_WIDTH, dest=screen, dir='north') )
    
    def add_south(self, screen):
        self.add( objects.Trigger(self.game, x=0, y=SCREEN_HEIGHT, h=10, w=SCREEN_WIDTH, dest=screen, dir='south') )
    
    def add_east(self, screen):
        self.add( objects.Trigger(self.game, x=SCREEN_WIDTH, y=0, h=SCREEN_HEIGHT, w=10, dest=screen, dir='east') )
    
    def add_west(self, screen):
        self.add( objects.Trigger(self.game, x=-10, y=0, h=SCREEN_HEIGHT, w=10, dest=screen, dir='west') )
    
    # For two way linking:
    #   example   a <-> b
    def link_north(self, screen):
        self.add_north(screen)
        screen.add_south(self)
    
    def link_south(self, screen):
        self.add_south(screen)
        screen.add_north(self)
    
    def link_east(self, screen):
        self.add_east(screen)
        screen.add_west(self)
    
    def link_west(self, screen):
        self.add_west(screen)
        screen.add_east(self)

class TitleScreen(Screen):
    def __init__(self, game):
        Screen.__init__(self, game, wall_color=PURPLE)
        util.wall_border(game, self, top = 2, bottom = 1, left = 2, right = 2)

        self.add( objects.Thing(game, image=sprites.title, x=SCREEN_WIDTH/2, y=30) )
    
    def init(self):
        self.add( objects.LevelMarker(self.game, level=1, image=sprites.level1, x=50, y=89) )
        self.add( objects.LevelMarker(self.game, level=2, image=sprites.level2, x=202, y=40) )
        self.add( objects.LevelMarker(self.game, level=3, image=sprites.level3, x=180, y=66) )

        self.add( objects.LevelChanger(self.game) )
    
    def draw(self):
        return Screen.draw(self)