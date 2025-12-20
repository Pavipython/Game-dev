import pgzrun

WIDTH=600
HEIGHT=550


def draw():
    screen.blit("checkboard.png", (0,0))
    flower.draw()

flower=Actor("flower.png")

def on_mouse_down(pos):
    if flower.collidepoint(pos):
        print(flower)
    


    


pgzrun.go()