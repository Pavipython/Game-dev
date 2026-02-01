import pgzrun
import random, pyautogui
print(pyautogui.size())
WIDTH, HEIGHT=pyautogui.size()
HEIGHT-=100
items=["flower", "bee", "rat", "bagimg","cheeze"]
level=1
selected_items=[]
print("global")

# def setup():
#     print("setup")
#     for i in range(level+1):
#         random_item=random.choice(items)
#         actor_item=Actor(random_item)
#         selected_items.append(actor_item)
#         actor_item.pos=random.randint(50,700), 50
    
#     # for item in selected_items:
#     #     animate(item, y = HEIGHT , duration=10)



bin=Actor("recycling-bin.png")
bin.pos=(WIDTH//2,HEIGHT-100)
# setup()
animations=[]
gamecomplete=False
gameover=False

def draw():
    #print("draw")
    screen.blit("new_bg.jpg", (0,0))
    bin.draw()
    for item in selected_items:
        item.draw()
    if gameover:
        screen.draw.text("gameover",(400,400))
    elif gamecomplete:
        screen.draw.text("congratulation",(400,400))


def update():
    global selected_items
    if keyboard.a:
        bin.x-=3
    if keyboard.d:
        bin.x+=3
    #print("appeal")
    if len(selected_items) == 0:
        selected_items=make_list(level)

    move_bin()

def make_list(level):
    objects=options(level)
    sprites=sprite(objects)
    givingpos(sprites)
    animation(sprites)
    return sprites

def options(level):
    objects=["bagimg"]
    for i in range(level):
        objects.append(random.choice(items))
    return objects

def sprite(objects):
    sprites=[]
    for i in objects:
        sprites.append(Actor(i))
    return sprites

def givingpos(sprites):
    gap=len(sprites)+1
    gap_size=WIDTH/gap
    random.shuffle(sprites)
    for i,v in enumerate(sprites):
        v.x=(i+1)*gap_size

def animation(sprites):
    global animations
    for i in sprites:
        duration=10-level
        i.anchor=("center", "bottom")
        animations.append(animate(i,duration=duration,on_finished=gamend, y=HEIGHT))

def gamend():
    global gameover
    gameover=True
    stopanimation(animations)
    print("gameover")
def stopanimation(animations):
    for i in animations:
        if i.running:
            i.stop()

def move_bin():
    global animations, selected_items, gamecomplete, level
    for i in selected_items:
        if bin.colliderect(i):
            if "bagimg" in i.image:
                if level == 6:
                    gamecomplete=True
                    stopanimation(animations)
                else:
                    level+=1
                    selected_items=[]
                    animations=[]
            else:
                print(i)
                gamend()



pgzrun.go()