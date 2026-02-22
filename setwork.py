import random

stationary={"scissors","pencil","eraser","highlighter","board_marker","ruler"}

while stationary:
    tool=random.choice(list(stationary))
    #print(tool)
    guess = input("Guess one stationary ").lower()

    if guess == tool:
        print("correct")
        stationary.remove(tool)
    else:
        print("wrong stationary!")
        break 
    
