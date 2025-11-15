import pgzrun
import random

WIDTH=500
HEIGHT=500

reg=Actor("alien.png")
reg.pos = (random.randint(0,500),random.randint(0,500))
message = ""

def draw():
    screen.fill("light cyan")
    screen.draw.text(message, color="black", center=(400,10))
    reg.draw()

def on_mouse_down(pos):
    global message

    if reg.collidepoint(pos):
        reg.pos = (random.randint(0,500),random.randint(0,500))
        message=("collided")
    else:
        message=("missed")
    


pgzrun.go()

