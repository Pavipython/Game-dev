import pgzrun,random,pyautogui

print(pyautogui.size())
WIDTH,HEIGHT=pyautogui.size()
TITLE="endless_shooter_game"

enemies=[]
powers=[]
score=0
lives=3

character=Actor("new-character1.png")
character.pos=(100,HEIGHT/2)



def create_enemies():
    enemy=Actor("enemy.png")
    enemy.pos=(WIDTH,random.randint(0,HEIGHT-50))
    enemies.append(enemy)


def draw():
    screen.blit("background.png", (0,0))
    character.draw()
    for i in enemies:
        i.draw()
    for i in powers:
        i.draw()
    screen.draw.text(f"SCORE={score}",(50,50))
    screen.draw.text(f"LIVES={lives}",(50,100))

    

def update():
    global score, lives
    if keyboard.up:
        character.y-=10
    if keyboard.down:
        character.y+=10
    if character.y < 0:
        character.y=HEIGHT
    if character.y > HEIGHT:
        character.y=0
    
    if keyboard.space:
        projectile=Actor("projectile2.png")
        projectile.pos=character.x+60,character.y-60
        powers.append(projectile)
    
    for i in powers:
        i.x+=4
        if i.x > WIDTH:
            powers.remove(i)
        for e in enemies:
            if e.colliderect(i):
                enemies.remove(e)
                powers.remove(i)
                score+=1

    for i in enemies:
        i.x-=4
        if i.x < 0:
            enemies.remove(i)
        if character.colliderect(i):
            enemies.remove(i)
            if lives > 0:
                lives-=1
            
    
clock.schedule_interval(create_enemies,2)


pgzrun.go()