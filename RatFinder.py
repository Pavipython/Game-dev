import pgzrun
import random
WIDTH=700
HEIGHT=650

rats=[]
list=1
start=[]
end=[]
def draw():
    screen.blit("checkboard.png", (0,0))
    num=1
    for rat in rats():
        rat.draw()
        num+=1
    for i in range(len(start)):
        screen.draw.line(start[i],end[i],"white")


for i in range(3):
    rat=Actor("rat.png")
    rat.pos(random.randint(60,600), random.randint(60, 600))
    rats.append(rat)

def on_mouse_down(pos):
    if list == 3:
        return
    cur=rats[list]
    prev=rats[list-1]
    if cur.collidepoint(pos):
        start.append(prev.pos)
        end.append(cur.pos)
        list+=1
    else:
        start.clear()
        end.clear()
        list=1

pgzrun.go()