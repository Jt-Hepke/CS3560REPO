#Python RPG GAME

#player class
class Player:
    def __init__(self):
        self.health = 100
        self.maxHealth = 100
        self.x = 0
        self.y = 0

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
        player.y += 1 # adjust position
    elif move == "s":
        print("Moved down")
        player.y -= 1
    elif move == "a":
        print("Moved left")
        player.x -= 1
    elif move == "d":
        print("Moved right")
        player.x += 1
    else:
        print("INVALID")
    print("Current place: ", player.x, player.y)
