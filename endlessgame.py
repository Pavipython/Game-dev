import pgzrun,random,pyautogui

print(pyautogui.size())
WIDTH,HEIGHT=pyautogui.size()
TITLE="endless_shooter_game"

enemies=[]

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

    
def update():
    if keyboard.up:
        character.y-=10
    if keyboard.down:
        character.y+=10
    if character.y < 0:
        character.y=HEIGHT
    if character.y > HEIGHT:
        character.y=0
    
    for i in enemies:
        i.x-=4
        if i.x < 0:
            enemies.remove(i)
        if character.colliderect(i):
            enemies.remove(i)
    
clock.schedule_interval(create_enemies,1.5)

pgzrun.go()