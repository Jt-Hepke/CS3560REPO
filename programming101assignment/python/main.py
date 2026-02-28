#Python RPG GAME

import random #for random number generation

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

#what happens when you move
def movementEvent(player):
    event = random.randint(1,3) #generate a random number for what even happens when you move

    #take damage from enemy
    if event == 1:
        damage = random.randint(5,15) #generate a random number of damage the enemy did
        player.health -= damage
        print("An enemy damaged you!")
        print("You lost", damage, "health")
    #heal player
    elif event == 2:
        heal = random.randint(5,15) #random number of health gained
        player.health += heal
        
        #Check not over max health
        if player.health > player.maxHealth:
            player.health = player.maxHealth
        
        print("You got a healing potion!")
        print("You got ",heal, "health.")
    else:
        print("Nothing happened, keep moving....")
    print("Current Player Health: ", player.health)

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
        break
    #print("Current place: ", player.x, player.y)
    movementEvent(player) #call to random event class

    #end loop if player dies
    if player.health <= 0:
        print("You have died.")
        break
