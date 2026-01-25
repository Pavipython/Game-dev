import pgzrun
import random, pyautogui
print(pyautogui.size())
WIDTH, HEIGHT=pyautogui.size()
HEIGHT-=100
items=["bagimg","batteryimg","bottleimg","cheeze","chipsimg"]
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




# setup()
animations=[]
gamecomplete=False
gameover=False

def draw():
    #print("draw")
    screen.blit("new_bg.jpg", (0,0))
    for item in selected_items:
        item.draw()
    if gameover:
        screen.draw.text("gameover",(400,400))
    elif gamecomplete:
        screen.draw.text("congratulation",(400,400))

def update():
    global selected_items
    #print("appeal")
    if len(selected_items) == 0:
        selected_items=make_list(level)

def make_list(level):
    objects=options(level)
    sprites=sprite(objects)
    givingpos(sprites)
    animation(sprites)
    return sprites

def options(level):
    objects=["paperimg"]
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

def on_mouse_down(pos):
    global animations, selected_items, gamecomplete, level
    for i in selected_items:
        if i.collidepoint(pos):
            if "paper" in i.image:
                if level == 6:
                    gamecomplete=True
                    stopanimation(animations)
                else:
                    level+=1
                    selected_items=[]
                    animations=[]
            else:
                gamend()



pgzrun.go()