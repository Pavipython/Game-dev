import pgzrun
import random, pyautogui
print(pyautogui.size())
WIDTH, HEIGHT=pyautogui.size()

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

def draw():
    #print("draw")
    screen.blit("new_bg.jpg", (0,0))
    for item in selected_items:
        item.draw()

def update():
    global selected_items
    #print("appeal")
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
    gap=level+1# len(sprites)+1
    gap_size=WIDTH/gap
    random.shuffle(sprites)
    for i,v in enumerate(sprites):
        v.x=(i+1)*gap_size

def animation(sprites):
    global animations
    for i in sprites:
        duration=10-level
        animations.append(animate(i,duration=duration,on_finished=gameover, y=HEIGHT))

def gameover():
    pass
#   print("gameover")


pgzrun.go()