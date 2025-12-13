import pgzrun
import random
WIDTH=600
HEIGHT=550

satellite = []
idx = 1
start=[]
end=[]
gameover=False
def draw():
    screen.blit("space.png",(0,0))
    if gameover == True:
        screen.draw.text("GAMEOVER",color="red",pos=(300,250))
        return
    num=1
    for sat in satellite:
        sat.draw()
        screen.draw.text(str(num),color="red", pos=(sat.x, sat.y+20))
        num+=1
    for i in range(len(start)):
        screen.draw.line(start[i],end[i],"white")

for i in range(8):   
    sat=Actor("satellite.png")
    sat.pos=(random.randint(50,550), random.randint(50,500))
    satellite.append(sat)

def on_mouse_down(pos):
    global idx, gameover
    if idx == 8:
        gameover=True
        return
    curr=satellite[idx]
    prev=satellite[idx-1]
    if curr.collidepoint(pos):
        start.append(prev.pos)
        end.append(curr.pos)
        idx+=1
    else:
        start.clear()
        end.clear()
        idx=1



pgzrun.go()