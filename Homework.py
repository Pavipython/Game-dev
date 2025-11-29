import pgzrun

WIDTH=500
HEIGHT=500

player=Actor("football.png")
player.pos = (100,100)

def draw():
    screen.fill("grey")
    player.draw()

pgzrun.go()