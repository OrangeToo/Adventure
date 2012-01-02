
e = world.Screen(self, wall_color=BLACK)
util.wall_border(self, e, top=1, bottom=2, left=2, right=2)
e.add( objects.Thing(self, image=sprites.error, x=SCREEN_WIDTH/2 - sprites.error.get_width()/2, y=100) )

e.link_north(self.title)