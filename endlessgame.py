import pgzrun,random,pyautogui

print(pyautogui.size())
WIDTH,HEIGHT=pyautogui.size()
TITLE="endless_shooter_game"

enemies=[]
powers=[]
score=0
lives=3
gamestate="start"

character=Actor("new-character1.png")
character.pos=(100,HEIGHT/2)



def create_enemies():
    if gamestate == "play":
        enemy=Actor("enemy.png")
        enemy.pos=(WIDTH,random.randint(0,HEIGHT-50))
        enemies.append(enemy)


def draw():
    screen.blit("background.png", (0,0))
    character.draw()
    if gamestate == "start":
        screen.draw.text("Press space to start the game \n Press up and down keys to control character \n Press space to shoot \n You have three lives \n shoot the zombies to score",center=(WIDTH//2,HEIGHT//2))
    elif gamestate == "play":    
        for i in enemies:
            i.draw()
        for i in powers:
            i.draw()
        screen.draw.text(f"SCORE={score}",(50,50))
        screen.draw.text(f"LIVES={lives}",(50,100))
    else:
        screen.draw.text("Gameover",center = (WIDTH//2,HEIGHT//2), fontsize=40 )

    

def update():
    global score, lives, gamestate
    if keyboard.space and gamestate !="play":
        gamestate="play"
        score=0
        lives=3
    if gamestate == "play":

        if keyboard.up:
            character.y-=10
        if keyboard.down:
            character.y+=10
        if character.y < 0:
            character.y=HEIGHT
        if character.y > HEIGHT:
            character.y=0
            
        
        
        for i in powers:
            i.x+=4
            if i.x > WIDTH:
                powers.remove(i)
            for e in enemies:
                if e.colliderect(i):
                    enemies.remove(e)
                    powers.remove(i)
                    score+=1
                    break

        for i in enemies:
            i.x-=4
            if i.x < 0:
                enemies.remove(i)
            if character.colliderect(i):
                enemies.remove(i)
                if lives > 0:
                    lives-=1
                if lives==0:
                    gamestate="end"
    
clock.schedule_interval(create_enemies,2)

def on_key_down(key):
    if gamestate == "play" and key == keys.SPACE:
            projectile=Actor("projectile2.png")
            projectile.pos=character.x+60,character.y-60
            powers.append(projectile)


pgzrun.go()