import random
from display import *
from draw import *

screen = new_screen()
color = [ 255, 255, 255 ]

#all the randoms
#draws 204 lines because i finished this at 2:04
for i in range(204):
    draw_line(random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), screen, [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255) ])

display(screen)
save_extension(screen, 'img.png')
