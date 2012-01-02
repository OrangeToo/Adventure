
import pygame
from pygame.locals import *

pygame.init()

import os

import config
import objects
import sprites
import world
import util

from constants import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(config.WINDOW_SIZE)
        
        pygame.mouse.set_visible(False)

        self.window_size = config.WINDOW_SIZE

        self.fullscreen = 0
        if config.FULLSCREEN:
            self.fullscreen_toggle()
        
        self.blur = config.BLUR

        self.clock = pygame.time.Clock()
        self.fps = config.FPS
        
        self.title = world.TitleScreen(self)
        self.title.init()
        self.player = objects.Player(self, y=100)
        self.title.add(self.player)

        self.start()
    
    def start(self):
        end = 0
        while not end:
            for event in pygame.event.get():
                if event.type == QUIT: end = 1
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE: end = 1
                    elif event.key == K_F4: self.fullscreen_toggle()
                    elif event.key == K_F7: pass #Joystick toggle?
                    elif event.key == K_F8: self.blur = not self.blur
            
            #self.screen.fill(BLACK)
            
            self.player.parent.update()
            for obj in self.player.parent.objects:
                if obj.__class__ == objects.Trigger:
                    obj.dest.update()
            
            if self.blur:
                pygame.transform.smoothscale(self.player.parent.draw(), self.window_size, self.screen)
            else:
                pygame.transform.scale(self.player.parent.draw(), self.window_size, self.screen)
            
            pygame.display.flip()
            
            self.clock.tick(self.fps)
        
        pygame.quit()
    
    def reset(self):
        self.player = None
        self.screens = []
    
    def load_level(self, num):
        try:
            execfile( os.path.join('levels', 'level'+str(num)+'.py') )
        except:
            execfile( os.path.join('levels', 'error.py') )
    
    def fullscreen_toggle(self):
        if not self.fullscreen:
            pygame.display.set_mode(config.FULLSCREEN_WINDOW_SIZE, pygame.FULLSCREEN)
            self.window_size = config.FULLSCREEN_WINDOW_SIZE
        else:
            pygame.display.set_mode(config.WINDOW_SIZE)
            self.window_size = config.WINDOW_SIZE
        
        self.fullscreen = not self.fullscreen
