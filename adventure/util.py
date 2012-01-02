
from objects import *
from constants import *

BORDER_WIDTH = 15
SAFTEY = 0
def wall_border(game, screen, top = 1, bottom = 0, left = 0, right = 0):
    
    if top == 1:
    	screen.add( Wall(game, x=0,
                               y=0,
                               w=SCREEN_WIDTH/4,
                               h=BORDER_WIDTH) )
        
        screen.add( Wall(game, x=SCREEN_WIDTH-(SCREEN_WIDTH/4),
                               y=0,
                               w=SCREEN_WIDTH/4,
                               h=BORDER_WIDTH) )
    elif top == 2:
        screen.add( Wall(game, x=0,
                               y=0,
                               w=SCREEN_WIDTH,
                               h=BORDER_WIDTH) )
    
    if bottom == 1:
        screen.add( Wall(game, x=0,
                               y=SCREEN_HEIGHT-BORDER_WIDTH,
                               w=SCREEN_WIDTH/4,
                               h=BORDER_WIDTH) )
        
        screen.add( Wall(game, x=SCREEN_WIDTH-(SCREEN_WIDTH/4),
                               y=SCREEN_HEIGHT-BORDER_WIDTH,
                               w=SCREEN_WIDTH/4,
                               h=BORDER_WIDTH) )
    
    elif bottom == 2:
        screen.add( Wall(game, x=0,
                               y=SCREEN_HEIGHT-BORDER_WIDTH,
                               w=SCREEN_WIDTH,
                               h=BORDER_WIDTH) )
    
    if left == 1:
        screen.add( Wall(game, x=0,
                               y=0,
                               w=BORDER_WIDTH,
                               h=SCREEN_HEIGHT/4) )
        
        screen.add( Wall(game, x=0,
                               y=SCREEN_HEIGHT-(SCREEN_HEIGHT/4),
                               w=BORDER_WIDTH,
                               h=SCREEN_HEIGHT/4) )
    elif left == 2:
        screen.add( Wall(game, x=0,
                               y=0,
                               w=BORDER_WIDTH,
                               h=SCREEN_HEIGHT) )
    
    if right == 1:
        screen.add( Wall(game, x=SCREEN_WIDTH-BORDER_WIDTH,
                               y=0,
                               w=BORDER_WIDTH,
                               h=SCREEN_HEIGHT/4) )
        
        screen.add( Wall(game, x=SCREEN_WIDTH-BORDER_WIDTH,
                               y=SCREEN_HEIGHT-(SCREEN_HEIGHT/4),
                               w=BORDER_WIDTH,
                               h=SCREEN_HEIGHT/4) )
    elif right == 2:
        screen.add( Wall(game, x=SCREEN_WIDTH-BORDER_WIDTH,
                               y=0,
                               w=BORDER_WIDTH,
                               h=SCREEN_HEIGHT) )

def draw_text(screen, text):
    pass
