#!/usr/env python3

from gamesetting import rooms
from os import system,name
import time

def showInstructions():
    f = open("welcome.txt", "r")
    print(f.read())
    f.close()

    #print a main menu, the commands, and some general info about the game
    print('''
    WELCOME TO THE MAZE OF ROTHGAR!!!
    ENTER AND EXPERIENCE YOUR WILDEST DREAMS!!!! OR... BECOME A VICTIM TO YOUR DARKEST NIGHTMARE!!! 
    ========
    Commands:
      go [direction]
      get [item]
      quit [allows you to exit the game at any time]
    ''')

    #displays the timer before the game begins
    for i in range(10,0,-1):
        print(f"The game will start in {i} seconds ", end="\r", flush=True)
        time.sleep(1)
    
    clear()
#shows player their current status i.e. (current room, inventory, and item)
def showStatus():
    """determine the current status of the player"""
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print('Inventory : ' + str(inventory))
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

def clear():
    
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


#an inventory, which is initially empty
inventory = []

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:
    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':  
        move = input('>')
        clear()

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(f"A {move[1]} has been added to your inventory!")
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    if move[0] == 'quit':
        gameover = open("gameover.txt", "r")
        print(gameover.read())
        gameover.close()
        print('\n\nScary little human couldnt handle the maze of Rothgar? Your name will forever be remembered as Gooshcar the Frieghtened\n\n')
        break

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        gameover = open("gameover.txt", "r")
        print(gameover.read())
        gameover.close()
        print('\n\nA monster has got you... GAME OVER! SEE? I TOLD YOU! FOOLISH MORTAL! YOU EXPEREINCED YOUR DARKEST NIGHTMARE!\n\n')
        break

    #player wins if theyr ein the garden and have key&potion in their inventory
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        winner = open("winner.txt", "r")
        print(winner.read())
        winner.close()
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN! SEE? I TOLD YOU! YOU EXPERINCED YOUR WILDEST OF DREAMS!')
        break