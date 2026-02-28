#Python RPG GAME

import random #for random number generation

#player class
class Player:
    def __init__(self):
        self.health = 100
        self.maxHealth = 100
        self.x = 0
        self.y = 0
        self.damage = 10

#create the player
player = Player()

print("Use 'wasd' to move.")
print("Type q to quit.")

#enemy class
class Enemy:
    def __init__(self):
        self.health = random.randint(20,40) #give it random health
        self.damage = random.randint(5,12) #game it random damage amount

#item class
class Item:
    def __init__(self, name, healAmount):
        self.name = name
        self.healAmount = healAmount

#what happens when you move
def movementEvent(player):
    event = random.randint(1,3) #generate a random number for what even happens when you move

    #take damage from enemy
    if event == 1:
        print("You ran into an enemy!")
        enemy = Enemy() #make enemy class
        player.health -= enemy.damage #the enemy's random damage amount is taken from the player
        print("The enemy hit you for", enemy.damage)
    #heal player
    elif event == 2:
        print("You have found the item: healing potion!")
        item = Item("Potion", 20)

        player.health += item.healAmount
        
        #Check not over max health
        if player.health > player.maxHealth:
            player.health = player.maxHealth
        
        print("You healed for", item.healAmount)
    else:
        print("Nothing was found in this area. Keep moving!")
    
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
