import pgzrun
import random
WIDTH=800
HEIGHT=500

items=["bagimg","batteryimg","bottleimg","cheeze","chipsimg"]
level=1
selected_items=[]

def setup():
    for i in range(level+1):
        random_item=random.choice(items)
        actor_item=Actor(random_item)
        selected_items.append(actor_item)
        actor_item.pos=random.randint(50,700), 50
    
    for item in selected_items:
        animate(item, y = HEIGHT , duration=10)




setup()

def draw():
    screen.blit("new_bg.jpg", (0,0))
    for item in selected_items:
        item.draw()

def update():
    pass

pgzrun.go()