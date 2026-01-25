import pgzrun, random
WIDTH, HEIGHT=550, 600

stars=[]
index = 1
start=[]
end=[]
gameover=False

def draw():
    screen.blit("space.png", (0,0))

    if gameover == True:
        screen.draw.text("GAMEOVER",color="red",pos=(280,260))
        return
    num=1
    for star1 in stars:
        star1.draw()
        screen.draw.text(str(num),color="red", pos=(star1.x, star1.y+20))
    for star2 in stars:
        star2.draw()
        screen.draw.text(str(num),color="red", pos=(star2.x, star2.y+20))
    for star3 in stars:
        star3.draw()
        screen.draw.text(str(num),color="red", pos=(star3.x, star3.y+20))
        num+=1
    for i in range(len(start)):
        screen.draw.line(start[i],end[i],"white")
    for l in range(len(start)):
        screen.draw.line(start[l],end[l],"green")
    for o in range(len(start)):
        screen.draw.line(start[o],end[o],"cyan")

for i in range(3):
    star1=Actor("purple-star.png")
    star1.pos=(random.randint(40,560), random.randint(40,560))
    stars.append(star1)

for l in range(3):
    star2=Actor("orange-star.png")
    star2.pos=(random.randint(40,560), random.randint(40,560))
    stars.append(star2)

for o in range(3):
    star3=Actor("red-star.png")
    star3.pos=(random.randint(40,560), random.randint(40,560))
    stars.append(star3)

def on_mouse_down(pos):
    global index, gameover
    if index == 8:
        gameover=True
        return
    cur=stars[index]
    prev=stars[index-1]
    if cur.collidepoint(pos):
        start.append(prev.pos)
        end.append(cur.pos)
        index+=1
    else:
        start.clear()
        end.clear()
        index=1


pgzrun.go()
