import pgzrun
import random, pyautogui
print(pyautogui.size())
WIDTH, HEIGHT=pyautogui.size()

items=["bagimg","batteryimg","bottleimg","cheeze","chipsimg"]
level=1
selected_items=[]
print("global")

def setup():
    print("setup")
    for i in range(level+1):
        random_item=random.choice(items)
        actor_item=Actor(random_item)
        selected_items.append(actor_item)
        actor_item.pos=random.randint(50,700), 50
    
    # for item in selected_items:
    #     animate(item, y = HEIGHT , duration=10)




setup()

def draw():
    #print("draw")
    screen.blit("new_bg.jpg", (0,0))
    for item in selected_items:
        item.draw()

def update():
    #print("appeal")
    pass

pgzrun.go()