#Python RPG GAME

#player class
class Player:
    def __init__(self):
        self.health = 100
        self.maxHealth = 100

#create the player
player = Player()

print("Use 'wasd' to move.")
print("Type q to quit.")

#start game loop
while True:
    move = input("Enter move: ") #get input from user
    if move == "q":
        print("GAME QUIT")
        break #end game loop
    elif move == "w":
        print("Moved up")
    elif move == "s":
        print("Moved down")
    elif move == "a":
        print("Moved left")
    elif move == "d":
        print("Moved right")
    else:
        print("INVALID")
    
    

