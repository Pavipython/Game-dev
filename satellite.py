import pgzrun
import random
WIDTH=600
HEIGHT=550

satellite = []


def draw():
    screen.blit("space.png",(0,0))
    num=1
    for sat in satellite:
        sat.draw()
        screen.draw.text(str(num),color="red", pos=(sat.x, sat.y+20))
        num+=1


for i in range(8):   
    sat=Actor("satellite.png")
    sat.pos=(random.randint(50,550), random.randint(50,500))
    satellite.append(sat)


pgzrun.go()