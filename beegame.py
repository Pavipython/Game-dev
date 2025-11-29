import pgzrun
import random

WIDTH=500
HEIGHT=500

def draw():
    screen.blit("background.png",(0,0))
    bee.draw()
    flower.draw()

bee=Actor("bee.png")
bee.pos=(250,250)

flower=Actor("flower.png")
flower.pos=(random.randint(0,500), random.randint(0,500))

def update():
    if keyboard.a:
        bee.x-=3
    if keyboard.d:
        bee.x+=3
    if keyboard.w:
        bee.y-=3
    if keyboard.s:
        bee.y+=3

    if flower.colliderect(bee):
        flower.pos=(random.randint(0,500), random.randint(0,500))
        



















pgzrun.go()