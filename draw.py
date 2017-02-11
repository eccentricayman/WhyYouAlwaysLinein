from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    
    dx = 2 * (x1 - x0)
    dy = 2 * (y1 - y0)
    d = dy + (x1 - x0)

    while x < x1:
        plot(screen, color, x, y)
        if (d > 0):
            y += 1
            d += dx
        x += 1
        d += dy
