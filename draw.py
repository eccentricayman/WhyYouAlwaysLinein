from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    
    dx = x1 - x0
    dy = y1 - y0
    #d = dy + (x1 - x0)

    if x0 > x1:
        draw_line(x1, y1, x0, y0, screen, color)

    #quadrant 1
    if (dy >= 0):
        #octant 1
        if (-dx >= dy):
            dx *= 2
            dy *= 2
            d = (2 * dy) + dx
            while x < x1:
                plot(screen, color, x, y)
                if (d > 0):
                    y -= 1
                    d += dx
                x += 1
                d -= dy
        else:
            #octant 2
            dx *= 2
            dy *= 2
            d = dy + (2 * dx)
            while y < y1:
                plot(screen, color, x, y)
                if (d < 0):
                    x += 1
                    d += dy
                y += 1
                d += dx
    else:
        #quadrant 4
        if dx <= dy:
            #octant 8
            dx *= 2
            dy *= 2
            d = (2 * dy) - dx
            while x < x1:
                plot(screen, color, x, y)
                if (d < 0):
                    y -= 1
                    d -= dx
                x += 1
                d += dy
        else:
            #octant 7
            dx *= 2
            dy *= 2
            d = dy - (2 * dx)
            while y > y1:
                plot(screen, color, x, y)
                if (d > 0):
                    x += 1
                    d += dy
                y -= 1
                d -= dx
            
                
