# What's in your namespace:
#
#  self
#    a reference to the main game object.
#
#  objects, world, util, config, sprites
#    modules with the obejcts, screens, utilities, configuration, and sprites
#
#  all of constants.py
#    stuff like colors (ex YELLOW, LGRAY) and screen sizes
#
# What else?
#  o game.title is your starting screen.  link to it so the player can move into
#    your level.
#  o make sure your triggers have a 'dir' attribute!
#  o use util.wall_border to make some easy walls.  0=no wall, 1=small opening, 2=full wall
#

a = world.Screen(self, bgcolor=LGRAY)
util.wall_border(self, a, top=1, bottom=0, left=2, right=2)
a.add(objects. Wall(self, x=40, y=115, w=240-80, h=20) )

for i in range(5): a.add( objects.HappyDragon(self, x=100) )

b = world.Screen(self, bgcolor=LGRAY)
util.wall_border(self, b, top=0, bottom=2, left=2, right=0)
b.add( objects.Wall(self, x=40, y=0, w=240-40, h=20) )

c = world.Screen(self, bgcolor=LGRAY, wall_color=GREEN)
util.wall_border(self, c, top=2, bottom=2, left=0, right=0)

d = world.Screen(self, bgcolor=LGRAY)
util.wall_border(self, d, top=0, bottom=2, left=0, right=2)
d.add( objects.Wall(self, x=0, y=0, w=240-40, h=20) )

self.title.link_south(a)

a.add( objects.Trigger(self, dest=b, dir='south', x=0, y=SCREEN_HEIGHT, h=20, w=SCREEN_WIDTH/2) )
a.add( objects.Trigger(self, dest=d, dir='south', x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT, h=20, w=SCREEN_WIDTH/2) )

b.add_north(a)
d.add_north(a)

c.link_east(d)
c.link_west(b)
