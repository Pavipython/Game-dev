import pgzrun
import random

WIDTH=500
HEIGHT=500

def draw():
    screen.blit("checkboard.png",(0,0))
    rat.draw()
    cheeze.draw()

rat=Actor("rat.png")
rat.pos=(250,250)

cheeze=Actor("cheeze.png")
cheeze.pos=(random.randint(0,500), random.randint(0,500))

def update():
    if keyboard.right:
        rat.x-=4
    if keyboard.left:
        rat.x+=4
    if keyboard.up:
        rat.y-=4
    if keyboard.down:
        rat.y+=4

pgzrun.go()