#!/usr/env python3

from gamesetting import rooms
from os import system, name
import time
import pygame


def showInstructions():
    clear()
    # read welcome message from txt file
    welcome = open("welcome.txt", "r")
    print(welcome.read())
    welcome.close()

    # print a main menu, the commands, and some general info about the game
    print('''
    WELCOME TO THE MAZE OF ROTHGAR!!!
    ENTER AND EXPERIENCE YOUR WILDEST DREAMS!!!! OR... BECOME A VICTIM TO YOUR DARKEST NIGHTMARE!!! 
    ========
    Commands:
      go [direction]
      get [item]
      quit [allows you to exit the game at any time]
    ''')

    # Plays the background game music
    pygame.init()
    pygame.mixer.music.load('LostWoods.wav')
    pygame.mixer.music.play()

    # displays a timer before the game begins
    # range returns a sequence of numbers, increments by 1(by default), and stops before a specified number
    # range(start, stop, step) step specifies the incrementation. So increment -1 starting from 10 ex(10,9,8, etc.. until it reaches 1).
    for i in range(10, 0, -1):
        print(f"  The game will start in {i} seconds ", end="\r", flush=True)
        time.sleep(1)
    clear()


# shows player their current status i.e. (current room, inventory, and item)
def showStatus():

    if currentRoom == 'Dining Room':
        kitchen = open("diningRoom.txt", 'r')
        print(kitchen.read())
        kitchen.close()
    elif currentRoom == 'Hall':
        hall = open("hallway.txt", 'r')
        print(hall.read())
        hall.close()
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


# inventory an empty list and will update when player gets an item
inventory = []

# start the player in the Hall (see gameSetting.py)
currentRoom = 'Hall'
# starts the game
showInstructions()
# loop forever
while True:
    showStatus()
    # os.system("LostWoods.mp3")

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')
        clear()

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(f"A {move[1]} has been added to your inventory!")
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    if move[0] == 'quit':
        gameover = open("gameover.txt", "r")
        print(gameover.read())
        gameover.close()
        print('\n\nScary little human couldnt handle the maze of Rothgar? Your name will forever be remembered as Gooshcar the Frieghtened\n\n')
        break

    # If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        gameover = open("gameover.txt", "r")
        print(gameover.read())
        gameover.close()
        print('\n\nA monster has got you... GAME OVER! SEE? I TOLD YOU! FOOLISH MORTAL! YOU EXPEREINCED YOUR DARKEST NIGHTMARE!\n\n')
        # time.sleep(3)
        # pygame.mixer.music.unload()
        # pygame.mixer.music.load('Gotcha.wav')
        # pygame.mixer.music.play()
        break

    # player wins if they're in the garden and have key&potion in their inventory
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        winner = open("winner.txt", "r")
        print(winner.read())
        winner.close()
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN! SEE? I TOLD YOU! YOU EXPERINCED YOUR WILDEST OF DREAMS!')
        break
