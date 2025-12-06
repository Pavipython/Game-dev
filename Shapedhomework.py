import pgzrun

WIDTH=500
HEIGHT=500

def draw():
    screen.fill("blue")
    screen.draw.filled_circle(color=(216, 90, 213), radius=50, pos=(90,90))
    screen.draw.filled_circle(color=(255,0,0), radius=30, pos=(90,90))
    screen.draw.line((140,0,), (30,405), color=(100,77,0))
    screen.draw.line((170,40,), (100,500), color=(0,255,0))


pgzrun.go()