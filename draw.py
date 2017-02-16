from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0

    dx = x0 - x1
    dy = y1 - y0

    #deal with quadrant two and quadrant three
    if (x0 > x1):
        draw_line(x1, y1, x0, y0, screen, color)
        return 0
    
    #first quadrant
    if (dy > 0):
        #first octant
        if (-dx >= dy):
            d = (2 * dy) + dx
            dx *= 2
            dy *= 2

            while (x < x1):
                plot(screen, color, x, y)
                if (d > 0):
                    y += 1
                    d += dx
                x += 1
                d += dy
        #second octant
        else:
            d = dy + (2 * dx)
            dx *= 2
            dy *= 2

            while (y < y1):
                plot(screen, color, x, y)
                if (d < 0):
                    x += 1
                    d += dy
                y += 1
                d += dx
    #4th quadrant
    else:
        #eighth octant
        if (dx <= dy):
            d = (2 * dy) - dx
            dx *= 2
            dy *= 2

            while (x < x1):
                plot(screen, color, x, y)
                if (d < 0):
                    y -= 1
                    d -= dx
                x += 1
                d += dy
        #seventh octant
        else:
            d = dy - (2 * dx)
            dx *= 2
            dy *= 2

            while (y > y1):
                plot(screen, color, x, y)
                if (d > 0):
                    x += 1
                    d += dy
                y -= 1
                d -= dx
