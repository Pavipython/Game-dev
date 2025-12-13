import pgzrun
import random

WIDTH=500
HEIGHT=500

Emojis=[]

def draw():
    screen.blit("background.png",(0,0))
    num=1
    for Emoji in Emojis:
        Emoji.draw()
        num+=1


for i in range(10):
    Emoji=Actor("emoji.png")
    Emoji.pos=(random.randint(50,400),random.randint(50,400))
    Emojis.append(Emoji)

pgzrun.go()