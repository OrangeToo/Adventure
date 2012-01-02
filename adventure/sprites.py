
import pygame
from pygame.locals import *

from constants import *

def size(text):
    xsize, ysize = 0, 0
    for y, line in enumerate(text.split('\n')):
        for x, char in enumerate(line):
            if xsize < x:
                xsize = x
        if ysize < y:
            ysize = y
    
    return xsize + 1, ysize + 1

def text2image(text, color):
    temp = pygame.surface.Surface(size(text))
    temp.fill((0,0,0))

    for y, line in enumerate(text.split('\n')):
        for x, char in enumerate(line):
            if char != ' ':
                temp.set_at((x, y), color)
    
    temp.set_colorkey((0,0,0))
    
    return temp

key = text2image(
"""
###
# #####
### # # 
"""[1:-1],
YELLOW)

smile = text2image(
"""
 ##### 
#######
## # ##
#######
# ### #
#     #
 ##### 
"""[1:-1],
YELLOW)

dragon = text2image(
"""
     ##
    ####
####  ##
#######
    ###
     #
     #
   ####
  ######
 ##   ##
##    ##
##    ##
##    ##
##   ###
########
  ####
    #
    ####
#      #
###    #
  ######
"""[1:-1],
YELLOW)

title = text2image(
"""
   ###    ########  ##     ## ######## ##    ## ######## ##     ## ########  ########
  ## ##   ##     ## ##     ## ##       ###   ##    ##    ##     ## ##     ## ##     
 ##   ##  ##     ## ##     ## ##       ####  ##    ##    ##     ## ##     ## ##     
##     ## ##     ## ##     ## ######   ## ## ##    ##    ##     ## ########  ###### 
######### ##     ##  ##   ##  ##       ##  ####    ##    ##     ## ##   ##   ##     
##     ## ##     ##   ## ##   ##       ##   ###    ##    ##     ## ##    ##  ##     
##     ## ########     ###    ######## ##    ##    ##     #######  ##     ## ########
"""[1:-1],
PURPLE)

error = text2image(
"""
######## ########  ########   #######  ########  
##       ##     ## ##     ## ##     ## ##     ## 
##       ##     ## ##     ## ##     ## ##     ## 
######   ########  ########  ##     ## ########  
##       ##   ##   ##   ##   ##     ## ##   ##   
##       ##    ##  ##    ##  ##     ## ##    ##  
######## ##     ## ##     ##  #######  ##     ## 
"""[1:-1],
BLACK)

level1 = text2image("""
  #
###
  #
  #
#####
"""[1:-1],
BLACK)

level2 = text2image("""
 ###
#   #
 ###
#
#####
"""[1:-1],
BLACK)

level3 = text2image("""
 ###
#   #
  ##
#   #
 ###
"""[1:-1],
BLACK)

level_changer = text2image("""
## ## ## ## ## #
               #
# 
#              #
               #
#
#              #
               #
#
#              #
               #
#
# ## ## ## ## ##
"""[1:-1],
BLACK)