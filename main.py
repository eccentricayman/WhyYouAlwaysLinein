from display import *
from draw import *

screen = new_screen()
color = [ 255, 255, 255 ]


draw_line(250, 250, 300, 200, screen, color)
display(screen)
save_extension(screen, 'img.png')
